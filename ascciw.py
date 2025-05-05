import logging, time
from colorama import init, Fore
from cost2 import sockconn
init()


kesf = """My tool is a bind shell that allows a client to connect to a server via port 443. However, before the connection can be established, the target must already be listening on port 443.\n If the target isn't configured to listen, the target will need to run the script I created, called revshell.py, which will start listening on port 443, enabling the client connection.

This tool is fully modifiable and can be adapted to the user's needs.\n Please note that I take no responsibility for any misuse of the tool. It was created for ethical purposes and learning. If you have any questions or need support, feel free to contact me. In case of any errors, please forgive me as I am not an expert, and the code is still being updated weekly.
"""




prg = """Il mio strumento è una bind shell, ovvero un programma che permette a un client (chi si connette) di collegarsi a un server (la macchina bersaglio) attraverso la porta 443.\n Tuttavia, affinché il collegamento avvenga correttamente, il server deve già essere in ascolto su quella porta.

Se il server non è configurato per ascoltare sulla porta 443, potrete  eseguire uno script chiamato revshell.py su una macchina bersaglio, che ho creato proprio per questo scopo sennò usate altro metodi o sperimentate su macchine che ascoltano sulla 443. \n Una volta avviato lo script, la macchina (bersaglio) inizierà ad ascoltare su quella porta, rendendo possibile la connessione da parte del client.

Questo strumento è completamente personalizzabile e può essere adattato in base alle esigenze dell’utente. È stato sviluppato con finalità educative e per apprendimento, e non mi assumo alcuna responsabilità per eventuali usi impropri. Se hai domande o hai bisogno di assistenza, non esitare a contattarmi. Il codice viene aggiornato settimanalmente, quindi se dovessero esserci errori, ti chiedo comprensione: non sono un esperto, ma continuo a migliorarlo con il tempo."""















ascii_ar24re3 = """
       :+===++++=++===++==             %=*++*=                   =+++++=++==                        
   :-##++===++++=++===++==#+:#     ::::%==++==%=              =##==++===++==####=-.:==#=            
-=+++==++====+====+=+=++===++===##    +#%==++==#%           #=+++==+++==++===++%%=#%++=++++=+++%%#  
 ---++***++***++***++***++***==    =-=**+***%         +****++***++***++********++***++***+*==  
    =+=++===++===++=+=++===++++=++==*==   +++==++%      :=#===++===++===++++=++===++===++===++=+:.  
     =#++===++===++===++====+===+++==++===++=+==+++=+++==#%===++====+++=++====+===++===++%-.        
       :---****+***++********++****+**************+***++*#*+*****+****+****-*+--+*+------+.         
           ==+===++===++=+=++===++===++===++===++===++===++===++===++===+++%==::===:                
                 =##+==+===++=+=+++===+===+++==++===++===+++==++===+++==+*##:                       
                    ---::-**+-%***+*%#*++***+****++***++***++**+++***+*---                          
                          ==+:%=++++%*++==++++=++===++===++===++=+=++=+#                            
                              #-=*===+++==++++=++++==+===++====+%==#%                               
                               ---%+***+*****%********++****+****--=+                               
                                  %==++=+=+++%=+++==++===++===++=:                                  
                                   =###%=#=#===+++==++===#%+-:=#                                    
                                       +- =%+****+****++*#*-.                                       
                                          =%=+=++=+=++====+#                                        
                                           :*==# -+=++====+%                                        
                                            %%*+  ----+****+                                         
                                            %%=-  .#.:=+=++:                                        
                                            %=.         =#                                          
                                          :+%           -++                                         
                                      :*:+=+%=           :+:**-      :                              
\033[1;33m                              =***####%%%-*#%=%######%===++%%%%%##-*#=-                             
                              ##############################%#####%##+#=-                           
                           :+:##############################%#####%##=#--:                          
                              =###################################-+#=+                             
                                                                   =#++                             
                                                                  :=#==\033[0m      
"""

 
logging.basicConfig(level=logging.INFO) #funny to think that my code wasnt working because of this line lol
print(ascii_ar24re3)
time.sleep(0.5)
logging.info(Fore.YELLOW + "Welcome To Shellpy bind")
time.sleep(1)

while True:
    time.sleep(0.3)
    
    logging.info(Fore.YELLOW + "Do you want to Continue? " + Fore.CYAN + "\nType 1 to continue" + Fore.RED + "\nType 0 to exit" + Fore.GREEN + "\nType 2 to get info about Bind Shell(EN)"+"\nType 90 to get info about Bind Shell(ITA)")
    resp = input()

    if not resp:
        time.sleep(0.3)
        logging.info(Fore.RED + "No answer, sorry you must exit")
    elif resp == '1':  
        if __name__ == "__main__":
            sock = sockconn()
            sock.insertinfo()
    elif resp == '0':  
        time.sleep(0.3)
        logging.info(Fore.MAGENTA + "See you soon!")
        time.sleep(2)
        break
    elif resp == '2': 
        time.sleep(0.3) 
        logging.info(Fore.GREEN + kesf)
    elif resp == '90':
        time.sleep(0.3)
        logging.info(Fore.GREEN + prg)

    else:
        time.sleep(0.3)
        logging.info(Fore.RED + "Invalid input, please choose a valid option.")
        continue
