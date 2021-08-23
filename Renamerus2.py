import os

folder = input("Enter folder name: ")
delimiter = input("Enter delimiter: ")

# for every file name
for filename in os.listdir(folder):
    
    # get every character after the delimiter
    try:
        ending = filename.split(delimiter,1)[1]
    except IndexError as e:
        print("Failed to rename: " + filename + "\nBecause delimter condition does not exist.")
        continue
    numbers = ""
    finalname = ""
    
    # for every character in the rest of the file name
    for char in ending:
        # check if it is a number
        # if it is add it to the numbers var
        # otherwise just break out of the for loop entirely
        if char.isnumeric():
            numbers += char
        else:
            break
    
    print("Renamed: " + filename)

    # create the final name for the file
    # which will be the filename with the number
    # of the file at the beginning in brackets
    finalname = '(' + numbers + ') ' + filename
    os.rename(folder + '/' + filename, folder + '/' + finalname)

print("Press any key to continue.")
input()
