import re

# Funciones para convertir palabras numéricas a números
def convert_word_to_number_spanish(word: int|str):
    try:
        return int(word)
    except ValueError:
        numbers = {
            "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
            "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
            "ochenta": 80, "noventa": 90, "media": 0.5, "medio": 0.5
        }
        return numbers.get(word.lower(), 0)
    
def convert_word_to_number_english(word: int|str):
    try:
        return int(word)
    except ValueError:
        numbers = {
            "zero": 0, "one": 1, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
            "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
            "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
            "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
            "eighty": 80, "ninety": 90, "half": 0.5
        }
        return numbers.get(word.lower(), 0)

def time_description_to_hours(time_description: str, language = "spanish"):
    if language == "spanish":
        return time_description_to_hours_spanish(time_description)
    elif language == "english":
        return time_description_to_hours_english(time_description)
        
    

def time_description_to_hours_spanish(time_description: str):
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace('y', ' ')
    time_description = time_description.replace(',', ' ')
    time_description = time_description.strip()

    if "media hora" == time_description:
        total_time_in_hours = 0.5
        return total_time_in_hours
        
    pattern = re.compile(r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?\s*(?:(\w+)\s*segundos?)?')
    match = pattern.match(time_description)

    if match:
        hours_word = match.group(1) or "0"
        minutes_word = match.group(2) or "0"
        seconds_word = match.group(3) or "0"

        hours = convert_word_to_number_spanish(hours_word)
        minutes = convert_word_to_number_spanish(minutes_word)
        seconds = convert_word_to_number_spanish(seconds_word)

        total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
    else:
        raise ValueError
    
    return total_time_in_hours

def time_description_to_hours_english(time_description: str):
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace('and', ' ')
    time_description = time_description.replace(',', ' ')
    time_description = time_description.strip()
    
    if "half hour" == time_description:
        total_time_in_hours = 0.5
        return total_time_in_hours

    pattern = re.compile(r'(?:(\w+)\s*hours?)?\s*(?:(\w+)\s*minutes?)?\s*(?:(\w+)\s*seconds?)?')
    match = pattern.match(time_description)

    if match:
        hours_word = match.group(1) or "0"
        minutes_word = match.group(2) or "0"
        seconds_word = match.group(3) or "0"

        hours = convert_word_to_number_english(hours_word)
        minutes = convert_word_to_number_english(minutes_word)
        seconds = convert_word_to_number_english(seconds_word)

        total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
    else:
        raise ValueError
    
    return total_time_in_hours

def time_description_to_hours(time_description: str, language = "spanish"):
    if "spanish" == language:
        try:
            total_time_in_hours = time_description_to_hours_spanish(time_description)
        except ValueError:
            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")
    elif "english" == language:
        try:
            total_time_in_hours = time_description_to_hours_english(time_description)
        except ValueError:
            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")
    return total_time_in_hours