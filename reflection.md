# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
 1 The game would not restart correctly.
 2 The hint would not give me correct logic, it would give me too low when I would put 100.
 3 The number of tries left would give incorrect numbers when submitting a guess.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used ChatGPT-style assistance and the Copilot Agent-like workflow provided by the coding assistant in the editor.

Correct suggestion: The AI suggested that the inconsistent hints were caused by mixed-type comparisons (sometimes the `secret` was a string). This was correct. I verified it by inspecting `app.py` and finding code that alternated casting the secret to `str` every other attempt; after forcing numeric comparison the bug disappeared and pytest passed.
Incorrect suggestion: Early on, the AI-generated patch returned both `outcome, message` from `check_guess`, while the rest of the code and tests expected a single outcome string. That change broke existing tests. I verified this by running `pytest` and seeing multiple failures; I then reverted `check_guess` to return just the outcome string and moved message creation into `app.py`.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed when the behavior was consistent in the app and the automated tests passed. For example, the regression test `test_large_guess_against_small_secret_numeric` asserts `check_guess(100, 9) == "Too High"` — this previously failed when the secret was compared as a string. After the fix, running `pytest` showed that tes passed.

I ran both targeted and full-test runs and All tests passed after the final changes.
AI helped propose the regression test and suggested likely root causes, I verified suggestions by reading the code and running tests.It also helped me understand i was ale to do single tests. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
- The secret number kept changing because streamlit would rerun the the script evertime the user would interact with the app. The number was constantly being replaced instead of staying the same. The way I would explain it to a friend is Streamlit works like a script that restarts evertime something happens on the app. The change I made was that I stored the secret number in session state instead of generating it everytime. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
- One habit I would like to reuse is to test frequently after making changes. Running the app evertime helped me quickly identify what was working and what was causing problems. One thing I would do differenty is give clearer instructions and give more context about the problems that need to be solved. This project showed me that Ai generated code can be helpful but at the same time it can still be giving wrong answers so it must be reviwed and also understood by the developer. 
