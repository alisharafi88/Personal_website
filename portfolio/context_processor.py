from .models import Portfolio


def portfolio(request):
    portfolios = Portfolio.objects.all()
    return {'portfolios': portfolios}
