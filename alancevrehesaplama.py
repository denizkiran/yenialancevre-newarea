def ana_menu():
    while True:
        print("Hoşgeldiniz,lütfen kullanmak istediğiniz şekili seçiniz.")
        print("1. Kare")
        print("2. Dikdörtgen")
        print("3. Üçgen")
        print("4. Çember")
        print("5. Çıkış")
        secim = input("Lütfen seçim yapınız: ")


        if secim == '1':
            kare()

        elif secim == '2':
            dikdortgen()

        elif secim == '3':
            ucgen()

        elif secim == '4':
            cember()

        elif secim == '5':
            print("İşlem sonlandırılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyiniz.")
def kare():
    kenarkk = int(input("Lütfen karenin kenar uzunluğunu giriniz: "))
    print(f"Kenar uzunluklarını girdiğiniz karenin alanı: '{kenarkk*kenarkk}' olarak bulunmuştur.")
    print(f"Kenar uzunluklarını girdiğiniz karenin çevresi: '{kenarkk*4}' olarak bulunmuştur.")


def dikdortgen():
    kenardk = int(input("Lütfen dikdörtgenin ilk kenarın uzunluğunu giriniz: "))
    kenardk2 = int(input("Lütfen dikdörtgenin ikinci kenarın uzunluğunu giriniz: "))
    print(f"Kenar uzunluklarını girdiğiniz dikdörtgenin alanı: '{kenardk*kenardk2}' olarak bulunmuştur.")
    print(f"Kenar uzunluklarını girdiğiniz dikdörtgenin çevresi: '{kenardk*2+kenardk2*2}' olarak bulunmuştur")
    if kenardk == kenardk2:
        print("Bu dikdörtgen karedir.")



def ucgen():
    ucgenk1 = int(input("Lütfen üçgenin ilk kenarın uzunluğunu giriniz: "))
    ucgenk2 = int(input("Lütfen üçgenin ikinci kenarın uzunluğunu giriniz: "))
    taban = int(input("Lütfen üçgenin taban uzunluğunu giriniz: "))
    yukseklik = int(input("Lütfen üçgenin yüksekliğini giriniz: "))
    print(f"Kenar uzunluklarını girdiğiniz üçgenin alanı: '{taban*yukseklik/2}' olarak bulunmuştur")
    print(f"Kenar uzunluklarını girdiğiniz üçgenin çevresi: '{ucgenk1+ucgenk2+taban}' olarak bulunmuştur")
    if ucgenk2 == ucgenk1 == taban:
        print("Bu üçgen eşkenar üçgendir.")

def cember():
    pi = 3.14159
    r = int(input("Lütfen çemberin yarıçapını giriniz: "))
    print(f"Yarıçapı girdiğiniz çemberin alanı: '{pi*r*r}' olarak bulunmuştur")
    print(f"Yarıçapı girdiğiniz çemberin çevresi: '{2*pi*r}' olarak bulunmuştur")

ana_menu()



