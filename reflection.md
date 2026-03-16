# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used ChatGPT-style assistance and the Copilot Agent-like workflow provided by the coding assistant in the editor.

- Correct suggestion: The AI suggested that the inconsistent hints were caused by mixed-type comparisons (sometimes the `secret` was a string). This was correct. I verified it by inspecting `app.py` and finding code that alternated casting the secret to `str` every other attempt; after forcing numeric comparison the bug disappeared and pytest passed.
- Incorrect/misleading suggestion: Early on, the AI-generated patch returned both `(outcome, message)` from `check_guess`, while the rest of the code and tests expected a single outcome string. That change broke existing tests. I verified this by running `pytest` and seeing multiple failures; I then reverted `check_guess` to return just the outcome string and moved message creation into `app.py`.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I judged a bug fixed when the behavior was consistent in the app and the automated tests passed. For example, the regression test `test_large_guess_against_small_secret_numeric` asserts `check_guess(100, 9) == "Too High"` — this previously failed when the secret was compared as a string. After the fix, running `pytest` showed that test (and the full suite) passed.

I ran both targeted and full-test runs:
- Single test: `pytest tests/test_game_logic.py::test_large_guess_against_small_secret_numeric -q` to quickly check the regression.
- Full suite: `pytest -q` to ensure no other behavior regressed. All tests passed after the final changes.

AI helped propose the regression test and suggested likely root causes; I verified suggestions by reading the code and running tests.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
