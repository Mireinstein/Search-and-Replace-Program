reading_file = open("review.txt", "r")

new_file_content = ""
for line in reading_file:

    '''creating individuall lines'''
    stripped_line = line.strip()

    '''replacing'''
    new_line = stripped_line.replace(" w)", "()")
    new_line = new_line.replace("NORMAL()", '"NORMAL"')
    new_line = new_line.replace("STOP()", '"STOP"')
    new_line = new_line.replace("NAVIGATING()", '"NAVIGATING"')
    new_line = new_line.replace(" INTERSECTION()", ' "INTERSECTION"')
    '''concatenating the lines'''
    new_file_content += new_line +"\n"

'''closing the file'''    
reading_file.close()

'''copying contents from reading_file content'''
writing_file = open("review.txt", "w")
writing_file.write(new_file_content)
writing_file.close()