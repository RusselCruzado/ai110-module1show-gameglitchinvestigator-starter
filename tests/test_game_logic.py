from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_hint_direction_matches_guess_position():
    # A lower guess needs a higher hint, and a higher guess needs a lower hint.
    cases = [
        (40, 50, "📈 Go HIGHER!"),
        (60, 50, "📉 Go LOWER!"),
    ]

    for guess, secret, expected_hint in cases:
        _, message = check_guess(guess, secret)
        assert message == expected_hint
