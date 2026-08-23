print("\nQ5: Number of FAQ entries in each category")

category_counts = df.groupby("category").size()

print(category_counts)
