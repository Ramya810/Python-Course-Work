# LinkedIn Profile System

# Input Section
profile_id = int(input("Enter LinkedIn Profile ID: "))
user_name = input("Enter Full Name: ")
current_position = input("Enter Current Job Title: ")
years_experience = float(input("Enter Total Years of Experience: "))

# List input
skills = [skill.strip() for skill in input("Enter Skills (comma-separated): ").split(',')]

# Tuple input
location = (
    input("Enter City: "),
    input("Enter Country: ")
)

# Float input
profile_strength = float(input("Enter Profile Strength Percentage: "))

# Set input
connections = set(input("Enter Top Connections (comma-separated): ").split(','))

# Dictionary input
company_name = input("Enter Current Company Name: ")
company_location = input("Enter Company Location: ")
company_info = {
    "Company": company_name,
    "Location": company_location
}

# Output Section
print("\n        ****LinkedIn Profile Summary****      ")

# 1. Comma Separation
print("Profile ID, Name, Experience:", profile_id, user_name, years_experience, sep=',')

# 2. Percentage Formatting
print("Profile Strength: %.2f%%" % profile_strength)

# 3. f-strings
print(f"Name: {user_name}")
print(f"Current Position: {current_position}")
print(f"Location: {location[0]}, {location[1]}")
print(f"Skills: {skills}")
print(f"Top Connections: {connections}")

# 4. .format() method
print("Current Company: {} ({})".format(company_info["Company"], company_info["Location"]))

#Output
'''Enter LinkedIn Profile ID: 838944
Enter Full Name: Keshetty Ramya Sri
Enter Current Job Title: Software Engineer
Enter Total Years of Experience: 01
Enter Skills (comma-separated): python,java,tableau,powerbi,C
Enter City: Hyderabad
Enter Country: india
Enter Profile Strength Percentage: 82.9
Enter Top Connections (comma-separated): varun,maahi,maira
Enter Current Company Name: Codegnan
Enter Company Location: Kukatpally

--- LinkedIn Profile Summary ---
Profile ID, Name, Experience:,838944,Keshetty Ramya Sri,1.0
Profile Strength: 82.90%
Name: Keshetty Ramya Sri
Current Position: Software Engineer
Location: Hyderabad, india
Skills: ['python', 'java', 'tableau', 'powerbi', 'C']
Top Connections: {'varun', 'maahi', 'maira'}
Current Company: Codegnan (Kukatpally)'''