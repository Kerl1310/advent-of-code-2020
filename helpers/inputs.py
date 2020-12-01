def read_number_input_as_list(filename):
    '''
    '''
    with open(filename) as f:
        content = f.readlines()
        content = [int(x.strip()) for x in content]
        return content
        