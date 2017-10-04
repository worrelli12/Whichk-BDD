from behave import *
from selenium import webdriver

use_step_matcher("re")


@given('The homepage is open')
def step_home(context):
    context.driver = webdriver.Chrome("C:\\Users\\worre\\AppData\\Local\\chromedriver.exe")
    context.driver.get("http://www.which.co.uk/reviews/televisions")


@given('The site is not loaded')
def step_impl(context):
    context.driver = webdriver.Chrome("C:\\Users\\worre\\AppData\\Local\\chromedriver.exe")
    context.driver.get("http://www.google.co.uk")


@given('a television has been added to compare')
def step_impl(context):
    context.driver.find_element_by_class_name('_3sLz3 action-add').click()


#This should work - the {link} should reoognise the same  word in the feature file***
#Returns an error when the Step Matcher looks for it
#Issue raised with JetBrains


@when('The {link} is clicked')
def step_impl(context, link):
    context.driver.find_element_by_link_text(link).click()


@when('The Sorter {option} is selected')
def step_impl(context, option):
    el = context.driver.find_element_by_id('product_listing_sorter')
    for option in el.find_elements_by_tag_name('option'):
        if option.text == option:
            option.click()
            break


@when('the 65 inch is selected')
def step_impl(context):
    context.driver.find_element_by_class_name('_3F1dv').click()


@when('a television is added to compare')
def step_impl(context):
    context.driver.find_element_by_class_name('_3sLz3 action-add').click()

@when('the page is loaded')
def step_impl(context):
    context.driver.get("http://www.which.co.uk/reviews/televisions")

@when('the comparison is made')
def step_impl(context):
    context.driver.find_element_by_class_name('view-comparison button button-primary icon-right').click()


@when('the pagination is used')
def step_impl(context):
    context.driver.find_element_by_link_text('9').click()


@then('The {page} opens')
def step_url(context, page):
    testoutput = context.driver.current_url
    assert testoutput,  page


@then('65 inch television returned')
def step_url(context):
    context.driver.find_elements_by_xpath("//*[contains(text(), '65U6663DB')]")
    pass


#Confirm that the Compare bar appears
@then('the compare bar appears')
def step_impl(context):
    context.driver.find_element_by_class_name('cont-products-compare active')
    pass


@then('the comparison opens')
def step_impl(context):
    context.driver.find_element_by_class_name('view-comparison button button-primary icon-right')
    testoutput = context.driver.current_url
    assert testoutput, 'http://www.which.co.uk/reviews/televisions/compare'

@then('product present')
def step_impl(context):
    context.driver.find_elements_by_xpath("//*[contains(text(), '32PHT4132/05')]")
    pass

@then('the navigation moves')
def step_impl(context):
    context.driver.implicitly_wait(10)  # seconds
    testoutput = context.driver.current_url
    assert testoutput, 'http://www.which.co.uk/reviews/televisions?sortby=testing_date_desc&page=9'