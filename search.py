string, lookup = input(), input()

class Borders:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

def search(string : str, lookup : str) -> str:
    all_of_borders = []
    j = 0 

    for i in range(len(string)):
        if string[i] == lookup[j]:
            if j == 0: 
                borders = Borders(i, -1)
            if j == (len(lookup) - 1): 
                borders.end = i + 1
                all_of_borders.append(borders)
                j = 0 
            else: j += 1 
        else: j = 0

    for borders in all_of_borders:
        string = string[0 : borders.start] + "_" +string[borders.start : borders.end] + "_" + string[borders.end: len(string)]
        for border in all_of_borders:
            border.start += 2
            border.end += 2

    return string

print(search(string, lookup))