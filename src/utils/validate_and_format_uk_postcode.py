import re


def validate_and_format_uk_postcode(postcode: str):
    # using the regex pattern from https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Validation and https://stackoverflow.com/questions/164979/regex-for-matching-uk-postcodes
    pattern_wiki = r"^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"

    # ultimately, I would use the pattern below as it is not as strict as the one above, and it is more readable. Allowing for better maintainability and readability, and the option to update if to strict.
    pattern = r"^[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}$"

    valid = bool(re.match(pattern, postcode))
    if valid:
        formatted_postcode = postcode.upper()
        return formatted_postcode


valid_postcodes = ["SW1W 0NY", "PO16 7GZ", "GU16 7HF",
                   "L1 8JQ", "EC1A 1BB", "W1A 0AX", "M1 1AE"]

invalid_postcodes = ["SW1W 0NYY", "PO16 7GZZ", "GU16 7HFF",
                     "L1 8JQQ", "EC1A 1BBB", "W1A 0AXX", "M1 1AEE"]

mixed_postcodes = ["SW1W 0NY", "PO16 7GZ", "GU16 7HF",
                   "SW1W 0NYY", "PO16 7GZZ", "GU16 7HFF"]


for postcode in mixed_postcodes:
    if validate_and_format_uk_postcode(postcode):
        print(f"{postcode} is a valid UK postcode.")
    else:
        print(f"{postcode} is not a valid UK postcode.")
