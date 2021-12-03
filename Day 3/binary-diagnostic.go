package main
import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"strings"
	"time"
)

func timeTrack(start time.Time, name string) {
	elapsed := time.Since(start)
	log.Printf("%s took %s", name, elapsed)
}

func readFile() [][]string {
	fileName := "/Users/alex/main/advent-of-code/Day 3/input.txt"
	fileBytes, err := ioutil.ReadFile(fileName)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	diagData := strings.Split(string(fileBytes), "\n")
	var diagSlice [][]string
	for i := range diagData {
		tmp := strings.Split(diagData[i], "")
		diagSlice = append(diagSlice, tmp)
	}
	return diagSlice
}

func mostFrequent(arr []int, invert bool) int { // assuming no tie
	m := map[int]int{}
	var maxCnt int
	var freq int
	for _, a := range arr {
		m[a]++
		if m[a] > maxCnt {
			maxCnt = m[a]
			freq = a
		}
	}
	if invert && freq == 0 {
		return 1
	} else if invert && freq == 1 {
		return 0
	}
	return freq
}

func binaryToDecimal(binaryStore []int) int64 {
	stringRep, _ := json.Marshal(binaryStore)
	cleanString := strings.Replace(string(stringRep), ",", "", -1)
	cleanestString := strings.Trim(cleanString, "[]")
	decimalVal, _ := strconv.ParseInt(cleanestString, 2, 64)
	return decimalVal
}

func checkTies(valueList []int) bool {
	arrSum := 0
	for _, a := range valueList {
		arrSum = arrSum + a
	}
	if float64(arrSum) == float64(len(valueList))/2 {
		return true
	}
	return false
}

func filterArray(dataToFilter [][]string, colToFilter int, valueToFilter int) [][]string {
	var newData [][]string
	for i := range dataToFilter {
		thisVal, _ := strconv.Atoi(dataToFilter[i][colToFilter])
		if thisVal == valueToFilter {
			newData = append(newData, dataToFilter[i])
		}
	}
	return newData
}

func strArrToIntArr(toConvert []string) []int {
	var newSlice []int
	for i := range toConvert {
		intVal, _ := strconv.Atoi(toConvert[i])
		newSlice = append(newSlice, intVal)
	}
	return newSlice
}

func systemRating(diagData [][]string, invert bool) []int {
	var filteredData = diagData
	columnCounter := 0
	for len(filteredData) > 1 {
		var columnValues []int
		var mostCommon int
		for i := range filteredData {
			thisVal, _ := strconv.Atoi(filteredData[i][columnCounter])
			columnValues = append(columnValues, thisVal)
		}
		isTied := checkTies(columnValues)
		if isTied && invert {
			mostCommon = 0
		} else if isTied && !invert {
			mostCommon = 1
		} else {
			mostCommon = mostFrequent(columnValues, invert)
		}
		filteredData = filterArray(filteredData, columnCounter, mostCommon)
		columnCounter += 1
	}
	return strArrToIntArr(filteredData[0])
}

func partOne(diagData [][]string) int64 {
	defer timeTrack(time.Now(), "partOne")
	nCols := len(diagData[0])
	var gammaStore []int
	var epsilonStore []int
	for i := 0; i < nCols; i++ {
		var columnValues []int
		for j := range diagData {
			thisVal, _ := strconv.Atoi(diagData[j][i])
			columnValues = append(columnValues, thisVal)
		}
		mostCommon := mostFrequent(columnValues, false)
		gammaStore = append(gammaStore, mostCommon)
		if mostCommon == 1 {
			epsilonStore = append(epsilonStore, 0)
		} else {
			epsilonStore = append(epsilonStore, 1)
		}
	}
	gamma := binaryToDecimal(gammaStore)
	epsilon := binaryToDecimal(epsilonStore)
	return gamma * epsilon
}

func partTwo(diagData [][]string) int64 {
	defer timeTrack(time.Now(), "partTwo")
	oxygenBinary := systemRating(diagData, false)
	co2Binary := systemRating(diagData, true)

	oxygenRating := binaryToDecimal(oxygenBinary)
	co2Rating := binaryToDecimal(co2Binary)

	return oxygenRating * co2Rating
}


func main() {
	depthData := readFile()
	fmt.Println(partOne(depthData))
	fmt.Println(partTwo(depthData))
}
