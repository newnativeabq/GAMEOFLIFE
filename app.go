package main

import (
	"fmt"
)


func main() {
	fmt.Println("Main App")
	matrix := bm.generateTiles(3, 3, 1)

	fmt.Println("Matrix ", matrix)
}