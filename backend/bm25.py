from rank_bm25 import BM25Okapi


def rank(text, size):
    """
    Fetch top @code{size} docs related to the given @code{text}
    :text str: user input
    :size int: number of relevent docs to return
    :return [{title: str, citations: str, dio: int, abstract: str}]:
        a list of dictionaries, each dictionary contains four keys:
            - title: title of the article
            - citations: number of times the article has been cited
            - doi: doi of the article
            - abstract: abstract of the article
    """
    example_result = [{'title': 't1', 'citations': 1, 'dio': '10.1007/978-3-540-46138-8_46',
                       'abstract': 'abstract1'},
                      {'title': 't2', 'citations': 2, 'dio': '20.1007/978-3-540-46138-8_46',
                       'abstract': 'abstract2'}]
    return example_result
