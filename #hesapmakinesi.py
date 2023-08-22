#hesapmakinesi
değer1=int(input("Rakam giriniz:"))
işlem=input("İşlem giriniz:")
değer2=int(input("Rakam giriniz:"))
toplama=değer2+değer1
çıkarma=değer1-değer2
bölme=değer1/değer2
çarpma=değer2*değer1
if işlem=="+":
    print(toplama)
if işlem=="-":
    print(çıkarma)
if işlem=="/":
    print(bölme)
if işlem=="*":
    print(çarpma)