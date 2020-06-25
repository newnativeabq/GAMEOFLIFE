"""
Grid Mechanics
"""

import numpy as np
import random




class Cell():
    def __init__(self, val=0, ngb=0, rand=True):
        if rand:
            self.val = random.randint(0,1)
        else:
            self.val = 0
        self.ngb = 0

    def __str__(self):
        return f'{self.val}-{self.ngb}'

    def advance(self):
        if self.ngb < 2 or self.ngb > 3:
            self.val = 0
        elif self.ngb == 3:
            self.val = 1




class ConvolveSquare():
    def __init__(self, base_matrix):
        self.mat = np.full_like(base_matrix[0], fill_value=False)
        self.mx = len(base_matrix[0][0])
        self.my = len(base_matrix[0])
        self.igrid = np.array([
            [-1, 1], [0, 1], [1, 1],
            [-1, 0], [0, 0], [1, 0],
            [-1, -1], [0, -1], [1, -1]
        ])
    

    def _return_valid_coord(self, coord):
        # print(f'test valid {coord} vs ({self.mx}, {self.my})')
        if coord[0] >= 0 and coord[0] < self.mx:
            if coord[1] >= 0 and coord[1] < self.my:
                # print('Valid')
                return coord 
        # print('Not Valid')
        return None



    def _build_indices(self, x, y):
        # print(f'index for {x} {y}; ')
        tcoord = np.array([x, y])
        return [
            self._return_valid_coord(tcoord + icoord) for icoord in self.igrid
        ]



    def _build_indexer(self, indexes, origin=None):
        mask = self.mat.copy()
        for dex in indexes:
            if dex is not None:
                x = dex[0]
                y = dex[1]
                mask[y][x] = True

        if origin is not None:
            mask[origin[1]][origin[0]] = False

        return mask.astype(bool)



    def __call__(self, x, y, vals=None):
        indexes = self._build_indices(x, y)
        indexer = self._build_indexer(indexes, origin=(x,y))
        return indexer




class Board():
    def __init__(self, x:int, y:int, z:int, rand=False):
        self.mat = buildMatrix(x, y, z, rand)
        self.ck = ConvolveSquare(self.mat)
        self.analyze_board()

        self.mx = x
        self.my = y
        self.mz = z

        self.zeros = np.zeros_like(self.mat)



    def iterfunc(self, func, layers:list=None):
        if layers is None:
            layers = range(self.mz)

        for z in layers:
            for y in range(self.my):
                for x in range(self.mx):
                    func(self.mat[z][y][x], coord=(x,y,z))


    def analyze_board(self, layers=None):
        if layers is None:
            count_neighbors(arr=self.mat[0], ck=self.ck)


    def advance(self, layers=None):
        def _advance_cell(cell, **kwargs):
            cell.advance()

        self.iterfunc(_advance_cell, layers)
        self.analyze_board()
    


    def _get_cell(self, coord):
        x, y, z = coord
        return self.mat[z][y][x]



    def set_cell_value(self, coord, value):
        cell = self._get_cell(coord)
        cell.val = value



    @property
    def values(self):
        temp = self.zeros.copy()
        for z in range(self.mz):
            for y in range(self.my):
                for x in range(self.mx):
                    temp[z][y][x] = self.mat[z][y][x].val
        return temp


    
    @property
    def neighbors(self):
        temp = self.zeros.copy()
        for z in range(self.mz):
            for y in range(self.my):
                for x in range(self.mx):
                    temp[z][y][x] = self.mat[z][y][x].ngb
        return temp








def buildMatrix(x: int, y: int, z:int, rand=False) -> list:
    def _build_z():
        return np.array([_build_board() for _ in range(z)])
    
    def _build_row():
        return np.array([Cell(rand) for _ in range(x)])

    def _build_board():
        return np.array([_build_row() for _ in range(y)])

    def _build_all():
        return _build_z()
    
    return np.array(_build_all())





def sliceMatrix(m: list, z) -> list:
    max_z = len(m)
    assert z <= max_z, "Z index out of range"
    return m[z]



def list_coords(arr):
    coords = []
    xs = np.arange(len(arr[0]))
    for j in range(len(arr)):
        coords.extend(
            list(zip(xs, [j]*len(arr)))
        )
    return coords




def count_neighbors(arr: list, ck):
    coords = list_coords(arr)
    for coord in coords:
        x = coord[0]
        y = coord[1]
        cell = arr[y][x]
        cell.ngb = sum(
            [c.val for c in arr[ck(x,y)]]
        )

    return coords




# if __name__ == "__main__":
#     board = Board(5,5,2)
#     m = board.mat

#     ck = ConvolveSquare(m)

#     # print('ck', ck(0,2))

#     count_neighbors(m[0], ck)
#     # count_neighbors(m[1], ck)

#     print('values')
#     print(board.values[0])
#     print('neighbors')
#     print(board.neighbors[0])
#     board.advance(layers=[0])
#     print(board.values[0])

