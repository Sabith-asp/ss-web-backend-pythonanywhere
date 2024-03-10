from django.contrib import admin

from .models import (
    MissionVision,
    HistoryofCollege,
    AboutCollege,
    SisterInstituition,
    FormerPrincipal,
    Accreditation,
    RecognitionandAward,
    StrategicPlan,
    RTI
)

admin.site.register(MissionVision)
admin.site.register(HistoryofCollege) 
admin.site.register(AboutCollege)
admin.site.register(SisterInstituition)
admin.site.register(FormerPrincipal)
admin.site.register(Accreditation)
admin.site.register(RecognitionandAward)
admin.site.register(StrategicPlan)
admin.site.register(RTI)