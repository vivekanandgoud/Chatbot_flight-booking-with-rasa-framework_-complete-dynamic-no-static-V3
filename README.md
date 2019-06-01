**Train Rasa NLU**
```
python -m rasa_nlu.train -c nlu_config.yml --data data/nlu.md -o models --fixed_model_name nlu --project current --verbose
```

```
2019-06-02 01:03:19 INFO     rasa_nlu.model  - Starting to train component SpacyNLP
2019-06-02 01:03:20 INFO     rasa_nlu.model  - Finished training component.
2019-06-02 01:03:20 INFO     rasa_nlu.model  - Starting to train component SpacyTokenizer
2019-06-02 01:03:20 INFO     rasa_nlu.model  - Finished training component.
2019-06-02 01:03:20 INFO     rasa_nlu.model  - Starting to train component SpacyFeaturizer
2019-06-02 01:03:20 INFO     rasa_nlu.model  - Finished training component.
2019-06-02 01:03:20 INFO     rasa_nlu.model  - Starting to train component RegexFeaturizer
2019-06-02 01:03:20 INFO     rasa_nlu.model  - Finished training component.
2019-06-02 01:03:20 INFO     rasa_nlu.model  - Starting to train component CRFEntityExtractor
2019-06-02 01:03:20 INFO     rasa_nlu.model  - Finished training component.
2019-06-02 01:03:20 INFO     rasa_nlu.model  - Starting to train component EntitySynonymMapper
2019-06-02 01:03:20 INFO     rasa_nlu.model  - Finished training component.
2019-06-02 01:03:20 INFO     rasa_nlu.model  - Starting to train component SklearnIntentClassifier
Fitting 2 folds for each of 6 candidates, totalling 12 fits

[Parallel(n_jobs=1)]: Done  12 out of  12 | elapsed:    0.1s finished
2019-06-02 01:03:20 INFO     rasa_nlu.model  - Finished training component.
2019-06-02 01:03:20 INFO     rasa_nlu.model  - Successfully saved model

```

**Run Rasa NLU**
```
python -m rasa_nlu.server --path ./models
```

**Train Rasa Core**
```
python -m rasa_core.train -d domain.yml -s data/stories.md -o models/dialogue -c policy.yml
```

```
Epoch 94/100
612/612 [==============================] - 0s 111us/sample - loss: 0.2292 - acc: 0.9412
Epoch 95/100
612/612 [==============================] - 0s 111us/sample - loss: 0.1965 - acc: 0.9444
Epoch 96/100
612/612 [==============================] - 0s 111us/sample - loss: 0.1761 - acc: 0.9461
Epoch 97/100
612/612 [==============================] - 0s 111us/sample - loss: 0.1919 - acc: 0.9428
Epoch 98/100
612/612 [==============================] - 0s 111us/sample - loss: 0.1653 - acc: 0.9575
Epoch 99/100
612/612 [==============================] - 0s 111us/sample - loss: 0.2010 - acc: 0.9330
Epoch 100/100
612/612 [==============================] - 0s 98us/sample - loss: 0.2160 - acc: 0.9314
2019-06-02 01:03:34 INFO     rasa_core.policies.keras_policy  - Done fitting keras policy model
**To run the custom action**
```
python -m rasa_core_sdk.endpoint --actions actions
```

**Run Rasa Core**
```
python -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml
```

**OutPut_1**

```
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  hey bot
Hello, cool how can i help you!.

Your input ->  movie
.....>> My appologies my knowlegdge limited to flight booking only.

Your input ->  give me mobiles info
.....>> My appologies my knowlegdge limited to flight booking only.
```


**OutPut_2**
```
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  hey chitti
Hello, cool how can i help you!.

Your input ->  i just want to book flight tickets from delhi to chennai
Sure. Please confirm the  Depature location?.

Your input ->  delhi
Sure. Please  confirm the  destination location?.

Your input ->  chennai
Sure. Please  confirm the  date of travel?.

Your input ->  25/08/2019
please choose connection flight Yes or No?

Your input ->  yes
available flight services:
1) Air Asia
2) Chennai Airlines
3) Delhi Airlines
choose the flight number to confrim


Your input ->  2

  Booking in process......!!!!

please enter your ID proof No. to continue?

Your input ->  A123456

Congratulations ****
 Your Flight2) Chennai Airlines   Booked succesfully
 Ref.NO:2) 123678640HLF99980012.


Your input ->
```

**OutPut _3**
```
Your input ->  hello chitti
Hello, cool how can i help you!.

Your input ->  flight shedule
Sure. Please let me know Depature location?.

Your input ->  bangalore
Sure. Please let me know destination location?.

Your input ->  tirupathi
Sure. Please let me know travel date?

Your input ->  24/08/2019
please choose connection flight Yes or No?

Your input ->  yes
available flight services:
1) Balaji Airlines
2) Indigo Airlines
choose the flight number to confrim


Your input ->  1

  Booking in process......!!!!

please enter your ID No.?

Your input ->  A123456

Congratulations ****
 Your Flight1) Balaji Airlines   Booked succesfully
 Ref.NO:1) 12323233245,8686867,86867867,24235345.


Your input ->
```


