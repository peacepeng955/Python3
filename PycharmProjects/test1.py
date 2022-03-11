from program import make_pizza,build_profile
# 使用星号(* )运算符可让Python导入模块中的所有函数: from program import *


def listtest():
	print("=======字符串=======:")
	recever = "ada lovelace " 
	print(recever.upper())          # 字符串大写
	print(recever.title())          # 字符串首字母大写
	print(recever.rstrip())         # 删除字符串末尾空白
	print(recever.lstrip())         # 删除字符串开头空白
	print(recever.strip())          # 删除字符串两端空白

	
	
	print("========列表========:")
	names = ["Peace", "Bruce", "Jojo", "Gus"]
	# for i in range(0,len(names)):
	# 	print(i,names[i])
	for name in names:
		print(name)
	
	names.append("Mia")				# 在列表末尾增加元素
	print(names)
	
	names.insert(4,"Yulia")			# 在列表的任何位置添加新元素
	print(names)
	
	del names[0]					# 删除列表任意位置的元素
	print(names)
	
	popname = names.pop()			# 删除并弹出列表末尾的元素，也可通过索引弹出列表任意位置元素
	print(popname)
	print(names)
	"""
	如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del 语句;如果你要在删除元
	素后还能继续使用它，就使用方法pop() 。
	"""
	names.remove("Bruce")			# 删除列表中具体的一个元素
	print(names)
	
	cars = ["bmw", "audi", "toyota", "subaru"]
	cars.sort()						# 永久性修改列表元素的排列顺序
	print("cars:\n",cars)
	
	cars.sort(reverse = True)		# 颠倒排序
	print(cars)
	print(sorted(cars))				# 临时性修改列表元素的排列顺序，保留原始列表顺序
	
	print("cars:",cars)
	cars.reverse()					# 反转列表元素的排列顺序
	print("反转列表元素:",cars)		
	
	print("=====数字列表简单的统计计算=====:")
	number = list(range(1,10,2))
	print(number)
	# print(len(number))
	
	squares = []
	# for value in range(1,11):
	# 	squares.append(value**2)
	# print(squares)
	squares = [value**2 for value in range(1,11)] 
	print(squares)
	print(max(squares))
	print(min(squares))
	print(sum(squares))


	print("=====习题4-6=====:")
	num = [value for value in range(1,21,2)]
	print(num)
	num = []
	for i in range(1,21,2):
		num.append(i)
	print(num)
	num = []
	a = []
	num = [value for value in range(3,31)]
	for i in range(0,len(num)):
		if(num[i] % 3 == 0):
			a.append(num[i])
	print(a)
	num = [value**3 for value in range(1,11)]
	print(num)
	num = []
	for i in range(1,11):
		num.append(i**3)
	print(num)
	print("=====习题4-6=====end")


	player_s = ["charles", "martina", "michael", "florence"]
	print(player_s[0:3])
	print(player_s[-3:])
	for player in player_s[0:3]:
		print(player.title())

	print("=========Attention=========:player_ss = player_s是行不通的,只是简单的赋值,不能得到两个列表")
	player_ss = player_s[:]
	print(player_ss)
	player_s.append("Peace")
	print(player_s)
	print(player_ss)

	player_s = ["charles", "martina", "michael", "florence"]
	his_food = player_s
	print(his_food)
	player_s.append("cannoli")
	print(player_s)
	print(his_food)


	print("========元组========:不可变的列表被称为元组")
	# 虽然不能修改元组的元素，但可以给存储元组的变量赋值，可重新定义整个元组.
	tuple1 = (50,100)
	print(tuple1[0])
	print(tuple1[1])




def conditionalTest():
	print("=====条件语句conditional=====:")
	cars = ["audi", "bmw", "subaru", "toyota"]
	for car in cars:
		if car == "bmw":
			print(car.upper())
		elif car == "audi" or car == "subaru" or car == "toyota":
			print(car.title())
		else:
			print("not found")


	name = "Peace"
	age = 26
	high = 165
	weight = 60
	if name == "Peace" and weight > 55 and age > 25:
		print("He is fat in 2021")
	else:
		print(".....")

	car = "subaru"
	print(car == "subaru")
	print(car == "audi")





def dictionaryTest():
	print("========字典========:")
	# 字典是一种动态结构，可随时在其中添加键—值对。要添加键—值对，可依次指定字典名、用方括号括起的键和相关联的值。
	# 对于字典中不再需要的信息，可使用del 语句将相应的键—值对彻底删除。使用del 语句时，必须指定字典名和要删除的键。
	person_Peace = {"name":"Peace" , "age":26 , "high":165}
	print(len(person_Peace))
	print(person_Peace)
	person_Peace["weight"] = 60
	print(person_Peace)
	person_Peace["weight"] = 58
	print(person_Peace)


	for key,value in person_Peace.items():
		print(key + "  " + str(value))
	for key in person_Peace.keys():
		print(key)


	print("========集合========:")
	# 集合类似于列表，但每个元素都必须是独一无二的,且无序的
	for key in set(person_Peace.keys()):
		print(key)

	aliens = []
	for i in range(30):
		new_alien = {"color":"red","point":"5","speed":"slow"}
		aliens.append(new_alien)
	for alien in aliens[:5]:
		print(alien)
	print("Total number of aliens: " + str(len(aliens)))



	identify = build_profile("Peace","peng",
									location="princeton",field="physics")

	print(identify)





def main():
	listtest()
	conditionalTest()
	dictionaryTest()





if __name__ == "__main__":
	main()




