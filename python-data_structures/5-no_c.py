def no_c(my_string):
    # Yeni boş string yaradırıq
    new_string = ''
    
    # Hər simvolu yoxlayırıq
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char  # c və C olmayan simvolları əlavə edirik
    
    return new_string
