import random

x = input('Enter your list : ')
y=[0,1,2,3,4]
random.shuffle(y)
print 'The randomized list : '
for i in y:
	print x[i]