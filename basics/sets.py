# set = collection which is unordered, unindexed. no allow duplicated values

utensils = {"ut1", "ut2", "ut3", "ut4", "ut5", "news"}
dishes = {"dishe1", "dishe2", "dishe3", "dishe4", "dishe5", "ut4"}

# utensils.add("napkin")
# utensils.remove("fork")
dishes.update(utensils)
dinner_table = utensils.union(dishes)

for x in dishes:
    print(x)

print(dinner_table)
print(dishes.difference(utensils))
print(dishes.intersection(utensils))