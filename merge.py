def sortlist(list):

    for i in range(0, len(list)):
      for j in range(i+1, len(list)):
        if list[i] > list[j]:
          temp = list[i]
          list[i] = list[j]
          list[j] = temp


def merge_list(list1, list2):

    sortlist(list1)
    sortlist(list2)

    size = len(list1) + len(list2)
    idx1 = 0
    idx2 = 0
    idx = 0
    newlist = [0] * size

    while idx1 < len(list1) and idx2 < len(list2):
      if list1[idx1] < list2[idx2]:
        newlist[idx] = list1[idx1]
        idx1 += 1
        idx += 1
      else:
        newlist[idx] = list2[idx2]
        idx2 += 1
        idx += 1

    while idx1 < len(list1):
      newlist[idx] = list1[idx1]
      idx1 += 1
      idx += 1

    while idx2 < len(list2):
      newlist[idx] = list2[idx2]
      idx2 += 1
      idx += 1

    return newlist

