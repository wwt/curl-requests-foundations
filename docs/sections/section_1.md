# REST API Access With cURL

## :material-bash: cURL Overview

[cURL](https://curl.se "cURL Homepage"){target=_blank} is an open-source Linux tool that allows your CLI to act as an HTTP client[^1]  Think of **cURL** sort of like a text-based web browser that you can use to do things like:

- Test and troubleshoot HTTP connectivity to a server.
- Interact with REST APIs.
- Download or upload files.
- Test certificate validity.

---

### :fontawesome-solid-file-code: cURL In Action

Because the native response format for **cURL** is unstructured text[^2], **cURL** typically is not part of programmatic workflows.  However, **cURL** has a wide variety of use cases and is an essential part of your development skillset.

???+ example "cURL Example"

    Here is a quick example of how **cURL** can make a REST API call to a [free, public service](https://jsonplaceholder.typicode.com/ "{JSON} Placeholder"){target=_blank} that provides a REST API test platform:

    1. You can paste this cURL command in just about any Linux environment and press ++enter++ or ++"Return"++ to send the request:

        ???+ note "Example cURL Command"
        
            ```shell
            curl https://jsonplaceholder.typicode.com/posts/1
            ```

    2. The response from the server should look something like this:

        ???+ done "Example Server Response"
        
            ```shell
            {
              "userId": 1,
              "id": 1,
              "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
              "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
            }
            ```

---

### :material-cursor-text: cURL Command Option Reference

**cURL** and a slew of configuration options, and you can find a reference for some of the more common options below:

???+ example "cURL Command Options"
    | Option                                         | Shorthand        | Purpose                                                                            |
    | :--------------------------------------------- | :--------------- | :--------------------------------------------------------------------------------- |
    | `--request`                                    | `-X`             | HTTP request method - `GET`[^3], `POST`, `PUT`, `PATCH`, `DELETE`                  |
    | `--header`                                     | `-H`             | HTTP client header(s) in key/value pairs - `"Content:application/json"`            |
    | `--url <url>`                                  |  N/A             | Request URL                                                                        |
    | `--cookie-jar <file_name>`                     | `c`              | Write session cookies to a local file                                              |
    | `--cookie <file_name>`                         | `-b`             | Send session cookies stored in a local file                                        |
    | `--data`, `--data-raw`, and `--data-urlencode` | `-d`             | HTTP request body, typically for `POST`, `PUT`, and `PATCH` methods                |
    | `--include`                                    | `-i`             | Display the response headers and response body in STDOUT                           |
    | `--head`                                       | `-I`             | Display ONLY the response headers in STDOUT                                        |
    | `--insecure`                                   | `-k`             | Allow insecure or self-signed certificates (insecure TLS)                          |
    | `--location`                                   | `-L`             | Follow HTTP 3XX redirect server responses                                          |
    | `--output <file_name>`                         | `-o <file_name>` | Write response to a file, instead of STDOUT                                        |
    | `--user`                                       | `-u`             | HTTP Basic Auth credentials in a key/value pair - `"user_name:password"`           |
    | `--verbose`                                    | `-v`             | Display detailed info for debugging (headers, TLS handshake messages, etc.)        |

---

## :fontawesome-solid-check: Moving On

You have the basics of **cURL** now, and it's time to take a look at **Python Requests**.  Click [here](../section_2/ "Next Section") to move to the next section.

[^1]: **cURL** supports many more protocols than HTTP, and those protocols are beyond the scope of this repository.
[^2]: Tools like [**JQ**](https://stedolan.github.io/jq/ "JQ Documentation"){target=_blank}, for example, can format JSON text into structured data.
[^3]: Default, when omitted.

--8<-- "includes/glossary.txt"
