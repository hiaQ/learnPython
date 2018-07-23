#!/user/bin/env python3
#coding:utf-8
import socket,threading,time

#创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#监听端口（创建一个socket之后要绑定监听的地址和端口，服务器可能
#有很多块网卡，可以绑定到某一块网卡上，也可以用0.0.0.0绑定到所
#有的网络地址，还可以用127.0.0.1绑定到本机地址，
s.bind(('127.0.0.1',9999))
#调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')

def tcplink(sock,addr):
	print('Accept new connection from %s:%s ...' % addr)
	sock.send(b'Welcome')
	while True:
		 data = sock.recv(1024)
		 time.sleep(1)
		 if not data or data.decode('utf-8') == 'exit':
		 	break
		 sock.send(('Hello, %s!') % data.decode('utf-8')).encode('utf-8')
	sock.close()
	print('Connection from %s:%s closed ' % addr)


while True:
	sock,addr = s.accept()
	t = threading.Thread(target = tcplink, args=(sock,addr))
	t.start()



