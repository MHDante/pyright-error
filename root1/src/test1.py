from concurrent.futures.thread import ThreadPoolExecutor
import grpc
from shared_code.my_lib import start_insecure

# pyright: reportUnknownMemberType = false
server = grpc.server(ThreadPoolExecutor(), handlers=None)

# do special stuff

start_insecure("localhost:8080",server )