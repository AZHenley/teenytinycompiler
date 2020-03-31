# Emitter object keeps track of the generated code and outputs it.
class Emitter:
    def __init__(self, fullPath):
        self.fullPath = fullPath
        self.code = ""

    def emit(self, code):
        self.code += code

    def emitLine(self, code):
        self.code += code + '\n'

    def writeFile(self):
        with open(self.fullPath, 'w') as outputFile:
            outputFile.write(self.code)