def construct_url(base_api, endpoint, query=None):
    if not endpoint.startswith('/'):
        endpoint = '/' + endpoint
    url = f"{base_api}{endpoint}"
    if query:
        url += f"?q={query}"
    return url
