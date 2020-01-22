import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

def mysql_set_location():
        try:
                db = MySQLdb.connect("localhost","root","PASSWORD","snipeit")
                cur = db.cursor()
                cur.execute("UPDATE users SET location_id = CASE" " WHEN employee_num = 'Head Office' THEN 7" " WHEN employee_num = 'Teresa' THEN 1" " WHEN employee_num = 'Batangas' THEN 2" " WHEN employee_num = 'Bulacan' THEN 3" " WHEN employee_num = 'Norzagaray' THEN 4" " WHEN employee_num = 'Iligan' THEN 5" " WHEN employee_num = 'Danao' THEN 6" " END;")
                db.commit()
                db.close()
                print(">>Location update succesful.")
        except Exception as err:
                print("MySQL error!")
                print(err)


def mysql_set_company():
	try:
		db = MySQLdb.connect("localhost","root","PASSWORD","snipeit")
		cur = db.cursor()
		cur.execute("UPDATE users SET company_id = CASE" " WHEN location_id = 7 THEN 1" " WHEN location_id = 1 THEN 2" " WHEN location_id = 2 THEN 3" " WHEN location_id = 3 THEN 4" " WHEN location_id = 4 THEN 5" " WHEN location_id = 6 THEN 6" " WHEN location_id = 5 THEN 7" " WHEN location_id = 8 THEN 9" " END;")
		db.commit()
		db.close()
		print(">>Company update succesful.")
	except Exception as err:
		print("MySQL error!")
		print(err)


def main():
	mysql_set_location()
	mysql_set_company()


if __name__ == '__main__':
        main()
