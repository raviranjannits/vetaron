def generateAnswer(ques ,index , embeddings , llm):
    query = ques
    docs = index.query(
        #namespace="example-namespace",
        vector = embeddings.embed_query(query),
        top_k=3,
        include_values=True ,
        include_metadata=True
    )

    Data=""
    for data in docs["matches"]:
        Data += data["metadata"]["data"]
        Data+="\n"

    prompt = f"""
    Use the following pieces of information to answer the user's question.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    Context: {Data}
    Question: {ques}

    Only return the helpful answer below and nothing else.
    Helpful answer:
    """
    response = llm(prompt)

    return response