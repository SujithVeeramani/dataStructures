count = 0

def simpleFunction():

    global count

    if count == 5: #base condition
        return 

    print(count)

    count+=1
    
    simpleFunction()



simpleFunction()

 