a = 'My name Alex \n'
b = 'Im 21 years old \n'
c = 'I love games \n'
d = 'And i love beer \n'

with open ('test.txt', 'w') as tx:
    s = tx.write(str(a))
    print(s)

with open ('test.txt', 'a+') as tx:
    j = tx.write(b)
    print(j)
    tx.close()

with open ('test.txt', 'a+') as tx:
        j = tx.write(c)
        f = tx.write(d)
        print(j,f)
        tx.close()



    
