def my_steps(num):
    
    if num < 1 or num > 25:
      raise ValueError

    if num <= 2:
      return num 

    list = [0] * (num)

    list[0] = 1
    list[1] = 2

    for i in range(2,num): 
      list[i] = list[i-1] + list[i-2]

    numofways = list[num-1]

    return numofways







