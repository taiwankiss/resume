import http.server
import functools

handler = functools.partial(
    http.server.SimpleHTTPRequestHandler,
    directory="/Users/taiwankiss/Documents/WEI/Ai/Resume"
)
http.server.test(HandlerClass=handler, port=8843)
