import csv


def get_input(file_path):
    process_details = {}
    with open(file_path, newline='') as csvfile:
        inp = csv.reader(csvfile, delimiter=' ')
        count = 0
        for row in inp:
            if count > 0:
                row_int_list = list(map(int, row[0].split(',')))
                process_details['p' + str(row_int_list[0])] = {}
                for i in info:
                    process_details['p' + str(row_int_list[0])][i] = row_int_list[info.index(i)]
            else:
                info = row[0].split(',')[1::]
            count += 1
        return process_details
