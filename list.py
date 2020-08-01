#Question 2
user1 = ["aman","raj","ayush","gracie"]

user2 = ["akshay","rakesh","raj","ram"]

#Merging the given two lists
user_list = user1+ user2


#creating a function to remove the duplicates
#the list is converted into dictionary using the list values as keys and then again
#converting them back into a list which will remove the duplicates
def my_function(x):
  return list(dict.fromkeys(x))

new_list = my_function(user_list)

print(new_list)

