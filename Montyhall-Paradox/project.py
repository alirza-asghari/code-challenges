from random import randint


def switch(doors, my_choice, open_door):
    for new_choice in [1,2,3]:
        if new_choice != my_choice and new_choice != open_door:
            my_choice = new_choice
            break
    return doors[my_choice]


def stay(doors, my_choice):
    return doors[my_choice]


def montyhall_simulation(iterations):
    switch_wins = 0
    stay_wins = 0
    for _ in range(iterations):
        doors = {1 : 0, 2 : 0, 3 : 0} # 1 is car and 0 is goat
        car_index = randint(1, 3)
        doors[car_index] = 1
        my_choice = randint(1, 3)
        while(True):
            open_door = randint(1, 3)
            if open_door != car_index and open_door != my_choice:
                break
        # initiating problem is now complete
        switch_wins += switch(doors, my_choice, open_door)
        stay_wins += stay(doors, my_choice)

    return switch_wins, stay_wins

            
test_size = int(input('How many time should I run the problem? '))
with_swith, with_stay = montyhall_simulation(test_size)
print(f'Wins {with_swith} time\'s with swithing the door and {with_stay} time\'s without switching out of {test_size}')







        