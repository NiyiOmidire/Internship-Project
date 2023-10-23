from behave import given, when, then


@given('Open Signin page')
def open_signin_page(context):
    context.app.signin_page.open_signin_page()


@when('Signin')
def signin(context):
    context.app.signin_page.signin()


@then('Verify sign in page successful')
def verify_signin_success(context):
    context.app.signin_page.verify_signin_success()