

# Created by worre at 02-Oct-17
Feature: Home Page
    Sample test cases for an interview

  Scenario Outline: Links
    Given The homepage is open
    When The <link> is clicked
    Then The <page> opens

    Examples: eglinks
    |link          |page                                                                                          |
    |Advice Guides |http://www.which.co.uk/reviews/televisions/article/guides                                     |
    |Best Buys     |http://www.which.co.uk/reviews/televisions/article/recommendations/which-best-buy-televisions |
    |Don\'t Buys   |http://www.which.co.uk/reviews/televisions/article/recommendations/which-dont-buy-televisions |


  Scenario Outline: Sorter Options with opened pages
    Given The homepage is open
    When  The Sorter <option> is selected
    Then  The <page> opens

    Examples: egoptions
    |option                  |page                                                                     |
    |Screen Size             |http://www.which.co.uk/reviews/televisions?sortby=screen_size_desc&page=1|
    |Most - recently launched|http://www.which.co.uk/reviews/televisions?sortby=launch_date_desc&page=1|

  Scenario: Confirm product is present on initial load
    Given The site is not loaded
    When the page is loaded
    Then product present

  Scenario: Search for a 65 inch TV
    Given The homepage is open
    When the 65 inch is selected
    Then 65 inch television returned

  Scenario: Pagination
    Given The homepage is open
    When the pagination is used
    Then the navigation moves

