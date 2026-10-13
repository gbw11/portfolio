scores = {
    'bogem' : 89,
    'sangho' : 100,
    'IU' : 78,
    'sori' : 76,
    'hejun' : 85
}

max = float("-inf")
for key, value in scores.items():
    if value > max:
        max = value
    

for key, value in scores.items():   
    if value == max :
        print(key)
        break