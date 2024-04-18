import time

from filters_module.wits import WITS

pdf_path = "WITS 2024 Guide.pdf"


def test():
    WITS(pdf_path)


start_time = time.time()
test()
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")
