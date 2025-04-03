import socket 
import subprocess
import time 


class sockconn():
  def __init__(self):
    self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  def insertinfo(self):
    try:
      self.ip = input("Insert IP Address: ")
    except Exception as Error:
      print(Error)
    try:
      self.port = int(input("Insert Port: "))
    except ValueError as Err3or:
      print(Err3or)
    finally:
      self.infoput()
  def infoput(self):
    if self.ip:
      if self.port:
       try:
        self.socket.connect((self.ip,self.port))
       except Exception as Errk:
        print("Error: {Errk}")
       while True:
        cmd = input("insert cmd: ")
        time.sleep(1)
        self.socket.sendall(cmd.encode("latin1",errors="ignore"))
        try:
           data = self.socket.recv(1024)
           print(f"Received: {data.decode('latin1',errors="ignore")}")
           continue
        except Exception as e: 
          print(e)
          break
        except KeyboardInterrupt:
          self.socket.close()
          break
        


        
if __name__ == "__main__":
    sock = sockconn()
    sock.insertinfo()
        

    
