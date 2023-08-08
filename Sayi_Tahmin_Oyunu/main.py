# Bu program Selim Eren Kaya tarafından yazılmıştır.

import random  # rastgele sayı üretme kütüphanesini çağırdığım kısım

rekor = 999
tahmin = 0
tahmin_sayaci = 0
oyun_devam = "e"
print("Sayı Tahmini oyununa hoşgeldiniz.")
while oyun_devam == "e" or oyun_devam == "E":
    sayi = random.randint(1, 100)  # rastgele sayı üretilen kısım
    while sayi != tahmin:  # tahmin yanlışsa çalıştırılacak kısım
        tahmin = int(input("Sayıyı bulmak için lütfen tahmin ediniz: "))
        if 1 <= tahmin <= 100:  # sayının 1 ile 100 arasında mı diye kontrol edildiği kısım
            if tahmin < sayi:  # tahmin sayıdan küçükse verilecek ipucu
                tahmin_sayaci += 1
                print("Daha büyük sayı")
            elif tahmin > sayi:  # tahmin sayıdan büyükse verilecek ipucu
                tahmin_sayaci += 1
                print("Daha küçük sayı")
        else:
            print("1-100 arasında geçerli bir değer girin lütfen.")
    else:  # tahmin doğruysa çalıştırılacak kısım
        tahmin_sayaci += 1
        print(f"Sayıyı doğru bildiniz tebrikler.\nSayı= {sayi}\nTahmin sayınız= {tahmin_sayaci}")
        if tahmin_sayaci <= rekor:  # rekorun atandığı kısım
            rekor = tahmin_sayaci
        # oyuna devam edilsin mi diye sorulan kısım
        oyun_devam = input("\nOyuna devam etmek için e/E bitirmek için h/H giriniz: ")
else:
    print(f"Oyun bitmiştir. Oyundaki en başarılı tahmin rekoru= {rekor}")
