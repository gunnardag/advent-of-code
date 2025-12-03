use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut count = 0;
    if let Ok(lines) = read_lines("./input") {
        for line in lines.map_while(Result::ok) {
            let mut max = 0;
            for i in 0..line.len() {
                for j in i+1..line.len() {
                    let k: i32 = format!("{}{}", line.chars().nth(i).unwrap(), line.chars().nth(j).unwrap()).parse().expect("EKKI NúMER");
                    if k > max {
                        max = k;
                    }
                }
            }
            count +=max;
        }
        println!("count: {}", count);
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
