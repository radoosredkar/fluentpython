import os
import time
import sys

import requests
import ipdb

POP20_CC = ("CN IN US ID BR PK NG BD RU JP " "MX PH VN ET EG DE IR TR CD FR").split()
BASE_URL = (
    "https://www.cia.gov/library/publications/the-world-factbook/attachments/flags"
)

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
DEST_DIR = f"{THIS_FOLDER}/downloads/"


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, "wb+") as fp:
        fp.write(img)


def get_flag(cc):
    url = f"{BASE_URL}/{cc.upper()}-flag.gif"
    resp = requests.get(url)
    if resp.status_code != 200:
        resp.raise_for_status()
    print(resp.status_code, end=" ")
    return resp.content


def show(text):
    print(text)
    sys.stdout.flush()


def download_many(cc_list):
    for cc in sorted(cc_list):
        try:
            image = get_flag(cc)
        except requests.exceptions.HTTPError as exc:
            res = exc.response
            if res.status_code == 404:
                status = HTTPStatus.not_found
                msg = "Not found"
            else:
                raise
        else:
            show(cc)
            save_flag(image, cc.lower() + ".gif")
            status = HTTPStatus.OK
            msg = "OK"
            status = HTTPStatus.OK
            msg = "OK"
        print(cc, msg)
    return len(cc_list)


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = f"\n{count} flags downloaded in {elapsed:.2f}s"
    print(msg)


if __name__ == "__main__":
    main(download_many)
