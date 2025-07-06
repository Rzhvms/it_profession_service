from django import forms
from .models import SurveyResponse


class SurveyForm(forms.ModelForm):
    EXPERIENCE_CHOICES = [
        ("html_css", "HTML/CSS"),
        ("python_js", "Python / JavaScript / другой язык"),
        ("figma", "Figma / Photoshop"),
        ("excel", "Excel / анализ данных"),
        ("devops", "Git / CI/CD / Docker"),
        ("no_exp", "Не пробовал, но интересно начать"),
    ]

    VALUE_CHOICES = [
        ("creativity", "Креативность"),
        ("stability", "Стабильность"),
        ("income", "Высокий доход"),
        ("growth", "Быстрое развитие"),
        ("remote", "Удалёнка / гибкость"),
        ("teamwork", "Работа в команде"),
        ("tech_focus", "Возможность погружаться в технологии"),
        ("leadership", "Руководящие перспективы"),
    ]

    experience = forms.MultipleChoiceField(
        choices=EXPERIENCE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="С чем вы ранее работали?"
    )

    values = forms.MultipleChoiceField(
        choices=VALUE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Что для вас важно при выборе профессии?"
    )

    class Meta:
        model = SurveyResponse
        exclude = ['created_at', 'llm_result', 'user']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите имя'}),
            'motivation': forms.RadioSelect(choices=[
                ("ui", "Создавать интерфейсы и красиво оформлять идеи"),
                ("logic", "Решать логические задачи и искать решения"),
                ("data", "Анализировать данные и искать закономерности"),
                ("qa", "Писать инструкции, проверять работу систем"),
                ("pm", "Организовывать процесс и управлять командой"),
            ]),
            'ideal_day': forms.RadioSelect(choices=[
                ("talking", "Много общения, совместная работа"),
                ("focus", "Максимум фокуса и минимум отвлечений"),
                ("switching", "Постоянное переключение между задачами"),
                ("freedom", "Полная свобода действий и экспериментов"),
                ("plan", "Чёткий план и стабильные задачи"),
            ]),
            'cognitive_strength': forms.RadioSelect(choices=[
                ("visual", "Работа с визуалом и макетами"),
                ("logic_struct", "Придумывание логики, структуры"),
                ("numbers", "Анализ чисел и графиков"),
                ("bugs", "Проверка и поиск ошибок"),
                ("teaching", "Объяснение сложного простыми словами"),
            ]),
            'self_type': forms.RadioSelect(choices=[
                ("hands_on", "Практик — люблю пробовать руками"),
                ("theorist", "Теоретик — люблю понять систему"),
                ("communicator", "Коммуникатор — люблю работать с людьми"),
                ("researcher", "Исследователь — люблю копать вглубь"),
            ]),
            'personality_trait': forms.RadioSelect(choices=[
                ("patient", "Терпеливо отлаживать детали"),
                ("creative", "Искать новое и нестандартное"),
                ("strategist", "Строить долгосрочную стратегию"),
                ("helper", "Помогать другим разобраться"),
                ("adaptive", "Быстро адаптироваться к новому"),
            ]),
            'work_environment': forms.RadioSelect(choices=[
                ("alone", "Самостоятельно и в тишине"),
                ("pair", "В паре с кем-то"),
                ("team", "В команде, обсуждая идеи"),
                ("leader", "В роли координатора/лидера"),
            ]),
            'reaction_to_difficulty': forms.RadioSelect(choices=[
                ("dig", "Начинаю копать и разбираться сам"),
                ("ask", "Сразу иду за советом"),
                ("try", "Пробую разные подходы"),
                ("hypothesis", "Формулирую гипотезу и тестирую"),
            ]),
            'creative_or_logical': forms.RadioSelect(choices=[
                ("ui", "Придумать и нарисовать интерфейс"),
                ("code", "Написать код, чтобы всё работало"),
                ("data", "Найти закономерности в данных"),
                ("qa", "Проверить чужой код на ошибки"),
                ("plan", "Составить план работы над продуктом"),
            ]),
        }
