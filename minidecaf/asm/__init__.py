from .command import *

class AsmEmitter:
    def __init__(self, outfile:str):
        self.f = open(outfile, 'w')
        self.s = ""
    # def __init(self):
    #     self.f = open("outfile.txt", 'w')

    def emit(self, com:AsmCommand):
        # print(f"{com}", file=self.f)
        self.s += f"{com}\n"
        # print(f"{com}")

    def getASM(self):
        return self.s

    def close(self):
        self.f.close()

    def __call__(self, coms:[AsmCommand]):
        for com in coms:
            #print(com)
            self.emit(com)
