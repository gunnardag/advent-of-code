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
        let divs: Vec::<usize> = get_divisibility(start.to_string());
        for d in divs {
            let mut tmpstart = start.to_string();
            let mut list2: Vec<String> = Vec::new();
            while tmpstart != "" {
                list2.push(tmpstart.to_string()[..d].to_string());
                tmpstart = tmpstart[d..].to_string();
            }
            if all_equal(list2.clone()) {
                range_count += start;
                break;
            }
        }
        start += 1;
    }
    return range_count;
}

fn get_divisibility(number: String) -> Vec<usize> {
    let mut divisibility: Vec<usize> = Vec::new();
    for i in 1..=number.to_string().len() / 2 {
        if number.to_string().len() % i == 0 {
            divisibility.push(i);
        }
    }
    return divisibility;
}

fn all_equal(strings: Vec<String>) -> bool {
    if let Some(first) = strings.first() {
        strings.iter().all(|s| s == first)
    } else {
        true
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
