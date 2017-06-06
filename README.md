# MI_Feature_Selection
Feature selection is an essential aspect of machine learning. When used properly it
can make classifiers more efficient and more accurate. Filter feature selection is a
category of common methods. These are classifier independent methods that use
approximations of mutual information to select a subset of features. However, these
approximations often rely on poor assumptions that are not usually true. These
assumptions can be avoided by using lower bound of mutual information instead.
This bound is calculated using an arbitrary measurable Q distribution. The closer
this Q distribution is to the data’s actual distribution, the better the bound becomes.
In this project I explore a weighted pairwise Q distribution that incorporates prior
knowledge of the data’s distribution. My experiments show a small improvement
over using un-weighted pairwise Q distributions.