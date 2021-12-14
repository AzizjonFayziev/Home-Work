def convertTemp(degree, value1, value2):
    if value1 == 'C': return (degree * (9 / 5)) + 32
    else: return (degree - 32) * (5 / 9)
print(convertTemp(30, 'C', 'F'))
print(convertTemp(86, 'F', 'C'))