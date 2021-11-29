from django.contrib import admin
from .models import Applications, Lsme, Hsme
from import_export.admin import ImportExportModelAdmin


#@admin.register(Applications, Lsme, Hsme)
#class ViewAdmin(ImportExportModelAdmin):
#    pass

class ViewAdminApplications(ImportExportModelAdmin):
    list_display = ['id',
                    'L_id',
                    'Application_date',
                    'H_id']

admin.site.register(Applications, ViewAdminApplications)

class ViewAdminLsme(ImportExportModelAdmin):
    list_display = ['id',
                    'L_id',
                    'Company',
                    'Sector',
                    'Location',
                    'No_of_employees_being_laid_off',
                    'Years']

admin.site.register(Lsme, ViewAdminLsme)

class ViewAdminHsme(ImportExportModelAdmin):
    list_display = ['id',
                    'H_id',
                    'Company',
                    'Sector',
                    'Location',
                    'No_of_employees_required',
                    'Years',
                    'Start_date',
                    'End_date']

admin.site.register(Hsme, ViewAdminHsme)
