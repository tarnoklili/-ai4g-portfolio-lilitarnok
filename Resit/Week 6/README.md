# Resit — Week 6: Language Models

## Workshop assignments -> [`homework/`](homework/)

**What was the assignment?**
The Week 6 workshop notebook: word embeddings (similarity, neighbours, a word map, analogies and the
stereotype they carry), order and memory (the RNN vs LSTM memory test, and pushing the LSTM to 50
words), transformers (one word with different meanings in context, where sentiment analysis fails,
next-word prediction, temperature, and the she/he bias after job titles), and the big individual
assignment: stress-test the sentiment model for one context. I chose feedback on a university's
student-support service, with a 14-sentence test set, error analysis, a bias probe and a written
judgement.

**What did I hand in?**
`homework/Week6_Workshop_Lili.ipynb`: the workshop notebook with every exercise done and run
from top to bottom, including all predictions, answers and the big assignment.

**What did I find difficult, and how did I solve it?**
The hardest parts of this workshop: predicting results before running a cell (several predictions were wrong: the LSTM remembered better than expected, and the typo sentence was read correctly), and explaining *why* a sentence fails and which step of the ladder would help. Some failures, like sarcasm about a five-week wait, need knowledge about the world, not only better language skills. The in-class activities (Contexto with a neighbour, the telephone game, "be attention") were answered from the activity descriptions, because I missed that class.

**AI use:** As the course allows, I used Claude (an AI assistant) for this notebook: it wrote and
ran the code and drafted the written answers. The notebook was run from top to bottom, so the
outputs you see are real.

### Checklist
- [x] My workshop / homework files are in `homework/`
- [x] Everything runs without errors
