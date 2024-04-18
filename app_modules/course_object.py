def CourseObject(degreeName, fields, requirements, APS, duration, campus):
    return {
        "degreeName": degreeName,
        "fields": fields,
        "requirements": requirements,
        "APS": APS,
        "duration": duration,
        "campus": campus,
    }


def FieldsObject(field, requirements, APS, campus):
    return {
        "field": field,
        "requirements": requirements,
        "APS": APS,
        "campus": campus,
    }


def CourseObject_2(degree, faculty, duration, fields):
    return {
        "degree": degree,
        "faculty": faculty,
        "duration": duration,
        "fields": fields,
    }


def get_faculty(page_number, faculties):
    closest_faculty = None
    closest_distance = float("inf")

    for faculty_data in faculties:
        distance = abs(faculty_data["page_num"] - page_number)

        if distance < closest_distance or (
            distance == closest_distance and faculty_data["page_num"] >= page_number
        ):
            closest_faculty = faculty_data["faculty"]
            closest_distance = distance

    return closest_faculty if closest_faculty is not None else "Unknown Faculty"


def get_faculty_2(page_number, table_number, faculties):
    closest_faculty = None
    closest_distance = float("inf")

    for faculty_data in faculties:
        page_distance = abs(faculty_data["page_num"] - page_number)
        table_distance = abs(faculty_data["table_num"] - table_number)

        # Consider both page number and table number for distance calculation
        distance = page_distance + table_distance

        if distance < closest_distance or (
            distance == closest_distance and faculty_data["page_num"] >= page_number
        ):
            closest_faculty = faculty_data["faculty"]
            closest_distance = distance

    return closest_faculty if closest_faculty is not None else "Unknown Faculty"


def get_requirements(table, table_num, row, row_start, col_start):
    requirements = {}
    for col_num, cell in enumerate(row[row_start : len(row) - 2], start=col_start):
        if table[table_num][col_num] != "" and table[table_num][col_num] is not None:
            subject = table[0][col_num]
            value = cell
            requirements[subject] = value
            table[0]

    if requirements:
        return requirements
    else:
        return None  # or an empty dictionary, depending on your use case


# def get_requirements(table, table_num, row, row_start, col_start):
#     requirements = {}
#     for col_num, cell in enumerate(row[row_start : len(row) - 2], start=col_start):
#         if table[table_num][col_num] != "" and table[table_num][col_num] is not None:
#             subject = table[0][col_num]
#             value = cell
#             requirements[subject] = value

#     if requirements:
#         return requirements
#     else:
#         return None  # or an empty dictionary, depending on your use case


# def get_requirements(table, row, row_start, col_start, col_end):
#     requirements = {}
#     for col_num, cell in enumerate(row[row_start:], start=col_start, end=col_end):
#         if table[1][col_num] != "" and table[1][col_num] is not None:
#             requirements = [table[0][col_num]] = cell
#             requirements[table[0][col_num]] = cell

#     if requirements:
#         return requirements


# def CourseObject_2(degree, duration):
#     return [
#         {
#             "degree": degree,
#             "faculty": "Education",
#             "duration": duration,
#             "fields": [
#                 {
#                     "field": "ARCHITECTURE",
#                     "requirements": {"sub_1": 5, "sub_2": 7, "sub_3": 4},
#                     "APS": 12,
#                     "campus": "APK",
#                 }
#             ],
#         }
#     ]
