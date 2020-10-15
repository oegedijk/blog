---
toc: true
layout: post
description: quickly deploying explainable AI dashboards
categories: [markdown]
title: Introducing explainerdashboard
---
As data scientists working in a public or regulated sector we are under increasing pressure to make sure that our machine learning models are transparent, explainable and fair. With the advent of tools such as SHAP and LIME, the old black-box trope actually does not really apply anymore, and it has become quite straightforward to explain how each feature contributed to each individual prediction for example. However straightforward for a data scientist is not the same as straightforward for a manager, supervisor or regulator. And so what is needed is a tool that allows non-technical stakeholders to inspect the workings, performance and predictions of a machine learning model without needing to learn Python or getting the hang of Jupyter notebooks. 


With the `explainerdashboard` python package, building, deploying and sharing interactive dashboards
that allow non-technical users to explore the inner workings of a machine learning model 
can be done with just two lines of code. For example to build this example hosted at [titanicexplainer.herokuapp.com/classifier](titanicexplainer.herokuapp.com/classifier), you just to 
need to fit a model:

```python
from sklearn.ensemble import RandomForestClassifier
from explainerdashboard.datasets import titanic_survive

X_train, y_train, X_test, y_test = titanic_survive()
model = RandomForestClassifier().fit(X_train, y_train)
```

And pass it to an `Explainer` object:

```python
from explainerdashboard import ClassifierExplainer

explainer = ClassifierExplainer(model, X_test, y_test)
```

And then you simply pass this `explainer` to an `ExplainerDashboard` and run it:

```python
from explainerdashboard import ExplainerDashboard
ExplainerDashboard(explainer).run()
```

This will launch a dashboard built on top off plotly `dash` that will run on
`http://localhost:8050` by default. 



With this dashboard you can for example see which features are the most 
important to the model:

![]({ site.baseurl }}/images/explainerdashboard/tab_importances.png "importances tab")

<!-- 
Or how the model performs:

![]({{ https://explainerdashboard.readthedocs.io }}en/latest/_images/tab_model_performance.png "model performance tab")

And you can explain how each individual feature contributed to each
individual prediction:

![]({{ https://explainerdashboard.readthedocs.io }}en/latest/_images/tab_individual_predictions.png "contributions tab")

Figure out how predictions would have changed if one or more of the variables
were different:

![]({{ https://explainerdashboard.readthedocs.io }}en/latest/_images/tab_whatif.png "whatif tab")

See how feature impact predictions :

![]({{ https://explainerdashboard.readthedocs.io }}en/latest/_images/tab_feature_dependence.png "feature dependence tab")


And even inspect every decision tree inside a random forest:

![]({{ https://explainerdashboard.readthedocs.io }}en/latest/_images/tab_decision_trees.png "decisiontrees tab")




 -->








