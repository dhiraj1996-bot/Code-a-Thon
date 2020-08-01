#Question 2
list1 = ["aman","raj","ayush","gracie"]
list2 = ["akshay","rakesh","raj","ram"]


#creating a function to check for duplicate values and then removing them
#and creating list without the duplicate values
def find_common(list1,list2):
    for x in list1:
      for y in list2:
        if x == y :
          list2.remove(x)
          list1.remove(y)


    print(" list1:",list1)
    print(" list2:",list2)
    print(" new_list:",list1+list2)


find_common(list1,list2)

