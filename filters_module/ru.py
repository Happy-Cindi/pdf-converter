import pdfplumber

from app_modules.course_object import CourseObject

_start = 22
_end = 132


def RU(pdf_path):
    courses = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            print(f"Page: {page_number + 1}")
            # print()

            for table_num, table in enumerate(page.extract_tables(), start=1):
                print(f"Table: {table_num}")

                for row_num, row in enumerate(table):
                    if row[0] == "Degrees":
                        for i in range(row_num, len(table)):
                            new_row = table[i]

                            print(new_row)
                print()
