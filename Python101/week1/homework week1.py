def my_fx(x , y , z):
 if x > y:
    t = x
 else:
    t = y
 if t > z:
    return t
 else:
    return z

print(my_fx(9,7,11))



def my_test(x,y):
    i = 1
    x=20
    y=25
    while i<min(x,y):
        if x/i==0 and y/i==0:
            print(i)
        else :
            i+=1






file_input = open("sentences.txt","r").readlines()
for m in range(0,10 ):
    print(file_input[m])


doMe = 'hello\nNew world\nEnjoy everyday'
appendFile = open("sentences.txt","a")
appendFile.write(doMe)
appendFile.flush()
appendFile.close()
