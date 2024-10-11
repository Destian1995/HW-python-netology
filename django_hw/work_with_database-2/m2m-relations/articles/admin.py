from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        # Используем список для подсчета основных разделов
        main_sections = [form.cleaned_data.get('is_main') for form in self.forms if form.cleaned_data.get('is_main') is not None]
        if sum(main_sections) == 0:
            raise ValidationError('Укажите основной раздел')
        elif sum(main_sections) > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
