import osconfeed_frozenJSON2 as osconfeed
import warnings


DB_NAME = "schedule1_db"
CONFERENCE = "conference.115"


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def load(db):
    raw_data = osconfeed.load()
    warnings.warn(f"loading {DB_NAME}")
    for collection, rec_list in raw_data["Schedule"].items():
        record_type = collection[:1]
        for record in rec_list:
            key = f"{record_type}.{record['serial']}"
            record["serial"] = key
            db[key] = Record(**record)

if __name__ == "__main__":
    import shelve
    db = shelve.open(DB_NAME)
    load(db)
    for k,v in db.items():
        if str(3471) in k:
            print(k,v)
    speaker = db["s.3471"]
    print(speaker.name, speaker.twitter)
db.close()
