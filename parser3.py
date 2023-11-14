import main
from sly import Parser
from lexer2 import CTokenLexer
from Program import Program
from Function import Function
from Ast3 import *
from SymbolTable2 import *
# from IntermediateCode import *

gst = SymbolTable()
lxr=CTokenLexer()
ln=lxr.lineno
inter_list =[]

class CTokenParser(Parser):
    tokens = CTokenLexer.tokens
    literals=CTokenLexer.literals
    precedence = (('left',"-","+"),('left',"*"))

    @_('main_func')
    def program(self,p):
        pr=Program()
        pr.addFunctionDetails(p[0].name,p[0])
        #print("Code Accepted");
        return pr

    @_('return_type identifier "(" ")" "{" local_var_decl statements "}"')
    def main_func(self, p):
        func = Function(p.return_type,p[1])
        # p.statements.append(p.return_stmt)
        # print(inter_list)
        print(p.statements)
        func.setStatementsAstList(p.statements)
        func.setLocalSymbolTable(gst)
        return func
    
    @_('INT')
    def return_type(self, p):
        return p.INT
    
    @_('statement ";" statements')
    def statements(self,p):
        return [p[0]] + p[2]

    @_('statement ";"')
    def statements(self,p):
        return [p[0]]
    
    @_('assignment_stmt')
    def statement(self, p):
        print(p[0])
        return [p[0]]

    @_('print_stmt')
    def statement(self, p):
        return p[0]

    # @_('assignment_stmt statements')
    # def statements(self, p):
    #     # print(p[0][0].print())
    #     # p[1].append(p[0])
    #     return p[0]


    # @_('print_stmt statements')
    # def statements(self, p):
    #     p[1].append(p[0])
    #     return p[1]
    
    @_('identifier "=" expr')
    def assignment_stmt(self, p):
        return AssignAst(p[0],p[2],ln)
        # entry = gst.getEntryOfSymbol(p[0])
    @_('expr "-" expr')
    def expr(self,p):
        pass

    @_('expr "*" expr')
    def expr(self,p):
        pass
    @_('expr "+" expr')
    def expr(self,p):
        return PlusAst(p[0],p[2],ln)

    @_('"(" expr ")"')
    def expr(self,p):
        return p[1]

    @_('identifier')
    def expr(self,p):
        return p[0]
    
    @_('constant')
    def expr(self,p):
        return p[0]
    # @_('identifier "=" constant ";"')
    # def assignment_stmt(self,p):
    #     return AssignAst(NameAst(gst.nameInSymbolTable(p.identifier)),NumberAst(p.constant),ln)
    
    @_('PRINT identifier')
    def print_stmt(self, p):
        return PrintAst(gst.getEntryOfSymbol(p.identifier.getSymbolName()))

    @_('type decl ";"')
    def local_var_decl(self,p):
        for val in p.decl:
            gst.addSymbol(SymbolTableEntry(val,p.type))

    @_('identifier "," decl')
    def decl(self,p):
        return [p.identifier] + p.decl

    @_('identifier')
    def decl(self,p):
        return [p.identifier]
    
    @_('INT')
    def type(self, p):
        return p[0]
    
    @_('DOUBLE')
    def type(self, p):
        return p[0]
    
    @_('ID')
    def identifier(self, p):
        entry = gst.getEntryOfSymbol(p[0])
        # print(p[0],entry)
        if(entry != None):
            return entry
        # print(p[0])
        e = SymbolTableEntry(p[0],DataType.INT)
        # print(e,p[0])
        gst.addSymbol(e)
        return NameAst(e)
    
    @_('NUMBER')
    def constant(self, p):
        return NumberAst(p[0])

    # @_('RETURN NUMBER ";"')
    # def return_stmt(self,p):
    #     return ReturnAst(NumberAst(p[1]))

    def error(self, p):
        # self.valid = False
        if p is None:
            print("Syntax error at EOF")
        else:
            print(f"Syntax error at line {p.lineno-1}")

# lexer = CTokenLexer()
# parser = CTokenParser()
# expression ='''  int main(){
#      double a,b,c,d;
#      a=b+c*d;
#      print a;
# }
# } '''
# linter = parser.parse(lexer.tokenize(expression))
# for elem in linter:
# 	elem.print()