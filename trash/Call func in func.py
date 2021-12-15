# block closed by (1- -1) parantesis containts working with functions as classes they are buy passing them to another functions
# block closed by (2- -2) paranthesis contains 2 functions computing integers 2nd and any degrees without multiplication
# block closed by (3- -3) paranthesis contains exploration of how the classes handle implicit and explicit construction - short answer implicit constructors doesn't work
# block closed by (4- -4) paranthesis contains solution for Hanoi Towers problem

#(1-
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


test_1=execute_functions_1

test_2=execute_functions_2

test_3=print_fs

test_1(test_2,test_3)

# -1)

#(2-
def yobnutaya_stepen_dvoyki(val):
    res=0
    for ind in range(0,val):
        res+=val
    print('%d^2=%d' % (val,res))

yobnutaya_stepen_dvoyki(400)

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

#-2)

#(3-
class Employee:  
    """Базовый класс для всех сотрудников"""  
    emp_count = 0  
  
    def __init__(self, name, salary):  
        self.name = name  
        self.salary = salary  
        Employee.emp_count += 1  
  
    def display_count(self):  
        print('Всего сотрудников: %d' % Employee.empCount)  
  
    def display_employee(self):  
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))

class Object:

    title : str
    age : int
    stack_of_values : list
    stack_of_employes : dict


    def __init__(self, title=None, age=0, vals=None, empl=None):
        self.title=title
        self.age=age
        self.stack_of_values=vals
        self.stack_of_employes=empl
        print('Class Object with name %s created' % self.title)

    def __del__(self):
        print('Object named %s is deleted' % self.title)

class Object1:
    title:str
    def __init__(self, title):
        self.title=title
        print('Class Object1 with name %s created' % self.title)

    def __del__(self):
        print('Object1 named %s is deleted' % self.title)

        
a:Object = Object('Dude', 24,[1,2,3,4,],{'Polland':'1',"Brad": "Peat"})
name=['Nate','John']
b:Object1 = name #doesn't create class, beacuse doesnt have this implicity between classes as C++ does or it does itself with first class classes
#also doesn't return mistake of the constructor of class object1, because it just wasn't created
print('b is list containing %s' %b)
#even prints overloaded b, which proves that in order to reduce number of mistake python automaticaly redifines datatype
c:Object1=Object1('Cassandra') #must use explicit cunstroctor for the classes

#-3)

#(4-

def HanoiTower(tower_height: int):
    
    if tower_height>1:
        return 2*HanoiTower(tower_height=tower_height-1)+1
    else:
        return 1

level=int(input('Enter the height of your tower(use integers): '))

print('Height of your tower is',HanoiTower(level))
#-4)