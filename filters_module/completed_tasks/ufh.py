import pdfplumber

from app_modules.course_object import CourseObject_2, FieldsObject, get_faculty_2

faculties = [
    {"faculty": "Education", "page_num": 1, "table_num": 1},
    {"faculty": "Management and Commerce", "page_num": 1, "table_num": 2},
    {"faculty": "Law", "page_num": 1, "table_num": 3},
    {"faculty": "Health Science", "page_num": 1, "table_num": 4},
    {"faculty": "Science and Agriculture", "page_num": 2, "table_num": 1},
    {"faculty": "Social Science and Humanities", "page_num": 2, "table_num": 2},
    {"faculty": "Science and Agriculture", "page_num": 2, "table_num": 3},
    {"faculty": "Social Science and Humanities", "page_num": 2, "table_num": 4},
]


def extract_requirements(table, start_row):
    requirements = {}
    for i in range(start_row + 1, min(start_row + 5, len(table))):
        if table[i][3] and table[i][4]:
            requirements[table[i][3]] = table[i][4]
        else:
            break
    return requirements


def UFH(pdf_path):
    courses = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            print(f"Page: {page_number + 1}")

            tables = page.extract_tables()

            for table_num, table in enumerate(tables, start=1):
                print(f"Table: {table_num }")
                faculty = get_faculty_2(page_number, table_num, faculties)

                row_num = 0
                while row_num < len(table):
                    row = table[row_num]

                    if "Programme\nName" not in row[0] if row[0] is not None else None:
                        requirements = extract_requirements(table, row_num)

                        fields = FieldsObject(
                            field=None,
                            requirements=requirements,
                            APS=row[5],
                            campus=None,
                        )

                        if fields:
                            course = CourseObject_2(
                                degree=row[0],
                                faculty=faculty,
                                duration=None,
                                fields=fields,
                            )

                            courses.append(course)

                        # Skip the rows that are already processed
                        row_num += len(requirements) + 1
                    else:
                        row_num += 1

    if courses:
        print(len(courses))
