# Term 1 - Week 3: Lists & Dictionaries

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**

**What did I hand in?**
_List the files, or link to them. Notebook exports, screenshots, scripts._

**What did I find difficult, and how did I solve it?**

### Checklist
- [ ] My workshop / homework files are in `homework/`
- [ ] Everything runs without errors, or I explained what does not and why

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
