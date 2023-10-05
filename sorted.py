def sort_dictionary(dict):
    list = []

    for i in dict:
      tuple = (i, dict[i][0])
      list.append(tuple)

    list.sort()
    
    return list
