def get_input(path):
        
    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]
        
    return lines