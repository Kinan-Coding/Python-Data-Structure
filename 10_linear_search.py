def linearSearch(array , query):
    for i in range(0, len(array)):
        if array[i] == query:
            return i    
    return -1

grades = [3 , 5 , 12 , 10 , 4]
search = 12

result = linearSearch(grades,search)
if  result == -1:
    print("Not Found")
else:
    print('Element Found')