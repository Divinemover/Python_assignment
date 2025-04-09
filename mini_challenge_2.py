for i in range(5):
    name_score = input('Enter student name and score (e.g., Faith 85): ')
    i = 0
    for i in len(name_score):
        if name_score.isspace() == False:
            i += 1
        else:
            break
