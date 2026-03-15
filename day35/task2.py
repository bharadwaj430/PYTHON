# print a string "Hi I'm Bharadwaj gupta studying Btech IT with 65%"
#fun(name="Bharadwaj",course="Btech", branch="IT", perc=65%)

def fun(fname,lname):
    print("Hi Im"+" "+fname+" "+lname)
fun(fname='bharadwaj',lname='gupta')

def fun1(fn,ln):
    print("Hlo"+ fn + ln)
fun1('how',  'are you')

def fun(*names):#*args
    return "Hi my name is"+ "satish " 

print(fun("a","b","c","d"))


def fun1(**names):
    return "Hi my name is"+" "+names["lname"]
print(fun1(fname="bharat",lname="kumar"))


    