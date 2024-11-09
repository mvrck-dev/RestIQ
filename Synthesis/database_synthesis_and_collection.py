import numpy as np
import pandas as pd
import names

num_people = 20
num_days = 14
sample_ids = np.arange(1, num_people + 1)
random_names = [names.get_full_name() for _ in range(num_people)]
num_records_per_day = 24
timestamps = pd.date_range(start='2024-09-01', periods=num_days * num_records_per_day, freq='H')
total_records = num_people * num_days * num_records_per_day

#personal information
personal_info = {
    'Name': random_names,
    'Age_group': np.random.choice([ '18-23', '24-29', '30-39', '40-49', '50-59', '60+'], num_people),
    'Profession': np.random.choice(['Engineer', 'Doctor', 'Artist', 'Teacher', 'Student'], num_people),
    'Gender': np.random.choice(['Male', 'Female','Non-Binary', 'Other'], num_people),
    'Ethnicity': np.random.choice(['Asian', 'Black', 'White', 'Hispanic', 'Other'], num_people),
    'Spectacles': np.random.choice(['yes', 'no'], num_people),
    'Person ID': sample_ids,
}

#purpose
purpose = {
    "Person ID":sample_ids,
    'reduce anxiety': np.random.choice(['yes', 'no'], num_people),
    'improve mood': np.random.choice(['yes', 'no'], num_people),
    'reduce fatigue': np.random.choice(['yes', 'no'], num_people),
    'improve sleep cycle': np.random.choice(['yes', 'no'], num_people),
    'improve sleep quality': np.random.choice(['yes', 'no'], num_people),
    'manage chronic health issues': np.random.choice(['yes', 'no'], num_people),
    'solve sleep disorder' : np.random.choice(['yes', 'no'], num_people),
    'optimize overall health and fitness': np.random.choice(['yes', 'no'], num_people),
    'optimize productivity': np.random.choice(['yes', 'no'], num_people),
    'restore energy levels': np.random.choice(['yes', 'no'], num_people),
    'improve overall well-being': np.random.choice(['yes', 'no'], num_people),
    'lessen migraine': np.random.choice(['yes', 'no'], num_people),
    'other':['no'] * num_people
}

for i in range(num_people):
    if all(purpose[key][i] == 'no' for key in purpose if key != 'Person ID' and key != 'other'):
        purpose['other'][i] = 'yes'

filtered_ids = [purpose['Person ID'][i] for i in range(num_people) if purpose['solve sleep disorder'][i] == 'yes']
sample_ids_filtered = len(filtered_ids)

#solve sleep disorder
sleep_disorders = {
    'Person ID': filtered_ids,
    'anxiety or stress': np.random.choice(['yes', 'no'], sample_ids_filtered),
    'insomnia': np.random.choice(['yes', 'no'],sample_ids_filtered ),
    'diagnosed ADHD': np.random.choice(['yes', 'no'], sample_ids_filtered),
    'trouble staying asleep': np.random.choice(['yes', 'no'], sample_ids_filtered),
    'snoring': np.random.choice(['yes', 'no'], sample_ids_filtered),
    'chronic body pain': np.random.choice(['yes', 'no'], sample_ids_filtered),
    'acute pain': np.random.choice(['yes', 'no'], sample_ids_filtered),
    'tobacco effect': np.random.choice(['yes', 'no'], sample_ids_filtered),
    'alcohol effect': np.random.choice(['yes', 'no'], sample_ids_filtered),
    'other': ['no'] * sample_ids_filtered
}

for i in range(sample_ids_filtered):
    if all(sleep_disorders[key][i] == 'no' for key in sleep_disorders if key != 'Person ID' and key != 'other'):
        sleep_disorders['other'][i] = 'yes'

# food intake
food_intake = {
    'Sample ID': np.repeat(sample_ids, 14),
    'Count of Day': np.tile(np.arange(1, 14 + 1), num_people),
    'Amount of Food Intake (cal)': np.random.randint(1500, 3000, num_people * num_days),
    'Felt Hungry at Intervals': np.random.randint(1, 5, num_people * num_days),
    'Number of Meals': np.random.randint(2, 6, num_people * num_days),
    'Caffeine intake': np.random.choice(['yes', 'no'], num_people * num_days),
    'Time': ['NULL'] * (num_people * num_days),
    'Litres of water': np.random.randint(1, 5, num_people * num_days),
    'Intervals of water intake': np.random.randint(1, 3, num_people * num_days),
}
for i in range(num_people * num_days):
    if food_intake['Caffeine intake'][i] == 'yes':
        food_intake['Time'][i] = np.random.randint(6, 18)

# Physical Activity
physical_activity = {
    'Sample ID': np.repeat(sample_ids, 14),
    'Count of Day': np.tile(np.arange(1, 14 + 1), num_people),
    'Number of Steps Walked': np.random.randint(1000, 20000, num_people * num_days),
    'Worked Out (Hours)': np.random.uniform(0, 3, num_people * num_days),
    'Type of Workout': np.random.choice(['Cardio', 'Strength', 'Yoga', 'None'], num_people * num_days),
    'TIme':np.random.choice(['Morning', 'Evening'], num_people * num_days),
    'Calories Lost': np.random.randint(100, 1000, num_people * num_days),
    'Heart Rate (Normal)': np.random.randint(60, 100, num_people * num_days),
    'Heart Rate (During Workout)': np.random.randint(80, 160, num_people * num_days),
    'Time Outs Between Physical Activity': np.random.randint(0, 60, num_people * num_days),
    'Sports (Hours)': np.random.uniform(0, 3, num_people * num_days),
    'Sport': np.random.choice(['Football', 'Basketball', 'Tennis','Badminton', 'Volleyball', 'None'], num_people * num_days)
}

'''phone motion
phone_motion = {
    'Sample ID': np.repeat(sample_ids, num_days * num_records_per_day),
    'count of the day': np.tile(np.arange(1, num_days + 1), num_people * num_records_per_day),
    'Timestamp': np.tile(timestamps, num_people * num_days),
    'Accelerometer X': np.random.uniform(-10, 10, total_records),
    'Accelerometer Y': np.random.uniform(-10, 10, total_records),
    'Accelerometer Z': np.random.uniform(-10, 10, total_records),
    'Gyroscope X': np.random.uniform(-5, 5, total_records),
    'Gyroscope Y': np.random.uniform(-5, 5, total_records),
    'Gyroscope Z': np.random.uniform(-5, 5, total_records),
}'''

#user-habits
user_habits = {
    'person ID': sample_ids,
    'limitting / eliminating caffeine': np.random.choice(['yes', 'no'], num_people),
    'limitting / eliminating alcohol': np.random.choice(['yes', 'no'], num_people),
    'limitting / eliminating smoking': np.random.choice(['yes', 'no'], num_people),
    'getting sunlight in the morning': np.random.choice(['yes', 'no'], num_people),
    'getting exercise': np.random.choice(['yes', 'no'], num_people),
    'wearing earplugs during sleep': np.random.choice(['yes', 'no'], num_people),
    'falling asleep to sounds': np.random.choice(['yes', 'no'], num_people),
    'journaling/reading books before bed': np.random.choice(['yes', 'no'], num_people),
    'wearing eye mask': np.random.choice(['yes', 'no'], num_people),
    'reducing blue light': np.random.choice(['yes', 'no'], num_people),
    'bedroom tempereature': np.random.choice(['cool', 'warm', 'normal'], num_people),
}

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

# Weekday/weekend labels
days = np.tile(np.arange(1, 14 + 1), num_people)
weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
day_labels = [weekdays[(day - 1) % 7] for day in days]
weekend_labels = ['Weekend' if day in ['Saturday', 'Sunday'] else 'Weekday' for day in day_labels]

# Adjustment of sleep cycles for weekends
for i in range(num_people * num_days):
    if weekend_labels[i] == 'Weekend':
        sleep_start_time[i] = (sleep_start_time_demo[i] + 1) % 24
        sleep_end_time[i] = (sleep_start_time_demo[i] + 2) % 24
        wake_up_time[i] = (wake_up_time_demo[i] + 2) % 24
        duration_of_sleep[i] = (wake_up_time_demo[i] + 2 - sleep_start_time_demo[i]) % 24 - 0.5

sleep_need = 8
sleep_debt = np.maximum(0, sleep_need - duration_of_sleep)

sleep_details = {
    'Sample ID': np.repeat(sample_ids, 14),
    'Count of Day': days,
    'Day Label': day_labels,
    'Weekend/Weekday': weekend_labels,
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
    'Phone Usage Before Sleep': np.random.randint(0, 3, num_people * num_days),
    'Sleep Debt': sleep_debt
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
    'Tired After (Hours)': np.random.uniform(0, 8, num_people * num_days),
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
    'Task for the day fullfilled': np.random.choice(['Yes', 'No'], num_people * num_days),
    'phone usage in general':np.random.randint(1,14, num_people * num_days)
}

df_personal_info = pd.DataFrame(personal_info)
df_sleep_details = pd.DataFrame(sleep_details)
df_food_intake = pd.DataFrame(food_intake)
df_physical_activity = pd.DataFrame(physical_activity)
df_profession_activity = pd.DataFrame(profession_activity)
df_end_of_day = pd.DataFrame(end_of_day)
df_sleep_disorders = pd.DataFrame(sleep_disorders)
df_purpose = pd.DataFrame(purpose)
df_user_habits = pd.DataFrame(user_habits)

df_personal_info.to_csv('personal_info.csv', index=False)
df_sleep_details.to_csv('sleep_details.csv', index=False)
df_food_intake.to_csv('food_intake.csv', index=False)
df_physical_activity.to_csv('physical_activity.csv', index=False)
df_profession_activity.to_csv('profession_activity.csv', index=False)
df_end_of_day.to_csv('end_of_day.csv', index=False)
df_sleep_disorders.to_csv('sleep_disorders.csv', index=False)
df_purpose.to_csv('purpose.csv', index=False)
df_user_habits.to_csv('user_habits.csv', index=False)
