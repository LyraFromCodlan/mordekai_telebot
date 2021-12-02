def execute_functions_1(func_11,func_12):
    print('First execution start')
    func_11(func_12)
    print('execute_functions_1 end')

def execute_functions_2(func_21):
    print('Second execution start')
    print('Enter value: ')
    value=input()
    func_21(value)
    print('execute_functions_2 end')
    
def print_fs(a):
    print('Here is your vaue:',a)


# test_1=execute_functions_1

# test_2=execute_functions_2

# test_3=print_fs

# test_1(test_2,test_3)

# def yobnutaya_stepen_dvoyki(val):
#     res=0
#     for ind in range(0,val):
#         res+=val
#     print('%d^2=%d' % (val,res))

# yobnutaya_stepen_dvoyki(400)

result=0
val,dg=[int(el) for el in input().split()]
tval=val

def yobnutaya_stepen(tval, deg):
    global result
    if deg==0:
        return 1,1
    elif deg==1:
        return tval,tval
    if deg>2:
        result,tval=yobnutaya_stepen(tval,deg-1)
        for ind in range(1,val):
            result=result+tval
    elif deg==2:
        for ind in range(0,val):
            result=result+tval
    tval=result
    return result,tval
ans=yobnutaya_stepen(val,dg)
print('%d^%d=%d' % (val,dg,ans[0]))