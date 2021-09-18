# Import ListView module
from django.views.generic import ListView
# Import Employee module
from .models import Employee
# Import Q module
from django.db.models import Q

# Define class for filtering data
class SearchEmployee(ListView):
    # Define model
	model = Employee
    # Define template
	template_name = 'search.html'
	
	# Filter 1
	# Apply filtering with multiple fields
	#queryset = Employee.objects.filter(department='HR', email='ali@gmail.com')
	
	# Filter 2
	# Apply filtering by using Q objects
	queryset = Employee.objects.filter( Q(post='Manager') | Q(department='Sales'))
	
	# Filter 3
	# Apply filtering by using Q objects
	#queryset = Employee.objects.filter(department='HR').filter(name='Mehrab Hossain')
	