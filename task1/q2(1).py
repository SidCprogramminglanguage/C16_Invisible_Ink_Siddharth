#brute force attempt i suppose means check whether the binary representation of the number == a number's binary representation
bin_input = input("Enter a number: ")
for i in range(1000): 
    if bin(i)[2:] == bin_input:
        print(f"The number is: {i}")
