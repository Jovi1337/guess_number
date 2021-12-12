import random
# random 是一個模組 (module)
# 很多個 module 就變成 package套件 (import 的時候可以整個套件裝進去，或是選擇單一模組) 

r = random.randint(1, 100)
# randint = random integer

while True:
	ans = input('請猜一個數字: ')		# input會把所有東西存成字串
	ans = int(ans)					# 所以要 int
	if ans == r:
		print('恭喜答對!!!   ')
		break
	elif ans > r:
		print('你猜得比答案大')
	elif ans < r:
		print('你猜得比答案小')
		