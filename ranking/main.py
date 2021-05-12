# -*- coding: utf-8 -*-

def load_lines(path, used_encoding="utf8"):
	
	lines=[];
	if (used_encoding is None):
		with open(path, "r") as f:
			lines=[l.strip("\r\n") for l in f.readlines()];
	else:
		with open(path, "r", encoding=used_encoding) as f:
			lines=[l.strip("\r\n") for l in f.readlines()];
	
	return lines;





def test1(inp_dir):
	
	input_dir=inp_dir
	
	from os import listdir, rename;
	from os.path import join;
	
	names=listdir(input_dir);
	
	n=len(names);
	
	for i, name in enumerate(names):
		old_path=join(input_dir, name);
		new_path=join(input_dir, ("%0"+str(len(str(n)))+"d%s")%(i+1, name[name.rfind("."):]));
		rename(old_path, new_path);

def test2(inp_dir):
	
	target_cols=128;
	
	input_dir=inp_dir
	
	from os import listdir, rename;
	from os.path import join;
	
	names=listdir(input_dir);
	
	n=len(names);
	
	import cv2;
	
	for i, name in enumerate(names):
		input_path=join(input_dir, name);
		output_path=join(input_dir, name[:name.rfind(".")]+"_t"+name[name.rfind("."):]);
		
		img=cv2.imread(input_path, 6);
		rows, cols=img.shape[:2];
		
		f=target_cols/cols;
		if (f!=1):
			img=cv2.resize(img, dsize=None, fx=f, fy=f);
		
		cv2.imwrite(output_path, img);
		
	pass;

def test3():
	
	img_dir="img/";
	output_path="table.html";
	
	img_lines=load_lines("image_scores.txt");
	method_lines=load_lines("method_scores.txt");
	
	img_scores=dict();
	for l in img_lines:
		parts=l.split();
		img_scores[parts[0]]=list(map(float, parts[1:]));
	
	print(img_scores)
	for j in range(len(img_scores[parts[0]])):
		scores=[];
		score_place=dict();
		for i, l in enumerate(img_lines):
			parts=l.split();
			#the addition is to break ties
			s=str(float(parts[j+1])+(i/(10**6)));
			score_place[s]=i;
			scores.append(s);
		print(scores);
		previous_positions_after_sorting=[score_place[x] for x in sorted(scores, key=lambda x:-float(x))];
		changed_scores=[0]*len(scores);
		for i in range(len(scores)):
			changed_scores[previous_positions_after_sorting[i]]=i;
		print(changed_scores);
		print();
		
		for i, l in enumerate(img_lines):
			parts=l.split();
			img_scores[parts[0]][j]=changed_scores[i];
	print(img_scores);
		
	
	start="\t\t\t\t";
	with open(output_path, "w", encoding="utf8") as f:
		for i, l in enumerate(method_lines):
			method=l.split()[0];
			f.write(start+"<tr>\n");
			f.write(start+"\t<td>Method&nbsp;#"+str(i+1)+"</td>\n");
			for j, s in enumerate(img_scores[method]):
				str(len(str(len(img_scores[method]))))
				src=img_dir+"/"+str(i+1)+"/"+("%02d"%(j+1))+".jpg";
				src_thumbnail=img_dir+"/"+str(i+1)+"/"+("%02d"%(j+1))+"_t.jpg";
				f.write(start+"\t<td><span style=\"display:none;\">"+str(s)+"</span><a href=\""+src+"\" target=\"_blank\"><img src=\""+src_thumbnail+"\" /></a></td>\n");
			f.write(start+"</tr>\n");
	
	
	pass;

def main():
	

	# for i in range(1,7):
	# 	inp_dir = "img/" + str(i) + "/"
	# 	print(inp_dir)

	# 	#rename the images
	# 	test1(inp_dir);
		
	# 	#create thumbnails
	# 	test2(inp_dir);
	
	#create the table data
	test3();
	
	pass;

if (__name__=="__main__"):
	main();
