import matplotlib.pyplot as plt

# Sample data
days = [1, 2, 3, 4, 5]
study = [1, 2, 3, 4, 2]
play = [2, 1, 1, 2, 1]
sleep = [5, 6, 5, 4, 5]

# Labels for the stack components
labels = ['Study', 'Play', 'Sleep']
colors = ['skyblue', 'orange', 'green']

# Create stack plot
plt.stackplot(days, study, play, sleep, labels=labels, colors=colors)

# Add legend and labels
plt.legend(loc='upper left')
plt.title('Daily Activities')
plt.xlabel('Day')
plt.ylabel('Hours')

# Show plot
plt.show()

import matplotlib.pyplot as plt

# Data
activities = ['Study', 'Play', 'Sleep', 'Other']
hours = [4, 2, 8, 2]
colors = ['skyblue', 'orange', 'lightgreen', 'pink']
explode = (0.1, 0, 0, 0)  # "explode" the 1st slice (Study)

# Create pie chart
plt.pie(hours, labels=activities, colors=colors, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=90)

# Add title
plt.title('Daily Activity Distribution')

# Show plot
plt.axis('equal')  # Ensures pie is a circle
plt.show()
