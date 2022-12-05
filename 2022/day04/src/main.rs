use std::fs;
use itertools::Itertools;

#[derive(Clone, Copy)]
struct Assignment {
    min: i32,
    max: i32,
}


impl Assignment {
    fn contains(self, other: Assignment) -> bool {
        return other.min >= self.min && other.max <= self.max
    }
    fn overlaps(self, other: Assignment) -> bool {
        return (self.min >= other.min && self.min <= other.max) 
            || (self.max >= other.min && self.min <= other.min)
    }
    fn to_string(self) -> String {
        format!("{}-{}", self.min, self.max)
    }
}


fn read_and_split_file(file_path: &str) -> Vec<String> {
    let contents = fs::read_to_string(file_path)
        .expect("unable to read file");
    let vec: Vec<String> = contents
        .split("\n")
        .map(|ln| ln.to_string())
        .collect();
    return vec
}


fn main() {
    let mut phase_1_total: i32 = 0;
    let mut phase_2_total: i32 = 0;
    for (_index, line) in read_and_split_file("./inputs/input.txt").iter().enumerate() {
        let ranges = line.as_str().split(",");
        let mut assignments: Vec<Assignment> = Vec::new();
        for range in ranges {
            let (start, end) = range
                .split("-")
                .map(|i| i.parse::<i32>().unwrap())
                .collect::<Vec<i32>>()
                .iter()
                .map(|v| *v)
                .collect_tuple()
                .unwrap();
            let ass: Assignment = Assignment{min:start, max:end};
            assignments.push(ass);
            println!("{}", ass.to_string())
        }
        if assignments[0].overlaps(assignments[1]) || assignments[1].overlaps(assignments[0]) {
            println!("Partial overlap detected");
            phase_2_total += 1;
        }

        if assignments[0].contains(assignments[1]) || assignments[1].contains(assignments[0]) {
            println!("Complete overlap detected");
            phase_1_total += 1;
        }
        println!("");
    }
    println!("Phase 1: {}", phase_1_total);
    println!("Phase 2: {}", phase_2_total);
}
