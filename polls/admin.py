from django.contrib import admin

# Register your models here.

from .models import Choice, Question

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None,  {'fields': ['question_text'] } ),
                 ('Date information', {'fields': ['pub_date'], 'classes': ['collapse'] } ),
                 ]
    
    #Esto le dice a Django: “los objetos Choice se editan en la página de admin de Question. Por defecto, proveer los campos para 3 choices”.
    inlines = [ChoiceInLine]
    
    #Añade  una tupla de los nombres de campo a mostrar, como columnas, en la página de listado:
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    
    #Esto agrega un “Filtro” en la barra lateral que permite filtrar el listado por el campo
    list_filter = ['pub_date']
    
    #Esto agrega un campo de búsqueda al tope del listado. Cuando alguien ingresa términos de búsqueda, Django va a buscar sobre el campo 
    #question_text. Se pueden usar tantos campos como uno quiera
    search_fields = ['question_text'] 
    

admin.site.register(Question, QuestionAdmin)
