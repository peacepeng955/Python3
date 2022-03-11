import program
# 使用星号(* )运算符可让Python导入模块中的所有函数: from program import *


def userinput():
	# name = input("Please enter your name: ")
	# print("Hello, " + name + "!")
	# print("Nice to meet you")

	prompt = "If you tell us who you are, we can personalize the messages you see." 
	prompt += "\nWhat is your first name? "
	print(prompt)

	age = input("How old are you?\n")
	print(type(age))
	age = int(age)
	print(type(age))

	while age >= 18:
		print("Wlecome to bar")
		break
	else:
		print("Go out!!! Now")
	# age = ""
	# while age != "18":
	# 	age = input("How old are you? ")
	# 	if age != "18":
	# 		print("print your age again")


	unconfirmed_users = ["peace" , "alex" , "gus" , "yulia"]
	confirmed_users = []
	while unconfirmed_users:
		current_user = unconfirmed_users.pop(0)
		print("Verifying user: " + current_user.title())
		confirmed_users.append(current_user)
	for confirmed_user in confirmed_users:
		print(confirmed_user.title())


	confirmed_users = ["peace" , "alex" , "peace" , "gus" , "yulia" , "peace"]
	print(confirmed_users)
	while "peace" in confirmed_users:
		confirmed_users.remove("peace")
	print(confirmed_users)



	identify = program.build_profile("Peace","peng",
									location="princeton",field="physics")

	print(identify)




def get_formatted_name(first, last, middle=""): 
	"""生成整洁的姓名"""
	if middle:
		full_name=first+" "+middle+" "+last 
	else:
		full_name = first + " " + last 
	return full_name.title()





def main():
	userinput()





if __name__ == "__main__":
	main()




# def make_pizza(size , *toppings):
# 	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
# 	for topping in toppings:
# 		print("- " + topping)
# 	# 形参名*toppings 中的星号让Python创建一个名为toppings 的空元组，并将收到的所有值都封装到这个元组中。传递过去的参数可以是一个，也可以是多个。
# 	# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。


# def build_profile(first, last, **user_info):
# 	profile = {}
# 	profile['first_name'] = first
# 	profile['last_name'] = last
# 	for key, value in user_info.items():
# 		profile[key] = value
# 	return profile
# 	# 形参**user_info 中的两个星号让Python创建一个名为user_info 的 空字典，并将收到的所有名称—值对都封装到这个字典中。






