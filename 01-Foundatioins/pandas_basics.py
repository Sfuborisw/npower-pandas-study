import pandas as pd

# 1. Create a simple dataset (imagine this is your sales data)
data = {
    "Name": ["Boris", "Shaunah", "Alice", "Bob", "Charlie"],
    "Role": ["Analyst", "Specialist", "Analyst", "Manager", "Analyst"],
    "Salary": [55000, 65000, 52000, 80000, 48000],
    "Experience_Years": [1, 5, 2, 10, 1],
}

# 2. Convert to a DataFrame (The core object in Pandas)
df = pd.DataFrame(data)

print("--- Full DataFrame ---")
print(df)

# 3. Filter data: Let's find all "Analysts"
analysts = df[df["Role"] == "Analyst"]

print("\n--- Filtered: Analysts Only ---")
print(analysts)

# 4. Basic Calculation: What is the average salary of an Analyst?
avg_salary = analysts["Salary"].mean()

print(f"\nAverage Analyst Salary: ${avg_salary:,.2f}")

# 5. Quick statistics summary
print("\n--- Statistics Summary ---")
print(df.describe())
