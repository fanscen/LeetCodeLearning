package main

import "fmt"

func isHappy(n int) bool {
	seen := make(map[int]bool)

	for n != 1 && !seen[n] {
		seen[n] = true
		n = getNext(n)
	}

	return n == 1
}

func getNext(num int) int {
	total := 0
	for num > 0 {
		digit := num % 10
		total += digit * digit
		num /= 10
	}
	return total
}

func main() {
	fmt.Println(isHappy(19))
	fmt.Println(isHappy(2))
}
