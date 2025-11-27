password_benar = "python123"
while True:
    password_input = input("Masukkan password: ")
    if password_input == password_benar:
        print("Password benar! Akses diberikan.")
        break
    else:
        print("Password salah. Coba lagi.")
