from pyTeamSnapAPI import TeamSnapAPI

def main():

    #create TeamSnapAPI object
    api = TeamSnapAPI()

    userid = api.find_me()

    teams_I_belong = api.list_teams(userid)

    variables = ['name','id','division_name','division_id']

    # print list with specific variables only

    api.print_list(teams_I_belong,variables)

    # print list with all variables

    api.print_list(teams_I_belong)







    '''
    for team in teams_I_belong:
        print(f"Team Name: {team['name']}")
        print(f"Team Id: {team['id']}")
        print(f"Division: {team['division_name']}")
        print(f"Division ID: {team['division_id']}")
        print("======================================")

    events_list = api.list_events(teamid=8780519)
    
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
