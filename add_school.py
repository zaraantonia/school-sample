def add_school_group(schools, sch2, sch1):
    for i in range(0, len(schools)):
        if schools[i].name == sch1.name:
            schools[i].names += sch2.names

            shortest_name = schools[i].names[0]
            min = len(schools[i].names[0])
            for j in range(1, len(schools[i].names)):
                if len(schools[i].names[j]) < min:
                    shortest_name = schools[i].names[j]

            short_name = ""
            for j in range(0, len(shortest_name)):
                if shortest_name[j].isupper():
                    short_name += shortest_name[j]

            schools[i].short_name = short_name
            schools[i].name = shortest_name
            schools[i].count = len(schools[i].names)

            break

    return schools
