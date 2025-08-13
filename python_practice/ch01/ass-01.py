import pandas as pd

temp_data = [
    [-0.1, 0.0, -0.1, -0.2], 
    [1.8, 2.0, 1.6, 1.6],    
    [6.4, 6.8, 5.8, 5.9],    
    [12.3, 12.9, 11.5, 11.5], 
    [17.9, 18.5, 17.1, 17.1], 
    [22.2, 22.8, 21.6, 21.5]  
]

months = ['january', 'february', 'march', 'april', 'may', 'june']
cities = ['City1', 'City2', 'City3', 'City4']

df = pd.DataFrame(data=temp_data, index=months, columns=cities)

print("\nMonthly Average Temperature Statistics Table")
print("-----------------------------------------")
print(df)
print("-----------------------------------------")


print("\nAverage Temperature in March for City2:")
print(df.loc['march', 'City2'])

print("\nAverage Temperature in April for City4:")
print(df.loc['april', 'City4'])

print("\nAverage Temperature in January for City3:")
print(df.loc['january', 'City3'])

print("\nAverage Temperature in June for City1:")
print(df.loc['june', 'City1'])