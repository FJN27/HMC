# CS5, hw1pr1
# Filename: hw1pr1.py
# Name:
# Problem description: Second Python lab, problem 1!

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example problem (problem 0):  [2, 7, 5, 9]

# print index 0 and 1 for array e. print the last two number for array pi
# answer0 = e[0:2] + pi[-2:]  

# print("answer0:", answer0)

# Problem 1: creating [7, 1]
answer1 =   e[1:2] + pi[1:2]
print("answer1:", answer1)

print("")
print("")
print("")

# problem 2:  [9, 1, 1]
answer2 = pi[5:0:-2]
print("answer2", answer2)

# problem 3: [1, 4, 1, 5, 9]
answer3 = pi[1:]
print("answer3:", answer3)


# problem 4: [1, 2, 3, 4, 5]
answer4 = e[2::-2] + pi[0:5:2]
print("answer4:", answer4)

# Lab1 string practice

h = 'harvey'
m = 'mudd'
c = 'college'


# Problem 5:  'hey'
answer5 = h[0] + h[4:6]    
print("answer5:", answer5)

# probelm 6:  Create collude 
answer6 = c[0:4] + m[1:3] + h[-2]
print("answer6:", answer6)

# Problem 7: Create arveyudd
answer7 = h[1:]+m[1:3]+m[3]
print("answer7", answer7)

# problem 8: Create hardeharharhar
answer8 = h[:3]+ m[3] + h[4] + 3*h[:3]
print("answer8:", answer8)

# problem 9. Create legomyego 
answer9 = c[3:6] + c[1] + m[0] + h[5] + c[-2] + c[1]

# Problem 10. Create clearcall 
answer10 = c[0:5:2] + h[1:3] + c[0] + h[1] + 2*c[2]