use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut dial = 50;
    let mut count = 0;
    if let Ok(lines) = read_lines("./input") {
        for line in lines.map_while(Result::ok) {
            let prev = dial;
            let movement = &line[1..].parse::<i32>().unwrap();
            match line.chars().next() {
                Some('R') => dial = dial + movement,
                Some('L') => dial = dial - movement,
                _ => println!("nada"),
            }
            // If we start from 0 we jut check how many roations we go
            if prev == 0 {
                count = count + (dial.abs() / 100);
                dial = dial % 100;
            } else {
                if dial <= 0 {
                    count = count + (dial.abs() / 100); // We check how many whole rotations we go
                    count = count + 1; // Additionally we register the first passing of the 0
                    dial = dial % 100;
                } else if dial > 99 {
                    count = count + (dial / 100); // We check how often we passed 100
                    dial = dial % 100;
                }
            }
            if dial < 0 {
                dial = dial + 100; // reset the dial between 0 - 99
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
