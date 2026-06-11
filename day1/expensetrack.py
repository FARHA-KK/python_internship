expense=[]
for i in range(7):
    exp=float(input(f"Enter expense of day {i+1}: "))
    expense.append(exp)
total=sum(expense)
avg=sum(expense)/7
high=max(expense)
low=min(expense)
print("total expense:",total)
print("avrage expense:",avg)
print("highest expense:",high)
print("lowest expense:",low)
