from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at', 'update_at')  # Columns to display in the admin list view
    search_fields = ('first_name', 'last_name', 'email')  # Searchable fields
    list_filter = ('created_at', 'update_at')  # Filters in the right sidebar
    prepopulated_fields = {'slug': ('first_name',)}  # Auto-populate slug field based on first_name

admin.site.register(Author, AuthorAdmin)
