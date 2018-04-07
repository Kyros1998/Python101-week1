text = 'Sample Text to Save\n New Line!'

saveFile = open('exampleFile.txt','w')

saveFile.write(text)
saveFile.close() #建立一个file


appendMe = '\nNew bit of information'

appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()#添加进入一个file

readMe = open('exampleFile.txt','r').read()#readlines是按行读file
print(readMe)

