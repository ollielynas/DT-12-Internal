
# removes everything that is not a number
def clean_int_input(text):
    try:
        return float(text)
    except:...
    text = text.lower()
    text = ''.join(ch for ch in text if ch.isdigit())
    return text



def text_to_int(text):
    text = text.lower()
    try:
        return float(text)
    except:
        ...

    text = ''.join(ch for ch in text if ch.isdigit() or ch == ".")
    try:
        if int(text) > 9999:
            return("number too large")
        return float(text)
    except:
        return " ? "

# input either a string or an int and get an int (default to 10)
def guaranty_int(text):
    if type(text) == str:
        text = text.lower()
    elif type(text) == int:
        return text

    try:
        return float(''.join(c for c in text if (c.isdigit() or c == '.')))
    except:
        return 10
