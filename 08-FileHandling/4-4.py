def display_file_in_chunks(file_name):
    file_path = 'it_company.csv'
    try:
        with open(file_name, 'r') as file:
            while True:
           
                lines = []
                for _ in range(1,6):
                    line = file.readline()
                    if not line: 
                        break
                    lines.append(line.strip())

                if not lines: 
                    print("End of file reached.")
                    break
                for line in lines:
                    print(line)

            
                input("Press Enter key to continue...")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

display_file_in_chunks(file_name)