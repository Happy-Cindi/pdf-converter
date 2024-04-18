import re

import pdfplumber

from app_modules.course_object import *

_start = 32
_end = 95


faculties = [
    {"faculty": "Art, Design and Architecture", "page_num": 30},
    {"faculty": "Business and Economics", "page_num": 38},
    {"faculty": "Education", "page_num": 52},
    {"faculty": "Engineering and the Built Environment", "page_num": 58},
    {"faculty": "Health Sciences", "page_num": 64},
    {"faculty": "Humanities", "page_num": 72},
    {"faculty": "Law", "page_num": 80},
    {"faculty": "Science", "page_num": 84},
]

pages_to_skip = [37, 48, 49, 55, 67, 78, 79]

# look into p: 55 and p: 67, they are content!


def UJ(pdf_path):
    courses = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            if (
                page_number >= _start - 1
                and page_number <= _end - 1
                and page_number + 1 not in pages_to_skip
            ):
                print()
                print(f"Page: {page_number + 1}")
                tables = page.extract_tables()

                new_table = []

                degree = None
                faculty = None
                duration = None
                fields = []

                for table_num, table in enumerate(tables, start=1):
                    faculty = get_faculty(page_number=page_number, faculties=faculties)

                    print(f"Table: {table_num + 1}")

                    for row_num, row in enumerate(table):
                        if row:
                            # Identify degree
                            for cell_num, cell in enumerate(row):
                                if cell is not None and "years" in cell:
                                    if len(cell) < 100:
                                        degree = re.sub(
                                            r"\(\d+ years?\)", "", cell
                                        ).strip()
                                        match = re.search(r"\((\d+) years?\)", cell)
                                        duration = (
                                            int(match.group(1))
                                            if match is not None
                                            else None
                                        )
                                elif cell is not None and "BEd Degree" in cell:
                                    if len(cell) < 100:
                                        degree = cell
                                        duration = 4

                            # Identify fields
                            cells_with_content = sum(
                                cell != "" and cell is not None for cell in row
                            )
                            cells_without_content = sum(
                                cell == "" or cell is None for cell in row
                            )
                            last_row_content = row[len(row) - 1]

                            if cells_with_content > cells_without_content:
                                first_row_length = len(row[0])  # type: ignore
                                row_length = len(row)

                                if first_row_length < 100 and row_length > 3:  # type: ignore
                                    # Course row
                                    if (
                                        row[0] != "EMMARGORP"
                                        and row[0] != "EEMMMMAARRGGOORRPP"
                                    ):
                                        new_table.append(row)
                                    else:
                                        # Header row
                                        ENGLISH = "English"

                                        # Check if it's a header row with the correct req format
                                        if (
                                            row[3] is not None
                                            and ENGLISH[::-1] in row[3]
                                        ):
                                            header_row = []
                                            # Revert the columns in the header row
                                            for (
                                                header_cell_num,
                                                header_cell,
                                            ) in enumerate(row):
                                                if (
                                                    header_cell
                                                    and header_cell is not None
                                                ):
                                                    decorated_cell = header_cell[::-1]
                                                    header_row.append(decorated_cell)

                                            if header_row:
                                                new_table.append(header_row)
                                        else:
                                            # Add a default header row if the format is not as expected
                                            new_table.append(
                                                [
                                                    "PROGRAMME",
                                                    "Qualiifcation\nCode",
                                                    "Minimum\nAPS",
                                                    "English",
                                                    "Mathematics",
                                                    "Mathematical\nLiteracy",
                                                    "Technical\nMathematics",
                                                    "CAREER",
                                                    "CAMPUS",
                                                ]
                                            )

                if new_table:
                    #     for row_num, row in enumerate(new_table):
                    #         if new_table[row_num][0] == "PROGRAMME":
                    #             # map start at the next row for fields
                    #             print(row)

                    #             for i in range(row_num + 1, len(new_table)):
                    #                 new_row = new_table[i]
                    #                 print(new_row)
                    #                 if new_row[0] == "PROGRAMME":
                    #                     print()
                    #                     break

                    for new_row_num, new_row in enumerate(new_table):
                        requirements = {}
                        for cell_num, cell in enumerate(new_row):
                            if (
                                new_row_num > 0
                                and cell_num >= 3
                                and cell_num < len(new_row) - 2
                            ):
                                requirements[new_table[0][cell_num]] = cell[::-1]

                        field = None
                        if requirements:
                            field = FieldsObject(
                                field=new_row[0],
                                requirements=requirements,
                                APS=new_row[2]
                                if len(new_row[2]) == 2
                                else new_row[2][::-1],
                                campus=new_row[len(new_row) - 1][::-1],
                            )

                        if field:
                            fields.append(field)
                    print()

                    if degree:
                        course = CourseObject_2(
                            degree=degree,
                            faculty=faculty,
                            duration=duration,
                            fields=fields,
                        )

                        if course:
                            print(course)
                            print()
                            courses.append(course)

        if courses:
            print(courses)
            return courses


# import re

# import pdfplumber

# from app_modules.course_object import *

# # _start = 40
# _start = 32
# _end = 95


# faculties = [
#     {"faculty": "Art, Design and Architecture", "page_num": 30},
#     {"faculty": "Business and Economics", "page_num": 38},
#     {"faculty": "Education", "page_num": 52},
#     {"faculty": "Engineering and the Built Environment", "page_num": 58},
#     {"faculty": "Health Sciences", "page_num": 64},
#     {"faculty": "Humanities", "page_num": 72},
#     {"faculty": "Law", "page_num": 80},
#     {"faculty": "Science", "page_num": 84},
# ]


# def UJ(pdf_path):
#     courses = []
#     fields = []
#     with pdfplumber.open(pdf_path) as pdf:
#         for page_number, page in enumerate(pdf.pages):
#             if page_number >= _start - 1 and page_number <= _end - 1:
#                 print()
#                 print(f"Page: {page_number + 1}")
#                 tables = page.extract_tables()

#                 faculty = get_faculty(page_number=page_number, faculties=faculties)

#                 for table_num, table in enumerate(tables, start=1):
#                     print(f"Table: {table_num + 1}")

#                     for row_num, row in enumerate(table):
#                         if row:
#                             # Identify degree
#                             for cell_num, cell in enumerate(row):
#                                 if cell is not None and "years" in cell:
#                                     if len(cell) < 100:
#                                         degree_row_num = row_num
#                                         degree = re.sub(
#                                             r"\(\d+ years?\)", "", cell
#                                         ).strip()
#                                         match = re.search(r"\((\d+) years?\)", cell)
#                                         duration = (
#                                             int(match.group(1))
#                                             if match is not None
#                                             else None
#                                         )

#                                         course = CourseObject_2(
#                                             degree=degree,
#                                             duration=duration,
#                                             faculty=faculty,
#                                             fields=fields,
#                                         )

#                                         if fields:
#                                             # print()
#                                             print(course)
#                                             courses.append(degree)

#                             # Identify fields
#                             cells_with_content = sum(
#                                 cell != "" and cell is not None for cell in row
#                             )
#                             cells_without_content = sum(
#                                 cell == "" or cell is None for cell in row
#                             )

#                             if (
#                                 cells_with_content > cells_without_content
#                                 and row[0] != "EMMARGORP"
#                                 and row[0] != "EEMMMMAARRGGOORRPP"
#                             ):
#                                 first_row_length = len(row[0])  # type: ignore
#                                 row_length = len(row)

#                                 if first_row_length < 100 and row_length > 3:
#                                     # requirements = get_requirements(
#                                     #     table=table,
#                                     #     table_num=table_num,
#                                     #     row=row,
#                                     #     row_start=2,
#                                     #     col_start=3,
#                                     # )

#                                     requirements = []

#                                     course_fields = FieldsObject(
#                                         field=row[0],
#                                         requirements=requirements,
#                                         APS=row[2],
#                                         campus=row[len(row) - 1],
#                                     )
#                                     fields.append(course_fields)

#                     print()
#         if courses and fields:
#             print(len(courses))
#             print(len(fields))


def UJ2(pdf_path):
    courses = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            if page_number >= _start - 1 and page_number <= _end - 1:
                print()
                print(f"Page: {page_number + 1}")
                tables = page.extract_tables()

                for table_num, table in enumerate(tables, start=1):
                    print(f"Table: {table_num + 1}")

                    new_row = []

                    for row_num, row in enumerate(table):
                        if row_num == 0:
                            for cell_num, cell in enumerate(row):
                                if (
                                    cell is not None
                                    and row_num == 0
                                    and row[len(row) - 1] == "SUPMAC"
                                ):
                                    new_row.append(cell[::-1])

                        if new_row and new_row[3] != "English":
                            print(new_row)
                            print(row)
