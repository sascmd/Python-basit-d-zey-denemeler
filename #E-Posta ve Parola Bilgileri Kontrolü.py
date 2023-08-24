#E-Posta ve Parola Bilgileri Kontrolü
print("Sitemize Hoşgeldiniz.Lütfen E-posta ve şifrenizi giriniz:")
kayıt_e_mail=(input("Lütfen Kayıt için e-mail adresinizi giriniz:"))
kayıt_şifre=(int(input("Lütfen Kayıt için Şifrenizi giriniz:")))
seçim=input("Tekrar girmek için (p) tuşuna basınız:")
email=kayıt_e_mail
şifre=kayıt_şifre
if seçim=="p":
    email=(input("Lütfen e-mail adresinizi giriniz:"))
şifre=(int(input("Lütfen Şifrenizi giriniz:")))
if email==kayıt_e_mail and şifre==kayıt_şifre:
    print("Giriş doğrulandı\nHoşgeldiniz")
else:
    print("Giriş işlemi başarısız\nTekrar giriniz")