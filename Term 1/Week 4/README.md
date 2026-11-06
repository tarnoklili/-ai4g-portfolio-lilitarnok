# Term 1 - Week 4: Strings, Text & Files

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**
The Week 4 workshop notebook: cleaning one piece of feedback with string methods, counting words
across responses (a "bag of words", with stopwords), writing and reading a file with `with open()`,
and the big assignment **Community Feedback Analyzer**: read a file of citizen feedback, clean,
split and count the words, and write a report with the number of responses, the average words
per response, the top 5 keywords and the urgent responses.

**What did I hand in?**
- `homework/Week4_Workshop_Lili.ipynb`: the workshop notebook with every exercise and both
  reflections, run from top to bottom.
- `homework/community_feedback.txt`: the made-up feedback file the analyzer reads (12 responses).
- `homework/feedback_report.txt`: the report it writes. The report also has a mood score and the
  numbers people mentioned. The notebook additionally runs a word search.

**What did I find difficult, and how did I solve it?**
Punctuation: without stripping `.,!?:;` from every word, `"great,"` and `"great"` count as two
different words. Deciding what counts as "urgent" was harder than the code: my four
words miss a serious message that does not use them, which is what the reflection is about.

**AI use:** As the course allows, I used Claude (an AI assistant) for this notebook: it wrote and
ran the code and drafted the written answers. The notebook was run from top to bottom, so the
outputs you see are real.

### Checklist
- [x] My workshop / homework files are in `homework/`
- [x] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

**Project title:** Urban Heat — Make Room for Nature

**My pair partner:** Luuk Aalders (assigned pair)

**Tool we had to use:** ComfyUI (node-based Stable Diffusion image and video generation)

**SDG we had to address:** SDG 13, Climate Action

**What problem does it solve, and for whom?**
Students who live or study in Dutch cities may spend time in hot, paved streets with little shade. The film aims to help them understand why shade and greenery matter in public spaces. This audience choice has not been tested with students.

**What did you build?**
A short film with six AI-generated shots. Two students move from a hot, exposed space to a shaded bench. We used ComfyUI to turn starting images and motion prompts into clips, then assembled the clips in a separate video editor.

**Link to the live thing (if any):**
Project details: [`hackathon/README.md`](hackathon/README.md). Workflow exports: [`hackathon/Text to image model Minor copy.json`](hackathon/Text%20to%20image%20model%20Minor%20copy.json), [`hackathon/Background mask model.json`](hackathon/Background%20mask%20model.json) and [`hackathon/Image to video generator minor copy.json`](hackathon/Image%20to%20video%20generator%20minor%20copy.json). Slides: [`hackathon/Urban_Heat_Presentation.pptx`](hackathon/Urban_Heat_Presentation.pptx).

**How do I run it?**
Use a local ComfyUI installation with Wan 2.2 support and a compatible GPU. Import [`hackathon/Image to video generator minor copy.json`](hackathon/Image%20to%20video%20generator%20minor%20copy.json), select the required models and add a starting image and prompts. See [`hackathon/README.md`](hackathon/README.md) for the model names and generation steps.

**Who did what?**
_(Lili: one sentence on how you and Luuk split the work.)_

**Ethical reflection - what are the risks of your tool? Who could it harm?**
Realistic AI scenes could be mistaken for footage of a real place or heatwave. We avoided named locations and temperature claims, and the characters are fictional, but we still need a visible AI-generated label. Dry leaves do not prove climate change, and shade does not solve the wider urban heat problem. Repeated generation used computing resources; one render took about an hour. We did not measure electricity use, so we cannot claim a low environmental impact. We reused starting images, should record the total generations and avoid unnecessary rerenders. We have not tested whether the film improves understanding.

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
