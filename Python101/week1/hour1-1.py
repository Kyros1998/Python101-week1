print('This is an example of print function')
print('Hi ','there')
print('Hi',str(5))


exampleVar = 55+32#exampleVar = print('what')
print(exampleVar)

x,y = (3,5)
print(x)
print(y)

condition   = 1
while condition < 10 :
    print (condition)
    condition += 1 #condition = =condition +1
    
'''while True:
    print('doing stuff')#infinite loop'''

exampleList = [1,5,6,1,6,7,8,9,345,53,5]
for x in exampleList:
    print (x)#在下方的其他指令如果首行不空则是单独指令，和此行平行，则会每个数字后运行一次

print('wulala ')


for x in range(1,11):#11是天花板
    print(x)



x =  5
y = 8
z = 5
a = 3


if z<y >x>a:
    print('y is greater than z and greater than x')

if z<=x:#==才是等于,!=不等于
    print('z is less than or equal to x')


x = 5
y = 8

if x > y:
    print('x is greater than y')
else:
    print('x is not greater than y')


x = 5
y = 10
z =  22

if x > y:
    print('x is greater than y')#一旦前面的一个指令是true，不会继续执行
elif x < z:
    print('x is less than z')
elif 5 > 2:
    print('5 is greater than 2')
else:
    print('if and if(s) never ran')
