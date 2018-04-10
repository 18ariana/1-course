import psycopg2
import psycopg2.extras
from pprint import pprint as pp
from tabulate import tabulate

conn = psycopg2.connect("host=localhost port=5432 dbname=odscourse user=postgres password=secret")
cursor = conn.cursor()  # cursor_factory=psycopg2.extras.DictCursor)


def fetch_all(cursor):
    colnames = [desc[0] for desc in cursor.description]
    records = cursor.fetchall()
    return [{colname: value for colname, value in zip(colnames, record)} for record in records]


"""
cursor.execute("")
records = cursor.fetchall()
print(records)
"""

""" 1.Сколько мужчин и женщин представлено в этом наборе данных? """
cursor.execute(
   """
   SELECT gender, AVG(height), COUNT(gender) AS ammount
   FROM mlboot
   GROUP BY gender
   """
   )
print('Задание 1')
print(tabulate(fetch_all(cursor), "keys", "psql"))


""" 2. Кто в среднем реже указывает, что употребляет алкоголь – мужчины или женщины? """

cursor.execute(
    """
    select count(alco) from mytable where gender = '1' and alco = '1';
    select count(alco) from mytable where gender = '2' and alco = '1';  
    """
)

print('Задание 2')
print(tabulate(fetch_all(cursor), "keys", "psql"))


""" 3.Во сколько раз (округленно, round) процент курящих среди мужчин больше, чем процент
    курящих среди женщин (по крайней мере, по этим анкетным данным)? """

cursor.execute(
    """
    select (((select count(smoke) from mytable where gender = '2' and smoke = '1')/(select count(gender) from mytable where
    gender = '2'))/((select count(smoke) from mytable where smoke = '1' and gender = '1')/(select count(gender) from mytable where
    gender = '1'))) from mytable limit 1;
    """
 )
 print('Задание 3')
print(tabulate(fetch_all(cursor), "keys", "psql"))


""" 4.В чём здесь измеряется возраст? На сколько месяцев (примерно) отличаются медианные значения
    возраста курящих и некурящих? """
    
cursor.execute(
    """
    SELECT DISTINCT ABS(
        (SELECT median(age) / 30 FROM mlboot WHERE smoke='1') - \
        (SELECT median(age) / 30 FROM mlboot WHERE smoke='0')
    )::int AS diff
    FROM mlboot
    """
) 
print('Задание 4')
print(tabulate(fetch_all(cursor), "keys", "psql"))



"""

 
    
    














    
