import sys
import timeit
import random

MAX = 999999 #elementos que serao sorteados

def radixsort(v):
    radix = 10
    maxLen = False
    aux = -1
    placement = 1
 
    while not maxLen:
      maxLen = True
      buckets = [list() for _ in range(radix)]
 
      for i in v:
        aux = i // placement
        buckets[aux % radix].append(i)
        if maxLen and aux > 0:
          maxLen = False
 
      a = 0
      for b in range(radix):
        buck = buckets[b]
        for i in buck:
          v[a] = i
          a += 1

      placement *= radix

def trocar(v, i, j):
    aux = v[i]
    v[i] = v[j]
    v[j] = aux

def particao(v, esq, dir):
    pivo = v[esq] 
    i = esq 
    j = dir+1
    while(True):
        i+=1
        while v[i] < pivo:
            if i >= dir: break
            i+=1
        j-=1
        while v[j] > pivo:
            if j <= esq: break
            j-=1
        if i >= j : break
        trocar(v,i,j)
    trocar(v,esq,j)
    return j

def quickSortIterative(v,low,high):
    size = high - low + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
 
    while top >= 0:
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
 
        p = particao(v, low, high)
 
        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1
 
        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high

def insertionSort(v):
    for i in range (1, len(v)):
        k = v[i]

        j = i-1
        while j >= 0 and k < v[j]:
            trocar(v, j+1, j)
            j -= 1

def randomSeq(tam):
    v = [0]*tam
    for x in range(0, tam):
        v[x] = random.randint(0, MAX)
    return v

def shuffleSeq(tam):
    v = [x for x in range(0, tam+1)]
    random.shuffle(v)
    return v

def testeQuickSort(vTeste, N):
    v = vTeste[:]
    quickSortIterative(v, 0, N-1)
    del v

def testeInsertionSort(vTeste):
    v = vTeste[:]
    insertionSort(v)
    del v
  

def testeRadixSort(vTeste):
    v = vTeste[:]
    radixsort(v)
    del v

def main():
    vTeste = [10]*100000 #vetor de teste
    N = len(vTeste)
    rep = 10
    while rep > 0:
        t1 = timeit.timeit(lambda: testeQuickSort(vTeste, N), number = 1)
        print (t1)
        t2 = timeit.timeit(lambda: testeInsertionSort(vTeste), number = 1)
        print (t2)
        t3 = timeit.timeit(lambda: testeRadixSort(vTeste), number = 1)
        print (t3)
        rep -= 1

if __name__ == '__main__':
    main()



