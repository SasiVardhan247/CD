from sly import Lexer

class CTokenLexer(Lexer):
    tokens = {INT, ID, PRINT, NUMBER}
    literals={'+','*','-','/','=','(',')',';','{','}',','}
    ignore = ' \t'
    
    INT = r'int'
    PRINT= r'print'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'
    
    def __init__(self):
        self.lineno = 1
        
    def ID(self, t):
        keywords = {'int', 'print'}  # Reserved keywords
        if t.value in keywords:
            t.type = t.value.upper()  # Convert to uppercase for keyword tokens
        return t

    def newline(self, t):
        r'\n+'
        self.lineno += len(t.value)
    
    def error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        self.index += 1
