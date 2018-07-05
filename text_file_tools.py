
#txt file print to screen - this code imports text from a text file and prints
input_file = open('enter_text_file_here.txt','r')

line = input_file.readline()
empty_str = ""

while line != empty_str:
    print(line)
    line = input_file.readline()

input_file.close()

#------------------------------------------------------

#txt file copier - this code makes a copy of a text file in a folder
input_file = open('enter_text_file_here.txt','r')
output_file = open('enter_text_file_copy_here.txt','w')

line = input_file.readline()
empty_str = ""

while line != empty_str:
    output_file.write(line)
    line = input_file.readline()

output_file.close()











