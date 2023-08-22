#kimlikdoğrulama
#kayıt
kayıt_adı=input("Kayıt için adınızı giriniz:")
kayıt_soyadı=input("Kayıt için soyadınızı giriniz:")
kayıt_tcno=int(input("Kayıt için T.C No giriniz:"))
#kayıtcheck
adı=kayıt_adı
soyad=kayıt_soyadı
tcno=kayıt_tcno
#kayıtkontrol
if input("Kayıt için adınızı giriniz:")==adı and input("Kayıt için soyadınızı giriniz:")==soyad and int(input("Kayıt için T.C No giriniz:"))==tcno:
    print("Giriş Onaylandı")
else:
    print("Giriş Onaylanmadı")