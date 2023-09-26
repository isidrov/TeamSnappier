from pyTeamSnapAPI import TeamSnapAPI

def main():

    # Create an instance of the TeamSnapAPI class
    api = TeamSnapAPI()

    # Find my own user's ID
    userid = api.find_me()
    print(f"My user ID is: {userid}")

    # Return Teams I belong
    teams_I_belong = api.list_teams(userid)

    '''
    # Print Teams with all its variables
    print(f"Printing Teams I belong:")
    print(f"************************")
    api.print_list(teams_I_belong)
    '''
    
    # Print Teams with specific variables only
    variables = ['name','id','division_name','division_id']
    print(f"Printing Teams I belong:")
    print(f"************************")
    api.print_list(teams_I_belong,variables)

    # Obtain Events scheduled in a team
    events_list = api.list_events(teamid=8780519)

    '''
    # Print Events with all its variables
    print(f"Printing Events:")
    print(f"************************")
    api.print_list(events_list)
    '''
    # Print Events with specific variables
    variables = ['name', 'location_name', 'id', 'type','is_game']
    api.print_list(events_list,variables)

    '''
    for event in events_list:
        print(f"Event Name: {event['name']}")
        print(f"Event Id: {event['id']}")
        print(f"Location: {event['division_name']}\tDivision ID: {team['division_id']}")
        print("\n")
    '''

    


    #events_list = api.list_events(userid=userid)

    '''
    events_list = api.list_events(userid)
    api.write_to_json_file(events_list, filename='events_list.json')
    search_user(userid)
    teams_I_belong = api.list_teams(userid)
    '''


    # ... [Include other operations here in the same manner]
    # ...

if __name__ == "__main__":
    main()
