# Nyx — A Decision Simulator, Explained for Beginners

This is a beginner explainer for this project, in plain language with one simple analogy. It is not a replacement for the technical paper or report.

**How to read the honesty labels:**

- **Verified** = the number or result is in a file Jayant actually produced, and it was checked here.
- **Reported, not verified** = the number comes from Jayant's own summary or slides. No seeds, no confidence intervals, and no test code were given with it. Treat it as "he says so", not "proven".
- **Plan only** = an idea or a target. It has not happened yet.

---


**In one line:** Nyx is a tiny pretend society that debates a hard question, so you can see what might go wrong before you decide in real life.

**Analogy:** It is like a flight simulator, but for decisions. Pilots practise crashes in a simulator. Nyx practises bad debates in a simulator.

**What Jayant actually did (verified):**

- He built a deterministic kernel. Deterministic means: same starting seed, same result, every time. No hidden randomness.
- He ran a worked example. The question was: "Should we ban smartphones in schools?"
- There were 6 agents: Maya (student), Mr. Rao (teacher), Mrs. Khan (parent), Principal, Dev (student), and Dr. Iyer (researcher). Seed 42. Eight rounds.

**The real result (verified):**

- The group's average reputation climbed round by round: 0.50, then 0.65, 0.84, 0.93, 0.98, 0.98, 1.00, and 1.00.
- Dev, the anxious student, had a crash in rounds 4 and 5. Then he recovered from round 6. Nobody else crashed.
- The final outcome numbers were: reputation 1.00, inequality 0.069, trust 0.714, and centralization 0.139. These are rounded.

**What is NOT proved / still open:**

- A simulation is not real life. These numbers describe the pretend society, not real students, teachers, or parents.
- The probabilities inside Nyx are simulation numbers. They are not validated against the real world.
- One small honest wrinkle: the README says the agents' inner variables live between 0 and 1, but in this real run some self-worth values went a little above 1, up to about 1.15. That is a known detail to fix later. It does not change the story above, but it should not be hidden.
