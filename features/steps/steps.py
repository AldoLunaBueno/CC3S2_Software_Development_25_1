from behave import given, when, then
from behave.runner import Context
from src.parsers import time_description_to_hours

@given('que he comido {cukes:g} pepinos')
def step_given_eaten_cukes(context: Context, cukes):
    context.belly.comer(cukes)

@when('espero {time_description}')
def step_when_wait_time_description(context: Context, time_description):
    tags = context.scenario.tags
    if "spanish" in tags:
        total_time_in_hours = time_description_to_hours(time_description, "spanish")
    elif "english" in tags:
        total_time_in_hours = time_description_to_hours(time_description, "english")
    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context: Context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context: Context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."