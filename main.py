from chunk import Chunk, OpCode
from debug import disassembleChunk

def main():
    chunk = Chunk()
    chunk.writeChunk(OpCode.OP_RETURN)

    disassembleChunk(chunk, "test chunk")

main()