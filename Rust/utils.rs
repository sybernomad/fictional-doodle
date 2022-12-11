fn str-to-int() {
    // Define a string to convert
    let string = "42";

    // Convert the string to an integer
    let number = match string.parse::<i32>() {
        Ok(n) => n,
        Err(e) => panic!("Error: {}", e),
    };

    // Print the resulting number
    println!("The number is: {}", number);
}
