# Menampilkan kontak Ari
a = {'Ari': 6281267888, 'Dina': 6287677776}
print("Kontak Ari:", a['Ari'])

# Menambah kontak
a["Riko"] = "6287654544"
print("Kontak:", a)

# Ubah kontak Dina
a['Dina'] = "6288999776"
print("Kontak:", a)

# Menampilkan semua nama
print(a.keys())

# Menampilkan semua nomor
print(a.values())

# Menampilkan daftar nama dan nomornya
print(a.items())

# Hapus kontak Dina
del a["Dina"]
print("Kontak:", a)
