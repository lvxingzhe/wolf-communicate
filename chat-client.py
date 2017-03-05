#!/usr/bin/python
#coding=utf-8

import socket,threading,time,os
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 监听端口:
    s.connect(('127.0.0.1', 9999))
    print 'Waiting for connection...'
#    while True:
        # 接受一个新连接:
        # 创建新线程来处理TCP连接:
    t1 = threading.Thread(target=receiveinfo, args=(s,))
    t1.start()
    t2 = threading.Thread(target=sendinfo, args=(s,))
    t2.start()
    t2.join()

def receiveinfo(sock):
    while True:
        try:
            buf=sock.recv(1024)
            if buf:
                print '\n对方:',buf
            else:
                continue
        except BaseException:
            pass

def sendinfo(sock):
    while True:
        try:
            buf=raw_input()
            if buf:
                if buf=='exit':
                    break
                sock.send(buf)
            else:
                continue
        except BaseException:
            pass
    sock.close()
#    os.abort()

if __name__=='__main__':
    main()
