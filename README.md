**Train Rasa NLU**
```
python -m rasa_nlu.train -c nlu_config.yml --data data/nlu.md -o models --fixed_model_name nlu --project current --verbose
```
**Run Rasa NLU**
```
python -m rasa_nlu.server --path ./models
```

**Train Rasa Core**
```
python -m rasa_core.train -d domain.yml -s data/stories.md -o models/dialogue -c policy.yml
```
**To run the custom action**
```
python -m rasa_core_sdk.endpoint --actions actions
```

**Run Rasa Core**
```
python -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml
```

**OutPut _1 **
```
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  hey chitti
Hello, cool how can i help you!.

Your input ->  help me in flight tickets
Sure. Please let me know Depature location?.

Your input ->  delhi
Sure. Please let me know destination location?.

Your input ->  chennai
Sure. Please let me know date of travel?.

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

**OutPut _2**
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


