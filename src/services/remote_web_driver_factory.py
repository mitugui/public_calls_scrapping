from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class RemoteWebDriverFactory():
    @staticmethod
    def get_driver():
        options = FirefoxOptions()
        
        options.add_argument('--headless')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-dev-shm-usage')
        
        options.set_preference('webdriver_accept_untrusted_certs', True)
        options.set_preference('acceptInsecureCerts', True)

        selenium_url = 'http://selenium:4444/wd/hub'

        return webdriver.Remote(
            command_executor=selenium_url,
            options=options
        )