use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
        const z: usize = 137;
        if let Ok(lines) = read_lines("./input") {
        let mut matrix: Vec<Vec<u8>> = Vec::new();
            for line in lines.map_while(Result::ok) {
                let mut st: String = line;
                st = st.replace("@", "1");
                st = st.replace(".", "0");
                let vec: Vec<u8> = st.chars().map(|c| c.to_digit(10).unwrap() as u8).collect();
                matrix.push(vec);
            }
            let mut count = 0;
            for i in 0..z {
                for j in 0..z {
                    let neighbors = count_neighbors(&matrix, i, j);
                    if neighbors < 4 && matrix[i][j] == 1 {
                        count += 1;
                    }
                }
            }
            println!("count: {}", count);
        }
}

fn count_neighbors(matrix: &Vec<Vec<u8>>, row: usize, col: usize) -> u8 {
    let h = matrix.len();
    let w = matrix[0].len();

    let directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ];

    let mut count = 0;

    for (dr, dc) in directions {
        let new_r = row as isize + dr;
        let new_c = col as isize + dc;

        // bounds check using dynamic sizes
        if new_r >= 0 && new_r < h as isize && new_c >= 0 && new_c < w as isize {
            if matrix[new_r as usize][new_c as usize] == 1 {
                count += 1;
            }
        }
    }

    count
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
