use std::fs;

fn main() {
    let path = "/Users/xxxxx/Documents";
    for file in fs::read_dir(path).unwrap() {
        println!("{}", file.unwrap().path().display());
    }
}