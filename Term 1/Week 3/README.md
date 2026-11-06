# Term 1 - Week 3: Lists & Dictionaries

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**
The Week 3 workshop notebook: lists (Food Bank Inventory), analysing list data (Wage Gap Analyzer),
dictionaries (City Services Map, with a district that is missing from the data), and the big
assignment **Food Bank Manager**: a menu program a volunteer could use to show stock, register
donations, hand out packages, warn about low stock and print a report. Plus Exercise 4, the first
API call to a language model.

**What did I hand in?**
`homework/Week3_Workshop_Lili.ipynb`: the workshop notebook with Exercises 1-3, the Food Bank
Manager (including the bonus: families served and a shortage list) and the three reflections,
with every cell except the API cells run in order. All names and data in it are made up, as the course asks.

Exercise 4 (the API call) is written in the notebook but **not run in this copy**: it needs my own
API key, and the course rule is that the key never goes in a notebook or in the portfolio. The
course page says the key and Exercise 4 are "not part of your portfolio"; the notebook's homework list
also asks for a screenshot of `ask.py` running in Cursor, which is not included here because it needs
my own key and laptop.

**What did I find difficult, and how did I solve it?**
Handing out a package when an item has run out. Subtracting 1 from an item at 0 gives -1, so the
loop has to skip it with `continue`. In the test run a small donation of baby food runs out after two
packages, and the program warns about it and puts it on the shortage list. "Rice" and "rice" would
also become two different items, so the program cleans the name with `.strip().lower()` first.

**AI use:** As the course allows, I used Claude (an AI assistant) for this notebook: it wrote and
ran the code and drafted the written answers. Every cell except the API cells was run in order, so the
outputs you see are real.

### Checklist
- [x] My workshop / homework files are in `homework/`
- [x] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

**Project title:** Rebuild

**My pair partner:** Felix

**Tool we had to use:** Gemini API from Python, with a Streamlit interface

**SDG we had to address:** SDG 10, Reduced Inequalities

**What problem does it solve, and for whom?**
People leaving prison, moving to another country, losing housing or going through another major life change may face many urgent tasks at once. Finding ID, housing, income and healthcare can be difficult without a stable address or support network. Rebuild helps put these tasks in order.

**What did you build?**
A Streamlit app where a user describes their situation in their own words. Gemini turns this into an ordered checklist across the relevant life areas. Users can tick off steps, ask for an explanation and update the plan while keeping completed steps.

**Link to the live thing (if any):**
Live app (built and deployed by Felix): https://rebuild-nq5nwmyxtv2ak6efhsybx9.streamlit.app/ · Project documentation: [`hackathon/README 3..md`](hackathon/README%203..md) and [`hackathon/README 3. 2.md`](hackathon/README%203.%202.md). Slides: [`hackathon/Rebuild_Plan_Hackathon_3_Final.pptx.pdf`](hackathon/Rebuild_Plan_Hackathon_3_Final.pptx.pdf).

**How do I run it?**
See the setup instructions in [`hackathon/README 3..md`](hackathon/README%203..md) and [`hackathon/README 3. 2.md`](hackathon/README%203.%202.md). They describe Python 3.10+, `pip install -r requirements.txt`, a `.env` file with `GEMINI_API_KEY`, and `streamlit run app.py`.

**Who did what?**
We brainstormed the idea, defined the problem and decided how the product should work together. Felix did most of the technical development, including building and deploying the Streamlit app; I worked on the planning and design decisions and made the presentation (problem, solution, SDG and ethical risks). We tested and refined the concept together.

**Ethical reflection - what are the risks of your tool? Who could it harm?**
Gemini could invent a phone number, organisation or legal requirement that a person in a difficult situation acts on. The prompt bans these details, and code checks the structure of the plan, but this does not prove that every answer is correct. Failed or empty plans also cost users time and limited data. User descriptions are sent to Gemini, and the prototype stores sensitive information in plain text without a real login; it needs encryption, authentication and a retention policy before real use. Crisis keywords can miss people or interrupt them unnecessarily, and the mainly US and English support list needs local, reachable services.

### Checklist
- [ ] Prototype code (or export / workflow file) is in `hackathon/`
- [x] This week's slides are in `hackathon/`
- [ ] The prototype actually runs, and I wrote down how to run it
- [x] Ethical reflection written above

---

## 3. Presentation -> [`presentation/`](presentation/)

*Only fill this in for the week your group was selected to present. You need at least **one** of these across the whole term.*

- [ ] My group presented in this week
- [ ] Slides are in `presentation/`
- [ ] Proof of the live demo is in `presentation/` (recording, screenshots, or link)

**How did it go? What would I do differently next time?**

---

## 4. Reflection

**What is the most important thing I learned this week?**

**Where does this connect to "AI for Good"?**
_One concrete link to ethics, sustainability or social impact._
