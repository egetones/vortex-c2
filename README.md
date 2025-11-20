<div align="center">

# Vortex C2

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Crypto](https://img.shields.io/badge/Encryption-AES--256-green)
![Type](https://img.shields.io/badge/Type-C2_Framework-red)

<p>
  <strong>An advanced, encrypted Command & Control (C2) framework for Red Team operations.</strong>
</p>

</div>

---

## Description

**Vortex C2** is a sophisticated post-exploitation framework designed to simulate real-world Advanced Persistent Threat (APT) scenarios. 

Unlike simple reverse shells (`nc`), Vortex implements **End-to-End Encryption (E2EE)** using **AES-256**. This ensures that network traffic between the implant and the server remains opaque to Network Intrusion Detection Systems (NIDS) and analysts.

### Key Capabilities

  **AES-256 Encryption:** All traffic is encrypted with CBC mode and PKCS7 padding.
  **Persistence Logic:** The implant automatically attempts to reconnect if the connection is dropped.
  **Remote Shell:** Full remote command execution capability.
  **Multi-threaded Server:** Handles multiple active sessions simultaneously.

---

## Architecture

1.  **`server.py`:** The Attacker's console. Listens for incoming connections.
2.  **`implant.py`:** The payload deployed on the target. It beacons back to the server.
3.  **`common.py`:** Shared cryptographic library handling encryption/decryption routines.

---

## Usage

### 1. Install Dependencies
```bash
pip install pycryptodome
```

### 2. Configure
Edit `implant.py` and set `C2_IP` to your server's IP address.

### 3. Start Server (Attacker)
```bash
python3 server.py
```

### 4. Deploy Implant (Victim)
```bash
python3 implant.py
```

*Once the implant connects, you will get a shell prompt on the server:*
```text
[+] Yeni Bağlantı: ('127.0.0.1', 45678)
Vortex@127.0.0.1> whoami
root
```

---

## ⚠️ Disclaimer

**Vortex C2 is developed strictly for educational and authorized testing purposes.** Using this software to control computers without permission is a crime. The developer assumes no liability for misuse.

---

## License

Distributed under the MIT License.
