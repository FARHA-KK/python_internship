def log_call(func):
    def wrapp(*args):
        print("calling function:",func.__name__)
        print("Arguments:",args)
        result=(func(*args))
        print(f"function {func.__name__} completed")
        return result
    return wrapp
@log_call
def add(a,b):
     return a+b
print("The result is:",add(2,3))
@log_call
def greeting(name):
    return f"Hello {name}"
print(greeting("Anu"))
@log_call
def multiply(a,b):
    return a*b
print("The result is:",multiply(4,5))
    
