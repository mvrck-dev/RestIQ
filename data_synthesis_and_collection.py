pip install names

import pandas as pd
import numpy as np
import names

num_people = 10
num_days = 14
sample_ids = np.arange(1, num_people + 1)
random_names = [names.get_full_name() for _ in range(num_people)]

#personal information
personal_info = {
    'Name': random_names,
    'Age': np.random.randint(18, 60, num_people),
    'Profession': np.random.choice(['Engineer', 'Doctor', 'Artist', 'Teacher', 'Student'], num_people),
    'Gender': np.random.choice(['Male', 'Female', 'Other'], num_people),
    'Sample ID': sample_ids,
    'Insomniac': np.random.choice(['Yes', 'No'], num_people),
    'Sleeping Pills': np.random.choice(['Rarely', 'Regularly', 'Almost Regular', 'Never'], num_people),
    'Anxiety or Temporary Stress?': np.random.choice(['Yes', 'No'], num_people),
    'Counseling': ['No'] * num_people
}

for i in range(num_people):
    if personal_info['Insomniac'][i] == 'Yes' or personal_info['Anxiety or Temporary Stress?'][i] == 'Yes':
        personal_info['Counseling'][i] = 'Yes'

#sleep details
sleep_start_time_demo = np.random.randint(22, 27, num_people * num_days)
sleep_end_time_demo = np.random.randint(23, 28, num_people * num_days)

sleep_start_time = sleep_start_time_demo % 24
sleep_end_time = (sleep_start_time_demo + 1) % 24

wake_up_time_demo = np.random.randint(26, 34, num_people * num_days)
wake_up_time = wake_up_time_demo % 24

duration_of_sleep = (wake_up_time_demo - sleep_start_time_demo) % 24 - 0.5

mid_day_naps = np.random.choice(['Yes', 'No'], num_people * num_days)
mid_day_nap_durations = np.where(mid_day_naps == 'Yes', np.random.randint(1, 4, num_people * num_days), 0)

sleep_details = {
    'Sample ID': np.repeat(sample_ids, 14),
    'Count of Day': np.tile(np.arange(1, 14 + 1), num_people),
    'Went to Sleep (Start Time)': sleep_start_time,
    'Went to Sleep (End Time)': sleep_end_time,
    'Woke Up At (Time)': wake_up_time,
    'Hours of Sleep': duration_of_sleep,
    'Number of Times Woken Up': np.random.randint(0, 5, num_people * num_days),
    'Heart Rate While Sleeping': np.random.randint(60, 100, num_people * num_days),
    'Mid-Day Naps': mid_day_naps,
    'Mid-Day Nap Duration': mid_day_nap_durations,
    'Dreams': np.random.choice(['Nightmares', 'Happy', 'Normal', 'No Dream'], num_people * num_days),
    'Sleep Quality (1-10)': np.random.randint(1, 11, num_people * num_days),
}

# Food Intake Details
food_intake = {
    'Sample ID': np.repeat(sample_ids, 14),
    'Count of Day': np.tile(np.arange(1, 14 + 1), num_people),
    'Amount of Food Intake (cal)': np.random.randint(1500, 3000, num_people * num_days),
    'Felt Hungry at Intervals': np.random.randint(1 , 5, num_people * num_days),
    'Number of Meals': np.random.randint(2, 6, num_people * num_days)
}

# Physical Activity
physical_activity = {
    'Sample ID': np.repeat(sample_ids, 14),
    'Count of Day': np.tile(np.arange(1, 14 + 1), num_people),
    'Number of Steps Walked': np.random.randint(1000, 20000, num_people * num_days),
    'Worked Out (Hours)': np.random.uniform(0, 3, num_people * num_days),
    'Type of Workout': np.random.choice(['Cardio', 'Strength', 'Yoga', 'None'], num_people * num_days),
    'Calories Lost': np.random.randint(100, 1000, num_people * num_days),
    'Heart Rate (Normal)': np.random.randint(60, 100, num_people * num_days),
    'Heart Rate (During Workout)': np.random.randint(80, 160, num_people * num_days),
    'Time Outs Between Physical Activity': np.random.randint(0, 60, num_people * num_days),
    'Sports (Hours)': np.random.uniform(0, 3, num_people * num_days),
    'Sport': np.random.choice(['Football', 'Basketball', 'Tennis','Badminton', 'Volleyball', 'None'], num_people * num_days)
}

# Profession Related Activity
profession_activity = {
    'Sample ID': np.repeat(sample_ids, 14),
    'Count of Day': np.tile(np.arange(1, 14 + 1), num_people),
    'Mental Work (Hours)': np.random.uniform(0, 8, num_people * num_days),
    'Number of Times Yawned': np.random.randint(0, 20, num_people * num_days),
    'Speed of Working': np.random.choice(['Normal', 'Slower', 'Faster'], num_people * num_days),
    'Cognitive Thinking Process': np.random.choice(['Normal', 'Slower', 'Higher'], num_people * num_days),
    'Number of Breaks' : np.random.randint(0, 3, num_people * num_days),
    'Could Do Tasks': np.random.choice(['Yes', 'No'], num_people * num_days),
    'Tired After (Hours)': np.random.uniform(0, 8, num_people * num_days)
}

# End of Day Questions
end_of_day = {
    'Sample ID': np.repeat(sample_ids, 14),
    'Count of Day': np.tile(np.arange(1, 14 + 1), num_people),
    'Stress Level (1-10)': np.random.randint(1, 11, num_people * num_days),
    'Mood (1-10)': np.random.randint(1, 11, num_people * num_days),
    'Tired All Day': np.random.choice(['Yes', 'No'], num_people * num_days),
    'Current Mood (1-10)': np.random.randint(1, 11, num_people * num_days),
    'Sleepy': np.random.choice(['Yes', 'No'], num_people * num_days),
    'Tired Now': np.random.choice(['Yes', 'No'], num_people * num_days),
    'Task for the day fullfilled': np.random.choice(['Yes', 'No'], num_people * num_days)
}

df_personal_info = pd.DataFrame(personal_info)
df_sleep_details = pd.DataFrame(sleep_details)
df_food_intake = pd.DataFrame(food_intake)
df_physical_activity = pd.DataFrame(physical_activity)
df_profession_activity = pd.DataFrame(profession_activity)
df_end_of_day = pd.DataFrame(end_of_day)

df_personal_info.to_csv('personal_info.csv', index=False)
df_sleep_details.to_csv('sleep_details.csv', index=False)
df_food_intake.to_csv('food_intake.csv', index=False)
df_physical_activity.to_csv('physical_activity.csv', index=False)
df_profession_activity.to_csv('profession_activity.csv', index=False)
df_end_of_day.to_csv('end_of_day.csv', index=False)
