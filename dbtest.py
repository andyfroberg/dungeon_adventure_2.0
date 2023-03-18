from da_database import DungeonAdventureDatabase

def main():
    db = DungeonAdventureDatabase('dcstats.db')
    db.create_db_with_dc_stats()
    rows = db.select_all_dcstats(db.conn)

    for row in rows:
        print(str(row))



if __name__ == "__main__":
    main()