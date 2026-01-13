from django.contrib import admin
from .models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,EQuestions6,\
EQuestions7,EQuestions8,EQuestions9,EQuestions10,EQuestions11,EQuestions12,EQuestions13,EQuestions14,DocumentsPrepared,PreRating,ReferalResponse,LendingRequirements


@admin.register(EQuestions)
class EQuestionsAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

@admin.register(EQuestions1)
class EQuestionsOneAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

@admin.register(EQuestions2)
class EQuestionsTwoAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

@admin.register(EQuestions3)
class EQuestionsThreeAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

@admin.register(EQuestions4)
class EQuestionsFourAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

@admin.register(EQuestions5)
class EQuestionsFiveAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

@admin.register(EQuestions6)
class EQuestionsSixAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

@admin.register(EQuestions7)
class EQuestionsSevenAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

@admin.register(EQuestions8)
class EQuestionsEightAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

@admin.register(DocumentsPrepared)
class DocumentsPreparedAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

@admin.register(PreRating)
class pre_ratingAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

@admin.register(ReferalResponse)
class referal_responseAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

@admin.register(LendingRequirements)
class lending_requirementsAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)