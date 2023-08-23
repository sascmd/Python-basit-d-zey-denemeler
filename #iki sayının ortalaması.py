#iki sayının ortalaması
sayı=int(input("Bir sayı giriniz:"))
sayı_2=int(input("Diğer Bir sayı giriniz:"))
ortalama=float(sayı+sayı_2)/2
seçim=input("Ortalama almak için o tuşuna basınız:")
if seçim=="o":
    print(ortalama)