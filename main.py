import argparse
from lexer2 import CTokenLexer
from parser2 import CTokenParser

parser = argparse.ArgumentParser()

parser.usage = "tinyCC [options] file"

parser.add_argument('-tokens',action='store_true',help="Show tokens in file.toks (or out.toks)")
parser.add_argument('-parse',action='store_true',help="Stop processing with parsing")
parser.add_argument('-ast', action='store_true',help="Show abstract syntax trees in file.ast (or out.ast)")
parser.add_argument('-symtab',action='store_true',help="Show symbol table in file.sym (or out.sym)")
parser.add_argument('-compile',action='store_true',help="Compile the program and generate spim code in file.spim (or out.spim)")
parser.add_argument('file',help="TinyC Program")
args = parser.parse_args()

lexer = CTokenLexer()
parser = CTokenParser()
f=open(args.file)
code=f.read()
tokens = lexer.tokenize(code)

# def __init__(self):
# 	self.result=None

args.compile = True  #default value
if args.tokens:
	if tokens:
		tokens_file_name = args.file +".toks"
		tokens_file = open(tokens_file_name,"w")
		# call tokenize and print tokens into tokens_file
		for token in tokens:
			tokens_file.write(f"type={token.type},value={token.value}\n")
	else:
		print("Invalid Code")

if args.parse:
	# call parser, which should not create Program data structure
	args.ast = False
	args.compile = False
	#result.print()
	result = parser.parse(tokens)
	if result:
		print("code accepted")
		result.print()
	else:
		print("errors in code!!! code not accepted")

if args.ast:
	result = parser.parse(tokens)
	if result:
		ast_file_name = args.file +".ast"
		ast_file = open(ast_file_name,"w")
		res=result.print()
		def flatten_nested_code(nested_code, flat_code=None):
			if flat_code is None:
				flat_code = []
			
			for item in nested_code:
				if isinstance(item, list):
					flatten_nested_code(item, flat_code)
				else:
					flat_code.append(item)
			return flat_code
		flat_code = flatten_nested_code(res)
		for fc in flat_code:
			ast_file.write(f"{fc}\n")
	else:
		print("errors in code!!! code not accepted")
	# call parser, creates Program object
	# call program.print(), which should print ast
if args.compile:
	target_code_file_name = args.file +".spim"
	target_code_file = open(target_code_file_name,"w")
    # call parser, creates Program object
    # call program.compile(), which should 
