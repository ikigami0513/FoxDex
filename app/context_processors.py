def theme_cookie(request):
    theme_value = request.COOKIES.get('theme')
    print(theme_value)
    return {
        'theme_value': theme_value
    }