from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

from compiler import *
####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,10,20)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

  ("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_manhunter,10,60)]),
#mercs
  ("merc_party","Mercenary Party",icon_axeman|carries_goods(2),0,fac_commoners,soldier_personality,[]),  

#raiders
  ("looters","Looters",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,10,200)]),
  
  ("fallen_phalanx","Fallen_Phalanx",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[]),
  ("shadow_operatives","Shadow_Operatives",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[]),
  ("ezeg_pirates","Ezeg_Pirates",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[]),

  ("plunderer","Plunderers",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[]),  
  ("raiders","Raiders",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[]),  
  ("wasteland_raiders","Rogue_Adventurers",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[]),  
  ("bandit_gang","Gangsters",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[]),  
  ("jackal_raiders","Boar Raiders",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[]),
  ("scavenge_template","Deserters",icon_axeman|carries_goods(3),0,fac_outlaws,bandit_personality,[]),  
  ("church_extremists","Cultists of Throd",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_zealot,1,5)]),

  ("steppe_bandits","Peasant Rebels",icon_peasant|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_farmer,10,50),(trp_peasant_woman,10,50)]),
  ("taiga_bandits","Nomads",icon_peasant|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_farmer,10,50),(trp_peasant_woman,10,50)]),
  ("desert_bandits","Hostile Settlers",icon_peasant|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_traveler,10,50),(trp_traveler_w,10,50)]),
  
  ("forest_bandits","Revolutionaries",icon_axeman|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_blades_warrior,4,200)]),
  ("mountain_bandits","Tattoo Gang",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_the_suits,4,90)]),
  ("sea_raiders","White Scarves",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_sea_raider,5,100)]),
  
  ("cannibals","Cannibals",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_cannibal,5,50)]),

  ("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),  
#infected
  ("infected", "Miasma-stricken Mob", icon_axeman|carries_goods(2), 0, fac_infected, bandit_personality, [(trp_infected_1, 10, 75),(trp_infected_2, 5, 30),(trp_infected_3, 2, 15),(trp_infected_6, 1, 5)]),
  ("infected_scavengers", "Miasma-stricken Swarm", icon_axeman|carries_goods(2), 0, fac_infected, bandit_personality, [(trp_infected_1, 15, 100),(trp_infected_2, 10, 75),(trp_infected_3, 5, 50),(trp_infected_4, 10, 25),(trp_infected_6, 1, 8)]),
  ("infected_soldiers", "Miasma-stricken Horde", icon_axeman|carries_goods(2), 0, fac_infected, bandit_personality, [(trp_infected_1, 25, 175),(trp_infected_2, 20, 120),(trp_infected_3, 15, 100),(trp_infected_4, 10, 25),(trp_infected_5, 20, 45),(trp_infected_6, 2, 10)]),

#undead
  ("undead", "Roaming Undead", icon_axeman|carries_goods(2), 0, fac_undeads, bandit_personality, [(trp_undead_1, 50, 250),(trp_risen, 25, 125),(trp_risen_tainted, 10, 50),(trp_risen_cursed, 1, 10)]),

#mutants
  ("spitters", "Spitters", icon_axeman|carries_goods(2), 0, fac_mutants, bandit_personality, [(trp_spitter, 5, 35)]),
  ("wolfclaw_mutants", "Howling Horrors", icon_axeman|carries_goods(2), 0, fac_mutants, bandit_personality, [(trp_wolfclaw_mutant,5, 50),(trp_wolfclaw_mutant_big,1, 10)]),
  ("brute_mutants", "Brutes", icon_axeman|carries_goods(2), 0, fac_mutants, bandit_personality, [(trp_brute_mutant,5, 15),(trp_tank_mutant,5, 12)]),
  ("ghouls", "Ghouls", icon_axeman|carries_goods(2), 0, fac_mutants, bandit_personality, [(trp_ghoul_scavenger, 5, 15),(trp_ghoul, 10, 60)]),
  ("rancors", "Horse-Eaters", icon_axeman|carries_goods(2), 0, fac_mutants, bandit_personality, [(trp_rancor, 5, 20)]),
  
  ("ghouls_army", "Ghouls", icon_axeman|carries_goods(2), 0, fac_mutants, bandit_personality, [(trp_ghoul, 250, 1000)]),
  
  ("throd_army", "Throd Invasion Force", icon_axeman|carries_goods(2), 0, fac_theocracy, bandit_personality, [(trp_cultist, 350,750),(trp_fanatic, 150,500),(trp_zealot, 25,75)]),

#factions
  # ("faction_scouts","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
#others
  ("messenger","Messenger",icon_peasant|pf_civilian,0,fac_commoners,merchant_personality,[]),
  ("player_caravan","Caravan (owned)",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,10,50)]),
    
  ("merchant_caravan","Merchant Caravan",icon_mule|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("village_farmers","Travellers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),
  ("refugees","Refugees",icon_peasant|pf_civilian,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,6,16)]),

  ("spy_partners", "Unremarkable Travellers", icon_player|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_player|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),

  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),

  ("messenger_party","Messenger",icon_flagbearer_b|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",icon_vaegir_knight,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
  ("center_reinforcements","Reinforcements", icon_axeman|pf_show_faction|carries_goods(4),0,fac_commoners,escorted_merchant_personality,[]),

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

  ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_f1_tier_0,20,50)]),
  ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_f1_tier_0,20,50),(trp_f1_tier_1,2,5),(trp_f1_tier_2,1,3)]),
  ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_f1_tier_0,20,50),(trp_f1_tier_3,2,5),(trp_f1_tier_4,2,4),(trp_f1_tier_4_cavalry,1,2)]),
  ("kingdom_1_reinforcements_d", "{!}kingdom_1_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_f1_tier_0,20,50),(trp_f1_tier_5,1,2),(trp_f1_tier_5_infantry,1,2),(trp_f1_tier_5_cavalry,1,2),(trp_f1_tier_6_sniper,1,2)]),
  ("kingdom_1_reinforcements_e", "{!}kingdom_1_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_f1_tier_0,20,50),(trp_f1_terror,1,2)]),

  ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_f2_tier_0,20,50)]),
  ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_f2_tier_0,20,50),(trp_f2_tier_1,2,5),(trp_f2_tier_2,1,3)]),
  ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_f2_tier_0,20,50),(trp_f2_tier_3,2,5),(trp_f2_tier_4,2,4),(trp_f2_fanatic,2,4)]),
  ("kingdom_2_reinforcements_d", "{!}kingdom_2_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_f2_tier_0,20,50),(trp_f2_tier_5,1,2),(trp_f2_rider,1,2),(trp_f2_flamer,1,2)]),
  ("kingdom_2_reinforcements_e", "{!}kingdom_2_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_f2_tier_0,20,50),(trp_f2_terror,1,2)]),

  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_f3_tier_0,20,50)]),
  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_f3_tier_0,20,50),(trp_f3_tier_1,2,5),(trp_f3_tier_2,1,3)]),
  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_f3_tier_0,20,50),(trp_f3_tier_3,2,5),(trp_f3_tier_4,2,4),(trp_f3_infantry,2,4),(trp_f3_rider,1,3)]),
  ("kingdom_3_reinforcements_d", "{!}kingdom_3_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_f3_tier_0,20,50),(trp_f3_tier_5,1,2),(trp_f3_vet_rider,1,2)]),
  ("kingdom_3_reinforcements_e", "{!}kingdom_3_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_f3_tier_0,20,50),(trp_f3_terror,1,2)]),
  
  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_f4_tier_0,20,50)]),
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_f4_tier_0,20,50),(trp_f4_tier_1,2,5),(trp_f4_tier_2,1,3)]),
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_f4_tier_0,20,50),(trp_f4_tier_3,2,5),(trp_f4_tier_3b,2,5),(trp_f4_tier_4,2,4),(trp_f4_tier_4_cavalry,2,4)]),
  ("kingdom_4_reinforcements_d", "{!}kingdom_4_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_f4_tier_0,20,50),(trp_f4_tier_5,1,2),(trp_f4_tier_5_cavalry,1,2),(trp_f4_tier_6_cavalry,1,2),(trp_f4_flamer,1,2),(trp_f4_tier_6,1,2)]),
  ("kingdom_4_reinforcements_e", "{!}kingdom_4_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_f4_tier_0,20,50),(trp_f4_terror,1,2)]),
  
  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_f5_tier_0,20,50)]),
  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_f5_tier_0,20,50),(trp_f5_tier_1,2,5),(trp_f5_tier_2,1,3)]),
  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_f5_tier_0,20,50),(trp_f5_tier_3,2,5),(trp_f5_rider,1,2),(trp_f5_tier_4,2,4),(trp_f5_flamer,2,4)]),
  ("kingdom_5_reinforcements_d", "{!}kingdom_5_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_f5_tier_0,20,50),(trp_f5_tier_5,1,2),(trp_f5_gunner,1,2),(trp_f5_rider_vet,1,2),(trp_f5_tier_6,1,2)]),
  ("kingdom_5_reinforcements_e", "{!}kingdom_5_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_f5_tier_0,20,50),(trp_f5_terror,1,2)]),
  
  ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_f6_tier_0,20,50)]),
  ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_f6_tier_0,20,50),(trp_f6_tier_1,2,5),(trp_f6_tier_2,1,3)]),
  ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_f6_tier_0,20,50),(trp_f6_tier_3,2,5),(trp_f6_tier_4,2,4),(trp_f6_rider,2,4)]),
  ("kingdom_6_reinforcements_d", "{!}kingdom_6_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_f6_tier_0,20,50),(trp_f6_tier_5,2,4),(trp_f6_tier_6,1,2)]),
  ("kingdom_6_reinforcements_e", "{!}kingdom_6_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_f6_tier_0,20,50),(trp_f6_terror,1,2)]),

  ("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_f7_tier_0,20,50)]),
  ("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_f7_tier_0,20,50),(trp_f7_tier_1,2,5),(trp_f7_tier_2,1,3)]),
  ("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_f7_tier_0,20,50),(trp_f7_tier_3,2,5),(trp_f7_tier_4,2,4),(trp_f7_rider,2,4)]),
  ("kingdom_7_reinforcements_d", "{!}kingdom_7_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_f7_tier_0,20,50),(trp_f7_tier_5,2,4),(trp_f7_tier_6,1,2)]),
  ("kingdom_7_reinforcements_e", "{!}kingdom_7_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_f7_tier_0,20,50),(trp_f7_terror,1,2)]),

#
  ("irregulars_reinforcements_a", "{!}irregulars_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_irregular_tier_0,20,50)]),
  ("irregulars_reinforcements_b", "{!}irregulars_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_irregular_tier_0,20,50),(trp_irregular_tier_1,2,5),(trp_irregular_tier_2,1,3)]),
  ("irregulars_reinforcements_c", "{!}irregulars_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_irregular_tier_0,20,50),(trp_irregular_tier_3,2,5),(trp_irregular_tier_4,2,4),(trp_irregular_rider,1,2)]),
  ("irregulars_reinforcements_d", "{!}irregulars_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_irregular_tier_0,20,50),(trp_irregular_tier_5,2,4),]),
  ("irregulars_reinforcements_e", "{!}irregulars_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_irregular_tier_0,20,50),(trp_irregular_terror,1,2)]),
#
  ("throd_reinforcements_a", "{!}throd_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_throd_tier_0,20,50)]),
  ("throd_reinforcements_b", "{!}throd_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_throd_tier_0,20,50),(trp_throd_tier_1,2,5),(trp_throd_tier_2,1,3)]),
  ("throd_reinforcements_c", "{!}throd_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_throd_tier_0,20,50),(trp_throd_tier_3,2,5),(trp_throd_tier_4,2,4),(trp_throd_rider,1,2)]),
  ("throd_reinforcements_d", "{!}throd_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_throd_tier_0,20,50),(trp_throd_tier_5,2,4),]),
  ("throd_reinforcements_e", "{!}throd_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_throd_tier_0,20,50),(trp_throd_terror,1,2)]),

  # ("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58)]),
  # ("taiga_bandit_lair","Tundra Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
  # ("desert_bandit_lair" ,"Desert Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
  # ("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
  # ("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
  # ("sea_raider_lair","Sea Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,50)]),
  # ("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),
  
  # ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

  # ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),

# Merc Camp
  # ("geroian_company", "White Cross_Patrol", icon_gray_knight|carries_goods(2), 0, fac_geroia, soldier_personality, [(trp_whitecross_sergeant, 1, 1),(trp_whitecross_swordsman, 7, 21),(trp_whitecross_pavisier, 7, 15)]),
  # ("geroian_army", "White Cross_Company", icon_gray_knight|carries_goods(5), 0, fac_geroia, soldier_personality, [(trp_whitecross_sergeant, 15, 28),(trp_whitecross_swordsman, 50, 100),(trp_whitecross_pavisier, 25, 50)]),

  # ("balion_company", "WY Co. Patrol", icon_gray_knight|carries_goods(2), 0, fac_balion, soldier_personality, [(trp_redcross_knight, 1, 2),(trp_redcross_longbowman, 7, 21),(trp_redcross_infantry, 7, 15)]),
  # ("balion_army", "WY Co. Fleet", icon_gray_knight|carries_goods(5), 0, fac_balion, soldier_personality, [(trp_redcross_knight, 15, 25),(trp_redcross_longbowman, 50, 100),(trp_redcross_infantry, 25, 50)]),

  # ("jumne_company", "Brotherhood of the Coast Raiders", icon_axeman|carries_goods(2), 0, fac_jumne, soldier_personality, [(trp_jumne_raider, 9, 25),(trp_jumne_skirmisher, 5, 12)]),
  # ("jumne_army", "Brotherhood of the Coast Fleet", icon_axeman|carries_goods(5), 0, fac_jumne, soldier_personality, [(trp_jumne_raider, 50, 120),(trp_jumne_skirmisher, 25, 50)]),

  # ("adventurer_company", "Warriors", icon_gray_knight|carries_goods(2), 0, fac_adventurers, soldier_personality, [(trp_zendar_infantry, 15, 50)]),
  # ("adventurer_army", "War Party", icon_gray_knight|carries_goods(5), 0, fac_adventurers, soldier_personality, [(trp_zendar_infantry, 70, 170)]),

# ("geroian_company", "Geroian Patrol", icon_axeman|carries_goods(2), 0, fac_geroia, soldier_personality, [(trp_geroia_sergeant,1,10),(trp_geroia_swordsman,25,90),(trp_geroia_pavisier,24,50)] ),
# ("geroian_army","Geroian Company",icon_gray_knight|carries_goods(5),0,fac_geroia,soldier_personality,[(trp_geroia_sergeant,50,50),(trp_geroia_swordsman,150,150),(trp_geroia_pavisier,100,100)]),

# ("balion_company", "Balion Patrol", icon_axeman|carries_goods(2), 0, fac_balion, soldier_personality, [(trp_balion_knight,1,10),(trp_balion_infantry,25,90),(trp_balion_longbowman,24,50)] ),
# ("balion_army","Balion Company",icon_gray_knight|carries_goods(5),0,fac_balion,soldier_personality,[(trp_balion_knight,50,50),(trp_balion_infantry,150,150),(trp_balion_longbowman,100,100)]),

# ("jumne_company", "Jumne Raiders", icon_axeman|carries_goods(2), 0, fac_jumne, soldier_personality, [(trp_jumne_huscarl,1,10),(trp_jumne_raider,25,90),(trp_jumne_skirmisher,24,50)] ),
# ("jumne_army","Jumne Army",icon_axeman|carries_goods(5),0,fac_jumne,soldier_personality,[(trp_jumne_huscarl,100,100),(trp_jumne_raider,100,100),(trp_jumne_skirmisher,100,100)]),

# ("adventurer_army","Steel Company",icon_gray_knight|carries_goods(5),0,fac_adventurers,soldier_personality,[(trp_hired_blade,40,40),(trp_mercenary_swordsman,40,40),(trp_mercenary_spear_thrower,40,40),(trp_mercenary_crossbowman,40,40),(trp_mercenary_horseman,20,20),(trp_mercenary_cavalry,20,20)]),
  # ("adventurer_company", "Adventurers", icon_gray_knight|carries_goods(2), 0, fac_adventurers, soldier_personality, [(trp_mercenary_cavalry, 1, 5),(trp_hired_blade, 7, 21),(trp_mercenary_crossbowman, 5, 15)]),
  # # ("adventurer_army", "Steel Company", icon_gray_knight|carries_goods(5), 0, fac_adventurers, soldier_personality, [(trp_mercenary_cavalry, 15, 28),(trp_hired_blade, 50, 100),(trp_mercenary_crossbowman, 25, 50)]),

# Merc Camp end
# Merc Camp Begin
# ("merc_camp_geroia_troops", "{!}Geroian Mercs", 0, 0, fac_commoners, 0, [(trp_whitecross_swordsman,5,10),(trp_whitecross_pikeman,4,8),(trp_whitecross_pavisier,4,8),(trp_whitecross_sergeant,1,2)]),
# ("merc_camp_balion_troops", "{!}Balion Mercs", 0, 0, fac_commoners, 0, [(trp_redcross_longbowman,5,12),(trp_redcross_infantry,4,10),(trp_redcross_knight,1,6)]),
# ("merc_camp_jumne_troops", "{!}Jumne Mercs", 0, 0, fac_commoners, 0, [(trp_jumne_raider,5,12),(trp_jumne_skirmisher,4,10)]),
# ("merc_camp_zendar_troops", "{!}Zendar Mercs", 0, 0, fac_commoners, 0, [(trp_zendar_infantry,12,30)]),
# ("merc_camp_arab_troops", "{!}Sandstorm Mercs", 0, 0, fac_commoners, 0, [(trp_desert_bandit,15,40)]),
# ("merc_camp_horde_troops", "{!}Horde Mercs", 0, 0, fac_commoners, 0, [(trp_black_khergit_horseman,12,30),(trp_black_khergit_guard,5,15)]),
# Merc Camp End
  
   ##diplomacy begin
  ("dplmc_spouse","Your spouse",icon_woman_b|pf_civilian|pf_show_faction,0,fac_neutral,merchant_personality,[]),

  ("dplmc_gift_caravan","Your Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
#recruiter kit begin
   ("dplmc_recruiter","Recruiter",icon_flagbearer_b|pf_show_faction,0,fac_neutral,merchant_personality,[(trp_dplmc_recruiter,1,1)]),
#recruiter kit end
   ##diplomacy end
]
# modmerger_start version=201 type=2
try:
    component_name = "party_templates"
    var_set = { "party_templates" : party_templates }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
