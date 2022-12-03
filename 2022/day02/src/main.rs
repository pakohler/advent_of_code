use std::fs;

#[derive(PartialEq, Copy, Clone)]
enum HandSelection {
    ROCK,
    PAPER,
    SCISSORS
}

#[derive(PartialEq, Copy, Clone)]
enum GameResult {
    WIN,
    LOSE,
    DRAW,
}

#[derive(PartialEq, Copy, Clone)]
struct Hand {
    selection: HandSelection,
}

impl Hand {
    fn new(letter: &String) -> Hand {
        let _rocks: String = "AX".to_string();
        let _papers: String = "BY".to_string();
        let _scissors: String = "CZ".to_string();
        let mut hand: Hand = Hand{selection: HandSelection::SCISSORS};
        if _rocks.contains(letter.as_str()) {
            hand.selection = HandSelection::ROCK
        } else if _papers.contains(letter.as_str()) {
            hand.selection = HandSelection::PAPER
        } else {
            // scissors
        }
        return hand;
    }
    fn score(self) -> i32 {
        if self.selection == HandSelection::ROCK {
            return i32::from(1)
        } else if self.selection == HandSelection::PAPER {
            return i32::from(2)
        } else { // SCISSORS
            return i32::from(3)
        }
    }
    fn beats(self) -> HandSelection {
        if self.selection == HandSelection::ROCK {
            return HandSelection::SCISSORS
        } else if self.selection == HandSelection::PAPER {
            return HandSelection::ROCK
        } else { // SCISSORS
            return HandSelection::PAPER
        }
    }
    fn loses_to(self) -> HandSelection {
        return Hand{selection: self.beats()}.beats()
    }
    fn to_string(self) -> String{
        if self.selection == HandSelection::ROCK {
            return "rock".to_string()
        } else if self.selection == HandSelection::PAPER {
            return "paper".to_string()
        } else {
            return "scissors".to_string()
        }
    }
}

#[derive(PartialEq, Copy, Clone)]
struct Command {
    result: GameResult
}

impl Command {
    fn new(code: &String) -> Command {
        let mut cmd: Command = Command{result: GameResult::WIN};
        if code == &"X".to_string() {
            cmd.result = GameResult::LOSE
        } else if code == &"Y".to_string() {
            cmd.result = GameResult::DRAW
        } else { // Z
            return cmd
        }
        return cmd
    }
    fn score(self) -> i32 {
        if self.result == GameResult::LOSE {
            return i32::from(0)
        } else if self.result == GameResult::DRAW {
            return i32::from(3)
        } else { // WIN
            return i32::from(6)
        }
    }
    fn to_string(self) -> String {
        if self.result == GameResult::WIN {
            return "win".to_string()
        } else if self.result == GameResult::LOSE {
            return "lose".to_string()
        } else {
            return "draw".to_string()
        }
    }
}

struct Game {
    opponent: Hand,
    command: Command,
}

impl Game {
    fn score(&self) -> i32 {
        let mut score = self.command.score();
        let loss_choice = self.opponent.beats();
        let win_choice = self.opponent.loses_to();
        let draw_choice = self.opponent.selection;
        let mut choice: Hand = Hand{selection: draw_choice};
        if self.command.result == GameResult::DRAW {
            //
        } else if self.command.result == GameResult::WIN {
            choice = Hand{selection: win_choice}
        } else {
            choice = Hand{selection: loss_choice}
        }
        println!(
            "{}: {} {}", 
            self.command.to_string(),
            self.opponent.to_string(),
            choice.to_string(),
        );
        score += choice.score();
        return score
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
    let mut total_score: i32 = 0;
    let mut round = 0;
    for line in read_and_split_file("./inputs/input.txt") {
        round += 1;
        let split: Vec<String> = line.split(" ").map(|hand| hand.to_string()).collect();
        let game: Game = Game{
            opponent: Hand::new(&split[0]),
            command: Command::new(&split[1]),
        };
        let score: i32 = game.score();
        println!("Round {}: {}", round, score);
        total_score += score;
    }
    println!("Total: {}", total_score);
}
