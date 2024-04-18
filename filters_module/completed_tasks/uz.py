import pdfplumber

from app_modules.course_object import CourseObject

_start = 11
# _start = 40
_end = 14


def UZ(pdf_path):
    courses = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            if page_number >= _start - 1 and page_number <= _end - 1:
                print()
                print(f"Page: {page_number + 1}")
                tables = page.extract_tables()

                for table_num, table in enumerate(tables, start=1):
                    column_content_table = []
                    new_final_table = []

                    for row_num, row in enumerate(table):
                        cells_with_content = sum(
                            cell != "" and cell is not None for cell in row
                        )
                        cells_without_content = sum(
                            cell == "" or cell is None for cell in row
                        )

                        if cells_with_content > cells_without_content and row_num > 1:
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
                            course = CourseObject(
                                degreeName=row[0],
                                fields=None,
                                requirements={row[3]},
                                APS=row[2],
                                duration=f"{row[1]} years",
                                campus=None,
                            )

                            courses.append(course)

        if courses:
            return courses
