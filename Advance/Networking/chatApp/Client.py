import socket
import threading

IP = "127.0.0.6"
PORT = 4567

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((IP,PORT))
  pesan = input("masukkan pesan : ")
  s.sendall(pesan)
  data = s.recv(1024).decode("utf-8")

print(f"success get data from server : {data!r}")
