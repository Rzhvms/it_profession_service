from django.conf import settings
from openai import OpenAI
import re


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.API_KEY,
)

MODEL_NAME = "deepseek/deepseek-chat-v3-0324:free"


def generate_it_recommendation(response):
    prompt = f"""
    На основе следующих ответов пользователя порекомендуй подходящие направления в IT:

    1. Мотивация: {response.motivation}
    2. Идеальный день: {response.ideal_day}
    3. Когнитивные предпочтения: {response.cognitive_strength}, тип: {response.self_type}
    4. Личностные особенности: {response.personality_trait}
    5. Рабочий стиль: {response.work_environment}, реакция на сложность: {response.reaction_to_difficulty}
    6. Творческий/логический уклон: {response.creative_or_logical}
    7. Опыт: {", ".join(response.experience)}
    8. Ценности: {", ".join(response.values)}

    Выбери из этого списка 2–3 наиболее подходящих направления:
    - Frontend-разработка
    - Backend-разработка
    - Data Science и AI
    - Тестирование
    - UI/UX-дизайн
    - GameDev
    - DevOps и инфраструктура
    - Продуктовый менеджмент
    - Системный анализ
    - Кибербезопасность

    Ответ должен быть строго по структуре:

    Рекомендации:

    1. Название направления – краткое объяснение, почему оно подходит (1–2 предложения).
    2. Название направления – ...
    3. Название направления – ...

    Описание направлений:

    Название направления:
    Описание в 4–6 предложениях: что это за профессия, какие навыки важны, перспективы и кому она подойдёт.

    Название направления:
    Описание...

    (Пиши на русском языке)
    """

    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Ты карьерный консультант в IT."},
                {"role": "user", "content": prompt},
            ],
            extra_headers={
                # можно указать сайт, если нужно для рейтинга OpenRouter
                # "HTTP-Referer": "https://your-site.com",
                # "X-Title": "IT Profiler",
            },
            extra_body={}
        )

        return process_content(completion.choices[0].message.content)

    except Exception as e:
        return f"Ошибка при запросе к OpenRouter API: {str(e)}"


def process_content(content):
    return content.replace('<think>', '').replace('</think>', '')


def format_recommendation(text):
    text = text.replace('*', '').replace('#', '').strip()
    lines = [line.strip() for line in text.split('\n') if line.strip()]

    html = ''
    recommendations = []
    details = []

    for i, line in enumerate(lines):
        if re.match(r'^[А-ЯA-Z][a-zа-я]+', line) and len(line.split()) < 5:
            recommendations = lines[:i]
            details = lines[i:]
            break
    else:
        recommendations = lines

    if recommendations:
        html += '<div style="margin-bottom: 1.5em;">'
        for line in recommendations:
            html += f'<p>{line}</p>'
        html += '</div>'

    current_title = None
    current_desc = []

    for line in details:
        if re.match(r'^[А-ЯA-Z][a-zа-я]+', line) and len(line.split()) < 5:
            if current_title:
                html += f'<p><strong>{current_title}</strong></p>'
                html += f'<p>{" ".join(current_desc).strip()}</p>'
            current_title = line.strip()
            current_desc = []
        else:
            current_desc.append(line)

    if current_title:
        html += f'<p><strong>{current_title}</strong></p>'
        html += f'<p>{" ".join(current_desc).strip()}</p>'

    return html