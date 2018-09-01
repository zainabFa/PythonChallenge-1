Types = ['Car', 'Device', 'Fruit', 'Sport']
Things = ['Apple', 'Tennis', 'Computer', 'Mercedes']
things = sorted(Things)



list = []
for i in things:
    for j in Types:
        if i == 'Apple' and j == 'Fruit':
            list.append([i , j])
        elif i == 'Computer'  and j == 'Device':
            list.append([i, j])
        elif i == 'Mercedes' and j == 'Car':
            list.append([i,j])
        elif i == 'Tennis' and j == 'Sport':
            list.append([i, j])
            myDict = dict(list)
            print(" myDict=" , myDict)






