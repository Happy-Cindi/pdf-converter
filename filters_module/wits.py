import re
from dataclasses import fields

import pdfplumber

from app_modules.course_object import CourseObject_2, FieldsObject, get_faculty

faculties = [
    {"faculty": "Commerce, Law and Management", "page_num": 16},
    {"faculty": "Engineering and the Built Environment", "page_num": 18},
    {"faculty": "Health Sciences", "page_num": 20},
    {"faculty": "Humanities", "page_num": 22},
    {"faculty": "Science", "page_num": 24},
]

pages_with_tables = [16]
# pages_with_tables = [16, 18, 20, 22, 24]


def WITS(pdf_path):
    courses = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            if page_number + 1 in pages_with_tables:
                print(f"Page: {page_number + 1}")
                tables = page.extract_tables()

                faculty = get_faculty(page_number, faculties)

                for table_num, table in enumerate(tables, start=1):
                    print(f"Table: {table_num + 1}")
                    for row_num, row in enumerate(table):
                        cells_with_content = sum(
                            cell != "" and cell is not None for cell in row
                        )

                        # Header and courses
                        if cells_with_content > 1:
                            if row[0] is not None and not "Programmes" in row[0]:
                                degree_col_num = int
                                duration_col_num = int

                                if page_number == 16:
                                    degree_col_num = 0
                                    duration_col_num = 1

                                    course = get_course(
                                        table, row, faculty, degree_col_num
                                    )
                                elif page_number == 18:
                                    break
                                elif page_number == 20:
                                    break
                                elif page_number == 22:
                                    break
                                elif page_number == 24:
                                    break

                                    if course:
                                        courses.append(course)

        if courses:
            for course_num, course in enumerate(courses):
                print(course)
                print()


def get_course(table, row, faculty, degree_col_num):
    requirements = {}
    for cell_num, cell in enumerate(row):
        if cell_num >= 3 and cell_num < len(row) - 1:
            requirements[table[0][cell_num]] = (
                cell if cell is not None and len(cell) < 200 else None
            )

    field = FieldsObject(
        field=None,
        requirements=requirements,
        APS=row[2],
        campus=None,
    )

    if field:
        course = CourseObject_2(
            degree=row[degree_col_num],
            faculty=faculty,
            duration=row[1],
            fields=field,
        )
