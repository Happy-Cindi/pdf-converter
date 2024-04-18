import pdfplumber

from app_modules.course_object import CourseObject_2, FieldsObject, get_faculty

FACULTIES = [
    {"faculty": "Engineering", "page_num": 10},
    {"faculty": "Management Sciences", "page_num": 12},
    {"faculty": "Natural Sciences", "page_num": 14},
]


_start = 10
_end = 14


def MUT(pdf_path):
    courses = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            tables = page.extract_tables()

            faculty = get_faculty(page_number, FACULTIES)

            if page_number >= _start - 1 and page_number <= _end - 1:
                for table_num, table in enumerate(tables):
                    print(f"Page: {page_number + 1}")

                    for row_num, row in enumerate(table):
                        new_row = [
                            cell for cell in row if cell != "" and cell is not None
                        ]

                        if (
                            new_row != []
                            and new_row[0] != "Qualification"
                            and len(new_row) > 2
                        ):
                            fields = FieldsObject(
                                field=None,
                                requirements=new_row[0],
                                APS=None,
                                campus=None,
                            )

                            course = CourseObject_2(
                                degree=new_row[0],
                                faculty=faculty,
                                duration=new_row[3],
                                fields=fields,
                            )

                            if course:
                                courses.append(course)

    if courses:
        return courses
