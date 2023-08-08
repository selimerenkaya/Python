from abc import ABC, abstractmethod
# Abstract Class metodunu
# kullanmak için kütüphaneden çağırdığım kısım


class Sekil(ABC):  # Subclasslarımda kullanmak üzere oluşturduğum Abstract Class (Soyut Sınıf)
    @abstractmethod
    def alan_hesapla(self):  # Alan hesaplama metodu
        pass

    @abstractmethod
    def cevre_hesapla(self):  # Çevre hesaplama metodu
        pass

    @abstractmethod
    def sekil_ciz(self):  # Şekil çizme metodu
        pass

    @abstractmethod
    def __str__(self):  # Nesne bilgilerini kullanıcıya döndürme metodu
        pass
