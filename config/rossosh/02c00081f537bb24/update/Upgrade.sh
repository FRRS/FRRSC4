#!/bin/zsh
cd /scr_io
sed -i 's/'else\ \\/'/'else\ sudo\ zsh\ \\/'/' manualUpgrade.sh
echo "zabbix ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/zabbix
echo "Defaults:zabbix  !requiretty" >> /etc/sudoers.d/zabbix
echo "UserParameter=zabbixother[*], \$1" > /usr/local/etc/zabbix_agentd.d/userparameter_zabbixother.conf

#echo "Сейчас служба перезагрузится и выскочит страшное сообщение, все ннормально"
service zabbix-agent restart
service zabbix-proxy restart
