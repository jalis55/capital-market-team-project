from django.contrib import admin
from capital_market.models import Applications, TeamMembers, Teams, Clients
# Register your models here.


class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    list_filter = ['position', 'team']


class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'application',
                    'primary_cont_person', 'secondary_cont_person']
    list_filter = ['application', 'primary_cont_person']


admin.site.register(Applications)
admin.site.register(Teams)
admin.site.register(TeamMembers, TeamMembersAdmin)
admin.site.register(Clients, ClientsAdmin)
