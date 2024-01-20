with open('text.txt') as file:
    with open('new_text.txt','w') as new_file:
        for elements in file:
            new_file.write(elements)
