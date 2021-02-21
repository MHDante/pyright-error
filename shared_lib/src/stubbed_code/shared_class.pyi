import grpc
import abc
from google.protobuf.empty_pb2 import Empty

class SharedClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetStatus(self,
        request: Empty,
        context: grpc.ServicerContext,
    ) -> int: ...