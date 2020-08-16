
def main():
	#write your code here
	first_num = input("Enter the first number: ")
	second_num = input("Enter the second number: ")
	operation = input("Enter the operation(+, -, /, *): ")

	if first_num.isnumeric() == True and second_num.isnumeric() == True:

		first_num = int(first_num)
		second_num = int(second_num)
		if operation == "+":
			result = first_num + second_num
			print("The answer is %s"%(result))
		elif operation == "-":
			result = first_num - second_num
			print("The answer is %s"%(result))
		elif operation == "/":
			result = first_num / second_num
			print("The answer is %s"%(result))
		elif operation == "*":
			result = first_num * second_num
			print("The answer is %s"%(result))
		else:
			print("invalid operation")
	else:
		print("invalid number")


	pass




if __name__ == '__main__':
	main()
