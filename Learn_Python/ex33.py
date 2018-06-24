
def create_num_list(start_num, end_num,x):
    i = start_num
    numbers = []
    while i < end_num:
      print ("At the top i is % d" % i)
      numbers.append(i)

      i = i + x
      print ("Numbers now: ", numbers)
      print ("At the bottom i is %d" % i)

    print ("The numbers: ")

    for num in numbers:
        print (num)

create_num_list(1, 20,2)
