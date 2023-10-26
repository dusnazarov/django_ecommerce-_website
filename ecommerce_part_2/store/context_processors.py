from .models import Category


def categorie(request):
    return {'categories': Category.objects.all() }
        
   