def solution(players, callings):
    players_dict = {player : i for i, player in enumerate(players)}
    
    for calling in callings:
        pre, index = players_dict[calling] - 1, players_dict[calling]
        players_dict[players[pre]], players_dict[players[index]] = index, pre
        players[pre], players[index] = players[index], players[pre]
        
    return players