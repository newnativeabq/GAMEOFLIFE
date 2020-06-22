// Draw, slice, and prepare grid


package main

import (
	"fmt"
	"reflect"
)





type Cell struct {
	val int
	ngb int
}




func generateTiles(x int, y int, z int) [][][]*Cell {
	var tiles [][][]*Cell

	tiles = make([][][]*Cell, x)

	for i := range tiles {
		tiles[i] = make([][]*Cell, y)
		for j := range tiles[i] {
			tiles[i][j] = make([]*Cell, z)
		}
	}


	for m := range tiles {
		for n := range tiles[m] {
			for r := range tiles[m][n] {
				tiles [m][n][r] := {0, 0}
			}
		}
	}

	return tiles
}


// func getLayerVal(ar [][][]Cell, z int) [][][]*int {
// 	var x, y int
	
// 	y = len(ar)
// 	x = len(ar[0])
	
// 	m = make([y][x]int, y)

// 	for i := range m {
// 		for j := range m[i] {
// 			m[i][j] = ar[i][j]
// 		}
// 	} 

// 	return m
// }




func main() {
	cell1 := Cell{
		val: 0,
		ngb: 0,
	}

	fmt.Println("Cell", cell1)

	matrix := generateTiles(3, 3, 1)
	fmt.Println("Matirx", matrix)

	sm := matrix[0]
	fmt.Println("Slice 0", sm, reflect.TypeOf(sm))

	fmt.Println("Slice 0[0]", sm[0], reflect.TypeOf(sm[0]))

	fmt.Println("Slice 0[0][0]", sm[0][0], reflect.TypeOf(sm[0][0]))
	fmt.Println("Cell Value From Slice", sm[0][0].val)

	fmt.Println("Length Matrix - Matrix[0] - Matrix[1]", len(matrix), len(matrix[0]), len(matrix[0][0]))

}
