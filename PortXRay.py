import socket
import sys
import subprocess
from datetime import datetime

subprocess.call("clear", shell=True)

target_server_ip = input("Please enter target ip : ")

print("Scanne in progress for " + target_server_ip)

time_1 = datetime.now()

try:
  for port in range(1, 1024):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    result = sock.connect_ex((target_server_ip, port))
    if result == 0:
        print("Port {}:  open".format(port))
        sock.close()
except KeyboardInterrupt:
  print("You have stopped the progression")
  sys.exit()

except socket.error:
    print("Cannot connect to your target")

time_2 = datetime.now()
result = time_1 - time_2
print("The scan took {}").format(str(result))