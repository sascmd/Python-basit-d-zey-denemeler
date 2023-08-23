#iki sayıdan küçük olanı bulma
komut=int(input("bir sayı gir(A):"))
komut_2=int(input("diğer sayıyı gir(B):"))
if komut<komut_2:
    print("A sayısı Küçük Olandır")
if komut_2<komut:
    print("B sayısı Küçük olandır")
else:
    print("İki sayı birbirine eşittir")