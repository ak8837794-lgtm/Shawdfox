# 1. Variables task

# a. create a variable named pi and store the value 22/7 in it. now check the data type of this variable .
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))

# b. Create a variable called for and assign it a value 4. See whathappens and find out the reason behind the behavior that you see.
# for = 4 SyntaxError: invalid syntax
for i in range(5):
    print(i)
for_value = 4
import keyword
print(keyword.kwlist)

#c. Store the principal amount, rate of interest, and time indifferent variables and then calculate the Simple Interest for 3 years. Formula: Simple Interest = P x R x T / 100

# Storing the values
principal = 10000  # Principal amount in currency units
rate = 5           # Rate of interest in percent per annum
time = 3           # Time in years

# Calculating Simple Interest
simple_interest = (principal * rate * time) / 100

# Displaying the result
print("Simple Interest for 3 years is:", simple_interest)  # Simple Interest for 3 years is: 1500.0


# 2. Numbers 

# a. Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string. Print the result. Try to identify the representation used.
def format_number(value, format_spec):
    formatted = format(value, format_spec)
    return f"The formatted value is: {formatted}"

# Call the function with 145 and 'o'
result = format_number(145, 'o')
print(result)  # The formatted value is: 221

# b. In a village, there is a circular pond with a radius of 84 meters.Calculate the area of the pond using the formula: Circle Area = πr^2. (Use the value 3.14 for π) Bonus Question: If there is exactly 1.4 liters of water in a square meter, what is the total amount of water in the pond? Print the answer without any decimal point in it. Hint: Circle Area = π r^2 Water in the pond = Pond Area Water per Square Meter

# Given values
radius = 84
pi = 3.14
water_per_sq_meter = 1.4

# Calculate area
area = pi * radius ** 2

# Calculate total water
total_water = area * water_per_sq_meter

# Print without decimal
print("Total water in the pond (liters):", int(total_water))  # Total water in the pond (liters): 31019

# c.  If you cross a 490meterlong street in 7 minutes, calculate your speed in meters per second. Print the answer without any decimal point in it. Hint: Speed = Distance / Time

distance = 490  # in meters
time_minutes = 7
time_seconds = time_minutes * 60

speed = distance / time_seconds

# Print speed without decimal
print("Speed in meters per second:", int(speed)) #Speed in meters per second: 1

# 3. If Condition

# a. Write a program to determine the BMI Category based on user input. Ask the user to: Enter height in meters Enter weight in kilograms Calculate BMI using the formula: BMI = weight / (height)2 Use the following categories: If BMI is 30 or greater, print "Obesity"If BMI is between 25 and 29, print "Overweight" If BMI is between 18.5 and 25, print "Normal" If BMI is less than 18.5, print "Underweight"
# Ask the user for input
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine BMI category
if bmi >= 30:
    category = "Obesity"
elif 25 <= bmi < 30:
    category = "Overweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
else:
    category = "Underweight"

# Display the result
print("Your BMI is:", round(bmi, 2))
print("BMI Category:", category)   # Enter your height in meters: 1.75,Enter your weight in kilograms: 68, Your BMI is: 22.2, BMI Category: Normal

# b. Write a program to determine which country a city belongs to. Givenlist of cities per country:Australia = ["Sydney","Melbourne", "Brisbane" ,"Perth"] UAE = ["Dubai" , "Abu Dhabi" , "Sharjah" , "Ajman"] India = ["Mumbai" , "Bangalore" , "Chennai" , "Delhi"] Ask the user to enter a city name and print the corresponding country.

# Define city lists by country
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Ask user for input
city = input("Enter the name of a city: ").strip()

# Normalize input for case-insensitive comparison
city_lower = city.lower()

# Check which country the city belongs to
if city_lower in [c.lower() for c in australia]:
    print(f"{city} is in Australia.")
elif city_lower in [c.lower() for c in uae]:
    print(f"{city} is in UAE.")
elif city_lower in [c.lower() for c in india]:
    print(f"{city} is in India.")
else:
    print(f"Sorry, I don't know which country {city} belongs to.") # Enter the name of a city: Dubai,Dubai is in UAE.

# c. Write a program to check if two cities belong to the same country. Ask the user to enter two cities and print whether they belong to the same country or not.

# Define city lists by country
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Combine into a dictionary for easier lookup
country_map = {
    "Australia": australia,
    "UAE": uae,
    "India": india
}

# Ask user for two cities
city1 = input("Enter the first city: ").strip()
city2 = input("Enter the second city: ").strip()

# Function to find the country of a city
def find_country(city):
    for country, cities in country_map.items():
        if city.lower() in [c.lower() for c in cities]:
            return country
    return None

# Find countries for both cities
country1 = find_country(city1)
country2 = find_country(city2)

# Compare and print result
if country1 and country2:
    if country1 == country2:
        print(f"Yes, both {city1} and {city2} are in {country1}.")
    else:
        print(f"No, {city1} is in {country1} and {city2} is in {country2}.")
else:
    print("One or both cities are not in the known list.")

# 4. File handiling:

# a. student_marks.csv contains the marks and other details for some students.
 # student_marks.csv contains the marks and other details for some students.
 # Write a python program to:
 # 1. Open the file in read mode
 # 2. Create a dictionary from the given data
 # 3. Add a new field to the dictionary total\_marks and store the total marks of
 # the students.
 # 4. Add a new field to the dictionary Average and store the average marks of the
 # students.
 # 5. Create a new file and write this information to the new file
 # (https://www.kaggle.com/arunkumar413/studentmarks) : 

# Step 1: Open the file in read mode
with open('student_marks.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    students = []

    # Step 2–4: Create dictionary, calculate total and average
    for row in reader:
        # Extract only subject marks (assuming columns like 'Math', 'Science', etc.)
        marks = [int(value) for key, value in row.items() if key.lower().startswith('subject') or key.lower() in ['math', 'science', 'english', 'physics', 'chemistry']]
        total = sum(marks)
        average = total / len(marks) if marks else 0

        # Add new fields
        row['Total_Marks'] = total
        row['Average'] = round(average, 2)

        students.append(row)

# Step 5: Write to a new file
fieldnames = list(students[0].keys())  # Get updated fieldnames

with open('student_marks_with_totals.csv', mode='w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print("✅ New file 'student_marks_with_totals.csv' created with total and average marks.")

# Create a new CSV file with the newly created total marks and average marks
import csv

# Step 1: Read the original CSV file
with open('student_marks.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    students = []

    for row in reader:
        # Extract numeric subject marks
        marks = []
        for key, value in row.items():
            try:
                marks.append(float(value))
            except ValueError:
                continue  # Skip non-numeric fields

        # Step 3: Calculate total and average
        total = sum(marks)
        average = total / len(marks) if marks else 0

        # Step 4: Add new fields
        row['Total_Marks'] = round(total, 2)
        row['Average'] = round(average, 2)
        students.append(row)

# Step 5: Write to a new CSV file
fieldnames = students[0].keys()

with open('student_marks_with_totals.csv', mode='w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print("✅ New CSV file 'student_marks_with_totals.csv' created with total and average marks.")

# 5. Inheritence

# a. Create inheritance using MobilePhone as base class and Apple &
# Samsung as child class
# 1. The base class should have properties:
# 1. ScreenType = Touch Screen
# 2. NetworkType = 4G/5G
# 3. DualSim = True or False
# 4. FrontCamera = (5MP/8MP/12MP/16MP)
# 5. rearCamera = (8MP/12MP/16MP/32MP/48MP)
# 6. RAM = (2GB/3GB/4GB)
# 7. Storage = (16GB/32GB/64GB) :-

# Base class
class MobilePhone:
    def __init__(self, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = "Touch Screen"
        self.network_type = "4G/5G"
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def display_specs(self):
        print(f"Screen Type: {self.screen_type}")
        print(f"Network Type: {self.network_type}")
        print(f"Dual SIM: {self.dual_sim}")
        print(f"Front Camera: {self.front_camera}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")

# Child class: Apple
class Apple(MobilePhone):
    def __init__(self):
        super().__init__(
            dual_sim=False,
            front_camera="12MP",
            rear_camera="48MP",
            ram="4GB",
            storage="64GB"
        )

# Child class: Samsung
class Samsung(MobilePhone):
    def __init__(self):
        super().__init__(
            dual_sim=True,
            front_camera="16MP",
            rear_camera="32MP",
            ram="3GB",
            storage="32GB"
        )

# Create objects and display their specs
print("📱 Apple Phone Specs:")
iphone = Apple()
iphone.display_specs()

print("\n📱 Samsung Phone Specs:")
galaxy = Samsung()
galaxy.display_specs()

# b . Create basic mobile phone functionalities in the classes like:
# make_call, recieve_call, take_a_picture, etc :-

# Base class
class MobilePhone:
    def __init__(self, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = "Touch Screen"
        self.network_type = "4G/5G"
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def display_specs(self):
        print(f"Screen Type: {self.screen_type}")
        print(f"Network Type: {self.network_type}")
        print(f"Dual SIM: {self.dual_sim}")
        print(f"Front Camera: {self.front_camera}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")

    # Basic functionalities
    def make_call(self, number):
        print(f"📞 Calling {number}...")

    def receive_call(self, caller):
        print(f"📲 Incoming call from {caller}...")

    def take_a_picture(self, camera='rear'):
        if camera == 'front':
            print(f"🤳 Taking a selfie with {self.front_camera} front camera.")
        else:
            print(f"📷 Taking a photo with {self.rear_camera} rear camera.")

# Child class: Apple
class Apple(MobilePhone):
    def __init__(self):
        super().__init__(
            dual_sim=False,
            front_camera="12MP",
            rear_camera="48MP",
            ram="4GB",
            storage="64GB"
        )

# Child class: Samsung
class Samsung(MobilePhone):
    def __init__(self):
        super().__init__(
            dual_sim=True,
            front_camera="16MP",
            rear_camera="32MP",
            ram="3GB",
            storage="32GB"
        )

# Example usage
iphone = Apple()
galaxy = Samsung()

print("📱 Apple Phone:")
iphone.display_specs()
iphone.make_call("9876543210")
iphone.take_a_picture("front")

print("\n📱 Samsung Phone:")
galaxy.display_specs()
galaxy.receive_call("Mom")
galaxy.take_a_picture("rear")

# c. Use super() constructor for calling parent class’s constructor

# Parent class
class MobilePhone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"MobilePhone initialized: {self.brand} {self.model}")

# Child class
class Apple(MobilePhone):
    def __init__(self, model):
        super().__init__("Apple", model)  # Call parent constructor using super()
        print("Apple-specific setup complete.")

# Another child class
class Samsung(MobilePhone):
    def __init__(self, model):
        super().__init__("Samsung", model)  # Call parent constructor using super()
        print("Samsung-specific setup complete.")

# Create objects
iphone = Apple("iPhone 15")
galaxy = Samsung("Galaxy S23") #  MobilePhone initialized: Apple iPhone 15,Apple-specific setup complete.,MobilePhone initialized: Samsung Galaxy S23,Samsung-specific setup complete.

# d . Make some objects of Apple class with different properties

# Base class
class MobilePhone:
    def __init__(self, model, dual_sim, front_camera, rear_camera, ram, storage):
        self.brand = "Apple"
        self.model = model
        self.screen_type = "Touch Screen"
        self.network_type = "4G/5G"
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def display_specs(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Screen Type: {self.screen_type}")
        print(f"Network Type: {self.network_type}")
        print(f"Dual SIM: {self.dual_sim}")
        print(f"Front Camera: {self.front_camera}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")

# Apple class inherits from MobilePhone
class Apple(MobilePhone):
    def __init__(self, model, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(model, dual_sim, front_camera, rear_camera, ram, storage)

# Creating different Apple phone objects
iphone_13 = Apple("iPhone 13", False, "12MP", "12MP", "4GB", "128GB")
iphone_14_pro = Apple("iPhone 14 Pro", False, "12MP", "48MP", "6GB", "256GB")
iphone_se = Apple("iPhone SE", False, "7MP", "12MP", "3GB", "64GB")

# Display their specs
print("📱 iPhone 13 Specs:")
iphone_13.display_specs()

print("\n📱 iPhone 14 Pro Specs:")
iphone_14_pro.display_specs()

print("\n📱 iPhone SE Specs:")
iphone_se.display_specs()            # 📱 iPhone 13 Specs: Brand: Apple Model: iPhone 13 Screen Type: Touch Screen Network Type: 4G/5G Dual SIM: False Front Camera: 12MP Rear Camera: 12MP RAM: 4GB Storage: 128GB ...


# e. Make some objects of Samsung class with different properties

# Base class
class MobilePhone:
    def __init__(self, brand, model, dual_sim, front_camera, rear_camera, ram, storage):
        self.brand = brand
        self.model = model
        self.screen_type = "Touch Screen"
        self.network_type = "4G/5G"
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def display_specs(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Screen Type: {self.screen_type}")
        print(f"Network Type: {self.network_type}")
        print(f"Dual SIM: {self.dual_sim}")
        print(f"Front Camera: {self.front_camera}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")

# Samsung class inherits from MobilePhone
class Samsung(MobilePhone):
    def __init__(self, model, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__("Samsung", model, dual_sim, front_camera, rear_camera, ram, storage)

# Samsung phone objects
galaxy_s21 = Samsung("Galaxy S21", True, "10MP", "64MP", "8GB", "128GB")
galaxy_a52 = Samsung("Galaxy A52", True, "32MP", "64MP", "6GB", "128GB")
galaxy_m13 = Samsung("Galaxy M13", True, "8MP", "50MP", "4GB", "64GB")

# Display their specs
print("📱 Galaxy S21 Specs:")
galaxy_s21.display_specs()

print("\n📱 Galaxy A52 Specs:")
galaxy_a52.display_specs()

print("\n📱 Galaxy M13 Specs:")
galaxy_m13.display_specs()  # Brand: Samsung Model: Galaxy S21 Screen Type: Touch Screen ,Network Type: 4G/5G ,Dual SIM: True ,Front Camera: 10MP Rear Camera: 64MP RAM: 8GB Storage: 128GB













