# Data Science Portfolio - Costa Kleoni
A collection of work from personal projects, academic coursework, and Kaggle competitions.  

[Web Applications](https://github.com/ckleoni/portfolio/blob/master/README.md#web-applications) &nbsp; | &nbsp; [Web Scraping](https://github.com/ckleoni/portfolio/blob/master/README.md#web-scraping) &nbsp; | &nbsp; [Data Preprocessing](https://github.com/ckleoni/portfolio/blob/master/README.md#data-preprocessing) &nbsp; | &nbsp; [Regression](https://github.com/ckleoni/portfolio/blob/master/README.md#regression) &nbsp; | &nbsp; [Classification](https://github.com/ckleoni/portfolio/blob/master/README.md#classification) &nbsp; | &nbsp; [Clustering](https://github.com/ckleoni/portfolio/blob/master/README.md#clustering)       
[Association Rule Learning](https://github.com/ckleoni/portfolio/blob/master/README.md#association-rule-learning) &nbsp; | &nbsp; [Reinforcement Learning](https://github.com/ckleoni/portfolio/blob/master/README.md#reinforcement-learning) &nbsp; | &nbsp; [Natural Language Processing](https://github.com/ckleoni/portfolio/blob/master/README.md#natural-language-processing) &nbsp; | &nbsp; [Deep Learning](https://github.com/ckleoni/portfolio/blob/master/README.md#deep-learning)      
[Dimensionality Reduction](https://github.com/ckleoni/portfolio/blob/master/README.md#dimensionality-reduction) &nbsp; | &nbsp; [Model Selection & Boosting](https://github.com/ckleoni/portfolio/blob/master/README.md#model-selection--boosting) &nbsp; | &nbsp; [Simulation](https://github.com/ckleoni/portfolio/blob/master/README.md#simulation) &nbsp; | &nbsp; [Actuarial Science](https://github.com/ckleoni/portfolio/blob/master/README.md#actuarial-science)         

Web Applications
------
* **Worldwide Earthquake Forecaster - Predicting earthquakes in real time and visualizing results in Google Maps**  
*Python (NumPy, Matplotlib, pandas, scikit-learn, XG Boost), HTML, Google Maps, Flask, PythonAnywhere*  
This project includes exploring an earthquake dataset, applying geo-based and rapid mapping techniques, applying feature engineering and aggregation techniques, fitting XG Boost model to predict likelihood of earthquakes at future dates, building a local Flask web application using an HTML slider and Google Maps, and uploading web application to Python Anywhere.  
[View Web App](http://ckleoni.pythonanywhere.com/) | [View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Worldwide_Earthquake_Forecaster.ipynb) | [View Code: main.py](https://github.com/ckleoni/portfolio/blob/master/Projects/WEF_main.py) | [View Code: HTML](https://github.com/ckleoni/portfolio/blob/master/Projects/WEF.html)

Web Scraping
------
* **eSports Earnings - Compiling eSports player annual earnings, by game title, game series, and game genre**  
*Python (Scrapy, NumPy, Matplotlib, pandas)*  
This project includes developing two spiders to crawl a website and compile total eSports player earnings year over year, and by game title, game series, and game genre. There is also a Jupyter notebook that explores this dataset and determines which games/genres are most profitable.  
[View Code: Spider 1](https://github.com/ckleoni/portfolio/blob/master/Projects/game_earnings.py) | [View Code: Spider 2](https://github.com/ckleoni/portfolio/blob/master/Projects/game_genres.py) | [View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/eSports_Earnings.ipynb)

Data Preprocessing
------
* **Data Preprocessing - Standard Example**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook briefly walks through how to import libraries, import a dataset, explore a dataset, handle missing data, handle categorical features, divide data into training/test sets, and scale features.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Data_Preprocessing.ipynb)

Regression
------
* **Simple Linear Regression - Predicting salary based on years of experience**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use Simple Linear Regression to predict Salary based on Years of Experience and visualize results of our training and test set predictions.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Simple_Linear_Regression.ipynb)  

* **Multiple Linear Regression - Predicting profit based on R&D spend, administration, marketing spend, and location**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use Multiple Linear Regression to predict Profit based on R&D Spend, Administration, Marketing Spend, and State, handle categorical data, removing dummy variable, and calculate Root Mean Squared Error to evaluate model performance.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Multiple_Linear_Regression.ipynb)  

* **Polynomial Regression - Predicting salary based on position level**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use Polynomial Regression to predict Salary based on Position Level and visualize and compare results to Simple Linear Regression model.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Polynomial_Regression.ipynb)  

* **Support Vector Regression - Predicting salary based on position level**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use Support Vector Regression to predict Salary based on Position Level and visualize results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Support_Vector_Regression.ipynb)  

* **Decision Tree Regression - Predicting salary based on position level**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use Decision Tree Regression to predict Salary based on Position Level and visualize results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Decision_Tree_Regression.ipynb)  

* **Random Forest Regression - Predicting salary based on position level**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use Random Forest Regression to predict Salary based on Position Level and visualize results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Random_Forest_Regression.ipynb)  

Classification
------
* **Logistic Regression - Predicting likelihood of purchase based on age and estimated salary**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use Logistic Regression to predict likelihood of Purchase based on their Age and Estimated Salary, view accuracy via Confusion Matrix, and visualize results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Logistic_Regression.ipynb)  

* **K-Nearest Neighbors - Predicting likelihood of purchase based on age and estimated salary**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use K-Nearest Neighbors to predict likelihood of Purchase based on Age and Estimated Salary, view accuracy via Confusion Matrix, and visualize results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/K_Nearest_Neighbors.ipynb)  

* **Support Vector Machine - Predicting likelihood of purchase based on age and estimated salary**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use a Support Vector Machine to predict likelihood of Purchase based on Age and Estimated Salary, view accuracy via Confusion Matrix, and visualize results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Support_Vector_Machine.ipynb)  

* **Kernel Support Vector Machine - Predicting likelihood of purchase based on age and estimated salary**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use a Kernel Support Vector Machine to predict likelihood of Purchase based on Age and Estimated Salary, view accuracy via Confusion Matrix, and visualize results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Kernel_Support_Vector_Machine.ipynb)  

* **Naive Bayes - Predicting likelihood of purchase based on age and estimated salary**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use Naive Bayes to predict likelihood of Purchase based on Age and Estimated Salary, view accuracy via Confusion Matrix, and visualize results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Naive_Bayes.ipynb)  

* **Decision Tree Classification - Predicting likelihood of purchase based on age and estimated salary**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use Decision Tree Classification to predict likelihood of Purchase based on Age and Estimated Salary, view accuracy via Confusion Matrix, and visualize results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Decision_Tree_Classification.ipynb)  

* **Random Forest Classification - Predicting likelihood of purchase based on age and estimated salary**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use Random Forest Classification to predict likelihood of Purchase based on Age and Estimated Salary, view accuracy via Confusion Matrix, and visualize results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Random_Forest_Classification.ipynb)  

Clustering 
------
* **K-Means Clustering - Clustering customers based on annual income and spending scores**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use K-Means Clustering to Cluster Customers based on Annual Income and Spending Scores, use elbow method to determine optimal number of clusters, and visualize results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/K_Means_Clustering.ipynb)  

* **Hierarchical Clustering - Clustering customers based on annual income and spending scores**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use Hierarchical Clustering to Cluster Customers based on Annual Income and Spending Scores, use a dendogram to determine optimal number of clusters, and visualize results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Hierarchical_Clustering.ipynb)  

Association Rule Learning
------
* **Apriori - Determining purchasing relationship between grocery items**  
*Python (NumPy, Matplotlib, pandas, apyori)*  
This notebook illustrates how to use Apriori to determinine purchasing relationship between grocery items and view results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Apriori.ipynb)  

* **Eclat - Determining purchasing relationship between grocery items**  
*R (arules)*  
This notebook illustrates how to use Eclat to determinine purchasing relationship between grocery items and view results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Eclat.pdf)  

Reinforcement Learning
------
* **Upper Confidence Bound - Optimizing ad click through rate**  
*Python (NumPy, Matplotlib, pandas, math)*  
This notebook illustrates how to use Upper Confidence Bound to optimize Ad Click Through Rate and visualize ad selections.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Upper_Confidence_Bound.ipynb)  

* **Thompson Sampling - Optimizing ad click through rate**  
*Python (NumPy, Matplotlib, pandas, random)*  
This notebook illustrates how to use Thompson Sampling to optimize Ad Click Through Rate and visualize ad selections.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Thompson_Sampling.ipynb)  

Natural Language Processing
------
* **Natural Language Processing - Predicting if a review is positive or negative**  
*Python (NumPy, Matplotlib, pandas, scikit-learn, Natural Language Toolkit, Regular expression)*  
This notebook illustrates how to use Natural Language Processing to predict if a review is positive or negative, clean text data, create Bag of Words model, fit Naive bayes to training set, and view accuracy via Confusion Matrix.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Natural_Language_Processing.ipynb)  

Deep Learning
------
* **Artificial Neural Network - Predicting customer churn rate at a financial institution**  
*Python (NumPy, Matplotlib, pandas, scikit-learn, Keras)*  
This notebook illustrates how to implement an Artificial Neural Network to predict Customer Churn Rate at a Financial Institution, encode categorical data, scale features, initialize/compile/fit multi-layer Artificial Neural Network, and view accuracy via Confusion Matrix.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Artificial_Neural_Network.ipynb)  

* **Convolutional Neural Network - Classifying images of cat and dogs**  
*Python (Keras)*  
This notebook illustrates how to implement a Convolutional Neural Network to classify images of cats and dogs, initialize/compile/fit multi-layer Convolutional Neural Network, and apply Convolution/Pooling/Flattening/Full Connection.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Convolutional_Neural_Network.ipynb) 

Dimensionality Reduction
------
* **Principal Component Analysis - Extracting new independent variables from wine dataset to classify customer segments**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use Principal Component Analysis to extract new independent variables from wine dataset to classify customer segments, fit Logistic Regression model based on new independent variables, view accuracy via Confusion Matrix, and visualize results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Principal_Component_Analysis.ipynb)  

* **Linear Discriminant Analysis - Extracting new independent variables from wine dataset to classify customer segments**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use Linear Discriminant Analysis to extract new independent variables from wine dataset to classify customer segments, fit Logistic Regression model based on new independent variables, view accuracy via Confusion Matrix, and visualize results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Linear_Discriminant_Analysis.ipynb)  

* **Kernel Principal Component Analysis - Extracting new independent variables to predict likelihood of purchase based on age and estimated salary**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use Principal Component Analysis to extract new independent variables to predict likelihood of Purchase based on Age and Estimated salary, fit Logistic Regression model based on new independent variables, view accuracy via Confusion Matrix, and visualize results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Kernel_Principal_Component_Analysis.ipynb)  

Model Selection & Boosting
------
* **k-Fold Cross Validation - Testing accuracy of Kernel Support Vector Machine model**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use k-Fold Cross Validation to test accuracy of a Kernel Support Vector Machine model, view accuracy via Confusion Matrix, and visualizing results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/k_Fold_Cross_Validation.ipynb)  

* **Grid Search - Determining best model and best parameters of a Kernel Support Vector Machine**  
*Python (NumPy, Matplotlib, pandas, scikit-learn)*  
This notebook illustrates how to use Grid Search to determine best model and best parameters of a Kernel Support Vector Machine, view accuracy via Confusion Matrix, and visualizing results.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Grid_Search.ipynb) 

* **XG Boost - Predicting customer churn rate for a financial institution**  
*Python (NumPy, Matplotlib, pandas, scikit-learn, XGBoost)*  
This notebook illustrates how to use XG Boost to predict Customer Churn Rate for a Financial Institution, encode categorical data, scale features, view accuracy via Confusion Matrix, and apply k-Fold Cross Validation to show model accuracy.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/XG_Boost.ipynb) 

Simulation
------
* **Airport Security Simulation - Determine optimal number of ID check stations and personal scanners to reduce wait times to under 15 minutes**  
*Python (SimPy, NumPy, random)*  
This notebook illustrates how to use SimPy to simulate Airport Security and determine optimal number of ID Check Stations and Personal Scanners to reduce wait times to under 15 minutes.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Airport_Security_Simulation.ipynb)  

Actuarial Science
------
* **Insurance Premium Calculator - Calculating insurance premium using chain ladder method for loss development**  
*Python (NumPy, pandas)*  
This notebook illustrates how to use Chain Ladder method for loss development to calculate insurance premium.  
[View Notebook](https://github.com/ckleoni/portfolio/blob/master/Projects/Insurance_Premium_Calculator.ipynb)  
