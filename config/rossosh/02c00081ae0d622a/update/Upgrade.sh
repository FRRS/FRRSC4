#!/bin/bash
##Updating sript for FRRSC4 Ver.0.0.1.Bild.001
date > //scr_io/upgrade.txt
cd //etc/cron.d
sudo wget -O GSMinfotages https://raw.githubusercontent.com/FRRS/FRRSC4/master/config/rossosh/$HOSTNAME/update/GSMinfotages
echo "Готово"
##
