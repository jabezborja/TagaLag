class Position:
    def __init__(self, index, line, column, fileName, fileText):
        self.index = index
        self.line = line
        self.column = column
        self.fileName = fileName
        self.fileText = fileText

    def next(self, index_char):
        self.index += 1
        self.column += 1

        if index_char == "\n":
            self.line += 1
            self.column = 0

        return self

    def duplicate(self):
        return Position(self.index, self.line, self.column, self.fileName, self.fileText)