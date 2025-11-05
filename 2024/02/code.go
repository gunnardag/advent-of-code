package main

import (
	"bufio"
	"fmt"
	"os"
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

	// Step 2: Create a reader
	r := bufio.NewReader(f)

	safe := 0

	// Step 3: Read line by line
	for {
		line, err := r.ReadString('\n')
		if err != nil {
			break
		}

		line2 := strings.Replace(line, "\n", "", -1)
		result := strings.Split(line2, " ")

		array1 := make([]int, 0)
		for i := 0; i < len(result); i++ {
			a, err := strconv.Atoi(result[i])
			if err == nil {
				array1 = append(array1, a)
			} else {
				fmt.Printf("Error converting result[%d] ('%s') to int: %v\n", i, a, err)
			}
		}
		// Part 1
		// if checkReport(array1) {
		//   safe++
		// }

		// Part 2
		if checkTolererantlyReport(array1) {
			safe++
		}
	}

	fmt.Println(safe)

	defer f.Close()
}

func checkTolererantlyReport(slice []int) bool {
	if checkReport(slice) {
		return true
	}
	for i := 0; i < len(slice); i++ {
		newslice := append([]int{}, slice[:i]...)
		newslice = append(newslice, slice[i+1:]...)
		if checkReport(newslice) {
		return true
		}
	}
	return false
}

func checkReport(slice []int) bool {
	var increase bool = slice[1]-slice[0] > 0
	result := true
	for i := 0; i < len(slice)-1; i++ {
		if increase {
			if !check(slice[i], slice[i+1]) {
				result = false
			}
		} else {
			if !check(slice[i+1], slice[i]) {
				result = false
			}
		}
	}
	return result
}

func check(a int, b int) bool {
	if b-a <= 3 && b-a > 0 {
		return true
	}
	return false
}
