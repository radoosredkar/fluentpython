from urllib.request import urlopen
import warnings
import os
import json

URL = "http://www.oreilly.com/pub/sc/osconfeed"
JSON = "osconfeed.json"


def load():
    if not os.path.exists(JSON):
        msg = f"downloading {URL} to {JSON}"
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, "wb") as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)


def __main__():
    result = load()
    print(sorted(result["Schedule"].keys()))
    for key, value in sorted(result["Schedule"].items()):
        print(f"{len(value)} {key}")

if __name__ == "__main__":
    load
