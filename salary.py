print("enter the basic salary of employee")
bs = float (input())
hra = (20 * bs) / 100
da = (15 * bs) / 100
ts = bs + hra + da
print("total salary is", ts)
