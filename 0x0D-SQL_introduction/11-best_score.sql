1 -- list the score greather than or equle to 10
2 -- Execute: cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
3 SELECT secore, name FROM second_table WHERE secore >= 10 ORDER BY score DESC
