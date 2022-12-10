#!/usr/bin/env python3

import sys
from termcolor import colored
import subprocess,os
import time,argparse


"""
USAGE
ls file | ./gf_007
ls * | ./gf_007
"""


def get_arguments():
	parser = argparse.ArgumentParser("ls file | ./gf_007\n       ls *   | ./gf_007")
	args = parser.parse_args()

def banner():
	x="""
		_  _ _ _    _    ____ ____   ____ ____ ___ 
		|_/  | |    |    |___ |__/   |  | |  |   /
		| \\_ | |___ |___ |___ |  \\   |__| |__|  /  
      """


 
	y = "		+-----------------------------------------+"     
	z = "							~~Twitter: Killeroo7p\n"
	print(colored(x,'blue'))
	print(colored(y,'red'))
	print(colored(z,'green'))

def gf():
	os.mkdir("gf_results")
	all_files =[]
	for line in sys.stdin:
		all_files.append(line.strip())


	with open(os.devnull,"w") as DNULL:
		gf_list=((subprocess.check_output("gf --list",shell=True)).decode()).split("\n")

		for pattern in gf_list:
			total_found = 0
			if pattern=="jsvar":
				continue

			with open("gf_results/summary.txt","a") as summary_file:
				with open(f"gf_results/{pattern}","a") as result_file:
					for file in all_files:
						cmd = f"cat {file} | gf {pattern}"

						print(colored(pattern,"yellow")+"  --> "+colored(file,"cyan"),end="\r"),
						sys.stdout.flush()
						# time.sleep(1)
						# print(cmd)
						output = (subprocess.check_output(cmd,shell=True)).decode()
						if len(output)>1:
							total_found +=1
							print(colored(pattern,"yellow")+"  --> "+colored(file,"cyan")+"                                                          ")
							summary_file.write(f"{pattern}  --> {file}\n")
							result_file.write(f"FILE007: {file}\n{output}\n----------------------------------------------------------------------------------------\n")

					if total_found==0:
						os.remove(f"gf_results/{pattern}")

					with open("gf_results/logs.txt","a") as logFile:
						logFile.write(f"{pattern} = {total_found}\n")


def main():
	banner()
	get_arguments()
	gf()

main()