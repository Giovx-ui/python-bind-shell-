import logging, time
from colorama import init, Fore
from cost2 import sockconn

# Initialize colorama for colored output
init()

# Welcome message
kesf = """My tool is a bind shell that allows a client to connect to a server via port 443. However, before the connection can be established, the target must already be listening on port 443.\n If the target isn't configured to listen, the target will need to run the script I created, called revshell.py, which will start listening on port 443, enabling the client connection.

This tool is fully modifiable and can be adapted to the user's needs.\n Please note that I take no responsibility for any misuse of the tool. It was created for ethical purposes and learning. If you have any questions or need support, feel free to contact me. In case of any errors, please forgive me as I am not an expert, and the code is still being updated weekly.
"""

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

# Configure logging to handle info and error levels
logging.basicConfig(level=logging.INFO)
print(ascii_ar24re3)
time.sleep(0.5)
logging.info(Fore.YELLOW + "Welcome To Shellpy bind")
time.sleep(1)

while True:
    time.sleep(0.3)
    # Prompt user for input
    logging.info(Fore.YELLOW + "Do you want to Continue? " + Fore.CYAN + "\nType 1 to continue" + Fore.RED + "\nType 0 to exit" + Fore.GREEN + "\nType 2 to get info about Bind Shell")
    resp = input()

    if not resp:
        time.sleep(0.3)
        logging.info(Fore.RED + "No answer, sorry you must exit")
    elif resp == '1':  # Comparing as string
        if __name__ == "__main__":
            sock = sockconn()
            sock.insertinfo()
    elif resp == '0':  # Comparing as string
        time.sleep(0.3)
        logging.info(Fore.MAGENTA + "See you soon!")
        break
    elif resp == '2': 
        time.sleep(0.3) 
        logging.info(Fore.GREEN + kesf)
    else:
        time.sleep(0.3)
        logging.info(Fore.RED + "Invalid input, please choose a valid option.")
