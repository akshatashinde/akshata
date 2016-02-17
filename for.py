names=["a","b","c"]
values=[1,2,3]
f=1
for x in [1,2,3,4]:
    print x
    
for i in range(10):
    print i,i*i,i*i*i
    
for name,value in zip(names,values):
    print name,value
    
#def fact(no1):
#    for i in range(no1-1,1,-1):
#        f*=no1
#        print f
 
 
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num   

a=factorial(5)
print a
              
for n in names[::-1]:
    print n


print "reverse string"
def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]
    
m=reverse("string")
print m    
