from pathlib import Path

from streamlit.testing.v1 import AppTest


def test_attempts_left_decreases_after_guess():
    app_path = Path(__file__).parents[1] / "app.py"
    app = AppTest.from_file(str(app_path)).run()

    assert "Attempts left: 8" in app.info[0].value

    app.session_state.secret = 101
    app.text_input[0].set_value("1")
    app.button[0].click()
    app.run()

    assert "Attempts left: 7" in app.info[0].value
