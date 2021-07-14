# REST API Access With Python Requests

## :fontawesome-brands-python: Python Requests

[Python Requests](https://docs.python-requests.org/ "Python Requests Homepage"){target=_blank} is a third-party[^1] tool that allows you to write simple, human-readable REST API calls in Python.  Although the [Python Standard Library](https://docs.python.org/3/library/ "Python Standard Library"){target=_blank} contains a module which can make REST API calls[^2], [official Python documentation](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "Python urllib.request Documentation"){target=_blank} recommends the use of the **Python Requests** module because of its higher-level, more consumable interface.

**Python Requests** is an excellent tool for doing things like:

- Obtaining configuration and state information from a variety of REST-based IT systems.
- Sending configuration changes to different REST APIs.
- Automatically managing HTTP session state.
- Using simple keywords to convert Python objects into HTTP/REST API-compatible formats automatically.
- Converting server response data into Python objects.
- Managing HTTP exceptions.
- Building REST API interactions into your automated workflows.

---

### :fontawesome-solid-file-code: Python Requests In Action

For the most part, only your imagination limits what you can do with REST APIs and **Python Requests**.  Because of Python's programmatic flexibility, you can automate just about any task exposed by REST APIs.  Knowing how to use **Python Requests** is a skill that will help you automate both complex and straightforward workflows.

???+ example "Python Requests Example"

    Here is a quick example of how **Python Requests** can make a REST API call to a [free, public service](https://jsonplaceholder.typicode.com/ "{JSON} Placeholder"){target=_blank} that provides a REST API test platform:

    1. You can paste this Python Requests code into a Python 3.x interpreter and press ++enter++ or ++"Return"++ to send the request:

        ???+ note "Example Python Requests Command"
        
            ```python
            import requests
            req_url = 'https://jsonplaceholder.typicode.com/posts/1'
            req_headers = {'Content-Type':'application/json'}
            response = requests.get(req_url, headers=req_headers)
            print(f'{response.status_code} {response.reason}')
            print(response.json())
            ```

    2. The response from the server should look something like this:

        ???+ done "Example Server Response"
        
            ```python
            200 OK
            {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
            ```

---

### :material-code-braces: Python Requests Parameters Reference

**Python Requests** has many [parameters](https://docs.python-requests.org/en/latest/api/ "Python requests.request() Method Parameters") and you can find a reference for some of the more common parameters and keywords below:

???+ example "Python Requests Parameters"
    | Parameter | Class                 | Description                                                                      |
    | :-------- | :-------------------- | :------------------------------------------------------------------------------- |
    | `method`  | `str`                 | HTTP request method[^3] - `GET`, `POST`, `PUT`, `PATCH`, `DELETE`                |
    | `url`     | `str`                 | Request URL[^3]                                                                  |
    | `data`    | `dict`                | Form-encoded HTTP request body, typically for `POST`, `PUT`, and `PATCH` methods |
    | `json`    | `dict`                | JSON-encoded HTTP request body, typically for `POST`, `PUT`, and `PATCH` methods |
    | `headers` | `dict`                | HTTP client header(s) in key/value pairs - `{"Content": "application/json"}`     |
    | `cookies` | `dict` or `CookieJar` | HTTP cookies in key/value pairs - `{"Session_Token": "1234567890"}`              |
    | `auth`    | `tuple`               | HTTP Basic Auth credentials in a key/value pair - `("user_name", "password")`    |
    | `timeout` | `float` or `tuple`    | Number of seconds to wait for the server to respond to a request[^4]             |
    | `verify`  | `bool`                | Allow insecure or self-signed certificates (insecure TLS)[^5]                    |

---

## :material-code-braces: Python Requests Response Object Reference

The response from a **Python Requests** request is an [object](https://docs.python-requests.org/en/latest/api/#requests.Response "Python requests.Response class Attributes and Methods") with many attributes and methods.  The data available in the `Response` object will help you understand whether or not your REST API call was successful and give you detailed information, often in a structured data format, that you can use programmatically.  You can find a reference for some of the more common attributes and methods below:

???+ example "Python Requests Response Object Attributes & Methods[^6]"
    | Name                 | Return Object | Description                                                                            |
    | :------------------- | :------------ | :------------------------------------------------------------------------------------- |
    | `cookies`            | `CookieJar`   | Cookies returned by the server                                                         |
    | `headers`            | `dict`        | Response headers from the server                                                       |
    | `json()`             | `dict`        | JSON-encoded response body from the server                                             |
    | `links`              | `dict`        | And links found within the response header from the server                             |
    | `ok`                 | `bool`        | `True` if the HTTP status code is < `400`, `False` if the HTTP status code is >= `400` |
    | `raise_for_status()` | `HTTPError`   | Raise an `Exception` of the `HTTPError` type, if the HTTP status code is >= `400`      |
    | `reason`             | `str`         | HTTP reason text - `OK`, `Not Found`, `Bad Request`, etc.                              |
    | `status_code`        | `str`         | HTTP status code - `200`, `404`, `400`, etc.                                           |
    | `text`               | `str`         | Unicode-encoded response body from the server                                          |
    | `url`                | `str`         | Final URL location of the server response, including redirects                         |

## :fontawesome-solid-check: Keep Rolling

You have all of the information you need to get started with the hands-on exercises.  Click [here](../section_3/ "Next Section") to move to the next section.

[^1]: Installed with the [Python pip Package Management Tool](https://pypi.org/project/requests2/ "Python Requests on PyPI"){target=_blank}.
[^2]: Python [`urllib` module](https://docs.python.org/3/library/urllib.html "Python urllib Module"){target=_blank}.
[^3]: Required parameter.
[^4]: Default timeout is **unlimited** and, although not required, should be set.
[^5]: Default is `True`.
[^6]: Any item in the table below with trailing `()` characters is a `method` and all other items are `attributes`.

--8<-- "includes/glossary.txt"
