import socket
import sys
import subprocess
from datetime import datetime

subprocess.call("clear", shell=True)

target_server_ip = input("Please enter target ip :")

print("Scanne in progress for " + target_server_ip)