from duckduckgo_search import DDGS

def search_best_practices(query):

    results = []

    with DDGS() as ddgs:

        for r in ddgs.text(query, max_results=3):

            results.append(r["title"])

    return "\n".join(results)
