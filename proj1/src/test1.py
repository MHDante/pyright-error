from concurrent.futures.thread import ThreadPoolExecutor

from google.protobuf.empty_pb2 import Empty
import grpc
from shared_code.my_lib import start_insecure
from stubbed_code.shared_class import SharedClass

# pyright: reportUnknownMemberType = false
server : grpc.Server = grpc.server(ThreadPoolExecutor(), handlers=None)

class OverrideClass2(SharedClass):
    def GetStatus(self,
        request: Empty,
        context: grpc.ServicerContext,
    ) -> int: ...

start_insecure("localhost:8080",server )



from typing import Any, Dict, Callable

cheem :Type[Any] = float
meme:Type[Any] = cheem

my_dict : Dict[str, Type[Any]] = {}
my_dict["key"] = cheem
cheem = my_dict["key"]



