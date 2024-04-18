from typing import List, Optional


def ProcessCourse(
    degreeName: str,
    fields: List[str],
    requirements: List[str],
    duration: Optional[int] = None,
    APS: Optional[int] = None,
    campus: List[str] = [],
) -> dict:
    return {
        "degreeName": degreeName,
        "fields": fields,
        "requirements": requirements,
        "duration": duration,
        "APS": APS,
        "campus": campus,
    }
