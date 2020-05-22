from flags import save_flag, get_flag, show, main
import time
from concurrent import futures

MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + "-th" + ".gif")
    return cc


def download_many(cc_list):
    # cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in cc_list:
            furure = executor.submit(download_one, cc)
            to_do.append(furure)
            print(f"Scheduled for {cc}: {furure}")
    results = []
    for future in futures.as_completed(to_do):
        res = furure.result()
        print(f"{furure} result: {res}")
        results.append(res)
    return len(results)


if __name__ == "__main__":
    main(download_many)
