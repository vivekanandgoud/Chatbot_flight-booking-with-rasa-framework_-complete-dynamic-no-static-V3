from rasa_core_sdk import Action
import requests
import json
import pandas as pd

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.events import UserUtteranceReverted
from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.events import Restarted

Ref_no_flight =[]
FlightsFound =[]
confm = 0
		 
class SaveOrigin(Action):
        
	def name(self):
                
		return 'action_save_origin'
		
	def run(self, dispatcher, tracker, domain):
                
		orig = (tracker.latest_message)['text']#tracker.latest_message.text#next(tracker.get_latest_entity_values("from"), None)
		print(orig)
		#if not orig:
			#dispatcher.utter_message("Please enter a valid airport code")
			#return [UserUtteranceReverted()]
		return [SlotSet('from',orig)]

class actiondefault(Action):
        
	def name(self):
                
		return 'action_default_fallback'
		
	def run(self, dispatcher, tracker, domain):
                
		#orig = (tracker.latest_message)['text']#tracker.latest_message.text#next(tracker.get_latest_entity_values("from"), None)
		#print(orig)
		#if not orig:
		dispatcher.utter_message("...>> My appologies my knowlegdge limited to flight booking only.")
			#return [UserUtteranceReverted()]
		return []
	


class SaveDestination(Action):
	def name(self):
		return 'action_save_destination'
		
	def run(self, dispatcher, tracker, domain):
		dest = (tracker.latest_message)['text']#next(tracker.get_latest_entity_values("to"), None)
		#if not dest:
			#dispatcher.utter_message("Please enter a valid airport code")
			#return [UserUtteranceReverted()]
		return [SlotSet('to',dest)]
		
		
class SaveConnection(Action):
	def name(self):
		return 'action_save_connection'
		
	def run(self, dispatcher, tracker, domain):
		conct = (tracker.latest_message)['text']#next(tracker.get_latest_entity_values("date"), None)
		print(conct)
		#if not inp:
			#dispatcher.utter_message("Please enter a valid date")
			#return [UserUtteranceReverted()]
		return [SlotSet('connection',conct)]

class SaveDate(Action):
	def name(self):
		return 'action_save_date'
		
	def run(self, dispatcher, tracker, domain):
		inp = (tracker.latest_message)['text']#next(tracker.get_latest_entity_values("date"), None)
		#if not inp:
			#dispatcher.utter_message("Please enter a valid date")
			#return [UserUtteranceReverted()]
		return [SlotSet('date',inp)]

class SaveConfirm(Action):
	def name(self):
		return 'action_save_confirm'
		
	def run(self, dispatcher, tracker, domain):
                global Ref_no_flight
                global FlightsFound
                global confm
                
                
                confm = (tracker.latest_message)['text']#next(tracker.get_latest_entity_values("date"), None)
                #Ref_no_flightq=pd.read_csv('db.csv')
                #Ref_no_flightq=list(Ref_no_flightq)
                #print(Ref_no_flightq)
                #with open('db.txt', 'r') as f:
                        #for item in Ref_no_flight:
                                #Ref_no_flightq.append(item)
                message = "\n  Booking in process......!!!!\n"
		#if not inp:
			#dispatcher.utter_message("Please enter a valid date")
			#return [UserUtteranceReverted()]
                dispatcher.utter_message(message)
                return []

class SaveId(Action):
	def name(self):
		return 'action_save_id'
		
	def run(self, dispatcher, tracker, domain):
                global Ref_no_flight
                global FlightsFound
                global confm
                
                
                ids = (tracker.latest_message)['text']#next(tracker.get_latest_entity_values("date"), None)
                #Ref_no_flightq=pd.read_csv('db.csv')
                #Ref_no_flightq=list(Ref_no_flightq)
                print(ids)
                #with open('db.txt', 'r') as f:
                        #for item in Ref_no_flight:
                                #Ref_no_flightq.append(item)
                message = "\nCongratulations **** \n Your Flight" + str(FlightsFound[int(confm)-1])+ "   Booked succesfully \n Ref.NO:"+ str(Ref_no_flight[int(confm)-1])+".\n\n"
		#if not inp:
			#dispatcher.utter_message("Please enter a valid date")
			#return [UserUtteranceReverted()]
                dispatcher.utter_message(message)
                return []
		
class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset' 	
    def run(self, dispatcher, tracker, domain): 		
        return[AllSlotsReset()]



class ActionGetFlights(Action):
        
        # Read Json File
                       

	def name(self):
		return 'action_get_Flights'

	def run(self, dispatcher, tracker, domain):
                global Ref_no_flight
                global FlightsFound
                        
                orig=tracker.get_slot('from')
                dest=tracker.get_slot('to')
                dat=tracker.get_slot('date')
                conct=tracker.get_slot('connection')
                print(orig,dest,dat,conct)             
                category = tracker.get_slot('category')
                print(category)
                print("Server initiated")
                message = str(123)

                if conct == "cheap":
                        conct = "True"
                if conct == "fast":
                        conct = "False"
                if conct == "yes":
                        conct = "True"
                if conct == "no":
                        conct = "False"
                if conct == "Yes":
                        conct = "True"
                if conct == "No":
                        conct = "False"
		
                with open('ticket.json') as ticketfile:
                        
                        #TicketList = json.load(ticketfile)
                        #try:
                        TicketList = json.load(ticketfile)
                        #except:
                            #print("no json file loaded for finding Flights")

                        #print(TicketList)
                        #print("given attributes...:",From, Tos, Dates,Connection)
                        #valu="Kochi"
                        #valu1 ="1290,432,454545,667567,32312"
                        #FlightsFound = TicketList[1]["Airlines"]
                        FlightsFound = [str(i+1) + ") " + ticket["Airlines"]  for i, ticket in enumerate(filter(lambda ticket: ticket["From"] == orig and (ticket["Connection"] == conct), TicketList))]
                        Ref_no_flight = [str(i+1) + ") " + ticket["Ref_no"]  for i, ticket in enumerate(filter(lambda ticket: ticket["From"] == orig and (ticket["Connection"] == conct), TicketList))]
                                                #Ref_no_flight = [sticket["Ref_no"]  for ticket in enumerate(TicketList)]
                        print(FlightsFound)
                        print(Ref_no_flight)
                        #Ref_no_flighta = pd.DataFrame(Ref_no_flight)
                        #Ref_no_flighta.to_csv('db.csv')
                        #with open('db.txt', 'w') as f:
                                #for item in Ref_no_flight:
                                        #f.write("%s\n" % item)
                        message = str("available flight services:\n")+"\n".join(FlightsFound)+ "\n"+str("choose the flight number to confrim\n")
                dispatcher.utter_message(message)
		#BT=input()
		
                #print("\n Congratulations **** Your Flight:"+FlightsFound[(int(BT)-1)]+"Booked succesfully.")
                return []

