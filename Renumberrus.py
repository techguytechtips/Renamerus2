import os

folder = input("Enter folder name: ")
delimiter = input("Enter delimiter: ")

def getNumbers(filename):
    numbers = ""
    # get every character after the delimiter
    try:
        ending = filename.split(delimiter,1)[1]
    except IndexError:
       return numbers

    # for every character in the rest of the file name
    for char in ending:
        # check if it is a number
        # if it is add it to the numbers var
        # otherwise just break out of the for loop entirely 
        if char.isnumeric():
            numbers += char
        else:
            break
    return numbers


# for every file name
for filename in os.listdir(folder):
    
    numbers = getNumbers(filename)
    if (numbers == ""):
        print("Failed to rename: " + filename + "\nbecause delimter condition does not exist")
        print("or because there is no numbers after delimiter.")
        continue

    print("Renamed: " + filename)
    # create the final name for the file
    # which will be the filename with the number
    # of the file at the beginning in brackets
    finalname = '(' + numbers + ') ' + filename
    os.rename(folder + '/' + filename, folder + '/' + finalname)

print("Press any key to continue.")
input()
