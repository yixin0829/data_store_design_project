# data_store_design_project

## Problem Statement 
Design part of the sub-system for a data store of hate-speech-related content and allow social media platforms to match against this content.

## Notes (define terminologies)
- **misinformation**: information against reality dur to errors
- **hate speech**: public speech that expresses hate or encourages violence towards a person or group based on something such as race, religion, sex, or sexual orientation (Cambridge Dictionary)
- **ground truth**: desirable answer data for training your system (some may NOT be "true")
- **BERT**: Bidirectional Encoder Representations from Transformers

## Research & Workflow
- Choose a sub-problem to focus
- Research state of the art
- Research tools needed
- Code

### Sub-problem & Assumption
- Data collection and preprocessing: how do we obtain high-quality data(string text in this case) and how do we filter out ambiguity
    - As user reports may not always be accurate and data may depend on amount of users that one platform has, It would be useful to include both user self reports and selectively analysis in high-risk content genres/topics (e.g. COVID-19 related content these day to provent abusive comments on Asian-Americans).
    - **Tools needed**:bs4, selenium, pandas, .csv
- Design a classifier to determine which picece of information is hate speech ONLY
    - **Tools needed**:pandas, numpy, sklearn(logistic regression), .csv, NLP

## How to Run
- Run data_collection.py would scrap comments from Youtube comment session and write into a .csv file (issue exists)
- Then run nlp.py will preprocess the text data 
- logistic_model.py is used to train a classifier that can classify if a comment is hate speech or not 



