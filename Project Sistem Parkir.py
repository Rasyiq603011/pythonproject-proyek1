# Nama File : Project Sistem Parkir.property
# tanggal : 18 Februari 2025
# Pembuat : Cipta Haidar, Muhammad Arravi, Muhammad Nabil, Diaz Putri


# input data 
def inputKendaraan():
    
    return Tipe

def lamaParkir():
    lama =  int(input("Waktu parkir(jam): "))
    return lama
    
def platKendaraan():
    plat = input("Masukkan plat nomor kendaraan: ")
    return plat

def jenisKendaraan():
    cek = True
    while(cek):
        kendaraan = input("Masukkan jenis kendaraan(A:Motor, B:Mobil, C:Truk): ")
        if kendaraan == 'A':
            print("Kendaraan : Motor")
        elif kendaraan == 'B':
            print("Kendaraan : Mobil")
        elif kendaraan == 'C':
            print("Kendaraan : Truk")
        else:
            print("Jenis kendaraan tidak valid!")

    return kendaraan

# hitung biaya
def biaya_parkir(Tipe, lama):
    biaya = 0 
    if Tipe.lower() == 'motor': 
        biaya = 2000  
        if lama > 1:
            biaya += (lama - 1) * 2500  
    elif Tipe.lower() == 'mobil':
        biaya = 5000  
        if lama > 1:
            biaya += (lama - 1) * 5500
    elif Tipe.lower() == 'truk':
        biaya = 7000  
        if lama > 1:
            biaya += (lama - 1) * 7500
    else:
        return "Jenis kendaraan tidak valid"
    return biaya

# display
def display(Tipe, platnomor, lama, total_biaya):
    print("Modul Display")
    print("Jenis Kendaraan  : ", Tipe)
    print("Nomor Plat       : ", platnomor)  
    print("Lama Parkir      : ", lama, "jam")
    print("Total Biaya      : Rp.", total_biaya)

# safe data
def savedata(TipeKendaraan, lamaMasuk, nomorpolisi, harga):
    f = open("Data parkir.txt","a")
    f.write(
            "Data Parkir\n"
            "Tipe Kendaraan : " + TipeKendaraan +
            "\nNomor Polisi   : " + nomorpolisi +
            "\nLama Parkir    : " + lamaMasuk  +
            "\nBiaya parkir   : " + harga +
            "\n\n"
            )
    f.close()

run = True

while(True):
    Tipe = inputKendaraan()
    lama = lamaParkir()
    plat = platKendaraan()

    jenisKendaraan(Tipe)


    biaya = biaya_parkir(Tipe, lama)
    print(f"Biaya Parkir: Rp{biaya}")





savedata(Tipe, lama, platnomor, "12.000" )

f = open("Data parkir.txt","r")
print(f.read())
f.close()
