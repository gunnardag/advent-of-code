use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::cmp::min;
use std::cmp::max;

fn main() {
    let mut db2: Vec<(i64, i64)> = Vec::new();
    let mut count: i64 = 0;
    if let Ok(lines) = read_lines("./input") {
        // Parse and fill out "database"
        for line in lines.map_while(Result::ok) {
            if line == "" {
                break;
            }
            let values: Vec<&str> = line.split("-").collect();
            let a: i64 = values[0].parse::<i64>().unwrap();
            let b: i64 = values[1].parse::<i64>().unwrap();
            db2.push((a,b));
        }
    }
    let mut clean_db: Vec<(i64, i64)> = Vec::new();
    let mut area: (i64, i64)  = (0, 0);
    // Sanitize our old datbase into a new one. Only allow areas that don't intersect with any
    // other areas.
    // If they interesect, merge with the first intersecting area and start again.
    while db2.len() > 0 {
        if area == (0, 0) {
            area = db2.remove(0);
        }
        let index: usize = comb_vec(area, db2.clone());
        if index != usize::MAX {
            let intersect = db2.remove(index);
            area = (min(area.0, intersect.0), max(area.1, intersect.1));
        } else {
            clean_db.push(area);
            area = (0, 0);
        }
        if db2.len() == 0 && area != (0, 0){
            clean_db.push(area);
        }
    }
    // calculate all area coverage
    for item in clean_db {
        count += 1+item.1-item.0;
    }
    println!("count: {}", count);
}

fn comb_vec(val: (i64, i64), mut vec: Vec<(i64, i64)>) -> usize {
    for (i, v) in vec.iter_mut().enumerate() {
        if val.0 <= v.1 && v.0 <= val.1  {
            return i;
        }
    }
    return usize::MAX;
}


fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
