def my_steps(num: int):
    
    if num <= 2:
      return num 
    
    if num > 25 or num < 0:
      return 0

    list = [0] * (num)

    list[0] = 1
    list[1] = 2

    for i in range(2,num): 
      list[i] = list[i-1] + list[i-2]
  
    return list[num-1]







