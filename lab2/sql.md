select avg(height) from mytable where gender = '1';  
select avg(height) from mytable where gender = '2';  
select count(id) from mytable where gender = '1';  
select count(id) from mytable where gender = '2';  
select count(alco) from mytable where gender = '1' and alco = '1';  
select count(alco) from mytable where gender = '2' and alco = '1';  
select 
(((select count(smoke) from mytable where gender = '2' and smoke = '1')/(select count(gender) from mytable where gender = '2'))/((select count(smoke) from mytable where smoke = '1' and gender = '1')/(select count(gender) from mytable where gender = '1')))
from mytable limit 1;  


select(select avg(cardio) from mytable where gender = '2' and 
age >= 60*365 and age <= 64*365 and smoke = '1' and ap_hi >= 160 and ap_hi < 180 and cholesterol = '1') / (select avg(cardio) from mytable where gender = '2' and age >= 21900 and
age <= 64*365 and smoke = '1' and ap_hi < 120 and cholesterol = '1') from mytable limit 1;  


select (select avg(weight) from mytable where gender = '1' )/(select  avg(pow(height/100,2)) from mytable where gender = '1' ) from mytable limit 1 ;  
select (select avg(weight) from mytable where gender = '2' )/(select  avg(pow(height/100,2)) from mytable where gender = '2' ) from mytable  limit 1 ;  
select (select avg(weight) from mytable where cardio = '1' )/(select  avg(pow(height/100,2)) from mytable where cardio = '1' ) from mytable  limit 1 ;  
select (select avg(weight) from mytable where cardio = '0' )/(select  avg(pow(height/100,2)) from mytable where cardio = '0' ) from mytable  limit 1 ;  
select (select avg(weight) from mytable where cardio = '0' and gender = '2' and alco = '0' )/(select  avg(pow(height/100,2)) from mytable where cardio = '0' and gender = '2' and alco = '0' ) from mytable  limit 1 ;  
select (select avg(weight) from mytable where cardio = '0' and gender = '1' and alco = '0' )/(select  avg(pow(height/100,2)) from mytable where cardio = '0' and gender = '1' and alco = '0' ) from mytable  limit 1 ;    








