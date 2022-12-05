use std::collections::HashSet;
use std::fs;

const LETTERS: &str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

#[derive(Clone)]
struct Rucksack {
    left: String,
    right: String,
}

impl Rucksack {
    fn misfiled(self) -> char {
        for c in self.left.chars() {
            if self.right.contains(c) {
                return c
            }
        }
        return '!';
    }

    fn contents(self) -> String {
        return self.left + &self.right
    }
}

fn multi_hashset_intersection(sets: Vec<HashSet<char>>) -> HashSet<char> {
    let mut sets: Vec<HashSet<char>> = sets.iter().cloned().collect();
    let mut intersection: HashSet<char> = sets.pop().unwrap();
    for set in sets {
        intersection = intersection
            .intersection(&set)
            .copied()
            .collect()
    }
    return intersection
}

#[derive(Clone)]
struct ElfGroup {
    elves: Vec<Rucksack>
}

impl ElfGroup {
    fn badge(self) -> char {
        let common_contents = multi_hashset_intersection(
            self.elves
                .iter()
                .map(|bag| HashSet::from_iter(
                    bag.clone().contents().chars()
                )).collect()
        );
        return *common_contents.iter().next().unwrap();
    }
}

fn get_priority(letter: char) -> i32 {
    return LETTERS.find(letter).unwrap() as i32 + 1
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
    let mut phase_1_priority_sum: i32 = 0;
    let mut phase_2_priority_sum: i32 = 0;
    let mut group: ElfGroup = ElfGroup{
        elves: {Vec::new()}
    };
    for (_index, line) in read_and_split_file("./inputs/input.txt").iter().enumerate() {
        let half = line.len() / 2;
        let (left, right) = line.split_at(half);
        let ruck: Rucksack = Rucksack{
            left: left.to_string(),
            right: right.to_string(),
        };
        let misfiled = ruck.clone().misfiled();
        let phase_1_incr = get_priority(misfiled);
        group.elves.push(ruck.clone());
        if (_index + 1) % 3 == 0 {
            let group_id = (_index + 1) % 3;
            let badge = group.clone().badge();
            let phase_2_incr = get_priority(badge);
            phase_2_priority_sum += phase_2_incr;
            println!(
                "Group {} badge is {}; priority + {}",
                group_id,
                badge,
                phase_2_incr,
            );
            group.elves.clear();
        }
        phase_1_priority_sum += phase_1_incr;
        println!("Misfiled: {}; priority + {}", misfiled, phase_1_incr);
    }
    println!("Phase 1 Total: {}", phase_1_priority_sum);
    println!("Phase 2 Total: {}", phase_2_priority_sum);
}
