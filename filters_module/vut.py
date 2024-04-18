import pdfplumber

from app_modules.course_object import CourseObject

_start = 1
_end = 2


def VUT(pdf_path):
    courses = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            if page_number >= _start - 1 and page_number <= _end - 1:
                print()
                print(f"Page: {page_number + 1}")
                tables = page.extract_tables()

                for table_num, table in enumerate(tables, start=1):
                    print(f"Table: {table_num + 1}")
                    for row_num, row in enumerate(table):
                        if any(
                            isinstance(cell, str) and "Subjects" in cell
                            for cell in row
                            if cell is not None
                        ):
                            print(row)
                            print()
