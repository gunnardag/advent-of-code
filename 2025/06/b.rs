use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut db: Vec<String> = Vec::new();

    let mut count: i64 = 0;
    let mut len: usize = 0;
    if let Ok(lines) = read_lines("./input") {
        // Here we fill our database
        for line in lines.map_while(Result::ok) {
            if len==0 {
                len = line.len();
            }
            db.push(line);
        }

        // Here we check each index, fill each problem and calculate when we have nothing going on
        let mut work: Vec<i64> = Vec::new();
        let mut a: String = "".to_string();
        for i in 0..len {
            let mut nr_str: String = "".to_string();

            for d in &db {
                nr_str += &d.chars().nth(i).expect("out of bounds").to_string();
            }

            // If string is empty, the problem has been filled, we calculate and reset
            // else we continue gathering info for each problem
            if nr_str.trim() == "".to_string() { 
                count += calculate(work, a);
                work = Vec::new();
                a = "".to_string();
            } else {
                if nr_str.contains("*") || nr_str.contains("+") {
                    a = nr_str.pop().unwrap().to_string();
                }
                work.push(nr_str.trim().parse::<i64>().unwrap());
            }
        }
        // we can't forget the last problem
        count += calculate(work, a);
    }
    println!("{}", count);
}

fn calculate(db: Vec<i64>, v: String) -> i64 {
    if v == "+" {
        return db.iter().fold(0, |acc, x| acc + x);
    } else if v == "*" {
        return db.iter().fold(1, |acc, x| acc * x);
    }
    return 0;
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

