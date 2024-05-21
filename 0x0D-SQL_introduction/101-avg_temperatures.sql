1 -- list average temperatures
2 -- Excute: cat 101-avg-temperatures.sql | mysql -hlocalhost -p hbn_0c_0
3 SELECT city AVG(value) AS avg_temp FROM temperature GROUP BY city ORDER avg_temp DESC;
