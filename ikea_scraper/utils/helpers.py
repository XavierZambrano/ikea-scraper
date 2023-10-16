import requests
from scrapy.http import Response, TextResponse, Request


def fake_response_from_file(file_path: str, url: str = None):
    """
    Create a Scrapy fake HTTP response from a HTML file
    @param file_path: The filepath
    @param url: The URL of the response.
    returns: A scrapy HTTP response which can be used for unittesting.
    """
    if not url:
        url = 'http://www.example.com'

    request = Request(url=url)

    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()

    response = TextResponse(
        url=url,
        request=request,
        body=file_content,
        encoding='utf-8',
    )

    return response
