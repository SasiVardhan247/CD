from SymbolTable import SymbolTable
class Function:
	def __init__(self, returnType, name):
		self.returnType = returnType
		self.name       = name
		self.statementsAstList = []
		self.localSymbolTable = SymbolTable()
	def setStatementsAstList(self, sastList):
		# print(sastList)
		self.statementsAstList = sastList
	def getStatementsAstList(self):
		# print(self.statementsAstList)
		return self.statementsAstList
	def setLocalSymbolTable(self,localList):
		self.localSymbolTable = localList
	def getLocalSymbolTable(self):
		return self.localSymbolTable
	def print(self):
		print(f'  Procedure:{self.name}, ReturnType:{self.returnType}')
		# print(self.setStatementsAstList)
		for sal in self.statementsAstList:
			sal.print()