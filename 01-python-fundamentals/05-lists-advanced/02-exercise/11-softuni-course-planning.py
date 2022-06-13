lessons = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    tokens = command.split(":")
    command = tokens[0]
    lesson = tokens[1]

    if command == "Add" and lesson not in lessons:
        lessons.append(lesson)
    
    elif command == "Insert" and lesson not in lessons:
        index = int(tokens[-1])
        lessons.insert(index, lesson)
    
    elif command == "Remove" and lesson in lessons:
        lessons.pop(lessons.index(lesson))
        if f"{lesson}-Exercise" in lessons:
            lessons.pop(lessons.index(lesson + 1))

    elif command == "Swap" and lesson in lessons:
        new_lesson = tokens[-1]
        lesson_index = lessons.index(lesson)

        if new_lesson in lessons:
            new_lesson_index = lessons.index(new_lesson)
            lessons[new_lesson_index] = lesson # swap places
            lessons[lesson_index] = new_lesson # swap places

        # if exercise exists then move it as well
        if (f"{new_lesson}-Exercise") in lessons:
            exercise_index = lessons.index(f"{new_lesson}-Exercise")
            lessons.insert(lesson_index + 1, lessons.pop(exercise_index))
    
    # if no such lesson create it and an add exercise as well
    elif command == "Exercise":
        if lesson not in lessons:
            lessons.append(lesson)
            lessons.append(f"{lesson}-Exercise")
            
        # if lesson exist but no exercise then add it on the next index
        elif lesson in lessons and (f"{lesson}-Exercise") not in lessons:
            lesson_index = lessons.index(lesson)
            lessons.insert(lesson_index + 1, f"{lesson}-Exercise")

for i, lesson in enumerate(lessons):
    print(f"{i+1}.{lesson}")