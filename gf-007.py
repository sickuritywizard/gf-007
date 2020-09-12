#!/usr/bin/env python3

import sys,shutil
from termcolor import colored
import subprocess,os
import time,argparse


#RUN THIS PROGRAM IN ANY DIRECTORY CONTAINING JS,TEXT,HTML FILES AND IT WILL RUN GF FOR ALL THE FILES" 

def banner():
	x="""
	                                                                     
		 ██████╗ ███████╗     ██████╗  ██████╗ ███████╗
		██╔════╝ ██╔════╝    ██╔═████╗██╔═████╗╚════██║
		██║  ███╗█████╗█████╗██║██╔██║██║██╔██║    ██╔╝
		██║   ██║██╔══╝╚════╝████╔╝██║████╔╝██║   ██╔╝ 
		╚██████╔╝██║         ╚██████╔╝╚██████╔╝   ██║  
		 ╚═════╝ ╚═╝          ╚═════╝  ╚═════╝    ╚═╝                                                                   
      """

 
	y = "		+--------------------------------------------+"     
	z = "							~~Twitter: Killeroo7p\n"
	print(colored(x,'blue'))
	print(colored(y,'red'))
	print(colored(z,'green'))


def get_arguments():
	parser = argparse.ArgumentParser("Runs gf in current Directory")
	parser.add_argument('-w','--whitelist',dest='whitelist',help="Run Gf only on these extensions(js,html,txt)")
	parser.add_argument('-b','--blacklist',dest='blacklist',help="Exclude gf on these extensions(php,html)")
	parser.add_argument('-a','--all-files',dest='all_files',action="store_true",help="Run Gf on js,html,etc files")
	parser.add_argument('-u','--url-files',dest='url_files',help="Run Gf on a Files with URL [Ex: -u file1,file2]")
	args = parser.parse_args()
	return args


def gf_all_files():

	try:
		os.mkdir("gf_results")
	except FileExistsError:
		print(colored("[-] gf_results Directory Already Exists","red"))
		exit(0)

	all_files = os.listdir()

	for file in all_files:   #Removing Directories
		if os.path.isdir(file):
			all_files.remove(file)

	allfiles_patterns = ["aws-keys","base64","cors","debug-pages","firebase","fw","go-functions","http-auth","ip","json-sec","meg-headers","php-curl","php-errors","php-serialized","php-sinks","php-sources","s3-buckets","sec","servers","strings","takeovers","upload-fields","urls","jsvar"]

	for pattern in allfiles_patterns:
		try:
			total_found = 0

			with open("gf_results/summary.txt","a") as summary_file:
				with open(f"gf_results/{pattern}","a") as result_file:
					for file in all_files:
						print(colored(pattern,"yellow")+"  --> "+colored(f"{file}                                              ","cyan"),end="\r"),
						sys.stdout.flush()

						cmd = f"gf {pattern} {file}"
						output = (subprocess.check_output(cmd,shell=True)).decode()
						if len(output)>1:
							total_found +=1
							result_file.write(output)
							summary_file.write(f"{pattern}  --> {file}\n")

					if total_found==0:
						os.remove(f"gf_results/{pattern}")
					else:
						print(colored(pattern,"yellow")+"  --> "+colored(f"{file} ","cyan")+"                                                                 ")
						with open("gf_results/logs.txt","a") as logFile:
							logFile.write(f"{pattern} = {total_found}\n")

		except KeyboardInterrupt:
			ans = input(colored("\n\nKeyboard Interrupt Detected. Confirm Exit(y/n): ","red"))
			if ans.lower()=="yes" or ans.lower()=="y":
				print(colored("Output saved to gf_results","green"))
				exit(0)
			else:
				continue
		except TypeError:
			pass
		except UnicodeDecodeError:
			pass

	print("                                                                                                            ")
	print(colored("Output saved to gf_results","green"))

def gf_url_files(filename):

	try:
		os.mkdir("gf_results")
	except FileExistsError:
		print(colored("[-] gf_results Directory Already Exists","red"))
		exit(0)

	files = filename.split(",")
	urlfile_patterns = ["debug_logic","idor","img-traversal","interestingEXT","interestingparams","lfi","rce","redirect","sqli","ssrf","ssti","xss","base64"]
#	Not_added = ["interestingsubs"]

	for pattern in urlfile_patterns:
		for file in files:
			try:
				print(colored(pattern,"yellow")+"  --> "+colored("Analyzing","cyan"),end="\r"),
				sys.stdout.flush()
				cmd = f"gf {pattern} {file}"
				output = (subprocess.check_output(cmd,shell=True)).decode()
				if len(output)>1:
					with open(f"gf_results/{pattern}","a") as result_file:
						result_file.write(output)
					with open("gf_results/summary.txt","a") as summary_file:
						summary_file.write(f"{pattern}  --> {file}\n")
					print(colored(pattern,"yellow")+"  --> "+colored(f"{file} ","cyan")+"                                                                 ")

			except KeyboardInterrupt:
				ans = input(colored("\n\nKeyboard Interrupt Detected. Confirm Exit(y/n): ","red"))
				if ans.lower()=="yes" or ans.lower()=="y":
					print(colored("Output saved to gf_results","green"))
					exit(0)
				else:
					continue
			except TypeError:
				pass
			except UnicodeDecodeError:
				pass

	print("                                                                                                            ")
	print(colored("Output saved to gf_results","green"))

def main():
	banner()
	args = get_arguments()

	if args.all_files:
		gf_all_files()

	elif args.url_files:
		file = args.url_files
		gf_url_files(file)   

	else:
		print(colored("[-]Please Specify Either -u or -a","red"))
		exit(0)


main()
