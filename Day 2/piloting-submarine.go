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
	fileName := "/Users/alex/main/advent-of-code/Day 2/input.txt"
	fileBytes, err := ioutil.ReadFile(fileName)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	navData := strings.Split(string(fileBytes), "\n")
	return navData
}

func partOne(navData []string) int {
	defer timeTrack(time.Now(), "partOne")
	hpoz, depth := 0, 0
	for i := range navData {
		lineData := strings.Split(string(navData[i]), " ")
		moveVal, _ := strconv.Atoi(lineData[1])
		if lineData[0] == "forward" {
			hpoz += moveVal
		} else if lineData[0] == "down" {
			depth += moveVal
		} else {
			depth -= moveVal
		}
	}
	return hpoz * depth
}

func partTwo(navData []string) int {
	defer timeTrack(time.Now(), "partTwo")
	hpoz, depth, aim := 0, 0, 0
	for i := range navData {
		lineData := strings.Split(string(navData[i]), " ")
		moveVal, _ := strconv.Atoi(lineData[1])
		if lineData[0] == "forward" {
			hpoz += moveVal
			depth += aim * moveVal
		} else if lineData[0] == "down" {
			aim += moveVal
		} else {
			aim -= moveVal
		}

	}
	return hpoz * depth
}

func main() {
	nData := readFile()
	fmt.Println(partOne(nData))
	fmt.Println(partTwo(nData))
}
