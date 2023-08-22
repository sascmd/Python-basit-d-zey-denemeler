def ortalama():
    def ortalamahesaplama(a, b):
        vize = a * (0.4)
        final = b * (0.6)
        ort = (vize + final)
        return ort  
    return ortalamahesaplama(60, 50)  
ortalama_sonuc = ortalama()
print("Ortalama:", ortalama_sonuc)
