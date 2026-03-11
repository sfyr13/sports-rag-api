import wikipedia

def search_wikipedia(query: str):
    """Search Wikipedia for a given query and return top results."""
    results = wikipedia.search(query)
    return results



def get_page_content(title: str):
    """
    Fetch full content of a Wikipedia page safely.
    Tries to handle PageError and DisambiguationError.
    """
    try:
        page = wikipedia.page(title)
        return {
            "title": page.title,
            "content": page.content,
            "url": page.url
        }
    except wikipedia.DisambiguationError as e:
        # If disambiguation, pick the first option
        first_option = e.options[0]
        page = wikipedia.page(first_option)
        return {
            "title": page.title,
            "content": page.content,
            "url": page.url
        }
    except wikipedia.PageError:
        # Page not found, return empty
        return {
            "title": title,
            "content": "",
            "url": ""
        }