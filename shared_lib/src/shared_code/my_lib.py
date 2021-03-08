import grpc

def start_insecure(addr:str, server: grpc.Server):
    server.add_insecure_port(addr)
    server.start()
    server.wait_for_termination()