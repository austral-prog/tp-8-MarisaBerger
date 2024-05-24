def get_coordinate(record):
    return record[1]

    


def convert_coordinate(coordinate):
    number = coordinate[0]
    letter = coordinate[-1]
    return (number, letter)

   


def create_record(azara_record, rui_record):
    azacor = get_coordinate(azara_record)
    ruicor = get_coordinate(rui_record)
    azatupla = convert_coordinate(azacor)
    if azatupla == ruicor:
        return azara_record + rui_record
    else:
        return "not a match"

