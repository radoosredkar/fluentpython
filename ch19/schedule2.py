import warnings
import inspect
import osconfeed

DB_NAME = "schedula2.db"
CONFERENCE = "conference_115"


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented


class MissingDatabaseRecord(RuntimeError):
    """Raised when database was required but was not set"""


class DbRecord(Record):

    __db = None

    @staticmethod
    def set_db(db):
        DbRecord.__db = db

    @staticmethod
    def get_db():
        return DbRecord.__db

    @classmethod
    def fetch(cls, ident):
        db = cls.get_db()
        try:
            return db[ident]
        except TypeError:
            if db is None:
                msg = f"database not set; call '{cls.__name__}.set_db(my_db)'"
                raise MissingDatabaseRecord(msg)
            else:
                raise

    def __repr__(self):
        if hasattr(self, "serial"):
            cls_name = self.__class__.__name__
            return f"{cls_name} serial={self.serial}"
        else:
            return super().__repr__()


class Event(DbRecord):
    @property
    def venue(self):
        key = f"venue.{self.venue_serial}"
        return self.__class__.fetch(key)

    @property
    def speakers(self):
        if not hasattr(self, "_speaker_objs"):
            spr_serials = self.__dict__["speakers"]
            fetch = self.__class__.fetch
            self._speaker_objs = [fetch(f"speaker.{key}") for key in spr_serials]
            return self._speaker_objs

    def __repr__(self):
        if hasattr(self, "name"):
            cls_name =self.__class__.__name__
            return f"{cls_name} {self.name}"
        else:
            return super().__repr__()


def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn(f"loading " + DB_NAME)
    for collection, rec_list in raw_data["Schedule"].items():
        record_type = collection[:-1]
        cls_name = record_type.capitalize()
        cls = globals().get(cls_name, DbRecord)
        if inspect.isclass(cls) and issubclass(cls, DbRecord):
            factory = cls
        else:
            factory = DbRecord
        for record in rec_list:
            key = f"{record_type}.{record['serial']}"
            record["serial"] = key
            db[key] = factory(**record)

if __name__ == "__main__":
    import shelve
    db = shelve.open(DB_NAME)
    load_db(db)
    DbRecord.set_db(db)
    event = DbRecord.fetch('event.33950')
    print(event)
    print(event.venue)
    print(event.venue.name)
    for spkt in event.speakers:
        print(f"{spkt.serial}: {spkt.name}")
db.close()
