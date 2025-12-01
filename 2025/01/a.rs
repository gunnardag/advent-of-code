use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut dial = 50;
    let mut count = 0;
    if let Ok(lines) = read_lines("./input") {
        for line in lines.map_while(Result::ok) {
            match line.chars().next() {
                Some('R') => dial = dial + &line[1..].parse::<i32>().unwrap(),
                Some('L') => dial = dial - &line[1..].parse::<i32>().unwrap(),
                _ => println!("nada"),
            }
            dial = dial % 100;
            if dial < 0 {
                dial = dial + 100;
            }
            if dial == 0 {
                count = count + 1;
            }
        }
        println!("{}", count);
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
