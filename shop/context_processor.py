from .models import Category

def category_processor(request):
    """
    Retrieve all categories from database
    Return categories in the context dictionary
    """
    categories = Category.objects.all()
    
    return {
        'categories' : categories
    }