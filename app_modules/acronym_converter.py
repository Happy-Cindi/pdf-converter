def AcronymConverter(folder_name):
    words = folder_name.split()

    acronym = "".join(
        [word[0].upper() for word in words if word.lower() not in ["of", "and", "the"]]
    )

    return acronym
