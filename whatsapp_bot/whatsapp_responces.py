from email import message


def responces(input_message):
    message = input_message.lower()

    if message=='nice':
        return 'very nice'
    elif message=='hello':
        return 'hello there'
    elif message=='good morning':
        return 'good morning'
    elif message == 'good night':
        return 'goodnight '
    elif message=='Good night Everyone':
        return 'good night'
    elif message == 'Good morning  Everyone':
        return 'good morning'
    else :
        return 'cool!'