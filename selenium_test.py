from selenium import webdriver

def test_home():
    # Open the selenium driver to the correct page
    driver = webdriver.Chrome()
    driver.get("http://204.209.76.167:8000/")

    # Test for the elements that are required to be on the web page
    assert driver.find_element_by_id("name") != None
    assert driver.find_element_by_id("about") != None
    assert driver.find_element_by_id("education") != None
    assert driver.find_element_by_id("skills") != None
    assert driver.find_element_by_id("work") != None
    assert driver.find_element_by_id("contact") != None


test_home()