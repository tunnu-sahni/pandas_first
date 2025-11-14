import pandas as pd

a = [1,3,4,5]

myvar = pd.Series(a)

print(myvar)


import pandas as pd

a = [3,452,2,4]

myvar = pd.Series(a)

print(myvar)


import pandas as pd

a = [3,1,3,4,5]

myvar = pd.Series(a)

print(myvar)


print(myvar[0])


print(myvar[2])


print(myvar[1])



import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)


import pandas as pd

a = [2, 4, 7, 8]

myvar = pd.Series(a, index = ["x", "y", "z", "t"])

print(myvar)



import pandas as pd

a = [1,4,6,8,9]

myvar = pd.Series(a, index = ["b", "c", "d", "e", "f"])

print(myvar)



print(myvar["b"])


print(myvar["e"])


print(myvar["d"])



# key/values objects as series


import pandas as pd

calories = {"day1": 420, "day2": 380, "day3":390}

myvar = pd.Series(calories)

print(myvar)


import pandas as pd

calories = {"day1": 480, "day2": 390, "day3": 700}

myvar = pd.Series(calories)

print(myvar)



import pandas as pd

calories = {"day3": 390, "day4": 690, "day5": 590}

myvar = pd.Series(calories)

print(myvar)



# DataFrame


import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40,45]
}

myvar = pd.DataFrame(data)

print(myvar)