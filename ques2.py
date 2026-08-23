def score_query(query, df):

    query_words = set(query.lower().split())

    results = []

    for index, row in df.iterrows():

        keywords = set(row["keywords"].lower().split())

        matched_words = query_words.intersection(keywords)

        if len(matched_words) > 0:

            confidence = len(matched_words) / len(keywords)

            results.append({

                "index": index,

                "question": row["question"],

                "answer": row["answer"],

                "category": row["category"],

                "matched_keywords": ", ".join(matched_words),

                "confidence": confidence

            })

    result_df = pd.DataFrame(results)

    if not result_df.empty:

        result_df = result_df.sort_values(

            by="confidence",

            ascending=False

        )

    return result_df

query = input("\nEnter your query for Q2: ")

result = score_query(query, df)

print("\nQ2: Entries ranked by confidence")

if result.empty:

    print("No matching FAQ found.")

else:

    print(result.to_string(index=False))
