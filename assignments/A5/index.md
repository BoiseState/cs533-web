# Assignment 5

:::{updated} F22
:::

This assignment is designed to develop and assess your ability to build classifiers and reason about
their effectiveness. You will use SciKit-Learn classifiers; it is possible to do part of the
assignment with statsmodels, but some of the models only exist in SciKit-Learn.

It is due **{date}`wk11 sun xlong` at 11:59 pm**.
Submit your notebook and its PDF export to {{LMS}}.

Throughout your writeup, **justify your decisions** based on theoretical knowledge, the background
reading, or what you observe in the data.

:::{tip}
Read the **entire assignment** before beginning.
:::

## Revision Log

- **Nov. 9** (for future reference): corrected reference to XGB class.
- **Nov. 2:** corrected lasso regression to specify `l1` instead of `lasso`, and
  point to the documentation on solvers.

## Context and Data

For this assignment, you will work with a data set of loans issued to small businesses, provided by the U.S. Small Business Administration.
We used a version of this data for an in-class activity earlier in the semester.

For more details on the data and its history, read [“Should This Loan be Approved or Denied?” A Large Dataset with Class Assignment Guidelines](https://doi.org/10.1080/10691898.2018.1434342) by Li, Mickel, and Taylor, published 2018 in the Journal of Statistics Education. The paper and data set are open-access under the Creative Commons Attribution license.

I have based this assignment on their class exercise.
You will be working with the full SBA National data set.
I have attached the data file to the {{LMS}} assignment.

Your goal in this assignment is to predict whether or not the business will pay off their loan.
This is recorded in the ``MIS_Status`` field, which is ‘PIF’ if the loan is paid in full and ‘CHGOFF’ if the borrower defaulted (the loan was charged off).
The Loan Documentation file contains more information about fields in the database; this is also in Table 1(a) in the paper, along with additional descriptions of some of the variables.
We are going to treat **paid in full as the positive class**: the goal is to predict 1 if the loan is likely to be paid off.  A logistic regression, therefore, is computing the log odds of complete payment.

The NAICS field indicates the industry sector of the business.
The first two digits are the broad sector (and progressively more specific sectors are indicated by more digits).
The [North American Industry Classification System](https://www.census.gov/cgi-bin/sssd/naics/naicsrch?chart=2012) provides the meanings of the first 2 digits.

## Feature Engineering

This data set will require some cleaning and manipulation to have usable features.
Some things you will likely need to do include:

- Convert the outcome variable into usable form for prediction.
- Convert other categorical variables into appropriate dummy or indicator variables.
- Bin some features. For example, the authors recommend looking at whether the term is at least 240 months to determine if a transaction is backed by real estate or not (longer-term loans are backed by real estate).
- Convert date fields into more usable form (Pandas date-time features let you parse them and convert them).  For example, you may want only the year.
- Compute interaction features or derived features.  For example, you may want to compute the fraction of the loan that was guaranteed by the SBA and use it as a feature.

Note that one of the fields is the chargeoff amount.  **Do not use this field as a feature** — why is this?

:::{ltip} Time
If you convert the disbursement date to a Pandas datetime, and the term to a Pandas {py:class}`pandas.tseries.offsets.DateOffset`, you can use them to get the loan end time. You might be able to do useful things with that and the dates of the Great Recession (Dec. 1, 2007 to June 30, 2009).
:::

Some features are likely not useful, at least in their current form.
You may want to design additional features based on your own exploration.P

Please feel free to discuss useful features or transformations on Piazza, but implement and describe the features you use from that yourself (or with your partner).

## Presenting Work

I expect you will need to do quite a bit of experimentation with different features and models in order to complete this assignment.

I do **not** want you to just present all of that in sequence in your final submission — it will be very difficult to read such a submission.

What will be far more effective is to *summarize*, and to build your final model (and maybe 1–2 exemplary intermediate models).  Things that you should include in such a summary:

* A description of your feature engineering process. How did you design features? How did you assess them?
* A list of the features you are using, with a brief justification for each.  This can be a bullet list of the features with a short sentence about why it is a useful feature.
* A list of features you tried that didn't work.  Again, can be a bullet list.

This will make it significantly easier for me to see the key pieces of your result.

As noted in the [notebook guide](../../resources/notebook-checklist.md), there are, in general, two ways to get to this:

- Build a big exploratory notebook, then clean it up (after saving a backup copy!).
- Build a big exploratory notebook, then create a new notebook and copy over the pieces that worked into a coherent order.

I do both, depending on the project and on how messy my exploratory notebook is.

If you want to submit your exploratory notebook as a separate file, that's fine (encouraged, even!), but I need the PDF of your final cleaned one to grade.

## Data Prep and Exploration (20%)

1.  Load the data and do your initial preparation.  How many observations and variables do you have?
2.  Select a 25% sample of the data for use in testing.
3.  Describe the distribution of the outcome variable.  What is the majority class?
4.  What is the accuracy, precision, and recall of the majority-class classifier on the test data?
5.  Identify some variables that, based on your understanding and reading (e.g. the source paper!) are likely to be useful for predicting default.  Describe them, your motivation, their distribution, and their relationship to outcomes (in the training data).  Do feature transformations you find useful here as well.  You may need to create interaction features, or do other feature transformations.

:::{admonition} Class Imbalance
:class: note

You will see that the classes on this data set are quite imbalanced.  Some propose resampling to
make the classes balanced for training.  If you want to consider that, think about: is such a classifier
being evaluated on the original problem?  Can you correct it to evaluate on the original problem?
:::

:::{admonition} Missing Data
:class: warning

Treat missing data with care in this assignment.  You may wish to drop or impute
(either a default value or a mean), depending on the feature.  Do **not** just call `dropna`,
because this will throw away a lot of instances! Only discard an instance if you actually
can't use it.
:::

## Subset Model (20%)

**Subset** your training and test data to only include data from California, for
business with NAICS codes starting with 53 (Real Estate and Rental and Leasing).
This mirrors the subsetting used in the source material assignment.

Build a logistic regression model using no more than 5 features to predict
default on this subset. Likely useful features include whether it is a new
business, a real estate transaction, the proportion guaranteed by SBA, and
whether it was active during the recession.

If you want to experiment with different features, create a tuning set that is a
subset of the training set, and use it to evaluate the accuracy of your model
with them. Test the final accuracy of one model on the test data using the
accuracy metric.

## Full Model (20%)

Extend your model from the subset data set (California/53) to the full data set.
Do you need to add state & industry terms? Do you need to use interaction terms?
Are there additional features that are useful?

Use a tuning set to make these decisions. Test one model from this section on
the test data.

:::{note}
For this and the other logistic regression sections, spend some time looking for
good features, but **time-box it**: use the best model you can create in a few
hours.  It's very hard to get logistic regression to demonstrate particularly strong
performance on this data set.
:::

## Regularized Regression (15%)

Use a lasso regression (``penalty='l1'`` in {py:class}`LogisticRegression <sklearn.linear_model.LogisticRegression>`) to train a model with many features and automatically select the most useful ones.
Use either a tuning set or {py:class}`sklearn.linear_model.LogisticRegressionCV` to select a useful value for there regularization strength (``C``).

:::{note}
{py:class}`~sklearn.linear_model.LogisticRegression` supports multiple different *solvers*. The default solver does not support L1 regression.
Look at its documentation to see how to change the solver to one that supports L1 regression.
:::

Note that while lasso regression will automatically *select* features, it can only work with the features you give it — you still need to transform data into useful form for influencing the predictor.

Also extend from Lasso to ElasticNet (``penalty='elasticnet'``, you will also need ``solver='saga'``; if you use {py:class}`sklearn.linear_model.LogisticRegressionCV`, you will need to pass it a list of L1 ratios as well as ``C`` values).

You might want to experiment with some more or different features on a tuning set!

Test **two** model from this section on the test data: one with lasso regression and one with ElasticNet.

## Random Forest (10%)

Let's now try a different type of classifier: a **random forest** ({py:class}`sklearn.ensemble.RandomForestClassifier`).
Consider trying different hyperparameters, such as the number of estimators, with some tuning data or with SciKit-Learn's cross-validation ({py:class}`~sklearn.model_selection.GridSearchCV`).  You may want to
include features you excluded from the logistic regression — random forests are able to make good use of a wide range 
of feature types without much need for transformation.

Test **one** random forest model on the test data.

## XGBoost (5%)

[XGBoost]: https://xgboost.readthedocs.io/

Finally, try an [XGBoost][] classifier.  It is similar to a random forest, but
it uses a different mechanism for building its decision trees.  The
{py:class}`xgboost.XGBClassifier` class provides an implementation of XGBoost
that works exactly like a SciKit-Learn model.  You will first need to install
the `py-xgboost` package from Conda or the `xgboost` package with `pip`.

Test **one** XGBoost model on the test data.

## Final Summary and Reflection (10%)

To wrap up, show the relative performance of your different models on the test data in a single chart (a bar chart or dot plot).
Do so with the following metrics:

- Accuracy
- Precision
- Recall / Sensitivity
- Specificity

Accuracy counts false positives and false negatives as equal errors, but in reality they do not have the same cost.
Compute the **cost** of each classifier by assigning a cost of 5 to a false positive (classified as a good risk but defaulted), 1 to a false negative, and 0 to correct classifications.
Show the cost of your different models in an appropriate chart.

The last analysis is to show overall the *false negative rate* for your different models.
After showing the overall FNR, break down the false positive rate and the
precision by business status, and show each model's FNR and precision for new
and existing businesses separately (I recommend a bar charts with model on the X
axis, FNR or precision on the y, and different bar colors for new and existing
businesses).
Does your model perform comparably well for new and existing businesses?

:::{note}
Disaggregating performance by business status may seem random, but it is important for something we will discuss after the assignment.
:::

Write 2-3 paragraphs about what you learn about your model performance and the usefulness of different features.

## Expected Time

These time estimates do **not** include compute time for hyperparameter search
with cross-validation.  Some of those runs can take an hour or two, depending on
your computer capacity.

- Data Prep and Exploration: 1.5 hours
- Subset Model: 1.5 hours (iterating with exploration for more features on the tune data)
- Full Model: 1.5 hours (iterating with exploration for more features on the tune data)
- Lasso Regression: 30 minutes
- ElasticNet: 30 minutes
- Random Forest: 1 hour
- xgboost: 30 minutes (reuse random forest effort)
- Summary, Reflection, and Cleanup: 2.5 hours
