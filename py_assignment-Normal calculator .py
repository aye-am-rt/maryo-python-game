yes=['y','Y']
restart='y'
while(restart in yes):
    def calculator(x,y,choice):
        if(choice=='add'):
            result = float(x + y)
            print("sum of ",x," and ",y,"=",end=' ')
            print(result)
            print("\n")
        elif(choice=='substract'):
            result = x-y
            print("substraction of ",x," and ",y,"=",end=' ')
            print(result)
            print("\n")
        elif(choice=='multiply'):
            result = x*y
            print("Multiplication of ",x," and ",y,"=",end=' ')
            print(result)
            print("\n")
        elif(choice=='devide'):
            if(y==0):
                print("Math Error,Can not devide by zero")
                print("\n")
            else:
                result = x/y
                print("division of ",x," and ",y,"=",end=' ')
                print(result)
                print("\n")
        elif(choice=='remainder'):
             if(y==0):
                 print("Math Error,Can not devide by zero")
                 print("\n")
             else:
                 result = x%y
                 print("remainder of ",x," and ",y,"=",end=' ')
                 print(result)
                 print("\n")
    choice =str(input("give your choice among add/substract/multiply/devide/remainder:"))
    avl_choices={'add','substract','multiply','devide','remainder'}
    if(choice in avl_choices):
        x =float(input("input first number"))
        y =float(input("input second number"))
        calculator(x,y,choice)
        restart=str(input("For Reuse,Press 'y'OR 'Y'..To Exit Press 'n'-: "))
        if(restart in ['y','Y','n']):
            continue;
        else:
            print("You should only give 'y','Y' OR 'n'")
            break;
        
    else:
        print("wrong choice,run again or quit!!")
        restart=str(input("For Reuse,Press 'y' To Exit Press 'n'-: "))
        if(restart in ['y','n','Y']==False):
            print("You should only give 'y' or 'n'")
            break;
print("thank you for use,end!!")
