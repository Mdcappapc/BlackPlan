from pyfiglet import figlet_format
from rich.console import Console
from os import system
from termcolor import cprint
from tools import *

c=Console()
code_line=0
kit=["Roll a dice  ","Flip a coin  ","Date & Time  ","Calculator   ","Time Counter ","Fake generate","Passwd Build ","Clear Console","Quit         "]
for tool in kit: assert len(tool)==13,"Spacing Access Denied!"

tools=[roll,flip_coin,date_time,calc,time_cnt,fake,passwd,clear_proj,exit_proj]
toolkit=dict(zip(range(1,len(kit)+1),kit))
def banner_kit():
	global code_line
#	system("clear {or} cls")
	banner=figlet_format("BlackPlan  1.0",justify="center")
	cprint(banner,"light_red",attrs=["bold"])
	print("\n"+"-"*79)
	print("|",end=" ")
	for k,v in toolkit.items():
		c.print(f"[green][{k}][/] [blue]{v}[/]",style="bold",end="     |    ")
		code_line+=1
		if code_line==3:
			code_line=0
			print("\n"+"-"*79)
			if k<len(kit):
				print("|",end=" ")
		
def prompt():
	while 1:
		try:
			choice=input("\n> ")
			if choice != runner:
				choice=int(choice)
				assert choice <= len(tools)
			break
		except Exception:
			cprint("[!] Wrong!","light_magenta",attrs=["bold"])
			
	return choice		

def main():
	banner_kit()
	while 1:
		tool=prompt()
		if tool==runner:
			break
		tools[tool-1]()
if __name__ == "__main__":
	main()
