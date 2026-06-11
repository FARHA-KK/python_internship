import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        print("start time:",start)
        result=func(*args,**kwargs)
        end=time.time()
        print("end time:",end)
        print("exicution time:",end-start)
        return result
    return wrapper
@timer

def counter(n):
    count=0
   
    for i in range(n):
         count+=1
    return count
counter(1000000)     
         
