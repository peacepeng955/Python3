def make_pizza(size , *toppings):
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
	# 形参名*toppings 中的星号让Python创建一个名为toppings 的空元组，并将收到的所有值都封装到这个元组中。传递过去的参数可以是一个，也可以是多个。
	# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。


def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	# 形参**user_info 中的两个星号让Python创建一个名为user_info 的 空字典，并将收到的所有名称—值对都封装到这个字典中。



class Dog_behavior():
	"""docstring for dog_behavior"""

	def __init__(self, name , age):
		"""初始化属性name和age"""
		# super(dog_behavior, self).__init__()
		self.name = name
		self.age = age
		

	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title() + " is now sitting.")


	def roll_over(self):
		"""模拟小狗被命令时打滚""" 
		print(self.name.title() + " is now sitting.")


# my_dog = Dog_behavior("willie", 6)
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")

# my_dog.sit()





class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type


	def describe_restaurant(self):
		print("This restaurant'name is " + self.restaurant_name + " and type is " + self.cuisine_type)

	def open_restaurant(self):
		print("Today is opening")




# 父类
class AutoCar():
	def __init__(self, make, model, year): 
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year 
		self.odometer_reading = 0

	def get_descriptive_name(self): 
		"""返回整洁的描述性信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		"""将里程表读数设置为指定的值,禁止将里程表读数往回调"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def fill_gas_tank(self):
		print("111111111111")




# 子类
class ElectricCar(AutoCar):
	def __init__(self, make, model, year): 
		"""初始化父类的属性"""
		super().__init__(make, model, year)
		self.battery = Battery()

	def fill_gas_tank(self):
		# 对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。为此，可在子类中定义一个这样的方法，即它与要重写的父类方法同名。
		print("222222222222")




class Battery():
	# "将实例当作属性来用"
	def __init__(self,battery_size = 70):
		"""初始化电瓶的属性"""
		self.battery_size = battery_size

	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kwh battery")





class AnonymousSurvey():
	def __init__(self,question):
		self.question = question
		self.responses = []

	def show_question(self):
		print("question: " + self.question)

	def store_response(self,new_response):
		self.responses.append(new_response)

	def show_result(self):
		print("Survey result:")
		for response in self.responses:
			print("---" + response)






def main():
	my_dog = Dog_behavior("willie", 6)
	print("My dog's name is " + my_dog.name.title() + ".")
	print("My dog is " + str(my_dog.age) + " years old.")
	my_dog.sit()

	restaurant1 = Restaurant("KFC", "snack")
	restaurant2 = Restaurant("Chinese food", "rice")
	restaurant3 = Restaurant("noodles", "noodles")

	restaurant1.describe_restaurant()
	restaurant2.describe_restaurant()
	restaurant3.describe_restaurant()

	print("\n----------父类子类------------:")
	my_tesla = ElectricCar("tesla", "model s", 2016)
	print(my_tesla.get_descriptive_name())
	my_tesla.update_odometer(60)
	my_tesla.read_odometer()
	my_tesla.fill_gas_tank()

	my_tesla.battery.describe_battery()




if __name__ == "__main__":
	main()







