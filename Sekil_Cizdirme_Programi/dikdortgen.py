import sekil
import turtle


class Dikdortgen(sekil.Sekil):  # Dikdörtgen şekli için oluşturduğum Subclass
    # Dikdörtgen bilgilerini değişkenlere atayan metot
    def __init__(self, sekil_isim, uzun_kenar, kisa_kenar):
        self.__sekil_isim = sekil_isim
        self.__uzun_kenar = uzun_kenar
        self.__kisa_kenar = kisa_kenar

    # Kullanıcıya sekil_isim değişkenini döndüren metot
    def get_sekil_isim(self):
        return self.__sekil_isim

    # Kullanıcıdan aldığı bilgiyle sekil_isim değişkenini değiştiren metot
    def set_sekil_isim(self, sekil_isim):
        self.__sekil_isim = sekil_isim

    # Kullanıcıya uzun_kenar değişkenini döndüren metot
    def get_uzun_kenar(self):
        return self.__uzun_kenar

    # Kullanıcıdan aldığı bilgiyle uzun_kenar değişkenini değiştiren metot
    def set_uzun_kenar(self, uzun_kenar):
        self.__uzun_kenar = uzun_kenar

    # Kullanıcıya kisa_kenar değişkenini döndüren metot
    def get_kisa_kenar(self):
        return self.__kisa_kenar

    # Kullanıcıdan aldığı bilgiyle kisa_kenar değişkenini değiştiren metot
    def set_kisa_kenar(self, kisa_kenar):
        self.__kisa_kenar = kisa_kenar

    # Dikdortgen şekli için alan hesaplama metodu
    def alan_hesapla(self):
        sekil_alan = self.__uzun_kenar * self.__kisa_kenar
        return sekil_alan

    # Dikdörtgen şekli için çevre hesaplama metodu
    def cevre_hesapla(self):
        cevre = 2 * (self.__uzun_kenar + self.__kisa_kenar)
        return cevre

    # Dikdörtgen çizimi sağlayan metot
    def sekil_ciz(self):
        ok = turtle.Turtle()
        for i in range(2):
            ok.forward(self.__uzun_kenar * 5)
            ok.right(90)
            ok.forward(self.__kisa_kenar * 5)
            ok.right(90)

        # Çizimi bitirme fonksiyonu
        turtle.exitonclick()

    # Dikdörtgen bilgilerini kullanıcıya döndüren metot
    def __str__(self):
        return (f"Girdiğiniz bilgilere göre"
                f"\n{self.__sekil_isim} Alanı = {self.alan_hesapla():.2f}"
                f"\n{self.__sekil_isim} Çevresi = {self.cevre_hesapla():.2f}")
