#chatbot
list_sorular = ["Nasılsın", "Adın Ne:", "Yaşın Kaç"]
list_cevaplar = ["İyiyim", "Uğur", 30]

seçenek = input("Bir soru seçiniz (Nasılsın / Adın Ne: / Yaşın Kaç): ")

if seçenek == "Nasılsın":
    print(list_cevaplar[0])
elif seçenek == "Adın Ne:":
    print(list_cevaplar[1])
elif seçenek == "Yaşın Kaç":
    print(list_cevaplar[2])
else:
    print("BU NE SİKİK SORU")
