import socket
import ipaddress
import re

dozvoljeni_karakteri_ip = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

dozvoljeni_karakteri_port = re.compile("([0-9]+)-([0-9]+)")

najmanji_port = 0
najveci_port = 65535

otvoreni_portovi = []

print(r""".-')   .-. .-')     ('-.       .-') _        _  .-')     ('-.                      _ (`-.              _  .-')   .-') _                      (`-.      ('-.   
 ( OO ). \  ( OO )  _(  OO)     ( OO ) )      ( \( -O )   ( OO ).-.                 ( (OO  )            ( \( -O ) (  OO) )                   _(OO  )_  _(  OO)  
(_)---\_),--. ,--. (,------.,--./ ,--,' ,-.-') ,------.   / . --. /     ,--.       _.`     \ .-'),-----. ,------. /     '._  .-'),-----. ,--(_/   ,. \(,------. 
/    _ | |  .'   /  |  .---'|   \ |  |\ |  |OO)|   /`. '  | \-.  \  .-')| ,|      (__...--''( OO'  .-.  '|   /`. '|'--...__)( OO'  .-.  '\   \   /(__/ |  .---' 
\  :` `. |      /,  |  |    |    \|  | )|  |  \|  /  | |.-'-'  |  |( OO |(_|       |  /  | |/   |  | |  ||  /  | |'--.  .--'/   |  | |  | \   \ /   /  |  |     
 '..`''.)|     ' _)(|  '--. |  .     |/ |  |(_/|  |_.' | \| |_.'  || `-'|  |       |  |_.' |\_) |  |\|  ||  |_.' |   |  |   \_) |  |\|  |  \   '   /, (|  '--.  
.-._)   \|  .   \   |  .--' |  |\    | ,|  |_.'|  .  '.'  |  .-.  |,--. |  |       |  .___.'  \ |  | |  ||  .  '.'   |  |     \ |  | |  |   \     /__) |  .--'  
\       /|  |\   \  |  `---.|  | \   |(_|  |   |  |\  \   |  | |  ||  '-'  /       |  |        `'  '-'  '|  |\  \    |  |      `'  '-'  '    \   /     |  `---. 
 `-----' `--' '--'  `------'`--'  `--'  `--'   `--' '--'  `--' `--' `-----'        `--'          `-----' `--' '--'   `--'        `-----'      `-'      `------' """)

while True:
    uneta_ip_adresa = input("\nMolimo unesite IP adresu cije portove zelite skenirati: ")
    if dozvoljeni_karakteri_ip.search(uneta_ip_adresa):
        print(f"{uneta_ip_adresa} je validna ip adresa")
        break

while True:
    
    print("Molimo unesite zeljeni raspon portova u formatu <int>-<int> primer(20-25)")
    raspon_portova = input("Unesi raspon portova: ")
    validacija_raspona_portova = dozvoljeni_karakteri_port.search(raspon_portova.replace(" ",""))
    if validacija_raspona_portova:
        najmanji_port = int(validacija_raspona_portova.group(1))
        najveci_port = int(validacija_raspona_portova.group(2))
        break


for port in range(najmanji_port, najveci_port + 1):
    
    try:
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
            s.settimeout(0.5)
            
            s.connect((uneta_ip_adresa, port))
            
            otvoreni_portovi.append(port)

    except:
        
        pass


for port in otvoreni_portovi:
    
    print(f"Port {port} je otvoren na adresi: {uneta_ip_adresa}.")




