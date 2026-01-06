items= { "apple ","banana", "tomato" }
items.add("orange")
print(items)

items.update({"mango", "Peach"})
print(items)
items.remove("banana")
print(items)
items.discard("tomatos")
print(items)

a =items.pop()

print(a)

b={1,2,3}

c={4,3,5}
result=b.union(c)
print(result)
result=b.intersection(c)
print(result)