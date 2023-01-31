import sys 
def square(x):
	return x**2

if __name__=='__main__':
	num = int(input("Entrer un entier :  "))
	result = square(num)
	print("le carré de ", num, " est ", result)

