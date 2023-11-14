from SymbolTable2 import *
class Function:
	def __init__(self, returnType, name):
		self.returnType = returnType
		self.name       = name
		self.statementsAstList = []
		self.localSymbolTable = SymbolTable()
		self.ls=[]
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
		# print(f'  Procedure:{self.name.getSymbolName()}, ReturnType:{self.returnType}')
		# ls=list()
		self.ls.append(f'  Procedure:{self.name.getSymbolName()}, ReturnType:{self.returnType}')
		# print(self.getStatementsAstList())
		for sal in self.statementsAstList:
			self.recursive_iterate(sal)
			# ls.append(sal.print())
		return self.ls

	def recursive_iterate(self,obj):
		if isinstance(obj, list):
			for item in obj:
				self.recursive_iterate(item)
		else:
			if hasattr(obj, 'print'):
				self.ls.append(obj.print())
			else:
				print(obj)