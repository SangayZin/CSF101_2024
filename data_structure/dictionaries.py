name = "Sangay Tenzin"  
age = 21  
height = 1.75  
is_student = True 
favorite_color = "Blue" 

person_info = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student,
    "favorite_color": favorite_color
}
print(person_info)

try:
    print(person_info["weight"])
except KeyError as e:
    print(f"Error: {e}")