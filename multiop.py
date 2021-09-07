First_num = int(input())
Second_num = int(input())

Mul = First_num * Second_num
Sum = First_num + Second_num
Sub = First_num - Second_num
Div = First_num / Second_num

print(Sum, Sub, Mul, Div)

f = open("results.txt","w")
f.write(str(Sum))
f.write(str(Sub))
f.write(str(Mul))
f.write(str(Div))
f.close
