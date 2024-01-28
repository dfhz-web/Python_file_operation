import os

# r = Read
# a = Append
# w = Write   #open the file as writing
# x = Create


#Read -  error if it doesn't exist 

f = open('names.txt', "r")
# print(f.read())
# to read caracther as I want 
# print(f.read(4))


# read the first line of the line
# print(f.readline())
# print(f.readline())

#loop through each line of the line and print those lines
for line in f:
    print(line)

#it is import to close those files, it could that you change something on the file, and that change is not goona to show up  unti you close the file, and then you want to reopen it , and you can see that change
f.close()

print('**********names.txt***********************')

try:
    f = open("names.txt")
    print(f.read())
except:
    print("File no found")
finally:
    f.close
print('**********Endingnames.txt******************')



# Append - creates the file if it doesn't exist
f = open("names.txt", "a")
f.write("Daniel\n")
f.close()


f = open("names.txt", "r")
print(f.read())
f.close()

print('*********************************')

# Write(overwrite) 

f = open("context.txt", "w")
f.write("I deleted all of the context.txt")
f.close()

f = open("context.txt", "r")
print(f.read())
f.close()


print('*********************************')

# Two wats to create a new file

#Opens a file for writing , creates the file if it does not exists

f = open("list.txt", "w")
f.close()


#Creates the specified file, but returns an error if the file exists 

if not os.path.exists("dave.txt"):
    f = open("dave.txt","x")
    f.close()


# Delete a file 
    
# Avoid an error if it doesn't exist
if os.path.exists("context1.txt"):
    os.remove("context.txt")
else:
    print("The file you  wish does not exist")


print('*********************************')

with open("more_names.txt", "r") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)