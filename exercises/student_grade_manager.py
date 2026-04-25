# Student grade manager

# Creá una lista de diccionarios llamada students con 3 estudiantes. Cada estudiante tiene:

# name — nombre
# age — edad
# grades — una lista con 3 notas numéricas


# Creá una función llamada get_average que reciba una lista de notas y retorne el promedio

# Recorré la lista de estudiantes con un loop y para cada estudiante:
# Calculá el promedio usando tu función
# Si el promedio es mayor o igual a 6 imprimí {name} passed with an average of {average}
# Si no imprimí {name} failed with an average of {average}

#Creá una lista de diccionarios llamada students con 3 estudiantes. Cada estudiante tiene:
students = [
    {"name": "Ignacio", "age": 34, "grades": [8, 9, 10]},
    {"name": "Maria", "age": 31, "grades": [10, 11, 12]},
    {"name": "Billy", "age": 20, "grades": [7, 11, 10]},
    {"name": "Mandy", "age": 26, "grades": [4, 5, 8]}
]

# Creá una función llamada get_average que reciba una lista de notas y retorne el promedio
def get_average(grades):
    return sum(grades) / len(grades)

passing_score = 7

# Recorré la lista de estudiantes con un loop y para cada estudiante:
for student in students:
    average = get_average(student["grades"])
    if average >= passing_score:
        print(f"{student["name"]} passed with an average of {average}")
    else: print(f"{student["name"]} failed with an average of {average}")