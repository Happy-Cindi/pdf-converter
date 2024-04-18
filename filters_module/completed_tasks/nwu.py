import pdfplumber
import re

from app_modules.filter_row import FilterRow
from app_modules.process_course import ProcessCourse

page_start = 6
page_end = 14


def NWU(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # tables = pdf.pages[page_number - 1].extract_tables()

        courses = []

        for page_num in range(page_start, page_end):
            tables = pdf.pages[page_num - 1].extract_tables()

            for table_number, table in enumerate(tables):
                tableDataStructure = [
                    "Degree",
                    "Field",
                    "Subjects / Requirements",
                    "APS",
                    "Campus",
                ]

                if table:
                    table_length = len(table)
                    cols_num = len(table[0]) if table and len(table) > 0 else 0

                    for row_num, row in enumerate(table):
                        courseRow = []
                        course_row_2 = []

                        reversed_courseRow = courseRow.reverse()
                        reversed_course_row = course_row_2.reverse()
                        if row:
                            # Check for APS col num as an identifier
                            aps_col = int

                            for i in range(0, cols_num):
                                cell_content = row[i]

                                # Check if the cell_content is an integer
                                if str(cell_content).isdigit():
                                    aps_as_row_identifier = (cell_content)
                                    aps_col = i

                                    # Now we go up and check for content
                                    for h in range(aps_col + 1, len(row)):
                                        cell = row[h]

                                        if cell is not None and cell != "":
                                            courseRow.append(cell)
                                            break

                                    # Count down from aps_col to 0
                                    for j in range(aps_col, -1, -1):
                                        cell = row[j]

                                        if cell is not None and cell != "":
                                            courseRow.append(cell)

                                        elif j in (0, 1) and (
                                            cell is None or cell == ""
                                        ):
                                            courseRow.append(cell)

                                    # ...........................................................
                                    # Creating courses array finally
                                    if courseRow and len(courseRow) == 4:
                                        courses.append(reversed_courseRow)
                                    else:
                                        row_length = len(courseRow)
                                        stop_at = int

                                        if row_length == 6:
                                            stop_at = 4
                                        else:
                                            stop_at = 5

                                        for z in range(0, stop_at, +1):
                                            cell = courseRow[z]
                                            course_row_2.append(cell)

                                        if course_row_2:
                                            courses.append(course_row_2[::-1])

        return courses
