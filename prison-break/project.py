def cell_flipping(cells):
    for i in range(len(cells)):
        if cells[i] in [0, 1]:
            cells[i] = cells[i] ^ 1
            # flipping bits with xor operation
        
def all_locked(cells):
    for i in range(1, len(cells)):
        if cells[i] == 1: return False
    return True
        
def prison_break(cells):
    if cells[0] == 0:
        print('We are locked')
        return
    
    free_counter = 0
    while not all_locked(cells):
        for i in range(1, len(cells)):
            if cells[i] == 1:
                free_counter += 1
                cells[i] = -1 # that means this cell is free now
                cell_flipping(cells)     
    print(f'We have released {free_counter} prisoners')

cells = [1, 1, 0, 0, 0, 1, 0]
prison_break(cells) # output 4
                

    
