#!/bin/zsh
##Updating sript for FRRSC4 Ver.0.0.1.Bild.001
date > //scr_io/upgrade.txt
cd //etc/cron.d
sudo wget -O https://raw.githubusercontent.com/FRRS/FRRSC4/master/config/rossosh/$HOST/update/GSMinfotages
echo "Готово"
##
