from header_factions import *
# from module_constants import * #

from compiler import *
####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", 0.1),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x888888),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

  ("culture_1",  "{!}culture_1", 0, 0.9, [], []),
  ("culture_2",  "{!}culture_2", 0, 0.9, [], []),
  ("culture_3",  "{!}culture_3", 0, 0.9, [], []),
  ("culture_4",  "{!}culture_4", 0, 0.9, [], []),
  ("culture_5",  "{!}culture_5", 0, 0.9, [], []),
  ("culture_6",  "{!}culture_6", 0, 0.9, [], []),
  ("culture_7",  "{!}culture_7", 0, 0.9, [], []),
  ("culture_8",  "{!}culture_8", 0, 0.9, [], []),
  ("culture_irregulars",  "{!}culture_irregulars", 0, 0.9, [], []),
  ("culture_throd",  "{!}culture_throd", 0, 0.9, [], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.01),("mountain_bandits", -0.05),("forest_bandits", -0.05),("cannibals", -0.05),("mutants", -0.05),("infected", -0.05),
  ], [],
  0xE12126), #changed name so that can tell difference if shows up on map

###
  ("kingdom_1",  "Entenaii Empire", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)],[],
  0xcc0000), #dark_red
###
  ("kingdom_2",  "Entenaii Dominion",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)],[],
  0x744800), #brown_red
###
  ("kingdom_3",  "Kingdom of Galvae", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)],[],
  0x553089), #purple
###
  ("kingdom_4",  "Molvat-Berchav Union",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)],[],
  0x5b5b5b), #dark_grey
###
  ("kingdom_5",  "Vitzland Territories",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)],[],
  0x38761d), #dark_green
###
  ("kingdom_6",  "Trezzo Republic",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)],[],
  0xffe599), #white_gold
###
  ("kingdom_7",  "Itami Castedom",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)],[],
  0x3333FF), #blue
###
  ("kingdom_8",  "Barshide Confederacy",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)],[],
  0x64bc8e), #cyan
###
  ("irregulars",  "Irregulars",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.1),("mountain_bandits", -0.05),("forest_bandits", -0.05)],[],
  0x000000), #black
###
  ("theocracy",  "Theocracy of Throd",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.1),("mountain_bandits", -0.05),("forest_bandits", -0.05),("mutants", 0.30),("infected", 0.30),],[],
  0xFF0088), #pink

################
##Barbed Wire###
################
##Entenaii Empire
##Entenaii Dominion
##Kingdom of Galvae
##Molvat-Berchav Union
##Vitzland Territories
##Trezzo Republic
##Itami Castedom
##Barshide Confederacy
##Irregulars
##Theocracy of Throd
##Other

###
  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),
  
  ("robber_knights",  "Robber_Knights", 0, 0.1, [], []),

  ("khergits","Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], []),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x888888),
  ("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
  ("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),

  ("slavers","Slavers", 0, 0.1, [], []),

  ("cannibals", "Cannibals", max_player_rating(-30)|ff_always_hide_label, 0.0, [
      ("commoners", -0.6),
      ("outlaws", -0.6),
      ("player_faction", -0.15),
      ("kingdom_1", -0.15),
      ("kingdom_2", -0.15),
      ("kingdom_3", -0.15),
      ("kingdom_4", -0.15),
      ("kingdom_5", -0.15),
      ("kingdom_6", -0.15),
      ("kingdom_7", -0.15),
      ("irregulars", -0.15),
      ("theocracy", -0.15),
      ("manhunters", -0.6),
      ("deserters", -0.15),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
      ("slavers", -0.6),
      ("mutants", -0.15),
      ("infected", -0.15),
  ], [], 0x888888),

  ("church","Church Extremists", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),

  ("infected", "Infected", max_player_rating(-30)|ff_always_hide_label, 0.0, [
      ("commoners", -0.6),
      ("outlaws", -0.6),
      ("player_faction", -0.15),
      ("kingdom_1", -0.15),
      ("kingdom_2", -0.15),
      ("kingdom_3", -0.15),
      ("kingdom_4", -0.15),
      ("kingdom_5", -0.15),
      ("kingdom_6", -0.15),
      ("kingdom_7", -0.15),
      ("irregulars", -0.15),
      ("theocracy", 0.30),
      ("manhunters", -0.6),
      ("deserters", -0.15),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
      ("slavers", -0.6),
      ("mutants", 0),
      ("cannibals", -0.15),
  ], [], 0xFF0088),  #pink alt:E2007C
  ("mutants", "Mutants", max_player_rating(-30)|ff_always_hide_label, 0.0, [
      ("commoners", -0.6),
      ("outlaws", -0.6),
      ("player_faction", -0.15),
      ("kingdom_1", -0.15),
      ("kingdom_2", -0.15),
      ("kingdom_3", -0.15),
      ("kingdom_4", -0.15),
      ("kingdom_5", -0.15),
      ("kingdom_6", -0.15),
      ("kingdom_7", -0.15),
      ("irregulars", -0.15),
      ("theocracy", 0.30),
      ("manhunters", -0.6),
      ("deserters", -0.15),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
      ("slavers", -0.6),
      ("infected", 0),
      ("cannibals", -0.15),
  ], [], 0xFF0088),   #pink alt:E2007C
  ("undeads","Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("peasant_rebels","Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","Noble Refugees", 0, 0.5,[], []),
]

##diplomacy start+ Define these for convenience
dplmc_factions_begin = 1 #As mentioned in the notes above, this is hardcoded and shouldn't be altered.  Deliberately excludes "no faction".
dplmc_non_generic_factions_begin = [x[0] for x in enumerate(factions) if x[1][0] == "merchants"][0] + 1
dplmc_factions_end   = len(factions)
##diplomacy end+
# modmerger_start version=201 type=4
try:
    component_name = "factions"
    var_set = { "factions":factions,"default_kingdom_relations":default_kingdom_relations, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
