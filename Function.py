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
		print(f'DataType: {self.returnType}, Name: {self.name}')
