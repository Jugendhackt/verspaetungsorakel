import os

import verspaetungsorakel.model as model
from verspaetungsorakel.fetch.utils import sent_db_api_request

DB_API_ID = os.getenv("DB_API_ID")
DB_API_KEY = os.getenv("DB_API_KEY")


def main():
    url = "https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/station/*"
    try:
        result = sent_db_api_request(url)
    except ConnectionError as e:
        print(e)
        return

    stations = result["stations"]["station"]
    # db_stations = []

    model.db.connect()
        # print(station)
        model.Station.get_or_create(name=station["@name"], number=station["@eva"], ds100=station["@ds100"])
        # db_stations.append({
        #     "name": station["@name"],
        #     "number": station["@eva"],
        #     "ds100": station["@ds100"]})

    # with model.db.atomic():
    #     # TODO: Don't ignore conflicts, update row instead
    #     model.Station.insert_many(db_stations).on_conflict_ignore().execute()
    model.db.close()


if __name__ == "__main__":
    main()
