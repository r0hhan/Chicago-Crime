select * from crime;
select * from district;
select * from police_district;
select * from ward;

/*
S1MPLE
1.pie chart showing all the crimes in % of total crime count
2.decline in crime rate (chunks of 4yrs i.e. 5 bars in graph, 2001-2004, 2005-2008, 2009-2012, 2013-2016, 2017-present)
3.show plot of crimes on map? (last 2-3yrs prolle)

COMPLEX
1.% decline in total crime from 2001-2019 (plot top X declines)
2.% decline for every crime for given year set (plot top X declined)
3.incidents by hour of the day (2018-19)(narcotics, sexual assault, theft, robbery, etc)
4.% arrests grouped by police district to see which pd has highest %arrests, output top 5 (how many years, ask user/on us)
5.which wards got safer over the years per 10k population (group by ward). show top 5/list
6.%arrests of all crime w.r.t type of crime (all over)
*/
--COMPLEX1
SELECT ROUND(100*(x.c-y.c)/x.c,2) decline
FROM (SELECT COUNT(*) c
        FROM crime
        WHERE EXTRACT(YEAR FROM date_of_crime)=2002) x
    CROSS JOIN
    (SELECT COUNT(*) c
        FROM crime
        WHERE EXTRACT(YEAR FROM date_of_crime)=2005) y

--COMPLEX2
SELECT x.type_of_crime, ROUND(100*(x.c-y.c)/x.c,2) decline
FROM(SELECT type_of_crime, COUNT(*) c
        FROM crime
        WHERE EXTRACT(YEAR from date_of_crime)=2005
        GROUP BY type_of_crime) x,
    (SELECT type_of_crime, COUNT(*) c
        FROM crime
        WHERE EXTRACT(YEAR from date_of_crime)=2010
        GROUP BY type_of_crime) y
WHERE x.type_of_crime=y.type_of_crime AND x.c>y.c
ORDER BY decline DESC

--COMPLEX3
SELECT EXTRACT(HOUR FROM date_of_crime), COUNT(*) count_crime
FROM crime
WHERE EXTRACT(YEAR FROM date_of_crime) BETWEEN 2018 and 2019 AND type_of_crime = 'BATTERY'
GROUP BY EXTRACT(HOUR FROM date_of_crime)
ORDER BY EXTRACT(HOUR FROM date_of_crime)

--COMPLEX4
SELECT x.pdistrict_id, ROUND(100*y.c/x.c, 2) perc_arrest
FROM(SELECT pdistrict_id, COUNT(*) c
        FROM crime
        WHERE EXTRACT(YEAR FROM date_of_crime)=2018
        GROUP BY pdistrict_id) x,
    (SELECT pdistrict_id, COUNT(*) c
    FROM crime
    WHERE arrest='TRUE' AND EXTRACT(YEAR FROM date_of_crime)=2018
    GROUP BY pdistrict_id) y
WHERE x.pdistrict_id=y.pdistrict_id
ORDER BY perc_arrest DESC

--COMPLEX5
SELECT x.ward_id, ROUND(10000*(a/wpopulation_2000 - b/wpopulation_2010),2) safer
FROM(SELECT w.ward_id, w.wpopulation_2000, count(*) a
        FROM ward w, crime c where w.ward_id=c.ward_id AND EXTRACT(YEAR FROM date_of_crime)=2002
        GROUP BY (w.ward_id, w.wpopulation_2000)) x,
    (SELECT w.ward_id, w.wpopulation_2010, count(*) b
        FROM ward w, crime c where w.ward_id=c.ward_id AND EXTRACT(YEAR FROM date_of_crime)=2010
        GROUP BY (w.ward_id, w.wpopulation_2010)) y
WHERE x.ward_id=y.ward_id AND (a/wpopulation_2000 - b/wpopulation_2010)>0
ORDER BY safer DESC

--COMPLEX6
SELECT x.type_of_crime, crimes, arrests, ROUND(100*arrests/crimes,2) perc_arrests
FROM(SELECT type_of_crime, count(*) crimes
        FROM crime
        GROUP BY type_of_crime) x,
    (SELECT type_of_crime, count(*) arrests
        FROM crime
        WHERE arrest='TRUE'
        GROUP BY type_of_crime) y
WHERE x.type_of_crime=y.type_of_crime
ORDER BY perc_arrests DESC


--S1MPLE 1
SELECT type_of_crime,
    round(100*(COUNT(*) / SUM(COUNT(*)) OVER ()),2) perc
FROM crime
GROUP BY type_of_crime

--S1MPLE 2
SELECT COUNT(*)
FROM CRIME
WHERE EXTRACT(YEAR FROM date_of_crime) BETWEEN 2001 and 2005

SELECT COUNT(*)
FROM CRIME
WHERE EXTRACT(YEAR FROM date_of_crime) BETWEEN 2006 and 2010

SELECT COUNT(*)
FROM CRIME
WHERE EXTRACT(YEAR FROM date_of_crime) BETWEEN 2011 and 2015

SELECT COUNT(*)
FROM CRIME
WHERE EXTRACT(YEAR FROM date_of_crime) BETWEEN 2016 and 2019

SELECT COUNT(*)
FROM CRIME
WHERE EXTRACT(YEAR FROM date_of_crime) BETWEEN 2017 and 2019

--S1MPLE3 (heat map under construction *bonus query* xd)
