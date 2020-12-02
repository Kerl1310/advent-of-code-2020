def read_number_input_as_list(filename):
    '''
    '''
    content = read_file(filename)
    content = [int(x.strip()) for x in content]
    return content

def read_file(filename):
    '''
    '''
    with open(filename) as f:
        content = f.readlines()
        return content