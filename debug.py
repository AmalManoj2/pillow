from chunk import Chunk, OpCode

def disassembleChunk(chunk, name):
    print(name)

    for offset in range(0,len(chunk.code)):
        offset = disassembleInstruction(chunk, offset)

def disassembleInstruction(chunk, offset):
    print(offset, end=" ")

    Instruction = chunk.code[offset]

    if Instruction == OpCode.OP_RETURN:
        return simpleInstruction("OP_RETURN", offset)
    else:
        print("Unknown OpCode")
        return offset + 1
    
def simpleInstruction(name, offset):
    print(name)
    return offset + 1