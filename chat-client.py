#!/usr/bin/python
#coding=utf-8
#python v2.7
#client

import socket,threading,time,os
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 监听端口:
    ipaddress = raw_input("Please input ip address of other side:\n")
    port = 9999
    s.connect((ipaddress, port))
    print 'Waiting for connection...'
    t1 = threading.Thread(target=receiveinfo, args=(s,))
    t1.setDaemon(True)
    t1.start()
    t2 = threading.Thread(target=sendinfo, args=(s,))
    t2.start()
    t2.join()
    s.close()
    exit(0)

def receiveinfo(sock):
    while True:
        try:
            buf=sock.recv(1024)
            if buf:
                print '\n对方:',buf
            else:
                continue
        except BaseException,e:
            print e
            break

def sendinfo(sock):
    while True:
        try:
            buf=raw_input()
            if buf:
                sock.send(buf)
                if buf=='exit':
                    break
            else:
                continue
        except BaseException,e:
            print e
            break 

if __name__=='__main__':
    main()
