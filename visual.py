#!/bin/python3

from datetime import datetime

class visual:
    @staticmethod
    def opening():
        print('''
                   _ ______ ____           
                  | |  ____|  _ \   /\     
                  | | |__  | |_) | /  \    
              _   | |  __| |  _ < / /\ \   
             | |__| | |____| |_) / ____ \  
              \____/|______|____/_/  _ \_\ 
              / ____|/ ____|   /\   | \ | |
             | (___ | |       /  \  |  \| |
              \___ \| |      / /\ \ | . ` |
              ____) | |____ / ____ \| |\  |
             |_____/ \_____/_/    \_\_| \_|
                 ''')
    @staticmethod
    def lines():
        print('-' * 50)

    @staticmethod
    def banner(target):
        visual.lines()
        print(f"Escaneando o endereço: {target}")
        print(f"Início: {str(datetime.now())}")
        visual.lines()
