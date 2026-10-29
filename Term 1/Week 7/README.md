# Term 1 - Week 7: Computer Vision

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

**Project title:** Knotweed Checker: spot invasive Japanese knotweed from a phone photo

**My pair partner:** Jelle Schwarz

**Tool we had to use:** Roboflow

**SDG we had to address:** SDG 15, Life on Land (target 15.8: invasive alien species)

**What problem does it solve, and for whom?**
Japanese knotweed is an invasive plant that pushes out native plants and regrows from tiny root pieces. Dutch municipalities spend millions on it (Amsterdam set aside €8.2 million) and ask residents to report where it grows, but most residents cannot tell it from look-alikes such as bindweed. Our user is a resident or park volunteer in the Netherlands who sees a suspicious plant and wants to know in seconds whether to report it.

**What did you build?**
A web app where you take or upload a photo of a plant. Our Roboflow model, trained on 832 Dutch photos, says whether it is knotweed. If it is likely knotweed, the app says "don't cut it, report it"; if unsure, it asks for a closer photo. On 168 new photos from Belgium and Germany it was 93% right, with four times fewer false alarms than a general AI model (CLIP).

**Link to the live thing (if any):**
Code, slides, data card and results: [`hackathon/`](hackathon/) (start with [`hackathon/README.md`](hackathon/README.md)). Screenshot of the app answering a test photo: [`hackathon/examples/app-screenshot.jpg`](hackathon/examples/app-screenshot.jpg). The model is in our private Roboflow workspace, so we demo it live.

**How do I run it?**
In `hackathon/`: `pip install -r requirements.txt`, set `ROBOFLOW_API_KEY` and `ROBOFLOW_MODEL=knotweed-nl/1`, then `streamlit run app.py`. Full steps in [`hackathon/README.md`](hackathon/README.md).

**Who did what?**
WHO_DID_WHAT

**Ethical reflection - what are the risks of your tool? Who could it harm?**
A missed knotweed means a patch is not reported and keeps spreading. A false alarm could make someone cut or poison a harmless plant, and cutting real knotweed the wrong way spreads it. So the app never tells anyone to remove a plant, only to report it, and only says "likely knotweed" at 70% confidence or more. Our data comes from nature enthusiasts' close-up photos, so real street snapshots may do worse than our tests, and photos are sent to Roboflow's servers, so users should not photograph people or house numbers. Full data card: [`hackathon/DATA_CARD.md`](hackathon/DATA_CARD.md).

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
We expected the model to fail on young spring shoots, but when we tested it on 168 new photos from Belgium and Germany it found 27 of 30 spring plants. The real problem was somewhere else: iNaturalist's search had mixed up knotweed and bindweed, so about 70 of our photos had the wrong label before we caught it. Testing taught us more than guessing.

**Where does this connect to "AI for Good"?**
Invasive species are one of the main threats to biodiversity on land (SDG 15). A tool that helps residents report knotweed early, while warning them not to act on it themselves, uses AI to support the people who protect nature instead of replacing their judgement.
