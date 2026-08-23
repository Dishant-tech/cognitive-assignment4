def score_query_with_ties(query, df):

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

    if result_df.empty:
        return result_df

    max_confidence = result_df["confidence"].max()

    result_df = result_df[
        result_df["confidence"] == max_confidence
    ]

    return result_df


query = input("Enter your query: ")

result = score_query_with_ties(query, df)

print("Matching entries:")

print(result)
