use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut filldb: bool = true;
    let mut db2: Vec<(i64, i64)> = Vec::new();

    let mut count: i64 = 0;
    if let Ok(lines) = read_lines("./input") {
        for line in lines.map_while(Result::ok) {
            if line == "" {
                filldb = false;
                continue;
            }
            if filldb {
                let values: Vec<&str> = line.split("-").collect();
                let a: i64 = values[0].parse::<i64>().unwrap();
                let b: i64 = values[1].parse::<i64>().unwrap();
                db2.push((a,b));
            } else {
                let val: i64 = line.parse::<i64>().unwrap();
                for t in &db2 {
                    if val >= t.0 && val <= t.1 {
                        count += 1;
                        break;
                    }
                }
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

