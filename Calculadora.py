
def sum(x,y):
    result=x+y
    print (result)
    return result

def sub(x,y):
    result= x-y
    print (result)
    return result

def mut(x, y):
    result=x*y
    print (result)
    return result

def div(x,y):
    result= x/y
    print (result)
    return result  
    

while True:
    x=int(input("x: "))
    f=str(input("formula: "))
    y=int(input("y: "))
    if(f=="+"):
        sum(x,y)
        print(sum)
        
    elif (f=="-"):
        sub(x,y)
        print (sub)
    elif (f=="x"):
        mut(x,y)
        print(mut)
    elif (f=="/"):
        div(x,y)
        print(div)
    elif(f=="P"):
        print("Espero ter ajudado ;)")
        break
    else:
        print("OPS! Comando desconhecido")
    continue