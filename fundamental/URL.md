# URL — Lecture Notes

## Definition
- **URL** (Uniform Resource Locator): a compact string that specifies the location of a resource on the internet and the protocol used to access it. URLs are used by browsers, APIs, and networked applications to locate resources.

## URL vs URI vs URN
- **URI (Uniform Resource Identifier):** Generic identifier for a resource.
- **URL:** A type of URI that provides a means to locate the resource (includes access method and location).
- **URN (Uniform Resource Name):** A URI that names a resource without implying its location or how to obtain it.

## General Structure
The typical components of an URL:

```
scheme://[user:pass@]host[:port]/path/to/resource[?query][#fragment]
```

- **Scheme (protocol):** e.g., `http`, `https`, `ftp`, `mailto`, `file` — indicates how to access the resource.
- **Userinfo (optional):** `user:password@` (rarely used in modern practice for security reasons).
- **Host:** Domain name or IP (e.g., `example.com`, `192.0.2.1`).
- **Port (optional):** Network port (default 80 for HTTP, 443 for HTTPS).
- **Path:** Resource path on the server (e.g., `/docs/index.html`).
- **Query string (optional):** `?key=value&key2=value2` — parameters passed to the server or application.
- **Fragment (optional):** `#section` — client-side reference within the resource (not sent to the server).

## Examples
- Basic HTTP URL:
```
https://example.com/path/page.html
```
- URL with query parameters:
```
https://api.example.com/search?q=data+analytics&limit=10
```
- FTP URL:
```
ftp://ftp.example.com/files/archive.zip
```
- Mailto (opens email client):
```
mailto:alice@example.com?subject=Hi
```

## URL Encoding (Percent-encoding)
- Use percent-encoding for unsafe characters and spaces (space → `%20`).
- Example: `https://example.com/search?q=C%23+tutorial` (C# encoded as `C%23`).

## Query Parameters — Conventions
- Format: `?key1=value1&key2=value2`
- Multiple values: repeated keys (`?tag=math&tag=python`) or comma-separated values depending on API design.
- When designing APIs, prefer clear parameter names and document expected types and defaults.

## Practical Notes
- **Default ports:** Omit the port when using the standard port for a scheme (HTTP 80, HTTPS 443).
- **Fragments** are processed by the client and are not submitted to servers.
- **Case sensitivity:** Scheme and host are case-insensitive; path and query are often case-sensitive depending on server.
- **Security:** Prefer `https` over `http` to encrypt data in transit and protect credentials/query data.

## Parsing & Using URLs (Examples)
- Using `curl` to GET a URL:
```bash
curl "https://api.example.com/items?id=42"
```
- Parse URL in Python:
```python
from urllib.parse import urlparse, parse_qs

u = urlparse('https://example.com/search?q=test&page=2#top')
print(u.scheme, u.netloc, u.path)
print(parse_qs(u.query))
```

## RESTful URL Design Tips
- Use nouns for resources: `/users/123/orders` (not verbs).
- Keep URLs hierarchical and predictable.
- Use query parameters for filtering, sorting, and pagination.
- Avoid exposing implementation details in URLs.

## Common Schemes
- `http`, `https`, `ftp`, `ftps`, `mailto`, `file`, `ws` (WebSocket), `wss` (secure WebSocket)

## Troubleshooting
- `404 Not Found`: resource path incorrect or resource removed.
- `403 Forbidden`: permission issue.
- `500` series: server-side error.
- Use browser dev tools or `curl -v` to inspect requests and responses.

---

Prepared as concise lecture notes covering definition, structure, examples, and usage of URLs.

