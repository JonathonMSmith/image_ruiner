import shutil

def copy_im_file(filename, *args):
    split = filename.split('.')
    id_str = '_'
    for arg in args:
        id_str = id_str + str(arg) + '_'
    file_copy = split[0] + id_str + 'copy.' + split[1]
    return file_copy

def delete_middle(filename, gap=1, skip=300):
    file_copy = copy_im_file(filename)
    with open(file_copy, 'wb') as new_file:
        with open(filename, 'rb') as old_file:
            for i, line in enumerate(old_file):
                if i == 0 or i % skip != 0:
                    new_file.write(line)
                else:
                    half = int(len(line)/2)
                    first_half = line[:half]
                    second_gap_half = line[half+gap:]
                    new_file.write(first_half+second_gap_half)

def delete_lines(filename, start=0, stop=None):
    file_copy = copy_im_file(filename)
    if stop == None:
        stop = len(open(filename, 'rb').readlines())
        print(stop)
    with open(file_copy, 'wb') as new_file:
        with open(filename, 'rb') as old_file:
            for i, line in enumerate(old_file):
                if i < start or i > stop:
                    new_file.write(line)
                else:
                    continue
