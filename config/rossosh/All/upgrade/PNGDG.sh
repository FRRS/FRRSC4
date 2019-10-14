#!/bin/zsh
IP1="8.8.8.8"
IP2="10.44.44.1"
TRIES=4
currentDate=`date`

PING=$(ping -qc $TRIES -W 1 $IP1)
I1=$(echo -e "$PING" | grep packet)
PERCENT_LOST1=$(echo -e "$I1" | awk '{ print $6 }' | tr -d '%')

if [[ $PERCENT_LOST1 -eq 100 ]]
    then echo "$currentDate потеря связи c 8.8.8.8" >> /var/log/PINGDOG.log;

	# гасим GPRS
	poff -a > /dev/null 2>&1
	# перегружаем модуль GSM
	echo -e "AT+CFUN=1,1\r\n" >/dev/ttyS1
	rm /etc/flggprs

fi

PING=$(ping -qc $TRIES -W 1 $IP2)
I2=$(echo -e "$PING" | grep packet)
PERCENT_LOST2=$(echo -e "$I2" | awk '{ print $6 }' | tr -d '%')

if [[ $PERCENT_LOST2 -eq 100 ]]
    then echo "$currentDate потеря связи c 10.44.44.1" >> /var/log/PINGDOG.log;
	# гасим GPRS
	poff -a > /dev/null 2>&1
	# перегружаем модуль GSM
	echo -e "AT+CFUN=1,1\r\n" >/dev/ttyS1
	rm /etc/flggprs
fi