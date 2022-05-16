import sqlite3
conn = sqlite3.connect('test6.db')

def database_entry():
   
    conn.executescript("""DROP TABLE IF EXISTS Movies;
                       CREATE TABLE Movies
             (
             NAME               TEXT   NOT NULL,
             ACTOR              TEXT   NOT NULL,
             ACTRESS            TEXT   NOT NULL,
             DIRECTOR           TEXT   NOT NULL,
             YEAR_OF_RELEASE    INT    NOT NULL
             );
                       """);
    conn.execute("INSERT INTO Movies (NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
          VALUES ('MOVIE1','ACTOR1','ACTRESS2','DIRECTOR1',2020)");
    conn.execute("INSERT INTO Movies (NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
          VALUES ('MOVIE2','ACTOR2','ACTRESS4','DIRECTOR2',2021)");
    conn.execute("INSERT INTO Movies (NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
          VALUES ('MOVIE3','ACTOR3','ACTRESS1','DIRECTOR2',2022)");
    conn.execute("INSERT INTO Movies (NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
          VALUES ('MOVIE4','ACTOR2','ACTRESS1','DIRECTOR3',2021)");
    conn.execute("INSERT INTO Movies (NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
          VALUES ('MOVIE5','ACTOR2','ACTRESS2','DIRECTOR4',2022)");
    conn.execute("INSERT INTO Movies (NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
          VALUES ('MOIVE6','ACTOR1','ACTRESS2','DIRECTOR2',2022)");
    conn.execute("INSERT INTO Movies (NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
          VALUES ('MOVIE7','ACTOR3','ACTRESS3','DIRECTOR2',2021)");
    conn.execute("INSERT INTO Movies (NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
          VALUES ('MOVIE8','ACTOR3','ACTRESS2','DIRECTOR5',2019)");
    conn.execute("INSERT INTO Movies (NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
          VALUES ('MOVIE9','ACTOR1','ACTRESS4','DIRECTOR1',2018)");
    conn.execute("INSERT INTO Movies (NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
          VALUES ('MOVIE10','ACTOR2','ACTRESS3','DIRECTOR6',2017)");

database_entry();


cursor=conn.execute("PRAGMA table_info(Movies)")
cursor.execute("SELECT * FROM Movies")
print("Printing Movies Table")
rows=cursor.fetchall()
for row in rows:
    s = "    {:^9}     {:^9} {:^9} {:^9} {:4}".format(row[0],row[1],row[2],row[3],row[4])
    print(s)
    
y=input("Enter actor name")

cursor.execute("Select * from Movies where ACTOR=(?)",[y,])
rows=cursor.fetchall()
for row in rows:
    s = "    {:^9}     {:^9} {:^9} {:^9} {:4}".format(row[0],row[1],row[2],row[3],row[4])
    print(s)

conn.close()