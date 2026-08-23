print("\nQ4: Updating one FAQ entry")

df.loc[0, "answer"] = "The annual fee is charged once every year. Please check your billing section for details."

df.to_csv("updated_faq.csv", index=False)

print("Updated DataFrame:")

print(df)

print("\nDataFrame saved successfully as updated_faq.csv")
