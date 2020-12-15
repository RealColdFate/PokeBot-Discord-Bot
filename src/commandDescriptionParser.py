command_file_name = "../data/commands.txt"

WRAP_LIMIT = 35  # how many chars to warp the help line after used for formatting


# returns a dictionary of all of the command names and their descriptions
def command_dict():
    temp_dict = {}
    with open(command_file_name, 'r') as file:
        for line in file:
            command = line.split('~')
            temp_dict[command[0]] = command[1]
        file.close()
    return temp_dict


# formats help description into a more readable form
def format_command_help_description(name, desc):
    ret_str = "- " + name + "\n\t"
    desc = desc.split(' ')
    char_count = 0
    for i in desc:
        char_count += len(i)
        if char_count >= WRAP_LIMIT:
            ret_str += "\n\t"
            char_count = 0
        if '\n' not in i:
            ret_str += i + " "
        else:
            ret_str += i + "\n"
    return ret_str


# returns a string of all of the available commands
def help_print_all_string(dictionary):
    o_string = "\n"
    for k, v in dictionary.items():
        o_string += format_command_help_description(k, v)
    print(o_string)
