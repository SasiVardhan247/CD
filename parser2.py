import main
from sly import Parser
from lexer2 import CTokenLexer
from Program import Program
from Function import Function
from Ast import *
from SymbolTable2 import *
from IntermediateCode import *

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
        # print(p.statements)
        func.setStatementsAstList(p.statements + inter_list)
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
        pass

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
        # return AssignAst(NameAst(gst.nameInSymbolTable(p[0])),NameAst(gst.nameInSymbolTable(p[2])),ln)
        entry = gst.getEntryOfSymbol(p[0])
        if(entry == None):
            entry = SymbolTableEntry(p[0],DataType.INT)
            gst.addSymbol(entry)
        result = Variable(entry)
        opd1 = Variable(p[2])
        opd2 = None
        q = Quadruple(opd1,opd2,result,"=")
        inter_list.append(q)
        return inter_list

    @_('expr "-" expr')
    def expr(self,p):
        e = gst.newTemp()
        result = Variable(e)
        opd1 = Variable(p[0])
        opd2 = Variable(p[2])
        q = Quadruple(opd1,opd2,result,"-")
        inter_list.append(q)
        return e

    @_('expr "*" expr')
    def expr(self,p):
        e = gst.newTemp()
        result = Variable(e)
        opd1 = Variable(p[0])
        opd2 = Variable(p[2])
        q = Quadruple(opd1,opd2,result,"*")
        inter_list.append(q)
        return e

    @_('expr "+" expr')
    def expr(self,p):
        e = gst.newTemp()
        result = Variable(e)
        opd1 = Variable(p[0])
        opd2 = Variable(p[2])
        q = Quadruple(opd1,opd2,result,"+")
        inter_list.append(q)
        return e

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
        # print(p[0])
        entry = gst.getEntryOfSymbol(p[0])
        if(entry != None):
            return entry
        e = SymbolTableEntry(p[0],DataType.INT)
        gst.addSymbol(e)
        return e
    
    @_('NUMBER')
    def constant(self, p):
        return p[0]

    # @_('RETURN NUMBER ";"')
    # def return_stmt(self,p):
    #     return ReturnAst(NumberAst(p[1]))

    def error(self, p):
        # self.valid = False
        if p is None:
            print("Syntax error at EOF")
        else:
            print(f"Syntax error token=`{p.type}`")

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