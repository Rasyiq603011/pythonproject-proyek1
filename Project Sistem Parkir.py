# Nama File : Project Sistem Parkir.property
# tanggal : 18 Februari 2025
# Pembuat : Cipta Haidar, Muhammad Arravi, Muhammad Nabil, Diaz Putri

#Package
import os
import time 

#================ Method ======================
# input data 
def lamaParkir(): #input lama waktu parkir
    lama =  int(input("Waktu parkir(jam): "))
    return lama
    
def platKendaraan(): #input plat nomor kendaraan
    plat = input("Masukkan plat nomor kendaraan: ")
    return plat

def inputKendaraan():
    while(True):
        Code = input("Masukkan jenis kendaraan(A:Motor, B:Mobil, C:Truk): ")
        if Code == 'A': # melakukan Penghubung kode denagn jenis kendaraannya
            print("Kendaraan : Motor")
            kendaraan = "motor"
            break
        elif Code == 'B':
            print("Kendaraan : Mobil")
            kendaraan = "mobil"
            break
        elif Code == 'C':
            print("Kendaraan : Truk")
            kendaraan = "truk"
            break
        else:
            print("Jenis kendaraan tidak valid!")

    return kendaraan #mereturn jenis kendaraannya

# hitung biaya
def biaya_parkir(Tipe, lama): #Hitung biaya parkir
    biaya = 0 
    if Tipe.lower() == 'motor': 
        biaya = 2000  # ketika kurang dari sama dengan 1 jam
        if lama > 1: #ketika lebih dari 1 jam 
            biaya += (lama - 1) * 2500  
    elif Tipe.lower() == 'mobil':
        biaya = 5000  
        if lama > 1:
            biaya += (lama - 1) * 5500
    elif Tipe.lower() == 'truk':
        biaya = 7000  
        if lama > 1:
            biaya += (lama - 1) * 7500
    
    return biaya

# display
def display(Tipe, platnomor, lama, total_biaya): #mendisplay struk
    print("\n=================== STRUK ===================\n")
    print("Jenis Kendaraan  :", Tipe)
    print("Nomor Polisi     :", platnomor)  
    print("Lama Parkir      :", lama, "jam")
    print("Total Biaya      : Rp.", total_biaya)
    print("\n=================== STRUK ===================")

# safe data
def savedata(TipeKendaraan, lamaMasuk, nomorpolisi, harga):
    f = open("Data parkir.txt","a+")
    i = hitung_baris_kosong() + 1 #menentukan indeks data
    f.write(
            "Data Parkir " + f"{i}"+"\n"
            "Tipe Kendaraan : " + TipeKendaraan +
            "\nNomor Polisi   : " + nomorpolisi +
            "\nLama Parkir    : " + f"{lamaMasuk} jam"  +
            "\nBiaya parkir   : " + f"Rp.{harga}" +
            "\n\n"
            ) # menuliskan pada file
    f.close()

    print("\nData Berhasil disimpan !!!\n")
        
def hitung_baris_kosong():
    file = open("Data parkir.txt", "r")
    jumlah_kosong = 0  
        
    for baris in file:
        if baris.strip() == '':  # Jika baris kosong (hanya spasi atau tidak ada teks)
            jumlah_kosong += 1  
    file.close()
    return jumlah_kosong  # Mereturn jumlah baris kosong
 
def olahParkir(): #MOdul untuk mengolah data parkir
    while(True):
        os.system('cls')
        Tipe = inputKendaraan()
        lama = lamaParkir()
        plat = platKendaraan()

        biaya = biaya_parkir(Tipe, lama)
        display(Tipe, plat, lama, biaya )

        savedata(Tipe, lama, plat, biaya)

        lanjut = input("Tekan Q untuk kembali : ")
        if lanjut.upper().strip() == 'Q':
            break


#======================== Main Program =============================
while(True):
    os.system('cls')
    print("========== PILIHAN MENU ==========")
    print("1. Masukan Data Parkir")
    print("2. Lihat data parkir")
    print("3. Quit")
    try : # meminta input berupa angka
        opsi = int(input("Menu yang dipilih : "))
    except: # bila yang diinputkan bukan angka maka akan di ulang
        print("Input tidak valid! Harus berupa angka.")
        time.sleep(1) 
        continue

    if opsi not in [1, 2, 3]: # bila input bukan 1, 2, 3 maka akan meminta input ulang
        print("Pilihan tidak valid. Harap masukkan angka 1, 2, atau 3.")
        time.sleep(1)
        continue

    if(opsi == 1): # olah Parkir
        olahParkir()
    elif(opsi == 2): # Melihat data parkir
        while(True):
            os.system('cls')
            f = open("Data parkir.txt","r")
            print(f.read())
            f.close()
            lanjut = input("Tekan Q untuk kembali !")
            if lanjut.upper().strip() == "Q":
                break

    elif(opsi == 3): #quit
        print("Terima kasih telah menggunakan sistem parkir.")  
        time.sleep(1)  
        break
    else:
        continue



