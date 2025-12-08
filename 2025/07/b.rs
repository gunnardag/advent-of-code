use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashMap;

fn main() {
    let mut paths: HashMap<usize, usize> = HashMap::new();
    let mut count: usize = 0;
    if let Ok(lines) = read_lines("./input") {
        for line in lines.map_while(Result::ok) {
            if line.contains("S") {
                paths.insert(line.find("S").unwrap(), 1);
            } else {

                // find indexes of all the splitters
                let splitters: Vec<usize> = line.char_indices().filter_map(|(i, ch)| {
                    if ch == '^' {
                        Some(i)
                    } else {
                        None 
                    }
                }).collect();

                let mut keys: Vec<usize> = Vec::new();
                let mut tmp: HashMap<usize, usize> = HashMap::new();

                // fill the tmp map with the split options
                for (key, _value) in &paths {
                    if splitters.contains(&key) {
                        let s: usize = *paths.get(key).unwrap();
                        *tmp.entry(key+1).or_insert(0) += s;
                        *tmp.entry(key-1).or_insert(0) += s;
                        keys.push(*key);
                    }
                }
                
                // remove keys from path because they were split there
                for k in keys {
                    paths.remove(&k);
                }

                // add the split options back to the paths
                for (key, value) in &tmp {
                    *paths.entry(*key).or_insert(0) += value;
                } 
            }
        }
    }
    for (_key, value) in &paths {
        count += value;
    }
    println!("{}", count);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

