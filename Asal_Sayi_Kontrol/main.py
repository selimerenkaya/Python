# Bu program Selim Eren Kaya tarafından yapılmıştır.
# Girilen sayı asal mı diye kontrol eden program

# Gerekli paketlerin indirilmesini sağlayan kısım
import subprocess
import sys

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'customtkinter'])
import customtkinter as ctk


# Programın özelliklerini içeren sınıf
class App(ctk.CTk):
    def __init__(self):
        # Ayarlar
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.geometry("400x280")
        self.title("Asal Sayı Kontrol")
        self.minsize(400, 280)

        # Görünüş
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

        # Program
        self.soru = Soru(self)
        self.mainloop()


# Programın içeriğini içeren sınıf
class Soru(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.grid(row=0, column=2)
        self.asallik_durumu = ctk.StringVar()

        # Yazılar
        # Başlık
        self.baslik = ctk.CTkLabel(self, text="Asal Sayı Kontrol", font=("Verdana", 24))
        self.baslik.pack(padx=15, pady=10, expand=True)

        # Soru
        self.soru = ctk.CTkLabel(self, text="Asal sayı olup olmadığını\nkontrol etmek istediğiniz sayıyı giriniz",
                                 font=("Verdana", 18))
        self.soru.pack(padx=15, pady=10, expand=True)

        # Sayı Girişi
        self.sayi = ctk.CTkEntry(self, placeholder_text="Sayı giriniz", font=("Verdana", 16))
        self.sayi.pack(padx=15, pady=10, expand=True)

        # Çalıştırma Butonu
        self.buton = ctk.CTkButton(self, text="Kontrol et", font=("Verdana", 16),
                                   command=lambda: self.asal_kontrol(self.sayi.get(), self.sayi_durum))
        self.buton.pack(padx=15, pady=10, expand=True)

        # Sayı Durumu
        self.sayi_durum = ctk.CTkLabel(self, text=self.asallik_durumu.get(), font=("Verdana", 18))
        self.sayi_durum.pack(padx=15, pady=10, expand=True)

    # Sayının asal olup olmadığını kontrol eden metot
    def asal_kontrol(self, sayi, grid: ctk.CTkLabel):
        grid.destroy()
        try:
            sayi = int(sayi)
            bolenler: list = []
            if sayi > 0:
                for i in range(2, sayi):
                    if sayi % i == 0:
                        bolenler.append(i)
                if len(bolenler) > 0:
                    self.asallik_durumu.set("Asal Değil")
                else:
                    self.asallik_durumu.set("Asal")
                self.sayi_durum = ctk.CTkLabel(self, text=self.asallik_durumu.get(), font=("Verdana", 18))
                self.sayi_durum.pack(padx=15, pady=10, expand=True)
            else:
                self.sayi_durum = ctk.CTkLabel(self, text="Negatif sayılar asal olamaz", font=("Verdana", 18))
                self.sayi_durum.pack(padx=15, pady=10, expand=True)
        except Exception:
            self.sayi_durum = ctk.CTkLabel(self, text="Lütfen sadece sayı giriniz", font=("Verdana", 18))
            self.sayi_durum.pack(padx=15, pady=10, expand=True)


App()
