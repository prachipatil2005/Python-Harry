def generateTable(n):
    table = ""  # Initialize as an empty string
    for i in range(1, 11):  # Generate the multiplication table
        table += f"{n} x {i} = {n * i}\n"
    
    # Fix the file path syntax
    file_path = f"D:/c drive/cs/Sem6/Python-harry/file_handling/tables/table_{n}.txt"
    with open(file_path, "w") as f:
        f.write(table)  # Write the table to the file

# Generate multiplication tables for numbers 2 through 20
for i in range(2, 21):
    generateTable(i)
