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

func contains(s []int, val int) (bool, int) {
	for ix, v := range s {
		if v == val {
			return true, ix
		}
	}

	return false, -1
}

func rowAll(row []int) bool {
	for _, val := range row {
		if val != -1 {
			return false
		}
	}
	return true
}

func colAll(board [][]int, colInd int) bool {
	for _, row := range board {
		if row[colInd] != -1 {
			return false
		}
	}
	return true
}

func winningScore(board [][]int, numberCalled int) int {
	var sumUnmarked = 0
	for _, row := range board {
		for _, val := range row {
			if val != -1 {
				sumUnmarked += val
			}
		}
	}
	return sumUnmarked * numberCalled
}

func timeTrack(start time.Time, name string) {
	elapsed := time.Since(start)
	log.Printf("%s took %s", name, elapsed)
}

func readFile() ([]int, [][][]int) {
	fileName := "/Users/alex/main/advent-of-code/Day 4/input.txt"
	fileBytes, err := ioutil.ReadFile(fileName)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	bingoData := strings.Split(string(fileBytes), "\n")
	var calledNumbers []int
	var boardCounter int
	var tempBoard, emptyBoard [][]int
	var boards [][][]int
	for i := range bingoData {
		if i == 0 {
			tmp := strings.Split(bingoData[i], ",")
			for j := range tmp {
				calledNumbers = append(calledNumbers, quietStrConv(tmp[j]))
			}
			continue
		}
		if len(bingoData[i]) == 0 {
			continue
		} else {
			tmpLine := strings.Split(bingoData[i], " ")
			var rowNumbers []int
			for k := range tmpLine {
				if len(tmpLine[k]) == 0 {
					continue
				}
				rowNumbers = append(rowNumbers, quietStrConv(tmpLine[k]))
			}
			tempBoard = append(tempBoard, rowNumbers)
			boardCounter += 1
		}
		if len(tempBoard) == 5 {
			boards = append(boards, tempBoard)
			tempBoard = emptyBoard
		}
	}
	return calledNumbers, boards
}

func partone(numbers []int, boards [][][]int) int {
	for _, val := range numbers {
		for _, board := range boards {
			for _, row := range board {
				var isIn, valPositionCol = contains(row, val)
				if isIn {
					row[valPositionCol] = -1
					if rowAll(row) || colAll(board, valPositionCol) {
						return winningScore(board, val)
					}
				}
			}
		}
	}
	return 0
}

func numElems(sliceSearch []bool) (int, int) {
	var numTrue, numFalse = 0, 0
	for _, elem := range sliceSearch {
		if elem {
			numTrue += 1
		} else {
			numFalse +=1
		}
	}
	return numTrue, numFalse
}

func parttwo(numbers []int, boards [][][]int) int {
	winningBoards := make([]bool, len(boards))
	lastWinningIdx := 0
	var _, numberNotWinning = numElems(winningBoards)
	for k := range winningBoards {
		winningBoards[k] = false
	}
	for _, val := range numbers {
		for i, board := range boards {
			if winningBoards[i] {
				continue
			}
			for _, row := range board {
				var isIn, valPositionCol = contains(row, val)
				if isIn {
					row[valPositionCol] = -1
					if rowAll(row) || colAll(board, valPositionCol) {
						winningBoards[i] = true
						_, numberNotWinning = numElems(winningBoards)
						lastWinningIdx = i
					}
				}
				if numberNotWinning == 0 {
					return winningScore(boards[lastWinningIdx], val)
				}
			}
		}
	}
	return 0
}

func main() {
	fmt.Println(partone(readFile()))
	fmt.Println(parttwo(readFile()))
}
