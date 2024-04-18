import re

import pdfplumber

from app_modules.course_object import CourseObject

_start = 13
# _start = 31
_end = 31


def UV(pdf_path):
    courses = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            if page_number >= _start - 1 and page_number <= _end - 1:
                print()
                print(f"Page: {page_number + 1}")
                tables = page.extract_tables()

                for table_num, table in enumerate(tables, start=1):
                    print(f"Table: {table_num +1}")

                    column_content_table = []
                    new_final_table = []

                    for row_num, row in enumerate(table):
                        row_length = len(row) - 1

                        if (
                            row
                            and row_num > 0
                            and row_length >= 3
                            and row[0] != ""
                            and row[0] != None
                        ):
                            column_content_table.append(row)

                    column_content = list(map(list, zip(*column_content_table)))

                    for new_row_num, new_row in enumerate(column_content):
                        new_row_without_content = all(
                            cell is None or cell == "" for cell in new_row
                        )

                        if not new_row_without_content:
                            new_final_table.append(new_row)

                    if new_final_table:
                        courses_table = list(map(list, zip(*new_final_table)))

                        for row_num, row in enumerate(courses_table):
                            cells_without_content = sum(
                                cell == "" or cell is None for cell in row
                            )
                            if not cells_without_content:
                                requirements = row[2]
                                match = re.search(r"(\d+)", requirements)
                                aps_value = match.group(1) if match else None

                                course = CourseObject(
                                    degreeName=row[0],
                                    fields=None,
                                    requirements={requirements.replace("\n", " ")},
                                    APS=aps_value,
                                    duration=row[3].replace("\n", " "),
                                    campus=None,
                                )

                                courses.append(course)

        if courses:
            return courses
