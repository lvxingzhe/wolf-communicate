#!/usr/bin/python
#coding=utf-8

import socket,threading,time
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 监听端口:
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print 'Waiting for connection...'
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=receiveinfo, args=(sock, addr))
        t.start()
        t = threading.Thread(target=sendinfo, args=(sock, addr))
        t.start()

def receiveinfo(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    while True:
        try:
            buf=sock.recv(1024)
            if buf:
                if buf=='exit':
                    break
                print '\n对方:',buf
            else:
                break
        except BaseException:
            pass
    sock.close()
    print 'Connection from %s:%s closed.' % addr

def sendinfo(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    while True:
        try:
            buf=raw_input()
            if buf:
                sock.send(buf)
            else:
                continue
        except BaseException:
            pass
    sock.close()
    print 'Connection from %s:%s closed.' % addr

if __name__=='__main__':
    main()
