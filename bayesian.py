import random

def morty(trails):
    s_wins=0
    c_wins=0
    for _ in range(trails):
        doors=['a','b','c']
        bike_location=random.choice(doors)
        i_choise=random.choice(doors)
        doors.remove(i_choise)
        if bike_location in doors:
            doors.remove(bike_location)
        m_choice=random.choice(doors)
        doors=[d for d in ['a','b','c'] if d!=m_choice and d!=i_choise]
        f_choice=doors[0]

        s_wins+=(i_choise==bike_location)
        c_wins+=(f_choice==bike_location)
    
    s_prob=s_wins/trails
    c_prob=c_wins/trails

    print(f"Probability of winning by staying: {s_prob:.2f}")
    print(f"Probability of winning by switching: {c_prob:.2f}")

trails=10
morty(trails)