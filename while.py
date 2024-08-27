def da(entLim):
    i = entLim
    while True: 
        print (i)
        i = i - 1
        if i == 0:
            break  


da(10)


def factoria(num):
	i = 2
	tmp = 1
	while i < num + 1:
		tmp = tmp * i
		i = i + 1
	return tmp


print (factoria(4))
print (factoria(5))
print (factoria(6))
