# Saves literally everything to the current working directory.
# This is because using the "Save all as HAR" function really sucks in both
# Chromium and Firefox.
# Chromium's is likely to freeze or fail, and Firefox does not seem to include
# everything (e.g. was recording a stream and the result seemed to have missing
# .ts files).

# You can use some simple bash scripts that involve the use of `type` to help
# you filter through all the files once you're done recording.

from mitmproxy import http
from datetime import datetime

def response(flow: http.HTTPFlow) -> None:
    f = open(datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f"), "wb")
    f.write(flow.response.get_content())
