# list datastructure
my_list=["porsche", "Rolls", "Range", "Mercedes", "Ferrari", 56 ,True]
my_list.append("Bentley")

print(type(my_list))
print(my_list[2])
my_list[4]="Bugatti"
print(f"{my_list[4]} is manufactured in Italy")
# numbers list

num_list=["100", "200", "300", "400", "500", "600"]
num_list.insert(1, "600")
print(num_list)

print(type(my_list))
# tuple datastructure

my_tuple=("Banana","apple","mangoes","pears","watermelon")
print(my_tuple)
print(len(my_tuple))
this_tuple=("Albert",)
print(this_tuple)
# my_tuple[0]="grapes"
print(f"I like eating a {my_tuple[0]} ")

# set datasructure
my_set={"Germany","Dubai","Maldives","Bucharest","Iceland"}
print(my_set)

# dictionary datastructure
my_dict = {"name": "Albert", "Age": 18,"Gender": "Male"}
print(my_dict)
print(my_dict["Age"])
print(f"My name is {my_dict['name']} and I'm {my_dict['Age']}")