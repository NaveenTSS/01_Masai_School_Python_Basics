# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 06:16:28 2026

@author: Naveen
"""

player_name=input("Enter Player name:")

no_of_games_played=int(input("No of games played:"))

total_score=int(input("Total Score acheived:"))

avg_score_per_game=total_score/no_of_games_played

print(f"Player: {player_name}\nGames Played: {no_of_games_played}\nTotal Score: {total_score}\nAverage Score: {avg_score_per_game}")
