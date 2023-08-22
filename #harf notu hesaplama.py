#harf notu hesaplama
öğrenci_adı=input("Adınızı Giriniz:")
öğrenci_numarası=int(input("Öğrenci Numaranızı Giriniz:"))
#ortalamahesaplamayöntemi
vize_notu=int(input("Vize Sonucunu Giriniz:"))
final_notu=int(input("Final Sonucunu Giriniz:"))
ortalama=(vize_notu)*(4/10)+(final_notu)*(6/10)
#puankarşılığıharfnotu
if ortalama>=90:
    print("Harf Notunuz:AA,Başarıyla Geçtiniz")
elif ortalama>=85 and ortalama<90:
    print("Harf Notunuz:Ba,Başarıyla Geçtiniz")
elif ortalama>=80 and ortalama<85:
    print("Harf Notunuz:BB,Başarıyla Geçtiniz")
elif ortalama>=75 and ortalama<80:
    print("Harf Notunuz:CB,Başarıyla Geçtiniz")
elif ortalama>=70 and ortalama<75:
    print("Harf Notunuz:CC,Başarıyla Geçtiniz")
elif ortalama>=65 and ortalama<70:
    print("Harf Notunuz:DC,Sorumlu Geçtiniz")
elif ortalama>=60 and ortalama<65:
    print("Harf Notunuz:DD,Sorumlu Geçtiniz")
elif ortalama>=55 and ortalama<60:
    print("Harf Notunuz:FD,Kaldınız")
else:
    print("Harf Notunuz:FF,Kaldınız")