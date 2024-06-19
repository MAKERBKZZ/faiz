import os
import json



def cariurutan(cariid):
    with open('nomer_car.json', 'r', encoding='utf-8') as openfile:
        data = json.load(openfile)
    for mydatacar in data["result"]:
        if mydatacar["id"] == cariid:
            return mydatacar["urutan"]
    
            
dir_list = os.listdir("cpm/cars/livery/")
dir_list.sort(key=int)
hsil={}
for idcar in dir_list:
    if "_" not in idcar:
        with open(f'cpm/cars/livery/{idcar}', 'r', encoding='utf-8') as openfile:
            datacar = json.load(openfile)
        asdf=cariurutan(idcar)
        if type(asdf)!=int:
            asdf=999
        hsil[idcar]={
            "urutan":asdf,
            "id":idcar,
            "itrlivery":1
        }
        # print(f"{idcar}\t:{hsil[idcar]['itrlivery']}")
    else:
        idcar=idcar.split("_")[0]
        hsil[idcar]['itrlivery']+=1
        # print(f"{idcar}\t:{hsil[idcar]['itrlivery']}   <- tambahan {hsil[idcar]}")

for tk in hsil:
    print(f'ID {hsil[tk]["id"]} ada {hsil[tk]["itrlivery"]} livery [No.{cariurutan(hsil[tk]["id"])}]')

