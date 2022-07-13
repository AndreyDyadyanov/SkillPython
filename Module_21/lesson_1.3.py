def seach_value(site, key):
    if key in site:
        return site[key]

    for sub_site in site.values():
        if isinstance(sub_site, dict):
            result = seach_value(sub_site, key)
            if result:
                break
    else:
        result = None

    return result



site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

user_key = input('Искомый ключ: ')

result = seach_value(site, user_key)
if result:
    print('Значание: {}'.format(result))
else:
    print('Нет такого ключа в структуре сайта нет.')


