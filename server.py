import socket
import datetime
import pickle

# Opret en socket objekt
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vælg IP-adresse og port
host = '127.0.0.1'
port = 7913

# Bind til adressen
s.bind((host, port))

# Lytter for klienter (maksimalt 5 klienter i kø)
s.listen(5)

while True:
    # Etablere forbindelse med klient
    c, addr = s.accept()
    print(f"Fik forbindelse fra {addr}")

    # Send tid på server til client
    ct = datetime.datetime.now()
    iso_str = ct.isoformat()
    byte_array = bytearray(iso_str, 'utf-8')
    c.send(byte_array)

    # Luk forbindelsen
    c.close()