import sys
import urllib.request

if urllib.request.urlopen("http://localhost:8080/health").getcode() == 200:
    sys.exit(0)
else:
    sys.exit(0)
