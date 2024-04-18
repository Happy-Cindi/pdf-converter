import pdfplumber

from app_modules.course_object import CourseObject

page_number = 15 - 1


def CPUT(pdf_path):
    courses = []

    subjects = {
        "english": "English",
        "mathPure": "Mathematics",
        "mathLit": "Mathematical Literacy",
        "mathTech": "Mathematics Technical",
        "accounting": "Accounting",
        "lifeSciences": "Life Sciences",
        "physicalSciences": "Physical Sciences",
        "techScience": "Technical Science",
    }

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            # tables = page.extract_tables()
            tables = page.extract_tables()

            print(f"Page: {page_number}")
            for table_num, table in enumerate(tables):
                for row_num, row in enumerate(table):
                    if row:
                        if row_num > 1 and page_number == 7 - 1:  # Row with course
                            degreeName = row[0]
                            fields = None
                            requirements = {
                                subjects["english"]: row[4],
                                subjects["mathPure"]: row[5],
                                subjects["mathTech"]: row[6],
                                subjects["mathLit"]: row[7],
                                subjects["lifeSciences"]: row[8],
                                subjects["physicalSciences"]: row[9],
                            }
                            APS = {"ECP": row[1], "Mainstream": row[2]}
                            duration = None
                            campus = None

                            course = CourseObject(
                                degreeName, fields, requirements, APS, duration, campus
                            )

                            courses.append(course)

                        if row_num > 0 and (page_number == 9 - 1):
                            degreeName = row[1]
                            fields = row[0]
                            requirements = {
                                subjects["english"]: row[4],
                                subjects["mathPure"]: row[5],
                                subjects["mathLit"]: row[6],
                                subjects["accounting"]: row[7],
                            }
                            APS = row[2]
                            duration = None
                            campus = None

                            course = CourseObject(
                                degreeName, fields, requirements, APS, duration, campus
                            )

                            courses.append(course)

                        if row_num > 0 and (page_number == 10 - 1) and row_num != 4:
                            if row_num == 1:
                                degreeName = (
                                    "BACHELOR IN EDUCATION: FOUNDATION PHASE TEACHING"
                                )
                            elif row_num == 2:
                                degreeName = (
                                    "BACHELOR IN EDUCATION: INTERMEDIATE PHASE TEACHING"
                                )
                            elif row_num == 3:
                                degreeName = "BACHELOR IN EDUCATION: SENIOR PHASE and FURTHER EDUCATION & TRAINING (FET) TEACHING"
                            else:
                                degreeName = None  # You may want to handle other cases

                            fields = None
                            requirements = row[1]
                            APS = row[0]
                            duration = None
                            campus = None

                            course = CourseObject(
                                degreeName, fields, requirements, APS, duration, campus
                            )

                            courses.append(course)

                        if row_num > 1 and page_number == 11 - 1:
                            degreeName = row[0]
                            fields = None
                            requirements = {
                                subjects["english"]: row[3],
                                subjects["mathPure"]: row[4],
                                subjects["mathTech"]: row[5],
                                subjects["mathLit"]: row[6],
                                subjects["lifeSciences"]: row[7],
                                subjects["physicalSciences"]: row[8],
                            }
                            APS = row[1]
                            duration = None
                            campus = None

                            course = CourseObject(
                                degreeName, fields, requirements, APS, duration, campus
                            )

                            courses.append(course)

                        if row_num > 0 and page_number == 13 - 1:
                            degreeName = row[0]
                            fields = None
                            requirements = {
                                subjects["english"]: row[2],
                                subjects["mathPure"]: row[4],
                                subjects["mathLit"]: row[5],
                                subjects["mathTech"]: row[6],
                            }
                            APS = row[1]
                            duration = None
                            campus = None

                            course = CourseObject(
                                degreeName, fields, requirements, APS, duration, campus
                            )

                            courses.append(course)

                        if row_num > 3 and page_number == 15 - 1:
                            degreeName = row[0]
                            fields = None
                            requirements = {
                                subjects["english"]: row[4],
                                subjects["mathPure"]: row[5],
                                subjects["mathTech"]: row[6],
                                subjects["mathLit"]: row[7],
                                subjects["physicalSciences"]: row[8],
                                subjects["techScience"]: row[9],
                            }
                            APS = row[1]
                            duration = None
                            campus = None

                            course = CourseObject(
                                degreeName, fields, requirements, APS, duration, campus
                            )

                            courses.append(course)

    if courses:
        return courses
