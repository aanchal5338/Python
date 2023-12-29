#Dictionary
persons = [
    {"name": "Alice", "age": 28, "city": "New York"},
    {"name": "Bob", "age": 22, "city": "San Francisco"},
    {"name": "Charlie", "age": 30, "city": "Los Angeles"},
    {"name": "David", "age": 24, "city": "Chicago"},
    {"name": "henry", "age": 26, "city": "america"}
]

# Filter
filtered_persons = []
for person in persons:
    if person["age"] >= 25:
        filtered_persons.append(person)

#Sorting
for i in range(len(filtered_persons)):
    for j in range(i + 1, len(filtered_persons)):
        if filtered_persons[i]["city"] > filtered_persons[j]["city"]:
            # Swap the positions if out of order
            filtered_persons[i], filtered_persons[j] = filtered_persons[j], filtered_persons[i]


print("Final List of Persons:")
for person in filtered_persons:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")
