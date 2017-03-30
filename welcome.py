import json
import platform
import re
import dateutil.parser
import datetime
# This will hold the colors that are needed for the logo. The keys will be
# used as the regex and it will replace the regex with the value.

todo_list = [];     # This array will contain the formatted todo list 
num_of_colors = 17  # This is amount of colors the terminal support 
color_dictionary = [
    
    # Normal
    ["#Nbla#", '\033[0;30m'],       # Black
    ["#Nred#", '\033[0;31m'],      # Red
    ["#Ngre#", '\033[0;32m'],       # Green
    ["#Nyel#", '\033[0;33m'],       # Yellow
    ["#Nblu#", '\033[0;34m'],       # Blue
    ["#Nmag#", '\033[0;35m'],       # Purple
    ["#Ncya#", '\033[0;36m'],       # Cyan
    ["#Nwhi#", '\033[0;37m'],       # White

    # Bright
    ["#Bbla#", '\033[1;30m'],       # Black
    ["#Bred#", '\033[1;31m'],       # Red
    ["#Bgre#", '\033[1;32m'],       # Green
    ["#Byel#", '\033[1;33m'],       # Yellow
    ["#Bblu#", '\033[1;34m'],       # Blue
    ["#Bmag#", '\033[1;35m'],       # Purple
    ["#Bcya#", '\033[1;36m'],       # Cyan
    ["#Bwhi#", '\033[1;37m'],       # White

    # Reset
    ["#Cend#", '\x1b[m']            # Reset color

]

# This method will add the formatted todo list in a separate list
# this list wil eventually be merged with the icon to be to the right of it
def load_todo_list():
    with open('welcome_script/tasks.json') as data_file:
        todo_object = json.load(data_file)
    
    task_array = todo_object["tasks"]
    todo_list.append(color_dictionary[8][1] + "===========================================")
    
    for task in task_array:
        date = dateutil.parser.parse(task["date"])
        todo_list.append('{:<44s} {:10s}'.format(
            color_dictionary[13][1] + task["class"] + color_dictionary[16][1] + " - " + task["task"], 
            color_dictionary[1][1] + date.strftime("%m/%d/%y"))
        )
        todo_list.append(color_dictionary[8][1] + "===========================================")

# This is the functon that will render the ascii icons from the json
# object as well as using regular expressions to give the logo colors.

def load_icon(line_num, icon_array):
    
    load_todo_list()
    start_point = round((line_num / 2) - (len(todo_list) / 2)) + 1
    
    for index, line in enumerate(icon_array):
        for color_rex in color_dictionary:
            line = re.sub(color_rex[0], color_rex[1], line)
        
        if index >= start_point and index < (start_point + len(todo_list)):
            print(
                    '{:<42s} {:50s}'.format(line + color_dictionary[16][1],
                    todo_list[index - start_point] + color_dictionary[16][1]
                ))
        else:
            print(line)

# This function gets the os name that the program running on and 
# creates an json object from the icon json file with the ascii art.
# then calls a functon that will render the image along with the data.

def color_parse_icon():
    with open('welcome_script/os_icons.json') as data_file:
        icon_object = json.load(data_file)

    _platform = platform.system().lower()
    num_lines = icon_object["NumOfLines"]
   
    if _platform == "linux" or _platform == "linux2":
        # TODO: linux
        print("Linux Icon")
    elif _platform == "darwin":
        # MAC OS X
        load_icon(num_lines, icon_object["Mac"])
    elif _platform == "win32":
        # TODO: Windows
        print("Windows Icon")


color_parse_icon()
