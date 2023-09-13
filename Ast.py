from enum import Enum
from abc import ABC,ABCMeta,abstractmethod
from SymbolTable import SymbolTable
from SymbolTable import SymbolTableEntry

DataType = Enum('DataType',['INT','DOUBLE'])

class AST(metaclass=ABCMeta):
	@abstractmethod
	def print(self):
		pass
	def typeCheckAST(self):
		pass
	def getDataType(self):
		pass

class NumberAst(AST):
	def __init__(self, number):
		self.value = number
	def print(self):
		print("Num:",self.value)
	def getDataType(self):
		return type(self.value)


class NameAst(AST):
	def __init__(self, symbolEntry):
		self.symbolEntry = symbolEntry
	def print(self):
		self.symbolEntry.print()
	def getDataType(self):
		return symbolEntry.getDataType()

class AssignAst(AST):
	def __init__(self,left,right,lineNo):
		self.left = left
		self.right = right
		self.lineNo = lineNo
	def typeCheckAST(self):
		if(left.getDataType()== right.getDataType()):
			return True
		else:
			return False
	def print(self):
		print("    Asgn:")
		print("      LHS ( ",end='')
		self.left.print()
		print(")")
		print("      RHS ( ",end='')
		self.right.print()
		print(")")
		

class PrintAst(AST):
	def __init__(self,symbolEntry):
		self.symbolEntry= symbolEntry
	def print(self):
		print("    Print:")
		print("      (",end="")
		self.symbolEntry.print()
		print(")")

class ReturnAst(AST):
	def __init__(self,rast):
		self.rast=rast
	def print(self):
		print("    Return ",end='')
		self.rast.print()


