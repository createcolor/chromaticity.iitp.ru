#!/bin/bash
scp -r -P33722 ./*.html ./*.css ./*.jpg ./*.png ./*.py ./*.csv 'senyai@arseniy.net:/var/www/chromaticity.iitp.ru'
