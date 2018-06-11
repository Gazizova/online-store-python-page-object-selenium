
class Locators(object):

    url = "http://automationpractice.com/index.php"

    # home page locator
    SignInButtonXpath = "//a[contains(@title, 'Log in to your customer account')]"
    ContactUsButtonXpath = "//a[contains(@title, 'Contact Us')]"
    WomenButtonXpath = "//a[contains(@title, 'Women')]"
    DressesButtonXpath = "//a[contains(@title, 'Dresses')]"
    T_shirtsButtonXpath = "//a[contains(@title, 'T-shirts')]"
    SearchID = "search_query_top"
    CartXpath = "//a[contains(@title, 'View my shopping cart')]"
    PopularXpath = "//*[@class='homefeatured']"
    BestSellersXpath = "//*[@class='blockbestsellers']"

    Footer_MyAccount = "//a[contains(@title, 'Manage my customer account')]"

    # login form
    EmailID = "email"
    PasswordID = "passwd"
    SubmitLoginButtonID = "SubmitLogin"


    # My account
    OrderHistoryAndDetailsXpath = '//span[text()="Order history and details"]'
    MyCreditSlips = '//span[text()="My credit slips"]'
    MyAddress = '//span[text()="My addresses"]'
    MyPersonalInformation = '//span[text()="My personal information"]'
    MyWishlist = '//span[text()="My wishlists"]'