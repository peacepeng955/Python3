import json
import csv
import unittest
from test2 import get_formatted_name
from program import AnonymousSurvey

file_name = "/Users/peace/Desktop/peace/peace/python/datefile/pi_digits.txt"
file_name2 = "/Users/peace/Desktop/peace/peace/python/datefile/pi_digits2.txt"
file_name3 = "/Users/peace/Desktop/peace/peace/python/datefile/numbers.json"
file_name4 = "/Users/peace/Desktop/peace/peace/python/datefile/zdateCPK.csv"

	# 得先用open()打开文件，这样才能访问它。关键字 with 在不再需要访问文件后将其关闭。
def file_reader():
	# with open(file_name) as file_object:
	# 	contents = file_object.read()
	# 	print(contents)

	with open(file_name) as file_object:
		lines = file_object.readlines()
	for line in lines:
		# print(line)
		print(line.strip())
	"""使用关键字with时，open()返回的文件对象只在with代码块内可用。如果要在with代码块外访问文件的内容，可在with代码块内将文件的各行
		存储在一个列表中，并在with代码块外使用该列表"""



def file_writer():
	# 写入文件
	action = input("write something")
	with open(file_name2, "w") as file_object:
		file_object.write(action)
	"""在这个示例中，调用open()时提供了两个实参。第一个实参也是要打开的文件的名称;第二个实参("w")告诉Python，我们要以写入模式 
		打开这个文件。打开文件时，可指定读取模式 ("r")、写入模式 ("w")、附加模式 ("a")或让你能够读取和写入文件的模式("r+")。如果
		你省略了模式实参，Python将以默认的只读模式打开文件。如果你要写入的文件不存在，函数open()将自动创建它.然而,以写入("w")模式
		打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件。"""
	"""以附加模式打开文件时，Python不会在返回文件对象前清空文件，而你写入到文件的行都将添加到文件末尾。如果指定的文件不存在，
		Python将为你创建一个空文件。"""


def json_dump():
	json_number = [1,2,3,4,5,6,7,8]
	with open(file_name3,"w") as fs_obj:
		json.dump(json_number,fs_obj)



def json_load():
	with open(file_name3) as fs_obj:
		num = json.load(fs_obj)
	print(num)



def py_csvData():
	with open(file_name4) as f:
		highs = []
		reader = csv.reader(f)
		# print(reader)
		header_row = next(csv.reader(f))
		print(header_row)
		# for index,column_header in enumerate(header_row):
		# 	print(index,column_header)
		for value in reader:
			print(value)
			highs.append(value[0])
		print(highs)





def save_user():
	user_name = input("What is your name?")
	with open(file_name3,"w") as fil_obj:
		json.dump(user_name,fil_obj)
	print("We'll remember you when you come back, " + user_name + "!")







def import_AnonymousSurvey():
	question = "What language did you first learn to speak?"
	my_survey = AnonymousSurvey(question)
	my_survey.show_question()
	response = "English"
	my_survey.store_response(response)
	my_survey.show_result()



class TestAnonymousSurvey(unittest.TestCase):
	def test_store_single_response(self):
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		my_survey.store_response("French")
		self.assertEqual(my_survey.responses[0], "French")



class NameTestCase(unittest.TestCase):
	"""docstring for NameTestCase"""
	def test_first_last_name(self):
		formatted_name = get_formatted_name("janis","joplin")
		self.assertEqual(formatted_name,"Janis Joplin")

	def test_first_middle_name(self):
		formatted_name = get_formatted_name("wolf","tiger","mozart")
		self.assertEqual(formatted_name,"Wolf Mozart Tiger")
# 方法名必须以 test_ 打头，这样它才会在我们运行 main函数时自动运行.








def main():
	# file_reader()
	# # file_writer()
	# json_dump()
	# json_load()
	py_csvData()

	# save_user()
	import_AnonymousSurvey()

	





if __name__ == "__main__":
	main()
	print("======割割割割割割割=======")
	unittest.main()





# =============unittest Module中的断言方法=================:
# |		方法					|	用途
# |	assertEqual(a, b)		|核实a == b
# |	assertNotEqual(a, b)	|核实a != b
# |	assertTrue(x)			|核实x 为True
# |	assertFalse(x)			|核实x 为False
# |	assertIn(􏰍􏰌􏰅􏰀item, list􏰄􏰍􏰋􏰌)	|核实item在list􏰋􏰌中
# |	assertNotIn(􏰍􏰌􏰅􏰀item, list􏰄􏰍􏰋􏰌)	|核实item不在list􏰋􏰌中










