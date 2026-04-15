from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Simetrik Anahtar (Gerçek hayatta bu anahtar dinamik üretilir)
# 32 byte = 256 bit (AES-256)
KEY = b"BuAnahtarCokGizliVe32Karakterli!" 

def encrypt(raw_data):
    """Veriyi AES-256 ile şifreler ve Base64'e çevirir."""
    try:
        # Rastgele bir IV (Initialization Vector) oluştur
        cipher = AES.new(KEY, AES.MODE_CBC)
        iv = cipher.iv
        
        # Veriyi blok boyutuna tamamla (Padding) ve şifrele
        encrypted_data = cipher.encrypt(pad(raw_data.encode(), AES.block_size))
        
        # IV + Şifreli Veriyi birleştir ve Base64 yap (Ağda bozulmasın diye)
        return base64.b64encode(iv + encrypted_data).decode()
    except Exception as e:
        return f"[ERR] Encryption Failed: {e}"

def decrypt(enc_data):
    """Base64 veriyi çözer ve AES ile deşifre eder."""
    try:
        decoded_data = base64.b64decode(enc_data)
        
        # İlk 16 byte IV'dir, kalanı şifreli veridir
        iv = decoded_data[:16]
        cipher_text = decoded_data[16:]
        
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        
        # Deşifre et ve Padding'i temizle
        return unpad(cipher.decrypt(cipher_text), AES.block_size).decode()
    except Exception as e:
        return f"[ERR] Decryption Failed: {e}"
