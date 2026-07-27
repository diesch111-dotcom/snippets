// Rust_for_loop_array2.rs
//
// An array is a collection of objects of the same type T
// use iter() so the loop does not consume the array

fn main() {
    
    let insects = ["ant", "bee", "wasp"];
    println!("Number of elements in array: {}", insects.len());

    for (index, insect) in insects.iter().enumerate() {
        println!("Index: {}, Insect: {}", index, insect);
    }
    // still exists
    println!("{:?}", insects);
    
}

/*
Number of elements in array: 3
Index: 0, Insect: ant
Index: 1, Insect: bee
Index: 2, Insect: wasp
["ant", "bee", "wasp"]
*/

