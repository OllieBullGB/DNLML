# DNLML
![DNLML Logo](https://i.imgur.com/Po2ARAa.png)

### Durhack Natural-Language Machine-Learning
This project provides a framework for people with
low technical skills to utilise machine learning
algorithms by providing an automated natural language environment for building machine learning models by providing a dataset and a natural language query.

This project was created for Durhack '23, a 24 hour hackathon held annually by Durham University CompSoc in association with HackathonsUK and MLH.

#### Example
- Dataset URL: https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data
- Query: "I want to predict whether a patient died or not"
- Process: ![Result](https://i.imgur.com/beHRvxK.jpeg)
- Result: the best trained model (LinearSVC) is pickled and then returned to the user as model.sav 

#### Technology
The technology used for this project is surprisingly simple (apart from model debugging)
- ChatGPT 3.5 (Natural language pprocessing
- Pandas (loading of dataset files into ddataframe
- sklearn (model selection and training of models)