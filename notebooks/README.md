# Customer Value Analysis and Segmentation

This is an example on how to take customer transaction data, and perform a customer value analysis on the given dataset, and cluster them into various segment. 

This is a common use case where businesses want to gain some insight into their clientele, understand different groups of customers they are dealing with, so that businesses can customise the services or campaigns to target individual groups to serve them more effectively.  

## Data
- [Online Retail Data](https://archive.ics.uci.edu/ml/datasets/online+retail) | This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers.

## Notebooks
- [data/](../.aml/data/) : contain a copy of raw data, transformed data. 
- [notebooks/](./)
    - [00-data/](./00-data/) : data exploration
    - [01-clustering/](./01-clustering/) : clustering methods
    - [02-interpretation/](./02-interpretation/)
- [models/](../.aml/models/) : contain data science and machine learning outputs e.g. models, etc.

## References
### Blog on DS/ML
- [Customer Segmentation on Online Retail Data](https://towardsdatascience.com/the-most-important-data-science-tool-for-market-and-customer-segmentation-c9709ca0b64a) | [Repo](https://github.com/optiflow/rfm-customer-segmentation)

- [Customer Segmentation on Instacart Data](https://towardsdatascience.com/customer-segmentation-using-the-instacart-dataset-17e24be9c0fe) | [Repo](https://github.com/jrkreiger/instacart-analysis)

- [Starbucks offers: Advanced customer segmentation with Python](https://seifip.medium.com/starbucks-offers-advanced-customer-segmentation-with-python-737f22e245a4) | [Repo](https://github.com/seifip/starbucks-customer-segmentation)

### Blog on Customer Analysis
- [RFM analysis for Customer Segmentation](https://clevertap.com/blog/rfm-analysis/) : Recency, Frequency, Monetary value of your customers.
- [Customer Lifetime Value: What is it and How to Calculate](https://clevertap.com/blog/customer-lifetime-value/)

### Wiki-like
- [Finding Optimum Number of Clusters](https://en.wikipedia.org/wiki/Determining_the_number_of_clusters_in_a_data_set)

- [Identifying Customer Segments](https://www.ritchieng.com/machine-learning-project-customer-segments/)

### Auto-ML for Clustering
- [Repo: Automl4Clust](https://github.com/tschechlovdev/Automl4Clust)
- [Repo: autocluster](https://github.com/wywongbd/autocluster)
