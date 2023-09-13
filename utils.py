from time import sleep
from termcolor import colored,cprint
from random import randrange,choice
from secrets import token_hex
from string import ascii_letters as alpha

runner='#'

def stopwatch(sec):
	cnt=0
	while cnt <= sec:
		print(colored(f"\r[*] Seconds: {cnt}","light_cyan"),end="")
		sleep(1)
		cnt+=1
	
def timer(sec):
	while sec >= 0:
		print(colored(f"\r[*] Seconds: {sec}","light_cyan"),end="")
		sleep(1)
		sec-=1
		
def pin(l):
	s=10**(l-1)
	f=10**l
	pwd=str(randrange(s,f))
	cprint("[*] Your PIN is : "+pwd,"light_cyan",attrs=["bold"])
	
def password(l):
	ch=choice(alpha) if l%2 else ""
	pwd=token_hex(l//2)+ch
	cprint("[*] Your Password is : "+pwd,"light_cyan",attrs=["bold"])
