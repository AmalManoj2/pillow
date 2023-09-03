from enum import Enum

class OpCode(Enum):
    OP_RETURN = 1

class Chunk:
    def __init__(self):
        self.code : list = []

    def writeChunk(self, byte): # You can add '-> int' to specify that it'll return 
            self.code.append(byte) 

chunk = Chunk()