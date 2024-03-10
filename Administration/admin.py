from django.contrib import admin

from .models import (
   ManagementCouncil,
   DirectorBoard,
   Chairman,
   Manager,
   MCQA,
   MCQAmember,
   Principal,
)

admin.site.register(ManagementCouncil)
admin.site.register(DirectorBoard) 
admin.site.register(Chairman)
admin.site.register(Manager)
admin.site.register(MCQA)
admin.site.register(MCQAmember)
admin.site.register(Principal)