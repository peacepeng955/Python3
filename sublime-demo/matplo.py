import pygal
import matplotlib.pyplot as plt
from random import choice
from random import randint


class RandomWalk():
	"""一个生成随机漫步数据的类"""

	def __init__(self,num_points = 30000):
		"""初始化随机漫步的属性"""
		self.num_points = num_points

		# 所有随机漫步都始于(0, 0)
		self.x_values = [0]
		self.y_values = [0]



	def fill_walk(self):
		"""计算随机漫步包含的所有点"""
	
		# 不断漫步，直到列表达到指定的长度
		while len(self.x_values) < self.num_points:
			# 决定前进方向以及沿这个方向前进的距离
			x_direction = choice([1,-1])
			x_distance = choice([0,1,2,3,4])
			x_step = x_direction * x_distance
	
			y_direction = choice([1,-1])
			y_distance = choice([0,1,2,3,4])
			y_step = y_direction * y_distance
	
			# 拒绝原地踏步
			if x_step == 0 and y_step ==0:
				continue
	
			# 计算下一个点的x和y值
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			# print(next_x)
	
			self.x_values.append(next_x)
			self.y_values.append(next_y)



class Die():
	"""表示一个骰子的类"""
	def __init__(self, num_sides = 6):
		"""骰子默认为6面"""
		self.num_sides = num_sides


	def roll(self):
		""""返回一个位于1和骰子面数之间的随机值"""
		return randint(1,self.num_sides)




def matplot():
	squares = [0,3,6,9,12,15,18]
	squares1 = [0,1,4,9,16,25,36]
	xxxx = [0,1,2,3,4,5,6]
	yyyy = [0,1,2,3,4,5,6]
	
	plt.plot(squares,linewidth = 2)
	plt.plot(squares1,linewidth = 2)
	plt.plot(xxxx,yyyy,linewidth = 2)
	
	# 设置图表标题，并给坐标轴加上标签
	plt.title("Squares Number",fontsize = 24)
	plt.xlabel("Vaule",fontsize = 12)
	plt.ylabel("Square of Value",fontsize = 12)
	
	# 设置刻度标记的大小
	plt.tick_params(axis = "both", which = "major", labelsize = 5)
	
	# 自定义颜色,元组分别表示红色、绿色和蓝色分量
	plt.scatter(200,600000,c=(0.9, 0, 0))
	plt.scatter(200,400000,c=(0, 0.9, 0))
	plt.scatter(200,200000,c=(0, 0, 0.9))
	
	x_values = list(range(1,1001))
	y_values = [x**2 for x in x_values]
	
	# 要删除数据点的黑色轮廓，可在调用scatter()时传递实参edgecolor="none".
	# plt.scatter(x_values,y_values,edgecolor="none",s=20)
	plt.scatter(x_values, y_values, c= y_values, cmap=plt.cm.Reds, edgecolor="none", s=20)
	
	
	# 设置每个坐标轴的取值范围
	plt.axis([0,1100,0,1100000])
	

	plt.show()
	# plt.savefig("squares_plot.png",bbox_inches="tight")         #保存图表





def showRandomWalk():
	# while True:
		rw = RandomWalk()
		point_numbers = list(range(rw.num_points))
		rw.fill_walk()
		plt.figure(dpi = 128, figsize = (7,5))               # 设置绘图窗口的尺寸
		plt.scatter(rw.x_values, rw.y_values, edgecolor="none", c=point_numbers, cmap=plt.cm.Blues, s=1)
		
		# 突出起点和终点
		plt.scatter(0,0,c="red",edgecolor="none",s=30)
		plt.scatter(rw.x_values[-1],rw.y_values[-1],c="red",edgecolor="none",s=30)

		plt.show()
		# keep_running = input("Make another walk?(y/n):")
		# if keep_running == "n":
		# 	break



def showDie():
	die = Die()
	results = []
	for roll_num in range(100):
		result = die.roll()
		results.append(result)
	# print(results)

	frequencies = []
	for value in range(1,die.num_sides+1):
		frequencie = results.count(value)
		frequencies.append(frequencie)
	# print(frequencies)

	# 对结果进行可视化
	hist = pygal.Bar()
	hist.title = "Results of rolling one D6 1000 times."
	hist.x_labels = ["1","2","3", "4","5","6"]
	hist.x_title = "Result"
	hist.y_title = "Frequency of Result"

	hist.add("D6",frequencies)
	hist.render_to_file("die_visual.svg")



	die_1 = Die()
	die_2 = Die(10)
	results = []
	for roll_num in range(100):
		result = die_1.roll() + die_2.roll()
		results.append(result)
	print(results)







def main():
	matplot()
	# showRandomWalk()
	# showDie()





if __name__ == "__main__":
	main()











