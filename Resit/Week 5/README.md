# Resit — Week 5: Machine Learning Basics

## Workshop assignments -> [`homework/`](homework/)

**What was the assignment?**
The Week 5 workshop notebook: train a first KNN model on the breast-cancer screening data, compare it with logistic regression and decision trees (and see overfitting in a tree with no depth limit), read the confusion matrix (dangerous misses versus false alarms), the big assignment (my own classifier on the wine dataset, four models compared, confusion matrix and conclusion), and the wrap-up recipe on the Titanic data with the four 'Your turn' cells: the cheat column, tuning the tree depth, checking the model per passenger class, and putting myself on the Titanic.

**What did I hand in?**
`homework/Week5_Workshop_Lili.ipynb`: the workshop notebook with every exercise done and run
from top to bottom, including the written answers.

**What did I find difficult, and how did I solve it?**
The hardest parts of this workshop: understanding why accuracy is not enough. The "lazy" model that always says "did not survive" already scores 61%, and the KNN cancer model made 4 dangerous misses for 1 false alarm. The confusion matrix and the recall per group show what one accuracy number hides. Scaling also mattered more than expected: KNN on the wine data went from 78% to 93% just by putting the measurements on the same scale.

**AI use:** As the course allows, I used Claude (an AI assistant) for this notebook: it wrote and
ran the code and drafted the written answers. The notebook was run from top to bottom, so the
outputs you see are real.

### Checklist
- [x] My workshop / homework files are in `homework/`
- [x] Everything runs without errors
