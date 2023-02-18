# SNI Hosts Finder
This is a Python script that can be used to discover the hosts that a web server is serving using Server Name Indication (SNI). SNI is an extension to the Transport Layer Security (TLS) protocol that allows clients to specify the hostname they are trying to connect to.

The script works by sending a TLS handshake message to the server with a list of SNI hostnames to check. If the server is serving any of the specified hosts, it will respond with a TLS certificate, which can be parsed to extract the hostname.

The script is easy to use and can be run from the command line. Simply provide a list of SNI hosts to check, along with the IP address or hostname of the web server, and the script will do the rest.

Features:

<ul><li>Quickly discovers the hosts a web server is serving using SNI
Easy to use and can be run from the command line
Lightweight and written in Python, making it easy to modify and extend
</li></ul>
<br/>Dependencies:

<ul><li>Python 3.x</li>
<li>pyOpenSSL library</li></ul>
<br/>
Packages/Libraries
<ul><li>socket</li>
<li>argparse</li>
<li>ssl</li></ul>

Usage:
>> python sni_finder.py [hostname]


Note: This script is intended for testing and educational purposes only. Do not use it to access websites or services without permission.
