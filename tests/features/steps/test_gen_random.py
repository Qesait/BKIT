from behave import Given, When, Then
from lab_python_fp.gen_random import gen_random


@Given('amount of numbers {amount} and minimum {min_} and maximum {max_}')
def step_impl(context, amount, min_, max_):
    context.amount = int(amount)
    context.min = int(min_)
    context.max = int(max_)
    context.generator = gen_random(context.amount, context.min, context.max)


@When('we generate numbers')
def step_impl(context):
    context.numbers = list(context.generator)


@Then('we have to get the specified number of numbers in a given range')
def step_impl(context):
    assert len(context.numbers) == context.amount
    assert all(context.min <= i <= context.max for i in context.numbers)

# behave tests/features
