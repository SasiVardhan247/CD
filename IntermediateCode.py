from SymbolTable2 import *

class Operand:
	pass

class Variable(Operand):
	def __init__(self,symbol_entry):
		self.symbol_entry = symbol_entry
	def print(self):
		self.symbol_entry.print()

class Constant(Operand):
	def __init__(self,value):
		self.value = value
	def print(self):
		print(self.value)

class Quadruple:
	def __init__(self, opd1,opd2,result,opcode):
		self.opd1 = opd1
		self.opd2 = opd2
		self.result = result
		self.opcode = opcode
	def getopd1(self):
		return self.opd1
	def print(self):
		# print(self.opd1.print())
		self.opd1.print()
		if(self.opd2 != None):
			self.opd2.print()
		self.result.print()
		print(self.opcode)	