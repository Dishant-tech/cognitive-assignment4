def same_category(category_name, df):

    result = df[
        df["category"].str.lower() == category_name.lower()
    ]

    return result


category_name = input("Enter category: ")

result = same_category(category_name, df)

print(result)
