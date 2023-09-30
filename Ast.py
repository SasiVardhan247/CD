import sys
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
		ls=f"Num: {self.value}"
		# print("Num:",self.value,end="")
		return ls

	def getDataType(self):
		return type(self.value)


class NameAst(AST):
	def __init__(self, symbolEntry):
		self.symbolEntry = symbolEntry
	def print(self):
		ls=f"{self.symbolEntry.print()}"
		# self.symbolEntry.print()
		return ls
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
		ls=list()
		ls.append("    Asgn:")
		# print("    Asgn:")
		ls.append(f"      LHS ( {self.left.print()} )")
		# print("      LHS ( ",end='')
		# self.left.print()
		# print(")")
		ls.append(f"      RHS ( {self.right.print()} )")
		# print("      RHS ( ",end='')
		# self.right.print()
		# print(")")
		return ls
		

class PrintAst(AST):
	def __init__(self,symbolEntry):
		self.symbolEntry= symbolEntry
	def print(self):
		ls=list()
		ls.append("    Print:")
		ls.append(f"      ( {self.symbolEntry.print()} )")
		# print("    Print:")
		# print("      (",end="")
		# self.symbolEntry.print()
		# print(")")
		return ls

class ReturnAst(AST):
	def __init__(self,rast):
		self.rast=rast
	def print(self):
		ls=list()
		ls.append("    Return ")
		ls.append(f"{self.rast.print()}")
		# print("    Return ",end='')
		# self.rast.print()
		return ls


