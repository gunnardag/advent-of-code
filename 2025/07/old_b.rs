use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut paths: Vec<String> = Vec::new();
    let mut count: i64 = 0;
    if let Ok(lines) = read_lines("./input") {
        for line in lines.map_while(Result::ok) {
            if line.contains("S") {
                paths.push(line.find("S").unwrap().to_string());
            } else {

                // find indexes of all the splitters
                let splitters: Vec<usize> = line.char_indices().filter_map(|(i, ch)| {
                    if ch == '^' {
                        Some(i)
                    } else {
                        None 
                    }
                }).collect();
                println!("splitters: {:?}", splitters);

                // Check my string list, get all indexes of the paths that are being split
                let mut indexes: Vec<usize> = paths.iter().enumerate().filter_map(|(j, value)| {
                    if splitters.contains(&(value.split("-").last().unwrap().parse::<usize>().unwrap())) {
                        Some(j)
                    } else {
                        None
                    }
                })
                .collect();

                // reverse the index list so when we manipulate the list we don't effect the lower
                // indexes
                indexes.reverse();
                println!("intexes: {:?}", indexes);

                // Take each string, put the new node in the end of the 
                for k in indexes {
                    let mut a = paths.remove(k);
                    let i = a.split("-").last().unwrap().parse::<usize>().unwrap();
                    paths.push(format!("{}-{}",a, i-1));
                    paths.push(format!("{}-{}",a, i+1));
                }
            }
            println!("is {} long",paths.len());
        }
    }
    println!("count: {}", paths.len());
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

