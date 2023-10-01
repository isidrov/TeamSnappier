from TeamSnappier import TeamSnapAPI

def main():

    # Create an instance of the TeamSnapAPI class
    api = TeamSnapAPI()

    # Return a list with a dict with all about myself
    myself = api.find_me()

    # Print relevant information about myself
    variables = ['email', 'id', 'first_name', 'last_name','managed_division_ids']
    api.print_list(myself, variables)
    
    # Obtain user_id and division_id
    user_id = myself[0]['id']
    managed_division_id = myself[0]['managed_division_ids'][0]

    # Print division details
    division = api.list_divisions(divisionid=managed_division_id)
    variables = ['name', 'id', 'league_url']
    api.print_list(division, variables)

    #List division locations
    division_locations = api.list_division_locations(divisionid=managed_division_id)
    variables = ['id', 'name']
    api.print_list(division_locations, variables)

    # Export locations
    api.json_to_csv(division_locations,'division_locations_exported.csv')

    # Print Teams I belongwith specific variables only
    teams_I_belong = api.list_teams(userid=user_id)
    variables = ['name','id','division_name','division_id']
    api.print_list(teams_I_belong,variables)

    # Find my team_id
    my_team_id = ''
    for team in teams_I_belong:
        if team['name'] == 'Edel. Volunteer (test) Team':
            my_team_id = team['id']
    
    # Export opponents of my team
    opponents = api.list_opponents(teamid=my_team_id)
    api.json_to_csv(opponents, 'opponents_exported.csv')

    # Bulk opponents
    api.create_opponents('bulk_opponents.csv')


    Print('test')

    # Create an event
    #api.create_event('schedule_game_template_2.csv')

    # {'href': 'https://api.teamsnap.com/v3/division_locations', 'rel': 'division_locations'}
    # {'href': 'https://api.teamsnap.com/v3/locations', 'rel': 'locations'}
    # {'href': 'https://api.teamsnap.com/v3/opponents', 'rel': 'opponents'}

    # Obtain Events scheduled in a team
    events_list = api.list_events(teamid=8780519)

    api.json_to_csv(events_list,'my_events_file.csv')


    # Print Events with all its variables

    api.print_list(events_list)


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
