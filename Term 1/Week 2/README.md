# Term 1 - Week 2: Loops & Functions

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**

**What did I hand in?**
Workshop retake: see [Resit/Week 2/](../../Resit/Week%202/).

**What did I find difficult, and how did I solve it?**

### Checklist
- [ ] My workshop / homework files are in `homework/`
- [ ] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

**Project title:** AI Study Stress Coach

**My pair partner:** Max Lopez

**Tool we had to use:** n8n

**SDG we had to address:** SDG 3, Good Health & Well-being

**What problem does it solve, and for whom?**
University and applied-science students can feel overwhelmed by stress, poor sleep, workload and deadlines. They may need help choosing one manageable next step. This tool offers general study support and is not a therapist or crisis service.

**What did you build?**
An n8n workflow with a short check-in form. Rules calculate a Low, Moderate or High stress category, and AI writes short study tips based on the answers. The workflow emails the advice to the student and logs the check-in in Google Sheets.

**Link to the live thing (if any):**
Workflow export: [`hackathon/ai-study-stress-coach.json`](hackathon/ai-study-stress-coach.json). Slides: [`hackathon/ai-study-stress-coach-deck.pdf`](hackathon/ai-study-stress-coach-deck.pdf). Demo video: [`hackathon/AI Study Stress Coach - FINAL Short Meter Aligned.mp4`](hackathon/AI%20Study%20Stress%20Coach%20-%20FINAL%20Short%20Meter%20Aligned.mp4).

**How do I run it?**
Import [`hackathon/ai-study-stress-coach.json`](hackathon/ai-study-stress-coach.json) into n8n. Connect the OpenAI, Gmail and Google Sheets nodes to your own accounts and choose the sheet for the log. Open the form and test it with fictional details and an authorised test inbox.

**Who did what?**
Max Lopez designed and built the n8n flow (scoring rule, AI safety instructions, email, Google Sheets logging) and did the testing and demo; I made the presentation.

**Ethical reflection - what are the risks of your tool? Who could it harm?**
AI advice can be wrong or too general, so prompts and test cases need review. Names, email addresses and well-being answers are sensitive; we should collect less data, restrict access and set a deletion period. The form can confirm a submission before the email succeeds, so executions need monitoring and support options should be visible immediately. Students may mistake a category for a diagnosis. We should explain that it comes from project rules and direct serious concerns to human support.

### Checklist
- [x] Prototype code (or export / workflow file) is in `hackathon/`
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
