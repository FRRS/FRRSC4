# Утилита опроса счетчика и записи в файлы и при значительном (3%) изменении передача в ZABBIX
import time
import subprocess

from time import sleep
from math import fabs

oldPsum = 0.1
oldPT1 = 0.1
oldPT2 = 0.1
oldPT3 = 0.1
oldPT4 = 0.1
oldUV = 0.1
oldIA = 0.1
oldFH = 0.1
oldPM = 0.1
oldFI = 0.1
num = 1

HOSTNAME = subprocess.getoutput("hostname")

while num < 10:

	#Get Wh data
	WHstr = subprocess.getoutput("/scr_io/tec")

	WHstr = WHstr[14:]
	WHstr = WHstr.replace("\n",":")
	WHstr = WHstr.replace(" ",":")
#	print ( WHstr )
	masWH = WHstr.split(':')	
	Devel = masWH[0]
	Model = masWH[2]
	SN = masWH[4]
	WHstr0 = "Узел учета модель: " + Model + " Серийный номер: " + SN
			
	Psum= float(masWH[7])
	PT1 = float(masWH[12])
	PT2 = float(masWH[15])
	PT3 = float(masWH[18])	
	PT4 = float(masWH[21])	
	WHstr1 = str('Потреблено всего: %.2f кВт/ч ' % Psum) + str('в т.ч. Тариф1: %.2f кВт/ч. ' % PT1)
	if (PT2 > 0) :
		WHstr1 = WHstr1 + str('Тариф2: %.2f кВт/ч. ' % PT2)
	if (PT3 > 0) :
		WHstr1 = WHstr1 + str('Тариф3: %.2f кВт/ч. ' % PT3)
	if (PT4 > 0) :
		WHstr1 = WHstr1 + str('Тариф4: %.2f кВт/ч. ' % PT4)

	# Write to file
	tFile = open('/scr_io/Wh1', "w")
	tFile.write(WHstr1)
	tFile.close()
		
	UV = float(masWH[28])
	IA = float(masWH[31])
	FH = float(masWH[40])	
	WHstr2 = str('%3.0fV' % UV) + str('%3.0fA' % IA) + str('%2.0f*' % FH)
	# Write to file
	tFile = open('/scr_io/Wh2', "w")
	tFile.write(WHstr2)
	tFile.close()

	PM = float(masWH[34])*1000
	FI = float(masWH[37])	
	WHstr3 = str('%5.0fW' % PM) + str(' $%2.0f' % FI)
	# Write to file
	tFile = open('/scr_io/Wh3', "w")
	tFile.write(WHstr3)
	tFile.close()	
	
	#OLD DATA
	if abs(Psum - oldPsum) > 1 :
		# SEND TO ZABBIX
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k all -o " + str(Psum))
		oldPsum = Psum
		#OLD DATA
	if abs(PT1 - oldPT1) > 1 :
		# SEND TO ZABBIX
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k T1 -o " + str(PT1))
		oldPT1 = PT1
	if abs(PT2 - oldPT2) > 1 :
		# SEND TO ZABBIX
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k T2 -o " + str(PT2))
		oldPT2 = PT2
	if abs(PT3 - oldPT3) > 1 :
		# SEND TO ZABBIX
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k T3 -o " + str(PT3))
		oldPT3 = PT3		
	if abs(PT4 - oldPT4) > 1 :
		# SEND TO ZABBIX
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k T4 -o " + str(PT4))
		oldPT4 = PT4		
	if abs(UV - oldUV) > 1 :
		# SEND TO ZABBIX
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k UV -o " + str(UV))
		oldUV = UV
	if abs(IA - oldIA) > 1 :
		# SEND TO ZABBIX
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k IA -o " + str(IA))
		oldIA = IA
	if abs(FH - oldFH) > 1 :
		# SEND TO ZABBIX
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k FG -o " + str(FH))
		oldFH = FH		
	if abs(PM - oldPM) > 10 :
		# SEND TO ZABBIX
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k PW -o " + str(PM))
		oldPM = PM
	if abs(FI - oldFI) > 1 :
		# SEND TO ZABBIX
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k CF -o " + str(FI))
		oldFI = FI	
		
	if (num < 2) :
	# Write to file
		tFile = open('/scr_io/Wh0', "w")
		tFile.write(WHstr0)
		tFile.close()
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k developer -o " + Devel)
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k model -o " + Model)
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k SN -o " + SN)
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k all -o " + str(Psum))
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k T1 -o " + str(PT1))
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k T2 -o " + str(PT2))
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k T3 -o " + str(PT3))
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k T4 -o " + str(PT4))
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k UV -o " + str(UV))
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k IA -o " + str(IA))
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k FG -o " + str(FH))
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k PW -o " + str(PM))
		subprocess.getoutput("zabbix_sender -vv -z 127.0.0.1 -s " + HOSTNAME + " -k CF -o " + str(FI))
		
	num = 2

	sleep(5)               # Wait 10 seconds.
