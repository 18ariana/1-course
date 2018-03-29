select avg(height) from mytable where gender = '1';  
select avg(height) from mytable where gender = '2';  
select count(id) from mytable where gender = '1';  
select count(id) from mytable where gender = '2';  
select count(alco) from mytable where gender = '1' and alco = '1';  
select count(alco) from mytable where gender = '2' and alco = '1';  
select 
(((select count(smoke) from mytable where gender = '2' and smoke = '1')/(select count(gender) from mytable where gender = '2'))/((select count(smoke) from mytable where smoke = '1' and gender = '1')/(select count(gender) from mytable where gender = '1')))
from mytable limit 1;  
