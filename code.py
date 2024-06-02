#import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Load the Dataset. Assign as df
df = pd.read_csv(r'C:\Users\hp\Downloads\Nutrical Dataset(Project 1).csv')

# First 5 Rows of the dataset 
df.head() 

# Inspecting there is any null value
print(df.isnull().sum())

# Providing the summary of the dataset.
df.describe()

# Evaluating the dataset that there is no null value
df.info()

#Plotting the distribution of Calories Count Across the Menu Items
plt.figure(figsize=(10, 6))
sns.histplot(df['Calories'], kde=True, color='green') # type: ignore
plt.title('Distribution of Calories Across Menu Items')
plt.xlabel('Calories')
plt.ylabel('Frequency')
plt.show()

# Boxplot different Category by Total Fat, Protein , Carbohydrates.
plt.figure(figsize=(12,8))
plt.subplot(3, 1, 1)
sns.boxplot(x='Category', y='Total Fat', data=df) # type: ignore
plt.title('Total Fat Content by Category')
plt.subplot(3, 1, 2)
sns.boxplot(x='Category', y='Protein', data=df) # type: ignore
plt.title('Protein Content by Category')
plt.subplot(3, 1, 3)
sns.boxplot(x='Category', y='Carbohydrates', data=df) # type: ignore
plt.title('Total Carbohydrates Content by Category')
plt.tight_layout()
plt.show()

#Trends in nutritional content across different food Category
avg_nutrition= df.groupby('Category')[['Total Fat','Protein', 'Carbohydrates']].mean()
print(avg_nutrition)

# Bar chart for average calories by category
avg_calories = df.groupby('Category')['Calories'].mean().sort_values()
plt.figure(figsize=(10, 6))
avg_calories.plot(kind='bar',color='#51647B')
plt.title('Average Calories by Food Category')
plt.xlabel('Category')
plt.ylabel('Average Calories')
plt.show()

# Bar chart comparing nutritional characteristics of different food categories
nutritional_cols = ['Total Fat', 'Saturated Fat', 'Cholesterol', 
'Sodium', 'Carbohydrates', 'Dietary Fiber', 'Sugars', 'Protein']
nutritional_data = df.groupby('Category')[nutritional_cols].mean()
nutritional_data.plot(kind='bar', figsize=(12, 6))
plt.title('Average Nutritional Content by Category')
plt.xlabel('Category')
plt.ylabel('Average Value')
plt.xticks(rotation=45)
plt.show()

 # Nutritional comparison for a few selected categories
selected_categories = ['Burgers', 'Salads', 'Desserts']
selected_data = df[df['Category'].isin(selected_categories)]
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Calories', data=selected_data) # type: ignore
plt.title('Calorie Comparison of Selected Categories')
plt.xlabel('Category')
plt.ylabel('Calories')
plt.show()

# Identify items with highest calories
highest_calorie_item =  df[df['Calories'] == df['Calories'].max()]
print(highest_calorie_item)

# Identify items with lowest calories.
lowest_calorie_item =  df[df['Calories'] == df['Calories'].min()]
print(lowest_calorie_item)
