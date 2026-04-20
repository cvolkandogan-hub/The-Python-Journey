# ============================================================
# DOSYA: pages/login_page.py
# AÇIKLAMA: SauceDemo login sayfasının tüm işlemleri burada
# Bu bir "sınıf" — login ile ilgili her şeyin evi
# ============================================================

class LoginPage:
    # Sayfadaki elementlerin adresleri — tek yerde tanımlı
    URL = "https://www.saucedemo.com"
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = ".error-message-container"

    def __init__(self, page):
        self.page = page

    def navigate(self):
        """Siteye git"""
        self.page.goto(self.URL)

    def login(self, username, password):
        """Kullanıcı adı ve şifre gir, login butonuna tıkla"""
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """Hata mesajını döndür"""
        return self.page.locator(self.ERROR_MESSAGE)

    def is_login_successful(self):
        """Login başarılı mı kontrol et"""
        return self.page.url == "https://www.saucedemo.com/inventory.html"