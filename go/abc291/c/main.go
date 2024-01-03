package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var wr = bufio.NewWriter(os.Stdout)

func main() {
	defer wr.Flush()
	sc.Split(bufio.ScanWords)
	sc.Buffer([]byte{}, math.MaxInt32)
	getI()
	s := getS()
	Map := map[string][]int{"U":{-1,0},
							"D":{1,0},
							"L":{0,-1},
							"R":{0,1}}
	visited := make(map[[2]int]bool)
	visited[[2]int{0,0}] = true
	x,y := 0,0
	for _,i := range s{
		// out(x,y)
		x += Map[string(i)][0]
		y += Map[string(i)][1]
		if visited[[2]int{x,y}]{
			out("Yes")
			return
		} else{
			visited[[2]int{x,y}] = true
		}
	}
	out("No")

	// use getI(), getS(), getInts(), getF()
}

func out(x ...interface{}) {
	fmt.Fprintln(wr, x...)
}

func getI() int {
	sc.Scan()
	i, e := strconv.Atoi(sc.Text())
	if e != nil {
		panic(e)
	}
	return i
}

func getF() float64 {
	sc.Scan()
	i, e := strconv.ParseFloat(sc.Text(), 64)
	if e != nil {
		panic(e)
	}
	return i
}

func getInts(N int) []int {
	ret := make([]int, N)
	for i := 0; i < N; i++ {
		ret[i] = getI()
	}
	return ret
}

func getS() string {
	sc.Scan()
	return sc.Text()
}


// min, max, asub, absなど基本関数

func sum(a ...int) int{
	temp := 0
	for _,v := range a{
		temp += v
	}
	return temp
}

func max(a ...int) int {
	temp := a[0]
	for _,v := range a{
		if temp < v{
			temp = v
		}
	}
	return temp
}

func min(a ...int) int {
	temp := a[0]
	for _,v := range a{
		if temp > v{
			temp = v
		}
	}
	return temp
}



func chmin(a *int, b int) bool {
	if *a < b {
		return false
	}
	*a = b
	return true
}

func chmax(a *int, b int) bool {
	if *a > b {
		return false
	}
	*a = b
	return true
}

func asub(a, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func abs(a int) int {
	if a >= 0 {
		return a
	}
	return -a
}

func lowerBound(a []int, x int) int {
	idx := sort.Search(len(a), func(i int) bool {
		return a[i] >= x
	})
	return idx
}

func upperBound(a []int, x int) int {
	idx := sort.Search(len(a), func(i int) bool {
		return a[i] > x
	})
	return idx
}

