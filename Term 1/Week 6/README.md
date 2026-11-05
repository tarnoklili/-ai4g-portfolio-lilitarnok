# Term 1 - Week 6: Language Models

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**

**What did I hand in?**
Workshop retake: see [Resit/Week 6/](../../Resit/Week%206/).

**What did I find difficult, and how did I solve it?**

### Checklist
- [ ] My workshop / homework files are in `homework/`
- [ ] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

**Project title:** AI Live Coding Pulse

**My pair partner:** Benjamin van Teeseling

**Tool we had to use:** A pre-trained Hugging Face sentiment model, run with the Python transformers library

**SDG we had to address:** SDG 9, Industry, Innovation and Infrastructure

**What problem does it solve, and for whom?**
An engineering team lead at a small or medium software company needs to decide whether to try, buy or wait for AI coding tools. Tools change quickly, and opinions are spread across many comments. The lead has little time to read them all.

**What did you build?**
A tool that collects Hacker News comments about AI coding tools every 15 minutes and labels them negative, neutral or positive. A dashboard shows mood over time and lets the user open the comments behind a change. On 50 comments labelled by hand, the cardiffnlp model agreed with 35 labels, compared with 12 for VADER.

**Link to the live thing (if any):**
Project archive: [`hackathon/wetransfer_hackathon_2026-10-15_1821.zip`](hackathon/wetransfer_hackathon_2026-10-15_1821.zip). Documentation: [`hackathon/README.md`](hackathon/README.md). Slides: [`hackathon/AI Coding Pulse Hackathon 6 - Benjamin & Lili.pdf`](hackathon/AI%20Coding%20Pulse%20Hackathon%206%20-%20Benjamin%20%26%20Lili.pdf).

**How do I run it?**
The commands in [`hackathon/README.md`](hackathon/README.md) are `pip install -r requirements.txt` and `python collect.py` for collection. For the dashboard, use `pip install -r requirements-dashboard.txt` and `streamlit run dashboard.py`. The listed project archive is [`hackathon/wetransfer_hackathon_2026-10-15_1821.zip`](hackathon/wetransfer_hackathon_2026-10-15_1821.zip).

**Who did what?**
Benjamin chose the Hugging Face models, picked the topic and wrote the code with help from Claude (AI). I labelled the 50 randomised comments for the honest test and helped with the presentation.

**Ethical reflection - what are the risks of your tool? Who could it harm?**
Hacker News commenters are a technical group and do not represent all developers or the industry. A team lead could make a poor decision by treating this as a general opinion survey. The model was trained on tweets and struggles with sarcasm and mixed or mild opinions; bots were not filtered and could cause a peak. We store no usernames, but comment IDs can lead back to people’s profiles. We should store only what is needed and must not use the tool to judge individuals or as the only basis for a decision.

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
