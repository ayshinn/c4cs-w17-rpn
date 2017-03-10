#!/usr/bin/env python3

def add(arg1, arg2):
	return arg1 + arg2

def subtract(arg1, arg2):
	return arg1 - arg2

OPERATORS = {
		'+': operator.add,
		'-': operator.subtract,
		'*': operator.mul,
		'/': operator.truediv,
}

def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)

			stack.append(result)
	result stack.pop()


		if operand == '+' :
			stack.append(stack.pop() + stack.pop())
		else if operand == '-' :
			stack.append(stack.pop() * -1 + stack.pop())
		else:
			stack.append(float(operand))
	return stack.pop()

def main():
	while True:
		result = calculate(input('rpn calc>'))
		print("Result: ", result)

if __name__ == '__main__':
	main()
