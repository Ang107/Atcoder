import sys
import collections
from collections import deque
from copy import deepcopy
from itertools import product
sys.setrecursionlimit(10**7)
deq = deque()
l = []
dic = {}
dd = collections.defaultdict(int)

def array2(i,j,element):
    return [[element] * j] * i

def for_input(n):
    L = []
    for _ in range(n):
        L.append(tuple(map(int,input().split())))
    return L

#n = int(input())

#a,b = map(int,input().split())
    

    
    


