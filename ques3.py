def same_category(category_name, df):

    result = df[

        df["category"].str.lower() == category_name.lower()

    ]

    return result

category_name = input("\nEnter category for Q3: ")

print("\nQ3: Entries belonging to the category")

category_result = same_category(category_name, df)

if category_result.empty:

    print("No entries found.")

else:

    print(category_result.to_string(index=False))
