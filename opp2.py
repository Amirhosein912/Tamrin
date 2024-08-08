# a = (1,2,3,4,5,6,7)
# myiterator = iter(a)
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# # print(next(myiterator))

# def myFor (a):
#     myiterator = iter(a)
#     while True:        
#         try:            
#             print(next(myiterator))      
#         except StopIteration:
#             break

# b = [1,2,3,4,5,6,7]
# myFor(b)


# n = [i for i in range(10) ]
# n = iter(n)
# print(next(n))
# print(next(n))
# print(next(n))


# n= (i for i in range(9))
# print(next(n))
# print(next(n))
# print(next(n))

# def greating(name):
#     return name

# print(greating("Amir"))

# def say_hello(s):
#     return s

# def greating(name):    
#     return say_hello(name)

# print(greating("Amir"))


# def greating(name):    
#     def say_hello(s):
#         return s
#     return say_hello(name)

# print(greating("Amir"))


# def greating(name):    
#     def say_hello():
#         return name
#     return say_hello

# a = greating("Amir")
# print(a())



# def greating(f):    
#     def say_goodbye():
#         print("goodBye")
#         f()    
#     return say_goodbye

# def say_hello():
#     print("hello ")

# a = greating(say_hello)
# a()

def greating(f):    
    def say_goodbye(name):
        print("goodBye")
        f(name)    
    return say_goodbye

@greating
def say_hello(name):
    print("hello")

say_hello("amir")
