import psycopg2

DATABASE_NAME = "news"


def get_the_most_viewed_articles(limit=3):
    query = """
    select articles.title,count(log.id)  as views
    from 
      articles ,log
    where 
        log.path = ('/article/' || articles.slug)
    group by 
        articles.title
    order by 
        views desc 
     limit 
        %i

    """ % (limit)

    return get(query)


def get_most_popular_authors():
    return get("""
    select authors.name,count(log.id) as views
    from 
        articles,authors,log
    where
        log.path = ('/article/' || articles.slug)
        and authors.id = articles.author
    group by 
        authors.id
    order by 
        views desc 
    
    """)


def get_the_day_that_have_the_most_of_errors():
    return get("""
        select
            to_char(errors_by_day.date,'Month,DD, YYYY') as date,
            to_char(((errors_by_day.count::decimal
                    /requests_by_day.count::decimal)*100)
                    ,'9.99')
                    || '%' as percentage
        from
            (select date(time),count(*) from log
                        group by date(time)) as requests_by_day,
            (select date(time),count(*) from log where status != '200 OK'
                        group by date(time)) as errors_by_day
        where
            requests_by_day.date = errors_by_day.date
            and ((errors_by_day.count::decimal
                    /requests_by_day.count::decimal)*100) > 1;
                    
        """)


def get(query):
    db = psycopg2.connect(database=DATABASE_NAME)
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()
