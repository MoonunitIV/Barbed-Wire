from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

from compiler import *
####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id.
#   11.2) Number of troops in this stack.
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
# pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small
pf_village = pf_is_static|pf_hide_defenders|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(-22.11, 55.28),[(trp_player,1,0)]), #[swycartographr] prev. coords: (-22.48, 70.18) #[swycartographr] prev. coords: (-4.82, 53.95) #[swycartographr] prev. coords: (4.54, 55.87) #[swycartographr] prev. coords: (-45.04, 66.99)
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(9.78,1.61),[]),                               #[swycartographr] prev. coords: (0, 0) #[swycartographr] prev. coords: (0.44, 1.14)
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(13.02,7.16),[(trp_temp_troop,3,0)]),        #[swycartographr] prev. coords: (1, 1)
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(24.09,13.24),[]),                         #[swycartographr] prev. coords: (0, 0) #[swycartographr] prev. coords: (23.62, 17.63)
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.45,12.17),[]),                        #[swycartographr] prev. coords: (1, 1) #[swycartographr] prev. coords: (-170.25, 55.78) #[swycartographr] prev. coords: (-1.12, 1.23)
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.55,31.12),[]),                        #[swycartographr] prev. coords: (1, 1)
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.23,42.45),[]),                        #[swycartographr] prev. coords: (1, 1)
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.2,15.73),[]),                          #[swycartographr] prev. coords: (1, 1) #[swycartographr] prev. coords: (1.81, 7.84) #[swycartographr] prev. coords: (1.79, 13.03)
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.12,-1.81),[]),                         #[swycartographr] prev. coords: (1, 1)
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.52,-23.92),[]),                              #[swycartographr] prev. coords: (1, 1)
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.31,-25.34),[]),                       #[swycartographr] prev. coords: (1, 1)
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.44,-26.76),[]),                       #[swycartographr] prev. coords: (1, 1)
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.62,-28.84),[]),                              #[swycartographr] prev. coords: (1, 1)
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.9,-30.21),[]),                                #[swycartographr] prev. coords: (1, 1)
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.83,-31.69),[]),                                #[swycartographr] prev. coords: (1, 1)

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.52,4.64),[]),                    #[swycartographr] prev. coords: (1, 1)
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.35,-19.99),[]),                     #[swycartographr] prev. coords: (1, 1) #[swycartographr] prev. coords: (-0.96, -6.64)
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.45,-26.71),[]),                  #[swycartographr] prev. coords: (1, 1) #[swycartographr] prev. coords: (-2.69, -9.54)

  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.41,-32.94),[]), #ganimet hesaplari icin #new: #[swycartographr] prev. coords: (1, 1)
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.76,-12.25),[]), #new:                #[swycartographr] prev. coords: (1, 1)

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

###############################################################
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.5,66.32),[]), #[swycartographr] prev. coords: (18, 60) #[swycartographr] prev. coords: (12.74, 45.3) #[swycartographr] prev. coords: (12.14, 43.07)
#########
##TOWNS##
#########

#Aberstwyth = Entenaii Dominion (Capital)
  ("town_1","Aberstwyth",  icon_map_dominion_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-251.55, 72.24),[], 229),               #[swycartographr] prev. coords: (-94.88, 54.99)
#Ivorstead = Entenaii Empire  
  ("town_2","Ivorstead",     icon_map_entenaii_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.59, 40.24),[], 120),                    #[swycartographr] prev. coords: (3.1, 107.69) #[swycartographr] prev. coords: (-108.17, 53.09)
#Bracklewhyte = Entenaii Dominion  
  ("town_3","Bracklewhyte",   icon_map_dominion_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-286.34, 34.06),[], 80),                    #[swycartographr] prev. coords: (-132.68, 53.01)
#Plkovice = Molvat-Berchav Union  
  ("town_4","Plkovice",     icon_map_union_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(209.75, 281.36),[], 290),                     #[swycartographr] prev. coords: (-127.86, 151.85) #[swycartographr] prev. coords: (127.25, 260.79)
#Todmorden = Entenaii Dominion  
  ("town_5","Todmorden",  icon_map_dominion_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-206.77, 283.54),[], 90),                       #[swycartographr] prev. coords: (-237.91, 105.52) #[swycartographr] prev. coords: (-225.73, 115.88)
#Millhallow = Entenaii Empire (Capital)  
  ("town_6","Millhallow",   icon_map_entenaii_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.54, -19.36),[], 228),          #[swycartographr] prev. coords: (68.18, 62.51)
#Canthagen = Entenaii Empire  
  ("town_7","Canthagen",   icon_map_entenaii_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-177.54, -19.01),[], 200),              #[swycartographr] prev. coords: (52.98, 138.47)
#Castellalvano = Trezzo Republic (Capital)
  ("town_8","Castellalvano", icon_map_republic_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-170.93, -216.81),[], 321),           #[swycartographr] prev. coords: (16.87, -74.7) #[swycartographr] prev. coords: (-171.94, -210.63)
#T ir an Tsioraiocht = Kingdom of Galvae  
  ("town_9","Tir an Tsioraiocht",   icon_map_galvae_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(143.27, -195.27),[], 333),     #[swycartographr] prev. coords: (-20.33, -10.42) #[swycartographr] prev. coords: (143.61, -144.84)
#Sely = Molvat-Berchav Union (Capital)
  ("town_10","Sely",   icon_map_union_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.59, 72.31),[], 222),                      #[swycartographr] prev. coords: (-35.62, 188.6) #[swycartographr] prev. coords: (124.65, 90.5)
#Gerarissa = Trezzo Republic  
  ("town_11","Gerarissa",  icon_map_republic_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-142.42, -299.15),[], 352),            #[swycartographr] prev. coords: (43.58, -13.44) #[swycartographr] prev. coords: (-145.37, -299.16)
#Murlayfield = Entenaii Dominion  
  ("town_12","Murlayfield", icon_map_dominion_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-192.8, 143.63),[], 25),                      #[swycartographr] prev. coords: (-147.86, 26.19) #[swycartographr] prev. coords: (-198.31, 142.9)
#Bolorence = Trezzo Republic  
  ("town_13","Bolorence",icon_map_republic_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-238.44, -183.56),[], 246),                      #[swycartographr] prev. coords: (44.8, -40.24) #[swycartographr] prev. coords: (-245.86, -183.42)
#Luninmyel = Molvat-Berchav Union  
  ("town_14","Luninmyel",  icon_map_union_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.09, 166.16),[], 82),                #[swycartographr] prev. coords: (-6.91, 164.62)
#Domhan Geal = Kingdom of Galvae  
  ("town_15","Domhan Geal",  icon_map_galvae_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(142.31, -61.13),[], 349),            #[swycartographr] prev. coords: (-6, 72.61) #[swycartographr] prev. coords: (123.23, -80.69)
#Mag Suaimhnis = Kingdom of Galvae (Capital)
  ("town_16","Mag Suaimhnis",  icon_map_galvae_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(196.24, -35.51),[], 182),        #[swycartographr] prev. coords: (-69.54, 30.21)
#Stastok = Molvat-Berchav Union  
  ("town_17","Stastok",  icon_map_union_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(307.23, -19.48),[], 90),                    #[swycartographr] prev. coords: (-58.36, 97.26) #[swycartographr] prev. coords: (282.88, -0.7)
#Gammonguard = Entenaii Empire
  ("town_18","Gammonguard",  icon_map_entenaii_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-224.28, 22.09),[], 16),              #[swycartographr] prev. coords: (120.6, 175.29)
#Helhoven = Vitzland Territories (Capital)
  ("town_19","Helhoven", icon_map_vitzland_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.45, -180.75),[], 98),                  #[swycartographr] prev. coords: (-181.22, 136.08) #[swycartographr] prev. coords: (29.55, -181.73)
#Altenkirchen = Vitzland Territories  
  ("town_20","Altenkirchen", icon_map_vitzland_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.07, -123.06),[], 270),             #[swycartographr] prev. coords: (-218.19, 159.73)
#Hoogsel = Vitzland Territories  
  ("town_21","Hoogsel", icon_map_vitzland_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.76, -117.93),[], 330),                 #[swycartographr] prev. coords: (-179.35, 105.81)
#Kreuzbach = Vitzland Territories  
  ("town_22","Kreuzbach", icon_map_vitzland_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.73, -156.11),[], 225),               #[swycartographr] prev. coords: (-138.47, 80.43)
#Rixcester = Entenaii Dominion
  #("town_23","Rixcester",  icon_map_dominion_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.24, 232),[], 229),               #[swycartographr] prev. coords: (-94.88, 54.99) #[swycartographr] prev. coords: (-240.55, 60.24)
#
  #("town_24","Tarrin",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.24, 232),[], 229),               #[swycartographr] prev. coords: (-94.88, 54.99) #[swycartographr] prev. coords: (-240.55, 60.24)
#
  #("town_25","Monmouth",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.24, 232),[], 229),               #[swycartographr] prev. coords: (-94.88, 54.99) #[swycartographr] prev. coords: (-240.55, 60.24)
#
  #("town_26","Bredwardine",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.24, 232),[], 229),               #[swycartographr] prev. coords: (-94.88, 54.99) #[swycartographr] prev. coords: (-240.55, 60.24)
#
  #("town_27","Glenarm",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.24, 232),[], 229),               #[swycartographr] prev. coords: (-94.88, 54.99) #[swycartographr] prev. coords: (-240.55, 60.24)
#
  #("town_28","Durrwich",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.24, 232),[], 229),               #[swycartographr] prev. coords: (-94.88, 54.99) #[swycartographr] prev. coords: (-240.55, 60.24)
#
  #("town_29","Aberuthven",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.24, 232),[], 229),               #[swycartographr] prev. coords: (-94.88, 54.99) #[swycartographr] prev. coords: (-240.55, 60.24)
#Zalchik = Molvat-Berchav Union
  #("town_30","Zalchik",  icon_map_union_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.24, 232),[], 229),               #[swycartographr] prev. coords: (-94.88, 54.99) #[swycartographr] prev. coords: (-240.55, 60.24)
#Moknovci = Molvat-Berchav Union
  #("town_31","Moknovci",  icon_map_union_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.24, 232),[], 229),               #[swycartographr] prev. coords: (-94.88, 54.99) #[swycartographr] prev. coords: (-240.55, 60.24)
#Pescadena = Trezzo Republic
  #("town_32","Pescadena",  icon_map_republic_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.24, 232),[], 229),               #[swycartographr] prev. coords: (-94.88, 54.99) #[swycartographr] prev. coords: (-240.55, 60.24)
#Domhan Briomhar = Kingdom of Galvae
  #("town_30","Domhan Briomhar",  icon_map_galvae_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.24, 232),[], 229),               #[swycartographr] prev. coords: (-94.88, 54.99) #[swycartographr] prev. coords: (-240.55, 60.24)

#

############
##CASTLES###
############

#entenaii
  ("castle_1","Forward_Base_Courage",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.05, -54.12),[],50),    #[swycartographr] prev. coords: (-101.3, -21) #[swycartographr] prev. coords: (-45.03, -20.17)
  ("castle_2","Forward_Base_Honour",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-176.41, -78.41),[],75),   #[swycartographr] prev. coords: (97.5, -2.2)
  ("castle_3","Forward_Base_Victory",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.05, -66.88),[],100),  #[swycartographr] prev. coords: (47.5, 111.3)

#dominion
  ("castle_4","First_Light_Mission",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.4, 159.14),[],180),  #[swycartographr] prev. coords: (32.5, 47.8)
  ("castle_5","Brazen_Mission",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.88, 303.53),[],90),  #[swycartographr] prev. coords: (-4.8, 63.7)
  ("castle_6","Open_Flame_Mission",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-135.46, 110.34),[],55), #[swycartographr] prev. coords: (37.6, 17.1)

#galvae
  ("castle_7","Reimse_Rioga",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(217.03, -119.45),[],45),            #[swycartographr] prev. coords: (109.5, 41.5)
  ("castle_8","Reimse_Crainn",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(134.68, 5.86),[],30),               #[swycartographr] prev. coords: (35.2, 89)
  ("castle_9","Reimse_Onoir",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.65, -66.1),[],100),              #[swycartographr] prev. coords: (-7.5, -82.6)

#union
  ("castle_10","Podoya_Fortified_Camp",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(283.98, -109.18),[],110),           #[swycartographr] prev. coords: (24.2, 96.85)
  ("castle_11","Zelenopul_Fortified_Camp",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.60, 211.18),[],75),              #[swycartographr] prev. coords: (-37.6, 111.22)
  ("castle_12","Vyatov_Fortified_Camp",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(141.51, 52.02),[],95),              #[swycartographr] prev. coords: (-84.75, 105.5)

#vitzland
  ("castle_13","Kanonenfestung_Messer",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.61, -126.37),[],115),         #[swycartographr] prev. coords: (-10.6, 17.6) #[swycartographr] prev. coords: (72.03, -122.16)
  ("castle_14","Kanonenfestung_Dolch",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-117.64, -141.03),[],90),        #[swycartographr] prev. coords: (-122.4, -18.1)
  ("castle_15","Kanonenfestung_Klinge",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.81, -87.38),[],235),         #[swycartographr] prev. coords: (-52.5, -28)

#republic
  ("castle_16","Castel_ci_Oro",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-208.16, -120.82),[],45),          #[swycartographr] prev. coords: (-10.6, -65.6)
  ("castle_17","Castel_ci_Genta",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.68, -213.61),[],15),          #[swycartographr] prev. coords: (140.3, -10.8)
  ("castle_18","Castel_ci_Piree",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.12, -134.04),[],300),         #[swycartographr] prev. coords: (14.4, 70.1) #[swycartographr] prev. coords: (-156.86, -134.75)

#itami
  ("castle_21","Itami_Embassy",icon_map_tower|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-358.19, 145.79),[],300),

#irregulars
  ("castle_19","Uprising_Fort",icon_map_bunker|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.02, 61.2),[],300),         #[swycartographr] prev. coords: (14.4, 70.1) #[swycartographr] prev. coords: (-156.86, -134.75)

#throd
  ("castle_20","War_Church_of_Throd",icon_map_tower|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-378.19, 135.79),[],300),         #[swycartographr] prev. coords: (14.4, 70.1) #[swycartographr] prev. coords: (-156.86, -134.75)

############
##Villages##
############

##Entenaii_Empire##
  ("village_1", "Dumbarton",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-175.65, -63.54),[], 100),            #[swycartographr] prev. coords: (-234.2, 176.85)
  ("village_2", "Burrafirth",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-106.73, -5.8),[], 344),              #[swycartographr] prev. coords: (73.56, -61.23)
  ("village_3", "Blaenau",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.66, 66.4),[], 203),             #[swycartographr] prev. coords: (-195.59, 159.41) #[swycartographr] prev. coords: (-115.82, 60.87)
  ("village_4", "Warcester",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-131.83, 56.63),[], 152),             #[swycartographr] prev. coords: (-70.53, 109.33) #[swycartographr] prev. coords: (-126.76, 43.98)
  ("village_5", "Astrakane",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-130.05, -10.48),[], 139),           #[swycartographr] prev. coords: (44.8, 9.6)
  ("village_6", "Malrton",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-208.04, 16.37),[], 100),            #[swycartographr] prev. coords: (-223.92, 95.21)
  ("village_7", "Carningsby",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-179.2, -4.8),[], 228),               #[swycartographr] prev. coords: (-0.2, -66)
  ("village_8", "Poltragow",  icon_map_tower|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-155.76, -19.62),[], 155),            #[swycartographr] prev. coords: (-146.89, 124.21)
  ("village_9", "Gormsey",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.58, -12.56),[], 352), #[swycartographr] prev. coords: (-76.55, -6.23)
  ("village_10","Coniston",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-230.57, 19.18),[], 170),            #[swycartographr] prev. coords: (-206.33, 113.47)
  ("village_11","Beckinsale",  icon_map_farm_4|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-162.61, 49.3),[], 261),            #[swycartographr] prev. coords: (22.7, -50.59) #[swycartographr] prev. coords: (-224.18, 28.9)
  ("village_12","Tallyvale",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.62, -31.61),[], 110), ##        #[swycartographr] prev. coords: (-45.8, -58.5)
  ("village_13","Whitebridge",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.65, -49.6),[], 44),             #[swycartographr] prev. coords: (107.32, 33.64)
  ("village_89","Sheviburgh",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129.52, 79.87),[], 0),           #[swycartographr] prev. coords: (70.1, -27.9) #[swycartographr] prev. coords: (28.19, -345.35)
  ("village_90","Birdwell",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-194.24, 39.78),[], 40),            #[swycartographr] prev. coords: (-12.7, -85.5) #[swycartographr] prev. coords: (8.71, -332.61)
  ("village_91","Harmstead",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-147.51, -62.02),[], 20),             #[swycartographr] prev. coords: (21.6, -95.3) #[swycartographr] prev. coords: (31.34, -340.89)
  
##Entenaii_Dominion##
  ("village_14","Lushingmire",  icon_map_farm_2|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-227.45,215.84),[], 126),          #[swycartographr] prev. coords: (35.45, 29.59) #[swycartographr] prev. coords: (-257.57, 123.33) #[swycartographr] prev. coords: (-230.86, 236.03)
  ("village_15","Flamfell",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-241.1, 98.25),[], 170),            #[swycartographr] prev. coords: (-119.86, 105.31)
  ("village_16","Mickleton",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.36, 165.39),[], 170), ##  #[swycartographr] prev. coords: (74, 86.8)
  ("village_17","Zelford",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-150.9, 322.87),[], 35), ##work  #[swycartographr] prev. coords: (44.7, 91.4)
  ("village_18","New Gavenston",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-266.34, 272.86),[], 170), ## #[swycartographr] prev. coords: (73.7, 30.1)
  ("village_19","Hannfield",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-258.01, 129.63),[], 170), ##  #[swycartographr] prev. coords: (152.3, 53.5)
  ("village_20","Rickport",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-172.6, 144.9),[], 170), ##     #[swycartographr] prev. coords: (116, 80.3)
  ("village_21","Bendolida",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.73, 316.1),[], 100), ##    #[swycartographr] prev. coords: (60.4, 85)
  ("village_22","Shauffield",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-203.82, 212.58),[], 110), ## #[swycartographr] prev. coords: (125.4, 64)
  ("village_23","Leadenglen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-205.26, 95.59),[], 152),           #[swycartographr] prev. coords: (-4.08, 157.23)
  ("village_24","Dilloguard",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-195.58, 167.09),[], 334),          #[swycartographr] prev. coords: (134.29, 125.51)
  ("village_25","Redport",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-202.7, 326.92),[], 170), ##          #[swycartographr] prev. coords: (125.2, -8)
  ("village_26","Labopoint",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-235.63, 69.66),[], 170), #[swycartographr] prev. coords: (-231.83, 27.94) #[swycartographr] prev. coords: (-172.18, 11.68) #[swycartographr] prev. coords: (-260.66, 58.07)
  ("village_27","Duffercairn",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-231.48, 112.52),[], 218),          #[swycartographr] prev. coords: (50.08, -82.64) #[swycartographr] prev. coords: (-221.86, 131.34)
  ("village_28","Polyton",  icon_map_farm_2|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-262.73, 84.62),[], 142),          #[swycartographr] prev. coords: (-19.51, 81.06)
  ("village_29","Duchelm",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-177.81, 286.72),[], 73),           #[swycartographr] prev. coords: (-37.85, 15.59)
  ("village_30","Titferglen",  icon_map_tower|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-309.16, 48.38),[], 170),           #[swycartographr] prev. coords: (-194.35, 107.48) #[swycartographr] prev. coords: (-307.17, 45.83)
  ("village_31","Beakhallow",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-264.14, 26.93),[], 295),          #[swycartographr] prev. coords: (127.23, 77.68)
  ("village_32","Gougeburg",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-243.93 , 316.73 ),[], 104),        #[swycartographr] prev. coords: (32.56, 100.17) #[swycartographr] prev. coords: (-233.95, 73.1)
  ("village_33","Vanham",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-285.23, 85.34),[], 193),          #[swycartographr] prev. coords: (-216.88, 41.19) #[swycartographr] prev. coords: (-294.02, 67.3)
  ("village_88","Tubthumpton",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-153.36, 221.97),[], 44),              #[swycartographr] prev. coords: (123.82, -4.43)
  ("village_105","Valeshire",  icon_map_house|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-107.38, 206.18),[], 297),              #[swycartographr] prev. coords: (-43.1, 75.42) #[swycartographr] prev. coords: (-85.4, 206.34)
  ("village_92","Alcombey",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-301.04, 333.61),[], 60),           #[swycartographr] prev. coords: (42.5, -111.6) #[swycartographr] prev. coords: (23.28, -333.24)
  ("village_93","Rotherhithe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-275.24, 363.73),[], 55),         #[swycartographr] prev. coords: (50, -94.8) #[swycartographr] prev. coords: (5.03, -349.69) #[swycartographr] prev. coords: (-313.65, 240.75)
  ("village_94","Croydon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-205.44, 245.14),[], 15),             #[swycartographr] prev. coords: (75.4, -61.65) #[swycartographr] prev. coords: (21.99, -351.33)
  
##Kingdom_of_Galvae##
  ("village_34","Peigin Ui Duillearga",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.74, -11.69),[], 218),            #[swycartographr] prev. coords: (61.62, 98.27) #[swycartographr] prev. coords: (108.83, -109.68)
  ("village_35","Fionnuala Ui Se",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(205.17, -2.69),[], 268),             #[swycartographr] prev. coords: (-175.32, 74.46) #[swycartographr] prev. coords: (113.24, -43.57)
  ("village_36","Caoimhe Ni Se",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(190.7, -134.61),[], 170),             #[swycartographr] prev. coords: (-151.88, 164.19) #[swycartographr] prev. coords: (216.8, -120.11)
  ("village_37","Duibheasa Ui Dubhagain",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(162.82, -170.91),[], 261),           #[swycartographr] prev. coords: (-4.09, 4.04)
  ("village_38","Blinne Ui Meara",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(91.26, -50.86),[], 29),              #[swycartographr] prev. coords: (-220.57, 85.35) #[swycartographr] prev. coords: (101.1, -60.93)
  ("village_39","Odharnait Nic Cosgair",  icon_map_tower|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(134.71, -161.84),[], 307),            #[swycartographr] prev. coords: (-73.04, -68.71) #[swycartographr] prev. coords: (140.18, -151.72)
  ("village_40","Barrdhubh Nic Gaibhtheachain",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(136.26, -44.02),[], 170), ## #[swycartographr] prev. coords: (-12, -53)
  ("village_41","Maire Ui Maoil Mhichil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106.29, -102.62),[], 100), ##work     #[swycartographr] prev. coords: (-95.46, 150.25)
  ("village_42","Teide Nic Cruadhlaoich",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(196.99, -83.61),[], 313),            #[swycartographr] prev. coords: (7.78, -89.54) #[swycartographr] prev. coords: (123.32, -72.56) #[swycartographr] prev. coords: (131.43, -63.91)
  ("village_43","Eilin Nic Amhlaidh",  icon_map_tower2|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(181.26, -61.48),[], 18),             #[swycartographr] prev. coords: (85.43, -84.25)
  ("village_44","Guibheasa Ui Hubhagain",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(51.8, -50),[], 130),
  ("village_45","Cuibh Ui Mubain",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(151.5, -3),[], 170),
  ("village_46","Tasa Ui Gain",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.29, -87.74),[], 170),        #[swycartographr] prev. coords: (-82.4, -48.8)
  ("village_95","Mag na Blathanna",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.72, 10.37),[], 10),               #[swycartographr] prev. coords: (99, -90.5) #[swycartographr] prev. coords: (16.89, -361.1)
  ("village_97","Tir Ceilte",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(224.99, -69.37),[], 160),        #[swycartographr] prev. coords: (82.3, -76.8) #[swycartographr] prev. coords: (13.2, -346.1)
  ("village_98","Mag na Nathracha",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(164.4, -131.88),[], 180),           #[swycartographr] prev. coords: (117.7, -62.2) #[swycartographr] prev. coords: (27.45, -349.98)
  
##Molvat-Berchav_Union##
  ("village_47","Zhabisty",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(260.18, 278.18),[], 216),               #[swycartographr] prev. coords: (-44.34, -38.49) #[swycartographr] prev. coords: (159.2, 248.92)
  ("village_48","Luninpolatsk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.74, 216.73),[], 39),                  #[swycartographr] prev. coords: (-12.86, 123.17) #[swycartographr] prev. coords: (-17, 167.19)
  ("village_49","Komastovo",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.4, 62.17),[], 10),          #[swycartographr] prev. coords: (90.8, 60.5)
  ("village_50","Poprance",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(293.39, -88.48),[], 170),       #[swycartographr] prev. coords: (64.1, 55.9)
  ("village_51","Hrasko",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.27, 169.87),[], 328),              #[swycartographr] prev. coords: (-204.9, 132.18) #[swycartographr] prev. coords: (11.15, 177.57)
  ("village_52","Sharliaky",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120.91, 245.29),[], 110),           #[swycartographr] prev. coords: (38.2, -67.7)
  ("village_53","Parbice",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.28, 127.04),[], 65),               #[swycartographr] prev. coords: (50.24, -61.99) #[swycartographr] prev. coords: (117.75, 81.08) #[swycartographr] prev. coords: (108.47, 82.55)
  ("village_54","Varlany",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(274.12, 64.31),[], 204),             #[swycartographr] prev. coords: (-21.56, -23.88) #[swycartographr] prev. coords: (-31.28, -57.32)
  ("village_55","Hajhalas",  icon_map_dest_city|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(194.15, 199.56),[], 53),           #[swycartographr] prev. coords: (-86.56, 49.57) #[swycartographr] prev. coords: (105.36, 226.99)
  ("village_56","Elknovo",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(146.54, 157.96),[], 170),             #[swycartographr] prev. coords: (-5.55, 75.5)
  ("village_57","Hosytvit",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(150.59, 78.02),[], 243),               #[swycartographr] prev. coords: (-45.39, 47.23) #[swycartographr] prev. coords: (137.75, 70.82)
  ("village_58","Wloclawek",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.50, 182.76),[], 190),               #[swycartographr] prev. coords: (140.86, 22.36) #[swycartographr] prev. coords: (119.15, -32.96) #[swycartographr] prev. coords: (141.66, 39.06) #[swycartographr] prev. coords: (240.98, 54.04) #[swycartographr] prev. coords: (78.5, 37.83)
  ("village_59","Stalonicza",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(122.69, 316.21),[], 278),              #[swycartographr] prev. coords: (-159.28, 53.61) #[swycartographr] prev. coords: (127.67, 297.23)
  ("village_60","Harghiol",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(251.47, 9.5),[], 326),              #[swycartographr] prev. coords: (-7.88, 65.47) #[swycartographr] prev. coords: (291.37, 18.67)
  ("village_61","Mangavasna",  icon_map_house|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(285.9, -52.61),[], 100),              #[swycartographr] prev. coords: (-243.54, 97) #[swycartographr] prev. coords: (270.97, 18.84)
  ("village_62","Murlija",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.25, 243.91),[], 100),              #[swycartographr] prev. coords: (36.7, 59.5)
  ("village_63","Andrutrov",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.09, 129.21),[], 100),             #[swycartographr] prev. coords: (-95.15, 191.35) #[swycartographr] prev. coords: (-10.49, 146.99)
  ("village_96","Evsitke",  icon_map_farm_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.97, 178.13),[], 116),               #[swycartographr] prev. coords: (-27.13, 33.33) #[swycartographr] prev. coords: (-22.85, 6.47) #[swycartographr] prev. coords: (-74.81, 192.19) #[swycartographr] prev. coords: (-37.63, 209.09)
  ("village_99","Balanomyssk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.22, 146.51),[], 0),     #[swycartographr] prev. coords: (158.35, -98) #[swycartographr] prev. coords: (19.36, -355.67)
  ("village_100","Saronza",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(215.55, 53.02),[], 40),           #[swycartographr] prev. coords: (150, -106.5) #[swycartographr] prev. coords: (16.93, -336.58)
  ("village_101","Batatity",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(154.45, 260.76),[], 20),       #[swycartographr] prev. coords: (154, -69.5) #[swycartographr] prev. coords: (4.09, -362.08)
  ("village_109","Birozuluk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.76, 124.47),[], 0),           #[swycartographr] prev. coords: (53, -114.5) #[swycartographr] prev. coords: (10.6, -339.08)
  ("village_110","Zhukomna",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.34, 264.53),[], 40),            #[swycartographr] prev. coords: (38, -104) #[swycartographr] prev. coords: (-5.79, -364.42)

##Empire_of_Vitzland##
  ("village_64","Kitzfeld",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.63, -175.3),[], 100),          #[swycartographr] prev. coords: (-160.44, 27.19) #[swycartographr] prev. coords: (-51.75, -166.08)
  ("village_65","Neunfeld",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.55, -92.8),[], 100),          #[swycartographr] prev. coords: (95.78, 66.69) #[swycartographr] prev. coords: (-17.87, -96.39)
  ("village_66","Tourvoorde",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.31, -167.69),[], 100),           #[swycartographr] prev. coords: (-137.02, 18.43)
  ("village_67","Avilun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.38, -142.89),[], 100),          #[swycartographr] prev. coords: (26.11, 133.31)
  ("village_68","Richtenwerder",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.71, -130.92),[], 100),          #[swycartographr] prev. coords: (-113.25, 52.42) #[swycartographr] prev. coords: (69.13, -128.12)
  ("village_69","Munchenthal",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.21, -142.28),[], 100),           #[swycartographr] prev. coords: (-24.35, 167.23) #[swycartographr] prev. coords: (18.55, -122.13)
  ("village_70","Klostermarkt",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.18, -130.74),[], 100),           #[swycartographr] prev. coords: (70.18, -22.85) #[swycartographr] prev. coords: (-29.1, -123.74)
  ("village_71","Gailstein",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.15, -157.64),[], 20),          #[swycartographr] prev. coords: (-108.85, 28.21)
  ("village_72","Hoogezijl",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.09, -206.92),[], 60),            #[swycartographr] prev. coords: (137.27, 200.05)
  ("village_73","Freikkon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.69, -130.94),[], 55),           #[swycartographr] prev. coords: (-77.46, 8.86)
  ("village_74","Maasschede",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.24, -170.31),[], 15),          #[swycartographr] prev. coords: (-37.9, 228.59)
  ("village_75","Isselbeuren",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.36, -119.82),[], 10),     #[swycartographr] prev. coords: (-166.61, 145.15)
  ("village_102","Kirchnitz",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.55, -150.92),[], 60),              #[swycartographr] prev. coords: (77.2, -91) #[swycartographr] prev. coords: (17.78, -322.53)
  ("village_103","Munzenhoring",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.43, -116.56),[], 55),      #[swycartographr] prev. coords: (121, -95.6) #[swycartographr] prev. coords: (21.67, -340.14)
  ("village_104","Reimunster",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.44, -111.99),[], 15),       #[swycartographr] prev. coords: (159, -58.5) #[swycartographr] prev. coords: (8.99, -355.07)
  
##Trezzo_Republic##
  ("village_76","Vallanse",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.6, -233.86),[], 105),         #[swycartographr] prev. coords: (119.85, -38.77) #[swycartographr] prev. coords: (-161.81, -213.83)
  ("village_77","Badava",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-222.19, -173.61),[], 160),         #[swycartographr] prev. coords: (-55.06, 151.86) #[swycartographr] prev. coords: (-219.04, -194.57)
  ("village_78","Aveirante",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-243.21, -214.09),[], 180),         #[swycartographr] prev. coords: (-66.28, 210.61) #[swycartographr] prev. coords: (-253.71, -209.8)
  ("village_79","Garano",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-119.83, -262.72),[], 0),           #[swycartographr] prev. coords: (133.43, 154.3)
  ("village_80","Casotri",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-266.27, -196.56),[], 40),            #[swycartographr] prev. coords: (-156.78, 101.69)
  ("village_81","Fatirante",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-260, -167.18),[], 20),         #[swycartographr] prev. coords: (-145.59, 84.88) #[swycartographr] prev. coords: (-251.21, -168.23)
  ("village_82","Bolora",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.69, -185.2),[], 60),           #[swycartographr] prev. coords: (77.18, 148.94)
  ("village_83","Trenremo",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-168.6, -178.49),[], 55),          #[swycartographr] prev. coords: (-274.25, 203.03) #[swycartographr] prev. coords: (-186.12, -195.21)
  ("village_84","Guidoceno",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-164.95, -315.06),[], 15),         #[swycartographr] prev. coords: (25.36, 60.11) #[swycartographr] prev. coords: (-166.94, -301.71)
  ("village_85","Ceretta",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-196.09, -121.5),[], 10),       #[swycartographr] prev. coords: (22.8, 71.7)
  ("village_86","Netalina",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-101.8, -240.18),[], 35),  #[swycartographr] prev. coords: (60.5, 68.2)
  ("village_87","Riogoza",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-167.47, -288.54),[], 100),              #[swycartographr] prev. coords: (-11.37, 30.95) #[swycartographr] prev. coords: (-53.08, -22.02) #[swycartographr] prev. coords: (-119.5, 290.99)
  ("village_106","Santatima",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132.41, -91.0),[], 35),            #[swycartographr] prev. coords: (10.3, -162.71) #[swycartographr] prev. coords: (3.57, -91)
  ("village_107","Barcejara",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-194.36, -182.49),[], 160),     #[swycartographr] prev. coords: (156.6, -84) #[swycartographr] prev. coords: (-2.67, -354.52)
  ("village_108","Bragarta",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129.99, -224.4),[], 180),           #[swycartographr] prev. coords: (28.8, -107.3) #[swycartographr] prev. coords: (15.95, -330.45)
  
##Mines##
##Entenaii_Empire
  ("entenaii_empire_mine_iron","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-189.18, -0.64),[]), #[swycartographr] prev. coords: (179.04, 90.45) #[swycartographr] prev. coords: (114.86, 169.27) rot: 0
  ("entenaii_empire_mine_coal","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-119.81, -29.32),[]), #[swycartographr] prev. coords: (179.04, 90.45) #[swycartographr] prev. coords: (114.86, 169.27) rot: 0

##Entenaii_Dominion
  ("entenaii_dominion_mine_iron","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-261.91, 118.97),[]), #[swycartographr] prev. coords: (179.04, 90.45) #[swycartographr] prev. coords: (114.86, 169.27) rot: 0
  ("entenaii_dominion_mine_coal","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-231.07, 326.12),[]), #[swycartographr] prev. coords: (179.04, 90.45) #[swycartographr] prev. coords: (114.86, 169.27) rot: 0

##Kingdom_of_Galvae##
  ("galvae_mine_iron","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.13, -79.19),[]), #[swycartographr] prev. coords: (179.04, 90.45) #[swycartographr] prev. coords: (114.86, 169.27) rot: 0
  ("galvae_mine_coal","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.96, -8.34),[]), #[swycartographr] prev. coords: (179.04, 90.45) #[swycartographr] prev. coords: (114.86, 169.27) rot: 0
  
##Molvat-Berchav_Union##
  ("union_mine_iron","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120.4, 99.26),[]), #[swycartographr] prev. coords: (179.04, 90.45) #[swycartographr] prev. coords: (114.86, 169.27) rot: 0
  ("union_mine_coal","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(238.61, 248.06),[]), #[swycartographr] prev. coords: (179.04, 90.45) #[swycartographr] prev. coords: (114.86, 169.27) rot: 0 #[swycartographr] prev. coords: (238.65, 248.57)
  
##Empire_of_Vitzland##
  ("vitzland_mine_iron","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.93, -159.8),[]), #[swycartographr] prev. coords: (179.04, 90.45) #[swycartographr] prev. coords: (114.86, 169.27) rot: 0
  ("vitzland_mine_coal","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.78, -139.79),[]), #[swycartographr] prev. coords: (179.04, 90.45) #[swycartographr] prev. coords: (114.86, 169.27) rot: 0
  
##Trezzo_Republic##
  ("republic_mine_iron","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.79, -278.05),[]), #[swycartographr] prev. coords: (179.04, 90.45) #[swycartographr] prev. coords: (114.86, 169.27) rot: 0
  ("republic_mine_coal","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-163.08, -157.08),[]), #[swycartographr] prev. coords: (179.04, 90.45) #[swycartographr] prev. coords: (114.86, 169.27) rot: 0

#extra

  ("salt_mine","Baren's_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.75, 150.94),[]), #[swycartographr] prev. coords: (179.04, 90.45) #[swycartographr] prev. coords: (114.86, 169.27) rot: 0
  #
  ("arena_1","The Grand Melee",icon_map_mercenary_camp|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.64,12.59),[],282), #[swycartographr] prev. coords: (22.15, -0.38) #[swycartographr] prev. coords: (-19.47, 53.96)
  # ("arena_1","No Tales Ground",icon_map_tower2|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.15,-0.38),[],282),
  # ("arena_2","Tribute Ground",icon_map_tower|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.2, -31),[]),
  # ("arena_3","Grand Arc Arena",icon_map_tower2|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.2, -31),[]),
  # ("arena_4","Cinder Ring",icon_map_tower|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -25),[]),

  ("starting_point","Abandoned Factory",icon_map_factory|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.45, 76.04),[],42), #(-35.19,-9.69) #[swycartographr] prev. coords: (-12.86, 107.69)
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(335.00, 335.00),[]), #[swycartographr] prev. coords: (335, 335)

  ("bridge_a_a","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-51.87,203.54),[],71), #[swycartographr] prev. coords: (-149.55, 25.34) #[swycartographr] prev. coords: (-52.82, 202.16) #[swycartographr] prev. coords: (-52.1, 203.66) rot: 25
  ("bridge_a_b","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(52.46,-120.01),[],121), #[swycartographr] prev. coords: (-152.66, 39.44) #[swycartographr] prev. coords: (-155.26, -2.3) rot: 204
  ("bridge_a_c","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-34.8,198.24),[],244), #[swycartographr] prev. coords: (-149.55, 93.94) #[swycartographr] prev. coords: (-103.42, 191.33) #[swycartographr] prev. coords: (-34.42, 198.21) rot: 174
  ("bridge_a_d","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-123.94,197.11),[],101), #[swycartographr] prev. coords: (-235.06, 128.93) #[swycartographr] prev. coords: (-150.34, 201.49) #[swycartographr] prev. coords: (-124.57, 196.85) rot: 158
  ("bridge_a_e","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(136.99,22.18),[],155), #[swycartographr] prev. coords: (-238.39, 121.95) #[swycartographr] prev. coords: (-197.1, 202.49) #[swycartographr] prev. coords: (137.31, 21.67) rot: 158 #[swycartographr] prev. coords: (136.53, 21.87)
  ("bridge_a_f","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-34.47,-7.13),[],115), #[swycartographr] prev. coords: (-195.57, 17.39) #[swycartographr] prev. coords: (-144.72, 49.6) #[swycartographr] prev. coords: (-34.75, -7.49) rot: 197
  ("bridge_a_g","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-245.86,260.31),[],111), #[swycartographr] prev. coords: (-184.19, -1.44) #[swycartographr] prev. coords: (-178.95, 22.88) #[swycartographr] prev. coords: (-117.75, 137.74) rot: 25 #[swycartographr] prev. coords: (-117.65, 137.13) rot: 109
  ("bridge_a_h","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-275.14,254.29),[],95), #[swycartographr] prev. coords: (-184.19, -1.44) #[swycartographr] prev. coords: (-178.95, 22.88) #[swycartographr] prev. coords: (-117.75, 137.74) rot: 25 #[swycartographr] prev. coords: (-117.65, 137.13) rot: 109
  ("bridge_a_i","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-284.33,337.93),[],121), #[swycartographr] prev. coords: (-184.19, -1.44) #[swycartographr] prev. coords: (-178.95, 22.88) #[swycartographr] prev. coords: (-117.75, 137.74) rot: 25 #[swycartographr] prev. coords: (-117.65, 137.13) rot: 109
  ("bridge_a_j","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-25.08,33.68),[],132), #[swycartographr] prev. coords: (-184.19, -1.44) #[swycartographr] prev. coords: (-178.95, 22.88) #[swycartographr] prev. coords: (-117.75, 137.74) rot: 25 #[swycartographr] prev. coords: (-117.65, 137.13) rot: 109
  ("bridge_a_k","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(223.1,-127.98),[],246), #[swycartographr] prev. coords: (-184.19, -1.44) #[swycartographr] prev. coords: (-178.95, 22.88) #[swycartographr] prev. coords: (-117.75, 137.74) rot: 25 #[swycartographr] prev. coords: (-117.65, 137.13) rot: 109
  ("bridge_a_l","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(211.71,-108.9),[],70), #[swycartographr] prev. coords: (-184.19, -1.44) #[swycartographr] prev. coords: (-178.95, 22.88) #[swycartographr] prev. coords: (-117.75, 137.74) rot: 25 #[swycartographr] prev. coords: (-117.65, 137.13) rot: 109
  ("bridge_a_m","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-118.05,136.98),[],109), #[swycartographr] prev. coords: (-184.19, -1.44) #[swycartographr] prev. coords: (-178.95, 22.88) #[swycartographr] prev. coords: (-117.75, 137.74) rot: 25 #[swycartographr] prev. coords: (-117.65, 137.13) #[swycartographr] prev. coords: (-117.54, 137.18)

  ("bridge_b_a","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-116.66,82.34),[],238), #[swycartographr] prev. coords: (-138.92, 57.67) #[swycartographr] prev. coords: (-116.97, 81.77) rot: 95
  ("bridge_b_b","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-103.87,191.08),[],352), #[swycartographr] prev. coords: (-143.35, 77.74) #[swycartographr] prev. coords: (-34.23, 198.69) #[swycartographr] prev. coords: (-103.87, 191.08) rot: 100
  ("bridge_b_c","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-178.84,23.1),[],246), #[swycartographr] prev. coords: (-151.18, 112.86) #[swycartographr] prev. coords: (-118.11, 136.04) #[swycartographr] prev. coords: (-178.84, 23.1) rot: 274
  ("bridge_b_d","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-150.45,201.54),[],17), #[swycartographr] prev. coords: (-152.05, 147.56) #[swycartographr] prev. coords: (-124.06, 197.11) #[swycartographr] prev. coords: (-150.64, 201.36) rot: 91
  ("bridge_b_e","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-199.24,223.84),[],234), #[swycartographr] prev. coords: (-185.38, 118) #[swycartographr] prev. coords: (-199.24, 223.84) rot: 82
  ("bridge_b_f","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-157.23,246.83),[],7), #[swycartographr] prev. coords: (-167.71, 149.59) #[swycartographr] prev. coords: (-157.85, 246.8) rot: 236
  ("bridge_b_g","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-144.77,49.34),[],239), #[swycartographr] prev. coords: (-17.69, 134.26) #[swycartographr] prev. coords: (-34.89, -6.21) #[swycartographr] prev. coords: (-144.77, 49.34) rot: 210
  ("bridge_b_h","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-76.86,185.3),[],344), #[swycartographr] prev. coords: (-61.79, 87.53) #[swycartographr] prev. coords: (-77.3, 185.08) rot: 212
  ("bridge_b_i","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(112.58,-122.57),[],235), #[swycartographr] prev. coords: (-37.03, 109.25) #[swycartographr] prev. coords: (222.64, -127.72) rot: 205 #[swycartographr] prev. coords: (222.7, -128) rot: 256 #[swycartographr] prev. coords: (112.52, -122.91)
  ("bridge_b_j","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-196.63,202.8),[],0), #[swycartographr] prev. coords: (101.91, 42.9) #[swycartographr] prev. coords: (134.78, 22.43) #[swycartographr] prev. coords: (-196.63, 202.8) rot: 251
  ("bridge_b_k","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(149.49,-115.11),[],2), #[swycartographr] prev. coords: (73.77, 148.16) #[swycartographr] prev. coords: (211.29, -108.71) rot: 263 #[swycartographr] prev. coords: (211.84, -108.89) rot: 71
  ("bridge_b_l","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-57.2,-135.94),[],3), #[swycartographr] prev. coords: (-147.55, 0.26) #[swycartographr] prev. coords: (51.75, -118.98) rot: 182 #[swycartographr] prev. coords: (-76.48, -179.13) rot: 311
  ("bridge_b_m","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-15.68,-81.16),[],289), #[swycartographr] prev. coords: (-147.55, 0.26) #[swycartographr] prev. coords: (51.75, -118.98) rot: 182 #[swycartographr] prev. coords: (-76.48, -179.13) rot: 311 #[swycartographr] prev. coords: (-15.47, -80.93)
  ("bridge_b_n","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-0.4,-100.71),[],22), #[swycartographr] prev. coords: (-147.55, 0.26) #[swycartographr] prev. coords: (51.75, -118.98) rot: 182 #[swycartographr] prev. coords: (-76.48, -179.13) rot: 311 #[swycartographr] prev. coords: (-0.24, -100.73)
  ("bridge_b_o","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(96.32,-23.15),[],20), #[swycartographr] prev. coords: (-147.55, 0.26) #[swycartographr] prev. coords: (51.75, -118.98) rot: 182 #[swycartographr] prev. coords: (-76.48, -179.13) rot: 311 #[swycartographr] prev. coords: (-76.32, -179.18) rot: 302
  ("bridge_b_p","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-67.92,178.28),[],297), #[swycartographr] prev. coords: (-147.55, 0.26) #[swycartographr] prev. coords: (51.75, -118.98) rot: 182 #[swycartographr] prev. coords: (-76.48, -179.13) rot: 311 #[swycartographr] prev. coords: (-76.32, -179.18) rot: 302
  ("bridge_b_q","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-197.13,-98.42),[],9), #[swycartographr] prev. coords: (-147.55, 0.26) #[swycartographr] prev. coords: (51.75, -118.98) rot: 182 #[swycartographr] prev. coords: (-76.48, -179.13) rot: 311 #[swycartographr] prev. coords: (-76.32, -179.18) rot: 302
  ("bridge_b_r","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-83.13,125.19),[],255), #[swycartographr] prev. coords: (-147.55, 0.26) #[swycartographr] prev. coords: (51.75, -118.98) rot: 182 #[swycartographr] prev. coords: (-76.48, -179.13) rot: 311 #[swycartographr] prev. coords: (-76.32, -179.18) rot: 302 #[swycartographr] prev. coords: (-76.6, -179.36) rot: 307
  ("bridge_b_s","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-80.79,144.1),[],209), #[swycartographr] prev. coords: (-147.55, 0.26) #[swycartographr] prev. coords: (51.75, -118.98) rot: 182 #[swycartographr] prev. coords: (-76.48, -179.13) rot: 311 #[swycartographr] prev. coords: (-76.32, -179.18) rot: 302 #[swycartographr] prev. coords: (-76.6, -179.36) rot: 307
  ("bridge_b_t","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-99.37,123.65),[],239), #[swycartographr] prev. coords: (-147.55, 0.26) #[swycartographr] prev. coords: (51.75, -118.98) rot: 182 #[swycartographr] prev. coords: (-76.48, -179.13) rot: 311 #[swycartographr] prev. coords: (-76.32, -179.18) rot: 302 #[swycartographr] prev. coords: (-76.6, -179.36) rot: 307
  ("bridge_b_u","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-76.46,-179.28),[],307), #[swycartographr] prev. coords: (-147.55, 0.26) #[swycartographr] prev. coords: (51.75, -118.98) rot: 182 #[swycartographr] prev. coords: (-76.48, -179.13) rot: 311 #[swycartographr] prev. coords: (-76.32, -179.18) rot: 302 #[swycartographr] prev. coords: (-76.6, -179.36)

  ("map_warehouse","map_warehouse",icon_map_warehouse|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-152.33,126.47),[],278), #[swycartographr] prev. coords: (-179.03, 143.46)
  ("map_warehouse2","map_warehouse",icon_map_warehouse|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-132.24,7.06),[],96), #[swycartographr] prev. coords: (-120.37, 37.52)
  ("map_warehouse3","map_warehouse",icon_map_warehouse|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(58.35,3.42),[],111), #[swycartographr] prev. coords: (68.8, 20.34)
  ("map_warehouse4","map_warehouse",icon_map_warehouse|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-51.36,234.8),[],147), #[swycartographr] prev. coords: (-34.55, 218.49)
  ("map_warehouse5","map_warehouse",icon_map_warehouse|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(74.5,80.09),[],115), #[swycartographr] prev. coords: (-22.79, 108.05)

  ("map_boat_1a","map_boat_1a",icon_map_boat_1|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-27.56,-282.32),[],209), #[swycartographr] prev. coords: (-194.49, -12.37)
  ("map_boat_1b","map_boat_1a",icon_map_boat_1|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(221.75,-110.39),[],299), #[swycartographr] prev. coords: (43.88, 208.73)
  ("map_boat_1c","map_boat_1a",icon_map_boat_1|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(28.22,292.34),[],191), #[swycartographr] prev. coords: (41.87, 162.79)
  ("map_boat_1d","map_boat_1a",icon_map_boat_1|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-223.96,204.8),[],277), #[swycartographr] prev. coords: (-268.92, 157.3)
  ("map_boat_1e","map_boat_1a",icon_map_boat_1|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-35.47,270.08),[],290), #[swycartographr] prev. coords: (-280.67, 202.02) #[swycartographr] prev. coords: (-45.36, 194.97) #[swycartographr] prev. coords: (-33, 234)

#secret_bases
  ("map_secret_base_shadow","Hidden_Bunker",icon_map_bunker|pf_is_static|pf_hide_defenders,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-99.53,-95.68),[],131), #[swycartographr] prev. coords: (-62.09, 173.59)
  ("map_secret_base_throd","Throd_Chapel",icon_map_monastery|pf_is_static|pf_hide_defenders,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-346.74,225.25),[],345), #[swycartographr] prev. coords: (126.07, -56.15) #[swycartographr] prev. coords: (157.17, -88.26)
  ("map_secret_base_irregular","Irregular_Forward_Camp",icon_map_mercenary_camp|pf_is_static|pf_hide_defenders,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-54.61,-23.39),[],237), #[swycartographr] prev. coords: (-182.52, 51.84) #[swycartographr] prev. coords: (-174.7, 52.52)
  ("map_secret_base_legion","Hall_of_the_Fallen_Legion",icon_bandit_lair|pf_is_static|pf_hide_defenders,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-86.96,248.73),[],192), #[swycartographr] prev. coords: (-80.59, -35.77)
  ("map_secret_base_ezeg","Ezeg_Lair",icon_bandit_lair|pf_is_static|pf_hide_defenders,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-16.88,-177.79),[],303), #[swycartographr] prev. coords: (-246.77, 151.74) #[swycartographr] prev. coords: (-232.62, 110.74)
  ("map_secret_base_yanizar","Yanizar_Camp",icon_bandit_camp|pf_is_static|pf_hide_defenders,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-97.83,-202.97),[],303), #[swycartographr] prev. coords: (-246.77, 151.74) #[swycartographr] prev. coords: (-232.62, 110.74)

#
  ("map_razed_city_1", "Tarrin (RAZED)", icon_map_razed_city|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-192.48, -63.68), [], 126), #[swycartographr] prev. coords: (5.68, 89.59) #[swycartographr] prev. coords: (234.58, -145.79)
  ("map_razed_city_2", "Monmouth (RAZED)", icon_map_razed_city|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-93.94, 231.52), [], 126), #[swycartographr] prev. coords: (5.68, 89.59) #[swycartographr] prev. coords: (234.58, -145.79)
  ("map_razed_city_3", "Bredwardine (RAZED)", icon_map_razed_city|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-177.43, -147.56), [], 126), #[swycartographr] prev. coords: (5.68, 89.59) #[swycartographr] prev. coords: (234.58, -145.79)
  ("map_razed_city_4", "Glenarm (RAZED)", icon_map_razed_city|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-82.93, -89.53), [], 126), #[swycartographr] prev. coords: (5.68, 89.59) #[swycartographr] prev. coords: (234.58, -145.79)
  ("map_razed_city_5", "Durrwich (RAZED", icon_map_razed_city|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-5.03, -87.65), [], 126), #[swycartographr] prev. coords: (5.68, 89.59) #[swycartographr] prev. coords: (234.58, -145.79)
  ("map_razed_city_6", "Aberuthven (RAZED)", icon_map_razed_city|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-122.36, -109.03), [], 126), #[swycartographr] prev. coords: (5.68, 89.59) #[swycartographr] prev. coords: (234.58, -145.79)
  ("map_razed_city_7", "Zalchik (RAZED)", icon_map_razed_city|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (224.43, 140.07), [], 126), #[swycartographr] prev. coords: (5.68, 89.59) #[swycartographr] prev. coords: (234.58, -145.79)
  ("map_razed_city_8", "Moknovci (RAZED)", icon_map_razed_city|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (235.53, -165.53), [], 126), #[swycartographr] prev. coords: (5.68, 89.59) #[swycartographr] prev. coords: (234.58, -145.79)
  ("map_razed_city_9", "Pescadena (RAZED)", icon_map_razed_city|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-106.77, -171.69), [], 126), #[swycartographr] prev. coords: (5.68, 89.59) #[swycartographr] prev. coords: (234.58, -145.79)
  ("map_razed_city_10", "Domhan Briomhar (RAZED)", icon_map_razed_city|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (41.95, -24.53), [], 126), #[swycartographr] prev. coords: (5.68, 89.59) #[swycartographr] prev. coords: (234.58, -145.79) #[swycartographr] prev. coords: (77.08, -125.28)

  # ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(26, 77),[(trp_looter,15,0)]),
  # ("steppe_bandit_spawn_point"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(125, 9),[(trp_looter,15,0)]),
  # ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(78, 84),[(trp_looter,15,0)]),
  # ("forest_bandit_spawn_point"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-35, 18),[(trp_looter,15,0)]),
  # ("mountain_bandit_spawn_point","the highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-90, -26.8),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(85.59, 106.26),[(trp_looter,15,0)]), #[swycartographr] prev. coords: (48.5, 110)
  # ("sea_raider_spawn_point_2"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-42, 76.7),[(trp_looter,15,0)]),
  # ("desert_bandit_spawn_point"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(110, -100),[(trp_looter,15,0)]),
 # add extra towns before this point
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., -12.53),[(trp_looter,15,0)]), #[swycartographr] prev. coords: (13.15, 0) #[swycartographr] prev. coords: (24.63, 21.53) #[swycartographr] prev. coords: (2.81, 17.04) #[swycartographr] prev. coords: (5.44, -5.45) #[swycartographr] prev. coords: (0, -6.03)
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., -13.68),[(trp_looter,15,0)]), #[swycartographr] prev. coords: (7.14, 0) #[swycartographr] prev. coords: (27.18, 16.95) #[swycartographr] prev. coords: (15.8, 21) #[swycartographr] prev. coords: (0, -13.72)
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 35.93),[(trp_looter,15,0)]), #[swycartographr] prev. coords: (6.51, 0) #[swycartographr] prev. coords: (32.18, 11.84) #[swycartographr] prev. coords: (-58.21, 14.23) #[swycartographr] prev. coords: (-10.62, 24.52) #[swycartographr] prev. coords: (0, 55.85)
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., -32.28),[(trp_looter,15,0)]), #[swycartographr] prev. coords: (19.66, 0) #[swycartographr] prev. coords: (26.79, 27.47) #[swycartographr] prev. coords: (0, 26.45)
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., -43.65),[(trp_looter,15,0)]), #[swycartographr] prev. coords: (12.93, 0) #[swycartographr] prev. coords: (20.98, 22.95) #[swycartographr] prev. coords: (9.98, 25.12) #[swycartographr] prev. coords: (0, -19.76)
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., -14.45),[(trp_looter,15,0)]), #[swycartographr] prev. coords: (24.83, 0) #[swycartographr] prev. coords: (22.44, 33.86) #[swycartographr] prev. coords: (6.87, 30.7) #[swycartographr] prev. coords: (20.77, -13.43) #[swycartographr] prev. coords: (0, -18.42)

  ("outpost_1", "Outpost", icon_map_camp_2|pf_disabled|pf_is_static|pf_always_visible, no_menu, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (-51.99, 51.91), []), #[swycartographr] prev. coords: (0, 0) #[swycartographr] prev. coords: (-15.55, -4.82)
  ("outpost_2", "Outpost", icon_map_camp_2|pf_disabled|pf_is_static|pf_always_visible, no_menu, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (-49.03, 57.4), []), #[swycartographr] prev. coords: (1, -1) #[swycartographr] prev. coords: (-37.84, 27.45)
  # ("map_volcano", "volcano", icon_map_dummy|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (285.4, -9.95), [], 174),

  ("vehicles", "Vehicles", icon_map_dummy|pf_disabled|pf_is_static|pf_always_visible, no_menu, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (-55.71, 46.79), []), #[swycartographr] prev. coords: (0, 0) #[swycartographr] prev. coords: (-15.23, 2.86)


  ]
# modmerger_start version=201 type=2
try:
    component_name = "parties"
    var_set = { "parties" : parties }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
