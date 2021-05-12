def render_person(name, birthday, eyecolor, age, gender):
    return f"{name} is a {age} years old {gender} born in {birthday} with {eyecolor} eyes"


print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))