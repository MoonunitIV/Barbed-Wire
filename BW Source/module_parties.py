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
pf_village = pf_is_static|pf_hide_defenders|pf_show_faction|pf_label_small

parties = [
#!#
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(-22.11, 55.28),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(9.78,1.61),[]),                               
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(13.02,7.16),[(trp_temp_troop,3,0)]),        
#!#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(24.09,13.24),[]),                         
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.45,12.17),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.55,31.12),[]),                        
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.23,42.45),[]),                        
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.2,15.73),[]),                       
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.12,-1.81),[]),                         
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.52,-23.92),[]),                              
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.31,-25.34),[]),                       
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.44,-26.76),[]),                       
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.62,-28.84),[]),                              
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.9,-30.21),[]),                                
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.83,-31.69),[]),                                

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.52,4.64),[]),                    
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.35,-19.99),[]),                    
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.45,-26.71),[]),                 

  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.41,-32.94),[]),
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.76,-12.25),[]),

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

###############################################################
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.5,66.32),[]),
#########
##TOWNS##
#########

#Aberstwyth = Entenaii Dominion (Capital)
  ("town_1","Aberstwyth",  icon_map_dominion_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-251.55, 72.24),[], 229),    
#Ivorstead = Entenaii Empire  
  ("town_2","Ivorstead",     icon_map_entenaii_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.59, 40.24),[], 120),
#Bracklewhyte = Entenaii Dominion  
  ("town_3","Bracklewhyte",   icon_map_dominion_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-286.34, 34.06),[], 80),  
#Plkovice = Molvat-Berchav Union  
  ("town_4","Plkovice",     icon_map_union_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(209.75, 281.36),[], 290),      
#Todmorden = Entenaii Dominion  
  ("town_5","Todmorden",  icon_map_dominion_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-206.77, 283.54),[], 90),     
#Millhallow = Entenaii Empire (Capital)  
  ("town_6","Millhallow",   icon_map_entenaii_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.54, -19.36),[], 228),  
#Canthagen = Entenaii Empire  
  ("town_7","Canthagen",   icon_map_entenaii_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-177.54, -19.01),[], 200),   
#Castellalvano = Trezzo Republic (Capital)
  ("town_8","Castellalvano", icon_map_republic_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-170.93, -216.81),[], 321),
#T ir an Tsioraiocht = Kingdom of Galvae  
  ("town_9","Tir an Tsioraiocht",   icon_map_galvae_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(142.67, -195.5),[], 321),  #[swycartographr] prev. coords: (143.27, -195.27)
#Sely = Molvat-Berchav Union (Capital)
  ("town_10","Sely",   icon_map_union_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.59, 72.31),[], 222),            
#Gerarissa = Trezzo Republic  
  ("town_11","Gerarissa",  icon_map_republic_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-142.42, -299.15),[], 352),  
#Murlayfield = Entenaii Dominion  
  ("town_12","Murlayfield", icon_map_dominion_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-192.8, 143.63),[], 25),    
#Bolorence = Trezzo Republic  
  ("town_13","Bolorence",icon_map_republic_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-238.44, -183.56),[], 246),    
#Luninmyel = Molvat-Berchav Union  
  ("town_14","Luninmyel",  icon_map_union_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.09, 166.16),[], 82),          
#Domhan Geal = Kingdom of Galvae  
  ("town_15","Domhan Geal",  icon_map_galvae_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(142.31, -61.13),[], 349),    
#Mag Suaimhnis = Kingdom of Galvae (Capital)
  ("town_16","Mag Suaimhnis",  icon_map_galvae_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(196.24, -35.51),[], 182),  
#Stastok = Molvat-Berchav Union  
  ("town_17","Stastok",  icon_map_union_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(307.23, -19.48),[], 90),          
#Gammonguard = Entenaii Empire
  ("town_18","Gammonguard",  icon_map_entenaii_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-224.28, 22.09),[], 16),   
#Helhoven = Vitzland Territories (Capital)
  ("town_19","Helhoven", icon_map_vitzland_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.45, -180.75),[], 98),       
#Altenkirchen = Vitzland Territories  
  ("town_20","Altenkirchen", icon_map_vitzland_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.07, -123.06),[], 270),  
#Hoogsel = Vitzland Territories  
  ("town_21","Hoogsel", icon_map_vitzland_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.76, -117.93),[], 330),      
#Kreuzbach = Vitzland Territories  
  ("town_22","Kreuzbach", icon_map_vitzland_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.73, -156.11),[], 225),    
#Rixcester = Entenaii Dominion
  ("town_23","Rixcester",  icon_map_dominion_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.56, 209.06),[], 229),   
#Tarrin = Entenaii Dominion
  ("town_24","Tarrin",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-192.48, -63.68), [], 126),           
#Monmouth = Entenaii Dominion
  ("town_25","Monmouth",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-174.83, 100.52), [], 126),         
#Bredwardine = Entenaii Dominion
  ("town_26","Bredwardine",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-245.28, 339.83), [], 126),      
#Glenarm = Entenaii Dominion
  ("town_27","Glenarm",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.93, -89.53), [], 126),           
#Durrwich = Entenaii Dominion
  ("town_28","Durrwich",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.03, -87.65), [], 126),           
#Aberuthven = Entenaii Dominion
  ("town_29","Aberuthven",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-122.36, -109.03), [], 126),      
#Zalchik = Molvat-Berchav Union
  ("town_30","Zalchik",  icon_map_union_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(224.43, 140.07), [], 126),        
#Moknovci = Molvat-Berchav Union
  ("town_31","Moknovci",  icon_map_union_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(235.53, -165.53), [], 126),
#Andenken = Vitzland Territories
  ("town_32","Andenken",  icon_map_republic_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-106.77, -171.69), [], 126),  
#Domhan Briomhar = Kingdom of Galvae
  ("town_33","Domhan Briomhar",  icon_map_galvae_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.03, -25.88), [], 126),
#Enmamoto = Itami Castedom (Capital)
  ("town_34","Enmamoto",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.1, 154.01), [], 126),           
#Nakashibiro = Itami Castedom
  ("town_35","Nakashibiro",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.4, 294.37), [], 126),       
#Khater = Bashide Confederacy (Capital)
  ("town_36","Khater",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.46, -378.81), [], 126),           
#Abdissu = Bashide Confederacy
  ("town_37","Abdissu",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.46, -415.51), [], 126),           
#
############
##CASTLES###
############

#entenaii
  ("castle_1","Forward_Base_Courage",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.05, -54.12),[],50),
  ("castle_2","Forward_Base_Honour",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-176.41, -78.41),[],75),
  ("castle_3","Forward_Base_Victory",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.05, -66.88),[],100),

#dominion
  ("castle_4","First_Light_Mission",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.67, 225.39),[],180), 
  ("castle_5","Brazen_Mission",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-231.85, 276.89),[],90),
  ("castle_6","Open_Flame_Mission",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-135.46, 110.34),[],55),

#galvae
  ("castle_7","Reimse_Rioga",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(217.03, -119.45),[],45),         
  ("castle_8","Reimse_Crainn",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(134.68, 5.86),[],30),           
  ("castle_9","Reimse_Onoir",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.65, -66.1),[],100),           

#union
  ("castle_10","Podoya_Fortified_Camp",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(283.98, -109.18),[],110), 
  ("castle_11","Zelenopul_Fortified_Camp",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.60, 211.18),[],75),
  ("castle_12","Vyatov_Fortified_Camp",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(141.51, 52.02),[],95),    

#vitzland
  ("castle_13","Kanonenfestung_Messer",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.61, -126.37),[],115),
  ("castle_14","Kanonenfestung_Dolch",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-117.64, -141.03),[],90),
  ("castle_15","Kanonenfestung_Klinge",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.81, -87.38),[],235),

#republic
  ("castle_16","Castel_ci_Oro",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-208.16, -120.82),[],45),
  ("castle_17","Castel_ci_Genta",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.68, -213.61),[],15),
  ("castle_18","Castel_ci_Piree",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.12, -134.04),[],300),

#itami
  ("castle_21","Jol_Ka",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-106.52, 125.18),[],300),
  ("castle_23","Nion_Ka",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72.45, 191.6),[],300),
  ("castle_24","Mit_Ka",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.35, 201.61),[],300),

#Bashide
  ("castle_22","Bashide_Stronghold",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.69, -383.4),[],300),
  ("castle_25","Bashide_Stronghold",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.55, -412.63),[],300),
  ("castle_26","Bashide_Stronghold",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.55, -331.63),[],300),

#irregulars
  ("castle_19","Uprising_Fort",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.02, 61.2),[],300),

#throd
  ("castle_20","War_Church_of_Throd",icon_map_tower|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-378.19, 135.79),[],300),

############
##Villages##
############

##Entenaii_Empire##
  ("village_1", "Dumbarton",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-175.65, -63.54),[], 100), 
  ("village_2", "Burrafirth",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-106.73, -5.8),[], 344),  
  ("village_3", "Blaenau",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.66, 66.4),[], 203),      
  ("village_4", "Warcester",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-131.83, 56.63),[], 152),  
  ("village_5", "Astrakane",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-130.05, -10.48),[], 139),
  ("village_6", "Malrton",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-208.04, 16.37),[], 100),   
  ("village_7", "Carningsby",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-179.2, -4.8),[], 228),   
  ("village_8", "Poltragow",  icon_map_tower|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-155.76, -19.62),[], 155), 
  ("village_9", "Gormsey",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.58, -12.56),[], 352),   
  ("village_10","Coniston",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-230.57, 19.18),[], 170),   
  ("village_11","Beckinsale",  icon_map_farm_4|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-162.61, 49.3),[], 261), 
  ("village_12","Tallyvale",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.62, -31.61),[], 110),  
  ("village_13","Whitebridge",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.65, -49.6),[], 44), 
  ("village_89","Sheviburgh",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129.52, 79.87),[], 0),   
  ("village_90","Birdwell",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-194.24, 39.78),[], 40),    
  ("village_91","Harmstead",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-147.51, -62.02),[], 20),  
  
##Entenaii_Dominion##
  ("village_14","Lushingmire",  icon_map_farm_2|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-227.45,215.84),[], 126),   
  ("village_15","Flamfell",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-241.1, 98.25),[], 170),        
  ("village_16","Mickleton",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.36, 165.39),[], 170),     
  ("village_17","Zelford",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-177.78, 71.61),[], 35),         
  ("village_18","New Gavenston",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-266.34, 272.86),[], 170), 
  ("village_19","Hannfield",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-258.01, 129.63),[], 170),     
  ("village_20","Rickport",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-172.6, 144.9),[], 170),        
  ("village_21","Bendolida",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-170.91, 175.93),[], 100),     
  ("village_22","Shauffield",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-203.82, 212.58),[], 110),    
  ("village_23","Leadenglen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-205.26, 95.59),[], 152),     
  ("village_24","Dilloguard",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-195.58, 167.09),[], 334),    
  ("village_25","Redport",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-202.7, 326.92),[], 170),        
  ("village_26","Labopoint",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-235.63, 69.66),[], 170),      
  ("village_27","Duffercairn",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-231.48, 112.52),[], 218),   
  ("village_28","Polyton",  icon_map_farm_2|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-262.73, 84.62),[], 142),       
  ("village_29","Duchelm",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-177.81, 286.72),[], 73),        
  ("village_30","Titferglen",  icon_map_tower|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-309.16, 48.38),[], 170),     
  ("village_31","Beakhallow",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-264.14, 26.93),[], 295),     
  ("village_32","Gougeburg",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-243.93 , 316.73 ),[], 104),  
  ("village_33","Vanham",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-285.23, 85.34),[], 193),        
  ("village_88","Tubthumpton",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-153.36, 221.97),[], 44),    
  ("village_105","Valeshire",  icon_map_house|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-231.94, 142.83),[], 297),    
  ("village_92","Alcombey",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-301.04, 333.61),[], 60),       
  ("village_93","Rotherhithe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-275.24, 363.73),[], 55),    
  ("village_94","Croydon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-205.44, 245.14),[], 15),        
  
##Kingdom_of_Galvae##
  ("village_34","Peigin Ui Duillearga",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.74, -11.69),[], 218),         
  ("village_35","Fionnuala Ui Se",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(205.17, -2.69),[], 268),              
  ("village_36","Caoimhe Ni Se",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(190.7, -134.61),[], 170),               
  ("village_37","Duibheasa Ui Dubhagain",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(162.82, -170.91),[], 261),     
  ("village_38","Blinne Ui Meara",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(91.26, -50.86),[], 29),               
  ("village_39","Odharnait Nic Cosgair",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(134.71, -161.84),[], 307),      
  ("village_40","Barrdhubh Nic Gaibhtheachain",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(136.26, -44.02),[], 170),
  ("village_41","Maire Ui Maoil Mhichil",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106.29, -102.62),[], 100),     
  ("village_42","Teide Nic Cruadhlaoich",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(196.99, -83.61),[], 313),      
  ("village_43","Eilin Nic Amhlaidh",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(181.26, -61.48),[], 18),           
  ("village_44","Guibheasa Ui Hubhagain",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(51.8, -50),[], 130),
  ("village_45","Cuibh Ui Mubain",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(151.5, -3),[], 170),
  ("village_46","Tasa Ui Gain",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.29, -87.74),[], 170),                
  ("village_95","Mag na Blathanna",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.72, 10.37),[], 10),               
  ("village_97","Tir Ceilte",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(224.99, -69.37),[], 160),                  
  ("village_98","Mag na Nathracha",  icon_map_wooden_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(164.4, -131.88),[], 180),            
  
##Molvat-Berchav_Union##
  ("village_47","Zhabisty",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(260.18, 278.18),[], 216),   
  ("village_48","Luninpolatsk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.74, 216.73),[], 39),
  ("village_49","Komastovo",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.4, 62.17),[], 10),      
  ("village_50","Poprance",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(293.39, -88.48),[], 170),   
  ("village_51","Hrasko",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.27, 169.87),[], 328),     
  ("village_52","Sharliaky",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120.91, 245.29),[], 110),  
  ("village_53","Parbice",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.28, 127.04),[], 65),    
  ("village_54","Varlany",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(274.12, 64.31),[], 204),    
  ("village_55","Hajhalas",  icon_map_dest_city|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(194.15, 199.56),[], 53),
  ("village_56","Elknovo",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(146.54, 157.96),[], 170),    
  ("village_57","Hosytvit",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(150.59, 78.02),[], 243),    
  ("village_58","Wloclawek",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.50, 182.76),[], 190),   
  ("village_59","Stalonicza",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(122.69, 316.21),[], 278), 
  ("village_60","Harghiol",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(251.47, 9.5),[], 326),      
  ("village_61","Mangavasna",  icon_map_house|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(285.9, -52.61),[], 100),  
  ("village_62","Murlija",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.25, 243.91),[], 100),     
  ("village_63","Andrutrov",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.09, 129.21),[], 100),  
  ("village_96","Evsitke",  icon_map_farm_1|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.97, 178.13),[], 116),   
  ("village_99","Balanomyssk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.22, 146.51),[], 0),  
  ("village_100","Saronza",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(215.55, 53.02),[], 40),     
  ("village_101","Batatity",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(154.45, 260.76),[], 20),   
  ("village_109","Birozuluk",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.76, 124.47),[], 0),    
  ("village_110","Zhukomna",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.34, 264.53),[], 40),    

##Empire_of_Vitzland##
  ("village_64","Kitzfeld",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-86.63, -175.3),[], 100),      
  ("village_65","Neunfeld",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.55, -92.8),[], 100),      
  ("village_66","Tourvoorde",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.31, -167.69),[], 100),    
  ("village_67","Avilun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.38, -142.89),[], 100),       
  ("village_68","Richtenwerder",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.71, -130.92),[], 100),
  ("village_69","Munchenthal",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.21, -142.28),[], 100),   
  ("village_70","Klostermarkt",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.18, -130.74),[], 100), 
  ("village_71","Gailstein",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.15, -157.64),[], 20),    
  ("village_72","Hoogezijl",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.09, -206.92),[], 60),      
  ("village_73","Freikkon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.69, -130.94),[], 55),       
  ("village_74","Maasschede",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.24, -170.31),[], 15),    
  ("village_75","Isselbeuren",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.36, -119.82),[], 10),   
  ("village_102","Kirchnitz",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.55, -150.92),[], 60),    
  ("village_103","Munzenhoring",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.43, -116.56),[], 55),  
  ("village_104","Reimunster",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.44, -111.99),[], 15),     
  
##Trezzo_Republic##
  ("village_76","Vallanse",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.6, -233.86),[], 105),   
  ("village_77","Badava",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-222.19, -173.61),[], 160),    
  ("village_78","Aveirante",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-243.21, -214.09),[], 180),
  ("village_79","Garano",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-119.83, -262.72),[], 0),      
  ("village_80","Casotri",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-266.27, -196.56),[], 40),    
  ("village_81","Fatirante",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-260, -167.18),[], 20),    
  ("village_82","Bolora",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.69, -185.2),[], 60),      
  ("village_83","Trenremo",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-168.6, -178.49),[], 55),    
  ("village_84","Guidoceno",  icon_map_bunker|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-164.95, -315.06),[], 15), 
  ("village_85","Ceretta",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-196.09, -121.5),[], 10),     
  ("village_86","Netalina",  icon_village_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-101.8, -240.18),[], 35),    
  ("village_87","Riogoza",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-167.47, -288.54),[], 100),   
  ("village_106","Santatima",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132.41, -91.0),[], 35),   
  ("village_107","Barcejara",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-194.36, -182.49),[], 160),
  ("village_108","Bragarta",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129.99, -224.4),[], 180),  
  
##Mines##
##Entenaii_Empire
  ("entenaii_empire_mine_iron","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-189.18, -0.64),[]),  
  ("entenaii_empire_mine_coal","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-119.81, -29.32),[]), 

##Entenaii_Dominion
  ("entenaii_dominion_mine_iron","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-261.91, 118.97),[]), 
  ("entenaii_dominion_mine_coal","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-231.07, 326.12),[]), 

##Kingdom_of_Galvae##
  ("galvae_mine_iron","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.13, -79.19),[]),
  ("galvae_mine_coal","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.96, -8.34),[]),  
  
##Molvat-Berchav_Union##
  ("union_mine_iron","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120.4, 99.26),[]),  
  ("union_mine_coal","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(238.61, 248.06),[]),
  
##Empire_of_Vitzland##
  ("vitzland_mine_iron","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.93, -159.8),[]),
  ("vitzland_mine_coal","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.78, -139.79),[]),
  
##Trezzo_Republic##
  ("republic_mine_iron","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.79, -278.05),[]),
  ("republic_mine_coal","Iron_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-163.08, -157.08),[]),

#extra

  ("salt_mine","Baren's_Mine",icon_bandit_lair|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.75, 150.94),[]),
  #
  ("arena_1","The Grand Melee",icon_map_mercenary_camp|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.64,12.59),[],282),
  # ("arena_1","No Tales Ground",icon_map_tower2|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.15,-0.38),[],282),
  # ("arena_2","Tribute Ground",icon_map_tower|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.2, -31),[]),
  # ("arena_3","Grand Arc Arena",icon_map_tower2|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.2, -31),[]),
  # ("arena_4","Cinder Ring",icon_map_tower|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -25),[]),

  ("starting_point","Abandoned Factory",icon_map_factory|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.45, 76.04),[],42), #(-35.19,-9.69)
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(335.00, 335.00),[]),

  ("bridge_a_a","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-51.87,203.54),[],71),  
  ("bridge_a_b","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(52.46,-120.01),[],121), 
  ("bridge_a_c","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-34.8,198.24),[],244),  
  ("bridge_a_d","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-123.94,197.11),[],101),
  ("bridge_a_e","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(136.99,22.18),[],155),  
  ("bridge_a_f","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-34.47,-7.13),[],115),  
  ("bridge_a_g","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-245.86,260.31),[],111),
  ("bridge_a_h","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-275.14,254.29),[],95), 
  ("bridge_a_i","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-284.33,337.93),[],121),
  ("bridge_a_j","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-25.08,33.68),[],132),  
  ("bridge_a_k","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(223.1,-127.98),[],246), 
  ("bridge_a_l","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(211.71,-108.9),[],70),  
  ("bridge_a_m","bridge_a_a",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-118.05,136.98),[],109),

  ("bridge_b_a","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-116.66,82.34),[],238), 
  ("bridge_b_b","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-103.87,191.08),[],352),
  ("bridge_b_c","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-178.84,23.1),[],246),      
  ("bridge_b_d","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-150.45,201.54),[],17),     
  ("bridge_b_e","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-199.24,223.84),[],234),    
  ("bridge_b_f","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-157.23,246.83),[],7),      
  ("bridge_b_g","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-144.77,49.34),[],239),     
  ("bridge_b_h","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-76.86,185.3),[],344),      
  ("bridge_b_i","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(112.58,-122.57),[],235),    
  ("bridge_b_j","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-196.63,202.8),[],0),       
  ("bridge_b_k","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(149.49,-115.11),[],2),      
  ("bridge_b_l","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-57.2,-135.94),[],3),       
  ("bridge_b_m","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-15.68,-81.16),[],289),     
  ("bridge_b_n","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-0.4,-100.71),[],22),       
  ("bridge_b_o","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(96.32,-23.15),[],20),       
  ("bridge_b_p","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-67.92,178.28),[],297),     
  ("bridge_b_q","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-197.13,-98.42),[],9),      
  ("bridge_b_r","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-83.13,125.19),[],255),     
  ("bridge_b_s","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-80.79,144.1),[],209),      
  ("bridge_b_t","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-99.37,123.65),[],239),     
  ("bridge_b_u","bridge_b_a",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-76.46,-179.28),[],307),    

  ("map_boat_1a","map_boat_1a",icon_map_boat_1|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-27.56,-282.32),[],209), #[swycartographr] prev. coords: (-194.49, -12.37)
  ("map_boat_1b","map_boat_1a",icon_map_boat_1|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(221.75,-110.39),[],299), #[swycartographr] prev. coords: (43.88, 208.73)
  ("map_boat_1c","map_boat_1a",icon_map_boat_1|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(28.22,292.34),[],191), #[swycartographr] prev. coords: (41.87, 162.79)
  ("map_boat_1d","map_boat_1a",icon_map_boat_1|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-223.96,204.8),[],277), #[swycartographr] prev. coords: (-268.92, 157.3)
  ("map_boat_1e","map_boat_1a",icon_map_boat_1|pf_is_static|pf_always_visible|pf_no_label,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-35.47,270.08),[],290), #[swycartographr] prev. coords: (-280.67, 202.02) #[swycartographr] prev. coords: (-45.36, 194.97) #[swycartographr] prev. coords: (-33, 234)

#secret_bases
  ("map_secret_base_shadow","Hidden_Bunker",icon_map_bunker|pf_is_static|pf_hide_defenders,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-99.53,-95.68),[],131), #[swycartographr] prev. coords: (-62.09, 173.59)
  ("map_secret_base_throd","Throd_Chapel",icon_map_monastery|pf_is_static|pf_hide_defenders,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-346.74,225.25),[],345), #[swycartographr] prev. coords: (126.07, -56.15) #[swycartographr] prev. coords: (157.17, -88.26)
  ("map_secret_base_irregular","Renegade_Forward_Camp",icon_map_mercenary_camp|pf_is_static|pf_hide_defenders,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-54.61,-23.39),[],237), #[swycartographr] prev. coords: (-182.52, 51.84) #[swycartographr] prev. coords: (-174.7, 52.52)
  ("map_secret_base_legion","Hall_of_the_Fallen_Legion",icon_bandit_lair|pf_is_static|pf_hide_defenders,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-86.96,248.73),[],192), #[swycartographr] prev. coords: (-80.59, -35.77)
  ("map_secret_base_ezeg","Ezeg_Lair",icon_bandit_lair|pf_is_static|pf_hide_defenders,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-16.88,-177.79),[],303), #[swycartographr] prev. coords: (-246.77, 151.74) #[swycartographr] prev. coords: (-232.62, 110.74)
  ("map_secret_base_yanizar","yanizar_Camp",icon_bandit_camp|pf_is_static|pf_hide_defenders,no_menu,pt_none,fac_neutral,0,ai_bhvr_hold,0,(-97.83,-202.97),[],303), #[swycartographr] prev. coords: (-246.77, 151.74) #[swycartographr] prev. coords: (-232.62, 110.74)


#
  ("map_razed_city_1", "RAZED CITY", icon_map_razed_city|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0,(11.29, 49.86), [], 126),  #[swycartographr] prev. coords: (5.68, 89.59) #[swycartographr] prev. coords: (234.58, -145.79) #[swycartographr] prev. coords: (77.08, -125.28) #[swycartographr] prev. coords: (41.95, -24.53)
#
  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(26, 77),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(125, 9),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(78, 84),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-35, 18),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","the highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-90, -26.8),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(85.59, 106.26),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-42, 76.7),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(110, -100),[(trp_looter,15,0)]),
 # add extra towns before this point
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., -29.25),[(trp_looter,15,0)]), 
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., -25.77),[(trp_looter,15,0)]),       
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 35.93),[(trp_looter,15,0)]),        
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., -32.28),[(trp_looter,15,0)]),       
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., -43.65),[(trp_looter,15,0)]),       
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., -23.53),[(trp_looter,15,0)]),       

  ("outpost_1", "Outpost", icon_map_camp_2|pf_disabled|pf_is_static|pf_always_visible, no_menu, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (-51.99, 51.91), []),
  ("outpost_2", "Outpost", icon_map_camp_2|pf_disabled|pf_is_static|pf_always_visible, no_menu, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (-49.03, 57.4), []), 
  # ("map_volcano", "volcano", icon_map_dummy|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (285.4, -9.95), [], 174),

  ("vehicles", "Vehicles", icon_map_dummy|pf_disabled|pf_is_static|pf_always_visible, no_menu, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (-55.71, 46.79), []),


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
