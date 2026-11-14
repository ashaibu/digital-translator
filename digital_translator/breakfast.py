"""Translate a breakfast request into explicit instructions."""


def create_breakfast_plan(available_equipment):
    """Create a breakfast plan after checking available equipment."""

    required_equipment = {"frying pan", "toaster", "kettle"}

    missing_equipment = required_equipment - set(available_equipment)

    if missing_equipment:
        return {
            "error": "Missing required equipment.",
            "missing_equipment": sorted(missing_equipment),
        }

    assumptions = [
        "Breakfast is for one person.",
        "The meal consists of two slices of toast, two fried eggs and tea.",
        "A kitchen, frying pan, toaster and kettle are available.",
    ]

    steps = [
        "Wash your hands and clean the preparation area.",
        "Gather the bread, eggs, tea, water and required equipment.",
        "Boil water in the kettle.",
        "Prepare the tea in a clean cup.",
        "Toast two slices of bread using the toaster.",
        "Heat a little cooking oil in the frying pan.",
        "Fry two eggs until properly cooked.",
        "Place the toast and fried eggs on a clean plate.",
        "Serve the tea alongside the breakfast.",
    ]

    return {
        "assumptions": assumptions,
        "steps": steps,
    }
