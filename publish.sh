#!/bin/bash
# scp -r -P33722  'senyai@arseniy.net:/var/www/chromaticity.iitp.ru'
rsync -arvz -e 'ssh -p 33722' --progress ./*.html ./*.css ./*.jpg ./*.png ./*.py ./*.csv 'senyai@arseniy.net:/var/www/chromaticity.iitp.ru'