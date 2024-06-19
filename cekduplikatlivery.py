import os
import json
import time


def cariurutan(cariid):
    with open('nomer_car.json', 'r', encoding='utf-8') as openfile:
        data = json.load(openfile)
    for mydatacar in data["result"]:
        if mydatacar["id"] == cariid:
            return mydatacar["urutan"]


while True:
    dir_list = os.listdir("cpm/cars/livery/")
    itrlivery = 1
    listUrutan = {}
    urutansebelumnya = 0
    dir_list.sort(key=len)
    backup = []
    for idnya in dir_list:
        with open(f'cpm/cars/livery/{idnya}', 'r', encoding='utf-8') as openfile:
            data = json.load(openfile)
        bersiapbackup = f'{data["data"]["CarID"]}{data["data"]["texts"]}'
        # print(bersiapbackup)
        if bersiapbackup not in backup:
            backup.append(bersiapbackup)
        else:
            print(f"Duplikat terdeteksi {idnya}")
            os.remove(f"cpm/cars/livery/{idnya}")
    print("Syudah")
    time.sleep(100)
