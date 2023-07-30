import customtkinter as ctk
import random


class Baslat(ctk.CTkFrame):
    def __init__(self, parent, func, zorluk, oyun_turu):
        super().__init__(master=parent)
        self.grid(column=2, row=2)
        self.func = func
        self.zorluk = zorluk
        self.oyun_turu = oyun_turu

        ctk.CTkLabel(self, text="Element Bilme Oyunu", font=("Verdana", 24)).pack(padx=10, pady=10, expand=True)

        # Oyunun zorluk seviyesini belirleyen kısım
        ctk.CTkLabel(self, text="Zorluk Seviyesi", font=("Verdana", 16)).pack(padx=10, pady=5, expand=True)

        kolay = ctk.CTkCheckBox(self, text="Kolay", variable=self.zorluk,
                                command=lambda: self.secim("Kolay", orta, zor),
                                onvalue="Kolay", offvalue="Orta", font=("Verdana", 14))
        orta = ctk.CTkCheckBox(self, text="Orta", variable=self.zorluk,
                               command=lambda: self.secim("Orta", kolay, zor),
                               onvalue="Orta", offvalue="Zor", font=("Verdana", 14))
        zor = ctk.CTkCheckBox(self, text="Zor", variable=self.zorluk,
                              command=lambda: self.secim("Zor", kolay, orta),
                              onvalue="Zor", font=("Verdana", 14))

        kolay.pack(padx=10, pady=5, expand=True)
        orta.pack(padx=10, pady=5, expand=True)
        zor.pack(padx=10, pady=5, expand=True)

        # Oyunun türünü belirleyen kısım
        ctk.CTkLabel(self, text="\nOyun Türü", font=("Verdana", 16)).pack(padx=10, pady=5, expand=True)
        oyun_turu1 = ctk.CTkCheckBox(self, text="Element Adı Bilmece", variable=self.oyun_turu,
                                     command=lambda: self.oyun_tur("Element Adı Bilmece"),
                                     onvalue="Element Adı Bilmece", offvalue="Latince Sembol Bilmece",
                                     font=("Verdana", 14))
        oyun_turu2 = ctk.CTkCheckBox(self, text="Latince Sembol Bilmece", variable=self.oyun_turu,
                                     command=lambda: self.oyun_tur("Latince Sembol Bilmece"),
                                     onvalue="Latince Sembol Bilmece", offvalue="Element Adı Bilmece",
                                     font=("Verdana", 14))

        oyun_turu1.pack(padx=10, pady=5, expand=True)
        oyun_turu2.pack(padx=10, pady=5, expand=True)

        # Oyunu başlatma butonu
        self.buton = ctk.CTkButton(self, text="Oyunu Başlat", command=self.func)
        self.buton.pack(side="bottom", padx=10, pady=10, expand=True)

    # Arayüzde zorluk derecesini seçmeye yarayan metot
    def secim(self, zorluk_derecesi, deger1, deger2):
        self.zorluk.set(zorluk_derecesi)
        deger1.deselect()
        deger2.deselect()

    # Arayüzde oyun türünü seçmeye yarayan metot
    def oyun_tur(self, oyun_turu):
        self.oyun_turu.set(oyun_turu)

    # App Class'ına oyun ayarlarını döndüren metot
    def ayar_dondur(self):
        return self.oyun_turu.get(), self.zorluk.get()


class Oyun(ctk.CTkFrame):
    def __init__(self, parent, zorluk, oyun_turu, puan, element, sembol):
        super().__init__(master=parent)
        self.zorluk = zorluk
        self.oyun_turu = oyun_turu
        self.puan = puan
        self.element = element
        self.sembol = sembol
        self.elementler: dict = {}
        self.puan_tablosu = ctk.CTk
        self.ana_soru = ctk.CTk
        self.soru = ctk.CTk
        self.cevap = ctk.CTk
        self.dogru_cevap = ctk.CTk
        self.buton = ctk.CTk
        self.final_skoru = ctk.CTk
        self.sonuc_goster = False

        # Elementlerin ismi ve sembollerinin tutulduğu sözlükler (dictionary)
        # Kolay mod elementleri
        self.kolay_elementler: dict = {'Hidrojen': 'H', 'Helyum': 'He', 'Lityum': 'Li', 'Berilyum': 'Be', 'Bor': 'B',
                                       'Karbon': 'C', 'Azot': 'N', 'Oksijen': 'O', 'Flor': 'F', 'Neon': 'Ne',
                                       'Sodyum': 'Na', 'Magnezyum': 'Mg', 'Alüminyum': 'Al',
                                       'Silisyum': 'Si', 'Fosfor': 'P', 'Kükürt': 'S', 'Klor': 'Cl', 'Argon': 'Ar',
                                       'Potasyum': 'K', 'Kalsiyum': 'Ca'}

        # Orta mod elementleri
        self.orta_elementler: dict = {'Kurşun': 'Pb', 'Civa': 'Hg', 'Gümüş': 'Ag', 'Çinko': 'Zn', 'Altın': 'Au',
                                      'Krom': 'Cr', 'Mangan': 'Mn', 'Demir': 'Fe', 'Kobalt': 'Co', 'Nikel': 'Ni',
                                      'Bakır': 'Cu', 'Kalay': 'Sn', 'İyot': 'I', 'Platin': 'Pt', 'Titanyum': 'Ti',
                                      'Brom': 'Br', 'Kripton': 'Kr', 'Paladyum': 'Pd', 'Galyum': 'Ga', 'Arsenik': 'As'}

        # Zor mod elementleri
        self.zor_elementler: dict = {'Radon': 'Rn', 'İridyum': 'Ir', 'Baryum': 'Ba', 'Rodyum': 'Rh', 'Zirkonyum': 'Zr',
                                     'Germanyum': 'Ge', 'Vanadyum': 'V', 'Selenyum': 'Se', 'Tellür': 'Te',
                                     'Skandiyum': 'Sc', 'Rubidyum': 'Rb', 'Antimon': 'Sb', 'Ksenon': 'Xe',
                                     'İndiyum': 'In', 'Tungsten': 'W'}

        # Oyun zorluğuna göre sözlük atamasının yapıldığı kısım
        if self.zorluk == "Kolay":
            self.elementler = self.kolay_elementler
        elif self.zorluk == "Orta":
            self.elementler = self.orta_elementler
        elif self.zorluk == "Zor":
            self.elementler = self.zor_elementler
        self.cevap_listesi = list(self.elementler.items())

        # Oyun arayüzü
        self.oyun_degiskenleri()
        self.oyun_ekrani()

    # Oyuna ait değişkenlerin atamasını yapan metot
    def oyun_degiskenleri(self):
        element, sembol = random.choice(list(self.elementler.items()))
        self.elementler.pop(element)
        self.sembol = sembol
        self.element = element

    # Oyunu ekrana veren metot
    def oyun_ekrani(self):
        self.soru_goster(len(self.elementler))

    # Soruların gösterilmesini sağlayan metot
    def soru_goster(self, uzunluk):
        if uzunluk >= 0 and not self.sonuc_goster:
            self.puan_tablosu = ctk.CTkLabel(self, text=f"Puan = {self.puan}", font=("Verdana", 24))
            self.puan_tablosu.pack(side="top", padx=10, pady=5, expand=True)
            self.ana_soru = ctk.CTkLabel(self, text="Soru", font=("Verdana", 24))
            self.ana_soru.pack(padx=10, pady=5, expand=True)
            if self.oyun_turu == "Element Adı Bilmece":
                self.soru = ctk.CTkLabel(self, text=f"{self.sembol} Latince sembolü hangi elemente aittir?",
                                         font=("Verdana", 20))
                self.soru.pack(padx=10, pady=5, expand=True)
                self.cevap = ctk.CTkEntry(self, placeholder_text="Element ismi", font=("Verdana", 12))
                self.cevap.pack(padx=10, pady=5, expand=True)
                self.dogru_cevap = self.element
                self.buton = ctk.CTkButton(self, text="Sıradaki Soru", font=("Verdana", 12),
                                           command=lambda: self.cevap_kontrol(self.cevap, self.dogru_cevap,
                                                                              self.puan_tablosu,
                                                                              self.ana_soru, self.soru,
                                                                              self.cevap, self.buton))
                self.buton.pack(padx=10, pady=5, expand=True)

            elif self.oyun_turu == "Latince Sembol Bilmece":
                self.soru = ctk.CTkLabel(self, text=f"{self.element} Elementinin latince sembolü nedir?",
                                         font=("Verdana", 20))
                self.soru.pack(padx=10, pady=5, expand=True)
                self.cevap = ctk.CTkEntry(self, placeholder_text="Latince Sembol", font=("Verdana", 12))
                self.cevap.pack(padx=10, pady=5, expand=True)
                self.dogru_cevap = self.sembol
                self.buton = ctk.CTkButton(self, text="Sıradaki Soru", font=("Verdana", 12),
                                           command=lambda: self.cevap_kontrol(self.cevap, self.dogru_cevap,
                                                                              self.puan_tablosu,
                                                                              self.ana_soru, self.soru,
                                                                              self.cevap, self.buton))
                self.buton.pack(padx=10, pady=5, expand=True)
        else:
            # Oyun bitince final skorunu ve cevapları gösteren kısım
            self.final_skoru = ctk.CTkLabel(self, text=f"FİNAL SKORU\n{self.puan}", font=("Verdana", 24))
            self.final_skoru.pack(padx=10, pady=10, expand=True)
            ctk.CTkLabel(self, text=f"CEVAPLAR", font=("Verdana", 24)).pack(padx=10, pady=10, expand=True)

            # Cevapları yazdıran kısım
            for i in range(0, (len(self.cevap_listesi) // 5) + 1):
                if len(self.cevap_listesi) - i*5 < 5:
                    deger_siniri = len(self.cevap_listesi) - (i-1)*5
                    if deger_siniri == 4:
                        ctk.CTkLabel(self, text=f"\n{self.cevap_listesi[(i-1)*5+1][0]}: "
                                                f"{self.cevap_listesi[(i-1)*5+1][1]},   "
                                                f"{self.cevap_listesi[(i-1)*5+2][0]}: "
                                                f"{self.cevap_listesi[(i-1)*5+2][1]},   "
                                                f"{self.cevap_listesi[(i-1)*5+3][0]}: "
                                                f"{self.cevap_listesi[(i-1)*5+3][1]},   "
                                                f"{self.cevap_listesi[(i-1)*5+4][0]}: "
                                                f"{self.cevap_listesi[(i-1)*5+4][1]},   ")\
                            .pack(padx=10, pady=10, expand=True)
                    elif deger_siniri == 3:
                        ctk.CTkLabel(self, text=f"\n{self.cevap_listesi[(i - 1) * 5 + 1][0]}: "
                                                f"{self.cevap_listesi[(i - 1) * 5 + 1][1]},   "
                                                f"{self.cevap_listesi[(i - 1) * 5 + 2][0]}: "
                                                f"{self.cevap_listesi[(i - 1) * 5 + 2][1]},   "
                                                f"{self.cevap_listesi[(i - 1) * 5 + 3][0]}: "
                                                f"{self.cevap_listesi[(i - 1) * 5 + 3][1]}")\
                            .pack(padx=10, pady=10, expand=True)
                    elif deger_siniri == 2:
                        ctk.CTkLabel(self, text=f"\n{self.cevap_listesi[(i - 1) * 5 + 1][0]}: "
                                                f"{self.cevap_listesi[(i - 1) * 5 + 1][1]},   "
                                                f"{self.cevap_listesi[(i - 1) * 5 + 2][0]}: "
                                                f"{self.cevap_listesi[(i - 1) * 5 + 2][1]}")\
                            .pack(padx=10, pady=10, expand=True)
                    elif deger_siniri == 1:
                        ctk.CTkLabel(self, text=f"\n{self.cevap_listesi[(i - 1) * 5 + 1][0]}: "
                                                f"{self.cevap_listesi[(i - 1) * 5 + 1][1]}")\
                            .pack(padx=10, pady=10, expand=True)

                else:
                    ctk.CTkLabel(self, text=f"\n{self.cevap_listesi[i*5-4][0]}: {self.cevap_listesi[i*5-4][1]},   "
                                            f"{self.cevap_listesi[i*5-3][0]}: {self.cevap_listesi[i*5-3][1]},   "
                                            f"{self.cevap_listesi[i*5-2][0]}: {self.cevap_listesi[i*5-2][1]},   "
                                            f"{self.cevap_listesi[i*5-1][0]}: {self.cevap_listesi[i*5-1][1]},   "
                                            f"{self.cevap_listesi[i*5][0]}: {self.cevap_listesi[i*5][1]}   ",
                                 font=("Verdana", 12)).pack(padx=10, pady=10, expand=True)

    # Sorulara verilen cevapları kontrol eden metot
    def cevap_kontrol(self, soru_cevabi, dogru_cevap, grid1, grid2, grid3, grid4, grid5):
        if soru_cevabi.get() == dogru_cevap:
            self.puan += 5
        else:
            self.puan -= 3
        grid1.destroy()
        grid2.destroy()
        grid3.destroy()
        grid4.destroy()
        grid5.destroy()
        if len(self.elementler) == 0:
            self.sonuc_goster = True
        else:
            self.oyun_degiskenleri()

        self.soru_goster(len(self.elementler))
