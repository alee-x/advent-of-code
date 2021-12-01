package main
import (
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

func readFile() []string {
	fileName := "/Users/alex/main/advent-of-code/Day 1/challenge1-input.txt"
	fileBytes, err := ioutil.ReadFile(fileName)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	depthData := strings.Split(string(fileBytes), "\n")
	return depthData

}

func partOne(depthData []string) int {
	defer timeTrack(time.Now(), "partOne")
	numIncreasing := 0
	for i := range depthData {
		if i == len(depthData)-1 {
			break
		}
		firstVal, _ := strconv.Atoi(depthData[i])
		secondVal, _ := strconv.Atoi(depthData[i+1])
		if firstVal < secondVal {
			numIncreasing += 1
		}
	}
	return numIncreasing
}

func partTwo(depthData []string) int {
	defer timeTrack(time.Now(), "partTwo")
	numIncreasing := 0
	for i := range depthData {
		if i == len(depthData)-3 {
			break
		}
		firstWindowSum := sumStrings(depthData[i], depthData[i+1], depthData[i+2])
		secondWindowSum := sumStrings(depthData[i+1], depthData[i+2], depthData[i+3])
		if firstWindowSum < secondWindowSum {
			numIncreasing += 1
		}
	}
	return numIncreasing
}

func sumStrings(s1 string, s2 string, s3 string) int {
	s1int, _ := strconv.Atoi(s1)
	s2int, _ := strconv.Atoi(s2)
	s3int, _ := strconv.Atoi(s3)
	return s1int + s2int + s3int
}

func main() {
	depthData := readFile()
	fmt.Println(partOne(depthData))
	fmt.Println(partTwo(depthData))
}
