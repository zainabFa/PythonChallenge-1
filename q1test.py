files = { 'Input.txt': 'Randy',
'Code.py': 'Stan',
'Output.txt': 'Randy',
'test.py': 'Ali',
'djangoweb.py' : 'Ali'
}


dd ={}
for key ,val in files.items():

    dd[val] =dd.get((val), []) + [key]


print (dd)








