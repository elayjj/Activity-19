employees = [
    {"name": "John Doe", "department": "Sales", "id": 1, "age": 30, "email": "john.doe@company.com"},
    {"name": "Jane Smith", "department": "Human Resources", "id": 2, "age": 25, "email": "jane.smith@company.com"},
    {"name": "Mark Johnson", "department": "IT", "id": 3, "age": 40, "email": "mark.johnson@company.com"},
    {"name": "Lisa Wong", "department": "Marketing", "id": 4, "age": 28, "email": "lisa.wong@company.com"},
    {"name": "Paul Mcdonald", "department": "Finance", "id": 5, "age": 35, "email": "paul.mcdonald@company.com"}
]
for employee in employees:
    print(f"Name: {employee['name']}, Department: {employee['department']}, Email: {employee['email']}, Age: {employee['age']}")