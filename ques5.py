category_count = df.groupby("category").size()

print("Number of FAQ entries in each category:")

print(category_count)
