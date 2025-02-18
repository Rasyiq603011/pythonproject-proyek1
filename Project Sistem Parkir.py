# Nama File : Project Sistem Parkir.property
# tanggal : 18 Februari 2025
# Pembuat : Cipta Haidar, Muhammad Arravi, Muhammad Nabil, Diaz Putri


# input data 
# def input():
#     cek = True
#     while(cek):
#         Jenis = input("Masukan Jenis Kendaraan (Mobil atau Motor) : ")
#         Masuk = input("Waktu Masuk : ")        
#         Keluar = input("Waktu Keluar : ")

Tipe = input("Masukan Jenis Kendaraan (Mobil atau Motor) : ")
lama = input("Lama Masuk : ")
platnomor = input("Masukan plat nomor : ")


# hitung biaya
def biaya_parkir(jenis_kendaraan, lama):
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
    
biaya = biaya_parkir(Tipe, lama)
print(f"Biaya Parkir: Rp{biaya}")


# display


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

savedata(Tipe, lama, platnomor, "12.000" )

f = open("Data parkir.txt","r")
print(f.read())
f.close()
