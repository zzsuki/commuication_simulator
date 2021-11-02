from network.models import ThreadedTCPServer, ThreadedTCPRequestHandler, UDPServer
from config import PROTOCOL_PORT_MAP
from multiprocessing import Process


def start_server():
    server_list:list = []
    
    for _, v in PROTOCOL_PORT_MAP:
        tcp_port = v.get('TCP', default = None)
        if tcp_port:
            server = ThreadedTCPServer(('', tcp_port), ThreadedTCPRequestHandler)
            server_list.append(Process(target=server.serve_forever))
            
    for server in server_list:
        server.start()
        
    server_list[-1].join()