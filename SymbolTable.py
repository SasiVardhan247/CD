from enum import Enum
DataType = Enum('DataType',['INT','DOUBLE'])

class SymbolTableEntry:
	def __init__(self,name,datatype):
		self.name=name
		self.datatype=datatype
	def getSymbolName(self):
		return self.name
	def getDataType(self):
		return self.datatype
	def print(self):
		# print(f"Variable Name: {self.name} , DataType : {self.datatype}")
		print(f"Name:{self.name} _")


class SymbolTable:
	def __init__(self):
		self.table = []
	def addSymbol(self,symbol):
		self.table.append(symbol)
	def nameInSymbolTable(self,name):
		for ste in self.table:
			if ste.getSymbolName() == name:
				return ste
		return None
	def printSymbolTable(self):
		print("Symbol Table:")
		for ste in self.table:
			ste.print()


