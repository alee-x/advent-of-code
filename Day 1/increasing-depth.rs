#![feature(array_windows)]
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

fn parse_file() -> Vec<i32> {
    let file_name = "./challenge1-input.txt";
    let mut depth_measures: Vec<i32> = Vec::new();
    if let Ok(lines) = read_lines(file_name) {
        for line in lines {
            if let Ok(val) = line {
                depth_measures.push(val.parse().unwrap());
            }
        }
    }
    return depth_measures;
}

fn part_one(depth_measures: Vec<i32>) -> i32 {
    let mut number_increases = 0;
    for i in 0..depth_measures.len()-1 {
        if depth_measures[i] < depth_measures[i+1] {
            number_increases += 1;
        }
    }
    return number_increases;
}

fn part_two(depth_measures: Vec<i32>) -> i32 {
    let mut number_increases = 0;
    const N: usize = 3;
    let iter = depth_measures.array_windows::<N>();
    let mut windowed_vec: Vec<i32> = Vec::new();
    for it in iter {
        let window_sum = it[0] + it[1] + it[2];
        windowed_vec.push(window_sum);
    }
    for i in 0..windowed_vec.len()-1 {
        if windowed_vec[i] < windowed_vec[i+1] {
            number_increases += 1;
        }
    }
    return number_increases;
}

fn main() {
    let p1_start = Instant::now();
    println!("{}", part_one(parse_file()));
    let p1_duration = p1_start.elapsed();
    println!("Time for part one: {:?}", p1_duration);
    let p2_start = Instant::now();
    println!("{}", part_two(parse_file()));
    let p2_duration = p2_start.elapsed();
    println!("Time for part two: {:?}", p2_duration);
}
