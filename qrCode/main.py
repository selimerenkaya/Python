# Girilen URL'nin QR Code görselini üreten kod
import segno

if __name__ == '__main__':
    # Metin değişkenine girilen string ne ise onun QR Code'u oluşturulur
    metin: str = "https://www.linkedin.com/in/selim-eren-kaya-82b690252/"
    qrcode = segno.make_qr(metin)
    qrcode.save(
        "qrCode.png",
        scale=5,
        border=0,
    )
