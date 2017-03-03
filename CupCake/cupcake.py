import math
import string
import re

while True:

	print ("Cupcake cost estimator")
	print ("\n")
	p = re.compile('\d+(\.\d+)?')
	people =  (input('How many people will be been at your event? '))
	while p.match(people) == None or people == '0':
		people = (input('Invalid input, people should not be negative or letters, please enter again: '))
	ingred =  (input('What is the ingredients cost per cupcake? '))
	while p.match(ingred) == None or ingred == '0':
		ingred = (input('Invalid input, cost should not be negative or letters, please enter again: '))

	
	cupcake = float(people) * 1.5
	batches = cupcake / 12
	batches = math.ceil(batches)
	print ('Batches of cupcakes:',batches)
	hour = batches * 2
	print ('Hours of labor:' ,hour)
	in_cost = float(ingred) * batches * 12
	print ('Ingredients cost: $' + '%.2f' % in_cost)
	la_cost = 2 * batches * 30
	round(la_cost, 2)
	print ('Labor cost: $' + '%.2f' % la_cost)
	total_cost = in_cost + la_cost
	print ('Total cost: $' + '%.2f' % total_cost)
	per_cost = total_cost/(batches*12)
	# per_cost = math.ceil(per_cost * 100)/100.00
	print ('Cost per cupcake: $' + '%.2f' % per_cost)
	print ('\n')

	option = input('Would you like to do aother estimate? (y/n)' )
	if option == 'n':
		break
