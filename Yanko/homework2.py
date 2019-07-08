
# Задача1
def f(x,y):
    if x>0 and y>0:
        print("I")
    elif x<0 and y>0:
        print("II")
    elif x<0 and y<0:
        print("III")
    elif x>0 and y<0:
        print("IV")
    else:
        print("undefined")

# Задача2
def ul(a,b,c):
    return ("<ul>" + a+b+c + "</ul>")
print (ul("My ","name ","Andrew"))

def li(x):
    return("<li>" +x+ "</li>")
print(li("Hello!"))

# Задача3
