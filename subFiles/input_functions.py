import pyperclip


def clean_int_input(text):
    text = text.lower()
    text = ''.join(ch for ch in text if ch.isdigit())
    return text

def text_to_int(text):
    text = text.lower()
    text = ''.join(ch for ch in text if ch.isdigit())
    try:
        return int(text)
    except:
        return " ? "

def guaranty_int(text):
    if type(text) == str:
        text = text.lower()
    elif type(text) == int:
        return text
    text = ''.join(ch for ch in text if ch.isdigit())
    try:
        return int(text)
    except:
        return 10