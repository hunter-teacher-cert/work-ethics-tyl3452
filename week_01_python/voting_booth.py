#mrliu voting booth project
#not done, the algo to recount needs to be finished

#global variable of save list of votes
#Ham sandwich 
#Tuna fish sandwich 
#cucumber sandwich 
#pizza sandwich 
# initialize with initial test votes
# changed each vote to be a dictionary
list_of_votes = [{'ham': 1,'tuna': 2, 'cucumber': 3, 'pizza': 4},
                 {'ham': 2,'tuna': 4, 'cucumber': 1, 'pizza': 3},
                 {'ham': 4,'tuna': 1, 'cucumber': 2, 'pizza': 3},
                 {'ham': 1,'tuna': 3, 'cucumber': 2, 'pizza': 4},
                 {'ham': 4,'tuna': 1, 'cucumber': 2, 'pizza': 3}]

# global variable to save vote tally of first place votes
vote_results = {
    'ham': 0,
    'tuna': 0,
    'cucumber': 0,
    'pizza': 0
}

#reset global vote_results
def reset_tally():
    global vote_results
    vote_results = {
        'ham': 0,
        'tuna': 0,
        'cucumber': 0,
        'pizza': 0
    }

#tally the global vote_results using input parameter votes
def tally_votes(votes):
    global vote_results
    # tally all first place votes
    for vote in votes:
        if(vote['ham'] == 1):
            vote_results['ham'] += 1
        elif(vote['tuna'] == 1):
            vote_results['tuna'] += 1
        elif(vote['cucumber'] == 1):
            vote_results['cucumber'] += 1
        elif(vote['pizza'] == 1):
            vote_results['pizza'] += 1
        else:
            print('Error in tally votes')
    return

# takes one voter's ranked vote and adds it to list of votes
def voting_booth(votes):
    vote = {
        'ham': 0,
        'tuna': 0,
        'cucumber': 0,
        'pizza': 0
    }
    
    print('Rank the candidates listed below. Separate each rank by a space, e.g. 1 2 3 4')
    print('Ham, Tuna, Cucumber, Pizza')
    user_input = input()
    #print('testing user_input', user_input)

    # set vote to temp dictionary vote{} 
    temp_list = user_input.split()
    vote['ham'] = (int(temp_list[0]))
    vote['tuna'] = (int(temp_list[1]))
    vote['cucumber'] = (int(temp_list[2]))
    vote['pizza'] = (int(temp_list[3]))

    #add vote to list_of_votes
    votes.append(vote)
    
    return

# prints out all votes
# in raw dictionary form is ok for now
def display_votes(votes):
    for vote in votes:
        print(vote)
    return


# prints out who wins
# :return who the winner, TIE, or NOWIN
def check_winner(results):

    # check for winner - who has the most first place votes
    winner = ''
    winner_vote_total = 0
    vote_count = 0
    for candidate, votes in results.items():
        if(votes > winner_vote_total):
            winner_vote_total = votes
            winner = candidate
        elif(votes == winner_vote_total):
            winner = 'TIE'
        vote_count += 1

    # check and print out the winner
    # if no winner, print out top choice or TIE
    if(winner_vote_total/vote_count > 0.50):
        print('***', winner, '*** is the winner with',
              winner_vote_total, 'out of',vote_count,
              'total votes,', winner_vote_total/vote_count)
        return winner
    elif(winner == 'TIE'):
        print('It\'s a TIE!')
        return 'TIE'
    else:
        print('***', winner, '*** is top choice with',
              winner_vote_total, 'out of',vote_count,
              'total votes,', winner_vote_total/vote_count,
              'is not over the 50% threshold.!')
        return 'NOWIN'


# main algo to calculate results
# :param list_of_votes to tally results
# :param vote_results to store the tally
def calc_results(votes, vote_results):

    reset_tally()
    tally_votes(votes)
    check_winner(vote_results)
    return


# display vote result tally
def display_results(results):
    for candidate, votes in results.items():
        print(candidate, ':', votes)
    return


# main program
# menu to start off program
user_choice = 0
temp_list_of_votes = []

# loop menu until user wants to exit
while(user_choice != 5):
    print('Welcome to the Sandwich Voting Booth')
    print('1 - Vote for your sandwiches')
    print('2 - Display all raw votes')
    print('3 - Calculate winner winner chicken dinner')
    print('4 - Reset Vote tally')
    print('5 - EXIT')
    user_choice = int(input("Enter number of your choice:"))

    # branch to appropriate function form user choice
    if(user_choice == 1):
        voting_booth(list_of_votes)
        display_votes(list_of_votes)
    elif(user_choice == 2):
        display_votes(list_of_votes)
    elif(user_choice == 3):
        # copy list of votes
        for vote in list_of_votes:
            temp_list_of_votes.append(vote)
        calc_results(temp_list_of_votes, vote_results)
        display_results(vote_results)
    elif(user_choice == 4):
        reset_tally()
        display_results(vote_results)
    elif(user_choice == 5):
        print('EXIT TIME, BYE! Vote early, vote every time')
    else:
        print('Invalid input')


