def score_query_with_ties(query, df):

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

    if result_df.empty:

        return result_df

    max_confidence = result_df["confidence"].max()

    tied_results = result_df[

        result_df["confidence"] == max_confidence

    ]

    return tied_results

tie_query = input("\nEnter query for Q6: ")

tie_result = score_query_with_ties(tie_query, df)

print("\nQ6: Matching entries with highest confidence")

if tie_result.empty:

    print("No matching FAQ found.")

else:

    print(tie_result.to_string(index=False))
