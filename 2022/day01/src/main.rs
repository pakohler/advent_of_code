    //use std::env;
    use std::fs;

    struct Elf {
        snacks: Vec<i32>,
    }

    impl Elf {
        fn calories(&self) -> i32 {
            self.snacks.iter().sum::<i32>()
        }
    }


    fn build_elf() -> Elf {
        Elf {
            snacks: Vec::new()
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
        let mut elves: Vec<Elf> = vec![build_elf()];
        for line in read_and_split_file("./inputs/input1.txt") {
            if line.is_empty() {
                elves.push(build_elf());
            } else {
                let elf_count = elves.len();
                elves[elf_count-1]
                    .snacks
                    .push(line.parse::<i32>()
                    .unwrap());
            }
        }
        elves.sort_by_key(|e| e.calories());
        for elf in &elves {
            println!("{}", elf.calories())
        }
        let elf_count = elves.len();
        let mut top_3_sum: i32 = 0;
        for n in 1..4 {
            top_3_sum += elves[elf_count - n].calories();
        }
        println!("{}", top_3_sum);
    }
