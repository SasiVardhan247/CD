class Program:
	def __init__(self):
		self.functions = {}		
	
	def addFunctionDetails(self,name, function):
		self.functions[name] = function

	def print(self):
		# print("program:")
		ls = list()
		ls.append("Program :")
		for funname, function in self.functions.items():
			ls.append(function.print())
		return ls

	def getMainFunction(self):
		for funname, function in self.functions:
			if(funname == 'main'):
				return function
    
	# def getFunctionDeatils(self, name):
	# 	if name in functions:
	# 		return functions[name]
	# 