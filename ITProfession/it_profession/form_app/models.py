from django.db import models
from django.contrib.auth.models import User


class SurveyResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forms")

    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField("Имя", max_length=50)

    # 1. Мотивация и интересы
    motivation = models.CharField("Что вам ближе?", max_length=100)
    ideal_day = models.CharField("Ваш идеальный рабочий день...", max_length=100)

    # 2. Когнитивные предпочтения
    cognitive_strength = models.CharField("Что легче дается?", max_length=100)
    self_type = models.CharField("Ты больше:", max_length=100)

    # 3. Личностные особенности
    personality_trait = models.CharField("Что вам ближе по темпераменту?", max_length=100)

    # 4. Рабочий стиль
    work_environment = models.CharField("Комфортная обстановка:", max_length=100)
    reaction_to_difficulty = models.CharField("Как вы реагируете на сложность?", max_length=100)

    # 5. Творчество / логика
    creative_or_logical = models.CharField("Что вам приятнее?", max_length=100)

    # 6. Опыт (мультивыбор)
    experience = models.JSONField("Опыт", default=list, blank=True)

    # 7. Ценности (мультивыбор)
    values = models.JSONField("Ценности", default=list, blank=True)

    # LLM результат
    llm_result = models.TextField("Рекомендованное направление", blank=True)

    def __str__(self):
        return self.name
