def my_steps(num):
    
    if num <= 2:
      return num 
    
    if num > 25 or num < 1:
      raise ValueError

    list = [0] * (num)

    list[0] = 1
    list[1] = 2

    for i in range(2,num): 
      list[i] = list[i-1] + list[i-2]

    numofways = list[num-1]

    return numofways







