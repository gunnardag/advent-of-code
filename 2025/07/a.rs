use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut l: Vec<usize> = Vec::new();
    let mut count: i64 = 0;
    if let Ok(lines) = read_lines("./input") {
        for line in lines.map_while(Result::ok) {
            if line.contains("S") {
                l.push(line.find("S").unwrap());
            } else {
                let mut n: Vec<usize> = Vec::new();
                for (i, ch) in line.char_indices() {
                    if ch == '^' {
                        if l.contains(&i) {
                            count += 1;
                            n.push(i-1);
                            n.push(i+1);
                            l.retain(|&x| x != i);
                        }
                    }
                }
                for i in l {
                    n.push(i);
                }
                l = n;
                l.sort();
                l.dedup();
            }
        }
    }
    println!("count: {}", count);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

