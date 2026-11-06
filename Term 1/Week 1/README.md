# Term 1 - Week 1: Python Basics & Flow Control

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**
The Week 1 workshop notebook: Python as a calculator (the operators, including `//`, `%` and `**`),
variables and the four data types, `input()` with type conversion, and `if` / `elif` / `else` with a
simple income risk classifier and a reflection on whether it is fair. Then the big assignment
**Green or Not?**, a CO2 budget calculator that asks about flights, driving and diet, adds up the
yearly CO2 and says whether you are under, slightly over or far over the 2500 kg budget.

**What did I hand in?**
`homework/Week1_Workshop_Lili.ipynb`: the workshop notebook with every coding exercise and written
question done, and run from top to bottom. The two "write down your guess" prompts, the end-of-session
checklist and the cell for demo notes are left for me. In the test run, 2 flights, 3000 km of driving and eating meat daily
gives 2890 kg CO2, which is "slightly over budget".

**What did I find difficult, and how did I solve it?**
`input()` always gives back text, so `'6' * 7` gives `'6666666'`, not 42. The answer has to be
converted with `int()` or `float()` straight away. The other surprise was the classifier: adding age to income
made it worse, because now being young alone pushes someone up a risk level.

**AI use:** As the course allows, I used Claude (an AI assistant) for this notebook: it wrote and
ran the code and drafted the written answers. The notebook was run from top to bottom, so the
outputs you see are real.

### Checklist
- [x] My workshop / homework files are in `homework/`
- [x] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

**Project title:** FocusQuest

**My pair partner:** Ana Talg Wolf

**Tool we had to use:** Bolt.new or Lovable (the course brief allowed both); we used Lovable.

**SDG we had to address:** SDG 4, Quality Education

**What problem does it solve, and for whom?**
Many students know *what* they should study; the hard part is starting. A big, unclear task (a whole exam, a thesis chapter)
feels overwhelming, so it gets pushed back. This is common: a meta-analysis of procrastination research estimates that
80% to 95% of college students procrastinate (Steel, 2007, *Psychological Bulletin* 133(1), 65–94,
[doi.org/10.1037/0033-2909.133.1.65](https://doi.org/10.1037/0033-2909.133.1.65)). FocusQuest is meant for independent study, when a
student works alone towards a goal, and it was designed with students who experience ADHD-related focus difficulties in mind.

**Who is it for, and who is it not for?**
- **For:** university students studying on their own who want more structure: people who struggle with getting started,
  procrastination, distractions, time awareness, or coming back to work after a break.
- **Not the main users:** younger learners (the language and examples may not suit them), and practical subjects that depend on lab
  work, physical practice or specialist software (the app may be less useful there). It is **not for** anyone looking for a diagnosis
  or treatment: FocusQuest does not diagnose or treat ADHD and does not replace professional or educational support.
- **Conditions of use:** a suitable device, reliable internet, English, and basic digital skills (uploading a file or pasting text).

**What did you build?**
A web app (the live version is called StudyQuest) that turns a student's own study material into small study "quests".
Our documented study cycle:
1. **Input:** the student adds study material (uploads a PDF or pastes notes); the live app also asks for a goal and a deadline.
2. The app suggests topics or study quests from that material, and the student picks one.
3. The student chooses a session length and their energy level.
4. A focus timer runs, with a short, structured break.
5. **Output:** the student completes the session and moves forward towards the goal, one quest at a time.

**Where the required tool (Lovable) is used:** we used Lovable to generate and refine the web app. The prototype combines
study-material input, suggested quests, a time and energy choice, a focus timer, structured breaks and progress towards a goal.

**Why this solution fits the problem:** our design aims to help with choosing a small first step, not only with timing a session.
A timer alone covers the timing part; the suggested quests are meant to give a starting point taken from the student's own material.
Whether this really helps students start more easily still needs testing with students. FocusQuest addresses SDG 4 by aiming to make
independent learning more accessible and manageable: flexible sessions, one quest at a time, no public comparison or punishment for
missed days, and the learner keeps control over the timer, resources and breaks.

**Link to the live thing (if any):**
Live app: [map-my-study.lovable.app](https://map-my-study.lovable.app/) (online on 6 Nov 2026). Project details:
[`hackathon/FocusQuest Hackathon 1 README.pdf`](hackathon/FocusQuest%20Hackathon%201%20README.pdf) (original:
[`.pages`](hackathon/FocusQuest%20Hackathon%201%20README.pages)). Ethical reflection:
[`hackathon/FocusQuest Ethical Reflection.pdf`](hackathon/FocusQuest%20Ethical%20Reflection.pdf). Slides:
[`hackathon/FocusQuest_Final_Presentation.key`](hackathon/FocusQuest_Final_Presentation.key). The two PDF copies were made with
LibreOffice, so the layout differs a little from the Pages originals.

**How do I run it?**
Open the live app. No installation is needed. Set a goal and a deadline, add a PDF or paste notes (sample notes are
included for demonstrations and for cases where file processing is unavailable), pick a suggested quest, choose a focus length and
start the timer.

**Who did what?**
I wrote the README, the ethical reflection and the presentation slides; Ana Talg Wolf built the working product and the demo. We developed the concept, tested it and did the final review together.

**Ethical reflection - what are the risks of your tool? Who could it harm?**
The app may exclude students without a suitable device, reliable internet or enough English. Accessibility features need testing. The design assumes students have suitable course material and can judge AI suggestions; short sessions or an adventure map will not suit every learner or every subject. Uploaded notes may contain private or copyrighted information, so users need a clear explanation of processing, limited collection and storage, and protection for confidential files. Schools or employers could misuse activity records to judge effort, ability or disability. The prototype has not shown that it improves learning or reduces procrastination; voluntary testing with different students, including students with ADHD, is still needed.

**AI use:** We used Lovable to generate and refine the web app and ChatGPT to develop the concept and support the written
documentation; we reviewed the outputs, tested the product and remain responsible for the work. For the resit (November 2026),
Claude (an AI assistant) helped restructure this section against the hackathon rubric and found the Steel (2007) source; the project
description comes from our original README, ethical reflection and slides.

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
