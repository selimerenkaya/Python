# Selim Eren Kaya tarafından bu program yapılmıştır.

# Periyodik tablodaki en çok bilinen elementler bilme oyunu
from widgets import *
import sys
import subprocess
import pkg_resources


# Oyunun oynanacağı arayüzün tasarlandığı bölüm
class App(ctk.CTk):
    def __init__(self):

        # ayarlar
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.geometry("500x400")
        self.title("Element Bilme Oyunu")
        self.minsize(400, 300)

        # görünüş
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        # Widgetlar
        # 1 - Başlangıç Ekranı Widgetı
        self.zorluk = ctk.StringVar(value="Kolay")
        self.oyun_turu = ctk.StringVar(value="Element Adı Bilmece")
        self.baslatma = Baslat(self, self.baslat, self.zorluk, self.oyun_turu)

        # 2 - Oyun Bölümü Widgetı
        self.oyun = ctk.CTk
        self.puan: int = 0
        self.element: str = ""
        self.sembol: str = ""

        # Çalıştırma
        self.mainloop()

    # Başlangıç ekranı widgetın bitirilmesi ve oyuna geçilmesini sağlayan metot
    def baslat(self):
        self.oyun_turu, self.zorluk = self.baslatma.ayar_dondur()
        self.baslatma.grid_forget()
        if self.zorluk == "0":
            self.zorluk = "Orta"
        # Oyun Widgetını görünür kılan bölüm
        self.oyun = Oyun(self, self.zorluk, self.oyun_turu, self.puan, self.element, self.sembol)
        self.oyun.grid(column=2, row=1)


# Gerekli paketlerin indirilmesinin gerçekleştiği kısım
gereksinimler = {"customtkinter"}
indirilmis = {pkg.key for pkg in pkg_resources.working_set}
missing = gereksinimler - indirilmis
if missing:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])

# Uygulamanın başlatıldığı kısım
App()
