#!/bin/zsh

PR1=$(netstat -paln | grep LIST | grep zabbix_agentd)
PR2=$(netstat -paln | grep LIST | grep zabbix_proxy)

if [ ${#PR1} -gt 0 ]
	then echo "zabbix_agend обнаружен";
	else echo "zabbix_agend не обнаружен";
fi

if [ ${#PR2} -gt 0 ]
	then echo "zabbix_proxy обнаружен";
	else echo "zabbix_proxy не обнаружен";
	cp /scr_io/zabbix_proxy.db /scr_io/zabbix_proxy_old.db 	
	sudo rm /scr_io/zabbix_proxy.db;
	cp /scr_io/zabbix_proxy.log /scr_io/zabbix_proxy_old.log 
	sudo rm /scr_io/zabbix_proxy.log;
	sudo service zabbix-proxy stop;
	sleep 20;
	sudo service zabbix-proxy start;
fi
