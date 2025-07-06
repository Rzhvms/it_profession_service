from django.shortcuts import render
from .forms import SurveyForm
from .utils import generate_it_recommendation, format_recommendation
from django.contrib.auth.decorators import login_required


@login_required
def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.user = request.user
            response.save()

            raw_recommendation = generate_it_recommendation(response)
            recommendation = format_recommendation(raw_recommendation)

            response.llm_result = recommendation
            response.save()

            return render(request, 'form_app/result.html', {
                'recommendation': recommendation,
                'name': response.name,
                'response': response,
            })
    else:
        form = SurveyForm()
    return render(request, 'form_app/form.html', {'form': form})
