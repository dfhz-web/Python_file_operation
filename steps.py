def decode(message_file):
    with open(message_file, 'r') as file:
        message = file.readlines()   #read lines makes a list
        # print(message)

    # Remove newline characters from the words
    message = [line.strip() for line in message]
    # print(message)

    # Sort the words by the numeric part
    message = sorted(message, key=lambda x: int(''.join(filter(str.isdigit, x))))

    # Convert the list elements to a string representation
    list_str = '\n'.join(map(str, message))
    
    with open(message_file, 'w') as file:
    # Write the string representation of the list to the file
      file.writelines(list_str)

    
    with open(message_file, 'r') as file:
       lines =  file.readlines()


    #combine lines
    combined_lines1 = '  '.join(line.strip() for line in lines[1:2])
    combined_lines2 = '  '.join(line.strip() for line in lines[3:5])

    #modify them
    lines[1:2] = [combined_lines1]
    lines[3:5] = [combined_lines2]

    #overwrite
    with open('newfile.txt', 'w') as file:
        file.writelines(lines)

    # now go to select the last data for each line
        
    with open('newfile.txt','r') as file:
       lines = file.readlines()

    #process each line
    string=''
    for line in lines:
       #split the line into words
       words = line.split()
       #  print(words)
      
       #Get the last word 
       last_word = words[-1]
       string = string + " " + last_word

       #print result

    print(string)
    



    #last part get the last element for each line
    # line1 = [] 
    # line2 = [] 
    # line3 = [] 
    # with open('newfile.txt', 'r') as file:
    #    content1 = file.readline()
    #    content2 = file.readline()
    #    content3 = file.readline()

    # line1.append(content1)
    # line2.append(content2)
    # line3.append(content3)
    
    # print(line1)
    # print(line2)
    # print(line3)

    # print('result=')
    # returning = f"{line1.pop()} + {line2.pop()} + {line3.pop()}"
    # print(returning)
    

    


  

decode('text.txt')