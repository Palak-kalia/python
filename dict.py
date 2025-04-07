d={
    "name":"palak","age":"15","gender":"female"
}
print(d.keys())
print(d.values())
print(d.items())
a={
    "hello":"world","good":"luck"
}
d.update({'123':'04'})
print(d)

print(d.get("name"))

d.popitem()
print(d)

d.clear()
print(d)


