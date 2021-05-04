import csv


def create_it (part1, part2):
    with open('/home/giannos-g/Desktop/combine_and_merge_csv_files/example_combined.csv', 'a+', newline='')as f:
        thewriter = csv.writer (f)
        thewriter.writerow([part1[0], part1[1], part1[2], part2[1]])



def compare_them (file1, file2):
    csv_reader1 = csv.reader(file1, delimiter=',' )
    csv_reader2 = csv.reader(file2, delimiter=',' )
    line_count = 0
    for row1 in csv_reader1:
        for row2 in csv_reader2:
            if line_count == 0:
                with open('/home/giannos-g/Desktop/combine_and_merge_csv_files/example_combined.csv', 'w', newline='')as f:
                    thewriter=csv.writer(f)
                    thewriter.writerow(['PyScript', 'Memory', 'Time', 'Energy'])
                    line_count += 1
            else:
                if row1[0] == row2[0]: 
                    create_it (row1, row2)
                    line_count += 1

        file2 = open(r"/home/giannos-g/Desktop/combine_and_merge_csv_files/example_2.csv", "r")
        csv_reader2 = csv.reader(file2, delimiter=',' )

def main():
    file1 = open(r"/home/giannos-g/Desktop/combine_and_merge_csv_files/example_1.csv", "r")
    file2 = open(r"/home/giannos-g/Desktop/combine_and_merge_csv_files/example_2.csv", "r") 
    
    compare_them (file1, file2)

if __name__ == '__main__':
    main()