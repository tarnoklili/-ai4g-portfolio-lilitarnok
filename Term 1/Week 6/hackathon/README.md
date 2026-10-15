# Term 1 - Week 6: Language Models

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

> Your tool and your SDG for this hackathon are announced at the **start of Friday's class**.
> Write them down here once you know them.

https://youtu.be/2r9FmJ_TJLE?si=-16TqGWuJkXBJR7N

**Project title:**
AI Live Coding Pulse

**My pair partner:**
Lili Tárnok

**Tool we had to use:**
A pre-trained sentiment model from Hugging Face (https://huggingface.co/models), run with the transformers library, as in this week's lecture. AI coding assistants (Cursor, Claude Code, Antigravity) may help you build the product around it.

**SDG we had to address:**
9 — Industry, Innovation and Infrastructure

**What problem does it solve, and for whom?**
The problem. AI coding tools (Copilot, Cursor, Claude Code and similar) change every few weeks: new models, new prices, new bugs. Opinions about them are scattered over hundreds of forum comments a day, mixed with hype and complaints. Nobody who has to decide about buying them has time to read all of that, and a single blog post or a vendor's marketing is a poor guide. The result is that tools get bought too early (and then sit unused), or too late (and the team falls behind).

The user. An engineering team lead (or tech lead / engineering manager) at a small to medium software company, for example a team of 5 to 30 developers, who:
- is responsible for the team's tools and the budget for licences per developer
- is a developer themselves or close to the work, so they can read technical comments
- is not an AI specialist and has maybe 15 minutes a week to follow this topic

Not the user: individual developers choosing a tool for themselves, or investors.

**What did you build?**
A tool that collects new Hacker News comments about AI coding tools every 15 minutes, scores each as negative, neutral or positive with a pre-trained transformer, and stores it with timestamps in data/items.csv. A dashboard shows the mood per hour or day, how many comments each point is based on, and lets the user open the comments behind any peak or dip. We also tested the model on 50 comments labelled by hand and compared it with VADER.
We would hand cardiffnlp to the team lead, because it agreed with our labels 70% of the time against 24% for VADER, which calls almost everything positive. We’d still tell them it’s wrong about 3 times in 10, especially on sarcasm and mild opinions.

Collected: 572 items over 48 hours . Mood is mostly neutral and slightly negative (about 31% negative, 51% neutral, 18% positive at the last check).

**Where is the data?**
`Term 1/Week 6/hackathon/data/`:
- `items.csv`: all collected comments with time, label and score (one row per comment, newest at the bottom).
- `to_label.csv`: the 50 comments we labelled by hand.
- `test_table.csv` (and the PDF version): our labels against cardiffnlp and VADER.

**The tool has to keep collecting for 48 hours, and we have no laptop that can stay on that long. So `.github/workflows/collect.yml` runs `collect.py` on GitHub's servers every 15 minutes and commits the new data to the repository. GitHub's built-in schedule did not start on Tuesday evening, so from about 23:00 a free timer on cron-job.org triggers the same workflow every 15 minutes. Each run looks back 2 hours from the newest stored comment, so a missed run is caught up by the next one.**

**Stream and its terms**
Hacker News comments via the public Algolia search API (no key needed), fetched every 15 minutes by `collect.py` with the keyword filter in `config.py`. The Hacker News API page states no terms of use and "currently no rate limit"; we made few requests and only read public comments. We store item id, time, text, label and score, no usernames, but the item id leads back to the Hacker News page. We first tried EV charging, but it had only about 9 relevant comments per 48 hours, so we switched to AI coding tools.

**Model card summary**
`cardiffnlp/twitter-roberta-base-sentiment-latest`: RoBERTa trained on about 124 million English tweets (2018 to 2021), labels negative, neutral, positive, licence CC-BY-4.0. Tested on 50 comments we labelled by hand: 35/50 correct (70%), against 12/50 for the word-list baseline VADER (`data/test_table.csv`). Weak on sarcasm and mild opinions, which it tends to call neutral.

**How to run**
1. `pip install -r requirements.txt`, then `python collect.py` in `Term 1/Week 6/hackathon/`.
2. Automatic: `.github/workflows/collect.yml` runs it every 15 minutes and commits the data.
3. Dashboard: `git pull`, `pip install -r requirements-dashboard.txt`, `streamlit run dashboard.py`.
4. Test: `python label_sample.py`, label the 50 items, then `python compare.py`.

**Failures of the model (cardiffnlp wrong on 15 of 50)**

In 10 of the 15 errors the model said "neutral" while we saw an opinion. Four examples:

1. **Sarcasm** (item 50079378). "That's the brilliant part! Someone is on the hook but it's not going to be upper management. When it all goes tits up, you just fire your existing dev teams, hire in 'AI-native' devs ... and try again!"
   We said negative, the model said neutral (VADER said positive). Words like "brilliant" read as praise, and the sarcasm only shows from the whole message.

2. **Praise in the words, criticism in the meaning** (item 50077645). "You also unintentionally made a very compelling argument against vibecoding and treating software as a means to an end!"
   We said negative, the model said neutral. The sentence compliments the other person, but the writer's opinion about AI coding is negative. The model scores the tone of the sentence, not the writer's stance on the topic.

3. **Negative words about someone else's view** (item 50071162). "Obviously, many people have viewed AI's contribution to programming as just producing unreliable garbage. Yes, that's an incomplete and tenuous belief ..."
   We said neutral, the model said negative. "Garbage" and "unreliable" belong to other people's opinion, which the writer partly disagrees with.

4. **Mild, implicit opinion** (item 50072672). "For that I'm slowly turning towards AI-assisted coding with some hand editing afterwards."
   We said positive, the model said neutral. There are no strongly positive words, so the model plays safe. This is the most common failure.

**Lesson for our user:** the mood line probably under-reports opinions, because mild or sarcastic comments end up as "neutral". That is why the dashboard lets the team lead open the comments behind a peak or dip and read them.

**What it must not be used for**
As a measure of what "the public" or all developers think, to identify, profile or judge individual commenters, or as the only basis for a decision.

**Link to the live thing (if any):**
https://youtu.be/2r9FmJ_TJLE?si=-16TqGWuJkXBJR7N

**Files (in `Term 1/Week 6/hackathon/`)**
- `collect.py`, `config.py`: fetch new Hacker News comments, filter them, score them with the model and store them in `data/items.csv`.
- `dashboard.py`: the view (Streamlit dashboard).
- `label_sample.py`, `compare.py`: the test: draw 50 comments to label by hand, then compare with cardiffnlp and VADER.
- `requirements.txt`, `requirements-dashboard.txt`, `requirements-analysis.txt`: what to install for the collector, the dashboard and the test.
- `count_volume.py`: helper we used to check how many comments a topic gets.
- `data/`: `items.csv` (all collected comments), `to_label.csv` (our 50 labels), `test_table.csv` (test results).
- `.github/workflows/collect.yml` (repo root): runs the collector every 15 minutes.

**Who did what?**
Benjamin chose the huggingface models and used this to pick a topic, then wrote the code assisted with Claude AI. Lili labelled the 50 randomized comments and helped with the presentation.

**Ethical reflection - what are the risks of your tool? Who could it harm?**
Not to be used to judge individual commenters, or as the only basis for a decision. Our tool only shows what Hacker News commenters say, a group that is mostly technical and not representative, so a team lead who reads it as "what the industry thinks" could decide badly. The model was trained on tweets and misreads sarcasm and mixed messages (about 70% right on our test), and we did not filter bots, which could cause a peak. The people who could be harmed are the commenters: we keep no usernames, but the item id leads back to their profile. We reduce this by storing only what we need, and by stating in the dashboard and this README that the tool must not be used to judge individuals or as the only basis for a decision.

### Checklist
- [x] Prototype code (or export / workflow file) is in `hackathon/`
- [x] This week's slides are in `hackathon/`
- [x] The prototype actually runs, and I wrote down how to run it
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
