"""
Semua sintaksis dasar pemrograman terdiri dari
1. sekuesnsial : langkah berurutan
2. percabangan : langkah melompat jika kondisi terpenuhi
3. perulangan : mengulang langkah yang sama berkali-kali sampai kondisi terpenuhi
"""
# Sekuensial
"""
print('Ibu berkata, "Pergilah ke toko"')
print('anak menjawab, "apa yang harus saya lakukan?"')
print('Ibu berkata lagi "Belilah 6 botol susu, jika ada telor belilah 6"')
print("Maka budi berangkat ke toko")
print("dan mulai berbelanja")
"""

# Percabangan
jumlah_botol_susu = 1
jumlah_telur = 6
print("budi mengecek stok susu dan telur")
print(f"jumlah susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("budi membeli 1 botol susu")
    if jumlah_telur > 5:
        print("dan membeli 6 butir telur")
    else:
        print("tidak membeli telur")
else:
    print("budi tidak membeli susu")

print("budi pulang kerumah")