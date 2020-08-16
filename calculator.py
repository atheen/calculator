
def main():
	#write your code here
	first_num = input("Enter the first number: ")
	second_num = input("Enter the second number: ")
	operation = input("Enter the operation(+, -, /, *): ")
	if first_num.isnumeric() == False or second_num.isnumeric() == False:
		print("invalid numbers")
	elif operation != "+" and operation != "-" and operation != "*" and operation != "/":
		print("invalid operation")
	else:
		first_num = int(first_num)
		second_num = int(second_num)
		if operation == "+":
			result = first_num + second_num
		elif operation == "-":
			result = first_num - second_num
		elif operation == "/":
			result = first_num / second_num
		elif operation == "*":
			result = first_num * second_num
	print("The answer is %s"%(result))
	pass




if __name__ == '__main__':
	main()
