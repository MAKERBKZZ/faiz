from colr import color
import displaywarna

def generate():
    gabungwarna = ""
    contohnama = input("Nama anda adalah: ")

    # Inisialisasi data
    data = {
        "huruf": "",
        "kodewarna": [255, 0, 0],
        "mode": 1,
        "kodewarnaCPM": ""
    }

    while True:
        tanya = input("Mulai dari warna apa? [merah/hijau/biru/kuning/cyan/ungu/putih/magenta/oranye]: ")
        if tanya == "merah":
            data["kodewarna"] = [255, 0, 0]
            break
        elif tanya == "hijau":
            data["kodewarna"] = [0, 255, 0]
            break
        elif tanya == "biru":
            data["kodewarna"] = [0, 0, 255]
            break
        elif tanya == "kuning":
            data["kodewarna"] = [255, 255, 0]
            break
        elif tanya == "cyan":
            data["kodewarna"] = [0, 255, 255]
            break
        elif tanya == "ungu":
            data["kodewarna"] = [255, 0, 255]
            break
        elif tanya == "putih":
            data["kodewarna"] = [255, 255, 255]
            break
        elif tanya == "magenta":
            data["kodewarna"] = [255, 0, 255]
            break
        elif tanya == "oranye":
            data["kodewarna"] = [255, 165, 0]
            break
        else:
            print("Harus sesuai pilihan warna..!")

    for huruf in contohnama:
        while True:
            tambah = 45
            if data["mode"] == 1:
                if data["kodewarna"][1] + tambah <= 255:
                    data["kodewarna"][1] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [255, 255, 0]
            elif data["mode"] == 2:
                if data["kodewarna"][0] - tambah >= 0:
                    data["kodewarna"][0] -= tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 255, 0]
            elif data["mode"] == 3:
                if data["kodewarna"][2] + tambah <= 255:
                    data["kodewarna"][2] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 255, 255]
            elif data["mode"] == 4:
                if data["kodewarna"][1] - tambah >= 0:
                    data["kodewarna"][1] -= tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 0, 255]
            elif data["mode"] == 5:
                if data["kodewarna"][0] + tambah <= 255:
                    data["kodewarna"][0] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [255, 0, 255]
            elif data["mode"] == 6:
                if data["kodewarna"][2] - tambah >= 0:
                    data["kodewarna"][2] -= tambah
                    break
                else:
                    data["mode"] = 1
                    data["kodewarna"] = [255, 0, 0]

        gabungwarna += color(huruf,
                             fore=(data["kodewarna"][0],
                                   data["kodewarna"][1],
                                   data["kodewarna"][2]),
                             back=(0, 0, 0))
        # Dapatkan kode warna dalam format hex
        clrcode = "".join(f"{x:02x}" for x in data["kodewarna"])
        data["kodewarnaCPM"] += f"[{clrcode}]{huruf}"

    # Cetak hasil dan kode warna
    print(f"hasil\t:  {displaywarna.disp(data['kodewarnaCPM'])}")
    print(f"kode\t:  {data['kodewarnaCPM']}")
    
    return data["kodewarnaCPM"]


