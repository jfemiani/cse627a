

### 1. Overall Structure

A Text2QTI file is a plain-text file that wraps Markdown content in a simple, line-based syntax. At the top of the file you can specify a quiz title and description. For example:

```
Quiz title: My Quiz Title
Quiz description: This quiz covers topics X, Y, and Z.
```

Any text following the title lines is processed as part of the quiz.
The quiz description can be multiple lines, but **every subsequent line must be indented by two spaces.**

---

### 2. Questions and Answers

#### Question Declaration
- Each question begins with a line that starts with a number, a period, and at least one space.  
  **Example:**
  ```
  1. What is 2+2?
  ```

#### Answer Choices
- Each answer choice is on its own line and begins with a letter followed by a closing parenthesis and a space.
- The correct answer is indicated by an asterisk `*` immediately before the letter (with no additional spaces).  
  **Example:**
  ```
  a) 3
  *b) 4
  c) 5
  d) 22
  ```

#### Feedback (Optional)
- You can include feedback for the overall question or for specific answers.
  - **General Question Feedback:**  
    Begin a line with `...` immediately after the question text. This feedback will appear to the student after they submit an answer.
    
    **Example:**
    ```
    1. What is 2+2?
    ... Remember that addition is combining numbers.
    a) 3
    *b) 4
    c) 5
    d) 22
    ```
    
  - **Per-Answer Feedback:**  
    For each answer option, you can include feedback lines immediately after that option. 
    Feedback should also indicate the correctness of the answer.

    **Example:**
    ```
    1. What is 2+2?
    a) 3
    ... Incorrect. 3 is too low.
    *b) 4
    ... Correct! 2+2 equals 4.
    c) 5
    ... Incorrect.  5 is too high.
    d) 22
    ... Incorrect.  Far too high.
    ```

---

### 3. Multi-line Questions or Options

- If a question, answer choice, or feedback spans multiple lines, **every subsequent line must be indented** by at least one space or tab to indicate that it is part of the same block.
  
  **Example of a multi-line question:**
  ```
  2. Explain why the Beta distribution is a conjugate prior for the Bernoulli likelihood.
      This means that when you multiply the likelihood
      with the Beta prior, the resulting posterior is also a Beta
      distribution, which simplifies Bayesian updating.
  a) Because it is the only distribution available.
  *b) Because the functional form is preserved after multiplication.
  c) Because it always leads to a uniform posterior.
  d) Because it maximizes the likelihood.
  ```

- The same rule applies for multi-line answer choices or feedback. Make sure each additional line in the same block is consistently indented.

---

### 4. Math Formulas

- **Inline Math:** Use dollar signs `$...$` for inline math formulas. Do **not** use `\(` or `\)`.  
  **Example:**  
  `The likelihood is given by $p(x|\mu)= \mu^x (1-\mu)^{1-x}$.`

- **Display Math:** Use double dollar signs `$$...$$` for display math (block equations).  
  **Example:**
  ```
  3. Derive the normalization condition:
      $$
      \sum_{x=0}^1 p(x|\mu) = \mu + (1-\mu) = 1.
      $$
  a) Incorrect
  *b) Correct
  c) Incorrect
  d) Incorrect
  ```

---

### 5. Additional Quiz Options

Immediately after the quiz title and description, you can include quiz-level options on separate lines if needed. For example:

```
shuffle answers: true
show correct answers: false
```

These options must be set with plain text values of `true` or `false`.


### 6. Evaluating Questions

Please make sure that a student would not be able to guess the correct answer without knowing the material. 
Avoid making the correct answer stand out as the correct answer, for example by making it longer of more detailed then the other options. 


---

### 7. Putting It All Together – The Perfect Prompt

Below is a sample "perfect" Text2QTI prompt that demonstrates all of the features discussed:

```markdown
Quiz title: Calculus Fundamentals Quiz  
Quiz description: This quiz covers fundamental concepts in calculus, including differentiation and the power rule.
shuffle answers: true
show correct answers: false

1. What is the derivative of $x^3$ with respect to $x$?  
  Apply the power rule, which states that $\frac{d}{dx} x^n = n\,x^{n-1}$.
a) $3x$  
... Incorrect. The power rule requires multiplying by the exponent and reducing the exponent by one.
*b) $3x^2$  
... Correct! Differentiating $x^3$ gives $3x^2$ by the power rule.
c) $x^2$  
... Incorrect. This option omits the factor of 3.
d) $x^3$  
... Incorrect. The derivative of a function is not the same as the original function.

---

### Summary

- **Quiz Title & Description:** Set at the top with no indentation.
- **Question Lines:** Begin with a number, a period, and space; multiple lines for a question are indented.
- **Answer Choices:** Begin with a letter and a parenthesis on a new line (no indentation for these lines).
- **Feedback:** Lines beginning with `...`,  are used  per-answer feedback; if multi-line, indent consistently.
- **Math:** Use `$...$` for inline math and `$$...$$` for display math (do not use `\(` or `\)`).
- **Avoid** obvious answers or other common mistakes.
