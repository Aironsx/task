import datetime


def year(request):
    year_now = datetime.date.today().year
    return {'year': year_now}
