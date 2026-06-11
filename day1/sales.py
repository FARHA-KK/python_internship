
sales=[1200,1500,900,1800,2200,1700,1300]
count=0
total=sum(sales)
high=max(sales)
low=min(sales)
avg=sum(sales)/len(sales)
print("total sales:",total)
print("average sales:",avg)
print("highest sales:",high)
print("lowest sales:",low)
for i in range(len(sales)):
    if sales[i]>1500:
        count+=1
print("number of days where sales exceeded 1500:",count)

        
        
        