# name = "kinan"
# age = 17
# money = 560
# happy = True

# person = ['kinan', 17 , 560 , True]


# Dictionary (Hash Table)

persons =  [{'name':'kinan' , 'age':17 , 'money':560.75 , 'happy':True} , 
            {'name':'ammar' , 'age':17 , 'money':150.75 , 'happy':False},
            {'name':'david' , 'age':99 , 'money':1000 , 'happy':False}
            ] #Array Of Dictionaries


for index in range(0, len(persons)):
    print(persons[index]['name'])