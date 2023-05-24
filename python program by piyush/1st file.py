# calling a function
'''def my_function():
    print('hello I am from india')
my_function()'''


#### argument
'''def my_function(fname):
    print(fname + ' refres')
my_function('email')
my_function('tobies')
my_function('linus')'''

###number of argument
'''def my_function(fname,lname):
    print(fname + ' ' + lname)
my_function('email', 'refses')'''

### arbitary argument *arg
'''def my_function(*kids):
    print('the youngest child' + kids[2])
my_function('email','linus', 'piush')'''

#### keyward argumeent
'''def my_function(child1,child2,child3):
    print('the youngest child is' + child3)
my_function(child1 = 'piyush',child2 = 'laksh', cild3='dev')'''

#### defalut parameter value
'''def my_function(country = 'india'):
    print('i am from ' + country)
my_function('india')
my_function('uk')
my_function('russia')'''

###passing a list argument
'''def my_function(food):
    for x in food:
        print(x)
fruits = ['apple','mango','orange']
my_function(fruits)'''

#return value
'''def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(4))
print(my_function(5))'''
