import socket 
import subprocess
import time 
import logging
from colorama import init , Fore, Back
init()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logfile.log'), # imposta lo stream su file
        logging.StreamHandler() # imposta lo stream su console
    ]
)
class sockconn():
  def __init__(self):
    self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    global filetxt
    filetxt= "config.txt"
  def insertinfo(self):
    try:

      time.sleep(0.5)
      self.ip = input(Fore.CYAN + "Insert IP Address: ")
      self.port = int(input(Fore.LIGHTMAGENTA_EX + "Insert Port: "))
      if not self.port:
        self.port = 4444
      
      
    except Exception as Error:
      time.sleep(1)
      logging.info(Fore.RED + Error)
    finally:
      self.infoput()
  def infoput(self):
    if self.ip:
      if self.port:
       
       try:
        with open(filetxt,'w') as file:
          file.write(self.port)
          
        self.socket.connect((self.ip,self.port))
        time.sleep(1)
        logging.info(Fore.CYAN + f"trying to connect to {self.ip}:{self.port}")
       except Exception as Errk:
        time.sleep(1)
        logging.info(Fore.RED  + f"Error: {Errk}")
       while True:
        time.sleep(0.2)
        cmd = input(Fore.MAGENTA + "insert cmd: ")
        time.sleep(1)
        self.socket.sendall(cmd.encode("latin1",errors="ignore"))
        try:
           data = self.socket.recv(1024)
           logging.info( Fore.CYAN +  f"Received: {data.decode('latin1',errors="ignore")}")
           continue
        except Exception as e: 
          logging.info(Fore.RED  + e)
          break
        except KeyboardInterrupt:
          self.socket.close()
          logging.info(Fore.RED +  "Keyboard Interruption")
          break        




    
