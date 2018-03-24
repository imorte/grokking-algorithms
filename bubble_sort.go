package main

import (
	"fmt"
)

func main() {
	data := []int{12, 3, 2, 6, 5, 7}

	fmt.Println(bubbleSort(data))
	fmt.Println(bubbleSort1(data))
}

func bubbleSort(data []int) []int {
	slice := make([]int, len(data))
	copy(slice, data)
	for i := 0; i < len(slice)-1; i++ {
		for j := 0; j < len(slice)-1-i; j++ {
			if slice[j] > slice[j+1] {
				slice[j], slice[j+1] = slice[j+1], slice[j]
			}
		}
	}

	return slice
}

func bubbleSort1(data []int) []int {
	slice := make([]int, len(data))
	copy(slice, data)
	for i := 0; i < len(slice); i++ {
		for j := i + 1; j < len(slice); j++ {
			if slice[j] < slice[i] {
				slice[j], slice[i] = slice[i], slice[j]
			}
		}
	}

	return slice
}
