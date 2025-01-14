from colr import color
import displaywarna
# Example
# print(color('Hello there.', fore='00ffff', back='000'))
# print(color('Hello there.', fore=(255, 0, 0), back=(0, 0, 0)))


def generate():
    gabungwarna = ""
    contohnama = input("Nama anda adalah : ")
    # Data awal untuk pengaturan warna
    data = {
        "huruf": "",
        "kodewarna": [255, 0, 0],
        "mode": 1,
        "kodewarnaCPM": ""
    }

    while True:
        tanya = input("Mulai dari warna apa? [merah/hijau/biru/kuning/cyan/magenta] : ").lower()
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
        elif tanya == "magenta":
            data["kodewarna"] = [255, 0, 255]
            break
        else:
            print("Harus sesuai pilihan warna yang tersedia!")

    for huruf in contohnama:
        while True:
            # Penambahan warna dalam siklus
            tambah = 40
            if data["mode"] == 1:  # Merah ke kuning
                if data["kodewarna"][1] + tambah <= 255:
                    data["kodewarna"][1] += tambah
                    break
                else:
                    data["mode"] += 1
            elif data["mode"] == 2:  # Kuning ke hijau
                if data["kodewarna"][0] - tambah >= 0:
                    data["kodewarna"][0] -= tambah
                    break
                else:
                    data["mode"] += 1
            elif data["mode"] == 3:  # Hijau ke cyan
                if data["kodewarna"][2] + tambah <= 255:
                    data["kodewarna"][2] += tambah
                    break
                else:
                    data["mode"] += 1
            elif data["mode"] == 4:  # Cyan ke biru
                if data["kodewarna"][1] - tambah >= 0:
                    data["kodewarna"][1] -= tambah
                    break
                else:
                    data["mode"] += 1
            elif data["mode"] == 5:  # Biru ke magenta
                if data["kodewarna"][0] + tambah <= 255:
                    data["kodewarna"][0] += tambah
                    break
                else:
                    data["mode"] += 1
            elif data["mode"] == 6:  # Magenta ke merah
                if data["kodewarna"][2] - tambah >= 0:
                    data["kodewarna"][2] -= tambah
                    break
                else:
                    data["mode"] = 1

        # Gabungkan huruf dengan warna
        gabungwarna += color(
            huruf,
            fore=(data["kodewarna"][0], data["kodewarna"][1], data["kodewarna"][2]),
            back=(0, 0, 0)
        )

        # Generate kode warna untuk CPM
        kodas = []
        for t in range(3):
            clrcode = hex(data["kodewarna"][t])[2:]
            if len(clrcode) == 1:
                clrcode = "0" + clrcode
            kodas.append(clrcode)
        data["kodewarnaCPM"] += f"[{kodas[0]}{kodas[1]}{kodas[2]}]{huruf}"

    print(f"Hasil\t: {displaywarna.disp(data['kodewarnaCPM'])}")
    print(f"Kode\t: {data['kodewarnaCPM']}")
    return data["kodewarnaCPM"]
