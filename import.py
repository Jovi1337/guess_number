import random
# random 是一個模組 (module)
# 很多個 module 就變成 package套件 (import 的時候可以整個套件裝進去，或是選擇單一模組) 

r = random.randint(1, 100)
# randint = random integer

count = 0 	# 猜了幾次

while True:
	count = count + 1 	# count += 1 也是一樣意思
	ans = input('請猜一個數字: ')		# input會把所有東西存成字串
	ans = int(ans)					# 所以要 int
	if ans == r:
		print('恭喜答對!!!   ')
		print('這是你猜的第', count, '次')
		break
	elif ans > r:
		print('你猜得比答案大')
	elif ans < r:
		print('你猜得比答案小')
	print('這是你猜的第', count, '次')
