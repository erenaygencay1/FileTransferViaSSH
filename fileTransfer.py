	# -*- coding: utf-8 -*-
import subprocess
import sys
import getpass
Username = ""
ip = ""
passwd = ""
scp = []	



def main(ip,Username,passwd,os,path):
	

	if len(sys.argv) != 6:
		Usage()

	if os == 'l':
		transfer_linux(Username,ip,passwd,path)
	if os == 'w':
		transfer_win(Username,ip,passwd,path)
	if os != "w" and os != "l":
		print("[!] Wrong OS decleration !")
		Usage()


def Usage():
	print("[**] USAGE [**]")
	print(">>> python fileTransfer.py <targetIP> <Username> <Password> <TargetOS> <Path>")
	print("")
	print("TargetOS : \n \t if target os is windows : w \n \t if target is linux : l \n")
	print("Username : \n \t it is the ssh login username. \n\nPassword : \n \t it is the ssh login password. \n\nPath : \n \t it is the path of the file which want you send via ssh. ")


	

def transfer_linux(Username,ip,passwd,path):
	
	
	
	
	subprocess.check_output('sshpass -p '+passwd+' scp ' +path+ " " + Username + '@' + ip + ':/tmp; exit 0', stderr=subprocess.STDOUT, shell=True)
	print("[+] Transfer Completed.")
	print("[!] if you did not find the file on /tmp directory please check out provided password")



def transfer_win(Username,ip,passwd,path):
	
	
	
	
	subprocess.check_output('sshpass -p ' + passwd + " scp " + path + " " + Username + '@' + ip +':C:/Users/' + Username + ';'+ ' ' + 'exit 0', stderr=subprocess.STDOUT, shell=True)
	print("[+] Transfer Completed.")
	print("[!] if you did not find the file on C:\Users\<Username> directory please check out provided password")

try:

	if __name__ == "__main__":
		main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])

except IndexError:
	Usage()