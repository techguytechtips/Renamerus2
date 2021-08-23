import os

folder = input("Enter folder name: ")
delimiter = input("Enter Delimiter: ")

for filename in os.listdir(folder):
    try: 
        ending = filename.split(delimiter,1)[1]
    except IndexError as e:
        print("Failed to rename: ", end = filename)
        print(" Because the delimiter condition does not exist.")
        continue
    numbers = ""
    finalname = ""
    for char in ending:
        if char.isnumeric():
            numbers += char
        else:
            break
        
    print("Renamed: ", end = filename)
    print("")
    finalname = '(' + numbers + ') ' + filename
    os.rename(folder + '/' + filename, folder + '/' + finalname)

printf("Press any key to continue.")
input()
