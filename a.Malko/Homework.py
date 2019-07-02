def coordinat(x,y):
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
coordinat(-1,0)

# f("3","4") => "7"
# f("5","6") => "11"
def sum_str(x,y):
    sum = int(x)+int(y)
    print(str(sum))
sum_str(1,2)