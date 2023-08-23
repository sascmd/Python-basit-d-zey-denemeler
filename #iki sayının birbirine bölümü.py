#iki sayının birbirine bölümü
sayı=int(input("Bir sayı giriniz(A):"))
sayı_2=int(input("Diğer Bir sayı giriniz(B):"))
a_sayısının_b_sayısına_bölümü=int(sayı)/(sayı_2)
b_sayısının_a_sayısına_bölümü=int(sayı_2)/(sayı)
komut=input("Eğer A'yı B harfine bölmek istiyorsanız a harfine,B'yi A harfine bölmek istiyorsanız b harfine basınız:")
if komut=="a":
    print(a_sayısının_b_sayısına_bölümü)
if komut=="b":
    print(b_sayısının_a_sayısına_bölümü)