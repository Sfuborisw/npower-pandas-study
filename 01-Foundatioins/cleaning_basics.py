import pandas as pd
import numpy as np

# 1. Create a "dirty" dataset (simulating real-world scenarios)
raw_data = {
    "Date": ["2026-02-10", "2026-02-11", "2026-02-12", np.nan],  # Has missing values
    "Product": [" Latte", "Mocha ", "Latte", "Espresso"],  # Has extra spaces
    "Sales": [5.5, 6.0, "5.5", 4.5],  # Messy format (String vs Float)
    "Customer_ID": [101, 102, 101, 103],
}

df = pd.DataFrame(raw_data)
print("--- Raw Data ---")
print(df)

# --- Technique 1: Handle spaces (String Stripping) ---
# Fix ' Latte' and 'Mocha ' issues
df["Product"] = df["Product"].str.strip()

# --- Technique 2: Handle formats (Data Types) ---
# Convert Sales to numbers so we can calculate
df["Sales"] = pd.to_numeric(df["Sales"])

# --- Technique 3: Handle missing values (Handling Missing Values) ---
# Drop rows with missing values, or fill them (e.g., fill with 'Unknown')
df_cleaned = df.dropna(subset=["Date"])

print("\n--- Cleaned Data ---")
print(df_cleaned)
print("\nTotal Sales:", df_cleaned["Sales"].sum())
