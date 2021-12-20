package main
import (
	_ "encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	_ "strconv"
	"strings"
	"time"
)

func quietStrConv(strTo string) int {
	asInt, _ := strconv.Atoi(strTo)
	return asInt
}

func timeTrack(start time.Time, name string) {
	elapsed := time.Since(start)
	log.Printf("%s took %s", name, elapsed)
}

func readFile() ([][][]int, int, int) {
	fileName := "/Users/alex/main/advent-of-code/Day 5/test-input.txt"
	fileBytes, err := ioutil.ReadFile(fileName)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	navData := strings.Split(string(fileBytes), "\n")
	var allCoords [][][]int
	var maxX, maxY int
	for i := range navData {
		var coordFrom, coordTo []int
		var coordPair [][]int
		lineToCoord := strings.Split(navData[i], " -> ")
		cFromStr := strings.Split(lineToCoord[0], ",")
		cFX := quietStrConv(cFromStr[0])
		cFY := quietStrConv(cFromStr[1])
		coordFrom = append(coordFrom, cFX)
		coordFrom = append(coordFrom, cFY)
		cToStr := strings.Split(lineToCoord[1], ",")
		cTX := quietStrConv(cToStr[0])
		cTY := quietStrConv(cToStr[1])
		coordTo = append(coordTo, cTX)
		coordTo = append(coordTo, cTY)
		coordPair = append(coordPair, coordFrom)
		coordPair = append(coordPair, coordTo)
		allCoords = append(allCoords, coordPair)
		if cFX > maxX { maxX = cFX }
		if cFY > maxY { maxY = cFY }
		if cTX > maxX { maxX = cTX }
		if cTY > maxY { maxY = cTY }
	}
	return allCoords, maxY, maxY
}

func minAndMax(a int, b int) (int, int) {
	if a > b {
		return b, a
	} else if b > a {
		return a, b
	}
	return a, b
}

func numElemsCond(board [][]int, condValue int) int {
	var numCond = 0
	for _, row := range board {
		for _, numb := range row {
			if numb >= condValue {
				numCond += 1
			}
		}
	}
	return numCond
}

func lineGrad(coordA []int, coordB []int, diagC bool) (bool, string, float64) {
	var x1, x2 = coordA[0], coordB[0]
	var y1, y2 = coordA[1], coordB[1]
	if (x2 - x1) == 0 {
		return true, "y", 10000
	}
	var grad float64 = float64((y2 - y1) / (x2 - x1))
	if grad == 0 {
		return true, "x", grad
	}
	if diagC {
		if grad == 1 {
			return true, "diag", grad
		}
	}
	return false, "", grad
}

func partone(coordList [][][]int, maxX int, maxY int) (int, [][]int) {
	var blankBoard [][]int
	for i := 0; i <= maxY+1; i++ {
		var tmpRow []int
		for j := 0; j <= maxX+1; j++ {
			tmpRow = append(tmpRow, 0)
		}
		blankBoard = append(blankBoard, tmpRow)
	}
	for _, coord := range coordList {
		startC := coord[0]
		endC := coord[1]
		isVorH, lineDirection, _ := lineGrad(startC, endC, false)
		if isVorH {
			if lineDirection == "x" {
				startX, endX := minAndMax(startC[0], endC[0])
				fixedY := startC[1]
				for i := startX; i <= endX; i++ {
					blankBoard[fixedY][i] += 1
				}
			}
			if lineDirection == "y" {
				startY, endY := minAndMax(startC[1], endC[1])
				fixedX := startC[0]
				for i := startY; i <= endY; i++ {
					blankBoard[i][fixedX] += 1
				}
			}
		}
	}
	return numElemsCond(blankBoard, 2), blankBoard
}

func parttwo(coordList [][][]int, maxX int, maxY int) int {
	_, partialBoard := partone(coordList, maxX, maxY)
	for _, coord := range coordList {
		startC := coord[0]
		endC := coord[1]
		isVorH, lineDirection, _ := lineGrad(startC, endC, true)
		if isVorH && lineDirection == "diag" {
			diffX := startC[0] - endC[0]
			diffY := startC[1] - endC[1]
			var xstep, ystep int = 1,1
			var xcs, ycs []int
			if diffX > 0 {
				xstep = -1
				for i := startC[0]; i > endC[0]+xstep; i += xstep {
					xcs = append(xcs, i)
				}
			} else {
				for i := startC[0]; i < endC[0]+xstep; i += xstep {
					xcs = append(xcs, i)
				}
			}
			if diffY > 0 {
				ystep = -1
				for i := startC[1]; i > endC[1]+ystep; i += ystep {
					ycs = append(ycs, i)
				}
			} else {
				for i := startC[1]; i < endC[1]+ystep; i += ystep {
					ycs = append(ycs, i)
				}
			}
			for j := range xcs {
				partialBoard[ycs[j]][xcs[j]] += 1
			}
		}
	}
	fmt.Println(partialBoard)
	fmt.Println(numElemsCond(partialBoard, 2))
	return 0
}

func main() {
	var coords, maxX, maxY = readFile()
	var partoneAns, _ = partone(coords, maxX, maxY)
	fmt.Println(partoneAns)
	parttwo(coords, maxX, maxY)
}
