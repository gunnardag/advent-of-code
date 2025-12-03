use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut count = 0;
    if let Ok(lines) = read_lines("./input") {
        for line in lines.map_while(Result::ok) {
            count += process_number(line);
        }
        println!("{}", count);
    }
}

fn process_number(d: String) -> i64 {
    let mut jolt: String = "".to_string();
    let mut index = 0;
    for _ in 0..12 {
        let position = getmax(d[index..=d.len()-(12-jolt.len())].to_string());
        index += position;
        jolt = format!("{}{}", jolt, d.chars().nth(index).unwrap().to_string());
        index += 1;
    }
    return jolt.parse().expect("EKKI NUMER");
}


fn getmax(d: String) -> usize {
    let max_digit = d
        .chars()
        .max()
        .expect("string is nonempty and numeric");

    // All potitions of the max value character in the range
    let indices: Vec<usize> = d
        .char_indices()
        .filter_map(|(i, c)| if c == max_digit { Some(i) } else { None })
        .collect();

    // Return the first one
    let response = *indices.first().unwrap();
    return response;
}


fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
