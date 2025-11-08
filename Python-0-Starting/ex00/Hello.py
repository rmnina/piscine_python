ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

temp = list(ft_tuple)
temp[1] = "France!"
ft_tuple = tuple(temp)

ft_set.remove("tutu!") #can use discard() as well but it wont raise an error if value doesn't exist
ft_set.add("Paris!")

ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)