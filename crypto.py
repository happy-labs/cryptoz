import hashlib
import MySQLdb
import os


if __name__ == "__main__":
    """
    Main method here,
        read input file from command line
        hash it
        save it on db
    """
    #read db host via env variable
    DB_HOST = os.getenv("DB_HOST", "10.2.2.1")

    # connect to db
    db = MySQLdb.connect(host=DB_HOST,
                         user="root",
                         passwd="root",
                         db="cryptoz")
    cursor = db.cursor()

    # create database and tables/if not exists
    sql_hide_warning = "SET sql_notes = 0"
    sql_create_table = "CREATE TABLE IF NOT EXISTS hashes(\
                            msg varchar(100),\
                            hash varchar(100)\
                        )"
    cursor.execute(sql_hide_warning)
    cursor.execute(sql_create_table)

    while True:
        print('--------------------------------------------------------------')
        msg = raw_input("Enter Message : ").strip()
        print('--------------------------------------------------------------')

        # first generate hash
        print("MD5 hashing: %s" % msg)
        hash = hashlib.md5(msg.encode()).hexdigest()
        print("MD5 hash: %s" % hash)

        # save hash in db
        print("MD5 saving: %s" % hash)
        sql = "INSERT INTO hashes VALUES(%s, %s)"
        cursor.execute(sql, (msg, hash))
        db.commit()
