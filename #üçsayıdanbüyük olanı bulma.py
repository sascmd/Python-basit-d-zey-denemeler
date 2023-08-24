#üçsayıdanbüyük olanı bulma
ilk_sayı=int(input("İlk sayıyı giriniz(a):"))
ikinci_sayı=int(input("İkinci sayıyı giriniz(b):"))
üçüncü_sayı=int(input("Üçüncü sayıyı giriniz(c):"))
if ilk_sayı>ikinci_sayı and ilk_sayı>üçüncü_sayı:
    print("a en büyük sayıdır!")
elif ikinci_sayı>ilk_sayı and ikinci_sayı>üçüncü_sayı:
    print("b en büyük sayıdır!")
elif üçüncü_sayı>ilk_sayı and üçüncü_sayı>ikinci_sayı:
    print("c en büyük sayıdır")