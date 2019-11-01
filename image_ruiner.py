import shutil

def ruin_image(filename, gap=1, skip=300):
    split = filename.split('.')
    file_copy = split[0] + '_' + str(gap) + '_' + str(skip) + '_copy.' + split[1]
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
