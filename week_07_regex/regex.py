# Eric Liu

import re


def find_name(line):

    # Decided to separate out seaches

    # If there is a title in the name
    title_pattern = r"(Mr|Mrs|Ms|Mx|Dr)."
    result = re.findall(title_pattern,line)

    # If there is no title and has First + Last Name
    first_last_pattern = r""

    # If there is no title + Last name
    last_pattern = r""


    # pattern = r"(October|Oct|November|Nov)( \d{1,2}, \d{4})"
    # result = result + re.findall(pattern,line)
    return result


#result = find_date("10/15/2023 is a October 13, 2025 date as is 1/23/19")
#print(result)


f = open("datafile.dat")
for line in f.readlines():
    print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)
