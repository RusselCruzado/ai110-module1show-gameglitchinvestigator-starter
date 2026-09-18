# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    The game ran smoothly and had very obvious prompt and counting errors. The guess would be higher than the secret and the game would tell me to go higher instead of going lower. The attempts left counter was off, I would have one attempt left and the game would say it was game over. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

    First concrete bug: Hints show the opposite of what it's supposed to say. If user input is lower than secret, hint gives 'go lower' when it is supposed to say 'go higher'.
    Second concrete bug: When user loses and has no more attempts left, New Game feature does not work. A new game never starts. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 50 | "Go Higher" hint | "Go Lower" hint | None |
| Use all 8 attempts without guessing correctly, then click "New Game" | Fresh secret number is generated, attempts reset to 8, guess history cleared, "Game Over" prompt disappears | "Game Over" prompt stays, History never gets cleared | None |
| Make 7 guesses incorrectly (Attempts allowed: 8) | Attempts left should have the value of 1 | Attempts left outputs 0 which prompts "Game Over" with only 7 gusses | None |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    AI suggested just switching the two outputs with eachother for 'Go HIGHER' and 'Go LOWER'.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
    The code that was changed at first was very confusing because it changed both app.py and logic_utils.py but when I read it and noticed that it was referencing each other, I understood it, so I didn't change it. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    I ran it through streamlit to test if the bug was fixed. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    I manually tested it and ran it through streamlit, and it showed me that the AI fixed the logic and corrected it. 
- Did AI help you design or understand any tests? How?
    AI did help me design and understand the tests, it stated to me what it suggested to do and explained why certain lines should change. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    Streamlit reruns the entire code from top to bottom. It does that everytime a button is clicked, or something is typed in the app. Session state would be the app's memory that allows the app to restart after every interaction. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    The prompts I make should definitely be more clear and make sure the suggestions made have example code and the logic. I need to make sure I create pytest cases everytime I refactor. I'm still getting used to using repositories as well. 
- What is one thing you would do differently next time you work with AI on a coding task?
    I would tell AI to guide me to manually code it so I can understand the logic ever better. I also would instruct the AI, when running pytest, to show me what the AI is testing. One thing I did have a hiccup up on was implementing the code before going through the suggested code the AI, I had to undo the code just so I can go over the code first. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
    This project revealed to me that AI generated code can give you a more clear pathway of performing the same task differently that makes the code more readable. Using AI generated code also makes refactoring/debugging so much quicker and easier. 