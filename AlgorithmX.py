''' Implementation of Don Knuth's Algorithm X aka Dancing Links '''
import numpy as np

class colObj:
    '''Algorithm X column header'''
    def __init__(self, leftHdr, rightHdr, upHdr, downHdr, colHdr, size, name):
        self.L = leftHdr
        self.R = rightHdr
        self.U = upHdr
        self.D = downHdr
        self.C = colHdr
        self.size = size
        self.name = name

class Obj:
    '''Algorithm X data object, circular doubly linked list references'''
    def __init__(self, data, leftObj, rightObj, upObj, downObj, colObj):
        self.data = data
        self.L = leftObj
        self.R = rightObj
        self.U = upObj
        self.D = downObj
        self.C = colObj

def Asgn2LL(array):
    '''Assign given array to a circular, doubly linked list'''
    LinkedList = []
    n,m = np.shape(array)
    for rowI, row in enumerate(array):
        for itemI, item in enumerate(row):
            LinkedList.append(Obj(item, row[itemI-1], row[(itemI+1)%m], array[rowI-1][itemI], array[(rowI+1)%n][itemI], itemI))

    return LinkedList
''' A 2x2 Latin square can be implemented as [1 2; 2 1] OR [2 1; 1 2]. this
makes it a useful test case. The exact cover map has the form [] '''

L_sq = np.array([[1,2], [2, 1]])

LatinList = Asgn2LL(L_sq)

print('Complete')
