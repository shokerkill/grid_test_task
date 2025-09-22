def validate_llm_sections(prompt: list[str]) -> bool:
    expected_sections = [
        "SECTION 0", "SECTION 1", "SECTION 2", "SECTION 3", "SECTION 4",
        "SECTION 5", "SECTION 6", "SECTION 7", "SECTION 8", "SECTION 9", "SECTION 10"
    ]
    joined = "\n".join(prompt)
    return all(section in joined for section in expected_sections)