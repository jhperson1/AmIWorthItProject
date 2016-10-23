import time
##### this program creates an applet for people to evaluate, am I worth it?

### DESIGN SIDE OF PROGRAM

## PROGRAM FUNCTIONS

# retrieve y or n response
def get_YN_response():
	
	# ask for the user's input
	print "What do you think? Type 'n' for no and 'y' for yes: "
	answer = input()
	print "\n"
	# if the user says no
	if answer == 'n' or answer == 'N':
		return 1
	# if the user says yes
	elif answer == 'y' or answer == 'Y':
		return 2
	# if the user typed the wrong letter
	else:
		print "Could you say it once more? 'n' for no, 'y' for yes: "
		get_YN_response(x)

## ---------------------------
## YN questions - WORTH
## ---------------------------
# define the number of questions
NUM_YN_QUESTIONS_WORTH = 3

# create a matrix of questions to ask and responses
prints_YN_worth = [["\n" for x in NUM_YN_QUESTIONS_WORTH] for y in 3]
# create an array to store answers
answers_YN_worth == [1 for y in NUM_YN_QUESTIONS_WORTH]

# question 1
prints_YN_worth[0][0] = "Have you smiled in public today?"
	# response to no
	prints_YN_worth[1][0] = "You’re not alone. Sounds completely normal in fact. \n" + 
						"Sounds like you’re human. [whew we can’t have robots\n" +
						"taking over the world with this applet]\n"
	# response to yes
	prints_YN_worth[2][0] = "Sometimes seeing you smile is all it takes to change \n" +
						"a strangers day. Thank you for even potentially\n " +
						"giving someone the unintentional gift of your smile\n"
# question 2
prints_YN_worth[0][1] = "Have you ever spent hours just thinking?"
	# response to no
	prints_YN_worth[1][1] = "oh okay :^)\n"
	# response to yes
	prints_YN_worth[2][1] = "Sounds like you could really help someone going \n" +
						"through something similar ... thank you for \n" +
						"even being potentially able to help a stranger \n" +
						"with a topic that you've thought about and can \n" + 
						"help them think about. \n"
# question 3
prints_YN_worth[0][1] = "Do you know that people love you?"
	# response to no
	prints_YN_worth[1][2] = "Even if you don't really know who's out there that loves you, \n" + 
						"you still touch the lives of people around you and make \n" + 
						"their lives better. Even if you don't realize it, you \n" +
						"deserve to be loved. I hope you soon see how much the \n" +
						"world loves and needs you. \n"
	# response to yes
	prints_YN_worth[2][2] = " There's something that must be magnetic and beautiful\n" +
						"about your essence ... Love is a form of enhanced \n " +
						"perception and we're lucky to have your essence here\n" + 
						"to change the lives of those who love and can't help \n" +
						"but love the magnetic essence that is you \n"

## ---------------------------
## YN questions - RESOURCES
## ---------------------------
# define the number of questions
NUM_YN_QUESTIONS_RESOURCES = 3

# create a matrix of questions to ask and responses
prints_YN_resources = [["\n" for x in NUM_YN_QUESTIONS_RESOURCES] for y in 3]
# create an array to store answers
answers_YN_resources == [1 for y in NUM_YN_QUESTIONS_RESOURCES]

# question 1
prints_YN_resources[0][0] = "Do you find that you feel more comfortable talking to?\n" + 
						"a trained peer instead of a trained adult?"
	# response to no
	prints_YN_resources[1][0] = "Okay, leaning more towards adults over peers, got it\n"
	# response to yes
	prints_YN_resources[2][0] = "Ahhh, the power of peers. Okay, understood\n"
# question 2
prints_YN_resources[0][1] = "Do you prefer anonymous texting over in person \n" +
						"conversations?\n"
	# response to no
	prints_YN_resources[1][1] = "Okay, thanks for telling us\n"
	# response to yes
	prints_YN_resources[2][1] = "Okay, thanks for telling us. Texting can be this \n" +
	 					"really great tool so you can control how much you engage \n" + 
						"with it while still getting some potential insight.\n"
# question 3
prints_YN_resources[0][1] = "Do you prefer anonymous phone calls over in person \n" +
						"conversations?\n"
	# response to no
	prints_YN_resources[1][2] = "Okay, understood!\n" + 
	# response to yes
	prints_YN_resources[2][2] = "I think anonymity can be a powerful first step \n" +
						"of potentially entering a community beyond this applet\n" +

### APPLET IMPLEMENTATION
## welcome the user
print "-----------------------\n"
print "                       \n"
print "    Am I Worth It?     \n"
print "                       \n"
print "-----------------------\n"

## introductory message
print "Hello friend! \n" +
"Welcome to Am I Worth It?. We know that you may be going through\n" + 
"some hard times and we're here to provide you with all the support \n" +
"that we can! As you move through this applet, we hope to help you \n" +
"realize your intrinsic worth and the positive impact that you make \n" +
"on the world around you. The world is truly a better place because \n" +
"you are here. We hope that you'll answer the questions truthfully \n" +
"and thoughtfully so that we can help connect you to the best \n" +
"resources to help you realize your self worth. We'll start with \n" +
"some basic questions and move forward from there.\n"

print "Ready to explore? Press any letter to continue \n"
	response = input()
clear()

## ---------------------------
## SELF WORTH SECTION
## ---------------------------

# run through yes/ no questions
for x in range(0, NUM_YN_QUESTIONS_WORTH)
	# prompt the user with a question 
	print prints_YN_worth[0][x]
	# put a little time delay so the user can read
	time.sleep(2);
	# get the user's response
	response = get_YN_response()
	# store the user's response
	answers_YN_worth[x] = response;

	## RESPOND TO THE USER'S INPUT
	# if the user says no
	if response == 1: 
		print prints_YN_worth[1][x]
	# if the user says yes
	else:
		print prints_YN_worth[2][x]

	# check when the user wants to go to the next question
	print "Ready to move forward? Press any letter when you're ready \n"
	response = input()
	# clear the screen at the end of each question
	clear()

## ---------------------------
## FINDING THE RIGHT RESOURCES
## ---------------------------

# tell the user what this section is about and if they want to do it
print "Here's a part where maybe we could find some community for you to talk to \n"
# put a little time delay so the user can read
time.sleep(3);
response = get_YN_response()

# if the user says yes
if response == 2
#### skip lines to the next section

		# run through yes/ no questions
		for x in range(0, NUM_YN_QUESTIONS_RESOURCES)
			# prompt the user with a question 
			print prints_YN_resources[0][x]
			# put a little time delay so the user can read
			time.sleep(2);
			# get the user's response
			response = get_YN_response()
			# store the user's response
			answers_YN_resources[x] = response;

			## RESPOND TO THE USER'S INPUT
			# if the user says no
			if response == 1: 
				print prints_YN_resources[1][x]
			# if the user says yes
			else:
				print prints_YN_resources[2][x]

			# check when the user wants to go to the next question
			print "Ready to move forward? Press any key when you're ready \n"
			response = input()
			# clear the screen at the end of each question
			clear()

# ask the user what college they go to
while True:
	print "Do you go to Harvard or MIT?\n"
	response = input()
	if response == "Harvard" or response or "MIT" 
	or response == "harvard" or response or "mit":
		college = response
		break
	print "Could you type it one more time? 'Harvard' or 'MIT'?"

	## ---------------------------
	## FACEBOOK MESSAGE ANALYSIS
	## ---------------------------

	# tell the user about facebook sentiment analysis and ask if they want to do it
	print "Here's a portion of this applet to allow you to analyze \n" +
			"your facebook messages. We'll look over some of your \n" +
			"interaction with people and use that to help us find. \n" +
			"some compatible resources for ya.\n"
	# put a little time delay so the user can read
	time.sleep(2);

	fb_sentiment_analysis = get_YN_response()
		# if the user says yes
		if fb_sentiment_analysis == 2
			## insert a bunch of code about running the sentiment analysis (Stanford)
		clear()

# print some appropriate resources
# eventual goal: 
	#resource_algorithm(college, answers_YN_worth, answers_YN_resources, fb_sentiment_analysis)
# note that this program only applies to MIT resources currently

print "We've found some resources that may be helpful for you in this difficult time.\n" +
		"Please feel free to look over any of them. It takes courage to even reach for\n" +
		"help, let alone stick to it. We're proud that you've made it this far and hope \n" +
		"you get a chance to check out these resources we've found.\n"
print "\n"
print "\n"

# peers/ texting
if answers_YN_resources[0] == 2 or answers_YN_resources[2] == 1:
	print "Based on your responses, we found: Lean0n.me\n"
	print "\t Lean0n.me is a texting service composed of MIT students \n" +
		"\t who have gone through some stressers in college and were \n" + 
		"\t trained to help the next line of people potentially going\n" +
		"\t through something similar.\n" 
		"\t Start with a text: \" Could you help me through a tough time\" to (646) 798-4121\n" +
		"\t and consider being an advocate, because we need people like you \n" + 
		"\t to help and empower people with your thoughts and experiences <3 \n"
# adults in person (includes if answers_YN_resources[0] == 1)
elif answers_YN_resources[2] == 1 or answers_YN_resources[3] == 1: 
	print "Based on your responses, we found: MIT Student Support Serviced (S^3)\n"
	print "\t S^3 is desiged to be a hub of support for MIT students. \n" +
		"\t Their mission statement is:  \" Whether you are struggling with a pset \n" +
		"\t because of something going on in your life, you feel too ill to take \n" +
		"\t an exam, you are considering taking time away from the Institute, \n" +
		"\t or you just don’t know who to talk to, we can help.\" \n" +
		"\t S^3 is located in building 5, Use this for some moreinfo: http://studentlife.mit.edu/s3\n"
		"\t Hours: Monday through Friday, 9:00 am to 5:00 pm\n" +
		"\t Walk-in: Monday through Friday, 10:00 am to 11:00 am and 2:00 pm to 3:00 pm\n" +
		"\t Appointments or questions: Call (617) 253-4861\n"
# adults on the phone (includes if answers_YN_resources[0] == 1)
elif answers_YN_resources[3] == 2:
	print "Based on your responses, we found: Samaritans Statewide Helpline\n" +
			"\t They're a completely volunteer based organization, with\n" +
			"\t each samaritan having a 40 hour long training course to help \n" +
			"\t them help others <3. Here's their website: http://samaritanshope.org/\n" +
			"\t Contact: (877) 870-4673 | Call or Text 24/7\n"
	print "We also found: MIT on Call Resources, but they're not anonymous if that\n" +
			"affects your decision\n"
			"\t MIT Mental Health and Counseling Clinician on Call: (617) 253-4481, nights/weekends \n" +
			"\t Dean on Call: via campus police, (617) 253-1212, nights/weekends \n" +
			"\t MIT Medical Urgent Care: (617) 253-4481 \n"


# # resources question 1
# 	# adults
# 	if answers_YN_resources[0] == 1:
# 		print "Based on your response to question 1, we found: \n" +
# 			""
# 	# peers
# 	else:
# 		print  "Based on your response to question 1, we found: \n" +
# 			""

# # resources question 2
#	# in person
# 	if answers_YN_resources[1] == 1:
# 		print  "Based on your response to question 2, we found: \n"
# 	# texting
# 	else:
# 		print "Based on your response to question 2, we found: Lean0n.me\n"
# 		print "\t Lean0n.me is a texting service composed of MIT students \n" +
# 			"\t who have gone through some stressers in college and were \n" + 
# 			"\t trained to help the next line of people potentially going\n" +
# 			"\t through something similar.\n" 
# 			"\t Start with a text: \" Could you help me through a tough time\" to (646) 798-4121\n" +
# 			"\t and consider being an advocate, because we need people like you \n" + 
# 			"\t to help and empower people with your thoughts and experiences <3 \n"

# # resources question 3
# 	# in person
# 	if answers_YN_resources[2] == 1:
# 		print  "Based on your response to question 3, we found: \n"
# 	# anonymous phone call
# 	else:
# 		print "Based on your response to question 3, we found: Samaritans Statewide Helpline\n" +
# 			"\t They're a completely volunteer based organization, with\n" +
# 			"\t each samaritan having a 40 hour long training course to help \n" +
# 			"\t them help others <3. Here's their website: http://samaritanshope.org/\n" +
# 			"\t Contact: (877) 870-4673 | Call or Text 24/7\n"


## ---------------------------
## CONCLUSION
## ---------------------------
print "All the best my friend. With love, A.D. + J.H. + J.H."

