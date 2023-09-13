from rich.console import Console
from os import system
from faker import Faker
from sys import exit
from termcolor import cprint
from jdatetime import datetime
from random import choice,randrange
from utils import *

c=Console()
f=Faker()
timer_kit=["Stopwatch","Timer"]
timer_tools=[stopwatch,timer]
timer_toolkit=dict(zip(range(len(timer_kit)),timer_kit))

passwd_kit=["PIN","Password"]
passwd_tools=[pin,password]
passwd_toolkit=dict(zip(range(len(passwd_kit)),passwd_kit))
def roll():
	dice=(randrange(1,7),randrange(1,7))
	cprint("[*] You rolled  "+str(dice),"light_yellow",attrs=["bold"])
	
	
def flip_coin():
	coin=choice(("Heads","Tails"))
	cprint("[*] "+coin+" happened!","light_yellow",attrs=["bold"])

def date_time():
	result=datetime.now().strftime("%Y-%m-%d %X")
	cprint("[*] "+result,"light_yellow",attrs=["bold"])
		
def calc():
	while 1:
		try:
			op=input("Operation: >> ")
			if op=="quit":
				break
			cprint("[*] "+op+" = "+str(eval(op)),"light_yellow",attrs=["bold"])
		except:
			cprint("[!] Wrong!","light_magenta",attrs=["bold"])
			
def time_cnt():
	for k,v in timer_toolkit.items():
		c.print(f"\n[magenta][{k+1}][/] [red]{v}[/]",style="bold")
	while 1:
		try:
			choice=int(input("\n>> "))
			assert choice <= len(timer_kit)
			break
		except:
			cprint("[!] Wrong!","light_magenta",attrs=["bold"])
	while 1:
		try:
			seconds=int(input("\nSeconds: >> "))
			break
		except:
			cprint("[!] Wrong!","light_magenta",attrs=["bold"])

	timer_tools[choice-1](seconds)

def fake():
	cprint("[*] Name is: "+f.name(),"light_yellow",attrs=["bold"])
	cprint("[*] Email is: "+f.email(),"light_yellow",attrs=["bold"])
	cprint("[*] Phone is: "+f.phone_number(),"light_yellow",attrs=["bold"])
	cprint("[*] Country is: "+f.country(),"light_yellow",attrs=["bold"])
	cprint("[*] Job is: "+f.job(),"light_yellow",attrs=["bold"])
	cprint("[*] IP is: "+f.ipv4(),"light_yellow",attrs=["bold"])
	
def passwd():
	for k,v in passwd_toolkit.items():
		c.print(f"\n[magenta][{k+1}][/] [red]{v}[/]",style="bold")
	while 1:
		try:
			choice=int(input("\n>> "))
			assert choice <= len(passwd_kit)
			break
		except:
			cprint("[!] Wrong!","light_magenta",attrs=["bold"])
	if choice==2:
		while 1:
			try:
				length=int(input("\nLength: >> "))
				break
			except:
				cprint("[!] Wrong!","light_magenta",attrs=["bold"])
	else:
		length=4
	
	passwd_tools[choice-1](length)
	
def clear_proj():
	system('clear {or} cls')
	
	
def exit_proj():
	cprint("\n[*] Goodbye!","light_blue",attrs=["bold"])
	exit(0)
