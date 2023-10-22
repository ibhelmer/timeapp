import socket

# Opret socket objekt
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vælg IP-adresse og port
host = '127.0.0.1'
port = 7913

# Forbind til serveren
s.connect((host, port))

# Modtag besked fra serveren
print(s.recv(1024).decode())

# Luk forbindelsen
s.close()