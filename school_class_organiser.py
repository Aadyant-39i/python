classmates = ["Aarav", "Harteij", "Shyam", "Riyansh", "Isaac", "Ved", "Yohan"]
print("Classmates:", classmates)

print("Number of classmates:", len(classmates))
classmates.append(input("Enter a new classmate's name: "))
print("Updated list of classmates:", classmates)
classmates.remove(input("Enter the name of the classmate to remove: "))
classmates.sort()
print("Sorted list of classmates:", classmates)
classmates.reverse()
print("Reversed list of classmates:", classmates)
teacher = {"name": "Mr. Smith", "subject": "ICT", "years_of_experience": 3}
teacher["email"] = "smith@gisschool.com"
print("Teacher's information:", teacher)

roll_numbers = [1,2,3,4,5,6,7]
classmates.sort()
student_directory = dict(zip(roll_numbers, classmates))
print("Student directory:", student_directory)
print("student with roll number 3:", student_directory[3])

if len(classmates) < 7:
    print("we need to add more classmates to the list.")
else:
    print("we have enough classmates in the list.")

query = input("Enter a classmate's name to check if they are in the list: ")

if query == "Aarav":
    print("Aarav is in the list.")
elif query == "Harteij":
    print("Harteij is in the list.")
elif query == "Shyam":
    print("Shyam is in the list.")
elif query == "Riyansh":
    print("Riyansh is in the list.")
elif query == "Isaac":
    print("Isaac is in the list.")
elif query == "Ved":
    print("Ved is in the list.")
elif query == "Yohan":
    print("Yohan is in the list.")
else:
    print("This classmate is not in the list.")