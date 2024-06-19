import json
import os


dir_list = os.listdir("player/cars/")
itrlivery = 1
listUrutan = {}
while True:
    ygdicari = input("text di vynil yang di cari : ")
    for idnya in dir_list:
        with open(f'player/cars/{idnya}', 'r', encoding='utf-8') as openfile:
            data = json.load(openfile)
        if ygdicari in str(data):
            # print(json.dumps(data))
            print(idnya)
