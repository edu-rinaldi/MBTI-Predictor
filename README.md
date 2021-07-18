# MBTI Predictor

## What is a **MBTI**
The MBTI (Myers-Briggs Personality Type Indicator) divides everyone into **16 distinct personality** types across **4 axis**:

* Introversion (**I**) – Extroversion (**E**)
* Intuition (**N**) – Sensing (**S**)
* Thinking (**T**) – Feeling (**F**)
* Judging (**J**) – Perceiving (**P**)

This system is used in: *businesses, online, for fun, for research and lots more*.

Usually, for knowing which of the 16 personalities is closer to our one we have to answer to a questionnaire; why not automate this task?

## Learning task
Design and implement a model that given a collection of "posts" as input returns the most suited **Myers-Briggs personality type indicator (MBTI)** associated to the author.

Machine learning algorithms used for this project:
* Naive Bayes
* Linear SVC
* Logistic Regression
* Neural Network

## Google Colab or Databricks?
`MBTI.ipynb` notebook is designed to run on **Google Colab**, **BUT** setting `USING_COLAB=False` it should also run on **Databricks** (not full tested, so **Colab is reccomended**)

## Datasets
Two datasets has been used for this project:
1. MBTI Dataset ([Kaggle link](https://www.kaggle.com/datasnaek/mbti-type))
2. Reddit dataset (`datasets/reddit_mbti.parquet`)

## MBTI Dataset
This **dataset** contains over **8600 rows of data**, and on each row contains:

* **"posts"**: last 50 things a user have posted, each entry is separated by `"|||"`
* **"type"**: MBTI type

Notice that after splitting each post we will have about **430k rows**. 

**Acknowledgements:**
This data was collected through the PersonalityCafe forum; it provides a large selection of people and their MBTI personality type.


Credits to @datasnaek

## Reddit dataset
For obtaining a model with much more "generalization power" and for increasing the number of data to use during training phase I decided to collect new data and I came up with this new dataset.

It's a **PARQUET** dataset containing on each row:
* **redditor\_id**: posts' author id
* **post**: Last things the author posted; each entry is separated by "|||" (w.r.t. Mbti dataset, posts number on each entry ranges from 50 to 100)
* **text\_type**: identify if it's a comment, title or a post
* **type**: as the MBTI dataset
* **num\_post**: number of post in the row

This dataset contains 5754 records

### How data has been collected?
Data has been collected on **Reddit** using a scraper created by me (code available [here](https://github.com/edu-rinaldi/MBTI-Predictor/tree/main/scraper)).

First, I collected a list of users (and their personality) in 17 subreddits about MBTI ("r/mbti", "r/infp", ...); the personality information is given by a badge that is assigned to the user (**Reddit API** call it "author flair text").

Then, I've scraped the most recent posts of each user (max. 100 for each user) on the **ENTIRE** Reddit platform, this means that I scraped also posts not related to MBTI universe.

At the end for each post I assigned the badge (so the personality) related to the author.

## Final models
Final models that can be used are:
* `final_pipeline_202107080921`, composed by
    * **NaiveBayes model** for classifying between **I/E** type indicators, **f1-score:** 0.7414680295332422
    * **Neural Network model** for classifying between **N/S** type indicators, **f1-score:** 0.8314306227551886
    * **NaiveBayes model** for classifying between **T/F** type indicators, **f1-score:** 0.7338614509076911
    * **Neural Network model** for classifying between **P/J** type indicators, **f1-score:** 0.7301667584790412
* `final_pipeline_202107050925`, composed by
    * **Neural Network model** for classifying between **I/E** type indicators, **f1-score:** 0.744559472384674
    * **Neural Network model** for classifying between **N/S** type indicators, **f1-score:** 0.835502168084075
    * **Linear SVC model** for classifying between **T/F** type indicators, **f1-score:** 0.726088608434644
    * **Neural Network model** for classifying between **P/J** type indicators, **f1-score:** 0.72016943168465

They are both located in `pretrainedModels` folder of this repository.
