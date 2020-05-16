def party_timing(schedule):
    enter = []
    leave = []
    max_number = 0
    max_time = None
    for i in schedule:
        person_in, person_out = i
        enter.append(person_in)
        leave.append(person_out)
    
    for i in set(enter):
        people_in = [j for j in enter if j < i + 1]
        people_out = [j for j in leave if j < i + 1]
        tmp = len(people_in) - len(people_out)
        if max_number < tmp:
            max_number = tmp
            max_time = i
    
    return max_time, max_number

def party_timing_with_time_constraint(schedule, ystart, yend):
    enter = []
    leave = []
    max_number = 0
    max_time = None
    for i in schedule:
        person_in, person_out = i
        enter.append(person_in)
        leave.append(person_out)
    
    
    people_in = [j for j in enter if j < ystart + 1]
    people_out = [j for j in leave if j < yend + 1]
    tmp = len(people_in) - len(people_out)
    max_number = tmp
    max_time = i
    
    return max_time, max_number

    def party_timing_with_weight(schedule):
        enter = []
        leave = []
        weight = []
        max_number = 0
        max_time = None
        for i in schedule:
            person_in, person_out, w = i
            enter.append(person_in)
            leave.append(person_out)
            weight.append(w)
        
        for i in set(enter):
            people_in = [1*w for j, w in zip(enter, weight) if j < i + 1]
            people_out = [1*w for j, w in zip(leave, weight) if j < i + 1]
            tmp = sum(people_in) - sum(people_out)
            if max_number < tmp:
                max_number = tmp
                max_time = i

        return max_time, max_number

if __name__ = "__main__":
    sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9),
         (8, 10), (9, 12), (9, 10), (10, 11), (10, 12), (11, 12)]
    party_timing(sched)