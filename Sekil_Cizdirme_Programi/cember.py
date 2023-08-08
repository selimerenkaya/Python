import turtle

import sekil


class Cember(sekil.Sekil):  # Çember şekli için oluşturduğum Subclass
    # Dikdörtgen bilgilerini değişkenlere atayan metot
    def __init__(self, sekil_isim, yaricap):
        self.__sekil_isim = sekil_isim
        self.__yaricap = yaricap

    # Private değişkenler için get/set metotları
    # sekil_isim değişkeni için get/set metotları
    def get_sekil_isim(self):
        return self.__sekil_isim

    def set_sekil_isim(self, sekil_isim):
        self.__sekil_isim = sekil_isim

    # yaricap değişkeni için get/set metotları
    def get_yaricap(self):
        return self.__yaricap

    def set_yaricap(self, yaricap):
        self.__yaricap = yaricap

    # Çember şekli için alan hesaplama metodu
    def alan_hesapla(self):
        alan = 3.14 * (self.__yaricap ** 2)
        return alan

    # Çember şekli için çevre hesaplama metodu
    def cevre_hesapla(self):
        cevre = 2 * self.__yaricap * 3.14
        return cevre

    # Çember şekli için şekil çizme metodu
    def sekil_ciz(self):
        ok = turtle.Turtle()
        ok.circle(self.cevre_hesapla())

        # Çizimi bitirme fonksiyonu
        turtle.exitonclick()

    # Çember bilgilerini kullanıcıya döndüren metot
    def __str__(self):
        return (f"Girdiğiniz bilgilere göre"
                f"\n{self.__sekil_isim} Alanı = {self.alan_hesapla():.2f}"
                f"\n{self.__sekil_isim} Çevresi = {self.cevre_hesapla():.2f}")
