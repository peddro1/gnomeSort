from random import shuffle
import random
import math
import timeit
import matplotlib.pyplot as plt


timeGnome = []
elementos = [10000, 20000, 30000, 40000, 50000, 100000, 200000]

def geraLista(tam):
    
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista



def gnomeSort( arr, n): 
    index = 0
    while index < n: 
        if index == 0: 
            index = index + 1
        if arr[index] >= arr[index - 1]: 
            index = index + 1
        else: 
            arr[index], arr[index-1] = arr[index-1], arr[index] 
            index = index - 1
  
    return arr 
  


def timePopulate():
	for numElementos in elementos:
		base = []
		base = geraLista(numElementos)

	
		_tmp = list(base)
		timeGnome.append(timeit.timeit("gnomeSort({},{})".format(_tmp, numElementos), \
        setup="from __main__ import gnomeSort", \
        number=1))
		

def axis():
	timePopulate()

	
	plt.plot(elementos, timeGnome, label="gnomeSort")
  
def graphic():
	plt.legend(loc='upper center', shadow=True).get_frame().set_facecolor('0.90')
	plt.xlabel('Tamanho(int)')
	plt.ylabel('Tempo(s)')
	plt.show()

def main():
	axis()
	graphic()

if __name__ == "__main__":
	main()
