from behave import given, when, then
from behave.runner import Context
from src.parsers import time_descr_to_h
import random
import time

@given('que he comido {cukes:g} pepinos')
def step_given_eaten_cukes(context: Context, cukes):
    context.belly.comer(cukes)
    context.eaten_cukes = cukes

@when('espero un tiempo aleatorio entre {time_description_1} y {time_description_2}')
def step_when_wait_time_description(context, time_description_1, time_description_2):
    time_1 = time_descr_to_h(time_description_1)
    time_2 = time_descr_to_h(time_description_2)
    random_time = random.uniform(time_1, time_2)
    context.random_time = random_time
    context.belly.esperar(random_time)

@when('espero {time_description}')
def step_when_wait_time_description(context: Context, time_description):
    tags = context.scenario.tags
    if "spanish" in tags:
        total_time_in_hours = time_descr_to_h(time_description, "spanish")
    elif "english" in tags:
        total_time_in_hours = time_descr_to_h(time_description, "english")
    elif "stress" in tags:
        total_time_in_hours = time_descr_to_h(time_description)
    context.belly.esperar(total_time_in_hours)
    context.time = total_time_in_hours

@when('pregunto cuántos pepinos más puedo comer')
def step_when_irrelevant(context: Context):
    pass

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context: Context):
    if "stress" in context.scenario.tags:
        start = time.time()
        assert context.belly.esta_gruñendo(stress_test = True), "Se esperaba que el estómago gruñera, pero no lo hizo."
        end = time.time()
        print(f"  [STRESS] Took {(end-start):0.3f} seconds")
    else:
        assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context: Context):
    if "stress" in context.scenario.tags:
        assert context.belly.esta_gruñendo(stress_test = True), "Se esperaba que el estómago no gruñera, pero lo hizo."
    else:
        assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."
    
@then('mi estómago debería gruñir o no dependiendo del tiempo')
def step_then_belly_conditional_growl(context: Context):
    print(f"  Random time {context.random_time}")
    if context.random_time > 1.5:
        assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."
    else:
        assert not context.belly.esta_gruñendo(stress_test = True), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then('debería ocurrir un error')
def step_when_invalid_value_then_error(context: Context):
    try:
        context.belly.esta_gruñendo()
        assert False, "Se esperaba un ValueError"
    except ValueError:
        print("  El test fallo de forma controlada")

@then('debería haber comido {cukes:g} pepinos')
def step_given_eaten_cukes_then_eaten_the_same(context: Context, cukes):
    assert context.belly.pepinos_comidos() == cukes
    
@then('debería predecir que mi estómago va a gruñir')
def step_given_eaten_cukes_then_predict_growl(context: Context):
    assert context.belly.predict_growl()
    
@then('debería decirme que puedo comer {remaining_cukes:g} pepinos más')
def step_given_eaten_cukes_then_remaining_cukes(context: Context, remaining_cukes):
    assert context.belly.remaining_cukes_avoiding_growl() == remaining_cukes
    
@then('debería decirme que si como un pepino más voy a gruñir')
def step_given_eaten_cukes_max_then_one_more_growl(context: Context):
    assert context.belly.remaining_cukes_avoiding_growl() == 0
    
@then('debería decirme que ya es tarde, voy a gruñir')
def step_give_so_eaten_cukes_then_gonna_growl(context: Context):
    assert context.belly.remaining_cukes_avoiding_growl() == -1