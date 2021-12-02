use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::time::Instant;

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
    where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn parse_file() -> (Vec<i32>, Vec<String>) {
    let file_name = "./input.txt";
    let mut nav_measures: Vec<i32> = Vec::new();
    let mut nav_type: Vec<_> = Vec::new();
    if let Ok(lines) = read_lines(file_name) {
        for line in lines {
            if let Ok(val) = line {
                let tvec = val.split_whitespace().collect::<Vec<&str>>();
                nav_type.push(tvec[0].to_string());
                nav_measures.push(tvec[1].parse::<i32>().unwrap());
            }
        }
    }
    return (nav_measures, nav_type);
}

fn part_one() -> i32 {
    let (nav_measures, nav_type) = parse_file();
    let mut horizontal = 0;
    let mut depth = 0;
    for i in 0..nav_measures.len() {
        if nav_type[i].to_string() == "forward" {
            horizontal += nav_measures[i];
        } else if nav_type[i].to_string() == "down" {
            depth += nav_measures[i];
        } else {
            depth -= nav_measures[i];
        }
    }
    return depth * horizontal;
}

fn part_two() -> i32 {
    let (nav_measures, nav_type) = parse_file();
    let mut horizontal = 0;
    let mut depth = 0;
    let mut aim = 0;
    for i in 0..nav_measures.len() {
        if nav_type[i].to_string() == "forward" {
            horizontal += nav_measures[i];
            depth += aim * nav_measures[i];
        } else if nav_type[i].to_string() == "down" {
            aim += nav_measures[i];
        } else {
            aim -= nav_measures[i];
        }
    }
    return depth * horizontal;
}

fn main() {
    let p1_start = Instant::now();
    println!("{}", part_one());
    let p1_duration = p1_start.elapsed();
    println!("Time for part one: {:?}", p1_duration);
    let p2_start = Instant::now();
    println!("{}", part_two());
    let p2_duration = p2_start.elapsed();
    println!("Time for part two: {:?}", p2_duration);
}
