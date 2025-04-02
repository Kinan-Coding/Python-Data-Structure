grades = [10 , 6 , 5 , 20 , 15 , 0]

# Bubble Sort Algorithm 

# 1) Length for the array
length = len(grades)

# 2) Loop in elements in array
for index in range(0 , length - 1):
    for compare in range(0 , length - index - 1):
        first = grades[compare]
        second = grades[compare + 1]
        if first > second:
            grades[compare] = second
            grades[compare + 1] = first

print(grades)
print("Highest Grade: " + str(grades[-1]))
print("Lowest Grade: " + str(grades[0]))