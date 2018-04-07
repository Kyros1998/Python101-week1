def example():
    print('basic function')
    z = 2+9
    print(z)


example()#这一步才执行了操作

def simple_addition(num1,num2):
    answer = num1+num2
    print('num1 is',num1)
    print(answer)


    

simple_addition(5,3)#num1 = 5, num2 = 3,且变量之间的数目需要匹配

def simple(num1,num2):
    pass

def simple(num1,num2=5):
    print(num1,num2)

simple(2)#系统有一个default了，一个数就够




def basic_window(width,height,font='TNR',bgc='w',scrollbar=True):
    print(width,height,font,bgc)

basic_window(500,250)#想要跳过font给bgc赋值，就直接写basic_windows（500，250，bgc=‘b’）






x = 6#x如果不是一个global variable，所以后面不能输出x的操作值
def example2():
   global x 
   print(x)
    x+=5
   print(x)

example2()
