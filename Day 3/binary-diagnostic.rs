use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::time::Instant;
use std::convert::TryInto;

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
    where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn parse_file() -> Vec<Vec<i32>> {
    let file_name = "./input.txt";
    let mut diagnostic_readings: Vec<Vec<i32>> = Vec::new();
    if let Ok(lines) = read_lines(file_name) {
        for line in lines {
            if let Ok(val) = line {
                let char_vec: Vec<char> = val.chars().collect();
                let mut int_vec: Vec<i32> = Vec::new();
                for c in char_vec.into_iter() {
                   int_vec.push(c.to_digit(2).unwrap().try_into().unwrap());
                }
                diagnostic_readings.push(int_vec);
            }
        }
    }
    return diagnostic_readings;
}

fn inv(val: i32) -> i32 {
    return if val == 1 {
        0
    } else {
        1
    }
}

fn binary_to_decimal(bin_vec: Vec<i32>) -> i64 {
    let str_rep: String = bin_vec.into_iter().map(|i| i.to_string()).collect::<String>();
    let dec_rep = i64::from_str_radix(&str_rep, 2);
    return dec_rep.ok().unwrap();
}

fn most_freq(input_vec: Vec<i32>, do_inv: bool) -> i32 {
    let mut col_sum = 0 as f64;
    let mut most_common: i32 = 0;
    let vec_len_half = input_vec.len() as f64/2 as f64;
    for value in input_vec.iter() {
        col_sum += *value as f64;
    }
    if col_sum > vec_len_half {
        most_common = 1
    } else if col_sum < vec_len_half  {
        most_common = 0
    } else if col_sum == vec_len_half {
        most_common = 1
    }
    if do_inv {
        most_common = inv(most_common)
    }
    return most_common
}


fn filter_array(data: Vec<Vec<i32>>, col_position: usize, filter_value: i32) -> Vec<Vec<i32>> {
    let mut new_data: Vec<Vec<i32>> = Vec::new();
    for row in data.iter() {
        if row[col_position] == filter_value.try_into().unwrap() {
            new_data.push(row.to_vec());
        }
    }
    return new_data;
}


fn system_rating(diag_data: Vec<Vec<i32>>, invert: bool) -> Vec<i32> {
    let mut column_counter = 0;
    let mut filtered_data = diag_data;
    while filtered_data.len() > 1 {
        let mut column_values: Vec<i32> = Vec::new();
        let most_common: i32;
        for row in filtered_data.iter() {
            column_values.push(row[column_counter])
        }
        most_common = most_freq(column_values, invert);
        filtered_data = filter_array(filtered_data, column_counter, most_common);
        column_counter += 1;
    }
    return filtered_data[0].clone();
}

fn part_one() -> i64 {
    let diagnostics = parse_file();
    let n_cols = diagnostics[0].len();
    let mut gamma_store: Vec<i32> = Vec::new();
    let mut epsilon_store: Vec<i32> = Vec::new();
    for i in 0..n_cols {
        let most_common: i32;
        let mut column_values: Vec<i32> = Vec::new();
        for row in diagnostics.iter() {
            column_values.push(row[i])
        }
        most_common = most_freq(column_values, false);
        gamma_store.push(most_common);
        epsilon_store.push(inv(most_common));
    }
    let gamma = binary_to_decimal(gamma_store);
    let epsilon = binary_to_decimal(epsilon_store);
    return gamma * epsilon
}

fn part_two() -> i64 {
    let diagnostics = parse_file();
    let oxygen_binary = system_rating(diagnostics.clone(), false);
    let co2_binary = system_rating(diagnostics.clone(), true);

    let oxygen_rating = binary_to_decimal(oxygen_binary);
    let co2_rating = binary_to_decimal(co2_binary);
    return oxygen_rating * co2_rating
}

fn main() {
    let p1_start = Instant::now();
    println!("Part 1: {}", part_one());
    let p1_duration = p1_start.elapsed();
    println!("Time for part one: {:?}", p1_duration);
    let p2_start = Instant::now();
    println!("Part 2: {}", part_two());
    let p2_duration = p2_start.elapsed();
    println!("Time for part two: {:?}", p2_duration);
}
