# Week 2 — Description ({date}`wk2 range`)

:::{updated} F21
:::

The learning outcomes for this week are:

- To load a data file into Pandas and describe its basic structural characteristics.
- To identify the type of a variable and descriptive statistics appropriate to it.
- To describe the distribution of a variable numerically and visually.
- To describe how data was collected.
- To reason about limitations of the collection of data.

This week's material uses chapters 5 and 10 of {book}`p4da`.

## {{moverview}} Content Overview

:::{module} week2
:folder: 054cd8f5-5bbc-4050-b792-ad9000ef9fca
:::

## {{mcal}} Deadlines

- Week 2 quiz at **8am on Thursday**

## {{mvideo}} Describing Data

This video introduces the week's topic: describing data and data sets.
We discuss the pipeline by which phenomena become a data set.

:::{video}
:id: b0f572b6-cc0c-41ec-adee-ad9000efd57c
:length: 6m27s
:slide-id: 495979F9A431DDB0%2172971
:slide-auth: AGb5_joj5Xdvfk0
:name: 2-1 - Describing Data
:::

## {{mdoc}} What is a Dataset?

:::{reading}
:url: https://blog.ldodds.com/2013/02/09/what-is-a-dataset/
:title: What is a Dataset?
:length: 1950 words
:::

Read [What is a Dataset?](https://blog.ldodds.com/2013/02/09/what-is-a-dataset/) by Leigh Dodds.
This article looks at how the term ‘data set’ is defined by different communities, and the common themes to these definitions.

This article does reference some concepts we haven't yet gotten to.
For example, when they talk about whether the data has been labeled for a particular task, they are referring to labels we would use for a prediction or classification task, which we will discuss in a few weeks when we talk about regression and classification.
Don't feel like you need to understand every concept in this article in your first read; understand what you can, and we'll return to it.

## {{mdownload}} MovieLens Data

Download the [MovieLens 25M Dataset](https://grouplens.org/datasets/movielens/).  The Zip file is 250MB, and the files take about 1.2GB uncompressed.

You can use the smaller 20M or `latest-small` versions for practice if you want to play with a smaller version.

I will be using this dataset in the demo notebooks for this week.

:::{admonition} Data Citation
Harper, F. M. and Konstan, J. A. (2015) ‘The MovieLens Datasets: History and Context’, <cite>ACM Transactions on Interactive Intelligent Systems</cite>, 5(4), pp. 19:1–19:19.
DOI [10.1145/2827872](http://dx.doi.org/10.1145/2827872).

This paper is **not** an assigned reading — it is here for your information.
:::

## {{mvideo}} Pandas Basics

In this video, I introduce Pandas and the Pandas `DataFrame` data structure.
We see how to load a CSV file and inspect the resulting data frame.

:::{video}
:id: d6054cf9-e3dc-4f1e-8d4e-ad9000efd604
:length: 8m26s
:name: 2-2 - Pandas Basics
:::

### Resources

* [Notebook](2-2-PandasBasics.ipynb) (used for slides as well)
* Textbook section 5.1

## {{mvideo}} Variables and Types

In this video, we learn the different types of data (_variables_) that we will encounter.

:::{video}
:id: afc96ff2-0043-4387-af9b-ad9000efd6b0
:length: 15m56s
:slide-id: 495979F9A431DDB0%2172975
:slide-auth: AEdM3U338m0PRso
:name: 2-3 - Variables and Types
:::

:::{note}
In this video, I present categorical and ordinal variables as **fixed** and **finite**. While this describes any
categorical and ordinal variables you are likely to encounter, this is not strictly speaking correct.  It is
possible for a categorical or ordinal variable to be (countably) infinite.
:::

### Resources

* [Palmer Penguins data set](https://github.com/allisonhorst/palmerpenguins)

## {{mdoc}} Datasheets for Datasets

:::{reading} datasheets
:url: https://arxiv.org/abs/1803.09010
:title: Datasheets for Datasets
:length: 4100 words
:::

Read [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) by Timnit Gebru et al.

## {{mbook}} Textbook Chapters

This week's material uses chapters 5 and 10 of {book}`p4da`.
We aren't getting to everything in those chapters though.

## {{mvideo}} Groups and Aggregates

In this video, we discuss how compute aggregate statistics in Pandas.

:::{video} group-aggregate
:id: 4c5b7bbb-dc57-4484-b160-ad9000efd740
:length: 14m12s
:slide-id: 495979F9A431DDB0!72980
:slide-auth: APZCbpVCLFI74-U
:name: 2-4 - Groups and Aggregates
:::

### Resources

- [Notebook for this video](2-4-AggregatesAndGroups.ipynb)
- Textbook 10.1–10.2

## {{mvideo}} Descriptive Statistics

In this video, we discuss descriptive statistics for numeric variables.

:::{video} descriptive-statistics
:id: fd7d2c53-752b-4844-9919-ad9000efd7f2
:length: 16m32s
:slide-id: 495979F9A431DDB0%2172978
:slide-auth: AF4pIDEqeSJMSR8
:name: 2-5 - Descriptive Statistics
:::

### Terms

This video introduces the following terms:

- {term}`mean`
- {term}`median`
- {term}`standard deviation`
- {term}`variance`

## {{mvideo}} Describing Distributions

This video introdues the concept of _distributions_, and how we can see the shape and layout of our data.

:::{video}
:id: 5b6fb252-cd60-478b-aaf7-ad9000efd8b9
:length: 10m17s
:slide-id: 495979F9A431DDB0%2172985
:slide-auth: AFKFlxWtifklVVE
:name: 2-6 - Describing Distributions
:::

### Resources

- [Notebook](2-6-DescribingDistributions.ipynb)

## {{mvideo}} Data Sources and Bias

:::{video}
:id: 824f231f-7cda-42a5-917c-ad9000efd981
:length: 8m46s
:slide-id: 495979F9A431DDB0%2172983
:slide-auth: AAJ1g0hwAUBmF1c
:name: 2-7 - Data Sources and Bias
:::

### Resources

- Olteanu, Alexandra and Castillo, Carlos and Diaz, Fernando and Kiciman, Emre, Social Data: Biases, Methodological Pitfalls, and Ethical Boundaries (December 20, 2016). <cite>Frontiers in Big Data</cite> 2:13. doi: [10.3389/fdata.2019.00013](https://dx.doi.org/10.3389/fdata.2019.00013), Available at SSRN: <http://dx.doi.org/10.2139/ssrn.2886526>

## {{mquiz}} Week 2 Quiz

The Week 2 quiz will be over the material **above** this point.

## {{mvideo}} Codings and Encodings

This video talks more about how data is encoded, and what we need to document about that.

:::{video} encodings
:name: 2-8 - Codings and Encodings
:length: 8m57s
:::

### Resources

- [float.exposed](https://float.exposed/0x3dcccccd) - explore floating-point numbers

## {{mnotebook}} Tutorial Notebooks

The [tutorial notebooks](../../resources/tutorials/index.md) contain more info on the Python code, including more systematic overviews of the different Python and Pandas features.
I recommend you particularly pay attention to the [Python and Data](python-and-data) tutorials.

**We will not get to all Pandas features you might need in videos.**
These notebooks, the {book}`p4da` textbook, and the [Pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html) all provide additional information on Pandas, NumPy, and SciPy.

## {{mtask}} Practice

In a few videos, I have used the *Palmer Penguins* data set.

- Download {download}`../resources/data/penguins.csv` (provided under CC-0)
- Look at the documentation and references in the [source repository](https://github.com/allisonhorst/palmerpenguins)
- Describe the distributions of the different variables numerically and graphically
- See how many questions from *Datasheets for Datasets* you can find answers to in the penguin data documentation

For more practice, you can look at the paper for the MovieLens data and try to answer Datasheets questions for it too!

## {{massignment}} Assignment 1

Start working on [Assignment 1](../../assignments/A1/index.md).  It is due at the end of Week 3.
