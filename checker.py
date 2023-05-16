# Prompt the user for the input and output filenames and the maximum number of characters
input_filename = input('Enter the input filename: ')
output_filename = input('Enter the output filename: ')
max_chars = int(input('Enter the maximum number of characters per line: '))

# Open the input file for reading
with open(input_filename, 'r') as input_file:

    # Open the output file for writing
    with open(output_filename, 'w') as output_file:

        # Loop through each line in the input file
        for line in input_file:

            # Strip any whitespace from the line
            line = line.strip()

            # Check if the line is less than the maximum number of characters
            if len(line) < max_chars:

                # If the line is less than the maximum number of characters,
                # write it to the output file
                output_file.write(line + '\n')

# Print a message indicating that the program has finished
print('Done!')
