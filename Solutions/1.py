def main():
    with open(r"C:\Users\User\Documents\Coding\Advent\Inputs\1.txt","r") as f:
        data = f.read()
    data_list = data.split("\n")

    response = []
    for i in data_list:
        c = convert_to_num(i)
        response.append(first_last(c))
    sum = 0
    for i in response:
        sum += int(i)
    print(sum)


def first_last(text):
    first = ""
    last = ""
    for j in range(len(text)):
        if text[j].isnumeric():
            first = text[j]
            break
    rev = reversed(text)
    for j in rev:
        if j.isnumeric():
            last = j
            break
    if first and last:
        return str(first) + str(last)
    else:
        return ""
    
def convert_to_num(text):
    digits = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight",9:"nine"}
    response = ""
    for i in range(len(text)):
        if text[i].isnumeric():
            response+=str(text[i])
        for key, value in digits.items():
            if value in text[i:i+len(value)]:
                response+=str(key)
    print(text+": "+response)
    return response

main()
