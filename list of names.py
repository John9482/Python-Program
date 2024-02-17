# Prompt the user to enter names
names_input = input("Enter a list of names separated by commas or spaces: ")

# Split the input into a list of names
names_list = names_input.split(',')

names_list = [name.strip() for name in names_list]

# Sort the list of names alphabetically
names_list.sort()

# Remove duplicates from the sorted list
unique_names_list = []
[unique_names_list.append(name) for name in names_list if name not in unique_names_list]

# Display the final sorted list without duplicates
print("Sorted list of unique names:", unique_names_list)

# Count and print the total number of names entered
print("Total number of names entered:", len(unique_names_list))
