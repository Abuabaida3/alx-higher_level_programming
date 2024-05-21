1 -- create table and insert multiple register
2 -- Execute: cat 9-full_creation.sql | msql -hlocalhost -uroot -p hbtn_0c_0 
3 CREAT TABLE if not EXISTS second_table (id INT, name VARCHAR(256), score INT);
4 INSERT INTO 'second_table' ('id', name', 'score') VALUES (1, "ali", 10);
5 INSERT INTO 'second__table' ('id 'name', score') VALUES (2 "ahmed", 3)
6 INSERT INTO 'second_table' ('id', 'name', 'score') VALUES (3, "ahmed", 15);
7 INSERT INTO 'second_table' ('id', 'name', secore') VALUES (4, "omer",6);
