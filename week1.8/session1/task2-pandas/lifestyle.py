import pandas 

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?
# dataframe
# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.



# Find the total number of students
total_students = data.shape[0]

# Find the mean average GPA of the students
print(data['GPA'].mean())

# Find the standard deviation of how much sleep students get per day
print(data['Sleep_Hours_Per_Day'].std())

# Find the maximum amount of study hours per day
print(data['Study_Hours_Per_Day'].max())

# Sort the students by social hours per day ascending (lowest -> highest)
print(data.sort_values(by='Social_Hours_Per_Day'))

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
data['Total_Hours'] = data['Sleep_Hours_Per_Day'] + data['Study_Hours_Per_Day'] + data['Social_Hours_Per_Day']
print(data)

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
print(data[data['Stress_Level'] == 'high'])
print(data[data['Stress_Level'] == 'low'])
# Can you work out whether having a higher stress level leads to a higher GPA?
print("High stress level students have a mean GPA of: ", data[data['Stress_Level'] == 'high']['GPA'].mean())
print("Low stress level students have a mean GPA of: ", data[data['Stress_Level'] == 'low']['GPA'].mean())
