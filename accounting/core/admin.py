from core.models import ExpenseType, Expense, Revenue, RevenueType
from django.contrib import admin

admin.site.register(RevenueType)
admin.site.register(Revenue)
admin.site.register(ExpenseType)
admin.site.register(Expense)
