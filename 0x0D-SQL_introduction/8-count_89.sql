1 -- count rows with id 89
2 -- Execute cat 8-count_89.sql | mysqul -hlocalhost -uroot -p hbtn_0c_0 | tail -1
SELECT COUNT(*) FROM first_table WHERE id=89;
