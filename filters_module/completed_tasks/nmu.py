import pdfplumber

from app_modules.course_object import CourseObject_2, FieldsObject, get_faculty

faculties = [
    {"faculty": "Business and Economic Sciences", "page_num": 18},
    {"faculty": "Education", "page_num": 42},
    {"faculty": "Engineering and the Built Environment", "page_num": 50},
    {"faculty": "Health Sciences", "page_num": 72},
    {"faculty": "Humanities", "page_num": 84},
    {"faculty": "Law", "page_num": 98},
    {"faculty": "Science", "page_num": 104},
]

_start = 22
_end = 132


def NMU(pdf_path):
    courses = []
    with pdfplumber.open(pdf_path) as pdf:
        new_table = []
        for page_number, page in enumerate(pdf.pages):
            if page_number >= _start - 1 and page_number <= _end - 1:
                tables = page.extract_tables()
                print(f"Page: {page_number + 1}")

                for table_num, table in enumerate(tables):
                    for row_num, row in enumerate(table):
                        cells_with_content = sum(
                            cell != "" and cell is not None for cell in row
                        )

                        # Courses and fields rows
                        if row_num > 1 and cells_with_content >= 1:
                            if cells_with_content < 2:
                                degree_row = row
                                new_table.append(degree_row)
                            else:
                                field_row = row
                                new_table.append(field_row)

                if new_table:
                    courses = []
                    duration = None
                    degree = None
                    fields = []
                    faculty = get_faculty(page_number=page_number, faculties=faculties)

                    for row_num, row in enumerate(new_table):
                        cells_with_content = sum(
                            cell != "" and cell is not None for cell in row
                        )

                        if cells_with_content <= 1:
                            # Degree row
                            if degree and faculty:
                                # If a degree row is encountered while a course is already in progress, finalize and add the course
                                course = CourseObject_2(
                                    degree=degree,
                                    faculty=faculty,
                                    duration=duration,
                                    fields=fields,
                                )
                                courses.append(course)
                                fields = []  # Reset the fields list for the new course

                            degree = row[0]
                        else:
                            # Field row
                            field = FieldsObject(
                                field=row[0],
                                requirements=row[6],
                                APS={
                                    "AS for Math": row[3],
                                    "AS for Tech Math": row[4],
                                    "AS for Math Lit": row[5],
                                },
                                campus=None,
                            )
                            duration = row[2]

                            if field:
                                fields.append(field)

                    # After the loop, add the last course if it exists
                    if degree:
                        course = CourseObject_2(
                            degree=degree,
                            faculty=faculty,
                            duration=duration,
                            fields=fields,
                        )

                        courses.append(course)

    if courses:
        return courses
