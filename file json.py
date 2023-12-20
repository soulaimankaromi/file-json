import json

data = {
    "name": "John",
    "age": 25,
    "city": "Paris"
}

# Writing to the file "data.json"
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading from the file "data.json" and displaying its content
with open("data.json", "r") as file:
    data = json.load(file)
    print("File content before modification:")
    print(data)

# Adding a new key-value pair
data["language"] = "Python"

# Writing the modified dictionary back to the file
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading from the file "data.json" after modification and displaying its content
with open("data.json", "r") as file:
    modified_data = json.load(file)
    print("\nFile content after modification:")
    print(modified_data)
