# ============================================================
# DOSYA: basics/test_01_my_first_test_script.py
# AÇIKLAMA: The first professional test written using pytest
# ============================================================

def user_login_control(user_name, password):
    valid_user = "admin"
    valid_password = "Test1234"

    if user_name == valid_user and password == valid_password:
        return "SUCCESSFUL"
    elif user_name != valid_user:
        return "ERROR - Invalid username"
    else:
        return "ERROR - Invalid password"


def test_correct_credentials():
    result = user_login_control("admin", "Test1234")
    assert result == "SUCCESSFUL"

def test_wrong_password():
    result = user_login_control("admin", "wrong_password")
    assert result == "ERROR - Invalid password"

def test_wrong_username():
    result = user_login_control("hacker", "Test1234")
    assert result == "ERROR - Invalid username"

def test_empty_credentials():
    result = user_login_control("", "")
    assert result == "ERROR - Invalid username"
    
def test_buyuk_kucuk_harf_farki():
    result = user_login_control("Admin", "Test1234")
    assert result == "ERROR - Invalid username"