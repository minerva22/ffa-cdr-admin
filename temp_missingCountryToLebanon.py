from cdradmin.models import SuperidToLoanLiability, Country
lebanon = Country.objects.get(name__iexact='lebanon')
for x in SuperidToLoanLiability.objects.filter(country_of_utilization__isnull=True):
  x.country_of_utilization = lebanon
  x.save()

