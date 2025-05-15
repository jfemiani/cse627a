Generate a batch of quiz questions that test **durable conceptual understanding**, **failure-mode awareness**, and **reasoning under uncertainty** — not fact recall.

The questions should:
- Be **answerable weeks after instruction** if the student understood the principles
- Avoid rote definitions or symbolic lookup
- Require the student to reason through:
  - Edge cases
  - Implications of design choices
  - When methods fail or succeed
  - Model behavior under atypical conditions

Each question should:
- Be grounded in the core ideas of the topic
- Use realistic distractors that are plausible but incorrect
- Include scenario-based setups where possible

Do NOT test:
- Definitions or theorem names
- Small algebra manipulations or numerical tricks
- Paper history or author trivia

**Examples (non-topic-specific):**
1. Why might a maximum-likelihood classifier fail in low-data regimes?
2. When does the independence assumption in Naive Bayes cause incorrect predictions?
3. What tradeoff arises when increasing model complexity in the absence of regularization?
4. Which assumption does PCA violate if the data is not centered?
5. What failure mode occurs when using loopy belief propagation on a dense graph?

Generate 5–10 of these “conceptual transfer” questions for [INSERT SECTION HERE].
Each should be multiple choice (Text2QTI style), with plausible distractors and 1 clearly correct answer.

If I have not already told you what Text2QTI style is, suggest that I past in `text2qti-prompt.md` to remind you. 