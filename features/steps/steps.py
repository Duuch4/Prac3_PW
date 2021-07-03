@given(u'Exists a user "{user}" with password "{password}"')
def step_impl(context, user, password):
    from django.contrib.auth.models import User
    context.user = user
    context.password = password
    User.objects.create_user(username=user, email='user@example.com', password=password)


@given(u'I login as user "{user}" with password "{password}"')
def step_impl(context, user, password):
    context.browser.get(context.get_url('/accounts/login/?next=/era/'))
    form = context.browser.find_element_by_tag_name('form')
    usr = form.find_element_by_id('id_username')
    usr.send_keys(user)
    passw = form.find_element_by_id('id_password')
    passw.send_keys(password)
    login = form.find_element_by_tag_name('input')
    login.click()


@when(u'I create career')
def step_impl(context):
    context.browser.get(context.get_url('/era/facultad/9/career/create/'))
    form = context.browser.find_elements_by_tag_name("form")[-1]
    name = form.find_element_by_id('id_name')
    name.send_keys("Grado En Ingenieria Informatica")
    abr = form.find_element_by_id('id_abreviado')
    abr.send_keys("GEI")
    desc = form.find_element_by_id('id_description')
    desc.send_keys("Grau en enginyeria informatica a la EPS")
    submit = form.find_element_by_tag_name('input')
    submit.click()


@then(u'I\'m viewing the details page for career by "user"')
def step_impl(context):
    title = context.browser.find_element_by_tag_name("h1").text
    assert "info" in title


@when(u'I create faculty')
def step_impl(context):
    context.browser.get(context.get_url('/era/facultad/create'))
    form = context.browser.find_element_by_tag_name("form")
    name = form.find_element_by_id('id_name')
    name.send_keys("EPS")
    desc = form.find_element_by_id('id_description')
    desc.send_keys("Escola Politecnica superior")
    submit = form.find_element_by_tag_name('input')
    submit.click()


@then(u'I\'m viewing the details page for faculty by "user"')
def step_impl(context):
    title = context.browser.find_element_by_tag_name("h1").text
    assert "info" in title


@when(u'I edit a career')
def step_impl(context):
    context.browser.get(context.get_url('/era/facultad/9/career/9'))
    context.original = context.browser.find_element_by_tag_name("h1").text[7:-5]
    links = context.browser.find_elements_by_tag_name("a")
    for link in links:
    	if "Edit" in link.text:
    		link.click()
    		break
    name = context.browser.find_element_by_id('id_name')
    name.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    name.send_keys('GEM')
    button = context.browser.find_element_by_id('input')
    button.click()
    


@then(u'There are 1 career edited')
def step_impl(context):
    context.browser.get(context.get_url('/era/facultad/9/career/9'))
    assert context.original != context.browser.find_element_by_tag_name("h1").text[7:-5]


@when(u'I edit a faculty')
def step_impl(context):
    context.browser.get(context.get_url('/era/facultad/9'))
    context.original = context.browser.find_element_by_tag_name("h1").text[9:-5]
    links = context.browser.find_elements_by_tag_name("a")
    for link in links:
    	if "Edit" in link.text:
    		link.click()
    		break
    name = context.browser.find_element_by_id('id_name')
    name.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    name.send_keys('Magisteri')
    button = context.browser.find_element_by_id('input')
    button.click()


@then(u'There are 1 faculty edited')
def step_impl(context):
    context.browser.get(context.get_url('/era/facultad/9'))
    assert context.original != context.browser.find_element_by_tag_name("h1").text[9:-5]


@when(u'I see the list of the careers')
def step_impl(context):
    context.browser.get(context.get_url('/era/facultad/9'))


@then(u'I\'m viewing the list of all the careers by "user"')
def step_impl(context):
    facs = context.browser.find_elements_by_tag_name("li")
    for elem in facs:
    	print(elem.text)


@when(u'I see the list of the facultys')
def step_impl(context):
    context.browser.get(context.get_url('/era/'))


@then(u'I\'m viewing the list of all the facultys by "user"')
def step_impl(context):
    facs = context.browser.find_elements_by_tag_name("li")
    for elem in facs:
    	print(elem.text)
    

@then(u'I\'m viewing the list of all the careers by "faculty"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the list of all the careers by "faculty"')


@then(u'I\'m viewing the list of all the facultys')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the list of all the facultys')

