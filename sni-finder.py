# // Created   : Md Josif Khan
# // Contact  : facebook.com/josifvai
# // GitHub  : github.com/josifkhan
# // Python version : 3.11
import argparse,sys,os
import socket
import ssl
_='_'*50
def banners():
	os.system('clear')
	banner=f"""\033[1;30m
                         
 @@@@@@   @@@  @@@  @@@  
@@@@@@@   @@@@ @@@  @@@  |Tool Name - SNI FINDER
!@@       @@!@!@@@  @@!  |Created  : Md Josif Khan
!@!       !@!!@!@!  !@!  |YouTube  : Md Josif Khan
!!@@!!    @!@ !!@!  !!@  |Facebook : @josifvai
 !!@!!!   !@!  !!!  !!!  |GitHub   : @josifkhan
     !:!  !!:  !!!  !!:  |
    !:!   :!:  !:!  :!:  |
:::: ::    ::   ::   ::  
:: : :    ::    :   :    
{_}\033[0m

"""
	print(banner)
def find_sni_hosts(hostname):
	banners()
	try:
		ip_address = socket.gethostbyname(hostname)
		context = ssl.create_default_context()
		context.set_ciphers('HIGH:!aNULL')
		with socket.create_connection((ip_address, 443)) as sock:
			with context.wrap_socket(sock, server_hostname=hostname) as ssl_sock:
				sni_hosts = ssl_sock.getpeercert()["subjectAltName"]
				if not sni_hosts:
					print(f"\033[35;5;83mNo SNI hosts found for \033[32m{ip_address}\033[0m.")
				else:
					print(f"\033[35;5;93m- SNI hosts found for \033[1;32m{ip_address}\033[0m:")
					for host in sni_hosts:
						if host[0] == "DNS":
							print(f"\t- {host[1]}")
	except KeyboardInterrupt:sys.exit()
	#except ssl.SSLCertVerificationError:sys.exit("\033[38;5;83mInvalid hostname, try valid host.\033[0m")
if __name__ == "__main__":
	try:
		parser = argparse.ArgumentParser(description="\033[1;30mFind SNI hosts on an IP address.\033[0m")
		parser.add_argument("hostname", help="The Hostname to check.")
		args = parser.parse_args()
		find_sni_hosts(args.hostname)
	except KeyboardInterrupt:sys.exit()
	except AttributeError:sys.exit("\033[38;5;83mInvalid hostname, try valid host.\033[0m")