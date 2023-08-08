import math
import sekil
import turtle


class Ucgen(sekil.Sekil):  # Üçgen şekli için oluşturduğum Subclass
    # Üçgen bilgilerini değişkenlere atayan metot
    def __init__(self, sekil_isim, ucgen_kenar1, ucgen_kenar2, ucgen_kenar3, ucgen_aci1, ucgen_aci2, ucgen_aci3):
        self.__sekil_isim = sekil_isim
        self.__ucgen_kenar1 = ucgen_kenar1
        self.__ucgen_kenar2 = ucgen_kenar2
        self.__ucgen_kenar3 = ucgen_kenar3
        self.__ucgen_aci1 = ucgen_aci1
        self.__ucgen_aci2 = ucgen_aci2
        self.__ucgen_aci3 = ucgen_aci3

    # Private değişkenler için get/set metotları
    # sekil_isim değişkeni için get/set metotları
    def get_sekil_isim(self):
        return self.__sekil_isim

    def set_sekil_isim(self, sekil_isim):
        self.__sekil_isim = sekil_isim

    # ucgen_kenar1 değişkeni için get/set metotları
    def get_ucgen_kenar1(self):
        return self.__ucgen_kenar1

    def set_ucgen_kenar1(self, ucgen_kenar):
        self.__ucgen_kenar1 = ucgen_kenar

    # ucgen_kenar2 değişkeni için get/set metotları
    def get_ucgen_kenar2(self):
        return self.__ucgen_kenar2

    def set_ucgen_kenar2(self, ucgen_kenar):
        self.__ucgen_kenar2 = ucgen_kenar

    # ucgen_kenar3 değişkeni için get/set metotları
    def get_ucgen_kenar3(self):
        return self.__ucgen_kenar3

    def set_ucgen_kenar3(self, ucgen_kenar):
        self.__ucgen_kenar3 = ucgen_kenar

    # ucgen_aci1 değişkeni için get/set metotları
    def get_ucgen_aci1(self):
        return self.__ucgen_aci1

    def set_ucgen_aci1(self, ucgen_aci):
        self.__ucgen_aci1 = ucgen_aci

    # ucgen_aci2 değişkeni için get/set metotları
    def get_ucgen_aci2(self):
        return self.__ucgen_aci2

    def set_ucgen_aci2(self, ucgen_aci):
        self.__ucgen_aci2 = ucgen_aci

    # ucgen_aci3 değişkeni için get/set metotları
    def get_ucgen_aci3(self):
        return self.__ucgen_aci3

    def set_ucgen_aci3(self, ucgen_aci):
        self.__ucgen_aci3 = ucgen_aci

    # Üçgen şekli için alan hesaplama metodu
    def alan_hesapla(self):
        # alan formülü
        # s = çevre/2
        # |AB| = a, |BC| = b, |CA| = c
        # alan = √(s * (s-a) * (s-b) * (s-c)) - karekök işlemi uyguluyorum
        s = self.cevre_hesapla() / 2
        alan = math.sqrt(s * (s - self.__ucgen_kenar1) * (s - self.__ucgen_kenar2) * (s - self.__ucgen_kenar3))
        return alan

    # Üçgen şekli için çevre hesaplama metodu
    def cevre_hesapla(self):
        cevre = self.__ucgen_kenar1 + self.__ucgen_kenar2 + self.__ucgen_kenar3
        return cevre

    # Üçgen çizimi sağlayan metot
    def sekil_ciz(self):
        ok = turtle.Turtle()
        turtle.resetscreen()

        # |AB| kenarı
        ok.forward(self.__ucgen_kenar1 * 5)
        ok.left(180 - self.__ucgen_aci1)

        # |BC| kenarı
        ok.forward(self.__ucgen_kenar2 * 5)
        ok.left(180 - self.__ucgen_aci2)

        # |CA| kenarı
        ok.forward(self.__ucgen_kenar3 * 5)
        ok.left(180 - self.__ucgen_aci3)

        # Çizimi bitirme fonksiyonu
        turtle.exitonclick()

    # Üçgen bilgilerini kullanıcıya döndüren metot
    def __str__(self):
        return (f"Girdiğiniz bilgilere göre"
                f"\n{self.__sekil_isim} Alanı = {self.alan_hesapla():.2f}"
                f"\n{self.__sekil_isim} Çevresi = {self.cevre_hesapla():.2f}")
