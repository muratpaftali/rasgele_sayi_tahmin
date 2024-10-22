import random as rd
rasgele_sayi = rd.randint(1,100)
tahmin_sayaci = 0
print("Tuttuğum sayıyı tahmin et ")
while True:
    tahmin = int(input("Tahmininiz Nedir YAZ  :"))
    tahmin_sayaci += 1
    if tahmin < rasgele_sayi:
        print("Daha büyük Bir sayı Tahmin et ")
    elif tahmin > rasgele_sayi:
        print("Daha küçük bir sayı tahmin et ")
    else:
        print(f"Tebrikler rasgele olan {rasgele_sayi}  sayısını {tahmin_sayaci} kerede buldunuz ")
        break
