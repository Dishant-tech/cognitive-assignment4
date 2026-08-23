df.loc[0, "answer"] = "The annual fee is charged once every year."

print("Updated DataFrame:")

print(df)

df.to_csv("updated_faq.csv", index=False)

print("DataFrame saved to updated_faq.csv")
