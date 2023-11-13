from enum import Enum
DataType = Enum('DataType',['INT','DOUBLE'])

class SymbolTableEntry:
	def __init__(self,name,datatype):
		self.name=name
		self.datatype=datatype
		self.value=None
	def getSymbolName(self):
		return self.name
	def getDataType(self):
		return self.datatype
	def print(self):
		# print(f"Variable Name: {self.name} , DataType : {self.datatype}")
		# print(f"Name:{self.name} _",end="")
		st = f"Name:{self.getSymbolName()} _"
		print(self.getSymbolName(),end=" ")
		return st


class SymbolTable:
	def __init__(self):
		self.table = []
		self.count=0
	def addSymbol(self,symbol):
		self.table.append(symbol)
	# def nameInSymbolTable(self,name):
	# 	for ste in self.table:
	# 		if ste.getSymbolName() == name:
	# 			return ste
	# 	return None
	def nameInSymbolTable(self,name):
		for symb in self.table:
			if symb.getSymbolName()==name:
				return True
		return False
	def getEntryOfSymbol(self,name):
		for symb in self.table:
			if symb.getSymbolName()==name:
				return symb
		return None
	def print(self):
		ls=list()
		ls.append("Symbol Table:")
		# print("Symbol Table:")
		for ste in self.table:
			ls.append(ste.print())
		return ls
	def newTemp(self):
		name = "t" + str(self.count)
		self.count = self.count +1
		e = SymbolTableEntry(name,DataType.INT)
		self.addSymbol(e)
		return e


