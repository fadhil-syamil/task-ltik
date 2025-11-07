# Muhammad Fadhil As-Syamil
# 2502551
# 1A - Rekayasa Perangkat Lunak

print("="*50)
print("     SISTEM LOGIN SEDERHANA")
print("     MA AL-HIKMAH 2 CIREBON")
print("="*50)

username_benar = "alhikmahcirebon"
password_benar = "elhiq12345"

def tampilkan_header():
    print("\n" + "-"*50)
    print("           SILAKAN LOGIN")
    print("-"*50)

def input_kredensial():
    username = input("Username: ")
    password = input("Password: ")
    return username, password

def validasi_login(username, password):
    if username == username_benar and password == password_benar:
        return True
    return False

def proses_login():
    max_percobaan = 3
    percobaan = 0
    
    while percobaan < max_percobaan:
        tampilkan_header()
        user, pwd = input_kredensial()
        
        if validasi_login(user, pwd):
            print("\n" + "="*50)
            print("     ✓ LOGIN BERHASIL!")
            print(f"     Selamat datang, {user}!")
            print("="*50)
            return True
        else:
            percobaan += 1
            sisa = max_percobaan - percobaan
            
            if sisa > 0:
                print(f"\n✗ Username atau Password salah!")
                print(f"  Sisa percobaan: {sisa}")
            else:
                print("\n" + "="*50)
                print("     ✗ LOGIN GAGAL!")
                print("     Akun dikunci. Hubungi administrator.")
                print("="*50)
                
    return False

# Jalankan program
proses_login()