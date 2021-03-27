from .lexer import Lexer

class Run:
    def __init__(self, fileName, line):
        self.fileName = fileName
        self.line = line
        self.run()

    def run(self):
        lexer = Lexer(self.fileName, self.line)
        tokens, error = lexer.check_tokens()

        if error: print(error())
        else: print(tokens)