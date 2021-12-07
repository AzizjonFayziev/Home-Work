dict = {}

def toDict(*str):
    for i in range(len(str)):
        dict[i] = str[i]
    return dict
print(toDict('Hello', 'bro', '!!!'))