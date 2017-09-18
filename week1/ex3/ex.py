import sqlite3

with sqlite3.connect("database.sqlite") as conn:
  c = conn.cursor()
  c.execute("""
            SELECT * 
            FROM hall_of_fame INNER JOIN 
                 player_college ON hall_of_fame.player_id = player_college.player_id
                 ;""")


  #c.execute("""SELECT * FROM(SELECT * FROM player) a WHERE hall_of_fame.inducted == 'Y'
  #              INNER JOIN hall_of_fame b 
  #              ON a.player_id = b.player_id
  #              INNER JOIN (SELECT college_id, player_id FROM player_college) c
  #              ON a.player_id == c.player_id
  #              WHERE b.inducted == 'Y'
  #              GROUP BY college_id;""")
  rows = c.fetchall()
  
  bycollege = dict()
  #print(rows[0])
  for row in rows:
    if(row[6] == 'Y'):
      college = row[10]
      bycollege[college] = bycollege.get(college, 0) + 1
    #print(row[30])
  print(bycollege)
  #print(rows)
  #print(len(rows[0]))

