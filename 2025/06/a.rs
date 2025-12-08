use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut db: Vec<Vec<i64>> = Vec::new();

    let mut count: i64 = 0;
    if let Ok(lines) = read_lines("./input") {
        for line in lines.map_while(Result::ok) {
            let mut arr: Vec<i64> = Vec::new();
            let values: Vec<&str> = line.split(" ").collect();
            let mut index: usize = 0;
            for v in values {
                if v == "" {
                    continue;
                } else if v == "+" {
                    count += db.iter().fold(0, |acc, x| acc + x[index]);
                } else if v == "*" {
                    count += db.iter().fold(1, |acc, x| acc * x[index]);
                } else {
                    arr.push(v.parse::<i64>().unwrap());
                }
                index += 1;
            }
            db.push(arr);
        }
        println!("Sum: {}", count);
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

