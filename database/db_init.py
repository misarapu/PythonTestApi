import mysql.connector
import json

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sJ5L8&6LK0vHM{}8",
    database="artifydb"
)

sectors = [
    ("Manufacturing", 1, 0, 0, 0),
    ("Construction materials", 1, 1, 0, 0),
    ("Electronics and Optics", 1, 2, 0, 0),
    ("Food and Beverage", 1, 3, 0, 0),
    ("Bakery & confectionery products", 1, 3, 1, 0),
    ("Beverages", 1, 3, 2, 0),
    ("Fish & fish products", 1, 3, 3, 0),
    ("Meat & meat products", 1, 3, 4, 0),
    ("Milk & dairy products", 1, 3, 5, 0),
    ("Other", 1, 3, 6, 0),
    ("Sweets & snack food", 1, 3, 7, 0),
    ("Furniture", 1, 4, 1, 0),
    ("Bathroom/sauna", 1, 4, 2, 0),
    ("Bedroom", 1, 4, 3, 0),
    ("Children's room", 1, 4, 4, 0),
    ("Kitchen", 1, 4, 5, 0),
    ("Living room", 1, 4, 6, 0),
    ("Office", 1, 4, 7, 0),
    ("Other (Furniture)", 1, 4, 8, 0),
    ("Outdoor", 1, 4, 9, 0),
    ("Project furniture", 1, 4, 10, 0),
    ("Machinery", 1, 5, 0, 0),
    ("Machinery components", 1, 5, 1, 0),
    ("Machinery equipment/tools", 1, 5, 2, 0),
    ("Manufacture of machinery", 1, 5, 4, 0),
    ("Maritime", 1, 5, 5, 0),
    ("Aluminium and steel workboats", 1, 5, 5, 1),
    ("Boat/Yacht building", 1, 5, 5, 2),
    ("Ship repair and conversion", 1, 5, 5, 3),
    ("Metal structures", 1, 5, 6, 0),
    ("Other", 1, 5, 7, 0),
    ("Repair and maintenance service", 1, 5, 8, 0),
    ("Metalworking", 1, 6, 0, 0),
    ("Construction of metal structures", 1, 6, 1, 0),
    ("Houses and buildings", 1, 6, 2, 0),
    ("Metal products", 1, 6, 3, 0),
    ("Metal works", 1, 6, 4, 0),
    ("CNC-machining", 1, 6, 4, 1),
    ("Forgings, Fasteners", 1, 6, 4, 2),
    ("Gas, Plasma, Laser cutting", 1, 6, 4, 3),
    ("MIG, TIG, Aluminum welding", 1, 6, 4, 4),
    ("Plastic and Rubber", 1, 7, 0, 0),
    ("Packaging", 1, 7, 1, 0),
    ("Plastic goods", 1, 7, 2, 0),
    ("Plastic processing technology", 1, 7, 3, 0),
    ("Blowing", 1, 7, 3, 1),
    ("Moulding", 1, 7, 3, 2),
    ("Plastics welding and processing", 1, 7, 3, 3),
    ("Plastic profiles", 1, 7, 4, 0),
    ("Printing", 1, 8, 0, 0),
    ("Advertising", 1, 8, 1, 0),
    ("Book/Periodicals printing", 1, 8, 2, 0),
    ("Labelling and packaging printing", 1, 8, 3, 0),
    ("Textile and Clothing", 1, 9, 0, 0),
    ("Clothing", 1, 9, 1, 0),
    ("Textile", 1, 9, 2, 0),
    ("Wood", 1, 10, 0, 0),
    ("Other (Wood)", 1, 10, 1, 0),
    ("Wooden building materials", 1, 10, 2, 0),
    ("Wooden houses", 1, 10, 3, 0),
    ("Other", 2, 0, 0, 0),
    ("Creative industries", 2, 1, 0, 0),
    ("Energy technology", 2, 2, 0, 0),
    ("Environment", 2, 3, 0, 0),
    ("Service", 3, 0, 0, 0),
    ("Business services", 3, 1, 0, 0),
    ("Engineering", 3, 2, 0, 0),
    ("Information Technology and Telecommunications", 3, 3, 0, 0),
    ("Data processing, Web portals, E-marketing", 3, 3, 1, 0),
    ("Programming, Consultancy", 3, 3, 2, 0),
    ("Software, Hardware", 3, 3, 3, 0),
    ("Telecommunications", 3, 3, 4, 0),
    ("Tourism", 3, 4, 0, 0),
    ("Translation services", 3, 5, 0, 0),
    ("Transport and Logistics", 3, 6, 0, 0),
    ("Air", 3, 6, 1, 0),
    ("Rail", 3, 6, 2, 0),
    ("Road", 3, 6, 3, 0),
    ("Water", 3, 6, 4, 0)
]

my_cursor = db.cursor()
# my_cursor.execute("DROP DATABASE IF EXISTS artifydb")
# my_cursor.execute("CREATE DATABASE artifydb")

my_cursor.execute("""CREATE TABLE logins (id INT NOT NULL AUTO_INCREMENT, user_name VARCHAR(255) not null, session_id VARCHAR(255) not null
                      , PRIMARY KEY(id), UNIQUE(user_name, session_id))""")

my_cursor.execute("""CREATE TABLE sectors (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255), group_1 SMALLINT, group_2 SMALLINT, group_3 SMALLINT, group_4 SMALLINT
                      , PRIMARY KEY(id), UNIQUE(group_1, group_2, group_3, group_4))""")

my_cursor.execute("""CREATE TABLE users_in_sectors (login_id INT NOT NULL, sector_id INT NOT NULL
                      , PRIMARY KEY(login_id, sector_id)
                      , CONSTRAINT fk_sector_user FOREIGN KEY (login_id) REFERENCES logins(id)
                      , CONSTRAINT fk_user_sector FOREIGN KEY (sector_id) REFERENCES sectors(id))""")

my_cursor.executemany("INSERT INTO sectors (name, group_1, group_2, group_3, group_4) VALUES (%s, %s, %s, %s, %s)", sectors)
db.commit()