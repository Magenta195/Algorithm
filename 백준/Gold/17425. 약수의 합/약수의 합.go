package main

import (
	"bufio"
	"fmt"
	"os"
)

const maxVal int = 1000001

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
var fval = [maxVal]int{}
var gval = [maxVal]int{}

func initalize() {
	for i := 1; i < maxVal; i++ {
		for j := i; j < maxVal; j += i {
			fval[j] += i
		}
	}
	for i := 1; i < maxVal; i++ {
		gval[i] = gval[i-1] + fval[i]
	}
}

func query() {
	var q, n int
	fmt.Fscanln(reader, &q)
	for i := 0; i < q; i++ {
		fmt.Fscanln(reader, &n)
		fmt.Fprintln(writer, gval[n])
	}
}
func main() {
	defer writer.Flush()
	initalize()
	query()
}
