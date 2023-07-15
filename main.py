# main.py
# 0,1,1,2,3,5,8,13,21,34,55,89,144

def fibonacci(n):
  if n == 1:
    return 0
  if n == 2:
    return 1
  return fibonacci(n - 2) + fibonacci(n - 1)  
  
n = int(input("Enter a num: "))
print(fibonacci(n))
  
  
    

