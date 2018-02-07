''' Implementation of Don Knuth's Algorithm X aka Dancing Links '''


class colObj:
    '''Algorithm X column header'''
    def __init__(self, leftHdr, rightHdr, upHdr, downHdr, colHdr, size, name):
        self.L = leftHdr
        self.R = rightHdr
        self.U = upHdr
        self.D = downHdr
        self.C - colHdr
        self.size = size
        self.name = name

class Obj:
    '''Algorithm X data object, circular doubly linked list references'''
    def __init__(self, leftObj, rightObj, upObj, downObj, colObj):
        self.L = leftObj
        self.R = rightObj
        self.U = upObj
        self.D = downObj
        self.C = colHeader

''' A 2x2 Latin square can be implemented as [1 2; 2 1] OR [2 1; 1 2]. this
makes it a useful test case. The exact cover map has the form [] '''
