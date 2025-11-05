package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func main() {
	// Step 1: Open the file
	f, err := os.Open("input")
	if err != nil {
		fmt.Println(err)
		return
	}

	array1 := make([]int, 0)
	array2 := make([]int, 0)

	// Step 2: Create a reader
	r := bufio.NewReader(f)

	// Step 3: Read line by line
	for {
		line, err := r.ReadString('\n')
		if err != nil {
			break
		}
		result := strings.Split(strings.Replace(line, "\n", "", -1), "   ")

		a, errA := strconv.Atoi(result[0])
		if errA != nil {
			fmt.Println(errA)
			return
		}
		b, errB := strconv.Atoi(result[1])
		if errB != nil {
			fmt.Println(errB)
			return
		}
		array1 = append(array1, a)
		array2 = append(array2, b)
	}
	slices.Sort(array1)
	slices.Sort(array2)

	// Calculate first part
	sumA := 0
	i := 0
	for i < len(array1) {
		diff := array1[i] - array2[i]
		sumA = sumA + max(diff, -diff)
		i++
	}
	fmt.Println("Part one:")
	fmt.Println(sumA)
	fmt.Println("---------")

	sumB := 0
	j := 0
	for j < len(array1) {
		similarity := array1[j] * countOccurrences(array2, array1[j])
		sumB = sumB + similarity
		j++
	}
	fmt.Println("Part two:")
	fmt.Println(sumB)
	fmt.Println("---------")

	// Step 4: Close the file
	defer f.Close()
}

func countOccurrences(slice []int, value int) int {
	count := 0
	for _, v := range slice {
		if v == value {
			count++
		}
	}
	return count
}
