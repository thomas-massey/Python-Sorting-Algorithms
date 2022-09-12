import random

def return_list(data):
	for y in range(len(data)):
		move_done = False
		for x in range(len(data) - y - 1):
			if data[x] > data[x+1]:
				data[x], data[x+1] = data[x+1], data[x]
				move_done = True
		if not move_done:
			break
	return data

list = [random.randint(0, 1000) for x in range(100)]
print("Sorted = "+ str(return_list(list)))