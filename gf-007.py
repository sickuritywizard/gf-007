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
	parser = argparse.ArgumentParser("ls * | gf-007")
	args = parser.parse_args()


def gfauto():
	if os.path.exists("gf_results"):
		print(colored("[-] gf_results Directory Already Exists","red"))
		exit(0)

	try:
		os.mkdir("../gf_results")
	except FileExistsError:
		print(colored("[-] gf_results Directory Already Exists in parent Directory(../gf_results)","red"))
		exit(0)


	gf_list=((subprocess.check_output("gf --list",shell=True)).decode()).split("\n")
	all_files = os.listdir()

	for file in all_files:   #Removing Directories
		if os.path.isdir(file):
			all_files.remove(file)

	for file in all_files:   #Removing Directories
		if os.path.isdir(file):
			all_files.remove(file)

	try:
		remove_patterns = ["","ip","sec","jsvar","php-errors","servers","upload-fields","urls","meg-headers","http-auth","debug-pages","fw","php-sinks","json-sec","s3-buckets","urls"]
		for item in remove_patterns:
			gf_list.remove(item)
	except:
		pass

	pattern_with_one_process = ["ip","sec","jsvar","php-errors","servers","upload-fields","urls","meg-headers","http-auth","debug-pages","fw","php-sinks","json-sec","s3-buckets","urls"]   ###Patterns that display result from all file by default

	for pattern in pattern_with_one_process:
		try:
			with open("../gf_results/summary.txt","a") as summary_file:
				with open(f"../gf_results/{pattern}","a") as result_file:

					print(colored(pattern,"yellow")+"  --> "+colored("*","cyan"),end="\r"),
					sys.stdout.flush()
					cmd = f"cat * | gf {pattern}"
					output = (subprocess.check_output(cmd,shell=True)).decode()

					if len(output)>1:
						print(colored(pattern,"yellow")+"  --> "+colored(f"Found(Check {pattern} File)","cyan")+"                                                                 ")
						summary_file.write(f"{pattern}  --> *\n")
						result_file.write(output)

						with open("../gf_results/logs.txt","a") as logFile:
							logFile.write(f"{pattern} = Check Manually\n")

		except KeyboardInterrupt:
			ans = input(colored("\n\nKeyboard Interrupt Detected. Confirm Exit(y/n): ","red"))
			if ans.lower()=="yes" or ans.lower()=="y":
				print(colored("Output saved to gf_results","green"))
				shutil.move("../gf_results","./")
				exit(0)
			else:
				continue
		except TypeError:
			pass
		except UnicodeDecodeError:
			pass

		##For other Patterns
	for pattern in gf_list:

		try:
			total_found = 0

			with open("../gf_results/summary.txt","a") as summary_file:
				with open(f"../gf_results/{pattern}","a") as result_file:
					for file in all_files:
						print(colored(pattern,"yellow")+"  --> "+colored(file,"cyan"),end="\r"),
						sys.stdout.flush()

						cmd = f"cat {file} | gf {pattern}"
						output = (subprocess.check_output(cmd,shell=True)).decode()
						if len(output)>1:
							total_found +=1
							print(colored(pattern,"yellow")+"  --> "+colored(file,"cyan")+"                                                                 ")
							summary_file.write(f"{pattern}  --> {file}\n")
							result_file.write(f"FILE007: {file}\n{output}\n---------------------------------------------------------------\n")

					if total_found==0:
						os.remove(f"../gf_results/{pattern}")
					else:
						with open("../gf_results/logs.txt","a") as logFile:
							logFile.write(f"{pattern} = {total_found}\n")

		except KeyboardInterrupt:
			ans = input(colored("\n\nKeyboard Interrupt Detected. Confirm Exit(y/n): ","red"))
			if ans.lower()=="yes" or ans.lower()=="y":
				print(colored("Output saved to gf_results","green"))
				shutil.move("../gf_results","./")
				exit(0)
			else:
				continue
		except TypeError:
			pass
		except UnicodeDecodeError:
			pass

	print("                                                                                                            ")
	print(colored("Output saved to gf_results","green"))
	shutil.move("../gf_results","./")


def main():
	banner()
	get_arguments()
	gfauto()	


main()