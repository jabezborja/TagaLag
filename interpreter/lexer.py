from .global_configs import Configs
from .position_watcher import Position
from .error_handler import MalingSyntax

class Lexer:
    def __init__(self, fileName, line):
        self.line = line
        self.line_position = Position(-1, 0, -1, fileName, line)
        self.index_char = None
        self.next()

    def next(self): # Proceed to another character in the line.
        self.line_position.next(self.index_char)
        self.index_char = self.line[self.line_position.index] if self.line_position.index < len(self.line) else None

    def check_tokens(self) -> list:
        found_tokens = []

        while self.index_char != None:
            if self.index_char in ' \t': # If 'Tabs' or spaces, proceed to another character until next line.
                self.next()
            elif self.index_char in Configs.DIGITS:
                found_tokens.append(self.index_char)
                self.next()
            elif self.index_char in '+':
                found_tokens.append(Configs.TOK_PLUS)
                self.next()
            elif self.index_char in '-':
                found_tokens.append(Configs.TOK_MINUS)
                self.next()
            elif self.index_char in '*':
                found_tokens.append(Configs.TOK_MULTIPLY)
            elif self.index_char in '/':
                found_tokens.append(Configs.TOK_DIVIDE)
            else:
                return found_tokens, MalingSyntax

        return found_tokens, None