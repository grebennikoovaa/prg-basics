###
# Makes a copy of a text file
#

# File names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# Read the content of the original file
with open(original_file, 'r') as source:
    content = source.read()  # Read the entire content of the source file

# Write the content to the target file (copy)
with open(target_file, 'w') as target:
    target.write(content)  # Write the content to the target file

print(f"Contents of '{original_file}' have been copied to '{target_file}'.")