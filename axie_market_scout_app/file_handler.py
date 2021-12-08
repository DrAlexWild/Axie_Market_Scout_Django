import codecs
import time
#file_ = open(os.path.join(PROJECT_ROOT, 'filename'))

def read_one_line(filename):
    file = codecs.open(filename, "r+", "utf-8")
    lines = file.readlines()
    file.close()
    return lines[0]

def write_to_file_append(str, filename):
    try:
        file = codecs.open(filename, "a", "utf-8")  # append mode
        if str != "":
            file.write(str + '\n')
        file.close()
    except:
        write_to_file_append(str, filename)

def write_to_file_replace(str, filename):
    try:
        file = codecs.open(filename, "w", "utf-8")
        file.write(str + '\n')
        file.close()
    except:
        write_to_file_replace(str, filename)
def clear_file(filename):
    file = codecs.open(filename, "w", "utf-8")
    file.truncate(0)





#remove_equal_lines(betano_file_name, 'betclic_test_1.txt')
