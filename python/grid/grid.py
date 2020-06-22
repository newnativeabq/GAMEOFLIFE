"""
Grid Mechanics
"""

import numpy as np





class Cell():
    def __init__(self, val=0, ngb=0):
        self.val = 0
        self.ngb = 0

    def __str__(self):
        return f'{self.val}-{self.ngb}'

    def advance(self):
        if self.ngb < 2 or self.ngb > 3:
            self.val = 0
        elif self.ngb == 3:
            self.val = 1




class ConvolveSqure():
    def __init__(self, base_matrix):
        self.m = np.full_like(m[0], fill_value=False)
        self.mx = len(m[0])
        self.my = len(m)
        self.igrid = np.array([
            [-1, 1], [0, 1], [1, 1],
            [-1, 0], [0, 0], [1, 0],
            [-1, -1], [0, -1], [1, -1]
        ])
    

    def _return_valid_coord(self, coord):
        if coord[0] >= 0 and coord[0] <= self.mx:
            if coord[1] >=0 and coord[1] <= self.my:
                return coord 
        return None



    def _build_indices(self, x, y):
        return [
            self._return_valid_coord((x+c[0], y+c[1])) for c in self.igrid
        ]


    def _build_indexer(self, indexes, origin=None):
        mask = self.m.copy()
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







def buildMatrix(x: int, y: int, z:int) -> list:
    def _build_z():
        return np.array([_build_board() for _ in range(z)])
    
    def _build_row():
        return np.array([Cell() for _ in range(x)])

    def _build_board():
        return np.array([_build_row() for _ in range(y)])

    def _build_all():
        return _build_z()
    
    return np.array(_build_all())





def sliceMatrix(m: list, z) -> list:
    max_z = len(m)
    assert z <= max_z, "Z index out of range"
    return m[z]



def _list_coords(arr):
    coords = []
    xs = np.arange(len(arr[0]))
    for j in range(len(arr)):
        coords.extend(
            list(zip(xs, [j]*len(arr)))
        )
    return coords




def count_neighbors(m: list):
    # flatten slice
    mz = sliceMatrix(m, 0)
    coords = _list_coords(mz)
    # build indexer

    return coords




if __name__ == "__main__":
    m = buildMatrix(3, 3, 2)

    ck = ConvolveSqure(m)

    print(m[0][ck(0,2)])

    # print(count_neighbors(m))
