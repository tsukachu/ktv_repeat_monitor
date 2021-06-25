from urllib.parse import urlparse


def add_prefix_to_database_name(database_url, prefix="test_"):
    result = urlparse(database_url)
    path = result.path[:1] + prefix + result.path[1:]

    return f"{result.scheme}://{result.netloc}{path}"


def get_database_name(database_url):
    result = urlparse(database_url)
    return result.path[1:]
