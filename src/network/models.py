#!/usr/bin/python3
import socket
import socketserver
from config import PROTOCOL_PORT_MAP
from multiprocessing import Process


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            message = self.request.recv(1024)
            self.request.send(message)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True
    allow_reuse_port = True
    
    def __init__(self, server_address, RequestHandlerClass):
        super().__init__(server_address, RequestHandlerClass)


class TCPClient:
    def __init__(self, ip, port, buf_size:int = 1024, timeout:int =None):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))
        self.buf_size = buf_size
    
    def recv_message(self):
        return self.sock.recv(self.buf_size)
    
    def send_message(self, message: bytes):
        self.sock.send(message)
        
    def send_and_recv(self, message_list: list):
        while True:
            for message in message_list:
                self.send_message(bytes.fromhex(message))
                _ = self.sock.recv(self.buf_size)
    
    def client_forever(self):
        while True:
            self.send_and_recv([]) #TODO:设置不同协议的message
    
    def close(self):
        self.sock.close()
        
    def __del__(self):
        self.close()
        

class UDPServer:
    def __init__(self, host, port, buf_size:int = 1024):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        self.buf_size = buf_size
        
    def send(self, message:bytes, address:tuple):
        self.sock.sendto(message, address)
        
    def recv(self):
        return self.sock.recvfrom(self.buf_size)
    
    def recv_and_send(self):
        while True:
            message, address = self.recv()
            self.send(message, address)
            
    def serve_forever(self):
        self.recv_and_send()
        
    def close(self):
        self.sock.close()
    
