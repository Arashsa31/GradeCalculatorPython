#@author Arash
#Write a program that reads in a decimal points grades between 0-100 and 
#then converts it to the corresponding letter grade based upon the following table:
#90-100  A
#80-90   B
#70-80   C
#60-70   D
#0-60    F 

print("Enter a score between 0 to 100 to receive the corresponding grade:")
#user input
score = float(input())

#check score for double validity (does not test other exceptions)
while score < 0 or score > 100:
    print("The score you entered is incorrect. You entered the score {}. Please try again.".format(score))
    print("Enter a score between 0 to 100 to receive the corresponding grade:")
    score = float(input())
#convert number to letter grade
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

#print letter grade
print(grade)
