import base64
from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import DateInputForm
from .models import PsychomatrixBaseContent, PsychomatrixAdditionalContent

from .pillow import Pillow
from .calculator import Calculator


def index(request: HttpRequest, date: str = None) -> HttpResponse:
    if request.method == 'POST' or date:
        if date:
            date_str = date
            date = datetime.strptime(date_str, '%Y-%m-%d')

            return render_results(request, date, date_str)

        else:
            form = DateInputForm(request.POST)
            date_str = form.data["date"]

            if form.is_valid():
                date = datetime.strptime(date_str, '%Y-%m-%d')

                return render_results(request, date, date_str)

    else:
        form = DateInputForm()

    context_data = {'form': form}

    return render(request, "psychomatrix/index.html", context_data)


def render_results(request: HttpRequest, date: datetime, date_str: str) -> HttpResponse:
    pillow = Pillow()
    calculator = Calculator(date)
    numbers = calculator.get_all_numbers()

    image = pillow.create_image(numbers, date_str)
    basic_models, additional_models = get_contents(numbers)

    context_data = {
        'date_str': date_str,
        'image': base64.b64encode(image).decode('utf-8'),
        'basic_models': basic_models,
        'additional_models': additional_models
    }

    return render(request, "psychomatrix/result.html", context_data)


def get_contents(numbers: list) -> tuple[list, list]:
    basic_codes = [
        f'{enum}-нет' if num == '-' else num for enum, num in
        enumerate(numbers[:9], start=1)
    ]
    additional_codes = [
        f'{enum}-0' if num == '-' else f'{enum}-{num}'
        if enum not in [8, 3] else f'{enum}-'
        for enum, num in
        enumerate(numbers[9:], start=1)
    ]

    basic_contents = PsychomatrixBaseContent.objects.filter(
        code__in=basic_codes
    )
    additional_codes = PsychomatrixAdditionalContent.objects.filter(
        code__in=additional_codes
    )

    return basic_contents, additional_codes
