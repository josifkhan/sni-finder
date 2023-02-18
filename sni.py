# SNI FINDER IS A TOOL TO FIND THE SAME HOST/IP ASSOCIATED WITH OTHER DOMAIN NAMES, THE TOOL IS CREATED/SCRIPTED BY "MD JOSIF KHAN".
import os,sys,time,random,socket
import requests

os.system('clear')
hh5y='https://'
hhy='api'
cet34='.hacker'
etg='target.com/'
sfdf='reverse'
kujytb='ip'
ftjt='lookup/?'
sd='q='
hostt=[]
banner="""\033[1;30m
                                                         
 _|          _|  _|    _|  _|_|_|  _|      _|    _|_|_|  
 _|          _|  _|  _|      _|    _|_|    _|  _|        
 _|    _|    _|  _|_|        _|    _|  _|  _|  _|  _|_|  
   _|  _|  _|    _|  _|      _|    _|    _|_|  _|    _|  
     _|  _|      _|    _|  _|_|_|  _|      _|    _|_|_|  
                                                         
                       SNI FINDER
                 Created : Md Josif Khan
                 YT :   White King
                 FB : fb.com/josifvai
________________________________________________________
\033[0m"""
print(banner)
try:
	clr=random.choice('1 2 3 4'.split())
	inp=input(f'\033[1;30m[\033[32menter\033[0m\033[1;30m] Host/Domain/IP>>\033[1;3{clr}m')
	print('\033[0m')
	os.system('clear')
	print(banner)
	kiuyb=hh5y+hhy+cet34+etg+sfdf+kujytb+ftjt+sd+inp
	# print(kiuyb)
	print(f'\033[1;31mPLEASE WAIT, LOOKING UP FOR HOSTS IN "{inp}"\033[0m\n\n')
	sys.stdout.write(f'\r[+] getting host ({inp}) ip ')
	time.sleep(2)
	h=socket.gethostbyname(inp)
	sys.stdout.write(f'\r[✔] getting host ({inp}) ip {h}')
	print('\r')
	hosts=requests.get(url=kiuyb).text.split()
	# print(hosts)
	if 'Membership' in hosts:
		sys.exit('[!] Too much requests, try again later.')
	elif 'found' in hosts and 'DNS' in hosts:
		sys.exit('[!] No results found, try an other host.')
	elif 'error' in hosts:
		sys.exit('[!] Invalid host address.')
	else:
		pass
	print(f'\r[✔] results found : {len(hosts)}')
	time.sleep(1)
	print(f'\r[+] getting same ip hosted on "{inp}"')
	print('\r[+] please wait, this might takes some time.')
	print('')
	inpp=inp.replace(".","_")
	c=1
	for host in hosts:
		c+=1
		try:
			ip=socket.gethostbyname(host)
			if str(ip)==str(h):
				print(f'\r[{c}/{len(hosts)}] \033[32m{host} | \033[1;31m{socket.gethostbyname(host)}\033[0m')
				hostt.append('a')
				open(f'sni-{inpp}.txt','a').write(f'{host}/{ip}\n')
			else:
				pass
		except socket.gaierror:
			pass
	print('[✔] Task completed!')
	print(f'[✔] Target : {inp}/{h}')
	print(f'[✔] Results : {len(hosts)}')
	print(f'[✔] SNI hosts : {len(hostt)}')
	print(f'[✔] File saved : sni-{inpp}.txt')

except requests.exceptions.ConnectionError:
	sys.exit('\n[!] Connection lost:')
except socket.gaierror:
	sys.exit('\n[!] Invalid host address.')
except KeyboardInterrupt:
	sys.exit()
