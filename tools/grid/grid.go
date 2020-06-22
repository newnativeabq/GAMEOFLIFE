// Draw, slice, and prepare grid


package main

import "fmt"

type cell struct {
	val bool
	ngb int
}

func generateTiles(x int, y int, z int) [][][]*cell {
	var tiles [][][]*cell

	tiles = make([][][]*cell, x)

	for i := range tiles {
		tiles[i] = make([][]*cell, y)
		for j := range tiles[i] {
			tiles[i][j] = make([]*cell, z)
		}
	}

	return tiles
}

func main() {
	cell1 := cell{
		val: true,
		ngb: 0,
	}

	fmt.Println("Cell", cell1)

	matrix := generateTiles(3, 3, 1)
	fmt.Println("Matirx", matrix)

	sm := matrix[0]
	fmt.Println("Slice 0", sm)

	fmt.Println("Length Matrix - Matrix[0] - Matrix[1]", len(matrix), len(matrix[0]), len(matrix[0][0]))

}
