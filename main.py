import os
import time

from app_modules.acronym_converter import AcronymConverter
from app_modules.csv_generator import *
from app_modules.filter_row import *
from app_modules.json_generator import *
from app_modules.process_course import *
from filters_module.completed_tasks.nmu import NMU
from filters_module.completed_tasks.uj import UJ


def main(dir):
    prospectus_folders = os.scandir(dir)

    for prospectus_folder in prospectus_folders:
        # Check if the prospectus_folder is a directory
        if prospectus_folder.is_dir():
            prospectus_folder_name = prospectus_folder.name
            prospectus_folder_directory = prospectus_folder.path  #
            prospectus_folder_acronym = AcronymConverter(prospectus_folder_name)
            pdf_files = os.scandir(prospectus_folder.path)

            print("Prospectus: " + prospectus_folder_name)

            # Process the contents of the pdf files
            for pdf_file in pdf_files:
                if pdf_file.is_file():
                    pdf_file_name = pdf_file.name
                    pdf_file_directory = pdf_file.path

                    print(f"File: {pdf_file_name}")

                    # Extract tables or text,
                    # pdf_plumnber_table_extractor(pdf_file_directory)

                    # Apply general filters

                    # Apply filters based on pdf format

                    # Inject course into an object

                    # Generate json file
                    # fakeCourses = []

                    pdf_path_ = "NMU.pdf"
                    if pdf_file_name == "2024-Full-Undergraduate-Guide (1).pdf":
                        courses = NMU(pdf_path_)
                        generated_json = generate_json_file(
                            pdf_file_directory,
                            courses,
                            pdf_file_name,
                            prospectus_folder_directory,
                        )


if __name__ == "__main__":
    path = r"D:\Prospectus"
    start_time = time.time()
    main(path)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Elapsed time: {elapsed_time} seconds")
