import os
import subprocess
import time
cmd = os.system
#change your path dir here
path = '/home/user/Desktop/ESD'


def ewt():
    cmd('clear')
    
    print("""
        _       _ _   _       _ _             _ 
       (_)_ __ (_) |_(_) __ _| (_)_______  __| |
       | | '_ \| | __| |/ _` | | |_  / _ \/ _` |
       | | | | | | |_| | (_| | | |/ /  __/ (_| |
       |_|_| |_|_|\__|_|\__,_|_|_/___\___|\__,_|
          """)
    print("Checking Dir")
    Isexists = os.path.exists(path)
    
    if Isexists == True:
        print("OK")
        
        print("App Server is starting at port 3000")
          
        try:
            subprocess.call('~/Desktop/ESD/ewt.sh' , shell=True , executable="/usr/bin/bash")  
        except KeyboardInterrupt:
            cmd('clear')
            print("restarting the app luncher.")  
            main()
    else:
        print("Dir is not found")
        main()


def st():
    cmd('clear')
    
    print("""
        _       _ _   _       _ _             _ 
       (_)_ __ (_) |_(_) __ _| (_)_______  __| |
       | | '_ \| | __| |/ _` | | |_  / _ \/ _` |
       | | | | | | |_| | (_| | | |/ /  __/ (_| |
       |_|_| |_|_|\__|_|\__,_|_|_/___\___|\__,_|
          """)
    print("Checking Dir")
    Isexists = os.path.exists(path)
    
    if Isexists == True:
        print("OK")
        
        print("App Server is starting at port 3000")          
        try:                       
            subprocess.call('~/Desktop/ESD/s.sh' , shell=True , executable="/usr/bin/bash")
        except KeyboardInterrupt:
            cmd('clear')
            print("restarting the app luncher.")  
            main()
    else:
        print("Dir is not found")
        main()
        
def dt():
    cmd('clear')
    
    print("""
        _       _ _   _       _ _             _ 
       (_)_ __ (_) |_(_) __ _| (_)_______  __| |
       | | '_ \| | __| |/ _` | | |_  / _ \/ _` |
       | | | | | | |_| | (_| | | |/ /  __/ (_| |
       |_|_| |_|_|\__|_|\__,_|_|_/___\___|\__,_|
          """)
    cmd('clear')
    time.sleep(0.3)
    print("Checking Dir")
    Isexists = os.path.exists(path)
    
    if Isexists == True:
        print("OK")
        
        print("App Server is starting at port 3000")
        try:
            subprocess.call('~/Desktop/ESD/d.sh' , shell=True , executable="/usr/bin/bash")
        except KeyboardInterrupt:
            cmd('clear')
            print("restarting the app luncher.")  
            main()
    else:
        print("Dir is not found")
        main()


def main():
    print(""" 
          _                  _                  _               
         / \   _ __  _ __   | |_   _ _ __   ___| |__   ___ _ __ 
        / _ \ | '_ \| '_ \  | | | | | '_ \ / __| '_ \ / _ \ '__|
       / ___ \| |_) | |_) | | | |_| | | | | (__| | | |  __/ |   
      /_/   \_\ .__/| .__/  |_|\__,_|_| |_|\___|_| |_|\___|_|   
              |_|   |_|                                    
      
      
      """)


    print("1 :: ESP_Web_Tool")

    print("2 :: ESP_Serial_terminal")

    print("3 :: Duckify_Tool")
    chose = int(input("Enter app number :: "))
        
    if chose == 1:
        ewt()
    elif chose == 2:
        st()
    elif chose == 3:
        dt()
    else:
        print("fail")
main()
