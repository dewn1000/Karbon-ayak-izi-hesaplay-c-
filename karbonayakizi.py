print("Karbon ayak izi hesaplama aracı")
print("İstenilen bilgileri gir")
elektrik_f = int(input("Aylık elektrik faturanız nedir?"))
dogalgaz_f = int(input("Aylık doğalgaz faturanız nedir?"))
petrol_f = int(input("Aylık petrol faturanız nedir?"))
toplam_km = int(input("Arabanızdaki (yıllık) toplam kilometreniz nedir?"))
ucus = int(input("Geçen yıl kaç uçuş yaptınız?"))
ucus_s = int(input("Son bir yıl içinde kaç uçuş yaptınız"))
gazete = str(input("Gazetelerinizi geri dönüştürüyor musunuz?"))
aluminium = str(input("Alüminyum ve tenekeleri geri dönüştürüyor musunuz"))

karbon_ayak_izi = (elektrik_f * 105 + dogalgaz_f * 105 + petrol_f * 113 + toplam_km * 0.79 + ucus * 1100 + ucus_s * 4400)
if gazete == "hayır":
    karbon_ayak_izi = karbon_ayak_izi + 184
if aluminium == "hayır":
    karbon_ayak_izi = karbon_ayak_izi + 166

if karbon_ayak_izi > 22000:
    print("Karbon ayak iziniz:", karbon_ayak_izi)
    print("Çok yüksek!")
if karbon_ayak_izi < 22000:
    if karbon_ayak_izi > 16000:
        print("Karbon ayak iziniz:", karbon_ayak_izi)
        print("ortalama")
if karbon_ayak_izi < 16000:
    if karbon_ayak_izi > 6000:
        print("Karbon ayak iziniz:", karbon_ayak_izi)
        print("Düşük")
        if karbon_ayak_izi < 6000:
            print("Karbon ayak iziniz:", karbon_ayak_izi)
            print("Çok düşük")