use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;


fn main() {
    let mut count: u64 = 0;
    if let Ok(lines) = read_lines("./input") {
        for line in lines.map_while(Result::ok) {
            count += process_line(line);
        }
    }
    println!("Count final: {}", count);
}

fn process_line(mut line: String) -> u64 {
    let mut process_count = 0;
    if line.len() == 0 {
        return 0;
    }
    if &line[line.len()-1..] == "," {
        line = line[..line.len()-1].to_string(); 
    }
    let ranges: Vec<&str> = line.split(',').collect();
    for range in ranges {
        println!("{}", range);
        let range_parts: Vec<&str> = range.split('-').collect();
        let start: u64 = range_parts[0].parse().expect("not a number");
        let end: u64 = range_parts[1].parse().expect("not a number");
        process_count += process_range(start, end);
    }
    return process_count;
}

fn process_range(mut start: u64, end: u64) -> u64 {
    let mut range_count = 0;
    while start <= end {
        if start.to_string().len() % 2 == 0 {
            let mid = start.to_string().len() / 2;
            if &start.to_string()[..mid] == &start.to_string()[mid..] {
                range_count += start;
            }
        }
        start += 1;
    }
    return range_count;
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
