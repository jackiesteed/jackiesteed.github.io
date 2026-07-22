import urllib.request
try:
    req = urllib.request.urlopen('https://www.sdust.edu.cn/favicon.ico', timeout=5)
    print("favicon.ico exists, content type:", req.headers.get('Content-Type'))
except Exception as e:
    print("favicon.ico failed:", e)
