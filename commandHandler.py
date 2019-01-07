import report_tool


def run():
    """ Start the reporting tool """
    print("")
    answer_question_1()

    print("\n")
    answer_question_2()

    print("\n")
    answer_question_3()


def answer_question_1():
    print("Q1. What are the most popular three articles of all time?\n")
    rows = report_tool.get_the_most_viewed_articles()
    for row in rows:
        print("%s - %d views" % (row[0], row[1]))


def answer_question_2():
    print("Q2. Who are the most popular article authors of all time?\n")
    rows = report_tool.get_most_popular_authors()
    for row in rows:
        print("%s - %d views" % (row[0], row[1]))


def answer_question_3():
    print("Q3. On which days did more than 1% of requests lead to errors?\n")
    rows = report_tool.get_the_day_that_have_the_most_of_errors()
    for row in rows:
        print("%s - %s errors" % (row[0], row[1]))


run()
