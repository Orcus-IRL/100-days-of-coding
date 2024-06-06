import random
names = ["Alex" ,"Beth", "Caroline" ,"Dave", "Eleanor" ,"Freddie"]
student_score = {name:random.randint(1,100) for name in names}
# student_score = {name:random.randint(1,100) for name in names}
passed_students = {name:mark for (name,mark) in student_score.items() if mark > 50}
# passed_students = {name:mark for (name,mark) in student_score.items() if mark > 50}
# passed_students = {name:mark for (name,mark) in student_score.items() if mark >= 60


weather_c = eval(input())
# 🚨 Don't change code above 👆

weather_f = {key:((value* 9/5) + 32) for (key,value) in weather_c.items()}
# Write your code 👇 below:



print(weather_f)


sentence = input()
# 🚨 Don't change code above 👆
# Write your code below 👇

result = {words:len(words) for words in sentence.split()}


print(result)
