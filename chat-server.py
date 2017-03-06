#!/usr/bin/python
#coding=utf-8
#python v2.7
#server

import socket,threading,time

lock=threading.Lock()
myflag=False   #exit flag

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 监听端口:
    address='0.0.0.0'
    port=9999
    s.bind((address, port))
    s.listen(5)
    print 'Waiting for connection...'
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t1 = threading.Thread(target=receiveinfo, args=(sock, addr))
        t1.start()
        global myflag
        myflag = True
        t2 = threading.Thread(target=sendinfo, args=(sock, addr))
        t2.start()
        t1.join()
        t2.join()
        sock.close()

def receiveinfo(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    while True:
        try:
            buf=sock.recv(1024)
            if buf:
                print '\n对方:',buf
                if buf=='exit':
                    lock.acquire()
                    try:
                        global  myflag
                        myflag=False
                        print 'global flag:', myflag
                    finally:
                        lock.release()
                    break
            else:
                print 'exit ,because of buffer is None'
                break
        except BaseException,e:
            print e
    print 'Connection from %s:%s closed. by reveiveinfo thread' % addr

def sendinfo(sock, addr):
    sock.send('welcome!connecting successed...')
    myloop=True
    while myloop:
        try:
            buf=raw_input()
            if buf:
                sock.send(buf)
            else:
                continue
        except BaseException,e:
            print e
        lock.acquire()
        try:
            myloop=myflag
            print 'myflag:',myflag
        finally:
            lock.release()
    print 'Connection from %s:%s closed by sendinfo thread.' % addr

if __name__=='__main__':
    main()
