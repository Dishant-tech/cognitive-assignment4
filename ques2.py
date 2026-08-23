def score_query(query, df):

    query_words = set(query.lower().split())

    results = []

    for index, row in df.iterrows():

        keywords = set(row["keywords"].lower().split())

        matched_words = query_words.intersection(keywords)

        if len(matched_words) > 0:

            confidence = len(matched_words) / len(keywords)

            results.append({
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "confidence": confidence
            })

    result_df = pd.DataFrame(results)

    if not result_df.empty:
        result_df = result_df.sort_values(
            "confidence",
            ascending=False
        )

    return result_df


query = input("Enter your query: ")

result = score_query(query, df)

print(result)
