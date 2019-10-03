## happy path
* greet
  - utter_greet
* mood_great
  - action_hello_world

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## tthc path
* greet
	- utter_greet
* thutuchanhchinh
	- utter_traloi_tthc
* benhvien
	- utter_traloi_benhvien
* xinviec
	- utter_traloi_xinviec
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
* goodbye
  - utter_goodbye

## benhvien path
* benhvien
	- utter_traloi_benhvien

## xinviec path
* xinviec
	- utter_traloi_xinviec
