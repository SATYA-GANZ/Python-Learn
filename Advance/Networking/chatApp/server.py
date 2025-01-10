import socket
import threading

active_clients = {} # untuk active client yang diisi ama variabel soscks_client
def privMessage(message,socks_client,target,sender):
   global active_clients
   full = f"Pm from {sender} : " + message
   try:
      target.send(full.encode("utf-8"))
      if target:
        socks_client.send("pesan berhasil dikirim".encode("utf-8"))
   except Exception as e:
     print(f"error send message  {e}")
     
def broadcastMessage(message, sender):
  global active_clients
  for sock in active_clients:
    if sock != sender:
      try:
       sock.send(message.encode("utf-8"))
      except socks.error as e:
        print(f"error was occured {e}")

def handleUser(socks_client, socks_host):
  global active_clients
  socks_client.send("masukkan username : ".encode("utf-8"))
  username = socks_client.recv(1024).decode("utf-8")
  
  active_clients[socks_client] = username
  
  broadcastMessage(f"{username} telah memasuki chat room", socks_client)
  print(f"{username} dengan ip {socks_host} telah bergabung!")
  
  while True:
    try:
     message = socks_client.recv(1024).decode("utf-8")
     #pm = socks_client.recv(1024).decode("utf-8")
     if message.startswith("/pm") and message.count("|") == 2:
       #t.sleep(2)
       parts = message.split("|")
       
       command, targetUser, pesankan = parts
       
       #formatmsg = socks_client.recv(1024).decode("utf-8")
     #  print(formatmsg)
       #target_user, msg = formatmsg.split("|")
       sender = active_clients[socks_client]
       target = None
       
       for key,values in active_clients.items():
          if targetUser == values:
            target = key
       
       if target != None:    
           privMessage(pesankan,socks_client,target,sender)
       else:
        #  t.sleep(3)
          socks_client.send("cant find a host target".encode("utf-8"))
          
     elif message.startswith("/list"):
       user_list = ", ".join(active_clients.values())
       total_user = len(active_clients)
     #  for total in len(active_clients.values()):
         #x = total
       format_list = f"total user {total_user}\ncurrent user now : {user_list}"
       if user_list and total_user:
          socks_client.send(format_list.encode("utf-8"))
       else:
          print("nobody in chat room except you")
         
     elif message:
       fullMsg = f"{username} : {message}"
       print(fullMsg)
       
       broadcastMessage(fullMsg,socks_client)
    except socket.error as e:
      print(f"error : {e}")

  print(f"{username} meninggalkan chat ")
  del active_clients[socks_client]
  broadcastMessage(f"{username} left the chat", socks_client)
  socks_client.close()

def main():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(('127.0.0.97', 5000))
  server.listen(5)
  print("server running on port 5000")
  print(active_clients)
  
  while True:
    socks_client,socks_host = server.accept()
   # privMsg = threading.Thread(target=privMessage, args=(socks_client,msg,target))
    #privMsg.start
    
    thread = threading.Thread(target=handleUser,args=(socks_client,socks_host))
    thread.start()
    
if __name__ == "__main__":
  main()
