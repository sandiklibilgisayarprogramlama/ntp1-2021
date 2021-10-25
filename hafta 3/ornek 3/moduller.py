# -*- coding: UTF-8 -*-

import psutil

def ram_yeterlimi(ihtiyac_olan_ram):
    
    bilgisayar_ram=psutil.virtual_memory().total
    # pip install psutil
    if ihtiyac_olan_ram<bilgisayar_ram:
        print("Program çalışır")
    else:
        print("ram miktarı yeterli değil")


ram_yeterlimi(8000)