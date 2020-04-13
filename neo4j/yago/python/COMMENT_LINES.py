import sys
import in_place

# input arguments to program
# 1. path to the file generated by BOM.py : e.g. c:\yago\manipulation\neo4j\replace_lines.txt
# 2. path to ttl file changed inline : e.g. c:\yago\manipulation\neo4j\yagoConteXtFacts_en.ttl

if len(sys.argv) != 3:
    print("program takes three wo arguments: name of file with line numbers to give a comment;name of file that we want to change")
    '''example of file with line numbers where range is written with comma:
       10,15
       4
       7
       ...
    '''
    sys.exit()
line_numbers = []
with open(sys.argv[1]) as file:
    for cnt, line in enumerate(file):
        split = line.split(',')
        if len(split) > 1:
            for i in range(int(split[0].strip()), int(split[1].strip()) + 1):
                line_numbers.append(i)
        else:
            line_numbers.append(int(split[0].strip()))

cnt = 0
with in_place.InPlace(sys.argv[2],encoding="utf-8") as file:
    for line in file:
            cnt = cnt + 1
            if cnt in line_numbers:
                new_line = "#yuda " + line
                file.write(new_line)
            else:
                file.write(line)