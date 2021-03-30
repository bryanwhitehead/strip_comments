def solution(string,markers):
    print(string)
    output = ""
    i = 0
    length = len(string)
    while i < length:
        if string[i] == ' ' and string[i+1] == '\n':
            output += '\n'
            i += 1
        elif string[i] == ' ' and string[i+1] in markers:
            i += 1
        elif string[i] in markers:
            while i < length:
                if string[i] == '\n':
                    break
                i += 1
        else:
            output += string[i]
            i += 1        
    return output
            