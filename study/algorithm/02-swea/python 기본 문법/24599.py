d= dict()

d["HI"] = [1, 2, 3, "KFC1"]
d["OH"] = [1, 5, {"HO" : 14, "MY" : 119, "QQ" : "KFC2"}]
d[-153] = [(1, 2, (5, 6, "KFC3"))]


print(d["HI"][3])
print(d["OH"][2]["QQ"])
print(d[-153][0][2][2])