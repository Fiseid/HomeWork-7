world = 'hello world holla'
world = world.lower()
counted = {}
for i in world:
	if counted.get(i) is None:
		counted[i] = 1
	else:
		counted[i] += 1
print(counted)