#! /usr/bin/env python3
import psycopg2

# Format the three analysis questions as string, List SQL queries to run
preguntaUno = "1) The most popular 3 articles of all time (most accessed) are:"

queryUno = ("SELECT title, count(*) as num from articles "
            "JOIN log on path like CONCAT ('/article/', slug) GROUP by title "
            "ORDER by num desc limit 3")

preguntaDos = "2) The most popular article authors (w/most page views) are:"

queryDos = ("SELECT name, count(path) as num from authors "
            "JOIN articles on authors.id = author JOIN log "
            "ON path like CONCAT('/authors/', slug) "
            "GROUP by name ORDER by num desc")

preguntaTres = "3) These days had more than 1% of requests lead to errors:"

queryTres = ("SELECT date,(time) as date "
             "SUM(case when status != '200 OK' then 1 else 0 end) as errors "
             "COUNT(*) as totals from log "
             "GROUP by date(time) order by date(time) limit 5 "
             "SELECT date(time) as date "
             "100.0 * sum(case when status != '200 OK' then 1 else 0 end) "
             "COUNT(*) as perc from log group by date(time) "
             "ORDER by date(time) limit 5 "
             "SELECT date, round(perc::numeric, 2) as perc "
             "FROM (select date(time) as date "
             "100.0 * sum(case when status != '200 OK' then 1 else 0 end) "
             "COUNT (*) as perc from log "
             "GROUP by date(time)) as days_pct "
             "WHERE perc > 1 ORDER by date")


def makeTable(x):
    # Open newsdata.sql database and return result of query x
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(x)
    results = c.fetchall()
    db.close()
    return results


def sayResult(results, pregunta):
    # Displays formatted result of queries counting views
    print(pregunta)
    for result in results:
        print('\t' + result[0] + " with " + str(result[1]) + ' views')


def sayLastResult(results, pregunta):
    # Print formatted result of query with error as percentage
    print(pregunta)
    for result in results:
        print('\t' + str(result[0]) + " Error rate: " +
              str(round((result[1] * 100), 2)) + '%')


if __name__ == "__main__":
    sayResult(makeTable(queryUno), preguntaUno)
    sayResult(makeTable(queryDos), preguntaDos)
    sayLastResult(makeTable(queryTres), preguntaTres)
