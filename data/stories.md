## fallback
- utter_default

## fine_path_01
* greet
- utter_greet

## fine_path_02
* fine_ask
- utter_ask_departure

## fine_path_03
* fine_ask_departure
- action_save_origin
- utter_ask_destination

## fine_path_04
* fine_ask_destination
- action_save_destination
- utter_ask_date


## fine_path_05
* fine_ask_date
- action_save_date
- utter_ask_connection


## fine_path_06
* fine_ask_connection
- action_save_connection
- action_get_Flights



## fine_path_08
* confirmindex
- action_save_confirm
- utter_ask_id

## fine_path_09
* ask_id
- action_save_id

## fine_path_09
* fine_ask_story_1
    - utter_ask_departure
* fine_ask_story_1{"from": "delhi"}
    - action_save_origin
    - slot{"from": "delhi"}
    - utter_ask_destination
* fine_ask_story_1{"to": "chennai"}
    - action_save_destination
    - slot{"to": "chennai"}
    - utter_ask_date
* fine_ask_story_1{"date": "25-08-2019"}
    - action_save_date
    - slot{"date": "25-08-2019"}
    - utter_ask_connection
* fine_ask_story_1{"connection": "yes"}
    - action_save_connection
    - slot{"connection": "yes"}
	- action_get_Flights



# fine_path_10
* fine_ask_story_2
    - utter_ask_departure
* fine_ask_story_2{"from": "delhi","to": "chennai","date": "25-08-2019"}
    - action_save_origin
    - slot{"from": "delhi","to": "chennai","date": "25-08-2019"}
    - utter_ask_connection

## out path 1
* out_scope
-utter_outscope
	
## thanks path 1
* thanks
- utter_anything_else
