def swapData():
    file_1:input('what is the name of the first file?:  ')
    file_2:input('what is the name of the second file?:  ')
    
    with open(file_1, 'r') as a:
        data_a = a.read()
    with open(file_1, 'w') as a:
        a.write(data_b)
    with open(file_2, 'r') as a:
        data_b = a.read()
    with open(file_2, 'w') as a:
        a.write(data_a)