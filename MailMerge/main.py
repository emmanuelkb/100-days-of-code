# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


with open("./Input/Names/invited_names.txt") as names_file, open("./Input/Letters/starting_letter.txt") as letter:
    guest_names = names_file.readlines()
    guest_names = [name.rstrip('\n') for name in guest_names]
    letter = letter.read()

for name in guest_names:
    new = letter.replace('[name]', name)
    with open(f"./Output/ReadyToSend/letter_for_{name}",'w') as output_file:
        output_file.write(new)
