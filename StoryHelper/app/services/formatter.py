def format_tokenarray(token_array, separator=' '):
    return separator.join(token_array).replace(' , ', ', ') \
                                 .replace(' .', '.') \
                                 .replace(' ; ', '; ') \
                                 .replace(' - ', '-') \
                                 .replace(' : ', ': ')