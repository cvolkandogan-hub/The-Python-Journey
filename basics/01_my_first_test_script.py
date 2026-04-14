# ============================================================
# DOSYA: basics/01_my_first_test_script.py
# AÇIKLAMA: First test script in Python – Testing the intro function
# YAZAR: Cem
# ============================================================

def user_login_control(user_name, password):
    """
    A function that verifies user login credentials.
    In real-life scenarios, this function would test a web application.
    For now, we are only learning the logic.
    """
    valid_user = "admin"
    valid_password = "Test1234"

    if user_name == valid_user and password == valid_password:
        return "SUCCESSFUL ✅"
    elif user_name != valid_user:
        return "ERROR ❌ - Invalid username"
    else:
        return "ERROR ❌ - Invalid password"


# ---- TEST SCENARIOS ----

print("=" * 50)
print("TEST RESULTS")
print("=" * 50)

# Test 1: Correct credentials
result1 = user_login_control("admin", "Test1234")
print(f"Test 1 - Correct login:          {result1}")

# Test 2: Wrong password
result2 = user_login_control("admin", "wrong_password")
print(f"Test 2 - Wrong password:         {result2}")

# Test 3: Wrong username
result3 = user_login_control("hacker", "Test1234")
print(f"Test 3 - Wrong username:         {result3}")

# Test 4: Both are incorrect
result4 = user_login_control("", "")
print(f"Test 4 - Empty credentials:         {result4}")

print("=" * 50)