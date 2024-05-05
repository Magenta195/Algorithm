package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

var alphabetCount = map[string]int{}
var alphabetFirst = map[string]bool{}

type Alphabets []string

func (a Alphabets) Len() int {
	return len(a)
}

func (a Alphabets) Swap(i, j int) {
	a[i], a[j] = a[j], a[i]
}

func (a Alphabets) Less(i, j int) bool {
	return alphabetCount[a[i]] < alphabetCount[a[j]]
}

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)

	var n int = 0
	var ans int = 0
	fmt.Fscan(reader, &n)

	for i := 0; i < n; i++ {
		var str string = ""
		fmt.Fscan(reader, &str)
		for j, s := range str {
			if j == 0 {
				alphabetFirst[string(s)] = true
			}
			alphabetCount[string(s)] += int(math.Pow(10, float64(len(str)-j-1)))
		}
	}

	alphabet := []string{}
	for key, _ := range alphabetCount {
		alphabet = append(alphabet, key)
	}
	sort.Sort(Alphabets(alphabet))

	if len(alphabet) == 10 {
		for _, a := range alphabet {
			if !alphabetFirst[a] {
				alphabetCount[a] = 0
				break
			}
		}
		sort.Sort(Alphabets(alphabet))
	}
	for i, a := range alphabet {
		ans += alphabetCount[a] * (10 - len(alphabet) + i)
	}
	fmt.Println(ans)
}
