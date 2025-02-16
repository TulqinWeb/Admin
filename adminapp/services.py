from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_faculties():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_faculty""")
        faculties = dictfetchall(cursor)
        return faculties


def get_kafedras():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_kafedra""")
        kafedras = dictfetchall(cursor)
        return kafedras


def get_subjects():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_subject""")
        subjects = dictfetchall(cursor)
        return subjects


def get_teachers():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_teacher""")
        teachers = dictfetchall(cursor)
        return teachers


def get_groups():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_group""")
        groups = dictfetchall(cursor)
        return groups


def get_students():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_student""")
        students = dictfetchall(cursor)
        return students
