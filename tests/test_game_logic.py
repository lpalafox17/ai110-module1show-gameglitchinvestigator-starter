from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_large_guess_against_small_secret_numeric():
    # Regression test for lexicographic bug: ensure numeric comparison
    # 100 (guess) is greater than 9 (secret) and should be "Too High".
    # FIX: Added as part of repair; Copilot Agent suggested this regression case.
    assert check_guess(100, 9) == "Too High"
