# Bu program Selim Eren Kaya tarafından yazılmıştır.

import dikdortgen as dd
import ucgen as ucg
import cember as cemb


def main():
    try:
        # İşlemleri yapılması istenilen şeklin numarasının girildiği kısım
        secim = int(input("İşlemini gerçekleştirmek istediğiniz şekil numarasını giriniz"
                          "\n1- Dikdörtgen"
                          "\n2- Üçgen"
                          "\n3- Çember"
                          "\nNumara = "))

        # Dikdörtgen seçimi için nesne ataması ve işlemleri
        if secim == 1:
            dortgen = dd.Dikdortgen("Dikdörtgen", 50, 30)
            print(dortgen)
            dortgen.sekil_ciz()

        # Üçgen seçimi için nesne ataması ve işlemleri
        elif secim == 2:
            ucgen = ucg.Ucgen("Üçgen", 30, 40, 50, 90, 37, 53)
            print(ucgen)
            ucgen.sekil_ciz()

        # Çember seçimi için nesne ataması ve işlemleri
        elif secim == 3:
            cember = cemb.Cember("Çember", 10)
            print(cember)
            cember.sekil_ciz()

        # Geçersiz değer girilince çalıştırlacak kısım
        else:
            print("Geçersiz işlem değeri girdiniz.")

    except Exception as exception:
        print(f"HATA! Yanlış değer girdiniz."
              f"\n{exception}")


main()
