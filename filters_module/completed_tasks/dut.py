import time

import pdfplumber

from app_modules.course_object import CourseObject


def DUT(pdf_path):
    courses = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            # if page_number == 11 - 1:
            if page_number >= 11 - 1:
                tables = page.extract_tables()
                text = page.extract_text()

                print()
                print(f"Page: {page_number + 1}")

                course = []

                lines = text.split("\n")
                for line_number, line in enumerate(lines):
                    if line:
                        # Identify degree position
                        if line.startswith("Diploma") or line.startswith("Bachelor"):
                            course.append(line)

                        if line.startswith("Location"):
                            course.append(line)

                        if line.startswith("Duration"):
                            course.append(lines[line_number + 1])

                for table_num, table in enumerate(tables):
                    requirements = []
                    if table:
                        for row_num, row in enumerate(table):
                            if row:
                                if any(
                                    identifier in row
                                    for identifier in requirements_identifier
                                ):
                                    for i in range((row_num + 1), len(table) - 1):
                                        next_row = table[
                                            i
                                        ]  # remove "", None and " " in each cell
                                        formatted_row = [f"{next_row[0]} {next_row[1]}"]
                                        requirements.extend(formatted_row)

                    if requirements:
                        course.append(requirements)

                # if requirements:
                #     print(requirements)

                # return

                # course.append(row)

                # return
                # print(f"Table: {table_num}")

                if course:
                    if course:
                        print(course)
                        print()

    if courses:
        print(len(courses))
        print()


requirements_identifier = [
    "COMPULSORY SUBJECTS",
    "NSC RATING COD",
    "Compulsory Subjects",
    "NSC Rating Code",
]
# import time

# import pdfplumber

# from app_modules.course_object import CourseObject


# def DUT(pdf_path):
#     courses = []
#     with pdfplumber.open(pdf_path) as pdf:
#         for page_number, page in enumerate(pdf.pages):
#             # if page_number == 11 - 1:
#             if page_number >= 11 - 1:
#                 tables = page.extract_tables()
#                 text = page.extract_text()

#                 print(f"Page: {page_number + 1}")

#                 lines = text.split("\n")
#                 for line_number, line in enumerate(lines):
#                     if line:
#                         # Identify degree position
#                         degreeName = (
#                             line
#                             if line.startswith("Diploma") or line.startswith("Bachelor")
#                             else None
#                         )
#                         fields = None
#                         requirements = None
#                         APS = None
#                         duration = None
#                         campus = line if line.startswith("Location") else None

#                         if degreeName:
#                             course = CourseObject(
#                                 degreeName,
#                                 fields,
#                                 requirements,
#                                 APS,
#                                 duration,
#                                 campus,
#                             )

#                             courses.append(course)

#                             print(course)
#                             print()

#     if courses:
#         print(len(courses))
#         print()


# import pdfplumber

# from app_modules.course_object import CourseObject


# def DUT(pdf_path):
#     courses = []
#     with pdfplumber.open(pdf_path) as pdf:
#         for page_number, page in enumerate(pdf.pages):
#             # if page_number == 11 - 1:
#             if page_number >= 11 - 1:
#                 tables = page.extract_tables()
#                 text = page.extract_text()

#                 print(f"Page: {page_number + 1}")

#                 lines = text.split("\n")
#                 for line_number, line in enumerate(lines):
#                     if line:
#                         # Identify degree position
#                         if line.startswith("Diploma") or line.startswith("Bachelor"):
#                             degreeName = line
#                             fields = None
#                             requirements = None
#                             APS = None
#                             duration = None
#                             campus = None

#                             course = CourseObject(
#                                 degreeName, fields, requirements, APS, duration, campus
#                             )

#                             courses.append(course)

#                             print(course)
#                             print()
#                             break

#     if courses:
#         print(len(courses))
#         print()


# import pdfplumber


# def DUT(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         for page_number, page in enumerate(pdf.pages):
#             # if page_number == 11 - 1:
#             if page_number >= 11 - 1:
#                 tables = page.extract_tables()
#                 text = page.extract_text()

#                 print(f"Page: {page_number + 1}")

#                 degreeName = None
#                 fields = None
#                 requirements = None
#                 APS = None
#                 duration = None
#                 campus = None

#                 lines = text.split("\n")
#                 for line_number, line in enumerate(lines):
#                     # print(f"Line {line_number + 1}: {line}")

#                     # Identify degree position

#                     first_letter = line[0]

#                     # if line and first_letter == "N" and ":" in line:
#                     # if line and line.startswith("NQF Level") and ":" in line: # and the starting length > 8

#                     nqf = "NQF Level"

#                     if line and line.startswith(nqf):
#                         # count the length of the found starting with nqf before ':' == len(nqf)
#                         length_before_colon = len(line.split(":")[0].strip())

#                         if length_before_colon == len(nqf):
#                             for i in range(line_number, 0, -1):
#                                 if ":" not in lines[i]:
#                                     # degreeName = line
#                                     degreeName = lines[i]
#                                     print(f"Degree: {degreeName}")
#                                     print()
#                                     break

#     print()
