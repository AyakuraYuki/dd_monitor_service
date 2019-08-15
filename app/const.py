import locale


def __os_locale_language():
    locale_info, locale_code = locale.getdefaultlocale()
    return str(locale_info[:str(locale_info).rindex('_')])


language = __os_locale_language()


def current_lang():
    if language == 'zh':
        return '中文'
    elif language == 'en':
        return 'English'
    elif language == 'ja':
        return '日本語'
    else:
        return language
