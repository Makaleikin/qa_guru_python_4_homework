def name_and_arguments(func_name, *args):
    func_name = func_name.replace("_", " ").capitalize()
    if len(args) == 2:
        print(func_name + " - " + "\"" + args[0] + "\"" + ", " + "\"" + args[1] + "\"")
    else:
        print(func_name + " - " + "\"" + args[0] + "\"")


def open_browser(browser_name):
    name_and_arguments(open_browser.__name__, browser_name)


def go_to_companyname_homepage(page_url):
    name_and_arguments(go_to_companyname_homepage.__name__, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    name_and_arguments(find_registration_button_on_login_page.__name__, page_url, button_text)


open_browser("Chrome")
go_to_companyname_homepage("https://www.google.com/")
find_registration_button_on_login_page("https://www.google.com/", "Search")