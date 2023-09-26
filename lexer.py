from sly import Lexer

class CTokenLexer(Lexer):
    tokens = {INT, ID, PRINT, NUMBER}
    literals={'+','*','-','/','=','(',')',';','{','}',','}
    ignore = ' \t'
    
    INT = r'int'
    PRINT= r'print'
    # RETURN= r'return'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'
    ignore_newline = r'\n+'
    
    def __init__(self):
        self.lineno = 1

    def newline(self, t):
        r'\n+'
        self.lineno += len(t.value)
    
    def error(self, t):
        # print(f"Illegal character '{t.value[0]}'")
        # raise Exception(f"Illegal character '{t.value[0]}'")
        self.index += 1
