import sqlite3
from gists_database.importer import import_gists_to_database
from gists_database.search   import search_gists
from gists_database.models   import Gist


def setup_database(db_path="gists.db"):
 
    conn = sqlite3.connect(db_path)
    with open("schema.sql", "r") as f:
        conn.executescript(f.read())  # ينفّذ كل الأوامر في schema.sql
    return conn

#______________________________________________________________

def demo_import_and_search(username):

    db = setup_database()

    #  import Gists  
    print(f"Importing gists for user '{username}'...")
    import_gists_to_database(db, username)


    print("\nAll gists:")
    all_gists = search_gists(db)
    for gist in all_gists:
        print(" ", gist)

    if all_gists:
        some_id = all_gists[0].id
        print(f"\nSearching for Gist with id='{some_id}':")
        filtered = search_gists(db, github_id=some_id)
        for gist in filtered:
            print(" ", gist)

if __name__ == "__main__":
    # غيّر هذا الاسم لحساب GitHub اللي تحب تجربه
    demo_import_and_search("gvanrossum")
