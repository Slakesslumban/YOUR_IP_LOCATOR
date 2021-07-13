import socket
from requests import get

host = socket.gethostname()
local_ip = socket.gethostbyname(host)
public_ip = get("https://api.ipify.org").text
print(host)
print(local_ip)
print(public_ip)