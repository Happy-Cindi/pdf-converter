import json
import os


def generate_json_file(
    pdf_file_directory: str,
    coursesArray,
    pdf_file_name,
    prospectus_folder_name,
):
    # test_folder = r"D:\test"
    json_file_path = os.path.join(
        r"D:\Prospectus\Nelson Mandela University", f"{prospectus_folder_name}.json"
    )

    # Convert all courses to JSON and write to a file
    with open(json_file_path, "w") as json_file:
        json.dump(coursesArray, json_file, indent=4)

    print(f"JSON file created at: {json_file_path}")


# import json
# import os


# def generate_json_file(
#     prospectus_pdf_acronym: str,
#     pdf_file_directory: str,
#     coursesArray: list,
# ):
#     json_file_path = os.path.join(pdf_file_directory, f"{prospectus_pdf_acronym}.json")

#     print(json_file_path)

#     # Convert all courses to JSON and write to a file
#     with open(f"{json_file_path}", "w") as json_file:
#         json.dump(coursesArray, json_file, indent=4)
