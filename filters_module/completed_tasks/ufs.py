import pdfplumber

from app_modules.course_object import CourseObject

_start = 20
_end = 41


def UFS(pdf_path):
    courses = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            if page_number >= _start - 1 and page_number <= _end - 1:
                print()
                print(f"Page: {page_number + 1}")
                tables = page.extract_tables()

                for table_num, table in enumerate(tables, start=1):
                    print(f"Table: {table_num}")

                    column_content_table = []
                    new_final_table = []

                    for row_num, row in enumerate(table):
                        cells_with_content = sum(
                            cell != "" and cell is not None for cell in row
                        )
                        cells_without_content = sum(
                            cell == "" or cell is None for cell in row
                        )

                        if (
                            cells_with_content > cells_without_content
                            and len(row[0]) > 3  # type: ignore
                        ):
                            column_content_table.append(row)

                    column_content = list(map(list, zip(*column_content_table)))

                    for new_row_num, new_row in enumerate(column_content):
                        new_row_without_content = all(
                            cell is None or cell == "" for cell in new_row
                        )

                        if (
                            not new_row_without_content
                            and new_row[0] != "Programme Director"
                            and new_row[0] != "Academic\nProgramme Code"
                        ):
                            new_final_table.append(new_row)

                    if new_final_table:
                        courses_table = list(map(list, zip(*new_final_table)))

                        for row_num, row in enumerate(courses_table):
                            last_cell = len(row) - 1
                            requirements = {}

                            for col_num, cell in enumerate(row[3:], start=3):
                                if (
                                    courses_table[1][col_num] != ""
                                    and courses_table[1][col_num] is not None
                                ):
                                    requirements[courses_table[0][col_num]] = cell

                            length_of_APS = (
                                len(row[2])
                                if len(row) > 2 and row[2] is not None
                                else 11
                            )

                            if row_num > 0 and length_of_APS <= 10:
                                campus_index = len(row) - 1

                                course = CourseObject(
                                    degreeName=row[0],
                                    fields=None,
                                    requirements=requirements,
                                    APS=row[2] if len(row[2]) == 2 else row[2][:2],
                                    duration=None,
                                    campus=(
                                        str(row[campus_index]).split()[-1]
                                        if campus_index < len(courses_table[0])
                                        and courses_table[0][campus_index]
                                        in ["Camp", "Campus"]
                                        else None
                                    ),
                                )

                                if length_of_APS <= 10:
                                    courses.append(course)

        if courses:
            for course_num, course in enumerate(courses):
                print(course)
                print()

            print(len(courses))
            return courses
