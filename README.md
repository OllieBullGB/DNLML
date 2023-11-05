# DNLML
![DNLML Logo](https://i.imgur.com/Po2ARAa.png)

### Durhack Natural-Language Machine-Learning
This project provides a framework for people with
low technical skills to utilise machine learning
algorithms by providing an automated natural language environment for building machine learning models by providing a dataset and a natural language query.

This project was created for Durhack '23, a 24 hour hackathon held annually by Durham University CompSoc in association with HackathonsUK and MLH.

If you wish to understand how the interesting part of this project works, please consult the DAML notebook

#### Example
- Dataset URL: https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data
- Query: "I want to predict whether a patient died or not"
- Process: ![Result](https://i.imgur.com/beHRvxK.jpeg)
- Result: the best trained model (LinearSVC) is pickled and then returned to the user as model.sav 

### Technology
The technology used for this project is surprisingly simple (apart from model debugging)
- Model Generation
    - ChatGPT 3.5 (Natural language pprocessing)
    - Pandas (loading of dataset files into ddataframe)
    - sklearn (model selection and training of models)
- API
    - FastAPI (API framework)
- Web Interface
    - Nuxt3

### Using the API
Because I have some credits left over from OpenAI, please feel free to use the DNLML API :)

url: <to be added after event>
- / : says Hello
- /link : processes an NLAI request with a dataset url
    - dataset_url: query
    - task: query
- /file : processes an NLAI request with a base64 encoded csv
    - dataset: body (ensure that the start 'data:text/csv;base64,' is removed from the front)
    - task: body

Both the processing routes will return the following
- type: the model that was selected as the best after tuning
- accuracy: the test accuracy of the chosen model
- url: a link to download the model as a pickle