import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

from names import *
# from random_troops import *

# from compiler import *
####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Troop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin fort's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
####################################################################################################################
def_attrib = str_7 | agi_5 | int_4 | cha_4

#Attributes / Skills
attr_lvl_1 =  str_7| agi_5| int_4| cha_4|level(1) #4
wp_start = wp(50)

attr_lvl_5 =  str_9| agi_7| int_4| cha_4|level(5) #8
knows_common = knows_inventory_management_2|knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_power_strike_1|knows_power_throw_1|knows_power_draw_1|knows_horse_archery_5
wp_common = wp_m(100)

attr_lvl_10 = str_11| agi_8| int_5| cha_5|level(10) #14
knows_battle_1 = knows_inventory_management_2|knows_weapon_master_2|knows_riding_2|knows_athletics_2|knows_power_strike_2|knows_power_throw_2|knows_power_draw_2|knows_horse_archery_5
wp_1_m = wp_m(125)
wp_1_r = wp_r(125)

attr_lvl_15 = str_14|agi_10| int_5| cha_5|level(15) #19
knows_battle_2 = knows_shield_1|knows_inventory_management_2|knows_weapon_master_2|knows_riding_2|knows_athletics_3|knows_power_strike_3|knows_power_throw_3|knows_power_draw_3|knows_horse_archery_5
wp_2_m = wp_m(150)
wp_2_r = wp_r(150)

attr_lvl_20 = str_16|agi_11| int_6| cha_6|level(20)
knows_battle_3 = knows_ironflesh_3|knows_shield_2|knows_inventory_management_2|knows_weapon_master_3|knows_riding_3|knows_athletics_3|knows_power_strike_4|knows_power_throw_4|knows_power_draw_4|knows_horse_archery_5
wp_3_m = wp_m(200)
wp_3_r = wp_r(200)

attr_lvl_25 = str_19|agi_13| int_6| cha_6|level(25)
knows_battle_4 = knows_ironflesh_3|knows_shield_3|knows_inventory_management_2|knows_weapon_master_4|knows_riding_3|knows_athletics_4|knows_power_strike_5|knows_power_throw_5|knows_power_draw_5|knows_horse_archery_5
wp_4_m = wp_m(250)
wp_4_r = wp_r(250)

attr_lvl_30 = str_21|agi_14|int_7|cha_7|level(30)
knows_battle_5 = knows_ironflesh_5|knows_shield_4|knows_inventory_management_2|knows_weapon_master_4|knows_riding_3|knows_athletics_4|knows_power_strike_6|knows_power_throw_6|knows_power_draw_6|knows_horse_archery_5
wp_5_m = wp_m(300)
wp_5_r = wp_r(300)

attr_lvl_35 = str_24|agi_16|int_7|cha_7|level(35)
knows_battle_6 = knows_ironflesh_6|knows_shield_5|knows_inventory_management_2|knows_weapon_master_5|knows_riding_5|knows_athletics_5|knows_power_strike_7|knows_power_throw_7|knows_power_draw_7|knows_horse_archery_5
wp_6_m = wp_m(350)
wp_6_r = wp_r(350)

attr_lvl_40 = str_27|agi_17|int_8|cha_8|level(40)
knows_battle_7 = knows_ironflesh_7|knows_shield_6|knows_inventory_management_2|knows_weapon_master_6|knows_riding_6|knows_athletics_6|knows_power_strike_8|knows_power_throw_8|knows_power_draw_8|knows_horse_archery_6
wp_6_m = wp_m(400)
wp_6_r = wp_r(400)

attr_lvl_45 = str_30|agi_19|int_8|cha_8|level(45)
knows_battle_8 = knows_ironflesh_8|knows_shield_7|knows_inventory_management_3|knows_weapon_master_7|knows_riding_7|knows_athletics_7|knows_power_strike_9|knows_power_throw_9|knows_power_draw_9|knows_horse_archery_7
wp_7_m = wp_m(450)
wp_7_r = wp_r(450)

attr_terror = str_75|agi_25|int_10|cha_10|level(50)

attr_tank = str_128|agi_30|int_4|cha_4|level(60)
knows_tank = knows_ironflesh_10|knows_shield_10|knows_inventory_management_1|knows_weapon_master_5|knows_riding_5|knows_athletics_5|knows_power_strike_10|knows_power_throw_5|knows_power_draw_5|knows_horse_archery_5

knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_10|knows_persuasion_4|knows_power_strike_2|knows_shield_2|knows_weapon_master_3|knows_ironflesh_3|knows_athletics_4|knows_leadership_1|knows_wound_treatment_2|knows_first_aid_2|knows_surgery_2|knows_power_throw_2|knows_spotting_3|knows_pathfinding_4|knows_horse_archery_5
knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_2|knows_athletics_5|knows_riding_6|knows_power_strike_1|knows_shield_2|knows_inventory_management_5|knows_power_throw_1|knows_horse_archery_5 #cambiado chief
#knows_tracker_npc = knows_weapon_master_1|knows_ironflesh_9|knows_athletics_4|knows_riding_3|knows_spotting_9|knows_pathfinding_9|knows_tracking_9|knows_inventory_management_5|knows_horse_archery_5
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2	#reset to native

king_attrib = str_20|agi_19|int_18|cha_20|level(40) #cambiado chief
king_skills = knows_weapon_master_10|knows_trainer_5|knows_riding_4|knows_ironflesh_10|knows_power_strike_10|knows_athletics_10|knows_shield_3|knows_tactics_10|knows_prisoner_management_9|knows_leadership_10|knows_wound_treatment_9|knows_first_aid_8|knows_surgery_8|knows_power_throw_5|knows_power_draw_6|knows_spotting_6|knows_pathfinding_5|knows_inventory_management_4|knows_persuasion_6|knows_engineer_6|knows_horse_archery_5#|knows_sea_king_4|knows_navigation_10|knows_maintenance_8 #
lord_attrib = str_18|agi_17|int_16|cha_18|level(38) #cambiado chief
lord_skills = knows_weapon_master_8|knows_trainer_4|knows_riding_4|knows_ironflesh_8|knows_power_strike_8|knows_athletics_8|knows_shield_3|knows_tactics_8|knows_prisoner_management_9|knows_leadership_8|knows_wound_treatment_7|knows_first_aid_6|knows_surgery_6|knows_power_throw_4|knows_power_draw_4|knows_spotting_4|knows_pathfinding_4|knows_inventory_management_3|knows_persuasion_4|knows_engineer_4|knows_horse_archery_5#|knows_sea_king_4|knows_maintenance_6
####################################################################################################################
reserved = 0
no_scene = 0
####################################################################################################################
tf_has_body = tf_guarantee_armor
tf_has_hand  = tf_guarantee_gloves
tf_has_head  = tf_guarantee_helmet
tf_has_shield  = tf_guarantee_shield
tf_has_ranged  = tf_guarantee_ranged
tf_has_horse  = tf_guarantee_horse
tf_all = tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all = tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_w_horse = tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield
####################################################################################################################
todo = []

#non-faction random guns

#revolvers
revolvers = [
  itm_pistol_revolver_1,
  itm_pistol_revolver_2,
  
  itm_common_revolver_1,
  itm_common_revolver_2,
  itm_common_revolver_3,
  itm_common_revolver_4,
  itm_common_revolver_5,
  itm_common_revolver_6,
  itm_common_revolver_7,
  itm_common_revolver_8,
  itm_common_revolver_9,
  itm_common_revolver_10,
  ]

#snub_revolvers
snub_revolvers = [
  itm_pistol_snubnosed_revolver,
  itm_crook_revolver_1,
  ]

#semi-auto_pistols
semi_pistols = [
  itm_pistol_walther_ppk,
  itm_pistol_1911,
  itm_pistol_1911_2,
  itm_pistol_browning_hp_maesen,
  itm_common_pistol_1,
  itm_common_pistol_2,
  itm_common_pistol_3,
  itm_common_pistol_4,
  itm_common_pistol_5,
  itm_common_pistol_6,
  itm_common_pistol_7,
  itm_common_pistol_8,
  ]

#assassin_pistols
silent_pistols = [
  itm_pistol_walther_ppk_sil,
  ]

#bad_smgs
smg_1 = [
  itm_irregular_smg,
  ]

#average_smgs
smg_2 = [
  itm_smg_mp40,
  ]

#drum_mags
smg_3 = [
  itm_smg_m31,
  itm_irregular_smg_2,
  ]

#rifles
rifles = [
  itm_rifle_arisaka,
  itm_rifle_arisaka_b,
  itm_common_bolt_action_rifle,
  itm_common_bolt_action_rifle_bayonet,
  itm_common_bolt_action_rifle_1,
  itm_common_bolt_action_rifle_bayonet_1,
  itm_common_bolt_action_rifle_2,
  itm_common_bolt_action_rifle_bayonet_2,
  itm_common_bolt_action_rifle_3,
  itm_common_bolt_action_rifle_bayonet_3,
  itm_common_bolt_action_rifle_single,
  ]

#carbine
carbines = [
  itm_common_bolt_action_carbine_1,
  itm_common_bolt_action_carbine_2,
  itm_common_bolt_action_carbine_3,
  itm_common_bolt_action_carbine_single,
  ]

#sniper
sniper_1 = [
	itm_empire_sniper,
    itm_berchav_sniper,
  ]

#short_2-shot_shotgun
shotgun_1 = [ 
  itm_double_barrel_shotgun_short,
  itm_shotgun_sawnoff,
  ]
  
#2-shot_shotgun
shotgun_2 = [
  itm_hunting_shotgun,
  itm_double_barrel_shotgun,
  ]

#trench_gun
trench_gun = [
  itm_shotgun_old,
  itm_shotgun_short_old,
  ] 

#lmg
lmg_1 = [
	itm_lmg_type_99,
  ]

################
##Barbed Wire###
################
##Entenaii Empire
entenaii_lord_gear = [
  (itm_smg_sten, imod_masterwork),
  (itm_pistol_ammo_pw, imod_large_bag),
  (itm_pistol_ammo_pw, imod_large_bag),
  (itm_trooper_sword, imod_balanced),
  (itm_entenaii_armour_officer, imod_reinforced),
  (itm_entenaii_uniform_noble, imod_reinforced),
  (itm_entenaii_helmet_lord, imod_lordly),
  (itm_entenaii_helmet_lord_full, imod_lordly),
  (itm_ammo_belt_1, imod_reinforced),
  (itm_entenaii_gauntlets, imod_reinforced),
  ]
##Entenaii Dominion
dominion_lord_gear = [
  (itm_dominion_shotgun, imod_masterwork),
  (itm_flameshot_ammo_pw, imod_large_bag),
  (itm_flameshot_ammo_pw, imod_large_bag),
  (itm_trooper_sword, imod_balanced),
  (itm_dominion_armour_officer, imod_reinforced),
  (itm_dominion_uniform_officer, imod_reinforced),
  (itm_dominion_hall_guard_helmet, imod_lordly),
  (itm_ammo_belt_1, imod_reinforced),
  (itm_dominion_gauntlets, imod_reinforced),
  itm_cloak_fanatic,
  ]
##Kingdom of Galvae
galvae_lord_gear = [
  (itm_galvae_lmg, imod_masterwork),
  (itm_mg_ammo_pw, imod_large_bag),
  (itm_galvae_shield_10, imod_reinforced),
  (itm_ornate_seax, imod_balanced),
  (itm_galvae_armour_officer, imod_reinforced),
  (itm_galvae_uniform_officer, imod_reinforced),
  (itm_galvae_mask_helmet, imod_lordly),
  (itm_cloak_1, imod_reinforced),
  (itm_galvae_gauntlets, imod_reinforced),
  ]
##Molvat-Berchav Union
union_lord_gear = [
  (itm_molvat_assault_rifle, imod_masterwork),
  (itm_rifle_ammo_pw, imod_large_bag),
  (itm_rifle_ammo_pw, imod_large_bag),
  (itm_shashka, imod_balanced),
  (itm_union_armour_officer, imod_reinforced),
  (itm_union_uniform_officer, imod_reinforced),
  (itm_union_helmet_officer, imod_lordly),
  (itm_ammo_belt_1, imod_reinforced),
  (itm_union_gauntlets, imod_reinforced),
  ]
##Vitzland Territories
vitzland_lord_gear = [
  (itm_vitzland_smg, imod_masterwork),
  (itm_pistol_ammo_pw, imod_large_bag),
  (itm_pistol_ammo_pw, imod_large_bag),
  (itm_blucher, imod_balanced),
  
  (itm_vitzland_armour_officer, imod_reinforced),
  (itm_vitzland_uniform_officer, imod_reinforced),
  (itm_vitzland_salet_ubersto, imod_lordly),
  (itm_vitzland_salet_ubersto_2, imod_lordly),
  
  (itm_ammo_belt_1, imod_reinforced),
  (itm_vitzland_gauntlets, imod_reinforced),
  ]
##Trezzo Republic
republican_lord_gear = [
  (itm_trezzo_smg, imod_masterwork),
  (itm_pistol_ammo_pw, imod_large_bag),
  (itm_pistol_ammo_pw, imod_large_bag),
  (itm_noble_rapier_3, imod_balanced),
  
  (itm_republican_armour_officer, imod_reinforced),
  (itm_republican_uniform_officer, imod_reinforced),
  itm_republican_noble_helmet,
  
  (itm_ammo_belt_1, imod_reinforced),
  (itm_republican_gauntlets, imod_reinforced),
  ]
##Itami Castedom
itami_lord_gear = [
  (itm_itami_pistol, imod_masterwork),
  (itm_pistol_ammo_pw, imod_large_bag),
  (itm_pistol_ammo_pw, imod_large_bag),
  (itm_katana, imod_balanced),
  
  (itm_itami_armour_officer, imod_reinforced),
  (itm_itami_uniform_officer, imod_reinforced),
  itm_itami_noble_helmet,
  
  (itm_ammo_belt_1, imod_reinforced),
  (itm_itami_gauntlets, imod_reinforced),
  ]


##Irregular

##Throd
throd_lord_gear = [
  itm_grenade_miasma,
  itm_grenade_miasma,
  itm_grenade_miasma,
  itm_war_axe,
  
  itm_throd_helmet,
  itm_throd_gauntlets,
  itm_throd_robe_armoured_heavy_2,
  itm_ghoul_horse,
  itm_ghoul_horse_2,
  itm_throd_shield,
  ]
##Other
companion_gear = [
  itm_irregular_bolt_action_carbine,
  itm_rifle_ammo,
  itm_knife,
  itm_irregular_uniform_regular,
  itm_civil_hat_1,
  ]

rusty_guns_1 = [
  
  (itm_pistol_revolver_1, imod_cracked),
  (itm_pistol_revolver_2, imod_cracked),
  (itm_pistol_c96, imod_cracked),
  (itm_pistol_snubnosed_revolver, imod_cracked),
  (itm_pistol_sw_629_2, imod_cracked),
  
  (itm_smg_sten, imod_cracked),
  (itm_smg_mp40, imod_cracked),
  (itm_smg_m31, imod_cracked),
  
  (itm_rifle_pa_musket, imod_cracked),
  (itm_rifle_pa_bolt_action, imod_cracked),
  (itm_rifle_svt40, imod_cracked),
  (itm_rifle_lever_action, imod_cracked),
  (itm_rifle_winchester, imod_cracked),
  
  (itm_shotgun_old, imod_cracked),
  (itm_shotgun_sawnoff, imod_cracked),
  (itm_shotgun_short_old, imod_cracked),
  ]  

swift_horses = [
  itm_swift_horse_1,
  itm_swift_horse_2,
  itm_swift_horse_3,
  itm_swift_horse_4,
  itm_swift_horse_5,
  itm_swift_horse_6,
  ]
####################################################################################################################
troops = [
["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,[],str_3|agi_3|int_3|cha_3,wp(10),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,[],0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_woman|tf_guarantee_all, 0, 0,fac_commoners,[],0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
####################################################################################################################
["arena_training_fighter_1","Novice Gladiator","Novice Gladiators",tf_has_body,no_scene,reserved,fac_commoners,
  [],attr_lvl_5,wp_common,knows_common,mercenary_face_1, mercenary_face_2],
["arena_training_fighter_2","Novice Gladiator","Novice Gladiators",tf_has_body,no_scene,reserved,fac_commoners,
  [],attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],
["arena_training_fighter_3","Regular Gladiator","Regular Gladiators",tf_has_body,no_scene,reserved,fac_commoners,
  [],attr_lvl_15,wp_2_m,knows_battle_2,mercenary_face_1, mercenary_face_2],
["arena_training_fighter_4","Regular Gladiator","Regular Gladiators",tf_has_body,no_scene,reserved,fac_commoners,
  [],attr_lvl_20,wp_3_m,knows_battle_3,mercenary_face_1, mercenary_face_2],
["arena_training_fighter_5","Regular Gladiator","Regular Gladiators",tf_has_body,no_scene,reserved,fac_commoners,
  [],attr_lvl_20,wp_3_m,knows_battle_3,mercenary_face_1, mercenary_face_2],
["arena_training_fighter_6","Veteran Gladiator","Veteran Gladiators",tf_has_body,no_scene,reserved,fac_commoners,
  [],attr_lvl_25,wp_4_m,knows_battle_4,mercenary_face_1, mercenary_face_2],
["arena_training_fighter_7","Veteran Gladiator","Veteran Gladiators",tf_has_body,no_scene,reserved,fac_commoners,
  [],attr_lvl_25,wp_4_m,knows_battle_4,mercenary_face_1, mercenary_face_2],
["arena_training_fighter_8","Veteran Gladiator","Veteran Gladiators",tf_has_body,no_scene,reserved,fac_commoners,
  [],attr_lvl_25,wp_4_m,knows_battle_4,mercenary_face_1, mercenary_face_2],
["arena_training_fighter_9","Champion Gladiator","Champion Gladiators",tf_has_body,no_scene,reserved,fac_commoners,
  [],attr_lvl_30,wp_5_m,knows_battle_5,mercenary_face_1, mercenary_face_2],
["arena_training_fighter_10","Champion Gladiator","Champion Gladiators",tf_has_body,no_scene,reserved,fac_commoners,
  [],attr_lvl_35,wp_6_m,knows_battle_6,mercenary_face_1, mercenary_face_2],
####################################################################################################################
["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,x_face, x_face],
####################################################################################################################
#soldiers:
#This troop is the troop marked as soldiers_begin
#civilians
["farmer","Peasant","Peasants",tf_has_body,no_scene,reserved,fac_commoners,
  [
  itm_arrows,
  itm_buckshot_ammo,

  itm_double_barrel_shotgun,
  itm_stones,
  itm_throwing_knives,
  itm_hunting_bow,
  itm_short_bow,

  itm_wooden_stick,
  itm_club,
  itm_shepherds_crook,
  itm_2by4,
  itm_pitch_fork,
  itm_pitch_fork_1,
  itm_pitch_fork_2,
  itm_wrench,
  itm_shovel_short,
  itm_shovel,
  itm_hand_saw,
  itm_hammer,
  itm_hatchet,
  itm_lumberjack_axe,
  itm_pickaxe,
  itm_staff,
  itm_simple_knife,
  itm_knife,
  itm_kukri_old,

  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  
  itm_straw_hat_1,
  itm_straw_hat_2,
  itm_peasant_cap_blue,
  itm_peasant_cap_red,
  itm_peasant_cap_green,
  itm_peasant_cap_black,
  itm_peasant_cap_white,
  itm_civ_hat_blue_1,
  itm_civ_hat_blue_2,
  itm_civ_hat_blue_3,
  itm_civ_hat_black_1,
  itm_civ_hat_black_2,
  itm_civ_hat_black_3,
  itm_civ_hat_brown_1,
  itm_civ_hat_brown_2,
  itm_civ_hat_green_1,
  itm_civ_hat_green_2,
  itm_civ_hat_green_3,
  itm_civ_hat_vblue_1,
  itm_civ_hat_vblue_2,
  itm_civ_hat_vblue_3,
  itm_civ_hat_blue_1f,
  itm_winter_hat_1, itm_winter_hat_2, itm_winter_hat_b,
  ],
  attr_lvl_5,wp_common,knows_common,man_face_middle_1, man_face_old_2],
["peasant_woman","Peasant","Peasants",tf_woman|tf_has_body,0,0,fac_commoners,[
  itm_arrows,
  itm_buckshot_ammo,

  itm_double_barrel_shotgun,
  itm_stones,
  itm_throwing_knives,
  itm_hunting_bow,
  itm_short_bow,

  itm_wooden_stick,
  itm_club,
  itm_hammer,
  itm_hatchet,
  itm_shepherds_crook,
  itm_simple_knife,
  itm_pitch_fork,
  itm_pitch_fork_1,
  itm_pitch_fork_2,
  itm_knife,

  itm_civilian_outfit_1w,
  itm_civilian_outfit_2w,
  itm_civilian_outfit_3w,
  itm_civilian_outfit_4w,
  itm_civilian_outfit_5w,
  itm_civilian_outfit_6w,
  itm_civilian_outfit_7w,
  itm_civilian_outfit_8w,
  itm_civilian_outfit_9w,
  itm_civilian_outfit_10w,
  itm_civilian_outfit_11w,

  itm_straw_hat_1,
  itm_straw_hat_2,
  itm_peasant_cap_blue,
  itm_peasant_cap_red,
  itm_peasant_cap_green,
  itm_peasant_cap_black,
  itm_peasant_cap_white,
  itm_civ_hat_blue_1,
  itm_civ_hat_blue_2,
  itm_civ_hat_blue_3,
  itm_civ_hat_black_1,
  itm_civ_hat_black_2,
  itm_civ_hat_black_3,
  itm_civ_hat_brown_1,
  itm_civ_hat_brown_2,
  itm_civ_hat_green_1,
  itm_civ_hat_green_2,
  itm_civ_hat_green_3,
  itm_civ_hat_vblue_1,
  itm_civ_hat_vblue_2,
  itm_civ_hat_vblue_3,
  itm_civ_hat_blue_1f,
  itm_winter_hat_1, itm_winter_hat_2, itm_winter_hat_b,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,woman_face_1,woman_face_2],
["traveler","Traveler","Travellers",tf_has_body,no_scene,reserved,fac_commoners,[
  itm_arrows,
  itm_pistol_ammo,

  itm_hunting_bow,
  itm_stones,
  itm_throwing_knives,
  itm_crook_revolver_1,

  itm_wooden_stick,
  itm_club,
  itm_simple_knife,
  itm_knife,

  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  
  itm_straw_hat_1,
  itm_straw_hat_2,
  itm_peasant_cap_blue,
  itm_peasant_cap_red,
  itm_peasant_cap_green,
  itm_peasant_cap_black,
  itm_peasant_cap_white,
  itm_civ_hat_blue_1,
  itm_civ_hat_blue_2,
  itm_civ_hat_blue_3,
  itm_civ_hat_black_1,
  itm_civ_hat_black_2,
  itm_civ_hat_black_3,
  itm_civ_hat_brown_1,
  itm_civ_hat_brown_2,
  itm_civ_hat_green_1,
  itm_civ_hat_green_2,
  itm_civ_hat_green_3,
  itm_civ_hat_vblue_1,
  itm_civ_hat_vblue_2,
  itm_civ_hat_vblue_3,
  itm_civ_hat_blue_1f,
  itm_winter_hat_1, itm_winter_hat_2, itm_winter_hat_b,
  
  ]+revolvers,
  attr_lvl_5,wp_common,knows_common,man_face_middle_1, man_face_old_2],
["traveler_w","Traveler","Travellers",tf_woman|tf_has_body,0,0,fac_commoners,[
  itm_arrows,
  itm_pistol_ammo,

  itm_hunting_bow,
  itm_stones,
  itm_throwing_knives,
  itm_crook_revolver_1,

  itm_wooden_stick,
  itm_club,
  itm_simple_knife,
  itm_knife,

  itm_civilian_outfit_1w,
  itm_civilian_outfit_2w,
  itm_civilian_outfit_3w,
  itm_civilian_outfit_4w,
  itm_civilian_outfit_5w,
  itm_civilian_outfit_6w,
  itm_civilian_outfit_7w,
  itm_civilian_outfit_8w,
  itm_civilian_outfit_9w,
  itm_civilian_outfit_10w,
  itm_civilian_outfit_11w,

  itm_straw_hat_1,
  itm_straw_hat_2,
  itm_peasant_cap_blue,
  itm_peasant_cap_red,
  itm_peasant_cap_green,
  itm_peasant_cap_black,
  itm_peasant_cap_white,
  itm_civ_hat_blue_1,
  itm_civ_hat_blue_2,
  itm_civ_hat_blue_3,
  itm_civ_hat_black_1,
  itm_civ_hat_black_2,
  itm_civ_hat_black_3,
  itm_civ_hat_brown_1,
  itm_civ_hat_brown_2,
  itm_civ_hat_green_1,
  itm_civ_hat_green_2,
  itm_civ_hat_green_3,
  itm_civ_hat_vblue_1,
  itm_civ_hat_vblue_2,
  itm_civ_hat_vblue_3,
  itm_civ_hat_blue_1f,
  itm_winter_hat_1, itm_winter_hat_2, itm_winter_hat_b,
  
  ]+revolvers,
  attr_lvl_10,wp_1_m,knows_battle_1,woman_face_1,woman_face_2],

##Hireable##
#common
["watchman","Watchman","Watchmen",tf_has_body|tf_has_head|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_pistol_ammo,

  itm_darts,
  itm_crook_revolver_1,

  itm_mace_1,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_staff,
  itm_trench_club_2,
  itm_bowie_knife,
  itm_knife,
  itm_kukri_rusty,
  itm_kukri_old,
  itm_metal_blade,

  itm_leather_gloves,
  itm_black_gloves,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,

  itm_straw_hat_1,
  itm_straw_hat_2,
  itm_peasant_cap_blue,
  itm_peasant_cap_red,
  itm_peasant_cap_green,
  itm_peasant_cap_black,
  itm_peasant_cap_white,
  itm_civ_hat_blue_1,
  itm_civ_hat_blue_2,
  itm_civ_hat_blue_3,
  itm_civ_hat_black_1,
  itm_civ_hat_black_2,
  itm_civ_hat_black_3,
  itm_civ_hat_brown_1,
  itm_civ_hat_brown_2,
  itm_civ_hat_green_1,
  itm_civ_hat_green_2,
  itm_civ_hat_green_3,
  itm_civ_hat_vblue_1,
  itm_civ_hat_vblue_2,
  itm_civ_hat_vblue_3,
  itm_civ_hat_blue_1f,
  itm_winter_hat_1, itm_winter_hat_2, itm_winter_hat_b,

  ]+revolvers,
  attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],
["caravan_guard","Patrolman","Patrolmen",tf_has_body|tf_has_ranged,no_scene,0,fac_commoners,[
  itm_rifle_ammo,

  itm_knife,
  itm_trench_club_2,
  itm_kukri_rusty,
  itm_mace_1,
  itm_staff,
  itm_bowie_knife,
  itm_big_club,
  itm_hatchet,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,

  itm_leather_gloves,
  itm_black_gloves,
  ]+rifles,
  attr_lvl_15,wp_2_m,knows_battle_2,mercenary_face_1, mercenary_face_2],
["mercenary_swordsman","Sentry","Sentries",tf_has_body|tf_has_head|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_pistol_ammo,

  itm_knife,
  itm_trench_club_2,
  itm_kukri_rusty,
  itm_metal_blade,
  itm_hand_axe,
  itm_staff,

  itm_wood_shield,
  itm_round_shield_leather,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,

  itm_gas_mask,
  itm_gas_mask_ww,
  itm_gas_mask_ww_e,
  itm_gas_mask_ca_90,
  
  itm_pot_helmet,
  itm_pot_helmet_face_cover,
  itm_simple_helmet,
  itm_simple_helmet_face_cover,

  itm_leather_gloves,
  itm_black_gloves,
  ]+smg_1,
  attr_lvl_20,wp_3_m,knows_battle_3,mercenary_face_1, mercenary_face_2],
["hired_blade","Warden","Wardens",tf_has_body|tf_has_hand|tf_has_head|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_rifle_ammo,

  itm_knife,
  itm_trench_club_2,
  itm_bayonet_2,
  itm_bayonet_1,
  itm_hatchet_tactical,

  itm_irregular_uniform_regular,
  itm_irregular_uniform_sergeant_1,

  itm_pot_helmet,
  itm_pot_helmet_face_cover,

  itm_simple_helmet,
  itm_simple_helmet_face_cover,
  itm_steel_helmet_1,
  itm_steel_helmet_1b,
  itm_steel_helmet_1_face_cover,
  itm_steel_helmet_1b_face_cover, 
  itm_steel_helmet_2, 
  itm_steel_helmet_3,
  itm_steel_helmet_1_gas,
  itm_steel_helmet_1b_gas,
  itm_brodie,
  itm_brodie_face_cover,
  itm_gas_mask,
  
  itm_gas_mask_ww,
  itm_gas_mask_ww_e,
  itm_gas_mask_ca_90,
  
  

  itm_leather_gloves,
  itm_black_gloves,
  ]+smg_2,
  attr_lvl_25,wp_4_m,knows_battle_4,mercenary_face_1, mercenary_face_2],
["sentinel","Sentinel","Sentinels",tf_has_body|tf_has_hand|tf_has_head|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_rifle_ammo,

  itm_knife,
  itm_trench_club_2,
  itm_bayonet_2,
  itm_bayonet_1,
  itm_big_spiked_club,
  itm_hatchet_tactical,

  itm_irregular_armour,

  itm_steel_helmet_1,
  itm_steel_helmet_1b,
  itm_steel_helmet_1_face_cover,
  itm_steel_helmet_1b_face_cover, 
  itm_steel_helmet_2, 
  itm_steel_helmet_3,
  itm_steel_helmet_1_gas,
  itm_steel_helmet_1b_gas,
  itm_brodie,
  itm_brodie_face_cover,
  itm_brodie_gasmask,
  itm_bandit_fullhelm,
  itm_bandit_fullhelm2,
  itm_bandit_bulwark_helm,

  itm_leather_gloves_metal,
  itm_black_gloves_metal,
  itm_scale_gauntlets,
  ]+rifles,
  attr_lvl_30,wp_5_m,knows_battle_5,mercenary_face_1, mercenary_face_2],

#rangers
["scout","Scout","Scouts",tf_has_body|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_arrows,
  itm_pistol_ammo,
  
  itm_crook_revolver_1,

  itm_club,
  itm_big_club,
  itm_crowbar,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_hatchet,
  itm_simple_knife,
  itm_knife,
  itm_kukri_rusty,
  itm_kukri_old,
  itm_metal_blade,
  itm_shovel_short,

  itm_throwing_knives,
  itm_darts,
  itm_short_bow,

  itm_leather_gloves,
  itm_black_gloves,

  itm_poor_shirt_2,

  itm_winter_hat_1, itm_winter_hat_2, itm_winter_hat_b,
#  
  itm_wooly_grey,
  itm_wooly_red,
  itm_wooly_green,
  itm_wooly_black,
  itm_wooly_tan,
 # itm_wooly_blue,
  itm_goggles_1,
  itm_goggles_1_face_cover,
  itm_bandana_camo,
  itm_bandana_black,
  itm_bandana_blue,
 # itm_bandana_red,
  itm_bandana_green,
  itm_bandana_white,
  ]+revolvers,
  attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],
["lookout","Lookout","Lookouts",tf_has_body|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_pistol_ammo,

  itm_darts,

  itm_mace_1,
  itm_big_club,
  itm_crowbar,
  itm_lead_pipe,
  itm_hand_axe,
  itm_bowie_knife,
  itm_knife,
  itm_trench_club_2,
  itm_metal_blade,
  itm_shovel,
  itm_hammer_big,

  itm_poor_shirt_3,

  itm_gas_mask,
  
  itm_gas_mask_ww,
  itm_gas_mask_ca_90,
  
  
  itm_goggles_1,
  itm_goggles_1_face_cover,

  itm_winter_hat_1, itm_winter_hat_2, itm_winter_hat_b,
  
  itm_leather_gloves,
  itm_black_gloves,
  ]+semi_pistols,
  attr_lvl_15,wp_2_m,knows_battle_2,mercenary_face_1, mercenary_face_2],
["spotter","Spotter","Spotters",tf_has_body|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_rifle_ammo,

  itm_knife,
  itm_bayonet_2,
  itm_bayonet_1,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_2,
  itm_bastard_club_1,
  itm_crowbar,
  itm_hatchet_tactical,
  itm_hand_axe,
  itm_bowie_knife,
  itm_hammer_big,

  itm_poor_shirt_4,

  itm_pot_helmet,
  itm_pot_helmet_face_cover,

  itm_simple_helmet,
  itm_simple_helmet_face_cover,
  itm_steel_helmet_1,
  itm_steel_helmet_1b,
  itm_steel_helmet_1_face_cover,
  itm_steel_helmet_1b_face_cover, 
  itm_steel_helmet_2, 
  itm_steel_helmet_3,
  itm_steel_helmet_1_gas,
  itm_steel_helmet_1b_gas,
  itm_vintage_helm,
  itm_vintage_helm_scarf,

  itm_leather_gloves,
  itm_black_gloves,
  ]+carbines,
  attr_lvl_25,wp_4_m,knows_battle_4,mercenary_face_1, mercenary_face_2],
["ranger","Ranger","Rangers",tf_has_body|tf_has_ranged|tf_has_hand,no_scene,reserved,fac_commoners,[
  itm_rifle_ammo,

  itm_knife,
  itm_bayonet_2,
  itm_katana,
  itm_bayonet_1,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_2,
  
  itm_bastard_club_1,
  itm_hatchet_tactical,
  itm_big_spiked_club,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,

  itm_helmet_gas,
  itm_helmet_gas_olive,

  itm_camouflage_helmet,
  
  itm_vintage_helm_scarf,

  itm_leather_gloves,
  itm_black_gloves,
  ]+rifles,
  attr_lvl_30,wp_5_m,knows_battle_5,mercenary_face_1, mercenary_face_2],

#gunmen
["mercenary_gunslinger","Hired_Gunslinger","Hired_Gunslingers",tf_has_body|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_pistol_ammo_4,

  itm_kukri_rusty,
  itm_bowie_knife,

  itm_mercenary_coat_1,
  itm_irregular_uniform_raider_1,
  
  itm_leather_gloves,
  itm_black_gloves,
  ]+semi_pistols,
  attr_lvl_20,wp_3_r,knows_battle_3,mercenary_face_1, mercenary_face_2],
["mercenary_rifleman","Hired_Rifleman","Hired_Riflemans",tf_has_body|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_rifle_ammo,

  itm_kukri_rusty,
  itm_bowie_knife,

  itm_mercenary_coat_1,

  itm_leather_gloves,
  itm_black_gloves,
  ]+carbines,
  attr_lvl_20,wp_3_r,knows_battle_3,mercenary_face_1, mercenary_face_2],
["mercenary_shotgunner","Hired_Trench_Raider","Hired_Trench_Raiders",tf_has_body|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_slug_ammo,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,

  itm_mercenary_cuirass,
  
  itm_bandit_fullhelm,
  itm_bandit_fullhelm2,
  itm_bucket_helm,
  itm_bandit_bulwark_helm,

  itm_leather_gloves_metal,
  itm_black_gloves_metal,
  itm_scale_gauntlets,
  ]+shotgun_2,
  attr_lvl_20,wp_3_r,knows_battle_3,mercenary_face_1, mercenary_face_2],
["mercenary_sniper","Hired_Sniper","Hired_Snipers",tf_has_body|tf_has_hand|tf_has_head|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_large_caliber_ammo,

  itm_bowie_knife,
  itm_bayonet_2,

  itm_mercenary_coat_1,
  itm_irregular_uniform_guard_1,

  itm_hooded_cloak_1,
  itm_hooded_cloak_2,
  itm_hooded_cloak_3,
  itm_hooded_cloak_4,
  itm_hooded_cloak_5,
  itm_camouflage_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  ]+sniper_1,
  attr_lvl_25,wp_4_r,knows_battle_4,mercenary_face_1, mercenary_face_2],
["mercenary_grenadier","Hired_Grenadier","Hired_Grenadiers",tf_has_body|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_grenade,
  itm_grenade_frag,
  itm_grenade_stick,
  itm_grenade_molotov,
  
  itm_pistol_ammo,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  
  itm_mercenary_coat_1,
  itm_irregular_uniform_regular,

  itm_pot_helmet,
  itm_pot_helmet_face_cover,

  itm_simple_helmet,
  itm_simple_helmet_face_cover,
  itm_steel_helmet_1,
  itm_steel_helmet_1b,
  itm_steel_helmet_1_face_cover,
  itm_steel_helmet_1b_face_cover, 
  itm_steel_helmet_2, 
  itm_steel_helmet_3,
  itm_steel_helmet_1_gas,
  itm_steel_helmet_1b_gas,
  
  itm_bucket_helm,

  itm_leather_gloves_metal,
  itm_black_gloves_metal,
  itm_scale_gauntlets,
  ]+revolvers,
  attr_lvl_25,wp_4_r,knows_battle_4,mercenary_face_1, mercenary_face_2],

["mercenary_brawler","Hired_Brawler","Hired_Brawlers",tf_has_body|tf_has_head|tf_has_hand,no_scene,reserved,fac_commoners,[
  itm_brassknuckles,

  itm_mercenary_coat_1,

  itm_bandana_camo,
  itm_bandana_black,
  itm_bandana_blue,
  itm_bandana_red,
  itm_bandana_green,
  itm_bandana_white,
  ],
  attr_lvl_25,wp_4_m,knows_battle_4,mercenary_face_1, mercenary_face_2],
["mercenary_powerfist","Hired_Pugilist","Hired_Pugilists",tf_has_body|tf_has_head|tf_has_hand,no_scene,reserved,fac_commoners,[
  itm_brassknuckles,

  itm_mercenary_cuirass,

  itm_pot_helmet,
  itm_pot_helmet_face_cover,
  
  itm_bucket_helm,

  itm_simple_helmet,
  itm_simple_helmet_face_cover,
  itm_steel_helmet_1,
  itm_steel_helmet_1b,
  itm_steel_helmet_1_face_cover,
  itm_steel_helmet_1b_face_cover, 
  itm_steel_helmet_2, 
  itm_steel_helmet_3,
  itm_brodie,
  itm_brodie_face_cover,

  ],
  attr_lvl_30,wp_5_m,knows_battle_5,mercenary_face_1, mercenary_face_2],
["mercenary_horseman","Hired_Rider","Hired_Riders",tf_mounted|tf_has_body|tf_has_head|tf_guarantee_horse,no_scene,reserved,fac_commoners,[
  itm_pistol_ammo,

  itm_throwing_spears,
  itm_throwing_metal_spears,

  itm_light_cav_sword,
  itm_iron_staff,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,

  itm_wood_shield,
  itm_round_shield_leather,

  itm_mercenary_coat_1,

  itm_bandana_camo,
  itm_bandana_black,
  itm_bandana_blue,
  itm_bandana_red,
  itm_bandana_green,
  itm_bandana_white,
  itm_winter_hat_1, itm_winter_hat_2, itm_winter_hat_b,
  
  itm_leather_gloves,
  itm_black_gloves,

  itm_steppe_horse,
  itm_courser,
  itm_hunter,
  
  ]+revolvers,
  attr_lvl_20,wp_3_m,knows_battle_3,mercenary_face_1, mercenary_face_2],
["mercenary_cavalry","Hired_Veteran Rider","Hired_Veteran Riders",tf_mounted|tf_has_body|tf_has_head|tf_guarantee_horse|tf_has_shield|tf_has_hand,no_scene,reserved,fac_commoners,[
  itm_rifle_ammo,

  itm_throwing_spears,
  itm_throwing_metal_spears,

  itm_knife,
  itm_lead_pipe,
  itm_iron_staff,
  itm_saber1,

  itm_round_shield_leather,
  itm_round_shield,

  itm_mercenary_cuirass,

  itm_pot_helmet,
  itm_pot_helmet_face_cover,
  itm_simple_helmet,
  itm_simple_helmet_face_cover,
  itm_steel_helmet_1,
  itm_steel_helmet_1b,
  itm_steel_helmet_1_face_cover,
  itm_steel_helmet_1b_face_cover, 
  itm_steel_helmet_2, 
  itm_steel_helmet_3,
  itm_vintage_helm,
  itm_vintage_helm_scarf,

  itm_leather_gloves_metal,
  itm_black_gloves_metal,
  itm_scale_gauntlets,

  itm_hunter,
  ]+carbines,
  attr_lvl_30,wp_5_m,knows_battle_5,mercenary_face_1, mercenary_face_2],
["mercenary_medic","Hired_Combat Medic","Hired_Combat Medics",tf_has_body|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_pistol_ammo,

  itm_knife,
  itm_knife,
  itm_knife,
  itm_bayonet_2,
  itm_bayonet_1,
  itm_bowie_knife,

  itm_mercenary_coat_1,

  itm_winter_hat_1, itm_winter_hat_2, itm_winter_hat_b,
  
  itm_leather_gloves,
  itm_black_gloves,
  ]+semi_pistols,
  attr_lvl_25,wp_4_r,knows_battle_4,mercenary_face_1, mercenary_face_2],

#Foreign#
#Yanizari
["mercenary_hunter","Hired_Yanizar","Hired_Yanizari",tf_has_body|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_yanizar_arrows,
  itm_yanizar_arrows,
  itm_recurve_bow,

  itm_kukri_old,

  itm_yanizar_uniform_1,
  
  itm_yanizar_helmet_1,

  itm_leather_gloves,
  itm_black_gloves,
  ],
  attr_lvl_20,wp_3_r,knows_battle_3,mercenary_face_1, mercenary_face_2],
["mercenary_archer","Hired_Yanizar Veteran","Hired_Yanizar Veterans",tf_has_body|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_yanizar_arrows,
  itm_yanizar_arrows,
  itm_rider_bow,
  itm_skirmisher_bow,

  itm_bayonet_2,

  itm_yanizar_uniform_1,
  
  itm_yanizar_helmet_2,

  itm_leather_gloves,
  itm_black_gloves,
  ],
  attr_lvl_25,wp_4_r,knows_battle_4,mercenary_face_1, mercenary_face_2],
["mercenary_horsearcher","Hired_Yanizar Rider","Hired_Yanizar Rider",tf_mounted|tf_has_body|tf_has_head|tf_guarantee_horse,no_scene,reserved,fac_commoners,[
  itm_yanizar_arrows,
  itm_yanizar_arrows,
  itm_recurve_bow,

  itm_kukri_old,

  itm_yanizar_uniform_1,
  
  itm_yanizar_helmet_1,

  itm_leather_gloves,
  itm_black_gloves,

  itm_foreign_horse_1,
  ],
  attr_lvl_20,wp_3_m,knows_battle_3,mercenary_face_1, mercenary_face_2],
["sentinel_horsearcher","Hired_Veteran Yanizar Rider","Hired_Veteran Yanizar Rider",tf_mounted|tf_has_body|tf_has_head|tf_guarantee_horse|tf_has_shield|tf_has_hand,no_scene,reserved,fac_commoners,[
  itm_yanizar_arrows,
  itm_yanizar_arrows,
  
  itm_rider_bow,
  itm_skirmisher_bow,

  itm_bayonet_2,

  itm_yanizar_uniform_1,
  
  itm_yanizar_helmet_2,

  itm_leather_gloves,
  itm_black_gloves,

  itm_foreign_horse_2,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,mercenary_face_1, mercenary_face_2],

#Candle Warriors
["follower_woman","Red_Candle","Red_Candles",tf_woman|tf_has_body|tf_guarantee_helmet,0,0,fac_commoners,[
  itm_arrows,
  itm_pistol_ammo,
  
  itm_short_bow,
  itm_crook_revolver_1,
  
  itm_kukri_rusty,
  itm_kukri_old,
  itm_mace_1,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_hatchet,
  itm_staff,
  itm_butchering_knife,
  
  itm_candle_outfit_red,
  
  itm_candle_bandana_red,
  
  itm_leather_gloves,
  itm_black_gloves,
  ]+revolvers,
  attr_lvl_15,wp_2_m,knows_battle_2,
  woman_face_1,woman_face_2],
["hunter_woman","Blue_Candle","Blue_Candles",tf_woman|tf_has_body|tf_guarantee_helmet|tf_has_ranged,0,0,fac_commoners,[
  itm_rifle_ammo,

  itm_knife,
  itm_kukri_rusty,
  itm_metal_blade,
  itm_mace_1,
  itm_lead_pipe,
  itm_hand_axe,
  itm_staff,
  itm_bowie_knife,

  itm_candle_outfit_blue,
  
  itm_candle_bandana_blue,
  
  itm_leather_gloves,
  itm_black_gloves,
  ]+rifles,
  attr_lvl_20,wp_3_r,knows_battle_3,
  woman_face_1,woman_face_2],
["fighter_woman","Black_Candle","Black_Candle",tf_woman|tf_has_body|tf_has_ranged|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_commoners,[
  itm_rifle_ammo,
  itm_common_bolt_action_rifle_bayonet_1,

  itm_knife,
  itm_knife,
  itm_knife,
 # itm_knife,
  itm_knife,
  itm_bayonet_2,
  itm_bayonet_1,
  itm_one_handed_war_axe_a,
  itm_big_spiked_club,
  itm_hammer_big,

  itm_candle_outfit_black,
  itm_candle_outfit_black_2,
  
  itm_candle_bandana_black,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ],
  attr_lvl_25,wp_4_r,knows_battle_4,woman_face_1,woman_face_2],
["sword_sister","Black_Candle_Rider","Black_Candle_Riders",tf_woman|tf_mounted|tf_has_body|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_has_ranged,0,0,fac_commoners,[
  itm_rifle_ammo_pw,

  itm_light_cav_sword,
  
  itm_big_spiked_club,
  itm_spiked_club,
  itm_hatchet_tactical,
  itm_one_handed_war_axe_a,
  itm_battle_axe,
  itm_hammer_big,

  itm_candle_armour_black,
  
  itm_candle_bandana_black,

  itm_leather_gloves_metal,
  itm_black_gloves_metal,
  itm_scale_gauntlets,
  
  itm_tundra_horse_1,
  
  ]+carbines,
  attr_lvl_30,wp_5_r,knows_battle_5,woman_face_1,woman_face_2],

###
["mercenaries_end","mercenaries_end","mercenaries_end",tf_hero,no_scene,reserved,fac_commoners,[itm_invisi_body,itm_invisi_boots,itm_invisi_gloves,itm_invisi_head,],def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
###
#shadow_operative
["shadow_operative_regular","Shadow_Operative","Shadow_Operatives",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_pistol_ammo,

  itm_hatchet,
  itm_hand_axe,
  itm_hatchet_tactical,
  itm_one_handed_war_axe_a,

  itm_shadow_operative_uniform_regular,

  itm_shadow_operative_regular_helmet,

  itm_black_gloves,
  ]+semi_pistols,
  attr_lvl_25,wp_4_r,knows_battle_4,bandit_face1, bandit_face2],
["shadow_operative_officer","Shadow_Operative_Officer","Shadow_Operative_Officers",tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,0,0,fac_outlaws,[
  itm_pistol_ammo_pw,

  itm_hatchet,
  itm_hand_axe,
  itm_hatchet_tactical,
  itm_one_handed_war_axe_a,

  itm_shadow_operative_uniform_officer,
  
  itm_commander_cap_1,

  itm_black_gloves,
  ]+smg_2,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["shadow_operative_gunner","Shadow_Operative_Gunner","Shadow_Operative_Gunners",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_mg_ammo,
  itm_shadow_lmg,

  itm_hatchet,
  itm_hand_axe,
  itm_hatchet_tactical,
  itm_one_handed_war_axe_a,

  itm_shadow_operative_uniform_gunner,

  itm_shadow_operative_gunner_helmet,

  itm_black_gloves,
  (itm_black_gloves_metal,imod_ragged),
  ],
  attr_lvl_30,wp_4_r,knows_battle_4,bandit_face1, bandit_face2],
["shadow_operative_elite","Shadow_Operative_Elite","Shadow_Operative_Elites",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_rifle_ammo_pw,

  itm_hatchet,
  itm_hand_axe,
  itm_hatchet_tactical,
  itm_one_handed_war_axe_a,

  itm_shadow_operative_uniform_elite,

  itm_shadow_operative_elite_cap,

  itm_black_gloves,
  ]+rifles,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["shadow_operative_saboteur","Shadow_Operative_Saboteur","Shadow_Operative_Saboteurs",tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet|tf_has_hand,0,0,fac_outlaws,[
  itm_rifle_ammo,

  itm_dynamite,
  itm_dynamite,

  itm_hatchet,
  itm_hand_axe,
  itm_hatchet_tactical,
  itm_one_handed_war_axe_a,

  itm_shadow_operative_uniform_saboteur,

  itm_shadow_operative_saboteur_helmet,

  (itm_black_gloves_metal,imod_ragged),
  ]+rifles,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["shadow_operative_knight","Shadow_Operative_Knight","Shadow_Operative_Knights",tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_outlaws,[
  itm_rifle_ammo_pw,

  itm_hatchet,
  itm_hand_axe,
  itm_hatchet_tactical,
  itm_one_handed_war_axe_a,

  itm_shadow_operative_armour,

  itm_shadow_operative_elite_cap,

  itm_leather_gloves_metal,
  itm_black_gloves_metal,
  itm_scale_gauntlets,
  ]+rifles,
  attr_lvl_40,wp_6_m,knows_battle_6,bandit_face1, bandit_face2],

#destroyed_shadow_operatives
["shadow_operative_remnant","Shadow_Operative_Remnant","Shadow_Operative_Remnants",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_rifle_ammo,

  itm_hatchet,
  itm_hand_axe,

  itm_shadow_operative_uniform_remnant,

  (itm_shadow_operative_elite_cap, imod_ragged),

  (itm_black_gloves, imod_ragged),
  ]+rifles,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
  
#vigilante
["manhunter","Vigilante","Vigilantes",tf_mounted|tf_has_body|tf_has_head|tf_has_ranged,0,0,fac_manhunters,[
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_bastard_club_1,

  itm_irregular_uniform_raider_1,
  
  itm_lobster,

  itm_leather_gloves,
  itm_black_gloves,
  ],
  attr_lvl_20,wp_3_m,knows_battle_3,mercenary_face_1, mercenary_face_2],
["manhunter_exp","Experienced Vigilante","Experienced Vigilantes",tf_mounted|tf_has_body|tf_guarantee_helmet|tf_has_hand|tf_guarantee_ranged,0,0,fac_manhunters,[
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_bastard_club_1,

  itm_bal_shield_2,

  itm_irregular_uniform_guard_1,
  
  itm_lobster,

  itm_leather_gloves,
  itm_black_gloves,
  ],
  attr_lvl_25,wp_4_m,knows_battle_4,mercenary_face_1, mercenary_face_2],
["manhunter_veteran","Veteran Vigilante","Veteran Vigilantes",tf_mounted|tf_has_body|tf_guarantee_helmet|tf_has_hand|tf_guarantee_ranged,0,0,fac_manhunters,[
  itm_blunt_slug_ammo_pw,
  itm_shotgun_riot,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_bastard_club_1,

  itm_irregular_armour,
  
  itm_lobster2,

  itm_leather_gloves_metal,
  itm_black_gloves_metal,
  itm_scale_gauntlets,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,mercenary_face_1, mercenary_face_2],

#military_police
["military_police_trooper","Military_Police_Trooper","Military_Police_Troopers",tf_has_body|tf_has_head|tf_has_ranged,0,0,fac_manhunters,[
  itm_pistol_ammo_pw,
  itm_empire_revolver,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_bastard_club_1,

  itm_irregular_uniform_raider_1,

  itm_brodie,

  itm_leather_gloves,
  itm_black_gloves,
  ],attr_lvl_20,wp_3_m,knows_battle_3,mercenary_face_1, mercenary_face_2],
["military_police_sergeant","Military_Police_Sergeant","Military_Police_Sergeants",tf_has_body|tf_guarantee_helmet|tf_has_hand|tf_guarantee_ranged,0,0,fac_manhunters,[
  itm_pistol_ammo_pw,
  itm_smg_sten,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_bastard_club_1,

  itm_bal_shield_2,

  itm_irregular_uniform_guard_1,

  itm_brodie,

  itm_leather_gloves,
  itm_black_gloves,
  ],attr_lvl_25,wp_4_m,knows_battle_4,mercenary_face_1, mercenary_face_2],
["military_police_officer","Military_Police_Officer","Military_Police_Officers",tf_has_body|tf_guarantee_helmet|tf_has_hand|tf_guarantee_ranged,0,0,fac_manhunters,[
  itm_rifle_ammo_pw,
  itm_empire_bolt_action_carbine,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_bastard_club_1,

  itm_irregular_armour,

  itm_brodie,

  itm_leather_gloves,
  itm_black_gloves,  
  ],attr_lvl_30,wp_5_m,knows_battle_5,mercenary_face_1, mercenary_face_2],

#press ganger
["slave_driver","Press Ganger","Press Ganger",tf_has_body|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_slavers,[
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_club,
  itm_staff,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,

  itm_sloppy_trench_coat,

  itm_goggles_1,
  itm_goggles_1_face_cover,

  itm_leather_gloves,
  itm_black_gloves,

  ],
  attr_lvl_20,wp_3_m,knows_battle_3,bandit_face1, bandit_face2],
["slave_hunter","Press Ganger Hunter","Press Ganger Hunters",tf_mounted|tf_has_body|tf_guarantee_helmet|tf_guarantee_horse|tf_has_hand|tf_guarantee_ranged,0,0,fac_slavers,[
  itm_blunt_slug_ammo,
  itm_shotgun_riot,
  
  itm_hammer_big,
  itm_lead_pipe,
  itm_iron_staff,

  itm_irregular_uniform_guard_1,

  itm_goggles_1,
  itm_goggles_1_face_cover,

  itm_leather_gloves,
  itm_black_gloves,

  itm_mountain_horse_1,
  itm_mountain_horse_2,
  itm_mountain_horse_3,
  itm_mountain_horse_4,
  itm_mountain_horse_5,
  itm_mountain_horse_6,
  itm_mountain_horse_7,
  itm_mountain_horse_8,
  itm_mountain_horse_9,
  itm_mountain_horse_10,

  ],
  attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["slaver_chief","Press Ganger Chief","Press Ganger Chiefs",tf_mounted|tf_has_body|tf_guarantee_helmet|tf_guarantee_horse|tf_has_hand|tf_guarantee_ranged,0,0,fac_slavers,[
  itm_blunt_slug_ammo_pw,
  itm_shotgun_riot,

  itm_sledgehammer,

  itm_irregular_uniform_guard_1,

  itm_goggles_1,
  itm_goggles_1_face_cover,
  itm_bandit_fullhelm,
  itm_bandit_fullhelm2,
  itm_bucket_helm,
  itm_bandit_bulwark_helm,

  itm_leather_gloves_metal,
  itm_black_gloves_metal,
  itm_scale_gauntlets,
  
  itm_mountain_horse_1,
  itm_mountain_horse_2,
  itm_mountain_horse_3,
  itm_mountain_horse_4,
  itm_mountain_horse_5,
  itm_mountain_horse_6,
  itm_mountain_horse_7,
  itm_mountain_horse_8,
  itm_mountain_horse_9,
  itm_mountain_horse_10,
  
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],

#bounty_hunter
["bounty_hunter","Bounty_Hunter","Bounty_Hunters",tf_mounted|tf_has_body|tf_guarantee_helmet|tf_has_hand,0,0,fac_slavers,[
  itm_pistol_ammo_4,

  itm_knife,
  itm_big_club,
  itm_big_spiked_club,

  itm_irregular_uniform_raider_1,
  
  itm_metal_combat_helmet,
  itm_metal_combat_helmet_black,

  itm_leather_gloves,
  itm_black_gloves,
  ]+semi_pistols,
  attr_lvl_30,wp_5_m,knows_battle_5,mercenary_face_1, mercenary_face_2],
["bounty_hunter_legend","Legendary_Bounty_Hunter","Legendary_Bounty_Hunters",tf_mounted|tf_has_body|tf_guarantee_helmet|tf_has_hand,0,0,fac_slavers,[
  itm_rifle_ammo_pw,
  
  itm_knife,
  itm_big_club,
  itm_big_spiked_club,

  itm_irregular_armour,
  
  itm_bandit_fullhelm,
  itm_bandit_fullhelm2,
  itm_bandit_bulwark_helm,

  itm_leather_gloves_metal,
  itm_black_gloves_metal,
  itm_scale_gauntlets,
  ]+carbines,
  attr_lvl_35,wp_6_m,knows_battle_6,mercenary_face_1, mercenary_face_2],

#other
["caravan_master","Trade merchant","Trade merchants",tf_mounted|tf_has_body|tf_guarantee_horse|tf_has_ranged,0,0,fac_commoners,[
  itm_rifle_ammo_pw,

  itm_staff,
  itm_knife,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,

  itm_irregular_uniform_guard_1,

  itm_civil_hat_1,
  itm_civil_hat_1b,
  itm_civil_hat_1c,
  itm_civil_hat_1d,
  itm_civil_hat_2,
  itm_civil_hat_3,
  itm_civil_hat_4,
  itm_civil_hat_5,
  itm_civil_hat_7,
  itm_civil_hat_9,
  itm_civil_hat_10,
  itm_civil_hat_11,
  itm_civil_hat_12,
  itm_civil_hat_13,
  itm_civil_hat_14,

  itm_winter_hat_1, itm_winter_hat_2, itm_winter_hat_b,
  
  itm_leather_gloves,
  itm_black_gloves,

  itm_plains_horse_1,
  itm_plains_horse_2,
  itm_plains_horse_3,
  itm_plains_horse_4,
  itm_plains_horse_5,
  
  ]+carbines,
  attr_lvl_30,wp_2_m,knows_battle_2|knows_inventory_management_10,
  mercenary_face_1, mercenary_face_2],
["courier","Courier","Courier",tf_mounted|tf_has_body|tf_guarantee_ranged,0,0,fac_neutral,[
  itm_pistol_ammo,

  itm_simple_knife,
  itm_knife,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,

  itm_winter_hat_1, itm_winter_hat_2, itm_winter_hat_b,
  
  itm_leather_gloves,
  itm_black_gloves,
  
  itm_swift_horse_1,
  itm_swift_horse_2,
  itm_swift_horse_3,
  itm_swift_horse_4,
  itm_swift_horse_5,
  itm_swift_horse_6,
  ]+revolvers,
  attr_lvl_25,wp_2_m,knows_battle_2|knows_inventory_management_10,mercenary_face_1, mercenary_face_2],

#bandits
["looter","Looter","Looters",tf_has_body,0,0,fac_outlaws,[
  itm_pistol_ammo,

  itm_throwing_knives,
  itm_darts,
  itm_crook_revolver_1,

  itm_wooden_stick,
  itm_club,
  itm_mace_1,
  itm_2by4nails,
  itm_crowbar,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_hatchet,
  itm_lumberjack_axe,
  itm_staff,
  itm_simple_knife,
  itm_knife,
  itm_butchering_knife,
  itm_kukri_old,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,
  
  itm_bandit_hood_blk,
  itm_bandit_hood_blu,
  itm_bandit_hood_grn,
  itm_bandit_hood_red,
  itm_bandit_hood_wht,

  itm_leather_gloves,
  ]+rusty_guns_1,attr_lvl_15,wp_2_m,knows_battle_2,bandit_face1, bandit_face2],
["bandit","Bandit","Bandits",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_pistol_ammo,

  itm_throwing_knives,
  itm_darts,
  itm_crook_revolver_1,

  itm_knife,
  itm_kukri_rusty,
  itm_metal_blade,
  itm_mace_1,
  itm_big_club,
  itm_spiked_club,
  itm_crowbar,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_lead_pipe,
  itm_hatchet,
  itm_hand_axe,
  itm_knife,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,
  
  itm_bandit_hood_blk,
  itm_bandit_hood_blu,
  itm_bandit_hood_grn,
  itm_bandit_hood_red,
  itm_bandit_hood_wht,
  itm_bandit_hood_blk_scarf,
  itm_bandit_hood_blu_scarf,
  itm_bandit_hood_grn_scarf,
  itm_bandit_hood_red_scarf,
  itm_bandit_hood_wht_scarf,
  
  itm_leather_gloves,
  itm_black_gloves,
  ]+smg_1,attr_lvl_20,wp_3_m,knows_battle_3,bandit_face1, bandit_face2],
["raider","Raider","Raiders",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_rifle_ammo,

  itm_throwing_spears,
  itm_throwing_metal_spears,
  itm_throwing_axes,

  itm_knife,
  itm_kukri_rusty,
  
  itm_metal_blade,
  itm_long_spiked_club,
  itm_big_club,
  itm_big_spiked_club,
  itm_crowbar,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_lead_pipe,
  itm_hand_axe,
  itm_one_handed_war_axe_a,
  itm_staff,
  itm_butchering_knife,
  itm_hammer_big,

  itm_light_bandit_cuirass_1,
  itm_light_bandit_armour_1,

  itm_gas_mask,
  itm_gas_mask_ca_90,
  
  itm_brodie,
  itm_brodie_face_cover,
  itm_metal_combat_helmet,

  itm_simple_helmet,
  itm_simple_helmet_face_cover,
  itm_steel_helmet_1,
  itm_steel_helmet_1b,
  itm_steel_helmet_1_face_cover,
  itm_steel_helmet_1b_face_cover, 
  itm_steel_helmet_2, 
  itm_steel_helmet_3,
  itm_steel_helmet_1_gas,
  itm_steel_helmet_1b_gas,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+rifles,attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["predator","Predator","Predators",tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,0,0,fac_outlaws,[
  itm_pistol_ammo,

  itm_throwing_spears,
  itm_throwing_metal_spears,
  itm_shuriken,
  itm_throwing_axes,

  itm_shortened_military_scythe,
  itm_katana,
  itm_spiked_club,
  itm_battle_axe,
  itm_war_axe,
  itm_sledgehammer,
  itm_makeshift_pipe,

  itm_bandit_plate_cuirass_1,
  itm_bandit_plate_cuirass_2,
  itm_bandit_plate_cuirass_3,
  itm_bandit_plate_cuirass_4,

  itm_brodie_gasmask,
  itm_brodie,
  itm_brodie_face_cover,
  itm_metal_combat_helmet,

  itm_steel_helmet_1,
  itm_steel_helmet_1b,
  itm_steel_helmet_1_face_cover,
  itm_steel_helmet_1b_face_cover, 
  itm_steel_helmet_2, 
  itm_steel_helmet_3,
  itm_steel_helmet_1_gas,
  itm_steel_helmet_1b_gas,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+smg_2,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["marauder","Marauder","Marauder",tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,0,0,fac_outlaws,[
  itm_slug_ammo,

  itm_throwing_spears,
  itm_throwing_metal_spears,

  itm_katana,
  itm_knife,
  itm_big_spiked_club,
  itm_spiked_club,
  itm_hammer_big,
  itm_sledgehammer_small,
  itm_one_handed_war_axe_a,

  itm_round_shield,
  itm_riot_shield,
  itm_tc_shield_1,
  itm_tc_shield_2,
  itm_tc_shield_5,

  itm_light_bandit_armour_1,
  itm_medium_bandit_cuirass_1,
  itm_medium_bandit_cuirass_2,
  itm_medium_bandit_cuirass_3,

  itm_brodie_gasmask,
  itm_brodie,
  itm_brodie_face_cover,
  itm_metal_combat_helmet,

  itm_steel_helmet_1,
  itm_steel_helmet_1b,
  itm_steel_helmet_1_face_cover,
  itm_steel_helmet_1b_face_cover, 
  itm_steel_helmet_2, 
  itm_steel_helmet_3,
  itm_steel_helmet_1_gas,
  itm_steel_helmet_1b_gas,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  
  itm_white_fur_collar,

  itm_mountain_horse_1,
  itm_mountain_horse_2,
  itm_mountain_horse_3,
  itm_mountain_horse_4,
  itm_mountain_horse_5,
  itm_mountain_horse_6,
  itm_mountain_horse_7,
  itm_mountain_horse_8,
  itm_mountain_horse_9,
  itm_mountain_horse_10,
  ]+shotgun_2,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],

["thief","Thief","Thief",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_pistol_ammo,

  itm_darts,
  itm_shuriken,
  itm_crook_revolver_1,

  itm_simple_knife,
  itm_knife,
  itm_butchering_knife,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,

  itm_hooded_cloak_1,
  itm_hooded_cloak_2,
  itm_hooded_cloak_3,
  itm_hooded_cloak_4,
  itm_hooded_cloak_5,
  itm_bandit_hood_blk,
  itm_bandit_hood_blu,
  itm_bandit_hood_grn,
  itm_bandit_hood_red,
  itm_bandit_hood_wht,
  itm_bandit_hood_blk_scarf,
  itm_bandit_hood_blu_scarf,
  itm_bandit_hood_grn_scarf,
  itm_bandit_hood_red_scarf,
  itm_bandit_hood_wht_scarf,
  
  itm_leather_gloves,
  itm_black_gloves,
  ]+revolvers,attr_lvl_20,wp_3_m,knows_battle_3,bandit_face1, bandit_face2],

["criminal_escaped","Escaped_Criminal","Escaped_Criminals",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_pistol_ammo,

  itm_wooden_stick,
  itm_club,
  itm_metal_blade,
  itm_long_spiked_club,
  itm_staff,
  itm_2by4nails,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_hatchet,
  itm_pickaxe,
  itm_staff,
  itm_simple_knife,

  itm_stones,
  itm_throwing_knives,
  itm_darts,
  itm_crook_revolver_1,

  itm_wooden_shield,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,

  itm_bandana_camo,
  itm_bandana_camo_goggles,
  itm_bandana_black,
  itm_bandana_black_goggles,
  itm_bandana_blue,
  itm_bandana_blue_goggles,
  itm_bandana_red,
  itm_bandana_red_goggles,
  itm_bandana_green,
  itm_bandana_green_goggles,
  itm_bandana_white,
  itm_bandana_white_goggles,
  itm_head_wrappings,
  itm_bandit_hood_blk,
  itm_bandit_hood_blu,
  itm_bandit_hood_grn,
  itm_bandit_hood_red,
  itm_bandit_hood_wht,
  itm_bandit_hood_blk_scarf,
  itm_bandit_hood_blu_scarf,
  itm_bandit_hood_grn_scarf,
  itm_bandit_hood_red_scarf,
  itm_bandit_hood_wht_scarf,

  itm_leather_gloves,
  itm_black_gloves,
  ]+revolvers,attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["criminal","Footpad","Footpads",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_pistol_ammo,

  itm_knife,
  itm_bayonet_2,
  itm_big_spiked_club,
  itm_bowie_knife,
  
  itm_crook_revolver_1,

  itm_swamp_bandit_1,
  itm_swamp_bandit_2,

  itm_swamp_headwear_1,
  itm_swamp_headwear_2,
  itm_swamp_headwear_3,

  itm_leather_gloves,
  itm_black_gloves,
  ],attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["slaver","Cut_throat","Cut_throats",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_pistol_ammo,
  
  itm_crook_revolver_1,
  
  itm_club,
  itm_spiked_club,
  itm_sledgehammer,
  itm_makeshift_pipe,
  itm_round_shield_leather,
  itm_round_shield,
  itm_wooden_shield,
  itm_wooden_stick,
  itm_staff,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,

  itm_swamp_bandit_1,
  itm_swamp_bandit_2,
  itm_swamp_bandit_3,
  itm_swamp_bandit_4,

  itm_swamp_headwear_1,
  itm_swamp_headwear_2,
  itm_swamp_headwear_3,

  itm_leather_gloves,
  itm_black_gloves,

  ]+revolvers,attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["outlaw","Outlaw","Outlaws",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_rifle_ammo,

  itm_knife,
  itm_bayonet_1,
  itm_bowie_knife,

  itm_swamp_bandit_4,
  itm_light_bandit_cuirass_1,

  itm_swamp_headwear_1,
  itm_swamp_headwear_2,
  itm_swamp_headwear_3,

  itm_leather_gloves,
  itm_black_gloves,
  ]+rifles,attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["highwayman","Highwayman","Highwaymen",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_rifle_ammo,

  itm_throwing_spears,
  itm_throwing_metal_spears,
  itm_throwing_axes,
  
  
  itm_shortened_military_scythe,
  itm_spiked_club,
  itm_sledgehammer,
  itm_battle_axe,
  itm_makeshift_pipe,

  itm_bandit_1,
  itm_bandit_2,

  itm_brodie_gasmask,
  itm_brodie,
  itm_brodie_face_cover,
  itm_metal_combat_helmet,

  itm_steel_helmet_1,
  itm_steel_helmet_1b,
  itm_steel_helmet_1_face_cover,
  itm_steel_helmet_1b_face_cover, 
  itm_steel_helmet_2, 
  itm_steel_helmet_3,
  itm_steel_helmet_1_gas,
  itm_steel_helmet_1b_gas,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  
  itm_mountain_horse_1,
  itm_mountain_horse_2,
  itm_mountain_horse_3,
  itm_mountain_horse_4,
  itm_mountain_horse_5,
  itm_mountain_horse_6,
  itm_mountain_horse_7,
  itm_mountain_horse_8,
  itm_mountain_horse_9,
  itm_mountain_horse_10,
  ]+carbines,attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["techno_thief","Corpse-thief","Corpse-thieves",tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_outlaws,[
  itm_shovel,
  itm_shovel_short,
  itm_entrenching_tool,

  itm_sloppy_trench_coat,

  itm_gas_mask,
  
  itm_gas_mask_ww,
  itm_gas_mask_ww_e,
  itm_gas_mask_ca_90,
  
  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ],attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["smuggler","Smuggler","Smugglers",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_rifle_ammo,

  itm_darts,

  itm_bayonet_1,
  itm_bowie_knife,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,
  
  itm_hooded_cloak_1,
  itm_hooded_cloak_2,
  itm_hooded_cloak_3,
  itm_hooded_cloak_4,
  itm_hooded_cloak_5,
  itm_bandit_hood_blk,
  itm_bandit_hood_blu,
  itm_bandit_hood_grn,
  itm_bandit_hood_red,
  itm_bandit_hood_wht,
  itm_bandit_hood_blk_scarf,
  itm_bandit_hood_blu_scarf,
  itm_bandit_hood_grn_scarf,
  itm_bandit_hood_red_scarf,
  itm_bandit_hood_wht_scarf,
  
  itm_leather_gloves,
  itm_black_gloves,
  ]+rifles,attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],

["thug","Thug","Thugs",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_pistol_ammo,

  itm_crook_revolver_1,
  
  itm_knife,
  itm_kukri_rusty,
  itm_metal_blade,
  itm_bayonet_1,
  itm_big_club,
  itm_hammer_big,
  itm_one_handed_war_axe_a,

  itm_light_bandit_armour_1,
  itm_bandit_3,
  itm_bandit_4,
  
  itm_brodie,
  itm_brodie_face_cover,

  itm_steel_helmet_1,
  itm_steel_helmet_1b,
  itm_steel_helmet_1_face_cover,
  itm_steel_helmet_1b_face_cover, 
  itm_steel_helmet_2, 
  itm_steel_helmet_3,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+revolvers,
  attr_lvl_25,wp_4_m,knows_battle_4,
  bandit_face1, bandit_face2],
["bruiser","Bruiser","Bruisers",tf_has_body|tf_has_hand,0,0,fac_outlaws,[
  itm_brassknuckles,

  itm_light_bandit_armour_1,
  itm_poor_shirt_5,
  itm_bandit_5,
  
  itm_brodie,
  itm_brodie_face_cover,

  itm_steel_helmet_1,
  itm_steel_helmet_1b,
  itm_steel_helmet_1_face_cover,
  itm_steel_helmet_1b_face_cover, 
  itm_steel_helmet_2, 
  itm_steel_helmet_3,
  ],
  attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["slasher","Slasher","Slashers",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_pistol_ammo,

  itm_crook_revolver_1,
  
  itm_knife,
  itm_metal_blade,
  itm_bayonet_1,
  itm_trench_knife,
  itm_trench_knife_1,
  

  itm_light_bandit_armour_1,
  itm_bandit_3,
  itm_bandit_4,

  itm_brodie,
  itm_brodie_gasmask,
  itm_brodie_face_cover,
  itm_steel_helmet_2,
  itm_steel_helmet_2_gas,
  itm_welder_mask_ms,

  itm_pot_helmet,
  itm_pot_helmet_face_cover,

  itm_simple_helmet,
  itm_simple_helmet_face_cover,
  itm_steel_helmet_1,
  itm_steel_helmet_1b,
  itm_steel_helmet_1_face_cover,
  itm_steel_helmet_1b_face_cover, 
  itm_steel_helmet_2, itm_steel_helmet_3,
  itm_steel_helmet_1_gas,
  itm_steel_helmet_1b_gas,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+semi_pistols,
  attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],

["butcher_thug","Butcher","Butchers",tf_has_body,0,0,fac_outlaws,[
  itm_pistol_ammo,

  itm_cleaver,
  itm_butchering_knife,

  itm_leather_vest_1,
  itm_leather_vest_2,
  itm_leather_vest_3,
  
  itm_simple_helmet,
  itm_simple_helmet_face_cover,
  itm_steel_helmet_1,
  itm_steel_helmet_1b,
  itm_steel_helmet_1_face_cover,
  itm_steel_helmet_1b_face_cover, 
  itm_steel_helmet_2, 
  itm_steel_helmet_3,
  itm_bandit_fullhelm,
  itm_bandit_fullhelm2,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+smg_1,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],

["enforcer","Enforcer","Enforcers",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_pistol_ammo,

  itm_katana,
  
  itm_shortened_military_scythe,
  itm_spiked_club,
  itm_big_spiked_club,
  itm_makeshift_pipe,
  itm_sledgehammer,
  itm_battle_axe,
  itm_war_axe,

  itm_medium_bandit_cuirass_1,
  itm_medium_bandit_cuirass_2,
  itm_medium_bandit_cuirass_3,
  
  itm_bandit_fullhelm,
  itm_bandit_fullhelm2,
  itm_bucket_helm,
  itm_metal_combat_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+smg_3,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["bandit_chief","Bandit_Chief","Bandit_Chiefs",tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,0,0,fac_outlaws,[
  itm_rifle_ammo_pw,

  itm_knife,
  itm_battle_axe,
  itm_war_axe,
  itm_one_handed_war_axe_a,
  itm_hammer_big,
  itm_big_spiked_club,
  itm_spiked_club,

  itm_round_shield_leather,
  itm_round_shield,
  itm_tc_shield_1,
  itm_tc_shield_2,
  itm_tc_shield_5,

  itm_bandit_plate_cuirass_1,
  itm_bandit_plate_cuirass_2,
  itm_bandit_plate_cuirass_3,
  itm_bandit_plate_cuirass_4,
  
  itm_bandit_fullhelm,
  itm_bandit_fullhelm2,
  itm_bucket_helm,
  itm_bandit_bulwark_helm,
  itm_metal_combat_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  itm_scale_gauntlets,
  ]+carbines,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],

["gunslinger","Gunslinger","Gunslingers",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_pistol_ammo_4,

  itm_kukri_rusty,
  itm_knife,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_lead_pipe,
  itm_bowie_knife,

  itm_bandit_1,
  itm_bandit_2,

  itm_leather_gloves,
  itm_black_gloves,
  ]+semi_pistols,
  attr_lvl_25,wp_4_r,knows_battle_4,bandit_face1, bandit_face2],
["assassin","Assassin","Assassin",tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,0,0,fac_outlaws,[
  itm_pistol_ammo_pw,
  itm_pistol_walther_ppk_sil,

  itm_butchering_knife,
  itm_bowie_knife,
  itm_trench_knife,
  itm_trench_knife_1,

  itm_northern_bandit_1,
  
  itm_hooded_cloak_1,
  itm_hooded_cloak_2,
  itm_hooded_cloak_3,
  itm_hooded_cloak_4,
  itm_hooded_cloak_5,

  itm_black_gloves,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["gunner","Gunner","Gunners",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_mg_ammo,

  itm_kukri_rusty,
  itm_knife,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_lead_pipe,
  itm_bowie_knife,

  itm_bandit_3,
  itm_bandit_4,

  itm_brodie,
  itm_brodie_face_cover,

  itm_steel_helmet_1,
  itm_steel_helmet_1b,
  itm_steel_helmet_1_face_cover,
  itm_steel_helmet_1b_face_cover,
  itm_steel_helmet_2, 
  itm_steel_helmet_3,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+lmg_1,attr_lvl_30,wp_4_r,knows_battle_4,bandit_face1, bandit_face2],
["sniper","Sniper","Snipers",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_large_caliber_ammo,

  itm_kukri_rusty,
  itm_knife,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_lead_pipe,
  itm_bowie_knife,

  itm_northern_bandit_1,

  itm_balaclava_black,
  itm_balaclava_green,
  itm_balaclava_grey,
  itm_balaclava_tan,

  itm_leather_gloves,
  itm_black_gloves,
  ]+sniper_1,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["saboteur","Saboteur","Saboteurs",tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,0,0,fac_outlaws,[
  itm_pistol_ammo,

  itm_dynamite,
  itm_dynamite,
  itm_grenade,
  itm_grenade_molotov,
  itm_grenade_stick,

  itm_knife,
  itm_crowbar,
  itm_wrench,
  itm_lead_pipe,
  itm_hammer_big,
  itm_hand_axe,
  itm_bowie_knife,

  itm_northern_bandit_1,

  itm_hooded_cloak_1,
  itm_hooded_cloak_2,
  itm_hooded_cloak_3,
  itm_hooded_cloak_4,
  itm_hooded_cloak_5,
  itm_welder_mask_ms,

  itm_leather_gloves,
  itm_black_gloves,
  ]+smg_2,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["assassin_sniper","Assassin Sniper","Assassin Sniper",tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,0,0,fac_outlaws,[
  itm_large_caliber_ammo_pw,

  itm_bowie_knife,
  itm_trench_knife,
  itm_trench_knife_1,

  itm_northern_bandit_1,

  itm_hooded_cloak_1,
  itm_hooded_cloak_2,
  itm_hooded_cloak_3,
  itm_hooded_cloak_4,
  itm_hooded_cloak_5,
  itm_camouflage_helmet,

  itm_black_gloves,
  ]+sniper_1,
  attr_lvl_30,wp_5_r,knows_battle_5,bandit_face1, bandit_face2],

["predator_legend","Legendary Predator","Legendary Predators",tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,0,0,fac_outlaws,[
  itm_rifle_ammo,

  itm_shortened_military_scythe,
  itm_katana,
  itm_spiked_club,
  itm_battle_axe,
  itm_war_axe,
  itm_sledgehammer,
  itm_makeshift_pipe,

  itm_heavy_bandit_armour,
  itm_heavy_bandit_armour_rusty,
  itm_heavy_bandit_armour_burnt,
  
  itm_bandit_knight_helm,
  itm_bandit_knight_helm_rusty,
  itm_bandit_knight_helm_burnt,
  itm_bucket_helm,
  itm_bandit_bulwark_helm,

  itm_leather_gloves_metal,
  itm_black_gloves_metal,
  itm_scale_gauntlets,
  
  itm_white_fur_collar,
  ]+rifles,
  attr_lvl_35,wp_6_m,knows_battle_6,
  bandit_face1, bandit_face2],
["marauder_legend","Legendary Marauder","Legendary Marauder",tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,0,0,fac_outlaws,[
  itm_buckshot_ammo,

  itm_katana,
  itm_knife,
  itm_big_spiked_club,
  itm_spiked_club,
  itm_hammer_big,
  itm_sledgehammer_small,
  itm_one_handed_war_axe_a,

  itm_round_shield,
  itm_riot_shield,
  itm_tc_shield_1,
  itm_tc_shield_2,
  itm_tc_shield_5,

  itm_bandit_plate_cuirass_1,
  itm_bandit_plate_cuirass_2,
  itm_bandit_plate_cuirass_3,
  itm_bandit_plate_cuirass_4,
  
  itm_bandit_trench_helm,
  itm_bucket_helm,
  itm_bandit_bulwark_helm,

  itm_leather_gloves_metal,
  itm_black_gloves_metal,
  itm_scale_gauntlets,
  
  itm_white_fur_collar,

  itm_mountain_horse_1,
  itm_mountain_horse_2,
  itm_mountain_horse_3,
  itm_mountain_horse_4,
  itm_mountain_horse_5,
  itm_mountain_horse_6,
  itm_mountain_horse_7,
  itm_mountain_horse_8,
  itm_mountain_horse_9,
  itm_mountain_horse_10,
  ]+shotgun_2,
  attr_lvl_35,wp_6_m,knows_battle_6,bandit_face1, bandit_face2],

#Adventurers
["wasteland_bandit","Adventurer","Adventurer_Regulars",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_pistol_ammo,

  itm_throwing_knives,
  itm_darts,

  itm_knife,
  itm_kukri_rusty,
  itm_metal_blade,
  itm_mace_1,
  itm_spiked_club,
  itm_crowbar,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_lead_pipe,
  itm_hatchet,
  itm_hand_axe,
  itm_knife,
  itm_butchering_knife,

  itm_adventurer_black,
  itm_adventurer_blue,
  itm_adventurer_blue_red,
  itm_adventurer_blue_yellow,
  itm_adventurer_brown,
  itm_adventurer_green,
  itm_adventurer_grey,
  itm_adventurer_grey_2,
  itm_adventurer_orange,
  itm_adventurer_red,
  itm_adventurer_red_yellow,
  itm_adventurer_yellow,

  itm_adventurer_black_hat,
  itm_adventurer_blue_hat,
  itm_adventurer_blue_red_hat,
  itm_adventurer_blue_yellow_hat,
  itm_adventurer_brown_hat,
  itm_adventurer_green_hat,
  itm_adventurer_grey_hat,
  itm_adventurer_grey_hat_2,
  itm_adventurer_orange_hat,
  itm_adventurer_red_hat,
  itm_adventurer_red_yellow_hat,
  itm_adventurer_yellow_hat,
  
  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+revolvers,attr_lvl_20,wp_3_m,knows_battle_3,bandit_face1, bandit_face2],
["wasteland_raider","Rowdy_Adventurer","Rowdy_Adventurers",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,[
  itm_rifle_ammo,

  itm_throwing_metal_spears,
  itm_throwing_axes,

  itm_knife,
  itm_knife,
  itm_kukri_rusty,
  
  itm_metal_blade,
  itm_long_spiked_club,
  itm_big_club,
  itm_big_spiked_club,
  itm_crowbar,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_lead_pipe,
  itm_hand_axe,
  itm_one_handed_war_axe_a,
  itm_staff,
  itm_butchering_knife,
  itm_hammer_big,

  itm_adventurer_rough_black,
  itm_adventurer_rough_blue,
  itm_adventurer_rough_blue_red,
  itm_adventurer_rough_brown,
  itm_adventurer_rough_cream,
  itm_adventurer_rough_green,

  itm_adventurer_rough_black_hat,
  itm_adventurer_rough_blue_hat,
  itm_adventurer_rough_blue_red_hat,
  itm_adventurer_rough_brown_hat,
  itm_adventurer_rough_cream_hat,
  itm_adventurer_rough_green_hat,
  
  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+carbines,attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["wasteland_predator","Adventurer_Toff","Adventurer_Toffs",tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,
  0,0,fac_outlaws,
  [
  itm_pistol_ammo,
  
  itm_bayonet_1,
  itm_bayonet_2,
  itm_bayonet_3,
  itm_bayonet_4,

  itm_adventurer_rich_black,
  itm_adventurer_rich_blue,
  itm_adventurer_rich_grey,
  itm_adventurer_rich_light_blue,
  itm_adventurer_rich_orange,
  itm_adventurer_rich_red,
  itm_adventurer_rich_white,

  itm_adventurer_rich_black_hat,
  itm_adventurer_rich_blue_hat,
  itm_adventurer_rich_grey_hat,
  itm_adventurer_rich_light_blue_hat,
  itm_adventurer_rich_orange_hat,
  itm_adventurer_rich_red_hat,
  itm_adventurer_rich_white_hat,

  itm_leather_gloves,
  itm_black_gloves,
  ]+smg_2,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["wasteland_marauder","Adventurer_Bravado","Adventurer_Bravados",tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,
  0,0,fac_outlaws,
  [
  itm_slug_ammo,

  itm_throwing_metal_spears,

  itm_katana,
  itm_knife,
  itm_big_spiked_club,
  itm_spiked_club,
  itm_hammer_big,
  itm_sledgehammer_small,
  itm_one_handed_war_axe_a,

  itm_round_shield,
  itm_riot_shield,
  itm_tc_shield_1,
  itm_tc_shield_2,
  itm_tc_shield_5,

  itm_adventurer_bravado_grey,
  itm_adventurer_bravado_blue,

  itm_adventurer_bravado_grey_hat,
  itm_adventurer_bravado_blue_hat,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),

  itm_mountain_horse_1,
  itm_mountain_horse_2,
  itm_mountain_horse_3,
  itm_mountain_horse_4,
  itm_mountain_horse_5,
  itm_mountain_horse_6,
  itm_mountain_horse_7,
  itm_mountain_horse_8,
  itm_mountain_horse_9,
  itm_mountain_horse_10,
  ]+shotgun_1,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["warlord","Adventurer_Leader","Adventurer_Leaders",tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,
  0,0,fac_outlaws,
  [
  itm_buckshot_ammo,

  itm_shortened_military_scythe,
  itm_katana,
  itm_battle_axe,
  itm_war_axe,
  itm_sledgehammer,
  itm_persian_broadsword,
  itm_kukri,
  itm_big_spiked_club,
  itm_spiked_club,
  itm_hammer_big,
  itm_sledgehammer_small,
  itm_one_handed_war_axe_a,

  itm_adventurer_rich_black,
  itm_adventurer_rich_blue,
  itm_adventurer_rich_grey,
  itm_adventurer_rich_light_blue,
  itm_adventurer_rich_orange,
  itm_adventurer_rich_red,
  itm_adventurer_rich_white,

  itm_adventurer_rich_black_hat,
  itm_adventurer_rich_blue_hat,
  itm_adventurer_rich_grey_hat,
  itm_adventurer_rich_light_blue_hat,
  itm_adventurer_rich_orange_hat,
  itm_adventurer_rich_red_hat,
  itm_adventurer_rich_white_hat,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),

  itm_aux_armour_1,
  ]+shotgun_2,
  attr_lvl_35,wp_6_m,knows_battle_6,bandit_face1, bandit_face2],

#totem_raiders
["jackal_raider","Boar_Raider","Boar_Raiders",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,
  [
  itm_pistol_ammo,

  itm_throwing_knives,
  itm_darts,
  itm_crook_revolver_1,

  itm_knife,
  itm_kukri_rusty,
  itm_metal_blade,
  itm_mace_1,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_hand_axe,
  itm_staff,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_1,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  ]+revolvers,
  attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["jackal_predator","Boar_Predator","Boar_Predators",tf_has_body|tf_guarantee_ranged|tf_has_head,0,0,fac_outlaws,
  [
  itm_rifle_ammo,

  itm_throwing_metal_spears,
  itm_shuriken,
  itm_throwing_axes,

  itm_big_spiked_club,
  itm_spiked_club,
  itm_sledgehammer,
  itm_battle_axe,
  itm_war_axe,
  
  
  itm_shortened_military_scythe,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_1,

  itm_boar_cloak,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+carbines,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["jackal_marauder","Boar_Marauder","Boar_Marauder",tf_has_body|tf_guarantee_ranged|tf_has_head,0,0,fac_outlaws,
  [
  itm_rifle_ammo,

  itm_big_spiked_club,
  itm_spiked_club,
  itm_lead_pipe,
  itm_hammer_big,
  itm_sledgehammer_small,
  itm_one_handed_war_axe_a,
  itm_staff,
  itm_knife,
  itm_knife,
  itm_kukri_rusty,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_1,

  itm_boar_cloak,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+rifles,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["jackal_chieftain","Boar_Chieftain","Boar_Chieftains",tf_has_body|tf_guarantee_all|tf_guarantee_ranged|tf_has_head,0,0,fac_outlaws,
  [
  itm_rifle_ammo,

  itm_big_spiked_club,
  itm_spiked_club,
  itm_sledgehammer,
  itm_battle_axe,
  itm_war_axe,
  
  
  itm_shortened_military_scythe,
  itm_big_spiked_club,
  itm_hammer_big,
  itm_sledgehammer_small,
  itm_one_handed_war_axe_a,
  itm_knife,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_2,

  itm_boar_cloak,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  
  itm_aux_armour_1,
  ]+rifles,
  attr_lvl_35,wp_6_m,knows_battle_6,bandit_face1, bandit_face2],

["boar_raider","Boar_Raider","Boar_Raiders",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,
  [
  itm_pistol_ammo,

  itm_throwing_knives,
  itm_darts,
  itm_crook_revolver_1,

  itm_knife,
  itm_kukri_rusty,
  itm_metal_blade,
  itm_mace_1,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_hand_axe,
  itm_staff,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_1,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  ]+revolvers,
  attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["boar_predator","Boar_Predator","Boar_Predators",tf_has_body|tf_guarantee_ranged|tf_has_head,0,0,fac_outlaws,
  [
  itm_rifle_ammo,

  itm_throwing_metal_spears,
  itm_shuriken,
  itm_throwing_axes,

  itm_big_spiked_club,
  itm_spiked_club,
  itm_sledgehammer,
  itm_battle_axe,
  itm_war_axe,
  
  
  itm_shortened_military_scythe,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_1,

  itm_boar_cloak,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+carbines,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["boar_marauder","Boar_Marauder","Boar_Marauder",tf_has_body|tf_guarantee_ranged|tf_has_head,0,0,fac_outlaws,
  [
  itm_rifle_ammo,

  itm_big_spiked_club,
  itm_spiked_club,
  itm_lead_pipe,
  itm_hammer_big,
  itm_sledgehammer_small,
  itm_one_handed_war_axe_a,
  itm_staff,
  itm_knife,
  itm_knife,
  itm_kukri_rusty,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_1,

  itm_boar_cloak,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+rifles,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["boar_chieftain","Boar_Chieftain","Boar_Chieftains",tf_has_body|tf_guarantee_all|tf_guarantee_ranged|tf_has_head,0,0,fac_outlaws,
  [
  itm_rifle_ammo,

  itm_big_spiked_club,
  itm_spiked_club,
  itm_sledgehammer,
  itm_battle_axe,
  itm_war_axe,
  
  
  itm_shortened_military_scythe,
  itm_big_spiked_club,
  itm_hammer_big,
  itm_sledgehammer_small,
  itm_one_handed_war_axe_a,
  itm_knife,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_2,

  itm_boar_cloak,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  
  itm_aux_armour_1,
  ]+rifles,
  attr_lvl_35,wp_6_m,knows_battle_6,bandit_face1, bandit_face2],

["goat_raider","Goat_Raider","Goat_Raiders",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,
  [
  itm_pistol_ammo,

  itm_throwing_knives,
  itm_darts,
  itm_crook_revolver_1,

  itm_knife,
  itm_kukri_rusty,
  itm_metal_blade,
  itm_mace_1,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_hand_axe,
  itm_staff,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_1,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  ]+revolvers,
  attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["goat_predator","Goat_Predator","Goat_Predators",tf_has_body|tf_guarantee_ranged|tf_has_head,0,0,fac_outlaws,
  [
  itm_rifle_ammo,

  itm_throwing_metal_spears,
  itm_shuriken,
  itm_throwing_axes,

  itm_big_spiked_club,
  itm_spiked_club,
  itm_sledgehammer,
  itm_battle_axe,
  itm_war_axe,
  
  
  itm_shortened_military_scythe,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_1,

  itm_boar_cloak,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+carbines,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["goat_marauder","Goat_Marauder","Goat_Marauder",tf_has_body|tf_guarantee_ranged|tf_has_head,0,0,fac_outlaws,
  [
  itm_rifle_ammo,

  itm_big_spiked_club,
  itm_spiked_club,
  itm_lead_pipe,
  itm_hammer_big,
  itm_sledgehammer_small,
  itm_one_handed_war_axe_a,
  itm_staff,
  itm_knife,
  itm_knife,
  itm_kukri_rusty,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_1,

  itm_boar_cloak,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+rifles,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["goat_chieftain","Goat_Chieftain","Goat_Chieftains",tf_has_body|tf_guarantee_all|tf_guarantee_ranged|tf_has_head,0,0,fac_outlaws,
  [
  itm_rifle_ammo,

  itm_big_spiked_club,
  itm_spiked_club,
  itm_sledgehammer,
  itm_battle_axe,
  itm_war_axe,
  
  
  itm_shortened_military_scythe,
  itm_big_spiked_club,
  itm_hammer_big,
  itm_sledgehammer_small,
  itm_one_handed_war_axe_a,
  itm_knife,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_2,

  itm_boar_cloak,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  
  itm_aux_armour_1,
  ]+rifles,
  attr_lvl_35,wp_6_m,knows_battle_6,bandit_face1, bandit_face2],

["bear_raider","Bear_Raider","Bear_Raiders",tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,
  [
  itm_pistol_ammo,

  itm_throwing_knives,
  itm_darts,
  itm_crook_revolver_1,

  itm_knife,
  itm_kukri_rusty,
  itm_metal_blade,
  itm_mace_1,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_hand_axe,
  itm_staff,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_1,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  ]+revolvers,
  attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["bear_predator","Bear_Predator","Bear_Predators",tf_has_body|tf_guarantee_ranged|tf_has_head,0,0,fac_outlaws,
  [
  itm_rifle_ammo,

  itm_throwing_metal_spears,
  itm_shuriken,
  itm_throwing_axes,

  itm_big_spiked_club,
  itm_spiked_club,
  itm_sledgehammer,
  itm_battle_axe,
  itm_war_axe,
  
  
  itm_shortened_military_scythe,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_1,

  itm_boar_cloak,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+carbines,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["bear_marauder","Bear_Marauder","Bear_Marauder",tf_has_body|tf_guarantee_ranged|tf_has_head,0,0,fac_outlaws,
  [
  itm_rifle_ammo,

  itm_big_spiked_club,
  itm_spiked_club,
  itm_lead_pipe,
  itm_hammer_big,
  itm_sledgehammer_small,
  itm_one_handed_war_axe_a,
  itm_staff,
  itm_knife,
  itm_knife,
  itm_kukri_rusty,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_1,

  itm_boar_cloak,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+rifles,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["bear_chieftain","Bear_Chieftain","Bear_Chieftains",tf_has_body|tf_guarantee_all|tf_guarantee_ranged|tf_has_head,0,0,fac_outlaws,
  [
  itm_rifle_ammo,

  itm_big_spiked_club,
  itm_spiked_club,
  itm_sledgehammer,
  itm_battle_axe,
  itm_war_axe,
  
  
  itm_shortened_military_scythe,
  itm_big_spiked_club,
  itm_hammer_big,
  itm_sledgehammer_small,
  itm_one_handed_war_axe_a,
  itm_knife,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,
  
  itm_wild_bodypaint_2,

  itm_boar_cloak,

  itm_boar_helmet,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  
  itm_aux_armour_1,
  ]+rifles,
  attr_lvl_35,wp_6_m,knows_battle_6,bandit_face1, bandit_face2],

#nomads
["nomad_wastrel","Nomad_Wastrel","Nomad_Wastrels",tf_has_body|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_arrows,
  itm_pistol_ammo,
  
  itm_crook_revolver_1,

  itm_club,
  itm_big_club,
  itm_crowbar,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_hatchet,
  itm_simple_knife,
  itm_knife,
  itm_kukri_rusty,
  itm_kukri_old,
  itm_metal_blade,
  itm_shovel_short,

  itm_throwing_knives,
  itm_darts,
  itm_short_bow,

  itm_leather_gloves,
  itm_black_gloves,

  itm_goatskin_tunic,
  
  itm_goat_cap,
  ]+revolvers,
  attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],
["nomad_vagabond","Nomad_Vagabond","Nomad_Vagabonds",tf_has_body|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_pistol_ammo,

  itm_darts,

  itm_mace_1,
  itm_big_club,
  itm_crowbar,
  itm_lead_pipe,
  itm_hand_axe,
  itm_bowie_knife,
  itm_knife,
  itm_knife,
  itm_metal_blade,
  itm_shovel,
  itm_hammer_big,

  itm_goatskin_tunic,
  
  itm_goat_cap,
  
  itm_leather_gloves,
  itm_black_gloves,
  ]+semi_pistols,
  attr_lvl_15,wp_2_m,knows_battle_2,mercenary_face_1, mercenary_face_2],
["nomad_drifter","Nomad_Drifter","Nomad_Drifters",tf_has_body|tf_has_ranged,no_scene,reserved,fac_commoners,[
  itm_rifle_ammo,

  itm_knife,
  itm_bayonet_2,
  itm_bayonet_1,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_bastard_club_1,
  itm_crowbar,
  itm_hatchet_tactical,
  itm_hand_axe,
  itm_bowie_knife,
  itm_hammer_big,

  itm_goatskin_tunic,
  
  itm_goat_cap,
  
  itm_white_fur_collar,

  itm_leather_gloves,
  itm_black_gloves,
  ]+carbines,
  attr_lvl_25,wp_4_m,knows_battle_4,mercenary_face_1, mercenary_face_2],
["nomad_wanderer","Nomad_Wanderer","Nomad_Wanderers",tf_has_body|tf_has_ranged|tf_has_hand,no_scene,reserved,fac_commoners,[
  itm_rifle_ammo,

  itm_knife,
  itm_bayonet_2,
  itm_katana,
  itm_bayonet_1,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_bastard_club_1,
  itm_hatchet_tactical,
  itm_big_spiked_club,

  itm_goatskin_tunic,
  
  itm_goat_hat,
  
  itm_white_fur_collar,

  itm_leather_gloves,
  itm_black_gloves,
  ]+rifles,
  attr_lvl_30,wp_5_m,knows_battle_5,mercenary_face_1, mercenary_face_2],

#Foreign Adventurers
["scavenger_violent","Foreign_Adventurer","Foreign_Adventurers",
  tf_has_body|tf_has_head|tf_has_ranged,no_scene,reserved,fac_outlaws,
  [
  itm_pistol_ammo,

  itm_adventurer_foreign_barshide_1,
  itm_adventurer_foreign_barshide_2,
  itm_adventurer_foreign_shonson_1,
  itm_adventurer_foreign_shonson_2,
  itm_adventurer_foreign_quvair_1,
  itm_adventurer_foreign_laloch_1,
  itm_adventurer_foreign_laloch_2,
  itm_adventurer_foreign_istak_1,
  itm_adventurer_foreign_istak_2,
  itm_adventurer_foreign_kesoki_1,
  itm_adventurer_foreign_kesoki_2,
  
  itm_adventurer_foreign_barshide_hat_1,
  itm_adventurer_foreign_barshide_hat_2,
  itm_adventurer_foreign_shonson_hat_1,
  itm_adventurer_foreign_shonson_hat_2,
  itm_adventurer_foreign_quvair_hat_1,
  itm_adventurer_foreign_laloch_hat_1,
  itm_adventurer_foreign_laloch_hat_2,
  itm_adventurer_foreign_istak_hat_1,
  itm_adventurer_foreign_istak_hat_2,
  itm_adventurer_foreign_kesoki_hat_1,
  itm_adventurer_foreign_kesoki_hat_2,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+revolvers,
  attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["scavenger_vet_violent","Veteran_Foreign_Adventurer","Veteran_Foreign_Adventurers",
  tf_has_body|tf_has_head|tf_has_ranged|tf_has_hand,no_scene,reserved,fac_outlaws,
  [
  itm_pistol_ammo,

  itm_adventurer_foreign_barshide_1,
  itm_adventurer_foreign_barshide_2,
  itm_adventurer_foreign_shonson_1,
  itm_adventurer_foreign_shonson_2,
  itm_adventurer_foreign_quvair_1,
  itm_adventurer_foreign_laloch_1,
  itm_adventurer_foreign_laloch_2,
  itm_adventurer_foreign_istak_1,
  itm_adventurer_foreign_istak_2,
  itm_adventurer_foreign_kesoki_1,
  itm_adventurer_foreign_kesoki_2,
  
  itm_adventurer_foreign_barshide_hat_1,
  itm_adventurer_foreign_barshide_hat_2,
  itm_adventurer_foreign_shonson_hat_1,
  itm_adventurer_foreign_shonson_hat_2,
  itm_adventurer_foreign_quvair_hat_1,
  itm_adventurer_foreign_laloch_hat_1,
  itm_adventurer_foreign_laloch_hat_2,
  itm_adventurer_foreign_istak_hat_1,
  itm_adventurer_foreign_istak_hat_2,
  itm_adventurer_foreign_kesoki_hat_1,
  itm_adventurer_foreign_kesoki_hat_2,

  itm_leather_gloves,
  itm_leather_gloves_metal,
  itm_black_gloves,
  itm_black_gloves_metal,
  ]+smg_1,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["scavenger_legend_violent","Renouned_Foreign_Adventurer","Renouned_Foreign_Adventurers",
  tf_has_body|tf_has_head|tf_has_ranged|tf_has_hand,no_scene,reserved,fac_outlaws,
  [
  itm_pistol_ammo_pw,

  itm_adventurer_foreign_barshide_1,
  itm_adventurer_foreign_barshide_2,
  itm_adventurer_foreign_shonson_1,
  itm_adventurer_foreign_shonson_2,
  itm_adventurer_foreign_quvair_1,
  itm_adventurer_foreign_laloch_1,
  itm_adventurer_foreign_laloch_2,
  itm_adventurer_foreign_istak_1,
  itm_adventurer_foreign_istak_2,
  itm_adventurer_foreign_kesoki_1,
  itm_adventurer_foreign_kesoki_2,
  
  itm_adventurer_foreign_barshide_hat_1,
  itm_adventurer_foreign_barshide_hat_2,
  itm_adventurer_foreign_shonson_hat_1,
  itm_adventurer_foreign_shonson_hat_2,
  itm_adventurer_foreign_quvair_hat_1,
  itm_adventurer_foreign_laloch_hat_1,
  itm_adventurer_foreign_laloch_hat_2,
  itm_adventurer_foreign_istak_hat_1,
  itm_adventurer_foreign_istak_hat_2,
  itm_adventurer_foreign_kesoki_hat_1,
  itm_adventurer_foreign_kesoki_hat_2,

  itm_leather_gloves,
  itm_leather_gloves_metal,
  itm_black_gloves,
  itm_black_gloves_metal,
  ]+smg_2,
  attr_lvl_35,wp_6_m,knows_battle_6,bandit_face1, bandit_face2],
["scavenger_power_violent","Crusher_Foreign_Adventurer","Crusher_Foreign_Adventurers",
  tf_has_body|tf_has_head|tf_has_hand,no_scene,reserved,fac_outlaws,
  [
  itm_brassknuckles,

  itm_adventurer_foreign_barshide_1,
  itm_adventurer_foreign_barshide_2,
  itm_adventurer_foreign_shonson_1,
  itm_adventurer_foreign_shonson_2,
  itm_adventurer_foreign_quvair_1,
  itm_adventurer_foreign_laloch_1,
  itm_adventurer_foreign_laloch_2,
  itm_adventurer_foreign_istak_1,
  itm_adventurer_foreign_istak_2,
  itm_adventurer_foreign_kesoki_1,
  itm_adventurer_foreign_kesoki_2,
  
  itm_adventurer_foreign_barshide_hat_1,
  itm_adventurer_foreign_barshide_hat_2,
  itm_adventurer_foreign_shonson_hat_1,
  itm_adventurer_foreign_shonson_hat_2,
  itm_adventurer_foreign_quvair_hat_1,
  itm_adventurer_foreign_laloch_hat_1,
  itm_adventurer_foreign_laloch_hat_2,
  itm_adventurer_foreign_istak_hat_1,
  itm_adventurer_foreign_istak_hat_2,
  itm_adventurer_foreign_kesoki_hat_1,
  itm_adventurer_foreign_kesoki_hat_2,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,mercenary_face_1, mercenary_face_2],

["ezeg","Ezeg","Ezegs",tf_has_body|tf_has_ranged,no_scene,reserved,fac_outlaws,[
  itm_ezeg_arrows,
  itm_recurve_bow,

  itm_kukri_old,

  itm_adventurer_foreign_barshide_1,
  itm_adventurer_foreign_barshide_2,
  
  itm_adventurer_foreign_barshide_hat_1,
  itm_adventurer_foreign_barshide_hat_2,

  itm_leather_gloves,
  itm_black_gloves,
  ],
  attr_lvl_20,wp_3_r,knows_battle_3,mercenary_face_1, mercenary_face_2],
["ezeg_raider","Ezeg_Raider","Ezeg_Raiders",tf_has_body|tf_has_ranged,no_scene,reserved,fac_outlaws,[
  itm_ezeg_arrows,
  itm_rider_bow,
  itm_skirmisher_bow,

  itm_bayonet_2,

  itm_adventurer_foreign_barshide_1,
  itm_adventurer_foreign_barshide_2,
  itm_bandit_scale_shirt_1,
  
  itm_adventurer_foreign_barshide_hat_1,
  itm_adventurer_foreign_barshide_hat_2,

  itm_leather_gloves,
  itm_black_gloves,
  ],
  attr_lvl_25,wp_4_r,knows_battle_4,mercenary_face_1, mercenary_face_2],
["ezeg_corsair","Ezeg_Corsair","Ezeg_Corsair",tf_has_body|tf_has_head|tf_guarantee_horse,no_scene,reserved,fac_outlaws,[
  itm_ezeg_arrows,
  itm_recurve_bow,

  itm_kukri_old,

  itm_bandit_scale_shirt_1,
  
  itm_adventurer_foreign_barshide_hat_1,
  itm_adventurer_foreign_barshide_hat_2,
  
  itm_white_fur_collar,

  itm_scale_gauntlets,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,mercenary_face_1, mercenary_face_2],
["ezeg_pillager","Ezeg_Pillager","Ezeg_Pillagers",tf_has_body|tf_has_head|tf_guarantee_horse|tf_has_shield|tf_has_hand,no_scene,reserved,fac_outlaws,[
  itm_ezeg_arrows,
  itm_rider_bow,
  itm_skirmisher_bow,

  itm_bayonet_2,

  itm_bandit_scale_armour_1,
  
  itm_adventurer_foreign_barshide_hat_1,
  itm_adventurer_foreign_barshide_hat_2,
  
  itm_white_fur_collar,

  itm_scale_gauntlets,
  ],
  attr_lvl_35,wp_6_m,knows_battle_6,mercenary_face_1, mercenary_face_2],

#cultists
["cultist","Throd_Cultist","Throd_Cultists",
  tf_has_body|tf_guarantee_ranged,
  0,0,fac_theocracy,
  [
  itm_pistol_ammo,

  itm_butchering_knife,
  itm_bayonet_1,
  itm_throwing_knives,
  itm_darts,

  itm_throd_robe_black,
  itm_throd_robe_grey,
  itm_throd_robe_armoured,

  itm_hood_black,
  itm_hood_black_scarf,
  itm_hood_white,
  itm_hood_white_scarf,
  itm_hood_red,
  itm_hood_red_scarf,

  itm_leather_gloves,
  itm_black_gloves,
  ]+semi_pistols,
  attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],
["fanatic","Throd_Fanatic","Throd_Fanatics",
  tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,
  0,0,fac_theocracy,
  [
  itm_pistol_ammo,
  
  itm_grenade_miasma,

  itm_crook_revolver_1,
  
  itm_knife,
  itm_kukri_rusty,
  itm_metal_blade,
  itm_bayonet_1,
  itm_butchering_knife,

  itm_wooden_shield,
  itm_wood_shield,
  itm_round_shield_leather,
  itm_round_shield,
  itm_tc_shield_1,
  itm_tc_shield_2,
  itm_tc_shield_5,

  itm_dynamite,

  itm_throd_robe_black,
  itm_throd_robe_grey,
  itm_throd_robe_armoured,

  itm_steel_helmet_2,
  itm_steel_helmet_2_gas,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+smg_1,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["zealot","Throd_Zealot","Throd_Zealots",
  tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,
  0,0,fac_theocracy,
  [
  itm_rifle_ammo,

  itm_grenade_miasma,
  
  itm_knife,
  itm_kukri_rusty,
  itm_metal_blade,
  itm_bayonet_1,
  itm_butchering_knife,
  itm_katana,

  itm_shuriken,

  itm_throd_shield,
  itm_wood_shield,
  itm_round_shield_leather,
  itm_round_shield,
  itm_tc_shield_1,
  itm_tc_shield_2,
  itm_tc_shield_5,

  itm_throd_robe_black,
  itm_throd_robe_grey,
  itm_throd_robe_armoured,

  itm_zealot_helm_1,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),

  ]+rifles,
  attr_lvl_35,wp_6_m,knows_battle_6,bandit_face1, bandit_face2],

#cannibal
["cannibal","Cannibal","Cannibals",
  tf_has_body|tf_guarantee_ranged,
  0,0,fac_cannibals,
  [
  itm_human_meat,

  itm_pistol_ammo,
  
  itm_crook_revolver_1,

  itm_butchering_knife,
  itm_cleaver,
  itm_hand_saw,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,
  
  itm_upgrade_bandage_bloody,

  itm_round_shield_flesh,

  itm_leather_gloves,
  itm_black_gloves,
  ]+rusty_guns_1,
  attr_lvl_25,wp_4_m,knows_battle_4,
  bandit_face1, bandit_face2],
["cannibal_cruel","Cruel Cannibal","Cruel Cannibals",
  tf_has_body|tf_guarantee_ranged,
  0,0,fac_cannibals,
  [
  itm_human_meat,

  itm_rifle_ammo,

  itm_cleaver,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,
  
  itm_upgrade_bandage_bloody,

  itm_round_shield_flesh,
  
  itm_white_fur_collar,

  itm_leather_gloves,
  itm_black_gloves,
  ]+carbines,
  attr_lvl_30,wp_5_m,knows_battle_5,
  bandit_face1, bandit_face2],

#fallen_phalanx
["phalanx_fresh","Fresh_Warrior_of_the_Fallen_Phalanx","Fresh_Warriors_of_the_Fallen_Phalanx",tf_has_body|tf_guarantee_ranged,0,0,fac_dark_knights,[
  itm_rifle_ammo_pw,

  itm_bayonet_1,

  itm_phalanx_uniform_1,

  itm_phalanx_fresh_helmet,

  itm_black_gloves,
  ]+rifles,
  attr_lvl_25,wp_4_r,knows_battle_4,bandit_face1, bandit_face2],
["phalanx_firstblood","Firstblood_Warrior_of_the_Fallen_Phalanx","Firstblood_Warriors_of_the_Fallen_Phalanx",tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,0,0,fac_dark_knights,[
  itm_rifle_ammo_pw,

  itm_bayonet_1,

  itm_phalanx_uniform_2,
  
  itm_phalanx_firstblood_helmet,

  itm_black_gloves,
  ]+rifles,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["phalanx_bloodied","Bloodied_Warrior_of_the_Fallen_Phalanx","Bloodied_Warriors_of_the_Fallen_Phalanx",tf_has_body|tf_guarantee_ranged,0,0,fac_dark_knights,[
  itm_rifle_ammo_pw,

  itm_bayonet_1,

  itm_phalanx_uniform_3,

  itm_phalanx_bloodied_helmet,

  itm_black_gloves,
  (itm_black_gloves_metal,imod_ragged),
  ]+rifles,
  attr_lvl_35,wp_5_r,knows_battle_5,bandit_face1, bandit_face2],
["phalanx_scarred","Scarred_Warrior_of_the_Fallen_Phalanx","Scarred_Warriors_of_the_Fallen_Phalanx",tf_has_body|tf_guarantee_ranged,0,0,fac_dark_knights,[
  itm_rifle_ammo_pw,

  itm_bayonet_1,

  itm_phalanx_uniform_4,

  itm_phalanx_scarred_helmet,

  itm_leather_gloves_metal,
  itm_black_gloves_metal,
  itm_scale_gauntlets,
  
  ]+rifles,
  attr_lvl_40,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["phalanx_chosen","Chosen_Warrior_of_the_Fallen_Phalanx","Chosen_Warriors_of_the_Fallen_Phalanx",tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet|tf_has_hand,0,0,fac_dark_knights,[
  itm_rifle_ammo_pw,

  itm_grenade_stick,
  itm_grenade_stick,

  itm_bayonet_1,

  itm_phalanx_uniform_5,

  itm_phalanx_chosen_helmet,

  itm_leather_gloves_metal,
  itm_black_gloves_metal,
  itm_scale_gauntlets,
  
  itm_aux_armour_1,
  ]+rifles,
  attr_lvl_45,wp_6_m,knows_battle_6,bandit_face1, bandit_face2],

#gangs
["the_suits","Tattoo Gangster","Tattoo Gangsters",
  tf_has_body|tf_guarantee_ranged|tf_has_head,0,0,fac_outlaws,
  [
  itm_pistol_ammo_4,
  itm_crook_revolver_1,

  itm_sloppy_trench_coat,

  itm_civil_hat_1_mask,
  itm_civil_hat_1b_mask,
  itm_civil_hat_1c_mask,
  itm_civil_hat_1d_mask,
  itm_civil_hat_2_mask,
  itm_civil_hat_3_mask,
  itm_civil_hat_4_mask,
  itm_civil_hat_5_mask,
  itm_civil_hat_7_mask,
  itm_civil_hat_9_mask,
  itm_civil_hat_10_mask,
  itm_civil_hat_11_mask,
  itm_civil_hat_12_mask,
  itm_civil_hat_13_mask,
  itm_civil_hat_14_mask,

  itm_black_gloves,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],

["sea_raider","White Wolves","White Scarves",
  tf_has_body|tf_woman|tf_guarantee_ranged,0,0,fac_outlaws,
  [
  itm_rifle_ammo,

  itm_big_club,
  itm_big_spiked_club,
  itm_spiked_club,
  itm_crowbar,
  itm_lead_pipe,
  itm_hand_axe,

  itm_throwing_metal_spears,
  itm_throwing_spears,
  itm_darts,
  itm_throwing_axes,

  itm_wooden_shield,
  itm_wood_shield,
  itm_round_shield_leather,
  itm_round_shield,

  itm_civilian_outfit_1w,
  itm_civilian_outfit_2w,
  itm_civilian_outfit_3w,
  itm_civilian_outfit_4w,
  itm_civilian_outfit_5w,
  itm_civilian_outfit_6w,
  itm_civilian_outfit_7w,
  itm_civilian_outfit_8w,
  itm_civilian_outfit_9w,
  itm_civilian_outfit_10w,
  itm_civilian_outfit_11w,
  
  itm_bandana_white,
  itm_headband_white_scarf,
  itm_hood_white_scarf,
  
  itm_white_fur_collar,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+rifles,
  attr_lvl_25,wp_4_m,knows_battle_4,woman_face_1, woman_face_2],

["blades_warrior","Revolutionary","Revolutionaries",
  tf_has_body|tf_guarantee_ranged,0,0,fac_outlaws,
  [
  itm_rifle_ammo,

  itm_blade,
  itm_metal_blade,

  itm_round_shield_leather,
  itm_round_shield,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,
  
  itm_hood_1,
  itm_hood_2,
  itm_hood_3,
  itm_hood_4,
  itm_hood_5,
  itm_hood_6,

  itm_leather_gloves,
  itm_black_gloves,
  (itm_leather_gloves_metal,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+carbines,
  attr_lvl_25,wp_4_m,knows_battle_4,bandit_face1, bandit_face2],

#bandits end

# infected
["infected_1","Miasma-stricken Civilian","Miasma Civilians",tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all_wo_ranged,0,0,fac_infected,
  [
  itm_arrows,
  itm_buckshot_ammo,

  itm_double_barrel_shotgun,
  itm_stones,
  itm_throwing_knives,
  itm_hunting_bow,
  itm_short_bow,

  itm_infected_attack,
  itm_wooden_stick,
  itm_club,
  itm_shepherds_crook,
  itm_2by4,
  itm_pitch_fork,
  itm_pitch_fork_1,
  itm_pitch_fork_2,
  itm_wrench,
  itm_shovel_short,
  itm_shovel,
  itm_hand_saw,
  itm_hammer,
  itm_hatchet,
  itm_lumberjack_axe,
  itm_pickaxe,
  itm_staff,
  itm_simple_knife,
  itm_knife,
  itm_kukri_old,

  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  
  itm_infected_2,itm_infected_3,itm_infected_4,itm_infected_5,itm_infected_6,itm_infected_7,itm_infected_9,
  ],
  attr_lvl_25,wp_2_m,knows_battle_2,x_face, x_face],
["infected_2","Miasma-stricken Watchman","Miasma-stricken Watchmen",tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_infected,
  [
  itm_pistol_ammo,

  itm_infected_2,itm_infected_3,itm_infected_4,itm_infected_5,itm_infected_6,itm_infected_7,itm_infected_9,
  
  itm_darts,
  itm_crook_revolver_1,
  
  itm_infected_attack,

  itm_mace_1,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_staff,
  itm_staff,
  itm_bowie_knife,
  itm_knife,
  itm_kukri_rusty,
  itm_kukri_old,
  itm_metal_blade,

  itm_leather_gloves,
  itm_black_gloves,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,
  ]+revolvers,
  attr_lvl_25,wp_3_m,knows_battle_3,x_face, x_face],
["infected_3","Miasma-stricken Ranger","Miasma-stricken Rangers",tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_infected,
  [
  itm_rifle_ammo,

  itm_knife,
  itm_bayonet_2,
  itm_katana,
  itm_bayonet_1,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_bastard_club_1,
  itm_hatchet_tactical,
  itm_big_spiked_club,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,

  itm_leather_gloves,
  itm_black_gloves,

  itm_infected_2,itm_infected_3,itm_infected_4,itm_infected_5,itm_infected_6,itm_infected_7,itm_infected_9,
  
  itm_infected_attack,
  ]+rifles,
  attr_lvl_30,wp_4_m,knows_battle_4,x_face, x_face],
["infected_4","Miasma-stricken Warrior","Miasma-stricken Warriors",tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_infected,
  [
  itm_shortened_military_scythe,
  itm_katana,
  itm_spiked_club,
  itm_battle_axe,
  itm_war_axe,
  itm_sledgehammer,
  itm_makeshift_pipe,

  itm_heavy_bandit_armour,
  itm_heavy_bandit_armour_rusty,
  itm_heavy_bandit_armour_burnt,

  itm_leather_gloves_metal,
  itm_black_gloves_metal,
  itm_scale_gauntlets,

  itm_infected_2,itm_infected_3,itm_infected_4,itm_infected_5,itm_infected_6,itm_infected_7,itm_infected_9,
  ],attr_lvl_30,wp_4_m,knows_battle_4,x_face, x_face],
["infected_5","Miasma-stricken Gunner","Miasma-stricken Gunners",tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_infected,
  [
  itm_mg_ammo,
  itm_lmg_type_99,

  itm_knife,
  itm_bayonet_2,
  itm_katana,
  itm_bayonet_1,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_bastard_club_1,
  itm_hatchet_tactical,
  itm_big_spiked_club,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,

  itm_leather_gloves,
  itm_black_gloves,

  itm_infected_2,itm_infected_3,itm_infected_4,itm_infected_5,itm_infected_6,itm_infected_7,itm_infected_9,
  
  itm_infected_attack,
  ],
  attr_lvl_35,wp_4_r,knows_battle_4,x_face, x_face],
["infected_6","Miasma-stricken Petard","Miasma-stricken Petards",tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_infected,
  [
  itm_lunge_mine,
  itm_dynamite,

  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,

  itm_infected_2,itm_infected_3,itm_infected_4,itm_infected_5,itm_infected_6,itm_infected_7,itm_infected_9,
  ],
  attr_lvl_30,wp_4_m,knows_battle_4,x_face, x_face],

# undeads
["undead_1","Trench Zombie","Trench Zombies",tf_undead|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_undeads,
  [
  itm_undead_1,

  itm_infected_attack,
  ],
  attr_lvl_25,wp_3_m,knows_battle_3,x_face, x_face],
["undead_2","Trench Zombie","Trench Zombies",tf_undead|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_undeads,
  [
  itm_undead_2,

  itm_infected_attack,
  ],
  attr_lvl_25,wp_3_m,knows_battle_3,x_face, x_face],

#cursed
["risen","Risen","Risen",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_undeads,
  [
  itm_pistol_ammo,
  itm_club,
  itm_trench_knife,
  itm_sharpened_stick,
  ]+revolvers,
  attr_lvl_15,wp_2_m,knows_battle_2,x_face, x_face],
  
["risen_tainted","Tainted Risen","Tainted Risen",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_undeads,
  [
  itm_rifle_ammo,
  itm_trench_club_4,
  itm_bayonet_3,
  itm_shortened_spear,
  
  itm_ravga_gauntlets,
  ]+rifles,
  attr_lvl_25,wp_3_m,knows_battle_3,x_face, x_face],

["risen_cursed","Cursed One","Cursed Ones",tf_skeleton|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_undeads,
  [
  itm_mg_ammo,
  itm_shadow_lmg,
  
  itm_flamberge,
  
  itm_cursed_one,
  itm_cursed_one_head,
  itm_invisi_gloves,
  itm_invisi_boots,
  ],
  attr_lvl_40,wp_5_m,knows_battle_5,x_face, x_face],

# mutants
["brute_mutant", "Brute Mutant", "Brute Mutants",tf_mutant_big|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0, 0, fac_mutants,
  [
  itm_miasma_ore,
  
  itm_brute_attack,
  itm_brute_body1b,
  ],
  attr_tank,wp_5_m,knows_battle_5,x_face, x_face],
["tank_mutant", "Towering Brute Mutant", "Towering Brute Mutants",tf_mutant_big|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0, 0, fac_mutants,
  [
  itm_miasma_ore,
  itm_miasma_ore,
  
  itm_tank_sword,
  itm_mutant_tank,
  ],
  attr_tank,wp_6_m,knows_battle_6,x_face, x_face],
["acid_mutant", "Bubbling Mutant", "Bubbling Mutants",tf_mutant|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_mutants,
  [
  itm_miasma_ore,
  
  itm_invisi_attack,
  itm_acid_mutant_1],
  attr_lvl_30, wp_3_m, knows_battle_3,
  x_face, x_face],
["nark_mutant_1", "Bloated Horror", "Bloated Horrors",tf_mutant_big|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0, 0, fac_mutants,
  [
  itm_miasma_ore,
  
  itm_invisi_gloves,
  itm_brute_attack,
  itm_invisi_head,
  itm_nark_mutant_1,
  itm_invisi_boots],
  attr_tank, wp_5_m, wp_5_m,x_face, x_face],
["spitter", "Spitter", "Spitters",tf_mutant|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_mutants,
  [
  itm_miasma_ore,
  
  itm_spitter_body,
  itm_infected_spit,
  itm_infected_spit,
  ],
  attr_lvl_30, wp_4_m, knows_battle_4,
  x_face, x_face],
["ghoul", "Trench Ghoul", "Trench Ghouls",tf_ghoul|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0, 0, fac_mutants,
  [
  itm_miasma_ore,
  
  itm_ghoul_body,
  itm_ghoul_body_2,
  itm_ghoul_body_3,
  itm_ghoul_body_4,
  
  itm_wooden_stick,
  itm_club,
  itm_long_spiked_club,
  itm_mace_1,
  itm_2by4,
  itm_2by4nails,
  #itm_crowbar,
  itm_lead_pipe,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_iron_staff,
  itm_hand_axe,
  #itm_lumberjack_axe,
  #itm_staff,
  itm_simple_knife,
  itm_knife,
  itm_butchering_knife,
  itm_kukri_rusty,
  itm_hand_saw,
  ],
  attr_lvl_30, wp_4_m, knows_battle_4|knows_athletics_8,x_face, x_face],
["ghoul_scavenger", "Trench Ghoul_Officer", "Trench Ghoul_Officers",tf_ghoul|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all_wo_ranged,0, 0, fac_mutants,
  [
  #itm_rifle_ammo,
  itm_pistol_ammo,
  
  itm_miasma_ore,

  itm_ghoul_body_4,
  itm_ghoul_body_3,
  #itm_ghoul_body_2,
  #itm_ghoul_body,
  
  itm_knife,
  itm_knife,
  itm_club,
  itm_mace_1,
  #itm_2by4nails,
  itm_crowbar,
  itm_lead_pipe,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_hand_axe,
 # itm_lumberjack_axe,
  #itm_staff,
  itm_trench_knife,
  itm_trench_knife_1,
  #itm_cleaver,
  itm_butchering_knife,
  itm_kukri_rusty,
  ]+rusty_guns_1,
  attr_lvl_40, wp_1_m, knows_battle_4|knows_athletics_10,x_face, x_face],
["rancor","Horse-eater","Horse-eaters",tf_rancor|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_mutants,
  [
  itm_miasma_ore,
  
  itm_rancor_body_a,
  itm_rancor_body_a,
  itm_rancor_body_a,
  itm_rancor_body_c,
  itm_invisi_head,
  itm_invisi_gloves,
  itm_invisi_boots,
  itm_rancor_attack,
  ],
  attr_tank, wp_4_m, knows_battle_4|knows_athletics_10,x_face, x_face],

["feral_beastling","Feral_Beastling","Feral_Beastlings",tf_mutant|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_mutants,
  [
  itm_miasma_ore,
  
  itm_beastling_1,
  itm_beastling_head,
  itm_beastling_hands,
  itm_rancor_attack,
  ],
  attr_lvl_30, wp_4_m, knows_battle_4|knows_athletics_8,x_face, x_face],
  
["wolfclaw_mutant","Howling Horror","Howling Horrors",tf_mutant|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_mutants,
  [
  itm_miasma_ore,
  
  itm_mutant_wolfclaw,
  itm_invisi_head,
  itm_invisi_gloves,
  itm_invisi_boots,
  itm_rancor_attack,
  ],
  attr_tank, wp_5_m, knows_battle_5,x_face, x_face],
["wolfclaw_mutant_big","Huge Howling Horror","Huge Howling Horrors",tf_mutant_big|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_all,0,0,fac_mutants,
  [
  itm_miasma_ore,
  
  itm_mutant_wolfclaw,
  itm_invisi_head,
  itm_invisi_gloves,
  itm_invisi_boots,
  itm_rancor_attack,
  ],
  attr_tank, wp_6_m, knows_battle_6,x_face, x_face],

#animals
["mutant_spider_big","Giant_Mutant_Spider", "Giant_Mutant_Spiders",tf_dummy|tf_guarantee_all|tf_guarantee_horse|tf_allways_fall_dead|tf_no_capture_alive,0, 0, fac_mutants,
  [
  itm_miasma_ore,
  
  itm_mutant_spider_big,
  itm_invisi_gloves,
  itm_invisi_head,
  itm_invisi_body,
  itm_invisi_boots,
  itm_spider_attack
  ],
  attr_tank,wp_4_m,knows_battle_4|knows_riding_10, x_face, x_face],
["mutant_spider","Mutant_Spider", "Mutant_Spiders",tf_dummy|tf_guarantee_all|tf_guarantee_horse|tf_allways_fall_dead|tf_no_capture_alive,0, 0, fac_mutants,
  [
  itm_miasma_ore,
  
  itm_mutant_spider,
  itm_invisi_gloves,
  itm_invisi_head,
  itm_invisi_body,
  itm_invisi_boots,
  itm_spider_attack
  ],
  attr_tank,wp_3_m,knows_battle_3|knows_riding_10, x_face, x_face],

["infected_doberman","Infected_Doberman", "Infected_Doberman",tf_dummy|tf_guarantee_all|tf_guarantee_horse|tf_allways_fall_dead|tf_no_capture_alive,0, 0, fac_infected,
  [
  itm_infected_doberman,
  itm_infected_doberman,
  itm_infected_doberman_2,
  itm_invisi_gloves,
  itm_invisi_head,
  itm_invisi_body,
  itm_invisi_boots,
  itm_invisi_attack,
  ],
  attr_lvl_25,wp_3_m,knows_battle_3|knows_riding_10, x_face, x_face],
["infected_dog","Infected_Dog", "Infected_Dog",tf_dummy|tf_guarantee_all|tf_guarantee_horse|tf_allways_fall_dead|tf_no_capture_alive,0, 0, fac_infected,
  [
  itm_infected_dog,
  itm_infected_dog,
  itm_infected_dog_2,
  itm_invisi_gloves,
  itm_invisi_head,
  itm_invisi_body,
  itm_invisi_boots,
  itm_invisi_attack,
  ],
  attr_lvl_25,wp_3_m,knows_battle_3|knows_riding_10, x_face, x_face],
["rabid_doberman","Rabid_Doberman", "Rabid_Doberman",tf_dummy|tf_guarantee_all|tf_guarantee_horse|tf_allways_fall_dead|tf_no_capture_alive,0, 0, fac_infected,
  [
  itm_rabid_doberman,
  itm_invisi_gloves,
  itm_invisi_head,
  itm_invisi_body,
  itm_invisi_boots,
  itm_invisi_attack,
  ],
  attr_lvl_25,wp_3_m,knows_battle_3|knows_riding_10, x_face, x_face],
["rabid_dog","Rabid_Dog", "Rabid_Dog",tf_dummy|tf_guarantee_all|tf_guarantee_horse|tf_allways_fall_dead|tf_no_capture_alive,0, 0, fac_infected,
  [
  itm_rabid_dog,
  itm_invisi_gloves,
  itm_invisi_head,
  itm_invisi_body,
  itm_invisi_boots,
  itm_invisi_attack,
  ],
  attr_lvl_25,wp_3_m,knows_battle_3|knows_riding_10, x_face, x_face],

############
##Factions##
############

## Entenaii Empire ##
["f1_tier_0","Entenaii Levy","Entenaii Levies",
  tf_has_body,0,0,fac_kingdom_1,
  [
  itm_pistol_ammo,
  itm_empire_revolver,

  itm_bowie_knife,
  itm_bayonet_2,
  itm_entrenching_tool,

  itm_entenaii_uniform_levy,
  ],
  attr_lvl_5,wp_start,knows_battle_1,man_face_younger_1, man_face_middle_2],
["f1_tier_1","Entenaii Private","Entenaii Privates",
  tf_has_body|tf_guarantee_ranged,0,0,fac_kingdom_1,
  [
  itm_pistol_ammo,
  itm_empire_revolver,

  itm_bowie_knife,
  itm_bayonet_2,
  itm_entrenching_tool,

  itm_entenaii_uniform_private,

  itm_entenaii_helmet,

  itm_entenaii_gloves,
  ],
  attr_lvl_15,wp_2_m,knows_battle_2,man_face_younger_1, man_face_middle_2],
["f1_tier_2","Entenaii Private 2nd Class","Entenaii Privates 2nd Class",
  tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_1,
  [
  itm_rifle_ammo,
  itm_empire_bolt_action_rifle,

  itm_bowie_knife,
  itm_bayonet_2,
  itm_entrenching_tool,

  itm_entenaii_uniform_private_2nd,

  itm_entenaii_helmet,

  itm_entenaii_gloves,
  ],
  attr_lvl_20,wp_3_m,knows_battle_3,man_face_young_1, man_face_old_2],
["f1_tier_3","Entenaii Private 1st Class","Entenaii Privates 1st Class",
  tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
  [
  itm_rifle_ammo,
  itm_empire_bolt_action_rifle_bayonet,
  itm_empire_bolt_action_rifle,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_bowie_knife,
  itm_bayonet_2,
  itm_trooper_sword,
  itm_entrenching_tool,
  itm_long_trench_club_1,
  itm_long_trench_club_2,

  itm_entenaii_uniform_private_1st,

  itm_entenaii_helmet_2,

  itm_entenaii_gloves,
  ],
  attr_lvl_25,wp_4_m,knows_battle_4,man_face_young_1, man_face_old_2],
["f1_tier_4","Entenaii Corporal","Entenaii Corporals",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
  [
  itm_rifle_ammo_pw,
  itm_empire_bolt_action_rifle_bayonet,

  itm_bastard_club_1,
  itm_bowie_knife,
  itm_bayonet_2,
  itm_trooper_sword,
  itm_long_trench_club_1,
  itm_long_trench_club_2,

  itm_entenaii_uniform_raider,

  itm_entenaii_helmet_3,

  itm_entenaii_gloves,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],
["f1_tier_5","Entenaii Sergeant","Entenaii Sergeants",
  tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_1,
  [
  itm_pistol_ammo_pw,
  itm_smg_sten,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_bowie_knife,
  itm_bayonet_2,
  itm_trooper_sword,

  itm_entenaii_uniform_sergeant,

  itm_entenaii_helmet_3_full,

  itm_entenaii_gloves,
  ],
  attr_lvl_35,wp_6_r,knows_battle_6,man_face_middle_1, man_face_older_2],
["f1_tier_5_infantry","Entenaii Heavy Infantry","Entenaii Heavy Infantries",
  tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_boots,0,0,fac_kingdom_1,
  [
  itm_mg_ammo,
  itm_entenaii_empire_lmg,

  itm_ironclub,

  itm_entenaii_armour,
  
  itm_entenaii_helmet_5,

  itm_entenaii_gauntlets,
  
  itm_ammo_belt_1,
  ],
  attr_lvl_35,wp_6_m,knows_battle_6,man_face_middle_1, man_face_older_2],
["f1_tier_6_sniper","Entenaii Sniper","Entenaii Snipers",
  tf_guarantee_ranged|tf_mounted|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
  [
  itm_large_caliber_ammo_pw,
  itm_empire_sniper,

  itm_bowie_knife,
  itm_bayonet_2,

  itm_entenaii_uniform_specialist,

  itm_entenaii_beret,
  
  itm_entenaii_gloves,
  
  itm_ammo_belt_3,
  ],
  attr_lvl_40,wp_6_r,knows_battle_6,man_face_middle_1, man_face_older_2],
["f1_tier_6_specialist","Entenaii Specialist","Entenaii Specialists",
  tf_guarantee_ranged|tf_mounted|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
  [
  itm_rifle_ammo_pw,
  itm_empire_bolt_action_carbine_silent,

  itm_bowie_knife,
  itm_bayonet_2,

  itm_entenaii_uniform_specialist,

  itm_entenaii_beret,
  
  itm_entenaii_gloves,
  ],
  attr_lvl_45,wp_6_r,knows_battle_6,man_face_middle_1, man_face_older_2],

#Cavalry
["f1_tier_4_cavalry","Entenaii Cuirassier","Entenaii Cuirassiers",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_kingdom_1,
  [
  itm_pistol_ammo_pw,
  itm_empire_revolver,
  
  itm_light_cav_sword,
  
  itm_entenaii_uniform_cavalry,

  itm_entenaii_helmet_4,

  itm_entenaii_demi_gauntlets,

  itm_entenaii_horse_1,
  itm_entenaii_horse_2,
  itm_entenaii_horse_3,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,man_face_middle_1, man_face_old_2],
["f1_tier_5_cavalry","Entenaii Lancer","Entenaii Lancers",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_kingdom_1,
  [
  itm_rifle_ammo_pw,
  itm_empire_bolt_action_carbine,

  itm_saber1,
  itm_lance1,
  
  itm_entenaii_armour,
  
  itm_entenaii_helmet_4,

  itm_entenaii_gauntlets,

  itm_entenaii_horse_3,
  itm_entenaii_horse_4,
  itm_entenaii_horse_5,
  ],
  attr_lvl_35,wp_6_m,knows_battle_6,man_face_middle_1, man_face_older_2],

#Vehicles
["f1_car_mechanic","Automobile_IMC","Automobile_IMCs",
  tf_has_body|tf_guarantee_ranged,0,0,fac_kingdom_1,
  [
  itm_pistol_ammo_pw,
  itm_empire_revolver,
  
  itm_bowie_knife,
  itm_bayonet_2,
  itm_spanner,
  itm_crowbar,
  itm_wrench,
  itm_monkeywrench,
  itm_screwdriver,
  itm_screwdriver2,
  itm_entrenching_tool,

  itm_entenaii_uniform_levy,
  ],
  attr_lvl_25,wp_2_r,knows_battle_2,man_face_young_1, man_face_old_2],
["f1_chopper_mechanic","Aeromobile_IMC","Aeromobile_IMCs",
  tf_has_body|tf_guarantee_ranged,0,0,fac_kingdom_1,
  [
  itm_pistol_ammo_pw,
  itm_empire_revolver,
  
  itm_bowie_knife,
  itm_bayonet_2,
  itm_spanner,
  itm_crowbar,
  itm_wrench,
  itm_monkeywrench,
  itm_screwdriver,
  itm_screwdriver2,
  itm_entrenching_tool,

  itm_entenaii_uniform_levy,
  ],
  attr_lvl_25,wp_2_r,knows_battle_2,man_face_young_1, man_face_old_2],

#Guards
["f1_guard","Entenaii Prison Guard","Entenaii Prison Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,

  itm_entenaii_uniform_guard,

  itm_entenaii_helmet_5,
  itm_entenaii_helmet_5_open,

  itm_entenaii_gloves,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],
["f1_castle_guard","Entenaii Guard","Entenaii Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
  [
  itm_buckshot_ammo,
  itm_buckshot_ammo,
  itm_entenaii_shotgun,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_bowie_knife,
  itm_bayonet_2,
  itm_trooper_sword,

  itm_entenaii_uniform_guard,

  itm_entenaii_helmet_3_full,

  itm_entenaii_demi_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],
["f1_hall_guard","Entenaii Imperial Guard","Entenaii Imperial Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
  [
  itm_pistol_ammo,
  itm_smg_sten,

  itm_ironclub,
  itm_trooper_sword,

  itm_entenaii_uniform_parade,
  
  itm_entenaii_helmet_5,

  itm_entenaii_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],

#Terror
["f1_terror","Entenaii Automaton","Entenaii Automatons",
  tf_droid|tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
  [
  itm_mg_ammo_pw,
  itm_mg_ammo_pw,
  itm_entenaii_empire_lmg,

  itm_trench_club_4,

  itm_entenaii_automaton_body,
  
  itm_entenaii_automaton_head,

  itm_automaton_hands,
  ],
  attr_terror, wp_5_r, knows_battle_5,x_face, x_face],

#Mech
["f1_mech","Entenaii_Tyrant-Class_Walker","Entenaii_Tyrant-Class_Walkers",
  tf_man_high|tf_guarantee_all|tf_allways_fall_dead|tf_no_capture_alive,no_scene,0,fac_kingdom_1,
  [
  itm_tech_parts,
  itm_b2series_attack,
  itm_invisi_head,
  itm_invisi_gloves,
  itm_invisi_boots,
  itm_mech_walker_1_body,
  itm_cannon_tyrant,
  ],
  attr_tank, wp_5_m, knows_battle_5,x_face, x_face],
["f1_mech_emperor","Entenaii_Imperial_Escort_Walker","Entenaii_Imperial_Escort_Walkers",
  tf_man_high|tf_guarantee_all|tf_allways_fall_dead|tf_no_capture_alive,no_scene,0,fac_kingdom_1,
  [
  itm_tech_parts,
  itm_b2series_attack,
  itm_invisi_head,
  itm_invisi_gloves,
  itm_invisi_boots,
  itm_mech_walker_imperial_body,
  itm_cannon_tyrant,
  ],
  attr_tank, wp_5_m, knows_battle_5,x_face, x_face],

## Entenaii Dominion ##
["f2_tier_0","Entenaii Dominion Levy","Entenaii Dominion Levies",
  tf_has_body,0,0,fac_kingdom_2,
  [
  itm_throwing_knives,
  itm_darts,
  
  itm_knife,
  itm_bayonet_1,
  itm_bowie_knife,
  itm_kukri_rusty,
  itm_kukri_old,
  itm_hatchet,
  itm_club,
  itm_2by4nails,
  itm_entrenching_tool,
  
  itm_straw_hat_1,
  itm_straw_hat_2,
  itm_dominion_civ_hat_1,
  
  itm_dominion_uniform_levy,
  ],
  attr_lvl_5,wp_start,knows_battle_1,man_face_younger_1, man_face_middle_2],
["f2_tier_1","Entenaii Dominion Recruit","Entenaii Dominion Recruits",
  tf_has_body,0,0,fac_kingdom_2,
  [
  itm_pistol_ammo,
  itm_dominion_revolver,
  
  itm_knife,
  itm_bayonet_1,
  itm_bowie_knife,
  itm_kukri_rusty,
  itm_kukri_old,
  itm_hatchet,
  itm_club,
  itm_entrenching_tool,
  
  itm_dominion_uniform_recruit,
  
  itm_dominion_recruit_helmet,

  itm_dominion_gloves,
  ],
  attr_lvl_15,wp_2_m,knows_battle_2,man_face_younger_1, man_face_middle_2],
["f2_tier_2","Entenaii Dominion Yeoman","Entenaii Dominion Yeomen",
  tf_has_body|tf_guarantee_ranged,0,0,fac_kingdom_2,
  [
  itm_rifle_ammo,
  itm_dominion_bolt_action_rifle,

  itm_bayonet_1,
  itm_hand_axe,
  itm_bowie_knife,
  itm_trench_knife,
  itm_trench_knife_1,
  itm_entrenching_tool,

  itm_dominion_uniform_yeoman,

  itm_dominion_infantry_helmet,

  itm_dominion_gloves,
  ],
  attr_lvl_20,wp_3_m,knows_battle_3,man_face_young_1, man_face_old_2],
["f2_tier_3","Entenaii Dominion Infantry","Entenaii Dominion Infantries",
  tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_2,
  [
  itm_rifle_ammo,
  itm_dominion_bolt_action_rifle_bayonet,
  itm_dominion_bolt_action_rifle,

  itm_trooper_sword,
  itm_bayonet_1,
  itm_trench_knife_1,
  itm_hand_axe,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_entrenching_tool,

  itm_dominion_uniform_infantry,

  itm_dominion_infantry_helmet,

  itm_dominion_gloves,
  ],
  attr_lvl_25,wp_4_m,knows_battle_4,man_face_young_1, man_face_old_2],
["f2_tier_4","Entenaii Dominion Veteran","Entenaii Dominion Veterans",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
  [
  itm_rifle_ammo,
  itm_dominion_bolt_action_rifle_bayonet,
  
  itm_hand_axe,
  itm_hammer_big,
  itm_bastard_club_1,
  itm_bayonet_1,
  itm_entrenching_tool,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,

  itm_dominion_uniform_veteran,
  
  itm_dominion_sergeant_helmet,

  itm_dominion_gloves,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,man_face_middle_1, man_face_old_2],
["f2_tier_5","Entenaii Dominion Vanguard","Entenaii Dominion Vanguards",
  tf_mounted|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_2,
  [
  itm_rifle_ammo,
  itm_dominion_assault_rifle,

  itm_trooper_sword,
  itm_hand_axe,
  itm_hammer_big,
  itm_sledgehammer_small,
  itm_sledgehammer,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_entrenching_tool,

  itm_dominion_armour,

  itm_dominion_sergeant_helmet,

  itm_dominion_gauntlets,
  
  itm_ammo_belt_2,
  ],
  attr_lvl_35,wp_6_m,knows_battle_6,man_face_middle_1, man_face_older_2],
["f2_fanatic","Entenaii Dominion Fanatic","Entenaii Dominion Fanatics",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
  [
  itm_flameshot_ammo,
  
  itm_dominion_shotgun,
  
  itm_grenade_molotov,
  itm_grenade_molotov,
  
  itm_torch,

  itm_dominion_uniform_fanatic,
  
  itm_dominion_fanatic_coif_a,
  itm_dominion_fanatic_coif_b,

  itm_dominion_gloves,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,man_face_middle_1, man_face_old_2],
["f2_flamer","Entenaii Dominion Fanatic Officer","Entenaii Dominion Fanatic Officers",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet,0,0,fac_kingdom_2,
  [
  itm_flameammo,
  itm_flamethrower,
  
  itm_torch,
  itm_fanatic_staff,

  itm_dominion_uniform_fanatic_officer,
  itm_dominion_uniform_fanatic_officer_2,
  
  itm_dominion_fanatic_officer_coif,

  itm_entenaii_gloves,
  
  itm_flamethrower_backpack,
  ],
  attr_lvl_35,wp_5_m,knows_battle_5,man_face_middle_1, man_face_old_2],

#Cavalry
["f2_rider","Entenaii Dominion Rough-rider","Entenaii Dominion Rough-riders",
  tf_has_body|tf_has_hand|tf_has_head|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_2,
  [
  itm_rifle_ammo,
  itm_dominion_bolt_action_carbine,
  
  itm_grenade_molotov,

  itm_light_cav_sword,
  itm_largeclub,

  itm_dominion_uniform_rough_rider,
  
  itm_dominion_cavalry_helmet,

  itm_dominion_demi_gauntlets,

  itm_entenaii_horse_1,
  itm_entenaii_horse_2,
  itm_entenaii_horse_3,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,man_face_middle_1, man_face_old_2],

#Vehicles
["f2_car_mechanic","Entenaii Dominion Automobile Mechanic","Entenaii Dominion Automobile Mechanics",
  tf_has_body|tf_guarantee_ranged,0,0,fac_kingdom_2,
  [
  itm_pistol_ammo,
  itm_dominion_revolver,

  itm_bowie_knife,
  itm_bayonet_1,
  itm_spanner,
  itm_crowbar,
  itm_wrench,
  itm_monkeywrench,
  itm_screwdriver,
  itm_screwdriver2,
  itm_entrenching_tool,

  itm_dominion_uniform_yeoman,

  itm_dominion_infantry_helmet,

  itm_dominion_gloves,
  ],
  attr_lvl_25,wp_2_r,knows_battle_2,man_face_young_1, man_face_old_2],

#Guards
["f2_guard","Entenaii Dominion Prison Guard","Entenaii Dominion Prison Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_hammer_big,
  itm_sledgehammer_small,

  itm_dominion_uniform_prison_guard,

  itm_dominion_guard_helmet,

  itm_dominion_demi_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],
["f2_castle_guard","Entenaii Dominion Guard","Entenaii Dominion Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
  [
  itm_rifle_ammo,
  itm_dominion_bolt_action_rifle_bayonet,

  itm_trooper_sword,
  itm_bayonet_1,
  itm_hand_axe,
  itm_hammer_big,
  itm_sledgehammer_small,

  itm_dominion_uniform_guard,
  
  itm_dominion_fanatic_noble_coif_a,
  itm_dominion_fanatic_noble_coif_c,

  itm_dominion_demi_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],
["f2_hall_guard","Entenaii Dominion Viceregal Guard","Entenaii Dominion Viceregal Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
  [
  itm_mg_ammo,
  itm_entenaii_dominion_lmg,

  itm_trooper_sword,
  itm_bayonet_1,
  itm_fanatic_staff,

  itm_dominion_uniform_viceregal_guard,
  
  itm_dominion_hall_guard_helmet,

  itm_entenaii_gauntlets,
  
  itm_cloak_fanatic,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],

#Terror
["f2_terror","Entenaii Dominion Condemned","Entenaii Dominion Condemned",
  tf_infected|tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
  [
  itm_throwing_chains,
  itm_throwing_chains,
  itm_throwing_chains,
  
  itm_long_fighting_axe,
  
  itm_dominion_condemned_body,
    
  itm_dominion_demi_gauntlets,
  ],
  attr_terror, wp_5_m, knows_battle_5,x_face, x_face],

#Mechs
["f2_mech","Entenaii_Dominion_Tyrant-Class_Walker","Entenaii_Dominion_Tyrant-Class_Walkers",
  tf_man_high|tf_guarantee_all|tf_allways_fall_dead|tf_no_capture_alive,no_scene,0,fac_kingdom_2,
  [
  itm_tech_parts,
  itm_b2series_attack,
  itm_invisi_head,
  itm_invisi_gloves,
  itm_invisi_boots,
  itm_mech_walker_3_body,
  itm_cannon_tyrant,
  ],
  attr_tank, wp_5_m, knows_battle_5,x_face, x_face],

## Kingdom of Galvae ##
["f3_tier_0","Galvae_Nobach","Galvae_Nobachs",
  tf_has_body|tf_guarantee_helmet,0,0,fac_kingdom_3,
  [
  itm_arrows,
  itm_hunting_bow,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_shepherds_crook,

  itm_galvae_uniform_levy,
  
  itm_galvae_mask_1,
  ],
  attr_lvl_5,wp_start,knows_battle_1,galvae_face_younger_1, galvae_face_middle_1],
["f3_tier_1","Galvae_Astaich","Galvae_Astaichs",
  tf_has_body|tf_guarantee_helmet,0,0,fac_kingdom_3,
  [
  itm_pistol_ammo,
  itm_galvae_revolver,
  itm_arrows,
  itm_short_bow,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_shepherds_crook,
  itm_bayonet_2,
  itm_entrenching_tool,

  itm_galvae_uniform_regular,
  
  itm_galvae_mask_1,

  itm_galvae_gloves,
  ],
  attr_lvl_15,wp_2_m,knows_battle_2,galvae_face_younger_1, galvae_face_middle_1],
["f3_tier_2","Galvae_Haighda","Galvae_Haighdas",
  tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_3,
  [
  itm_rifle_ammo,
  itm_galvae_bolt_action_rifle,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_bastard_club_1,
  itm_bayonet_2,
  itm_entrenching_tool,

  itm_galvae_uniform_sergeant,
  
  itm_galvae_masked_hood_1,
  itm_galvae_masked_hood_2,
  itm_galvae_masked_hood_3,
  itm_galvae_masked_hood_4,
  itm_galvae_masked_hood_6,

  itm_galvae_gloves,
  
  itm_cloak_9,
  ],
  attr_lvl_20,wp_3_m,knows_battle_3,galvae_face_young_1, galvae_face_old_1],
["f3_tier_3","Galvae_Gean_Haighda","Galvae_Gean_Haighdas",
  tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_boots,0,0,fac_kingdom_3,
  [
  itm_rifle_ammo,
  itm_galvae_bolt_action_rifle_bayonet,
  itm_galvae_bolt_action_rifle,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_bastard_club_1,
  itm_trooper_sword,
  itm_bayonet_2,

  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,

  itm_galvae_uniform_raider,

  itm_galvae_mask_1,
  itm_galvae_masked_hood_1,
  itm_galvae_masked_hood_2,
  itm_galvae_masked_hood_3,
  itm_galvae_masked_hood_4,
  itm_galvae_masked_hood_6,

  itm_galvae_gloves,
  
  itm_cloak_8,
  ],
  attr_lvl_25,wp_4_m,knows_battle_4,galvae_face_young_1, galvae_face_old_1],
["f3_tier_4","Galvae_Feannradai","Galvae_Feannradais",
  tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots,0,0,fac_kingdom_3,
  [
  itm_rifle_ammo,
  itm_galvae_bolt_action_rifle_bayonet,
  itm_galvae_assault_rifle,

  itm_ornate_seax,
  itm_bastard_club_1,
  itm_trooper_sword,
  itm_bayonet_2,

  itm_galvae_uniform_officer,
  
  itm_galvae_masked_metal_hood_1,
  itm_galvae_masked_metal_hood_2,
  itm_galvae_masked_metal_hood_3,
  itm_galvae_masked_metal_hood_4,
  itm_galvae_masked_metal_hood_5,
  itm_galvae_masked_metal_hood_6,

  itm_galvae_gloves,
  
  itm_cloak_7,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,galvae_face_middle_1, galvae_face_old_1],
["f3_tier_5","Galvae_Fear-deon","Galvae_Fear-deons",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots,0,0,fac_kingdom_3,	#why had tf_mounted|?
  [
  itm_mg_ammo,
  itm_galvae_lmg,
  
  itm_ornate_seax,
  itm_trooper_sword,
  itm_bastard_club_1,
  itm_bayonet_2,

  itm_galvae_armour,

  itm_galvae_mask_helmet,

  itm_galvae_gauntlets,
  
  itm_ammo_belt_4,
  ],
  attr_lvl_35,wp_6_m,knows_battle_6,galvae_face_middle_1, galvae_face_old_1],
["f3_infantry","Galvae_Ruraidh","Galvae_Ruraidhs",
  tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_kingdom_3,
  [
  itm_ornate_seax,
  itm_scottish_claymore,

  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,

  itm_galvae_armour,

  itm_galvae_mask_knight,
  
  itm_galvae_gauntlets,
  
  itm_cloak_4,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5|knows_shield_10,galvae_face_middle_1, galvae_face_old_1],

#Cavalry
["f3_rider","Galvae_Skuoa","Galvae_Skuoas",
  tf_guarantee_ranged|tf_has_body|tf_has_hand|tf_has_head|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
  [
  itm_arrows,
  itm_arrows,
  itm_rider_bow,
  itm_recurve_bow,

  itm_light_cav_sword,
  itm_ornate_seax,

  itm_galvae_armour_cavalry,
  
  itm_galvae_masked_hood_1,
  itm_galvae_masked_hood_2,
  itm_galvae_masked_hood_3,
  itm_galvae_masked_hood_4,
  itm_galvae_masked_hood_6,

  itm_galvae_demi_gauntlets,
  
  itm_cloak_6,
  
  itm_galvae_horse_1,
  itm_galvae_horse_2,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,galvae_face_middle_1, galvae_face_old_1],
["f3_vet_rider","Galvae_Dragen","Galvae_Dragens",
  tf_guarantee_ranged|tf_has_body|tf_has_hand|tf_has_head|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
  [
  itm_rifle_ammo,
  itm_galvae_bolt_action_carbine,

  itm_light_cav_sword,
  itm_ornate_seax,

  itm_galvae_armour_cavalry,
  
  itm_galvae_mask_knight,

  itm_galvae_demi_gauntlets,
  
  itm_cloak_10,
  
  itm_galvae_horse_1,
  itm_galvae_horse_2,
  ],
  attr_lvl_35,wp_6_m,knows_battle_6,galvae_face_middle_1, galvae_face_old_1],

#Guards
["f3_guard","Galvae_Danag_Guard","Galvae_Danag_Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots,0,0,fac_kingdom_3,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_ornate_seax,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_bastard_club_1,
  itm_trooper_sword,
  itm_bayonet_2,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,

  itm_galvae_uniform_guard,

  itm_galvae_demi_gauntlets,
  
  itm_galvae_mask_metal_2,
  
  itm_cloak_3,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,galvae_face_middle_1, galvae_face_old_1],
["f3_castle_guard","Galvae_Brochs_Guard","Galvae_Brochs_Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots,0,0,fac_kingdom_3,
  [
  itm_rifle_ammo,
  itm_galvae_bolt_action_rifle_bayonet,

  itm_ornate_seax,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_bastard_club_1,
  itm_trooper_sword,
  itm_bayonet_2,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,

  itm_galvae_uniform_guard,

  itm_galvae_demi_gauntlets,
  
  itm_galvae_masked_metal_hood_1,
  itm_galvae_masked_metal_hood_2,
  itm_galvae_masked_metal_hood_3,
  itm_galvae_masked_metal_hood_4,
  itm_galvae_masked_metal_hood_5,
  itm_galvae_masked_metal_hood_6,
  
  itm_cloak_2,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,galvae_face_middle_1, galvae_face_old_1],
["f3_hall_guard","Galvae_Sceath_Guard","Galvae_Sceath_Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_boots,0,0,fac_kingdom_3,
  [
  itm_rifle_ammo,
  itm_galvae_assault_rifle,

  itm_ornate_seax,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_bastard_club_1,
  itm_trooper_sword,
  itm_bayonet_2,
  
  itm_galvae_shield_1,
  itm_galvae_shield_2,
  itm_galvae_shield_3,
  itm_galvae_shield_4,
  itm_galvae_shield_5,
  itm_galvae_shield_6,
  itm_galvae_shield_7,
  itm_galvae_shield_8,
  itm_galvae_shield_9,

  itm_galvae_uniform_officer_cuirass,

  itm_galvae_mask_helmet,

  itm_galvae_gauntlets,
  
  itm_cloak_1,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,galvae_face_middle_1, galvae_face_old_1],

#Terror
["f3_terror","Galvae_Os-si", "Galvae_Os-si",
  tf_woman|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_boots,0,0,fac_kingdom_3,
  [
  itm_ossi_arrows,
  itm_ossi_bow,

  itm_ossi_blade,
  itm_ossi_blade_long,

  itm_galvae_ossi,
  itm_invisi_gloves,
  itm_invisi_boots,
  itm_invisi_head,
  ],
  attr_terror, wp_6_m, knows_battle_6|knows_power_draw_10|knows_athletics_10,woman_face_1, woman_face_2],

## Molvat-Berchav Union ##
["f4_tier_0","Union Enlisted Serf","Union Enlisted Serfs",
  tf_has_body,0,0,fac_kingdom_4,
  [
  itm_throwing_knives,
  itm_darts,
  
  itm_sharpened_stick,
  itm_bayonet_3,
  itm_entrenching_tool,
  
  itm_union_uniform_levy,
  
  itm_bandit_hood_blk,
  itm_bandit_hood_blu,
  itm_bandit_hood_grn,
  itm_bandit_hood_red,
  itm_bandit_hood_wht,
  itm_bandit_hood_blk_scarf,
  itm_bandit_hood_blu_scarf,
  itm_bandit_hood_grn_scarf,
  itm_bandit_hood_red_scarf,
  itm_bandit_hood_wht_scarf,
  itm_union_coif,
  ],
  attr_lvl_5,wp_start,knows_battle_1,0x000000000001d000000080000000000000000000001c00000000000000000000, 0x0000000ffe02c00079e7ffffffefffff00000000001fff380000000000000000],
["f4_tier_1","Union Recruit","Union Recruits",
  tf_has_body|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_4,
  [
  itm_pistol_ammo,
  itm_molvat_revolver,

  itm_sharpened_stick,
  itm_bayonet_3,
  itm_entrenching_tool,

  itm_union_uniform_regular,
  
  itm_union_coif,
  ],
  attr_lvl_15,wp_2_m,knows_battle_2,0x000000000001d000000080000000000000000000001c00000000000000000000, 0x0000000ffe02c00079e7ffffffefffff00000000001fff380000000000000000],
["f4_tier_2","Union Yeoman","Union Yeomen",
  tf_has_body|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_4,
  [
  itm_rifle_ammo,
  itm_molvat_bolt_action_rifle,
  itm_berchav_bolt_action_rifle,

  itm_shortened_spear,
  itm_bayonet_3,
  itm_entrenching_tool,

  itm_tc_shield_1,
  itm_tc_shield_2,
  itm_tc_shield_5,

  itm_union_uniform_yeoman,

  itm_union_coif,

  itm_union_gloves,
  ],
  attr_lvl_20,wp_3_r,knows_battle_3,0x000000000001d000000080000000000000000000001c00000000000000000000, 0x0000000ffe02c00079e7ffffffefffff00000000001fff380000000000000000],
["f4_tier_3","Union Skirmisher","Union Skirmisher",
  tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_4,
  [
  itm_rifle_ammo,
  itm_molvat_bolt_action_rifle_bayonet,
  itm_molvat_bolt_action_rifle,
  itm_berchav_bolt_action_rifle_bayonet,
  itm_berchav_bolt_action_rifle,

  itm_shortened_spear,
  itm_bayonet_3,

  itm_tc_shield_1,
  itm_tc_shield_2,
  itm_tc_shield_5,

  itm_union_uniform_light_infantry,

  itm_union_helmet,
  
  itm_union_gloves,
  
  itm_pony,
  ],
  attr_lvl_25,wp_4_r,knows_battle_4,0x000000000001d000000080000000000000000000001c00000000000000000000, 0x0000000ffe02c00079e7ffffffefffff00000000001fff380000000000000000],
["f4_tier_3b","Union Rifleman","Union Riflemen",
  tf_guarantee_ranged|tf_guarantee_helmet|tf_has_body,0,0,fac_kingdom_4,
  [
  itm_rifle_ammo,
  itm_molvat_bolt_action_rifle_bayonet,
  itm_berchav_bolt_action_rifle_bayonet,
  
  itm_sovnya,
  itm_bayonet_3,

  itm_union_uniform_rifleman,

  itm_union_helmet,
  
  itm_union_gloves,
  ],
  attr_lvl_25,wp_4_r,knows_battle_4,0x000000000001d000000080000000000000000000001c00000000000000000000, 0x0000000ffe02c00079e7ffffffefffff00000000001fff380000000000000000],
["f4_tier_4","Union Veteran","Union Veterans",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
  [
  itm_rifle_ammo,
  itm_molvat_semi_rifle,

  itm_sovnya,
  itm_shashka,
  itm_bayonet_3,
  itm_spear,
  
  itm_union_uniform_raider,
  
  itm_union_helmet_raider,

  itm_union_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,0x000000000001d000000080000000000000000000001c00000000000000000000, 0x0000000ffe02c00079e7ffffffefffff00000000001fff380000000000000000],
["f4_sniper","Union_Tundra_Sniper","Union_Tundra_Snipers",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
  [
  itm_large_caliber_ammo,
  itm_berchav_sniper,

  itm_shashka,
  itm_bayonet_3,
  itm_spear,
  
  itm_union_uniform_sniper,
  
  itm_union_hood_sniper,

  itm_union_mittens,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,0x000000000001d000000080000000000000000000001c00000000000000000000, 0x0000000ffe02c00079e7ffffffefffff00000000001fff380000000000000000],
["f4_tier_5","Union Sergeant","Union Sergeants",
  tf_mounted|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_4,
  [
  itm_rifle_ammo,
  itm_molvat_assault_rifle,
  itm_berchav_assault_rifle,

  itm_shashka,
  itm_bayonet_3,
  itm_spear,

  itm_union_uniform_sergeant,

  itm_union_helmet_sergeant,

  itm_union_gloves,
  ],
  attr_lvl_35,wp_6_r,knows_battle_6,0x000000000001d000000080000000000000000000001c00000000000000000000, 0x0000000ffe02c00079e7ffffffefffff00000000001fff380000000000000000],
["f4_flamer","Union Engineer","Union Engineers",
  tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_gloves|tf_has_body,0,0,fac_kingdom_4,
  [
  itm_flameammo,
  itm_flamethrower_union,
  
  itm_ravensbeak,
  
  itm_union_armour,

  itm_gas_mask_brown_01,

  itm_union_gauntlets,
  
  itm_flamethrower_backpack_union,
  ],
  attr_lvl_35,wp_6_r,knows_battle_6,0x000000000001d000000080000000000000000000001c00000000000000000000, 0x0000000ffe02c00079e7ffffffefffff00000000001fff380000000000000000],
["f4_tier_6","Union Gunner","Union Gunners",
  tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_4,
  [
  itm_mg_ammo,
  itm_molvat_lmg,

  itm_sovnya_1,
  itm_bayonet_3,

  itm_union_uniform_sergeant,

  itm_union_helmet_officer,

  itm_union_gloves,
  ],
  attr_lvl_40,wp_6_r,knows_battle_6,0x000000000001d000000080000000000000000000001c00000000000000000000, 0x0000000ffe02c00079e7ffffffefffff00000000001fff380000000000000000],

#Cavalry
["f4_tier_4_cavalry","Union Young Culsar","Union Young Culsars",
  tf_guarantee_ranged|tf_guarantee_helmet|tf_has_body|tf_has_head|tf_guarantee_horse,0,0,fac_kingdom_4,
  [
  itm_pistol_ammo,
  itm_molvat_revolver,

  itm_shashka,
  itm_sovnya,

  itm_union_uniform_cavalry,

  itm_union_young_culsar_helmet_1,
  itm_union_young_culsar_helmet_2,

  itm_union_gloves,

  itm_culsar_horse_1,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,brotherhood_face_younger_1, brotherhood_face_young_1],
["f4_tier_5_cavalry","Union Culsar","Union Culsars",
  tf_guarantee_ranged|tf_guarantee_helmet|tf_has_body|tf_has_head|tf_guarantee_horse,0,0,fac_kingdom_4,
  [
  itm_rifle_ammo,
  itm_molvat_bolt_action_carbine,

  itm_lance1,
  itm_shashka,

  itm_union_uniform_cavalry_cuirass,

  itm_union_culsar_helmet_1,
  itm_union_culsar_helmet_2,
  itm_union_culsar_helmet_3,
  itm_union_culsar_helmet_4,

  itm_union_demi_gauntlets,

  itm_culsar_horse_2,
  ],
  attr_lvl_35,wp_6_r,knows_battle_5,brotherhood_face_young_1, brotherhood_face_old_1],
["f4_tier_6_cavalry","Union Veteran Culsar","Union Veteran Culsars",
  tf_guarantee_ranged|tf_guarantee_helmet|tf_has_body|tf_has_head|tf_guarantee_horse,0,0,fac_kingdom_4,
  [
  itm_rifle_ammo_pw,
  itm_molvat_assault_rifle,
  itm_berchav_assault_rifle,

  itm_lance1,
  itm_shashka,

  itm_union_uniform_cavalry_cuirass,

  itm_union_veteran_culsar_helmet_1,

  itm_union_gauntlets,

  itm_culsar_horse_3,
  ],
  attr_lvl_40,wp_6_r,knows_battle_6,brotherhood_face_middle_1, brotherhood_face_older_1],

#Guards
["f4_guard","Union Safety Guard","Union Safety Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_staff,

  itm_union_uniform_guard,

  itm_union_helmet_sergeant,

  itm_union_demi_gauntlets,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,0x000000000001d000000080000000000000000000001c00000000000000000000, 0x0000000ffe02c00079e7ffffffefffff00000000001fff380000000000000000],
["f4_castle_guard","Union Peace Guard","Union Peace Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
  [
  itm_pistol_ammo,
  itm_molvat_revolver,

  itm_sovnya,
  itm_shashka,
  itm_bayonet_3,
  itm_spear,

  itm_tc_shield_1,
  itm_tc_shield_2,
  itm_tc_shield_5,

  itm_union_uniform_guard,

  itm_union_young_culsar_helmet_1,

  itm_union_demi_gauntlets,
  ],
  attr_lvl_35,wp_5_m,knows_battle_5,0x000000000001d000000080000000000000000000001c00000000000000000000, 0x0000000ffe02c00079e7ffffffefffff00000000001fff380000000000000000],
["f4_hall_guard","Union Brotherhood Guard","Brotherhood Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
  [
  itm_pistol_ammo_pw,
  itm_molvat_smg,

  itm_shashka,
  itm_sovnya_1,
  itm_bayonet_3,

  itm_union_armour_brotherhood,

  itm_union_helmet_brotherhood,

  itm_union_gauntlets,
  ],
  attr_lvl_40,wp_6_m,knows_battle_6,brotherhood_face_middle_1, brotherhood_face_older_1],

#Unique
["f4_marine","Union Marine","Union Marines",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
  [
  itm_rifle_ammo,
  itm_molvat_bolt_action_carbine,

  itm_shashka,
  itm_bayonet_3,
  
  itm_union_uniform_marine,

  itm_union_gloves,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,0x000000000001d000000080000000000000000000001c00000000000000000000, 0x0000000ffe02c00079e7ffffffefffff00000000001fff380000000000000000],
["f4_marine_armoured","Union Armoured Marine","Union Armoured Marines",
  tf_mounted|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_4,
  [
  itm_rifle_ammo,
  itm_molvat_bolt_action_carbine,

  itm_shashka,
  itm_bayonet_3,

  itm_union_uniform_marine_cuirass,

  itm_union_gauntlets,
  ],
  attr_lvl_35,wp_6_r,knows_battle_6,0x000000000001d000000080000000000000000000001c00000000000000000000, 0x0000000ffe02c00079e7ffffffefffff00000000001fff380000000000000000],

#Terror
["f4_terror","Union Ravga","Union Ravga",
  tf_skeleton|tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
  [
  itm_pistol_ammo,
  itm_molvat_smg,

  itm_sovnya_1,
  itm_bayonet_3,
  itm_shashka,

  itm_tc_shield_1,
  itm_tc_shield_2,
  itm_tc_shield_5,

  itm_union_ravga_armour,
  
  itm_ravga_gauntlets,
  
  itm_ravga_horse,
  ],
  attr_terror, wp_5_m, knows_battle_5,x_face, x_face],

## Vitzland Territories ##
["f5_tier_0","Vitzland Levy","Vitzland Levies",
  tf_has_body,0,0,fac_kingdom_5,
  [
  itm_butchering_knife,
  itm_bayonet_4,
  itm_entrenching_tool,

  itm_wooden_shield,
  itm_wooden_shield_2,
  itm_wood_shield,

  itm_vitzland_uniform_levy,
  ],
  attr_lvl_5,wp_start,knows_battle_1,man_face_younger_1, man_face_middle_2],
["f5_tier_1","Vitzland Private","Vitzland Privates",
  tf_has_body,0,0,fac_kingdom_5,
  [
  itm_pistol_ammo,
  itm_vitzland_pistol,

  itm_butchering_knife,
  itm_bayonet_4,
  itm_entrenching_tool,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,

  itm_wooden_shield,
  itm_wooden_shield_2,
  itm_wood_shield,

  itm_vitzland_uniform_regular,

  itm_vitzland_recruit_helmet,

  itm_vitzland_gloves,
  ],
  attr_lvl_15,wp_2_m,knows_battle_2,man_face_younger_1, man_face_middle_2],
["f5_tier_2","Vitzland Private 2nd Class","Vitzland Privates 2nd Class",
  tf_has_body|tf_guarantee_ranged,0,0,fac_kingdom_5,
  [
  itm_rifle_ammo,
  itm_vitzland_bolt_action_rifle,

  itm_hand_axe,
  itm_butchering_knife,
  itm_bayonet_4,
  itm_entrenching_tool,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,

  itm_wood_shield,
  itm_round_shield_leather,

  (itm_vitzland_uniform_regular, imod_thick),

  itm_vitzland_helmet,
  itm_vitzland_helmet,
  itm_vitzland_helmet,
  itm_vitzland_helmet_gasmask,

  itm_vitzland_gloves,
  ],
  attr_lvl_20,wp_3_m,knows_battle_3,man_face_young_1, man_face_old_2],
["f5_tier_3","Vitzland Sergeant","Vitzland Sergeants",
  tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_5,
  [
  itm_pistol_ammo,
  itm_vitzland_smg,

  itm_butchering_knife,
  itm_bayonet_4,
  itm_big_spiked_club,
  itm_one_handed_war_axe_a,

  itm_round_shield_leather,
  itm_round_shield,

  itm_vitzland_uniform_sergeant,
  
  itm_vitzland_salet_1,

  itm_vitzland_gloves,
  ],
  attr_lvl_25,wp_4_m,knows_battle_4,man_face_young_1, man_face_old_2],
["f5_tier_4","Vitzland Trench Raider","Vitzland Trench Raiders",
  tf_guarantee_ranged|tf_guarantee_all,0,0,fac_kingdom_5,
  [
  itm_buckshot_ammo,
  itm_vitzland_sawnoff,

  itm_spiked_club,
  itm_bastard_club_1,
  itm_sledgehammer_small,
  itm_one_handed_war_axe_a,
  itm_battle_axe,
  itm_blucher,
  
  itm_round_shield,

  itm_vitzland_uniform_raider,

  itm_vitzland_salet_2,

  itm_vitzland_gloves,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_young_1, man_face_old_2],
["f5_tier_5","Vitzland Armoured Trench Raider","Vitzland Armoured Trench Raiders",
  tf_mounted|tf_guarantee_all|tf_guarantee_ranged,0,0,fac_kingdom_5,
  [
  itm_buckshot_ammo_pw,
  itm_vitzland_shotgun,

  itm_flamberge,

  itm_vitzland_armour,

  itm_vitzland_salet_heavy,
  itm_vitzland_salet_heavy_2,
  itm_vitzland_salet_1_gasmask,

  itm_vitzland_gauntlets,
  ],
  attr_lvl_35,wp_6_m,knows_battle_6,man_face_middle_1, man_face_older_2],
["f5_tier_6","Vitzland Bunker Buster","Vitzland Bunker Busters",
  tf_mounted|tf_guarantee_all|tf_guarantee_ranged,0,0,fac_kingdom_5,
  [
  itm_grenade_stick_bundle,
  
  itm_buckshot_ammo_pw,
  itm_vitzland_sawnoff,

  itm_sledgehammer,

  itm_vitzland_armour,

  itm_vitzland_salet_heavy,
  itm_vitzland_salet_heavy_2,
  itm_vitzland_salet_1_gasmask,

  itm_vitzland_gauntlets,
  ],
  attr_lvl_40,wp_6_m,knows_battle_6,man_face_middle_1, man_face_older_2],
["f5_flamer","Vitzland Engineer","Vitzland Engineers",
  tf_guarantee_all|tf_has_body,0,0,fac_kingdom_5,
  [
  itm_flameammo,
  itm_flamethrower,

  itm_butchering_knife,
  itm_bayonet_4,
  itm_kukri_old,
  itm_metal_blade,
  itm_long_spiked_club,
  itm_hand_axe,
  itm_lumberjack_axe,
  itm_staff,
  itm_blucher,

  itm_vitzland_armour,
  
  itm_gas_mask_ca_90,
  itm_vitzland_helmet_gasmask,
  itm_vitzland_salet_1_gasmask,
  itm_vitzland_salet_3_gasmask,

  itm_vitzland_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_young_1, man_face_middle_2],
["f5_gunner","Vitzland Machine Gunner","Vitzland Machine Gunners",
  tf_guarantee_all|tf_has_body,0,0,fac_kingdom_5,
  [
  itm_mg_ammo,
  itm_vitzland_lmg,

  itm_knife,
  itm_kukri_old,
  itm_metal_blade,
  itm_butchering_knife,
  itm_bayonet_4,
  itm_hand_axe,
  itm_blucher,

  itm_vitzland_uniform_gunner,
  
  itm_vitzland_salet_2,

  itm_vitzland_gloves,
  
  itm_ammo_belt_1,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_young_1, man_face_middle_2],

#Cavalry
["f5_rider","Vitzland Vytr","Vitzland Vytrs",
  tf_guarantee_ranged|tf_guarantee_all|tf_guarantee_horse,0,0,fac_kingdom_5,
  [
  itm_pistol_ammo,
  itm_vitzland_pistol,

  itm_blucher,
  
  itm_round_shield_leather,

  itm_vitzland_uniform_cavalry_cuirass,

  itm_vitzland_salet_3,

  itm_vitzland_demi_gauntlets,

  itm_vitzland_horse_1,
  itm_vitzland_horse_2,
  ],
  attr_lvl_25,wp_4_m,knows_battle_4,man_face_young_1, man_face_old_2],
["f5_rider_vet","Vitzland Sundr Vytr","Vitzland Sundr Vytrs",
  tf_guarantee_ranged|tf_guarantee_all|tf_guarantee_horse,0,0,fac_kingdom_5,
  [
  itm_rifle_ammo,
  itm_vitzland_bolt_action_carbine,

  itm_blucher,
  
  itm_round_shield,

  itm_vitzland_armour_cavalry,
  
  itm_vitzland_salet_3,
  itm_vitzland_salet_1_gasmask,

  itm_vitzland_gauntlets,

  itm_vitzland_horse_2,
  itm_vitzland_horse_3,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,man_face_middle_1, man_face_old_2],

#Guards
["f5_guard","Vitzland Forhaz Guard","Vitzland Forhaz Guards",
  tf_guarantee_ranged|tf_guarantee_all|tf_guarantee_gloves,0,0,fac_kingdom_5,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_hammer_big,
  itm_sledgehammer_small,
  itm_trench_club_1,
  itm_trench_club_2,

  itm_round_shield,

  itm_vitzland_uniform_guard,
  
  itm_vitzland_salet_2,

  itm_vitzland_demi_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],
["f5_castle_guard","Vitzland Ferlde Guard","Vitzland Ferlde Guards",
  tf_guarantee_ranged|tf_guarantee_all|tf_guarantee_gloves,0,0,fac_kingdom_5,
  [
  itm_rifle_ammo,
  itm_vitzland_bolt_action_rifle_bayonet,

  itm_bayonet_4,
  itm_blucher,

  itm_round_shield,

  itm_vitzland_uniform_guard,
  
  itm_vitzland_salet_3,
  itm_vitzland_salet_3_gasmask,

  itm_vitzland_demi_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],
["f5_hall_guard","Vitzland Wactbavaion Guard","Vitzland Wactbavaion Guards",
  tf_guarantee_ranged|tf_guarantee_all|tf_guarantee_gloves,0,0,fac_kingdom_5,
  [
  itm_rifle_ammo,
  itm_vitzland_bolt_action_rifle_bayonet,

  itm_flamberge,

  itm_vitzland_armour,

  itm_vitzland_salet_heavy,
  itm_vitzland_salet_heavy_2,

  itm_vitzland_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],

#Terror
["f5_terror","Vitzland Nactman","Vitzland Nactmen",
  tf_infected|tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_5,
  [
  itm_pistol_ammo,
  itm_vitzland_smg,

  itm_sledgehammer,
  itm_butchering_knife,
  itm_bayonet_4,
  itm_blucher,

  itm_vitzland_nactman_armour,
  
  itm_nactman_head,

  itm_nachman_gauntlets,
  ],
  attr_terror, wp_5_m, knows_battle_5,x_face, x_face],

## Trezzo Republic ##
["f6_tier_0","Republican Coscritti","Republican Coscrittis",
  tf_has_body,0,0,fac_kingdom_6,
  [
  itm_throwing_knives,
  itm_darts,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_mace_1,
  itm_hatchet,
  itm_bayonet_1,
  itm_entrenching_tool,

  itm_republican_uniform_levy,
  ],
  attr_lvl_5,wp_start,knows_battle_1,man_face_younger_1, man_face_middle_2],
["f6_tier_1","Republican Rekluti","Republican Reklutis",
  tf_has_body,0,0,fac_kingdom_6,
  [
  itm_pistol_ammo,
  itm_trezzo_revolver,

  itm_throwing_knives,
  itm_darts,

  itm_cheap_rapier_1,
  itm_cheap_rapier_2,
  itm_cheap_rapier_3,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_mace_1,
  itm_hatchet,
  itm_bayonet_1,
  itm_entrenching_tool,

  itm_republican_uniform_regular,
  
  itm_republican_recruit_helmet,

  itm_republican_gloves,
  ],
  attr_lvl_15,wp_2_m,knows_battle_2,man_face_younger_1, man_face_middle_2],
["f6_tier_2","Republican Syldati","Republican Syldatis",
  tf_has_body|tf_guarantee_ranged,0,0,fac_kingdom_6,
  [
  itm_rifle_ammo,
  itm_trezzo_bolt_action_rifle,

  itm_cheap_rapier_1,
  itm_cheap_rapier_2,
  itm_cheap_rapier_3,

  (itm_republican_uniform_regular, imod_thick),
  
  itm_republican_infantry_helmet,

  itm_republican_gloves,
  ],
  attr_lvl_20,wp_3_m,knows_battle_3,man_face_young_1, man_face_old_2],
["f6_tier_3","Republican Veteran Syldati","Republican Veteran Syldatis",
  tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_6,
  [
  itm_rifle_ammo,
  itm_trezzo_bolt_action_rifle_bayonet,
  itm_trezzo_bolt_action_rifle,
  
  itm_cheap_rapier_1,
  itm_cheap_rapier_2,
  itm_cheap_rapier_3,

  itm_republican_uniform_sergeant,
  
  (itm_republican_infantry_helmet, imod_thick),
  
  itm_republican_gloves,
  ],
  attr_lvl_25,wp_4_m,knows_battle_4,man_face_young_1, man_face_old_2],
["f6_tier_4","Republican Canorale","Republican Canorales",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_6,
  [
  itm_rifle_ammo,
  itm_trezzo_bolt_action_rifle_bayonet,
  
  itm_cheap_rapier_1,
  itm_cheap_rapier_2,
  itm_cheap_rapier_3,

  itm_republican_uniform_raider,
  
  itm_republican_sergeant_helmet,

  itm_republican_gloves,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],
["f6_tier_5","Republican Servente","Republican Serventes",
  tf_mounted|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_6,
  [
  itm_pistol_ammo,
  itm_trezzo_smg,

  itm_cheap_rapier_1,
  itm_cheap_rapier_2,
  itm_cheap_rapier_3,

  itm_round_shield,

  itm_republican_uniform_officer_cuirass,
  
  itm_republican_raider_helmet,

  itm_republican_demi_gauntlets,
  
  itm_ammo_belt_2,
  ],
  attr_lvl_35,wp_6_r,knows_battle_6,man_face_middle_1, man_face_older_2],
["f6_tier_5_engineer","Republican Hutori","Republican Hutoris",
  tf_mounted|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_6,
  [
  itm_hand_torpedo,
  
  itm_flameammo,
  itm_flamethrower,

  itm_entrenching_tool,
  
  itm_republican_uniform_officer_cuirass,
  
  itm_gas_mask_ww,

  itm_republican_demi_gauntlets,
  ],
  attr_lvl_35,wp_6_r,knows_battle_6,man_face_middle_1, man_face_older_2],
["f6_tier_6","Republican Servente-senur","Republican Servente-senurs",
  tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_6,
  [
  itm_grenade,
  itm_grenade_frag,
  
  itm_pistol_ammo,
  itm_trezzo_smg_2,

  itm_estoc,
  itm_noble_rapier_1,
  itm_noble_rapier_2,
  itm_noble_rapier_3,
  
  itm_republican_armour,
  
  itm_republican_officer_helmet,

  itm_republican_gauntlets,
  
  itm_ammo_belt_2,
  ],
  attr_lvl_40,wp_6_r,knows_battle_6,man_face_middle_1, man_face_older_2],

#Cavalry
["f6_rider","Republican Cerabanieri","Republican Cerabanieris",
  tf_guarantee_ranged|tf_has_body|tf_has_hand|tf_has_head|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_6,
  [
  itm_rifle_ammo,
  itm_trezzo_bolt_action_carbine,

  itm_broadsword_1,
  itm_broadsword_2,

  itm_republican_uniform_cavalry,
  
  itm_republican_cavalry_helmet,

  itm_republican_demi_gauntlets,
  
  itm_trezzo_horse_1,
  itm_trezzo_horse_2,
  itm_trezzo_horse_3,
  itm_trezzo_horse_4,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,man_face_middle_1, man_face_old_2],

#Guards
["f6_guard","Republican Vardina Guarde","Republican Vardina Guardes",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_6,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_cheap_rapier_1,
  itm_cheap_rapier_2,
  itm_cheap_rapier_3,

  itm_round_shield,

  itm_republican_uniform_guard,
  
  itm_republican_guard_helmet,
  itm_republican_guard_helmet_2,

  itm_republican_demi_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],
["f6_castle_guard","Republican Caratri Guarde","Republican Caratri Guardes",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_6,
  [
  itm_rifle_ammo,
  itm_trezzo_bolt_action_rifle_bayonet,

  itm_cheap_rapier_1,
  itm_cheap_rapier_2,
  itm_cheap_rapier_3,

  itm_round_shield,

  itm_republican_uniform_guard_castle,
  
  itm_republican_castle_guard_helmet,

  itm_republican_demi_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],
["f6_hall_guard","Republican Bellemeria Guarde","Republican Bellemeria Guardes",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_6,
  [
  itm_rifle_ammo,
  itm_trezzo_bolt_action_rifle_bayonet,

  itm_noble_rapier_1,
  itm_noble_rapier_2,
  itm_noble_rapier_3,

  itm_round_shield,

  itm_republican_uniform_guard_hall,
  
  itm_republican_hall_guard_helmet,

  itm_republican_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],

#Terror
["f6_terror","Republican Servo-spider Cavalry", "Republican Servo-spider Cavalry",
  tf_mounted|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_6,
  [
  itm_grenade,
  itm_grenade_frag,
  
  itm_pistol_ammo,
  itm_trezzo_smg,
  
  itm_broadsword_1,
  itm_broadsword_2,
  
  itm_republican_servo_spider_uniform,
  
  itm_republican_cavalry_helmet,

  itm_servo_cav_gauntlets,
  
  itm_mech_spider,
  ],
  attr_terror, wp_6_r, knows_battle_5,man_face_young_1, man_face_old_2],

## Itami Castedom ##
["f7_tier_0","Itami Udak","Itami Udaks",
  tf_has_body,0,0,fac_kingdom_7,
  [
  itm_throwing_knives,
  itm_darts,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_mace_1,
  itm_hatchet,
  itm_bayonet_1,
  itm_entrenching_tool,

  itm_itami_uniform_levy,
  ],
  attr_lvl_5,wp_start,knows_battle_1,man_face_younger_1, man_face_middle_2],
["f7_tier_1","Itami Recruit","Itami Recruits",
  tf_has_body,0,0,fac_kingdom_7,
  [
  itm_pistol_ammo,
  itm_itami_pistol,

  itm_throwing_knives,
  itm_darts,

  itm_cheap_rapier_1,
  itm_cheap_rapier_2,
  itm_cheap_rapier_3,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_mace_1,
  itm_hatchet,
  itm_bayonet_1,
  itm_entrenching_tool,

  itm_itami_uniform_regular,
  
  itm_itami_recruit_helmet,

  itm_itami_gloves,
  ],
  attr_lvl_15,wp_2_m,knows_battle_2,man_face_younger_1, man_face_middle_2],
["f7_tier_2","Itami Soldier","Itami Soldiers",
  tf_has_body|tf_guarantee_ranged,0,0,fac_kingdom_7,
  [
  itm_rifle_ammo,
  itm_rifle_arisaka,

  itm_cheap_rapier_1,
  itm_cheap_rapier_2,
  itm_cheap_rapier_3,

  (itm_itami_uniform_regular, imod_thick),
  
  itm_itami_infantry_helmet,

  itm_itami_gloves,
  ],
  attr_lvl_20,wp_3_m,knows_battle_3,man_face_young_1, man_face_old_2],
["f7_tier_3","Itami Veteran Soldier","Itami Veteran Soldiers",
  tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_7,
  [
  itm_rifle_ammo,
  itm_rifle_arisaka_b,
  itm_rifle_arisaka,
  
  itm_cheap_rapier_1,
  itm_cheap_rapier_2,
  itm_cheap_rapier_3,

  itm_itami_uniform_sergeant,
  
  (itm_itami_infantry_helmet, imod_thick),
  
  itm_itami_gloves,
  ],
  attr_lvl_25,wp_4_m,knows_battle_4,man_face_young_1, man_face_old_2],
["f7_tier_4","Itami Corporal","Itami Corporals",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_7,
  [
  itm_rifle_ammo,
  itm_rifle_arisaka_b,
  
  itm_cheap_rapier_1,
  itm_cheap_rapier_2,
  itm_cheap_rapier_3,

  itm_itami_uniform_raider,
  
  itm_itami_sergeant_helmet,

  itm_itami_gloves,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],
["f7_tier_5","Itami Sergeant","Itami Sergeants",
  tf_mounted|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_7,
  [
  itm_pistol_ammo,
  itm_trezzo_smg,

  itm_cheap_rapier_1,
  itm_cheap_rapier_2,
  itm_cheap_rapier_3,

  itm_round_shield,

  itm_itami_uniform_officer_cuirass,
  
  itm_itami_raider_helmet,

  itm_itami_demi_gauntlets,
  
  itm_ammo_belt_2,
  ],
  attr_lvl_35,wp_6_r,knows_battle_6,man_face_middle_1, man_face_older_2],
["f7_tier_5_engineer","Itami Engineer","Itami Engineers",
  tf_mounted|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_7,
  [
  itm_hand_torpedo,
  
  itm_flameammo,
  itm_flamethrower,

  itm_entrenching_tool,
  
  itm_itami_uniform_officer_cuirass,
  
  itm_gas_mask_ww,

  itm_itami_demi_gauntlets,
  ],
  attr_lvl_35,wp_6_r,knows_battle_6,man_face_middle_1, man_face_older_2],
["f7_tier_6","Itami Senior Sergeant","Itami Senior Sergeants",
  tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_7,
  [
  itm_grenade,
  itm_grenade_frag,
  
  itm_pistol_ammo,
  itm_trezzo_smg_2,

  itm_katana,
  
  itm_itami_armour,
  
  itm_itami_officer_helmet,

  itm_itami_gauntlets,
  
  itm_ammo_belt_2,
  ],
  attr_lvl_40,wp_6_r,knows_battle_6,man_face_middle_1, man_face_older_2],

#Cavalry
["f7_rider","Itami Cavalry","Itami Cavalry",
  tf_guarantee_ranged|tf_has_body|tf_has_hand|tf_has_head|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_7,
  [
  itm_rifle_ammo,
  itm_rifle_arisaka,

  itm_katana,

  itm_itami_uniform_cavalry,
  
  itm_itami_cavalry_helmet,

  itm_itami_demi_gauntlets,
  
  itm_itami_horse_1,
  itm_itami_horse_2,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,man_face_middle_1, man_face_old_2],

#Guards
["f7_guard","Itami Guard","Itami Vardina Guardes",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_7,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_cheap_rapier_1,
  itm_cheap_rapier_2,
  itm_cheap_rapier_3,

  itm_round_shield,

  itm_itami_uniform_guard,
  
  itm_itami_guard_helmet,

  itm_itami_demi_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],
["f7_castle_guard","Itami Castle Guard","Itami Castle Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_7,
  [
  itm_rifle_ammo,
  itm_rifle_arisaka_b,

  itm_cheap_rapier_1,
  itm_cheap_rapier_2,
  itm_cheap_rapier_3,

  itm_round_shield,

  itm_itami_uniform_guard_castle,
  
  itm_itami_castle_guard_helmet,

  itm_itami_demi_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],
["f7_hall_guard","Itami Hall Guard","Itami Hall Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_7,
  [
  itm_rifle_ammo,
  itm_rifle_arisaka_b,

  itm_katana,

  itm_round_shield,

  itm_itami_uniform_guard_hall,
  
  itm_itami_hall_guard_helmet,

  itm_itami_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],

#Terror
["f7_terror","Itami Terro", "Itami Terror",
  tf_mounted|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_7,
  [
  itm_grenade,
  itm_grenade_frag,
  
  itm_pistol_ammo,
  itm_trezzo_smg,
  
  itm_katana,
  
  itm_itami_cavalry_helmet,
  ],
  attr_terror, wp_6_r, knows_battle_5,man_face_young_1, man_face_old_2],


## Irregular ##
["irregular_tier_0","Irregular Levy","Irregular Levies",
  tf_has_body,0,0,fac_irregulars,
  [
  itm_throwing_knives,
  itm_darts,
  itm_throwing_axes,
  
  itm_sharpened_stick,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  
  itm_irregular_uniform_levy,
  
  itm_bandit_hood_blk,
  itm_bandit_hood_blu,
  itm_bandit_hood_grn,
  itm_bandit_hood_red,
  itm_bandit_hood_wht,
  itm_bandit_hood_blk_scarf,
  itm_bandit_hood_blu_scarf,
  itm_bandit_hood_grn_scarf,
  itm_bandit_hood_red_scarf,
  itm_bandit_hood_wht_scarf,
  itm_straw_hat_1,
  itm_straw_hat_2,
  ],
  attr_lvl_5,wp_start,knows_battle_1,man_face_younger_1, man_face_middle_2],
["irregular_tier_1","Irregular Recruit","Irregular Recruits",
  tf_has_body,0,0,fac_irregulars,
  [
  itm_pistol_ammo,
  itm_common_revolver_5,
  
  itm_throwing_knives,
  itm_darts,
  itm_throwing_axes,
  
  itm_sharpened_stick,
  itm_entrenching_tool,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  
  itm_irregular_uniform_regular,
  
  itm_irregular_hat,

  itm_irregular_gloves,
  ],
  attr_lvl_15,wp_2_m,knows_battle_2,man_face_younger_1, man_face_middle_2],
["irregular_tier_2","Irregular Yeoman","Irregular Yeomen",
  tf_has_body|tf_guarantee_ranged,0,0,fac_irregulars,
  [
  itm_rifle_ammo,
  itm_irregular_bolt_action_rifle,
  itm_common_bolt_action_rifle,

  itm_knife,
  itm_kukri_rusty,
  itm_hand_axe,
  itm_bowie_knife,
  itm_trench_knife,
  itm_trench_knife_1,
  itm_entrenching_tool,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,

  itm_irregular_uniform_sergeant_1,

  itm_irregular_infantry_helmet,

  itm_irregular_gloves,
  ],
  attr_lvl_20,wp_3_m,knows_battle_3,man_face_young_1, man_face_old_2],
["irregular_tier_3","Irregular Infantry","Irregular Infantries",
  tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_irregulars,
  [
  itm_rifle_ammo,
  itm_irregular_bolt_action_rifle_bayonet,
  itm_common_bolt_action_rifle_bayonet,
  itm_irregular_bolt_action_rifle,

  itm_trooper_sword,
  itm_hand_axe,
  itm_hammer_big,
  itm_entrenching_tool,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  
  itm_rectangular_shield_1,
  itm_rectangular_shield_2,
  itm_rectangular_shield_3,
  itm_rectangular_shield_4,
  itm_rectangular_shield_5,
  itm_rectangular_shield_6,
  itm_rectangular_shield_7,
  itm_rectangular_shield_8,
  itm_rectangular_shield_9,
  itm_rectangular_shield_10,
  itm_rectangular_shield_11,
  itm_rectangular_shield_12,
  itm_rectangular_shield_13,
  itm_rectangular_shield_14,
  itm_rectangular_shield_15,
  itm_rectangular_shield_16,
  itm_rectangular_shield_17,
  
  itm_irregular_uniform_raider_1,

  itm_irregular_sergeant_helmet,

  itm_irregular_gloves,
  ],
  attr_lvl_25,wp_4_m,knows_battle_4,man_face_young_1, man_face_old_2],
["irregular_tier_4","Irregular Veteran","Irregular Veterans",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_irregulars,
  [
  itm_rifle_ammo,
  itm_irregular_bolt_action_rifle_bayonet,

  itm_trooper_sword,
  itm_hand_axe,
  itm_hammer_big,
  itm_sledgehammer_small,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  
  itm_irregular_uniform_cavalry_1,
  
  itm_irregular_raider_helmet,

  itm_irregular_gloves,
  
  itm_capelet_grey,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,man_face_middle_1, man_face_old_2],
["irregular_tier_5","Irregular Elite","Irregular Elites",
  tf_mounted|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_irregulars,
  [
  itm_pistol_ammo_pw,
  itm_irregular_smg,
  itm_irregular_smg_2,

  itm_lowlander_sword,
  
  itm_rectangular_shield_1,
  itm_rectangular_shield_2,
  itm_rectangular_shield_3,
  itm_rectangular_shield_4,
  itm_rectangular_shield_5,
  itm_rectangular_shield_6,
  itm_rectangular_shield_7,
  itm_rectangular_shield_8,
  itm_rectangular_shield_9,
  itm_rectangular_shield_10,
  itm_rectangular_shield_11,
  itm_rectangular_shield_12,
  itm_rectangular_shield_13,
  itm_rectangular_shield_14,
  itm_rectangular_shield_15,
  itm_rectangular_shield_16,
  itm_rectangular_shield_17,

  itm_irregular_armour,

  itm_irregular_officer_helmet,

  itm_irregular_gauntlets,
  
  itm_ammo_belt_2,
  ],
  attr_lvl_35,wp_6_m,knows_battle_6,man_face_middle_1, man_face_older_2],

#Cavalry
["irregular_rider","Irregular Rider","Irregular Riders",
  tf_guarantee_ranged|tf_has_body|tf_has_hand|tf_has_head|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_irregulars,
  [
  itm_rifle_ammo,
  itm_irregular_bolt_action_carbine,

  itm_light_cav_sword,

  itm_irregular_armour_cavalry,
  
  itm_irregular_cavalry_helmet,

  itm_irregular_demi_gauntlets,

  itm_plains_horse_1,
  itm_plains_horse_2,
  itm_plains_horse_3,
  itm_plains_horse_4,
  itm_plains_horse_5,
  
  itm_capelet_grey,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,man_face_middle_1, man_face_old_2],

#Guards
["irregular_guard","Irregular Prison Guard","Irregular Prison Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_irregulars,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,

  itm_rectangular_shield_1,
  itm_rectangular_shield_2,
  itm_rectangular_shield_3,
  itm_rectangular_shield_4,
  itm_rectangular_shield_5,
  itm_rectangular_shield_6,
  itm_rectangular_shield_7,
  itm_rectangular_shield_8,
  itm_rectangular_shield_9,
  itm_rectangular_shield_10,
  itm_rectangular_shield_11,
  itm_rectangular_shield_12,
  itm_rectangular_shield_13,
  itm_rectangular_shield_14,
  itm_rectangular_shield_15,
  itm_rectangular_shield_16,
  itm_rectangular_shield_17,
  
  itm_irregular_uniform_guard_1,

  itm_irregular_sergeant_helmet,

  itm_irregular_demi_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],
["irregular_castle_guard","Irregular Guard","Irregular Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_irregulars,
  [
  itm_rifle_ammo,
  itm_irregular_bolt_action_rifle_bayonet,

  itm_trooper_sword,
  itm_hand_axe,

  itm_rectangular_shield_1,
  itm_rectangular_shield_2,
  itm_rectangular_shield_3,
  itm_rectangular_shield_4,
  itm_rectangular_shield_5,
  itm_rectangular_shield_6,
  itm_rectangular_shield_7,
  itm_rectangular_shield_8,
  itm_rectangular_shield_9,
  itm_rectangular_shield_10,
  itm_rectangular_shield_11,
  itm_rectangular_shield_12,
  itm_rectangular_shield_13,
  itm_rectangular_shield_14,
  itm_rectangular_shield_15,
  itm_rectangular_shield_16,
  itm_rectangular_shield_17,
  
  itm_irregular_uniform_guard_1,

  itm_irregular_officer_helmet,

  itm_irregular_demi_gauntlets,
  
  itm_capelet_grey,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],
["irregular_hall_guard","Irregular Castle Guard","Irregular Castle Guards",
  tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_irregulars,
  [
  itm_pistol_ammo_pw,
  itm_irregular_smg_2,

  itm_trooper_sword,
  itm_hand_axe,

  itm_rectangular_shield_1,
  itm_rectangular_shield_2,
  itm_rectangular_shield_3,
  itm_rectangular_shield_4,
  itm_rectangular_shield_5,
  itm_rectangular_shield_6,
  itm_rectangular_shield_7,
  itm_rectangular_shield_8,
  itm_rectangular_shield_9,
  itm_rectangular_shield_10,
  itm_rectangular_shield_11,
  itm_rectangular_shield_12,
  itm_rectangular_shield_13,
  itm_rectangular_shield_14,
  itm_rectangular_shield_15,
  itm_rectangular_shield_16,
  itm_rectangular_shield_17,
  
  itm_irregular_armour_officer,

  itm_irregular_officer_helmet,

  itm_irregular_gauntlets,
  ],
  attr_lvl_30,wp_5_r,knows_battle_5,man_face_middle_1, man_face_old_2],

#Terror
["irregular_terror","Irregular Beast","Irregular Beaasts",
  tf_mutant|tf_guarantee_all,0,0,fac_irregulars,
  [
  itm_rancor_attack,
  itm_irregular_beastling_armour,
  itm_beastling_head,
  itm_beastling_hands,
  ],
  attr_terror, wp_5_m, knows_battle_5,x_face, x_face],

## Theocracy of Throd ##
["throd_tier_0","Miasma-slave Levy","Miasma-slave Levies",
  tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_has_body,0,0,fac_theocracy,
  [
  itm_throwing_knives,
  itm_darts,
  itm_throwing_axes,
  
  itm_sharpened_stick,
  
  itm_entenaii_uniform_levy,
  itm_dominion_uniform_levy,
  itm_galvae_uniform_levy,
  itm_union_uniform_levy,
  itm_vitzland_uniform_levy,
  itm_republican_uniform_levy,
  itm_irregular_uniform_levy,
  
  itm_infected_2,itm_infected_3,itm_infected_4,itm_infected_5,itm_infected_6,itm_infected_7,itm_infected_9,
  ],
  attr_lvl_5,wp_start,knows_battle_1,man_face_younger_1, man_face_middle_2],
["throd_tier_1","Miasma-slave Recruit","Miasma-slave Recruits",
  tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_has_body,0,0,fac_theocracy,
  [
  itm_pistol_ammo,
  itm_common_revolver_5,
  
  itm_throwing_knives,
  itm_darts,
  itm_throwing_axes,
  
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  
  itm_entenaii_uniform_private,
  itm_dominion_uniform_recruit,
  itm_galvae_uniform_regular,
  itm_union_uniform_regular,
  itm_vitzland_uniform_regular,
  itm_republican_uniform_regular,
  itm_irregular_uniform_regular,
  
  itm_infected_2,itm_infected_3,itm_infected_4,itm_infected_5,itm_infected_6,itm_infected_7,itm_infected_9,

  itm_entenaii_gloves,
  itm_dominion_gloves,
  itm_galvae_gloves,
  itm_union_gloves,
  itm_vitzland_gloves,
  itm_republican_gloves,
  itm_irregular_gloves,
  ],
  attr_lvl_15,wp_2_m,knows_battle_2,man_face_younger_1, man_face_middle_2],
["throd_tier_2","Miasma-slave Yeoman","Miasma-slave Yeomen",
  tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_has_body|tf_guarantee_ranged,0,0,fac_theocracy,
  [
  itm_rifle_ammo,
  itm_irregular_bolt_action_rifle,
  itm_common_bolt_action_rifle,

  itm_knife,
  itm_kukri_rusty,
  itm_hand_axe,
  itm_bowie_knife,
  itm_trench_knife,
  itm_trench_knife_1,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,

  itm_entenaii_uniform_private_2nd,
  itm_dominion_uniform_yeoman,
  itm_galvae_uniform_sergeant,
  itm_union_uniform_yeoman,
  itm_vitzland_uniform_sergeant,
  itm_republican_uniform_sergeant,
  itm_irregular_uniform_sergeant_1,

  itm_infected_2,itm_infected_3,itm_infected_4,itm_infected_5,itm_infected_6,itm_infected_7,itm_infected_9,

  itm_entenaii_gloves,
  itm_dominion_gloves,
  itm_galvae_gloves,
  itm_union_gloves,
  itm_vitzland_gloves,
  itm_republican_gloves,
  itm_irregular_gloves,
  ],
  attr_lvl_20,wp_3_m,knows_battle_3,man_face_young_1, man_face_old_2],
["throd_tier_3","Miasma-slave Infantry","Miasma-slave Infantries",
  tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_has_body|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_theocracy,
  [
  itm_rifle_ammo,
  itm_irregular_bolt_action_rifle_bayonet,
  itm_common_bolt_action_rifle_bayonet,
  itm_irregular_bolt_action_rifle,

  itm_trooper_sword,
  itm_hand_axe,
  itm_hammer_big,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  
  itm_rectangular_shield_1,
  itm_rectangular_shield_2,
  itm_rectangular_shield_3,
  itm_rectangular_shield_4,
  itm_rectangular_shield_5,
  itm_rectangular_shield_6,
  itm_rectangular_shield_7,
  itm_rectangular_shield_8,
  itm_rectangular_shield_9,
  itm_rectangular_shield_10,
  itm_rectangular_shield_11,
  itm_rectangular_shield_12,
  itm_rectangular_shield_13,
  itm_rectangular_shield_14,
  itm_rectangular_shield_15,
  itm_rectangular_shield_16,
  itm_rectangular_shield_17,
  
  itm_entenaii_uniform_private_1st,
  itm_dominion_uniform_infantry,
  itm_galvae_uniform_cavalry,
  itm_union_uniform_light_infantry,
  itm_vitzland_uniform_raider,
  itm_republican_uniform_raider,
  itm_irregular_uniform_raider_1,

  itm_infected_2,itm_infected_3,itm_infected_4,itm_infected_5,itm_infected_6,itm_infected_7,itm_infected_9,

  itm_entenaii_gloves,
  itm_dominion_gloves,
  itm_galvae_gloves,
  itm_union_gloves,
  itm_vitzland_gloves,
  itm_republican_gloves,
  itm_irregular_gloves,
  ],
  attr_lvl_25,wp_4_m,knows_battle_4,man_face_young_1, man_face_old_2],
["throd_tier_4","Miasma-slave Veteran","Miasma-slave Veterans",
  tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_ranged|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_theocracy,
  [
  itm_rifle_ammo,
  itm_irregular_bolt_action_rifle_bayonet,

  itm_trooper_sword,
  itm_hand_axe,
  itm_hammer_big,
  itm_sledgehammer_small,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  
  itm_entenaii_uniform_sergeant,
  itm_dominion_uniform_veteran,
  itm_galvae_uniform_raider,
  itm_union_uniform_sergeant,
  itm_vitzland_uniform_gunner,
  itm_republican_uniform_cavalry,
  itm_irregular_uniform_cavalry_1,
  
  itm_infected_2,itm_infected_3,itm_infected_4,itm_infected_5,itm_infected_6,itm_infected_7,itm_infected_9,

  itm_entenaii_demi_gauntlets,
  itm_dominion_demi_gauntlets,
  itm_galvae_demi_gauntlets,
  itm_union_demi_gauntlets,
  itm_vitzland_demi_gauntlets,
  itm_republican_demi_gauntlets,
  itm_irregular_demi_gauntlets,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,man_face_middle_1, man_face_old_2],
["throd_tier_5","Miasma-slave Elite","Miasma-slave Elites",
  tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_mounted|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_theocracy,
  [
  itm_grenade_miasma,
  
  itm_pistol_ammo_pw,
  itm_irregular_smg,
  itm_irregular_smg_2,

  itm_lowlander_sword,
  
  itm_rectangular_shield_1,
  itm_rectangular_shield_2,
  itm_rectangular_shield_3,
  itm_rectangular_shield_4,
  itm_rectangular_shield_5,
  itm_rectangular_shield_6,
  itm_rectangular_shield_7,
  itm_rectangular_shield_8,
  itm_rectangular_shield_9,
  itm_rectangular_shield_10,
  itm_rectangular_shield_11,
  itm_rectangular_shield_12,
  itm_rectangular_shield_13,
  itm_rectangular_shield_14,
  itm_rectangular_shield_15,
  itm_rectangular_shield_16,
  itm_rectangular_shield_17,

  itm_entenaii_uniform_officer,
  itm_dominion_uniform_officer,
  itm_galvae_uniform_officer,
  itm_union_uniform_officer,
  itm_vitzland_uniform_officer,
  itm_republican_uniform_officer,
  itm_irregular_uniform_officer_1,

  itm_infected_2,itm_infected_3,itm_infected_4,itm_infected_5,itm_infected_6,itm_infected_7,itm_infected_9,

  itm_entenaii_gauntlets,
  itm_dominion_gauntlets,
  itm_galvae_gauntlets,
  itm_union_gauntlets,
  itm_vitzland_gauntlets,
  itm_republican_gauntlets,
  itm_irregular_gauntlets,
  
  itm_ammo_belt_2,
  ],
  attr_lvl_35,wp_6_m,knows_battle_6,man_face_middle_1, man_face_older_2],

#Cavalry
["throd_rider","Miasma-slave Rider","Miasma-slave Riders",
  tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_guarantee_ranged|tf_has_body|tf_has_hand|tf_has_head|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_theocracy,
  [
  itm_grenade_miasma,
  
  itm_rifle_ammo,
  itm_irregular_bolt_action_carbine,

  itm_light_cav_sword,

  itm_entenaii_uniform_sergeant,
  itm_dominion_uniform_veteran,
  itm_galvae_uniform_raider,
  itm_union_uniform_sergeant,
  itm_vitzland_uniform_gunner,
  itm_republican_uniform_cavalry,
  itm_irregular_uniform_cavalry_1,
  
  itm_infected_2,itm_infected_3,itm_infected_4,itm_infected_5,itm_infected_6,itm_infected_7,itm_infected_9,

  itm_entenaii_demi_gauntlets,
  itm_dominion_demi_gauntlets,
  itm_galvae_demi_gauntlets,
  itm_union_demi_gauntlets,
  itm_vitzland_demi_gauntlets,
  itm_republican_demi_gauntlets,
  itm_irregular_demi_gauntlets,

  itm_ghoul_horse,
  itm_ghoul_horse_2,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,man_face_middle_1, man_face_old_2],

#Guards
["throd_guard","Throd_Prison Guard","Throd_Prison Guards",
  tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_has_body|tf_guarantee_ranged,
  0,0,fac_theocracy,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,

  itm_throd_robe_armoured,

  itm_hood_black,
  itm_hood_black_scarf,
  itm_hood_white,
  itm_hood_white_scarf,
  itm_hood_red,
  itm_hood_red_scarf,

  itm_leather_gloves,
  itm_black_gloves,
  ],
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["throd_castle_guard","Throd_Guard","Throd_Guards",
  tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,
  0,0,fac_theocracy,
  [
  itm_pistol_ammo,
  
  itm_grenade_miasma,

  itm_crook_revolver_1,
  
  itm_knife,
  itm_kukri_rusty,
  itm_metal_blade,
  itm_bayonet_1,
  itm_butchering_knife,

  itm_throd_shield,

  itm_dynamite,

  itm_throd_robe_armoured_heavy_1,

  itm_steel_helmet_2,
  itm_steel_helmet_2_gas,

  itm_black_gloves,
  (itm_throd_gauntlets,imod_ragged),
  (itm_black_gloves_metal,imod_ragged),
  ]+smg_1,
  attr_lvl_30,wp_5_m,knows_battle_5,bandit_face1, bandit_face2],
["throd_hall_guard","Throd_Castle Guard","Throd_Castle Guards",
  tf_infected|tf_allways_fall_dead|tf_no_capture_alive|tf_has_body|tf_guarantee_ranged|tf_has_head|tf_has_hand,
  0,0,fac_theocracy,
  [
  itm_rifle_ammo,

  itm_grenade_miasma,
  
  itm_knife,
  itm_kukri_rusty,
  itm_metal_blade,
  itm_bayonet_1,
  itm_butchering_knife,
  itm_katana,

  itm_shuriken,

  itm_throd_shield,

  itm_throd_robe_armoured_heavy_2,

  itm_zealot_helm_1,

  itm_throd_gauntlets,

  ]+rifles,
  attr_lvl_35,wp_6_m,knows_battle_6,bandit_face1, bandit_face2],

#Terror
["throd_terror","Miasma-Reaper","Miasma-Reapers",
  tf_allways_fall_dead|tf_no_capture_alive|tf_mutant|tf_guarantee_all,0,0,fac_theocracy,
  [
  itm_reaper_scythe,
  itm_ghoul_1,
  ],
  attr_terror, wp_5_m, knows_battle_5,x_face, x_face],

################
##Factions END##
################

##soldiers end##
["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",
  tf_hero|tf_randomize_face|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
  [
  itm_civilian_outfit_1w,
  itm_civilian_outfit_2w,
  itm_civilian_outfit_3w,
  itm_civilian_outfit_4w,
  itm_civilian_outfit_5w,
  itm_civilian_outfit_6w,
  itm_civilian_outfit_7w,
  itm_civilian_outfit_8w,
  itm_civilian_outfit_9w,
  itm_civilian_outfit_10w,
  itm_civilian_outfit_11w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,
  woman_face_1,woman_face_2],

["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",
  tf_hero, no_scene,reserved, fac_commoners,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,
  
  itm_civilian_outfit_1,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],
["galeas","Galeas","Galeas",tf_hero, 0, reserved, fac_commoners,
  [

  itm_civilian_outfit_1,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,0x000000000004718201c073191a9bb10c],
["mr_x", "Unknown", "Unknown", tf_hero, 0, 0, fac_commoners,
  [
  itm_pistol_ammo_pw,

  itm_pistol_sw_model_500,

  itm_sloppy_trench_coat,

  itm_civil_hat_4,
  ],
  lord_attrib,wp_5_m,lord_skills,
  0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],

["Xerina","Xerina","Xerina",tf_hero|tf_woman, 0,reserved,  fac_commoners,
  [
  itm_civilian_outfit_11w,
  ],
  def_attrib|level(39),wp_m(312),lord_skills,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
["Dranton","Dranton","Dranton",tf_hero, 0,reserved,  fac_commoners,
  [
  itm_civilian_outfit_1,
  ],
  def_attrib|level(42),wp_m(324),lord_skills,0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
["Kradus","Kradus","Kradus",tf_hero, 0,reserved,  fac_commoners,
  [
  itm_civilian_outfit_1,
  ],
  def_attrib|level(43),wp_m(270),lord_skills,0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],

# Add Extra Quest NPCs below this point
["local_merchant","Local Merchant","Local Merchants",
  tf_has_body, 0,0, fac_commoners,
  [
  itm_knife,

  itm_civilian_outfit_1,

  itm_civil_hat_1,
  itm_civil_hat_1_mask,
  itm_civil_hat_1b,
  itm_civil_hat_1b_mask,
  itm_civil_hat_1c,
  itm_civil_hat_1c_mask,
  itm_civil_hat_1d,
  itm_civil_hat_1d_mask,
  itm_civil_hat_2,
  itm_civil_hat_2_mask,
  itm_civil_hat_3,
  itm_civil_hat_3_mask,
  itm_civil_hat_4,
  itm_civil_hat_4_mask,
  itm_civil_hat_5,
  itm_civil_hat_5_mask,
  itm_civil_hat_7,
  itm_civil_hat_7_mask,
  itm_civil_hat_9,
  itm_civil_hat_9_mask,
  itm_civil_hat_10,
  itm_civil_hat_10_mask,
  itm_civil_hat_11,
  itm_civil_hat_11_mask,
  itm_civil_hat_12,
  itm_civil_hat_12_mask,
  itm_civil_hat_13,
  itm_civil_hat_13_mask,
  itm_civil_hat_14,
  itm_civil_hat_14_mask,
  ],
  attr_lvl_10,wp_1_m, knows_battle_1,merchant_face_1, merchant_face_2],
["tax_rebel","Rebel","Rebels", #copy
  tf_has_body,0,reserved,fac_commoners,
  [
  itm_pistol_ammo,

  itm_stones,
  itm_throwing_knives,

  itm_wooden_stick,
  itm_club,
  itm_simple_knife,
  itm_knife,
  itm_kukri_rusty,

  itm_civilian_outfit_1,

  itm_winter_hat_1, itm_winter_hat_2, itm_winter_hat_b,

  ]+revolvers,
  attr_lvl_10,wp_1_m,knows_battle_1,vaegir_face1, vaegir_face2],
["trainee_peasant","Peasant","Peasants",
  tf_has_body,0,reserved,fac_commoners,
  [
  itm_headband_black,
  itm_headband_white,
  itm_headband_red,
  itm_headband_blue,
  itm_headband_camo,
  itm_headband_green,
  
  itm_stones,

  itm_wooden_stick,
  itm_club,
  itm_simple_knife,
  itm_knife,
  itm_kukri_rusty,

  itm_civilian_outfit_1,

  itm_winter_hat_1, itm_winter_hat_2, itm_winter_hat_b,

  ],attr_lvl_10,wp_1_m,knows_battle_1,vaegir_face1, vaegir_face2],
["fugitive","Nervous Man","Nervous Men",
  tf_has_body,0,0,fac_commoners,
  [
  itm_knife,
  itm_bayonet_1,
  itm_big_club,
  itm_crowbar,
  itm_lead_pipe,
  itm_hand_axe,

  itm_sloppy_trench_coat,
  ],attr_lvl_25,wp_4_m, knows_battle_4,man_face_middle_1, man_face_old_2],
["fugitive_wanted_1", "Settler", "Wanted Men", #copy
  tf_has_body,0,0,fac_commoners,
  [
  itm_fisher,
  itm_fisher_2,
  itm_fisher_3,

  itm_sloppy_trench_coat,
  ],attr_lvl_25,wp_4_m, knows_battle_4,man_face_middle_1, man_face_old_2],
["fugitive_wanted_2", "Wanted Man", "Wanted Men", #copy
  tf_has_body,0,0,fac_commoners,
  [
  itm_fisher,
  itm_fisher_2,
  itm_fisher_3,

  itm_sloppy_trench_coat,
  ],attr_lvl_30,wp_5_m, knows_battle_5,man_face_middle_1, man_face_old_2],
["fugitive_wanted_3", "Wanted Man", "Wanted Men", #copy
  tf_has_body,0,0,fac_commoners,
  [
  itm_fisher,
  itm_fisher_2,
  itm_fisher_3,
  itm_sloppy_trench_coat,
  ],attr_lvl_35,wp_6_m, knows_battle_6,man_face_middle_1, man_face_old_2],
["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",
  tf_has_body|tf_guarantee_ranged,0,0,fac_commoners,
  [
  itm_pistol_revolver_1,
  itm_pistol_ammo_pw,
  itm_pistol_ammo,
  itm_club,
  itm_trench_club_1,
  itm_trench_club_2,
  itm_trench_club_3,
  itm_trench_club_4,
  itm_long_trench_club_1,
  itm_long_trench_club_2,
  itm_hammer,
  itm_knife,
  itm_bowie_knife,
  itm_kukri_rusty,
  itm_kukri_old,

  itm_civilian_outfit_1,
  itm_sloppy_trench_coat,
  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,

  itm_bandana_camo,
  itm_bandana_black,
  itm_bandana_blue,
  itm_bandana_red,
  itm_bandana_green,
  itm_bandana_white,
  ],
  attr_lvl_20,wp_3_m, knows_battle_3,bandit_face1, bandit_face2],
["hired_assassin","Freelancer","Freelancer", #copy
  tf_has_body|tf_guarantee_all,0,0,fac_commoners,
  [
  itm_pistol_walther_ppk_sil,
  itm_pistol_ammo_pw,
  itm_pistol_ammo,
  itm_knife,
  itm_knife,
  itm_hatchet,
  itm_lumberjack_axe,
  itm_hatchet_tactical,
  itm_sloppy_trench_coat,

  itm_hooded_cloak_1,
  itm_hooded_cloak_2,
  itm_hooded_cloak_3,
  itm_hooded_cloak_4,
  itm_hooded_cloak_5,
  ],
  attr_lvl_30,wp_5_m, knows_battle_5,bandit_face1, bandit_face2],
["fight_promoter","Fight Promoter","Fight Promoter",
  tf_has_body,0,0,fac_commoners,
  [
  itm_sloppy_trench_coat,

  itm_civil_hat_1,
  itm_civil_hat_1b,
  itm_civil_hat_1c,
  itm_civil_hat_1d,
  itm_civil_hat_2,
  itm_civil_hat_3,
  itm_civil_hat_4,
  itm_civil_hat_5,
  itm_civil_hat_7,
  itm_civil_hat_9,
  itm_civil_hat_10,
  itm_civil_hat_11,
  itm_civil_hat_12,
  itm_civil_hat_13,
  itm_civil_hat_14,
  ],
  attr_lvl_20,wp_3_m, knows_battle_3,bandit_face1, bandit_face2],
["brawler","Rough-Looking Brawler","Rough-Looking Brawler",
  tf_has_body,0,0,fac_commoners,
  [
  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,

  itm_bandana_camo,
  itm_bandana_black,
  itm_bandana_blue,
  itm_bandana_red,
  itm_bandana_green,
  itm_bandana_white,
  ],
  attr_lvl_30,wp_5_m, knows_battle_5, bandit_face1, bandit_face2],
["spy","Ordinary Townsman","Ordinary Townsmen", #copy
  tf_mounted|tf_has_body|tf_guarantee_gloves,
  0,0,fac_neutral,
  [
  itm_pistol_ammo,

  itm_bowie_knife,

  itm_sloppy_trench_coat,

  itm_civil_hat_1,
  itm_civil_hat_1b,
  itm_civil_hat_1c,
  itm_civil_hat_1d,
  itm_civil_hat_2,
  itm_civil_hat_3,
  itm_civil_hat_4,
  itm_civil_hat_5,
  itm_civil_hat_7,
  itm_civil_hat_9,
  itm_civil_hat_10,
  itm_civil_hat_11,
  itm_civil_hat_12,
  itm_civil_hat_13,
  itm_civil_hat_14,

  ]+revolvers,
  attr_lvl_20,wp_3_m, knows_battle_3,man_face_middle_1, man_face_older_2],
["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", #copy
  tf_mounted|tf_has_body|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
  [
  itm_pistol_ammo,

  itm_bowie_knife,

  itm_sloppy_trench_coat,

  itm_civil_hat_1,
  itm_civil_hat_1b,
  itm_civil_hat_1c,
  itm_civil_hat_1d,
  itm_civil_hat_2,
  itm_civil_hat_3,
  itm_civil_hat_4,
  itm_civil_hat_5,
  itm_civil_hat_7,
  itm_civil_hat_9,
  itm_civil_hat_10,
  itm_civil_hat_11,
  itm_civil_hat_12,
  itm_civil_hat_13,
  itm_civil_hat_14,
  
  ]+semi_pistols,
  attr_lvl_20,wp_3_m, knows_battle_3,vaegir_face1, vaegir_face2],
["nurse_for_lady","Nurse","Nurse",
  tf_woman|tf_has_body,0,reserved,fac_commoners,
  [
  itm_civilian_outfit_1w,
  itm_civilian_outfit_2w,
  itm_civilian_outfit_3w,
  itm_civilian_outfit_4w,
  itm_civilian_outfit_5w,
  itm_civilian_outfit_6w,
  itm_civilian_outfit_7w,
  itm_civilian_outfit_8w,
  itm_civilian_outfit_9w,
  itm_civilian_outfit_10w,
  itm_civilian_outfit_11w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,woman_face_1, woman_face_2],
["temporary_minister","Minister","Minister",tf_has_body,0,reserved,fac_commoners,
  [
  itm_sloppy_trench_coat,

  itm_civil_hat_1,
  itm_civil_hat_1b,
  itm_civil_hat_1c,
  itm_civil_hat_1d,
  itm_civil_hat_2,
  itm_civil_hat_3,
  itm_civil_hat_4,
  itm_civil_hat_5,
  itm_civil_hat_7,
  itm_civil_hat_9,
  itm_civil_hat_10,
  itm_civil_hat_11,
  itm_civil_hat_12,
  itm_civil_hat_13,
  itm_civil_hat_14,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,man_face_middle_1, man_face_older_2],
["farmer_from_bandit_village","Settler","Settlers",tf_has_body,no_scene,reserved,fac_commoners, #copy
  [
  itm_arrows,
  itm_pistol_ammo,

  itm_stones,
  itm_throwing_knives,
  itm_hunting_bow,
  itm_short_bow,

  itm_wooden_stick,
  itm_club,
  itm_staff,
  itm_2by4,
  itm_pitch_fork,
  itm_wrench,
  itm_screwdriver,
  itm_screwdriver2,
  itm_shovel_short,
  itm_shovel,
  itm_hand_saw,
  itm_hammer,
  itm_hatchet,
  itm_lumberjack_axe,
  itm_pickaxe,
  itm_staff,
  itm_simple_knife,
  itm_knife,
  itm_kukri_old,

  itm_civilian_outfit_2,

  ]+revolvers,
  attr_lvl_10,wp_1_m,knows_battle_1,man_face_middle_1, man_face_older_2],

## new walkers
["businessman","Businessman","Businessmen",
  tf_has_body,0,0,fac_commoners,
  [
  itm_steel_briefcase,
  itm_leather_briefcase,
  itm_sloppy_trench_coat,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],

["butcher","Butcher","Butchers",
  tf_has_body,0,0,fac_commoners,
  [
  itm_cleaver,
  itm_butchering_knife,

  itm_tavern_apron,

  itm_bandana_camo,
  itm_bandana_black,
  itm_bandana_blue,
  itm_bandana_red,
  itm_bandana_green,
  itm_bandana_white,
  itm_headband_black,
  itm_headband_white,
  itm_headband_red,
  itm_headband_blue,
  itm_headband_camo,
  itm_headband_green,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],
["carpenter","Carpenter","Carpenters",
  tf_has_body,0,0,fac_commoners,
  [
  itm_screwdriver,
  itm_screwdriver2,
  itm_hand_saw,
  itm_hammer,
  itm_hatchet,

  itm_fisher,
  itm_fisher_2,
  itm_fisher_3,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],
["dancer_girl","Dancer","Dancer",
  tf_woman|tf_has_body,0,0,fac_commoners,
  [
  itm_republican_consort_dress_1,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,woman_face_1,woman_face_2],
["doctor","Doctor","Doctors",
  tf_has_body,0,0,fac_commoners,
  [
  itm_doctor,

  itm_doctor_head,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],
["drug_dealer","Drug_Dealer","Drug_Dealers",
  tf_has_body,0,0,fac_commoners,
  [
  itm_sloppy_trench_coat,
  itm_poor_shirt_1,
  itm_poor_shirt_2,
  itm_poor_shirt_3,
  itm_poor_shirt_4,
  itm_poor_shirt_5,
  itm_poor_shirt_6,
  
  itm_hooded_cloak_1,
  itm_hooded_cloak_2,
  itm_hooded_cloak_3,
  itm_hooded_cloak_4,
  itm_hooded_cloak_5,
  itm_bandit_hood_blk,
  itm_bandit_hood_blu,
  itm_bandit_hood_grn,
  itm_bandit_hood_red,
  itm_bandit_hood_wht,
  itm_bandit_hood_blk_scarf,
  itm_bandit_hood_blu_scarf,
  itm_bandit_hood_grn_scarf,
  itm_bandit_hood_red_scarf,
  itm_bandit_hood_wht_scarf,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],
["drunk","Drunk","Drunk",
  tf_has_body,0,0,fac_commoners,
  [
  itm_tankard,
  itm_poor_shirt_1,

  itm_bandana_camo,
  itm_bandana_black,
  itm_bandana_blue,
  itm_bandana_red,
  itm_bandana_green,
  itm_bandana_white,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],
["ghoul_walker","Ghoul","Ghouls",
  tf_ghoul_human|tf_has_body,
  0,0,fac_commoners,
  [
  itm_civilian_outfit_3,

  itm_bandana_camo,
  itm_bandana_black,
  itm_bandana_blue,
  itm_bandana_red,
  itm_bandana_green,
  itm_bandana_white,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],
["mechanic","Mechanic","Mechanics",
  tf_has_body,0,0,fac_commoners,
  [
  itm_spanner,
  itm_crowbar,
  itm_wrench,
  itm_monkeywrench,
  itm_screwdriver,
  itm_screwdriver2,

  itm_mechanic,
  itm_mechanic_blue,
  itm_mechanic_brown,
  itm_mechanic_green,
  itm_mechanic_red,
  itm_fisher,
  itm_fisher_2,
  itm_fisher_3,

  itm_welder_mask,
  itm_welder_mask_ms,

  itm_bandana_camo,
  itm_bandana_black,
  itm_bandana_blue,
  itm_bandana_red,
  itm_bandana_green,
  itm_bandana_white,
  itm_goggles_1,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],
["musician","Musician","Musicians",
  tf_guarantee_gloves|tf_has_body,
  0,0,fac_commoners,
  [
  itm_civilian_outfit_8,

  itm_bandana_camo,
  itm_bandana_black,
  itm_bandana_blue,
  itm_bandana_red,
  itm_bandana_green,
  itm_bandana_white,

  itm_headband_black,
  itm_headband_white,
  itm_headband_red,
  itm_headband_blue,
  itm_headband_camo,
  itm_headband_green,
  itm_headband_pink,
  itm_wooly_grey,
  itm_wooly_red,
  itm_wooly_green,
  itm_wooly_black,
  itm_wooly_tan,
  itm_wooly_blue,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],
["church_priest","Follower_of_the_Fear_of_The_Miasma","Follower_of_the_Fear_of_The_Miasma",
  tf_has_body,0,0,fac_commoners,
  [
  itm_robe_1,
  itm_robe_2,
  itm_robe_3,
  itm_robe_4,
  (itm_robe_1, imod_ragged),
  (itm_robe_2, imod_ragged),
  (itm_robe_3, imod_ragged),
  (itm_robe_4, imod_ragged),
  itm_hood_1,
  itm_hood_2,
  itm_hood_3,
  itm_hood_4,
  (itm_hood_1, imod_ragged),
  (itm_hood_2, imod_ragged),
  (itm_hood_3, imod_ragged),
  (itm_hood_4, imod_ragged),
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],
["church_traveller","Traveler","Travellers",
  tf_has_body,0,0,fac_commoners,
  [
  itm_robe_1,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],
["gentleman","Traveller","Traveller",
  tf_has_body,0,0,fac_commoners,
  [
  itm_frock_1,
  itm_frock_2,
  itm_sloppy_trench_coat,

  itm_civil_hat_1,
  itm_civil_hat_1_mask,
  itm_civil_hat_1b,
  itm_civil_hat_1b_mask,
  itm_civil_hat_1c,
  itm_civil_hat_1c_mask,
  itm_civil_hat_1d,
  itm_civil_hat_1d_mask,
  itm_civil_hat_2,
  itm_civil_hat_2_mask,
  itm_civil_hat_3,
  itm_civil_hat_3_mask,
  itm_civil_hat_4,
  itm_civil_hat_4_mask,
  itm_civil_hat_5,
  itm_civil_hat_5_mask,
  itm_civil_hat_7,
  itm_civil_hat_7_mask,
  itm_civil_hat_9,
  itm_civil_hat_9_mask,
  itm_civil_hat_10,
  itm_civil_hat_10_mask,
  itm_civil_hat_11,
  itm_civil_hat_11_mask,
  itm_civil_hat_12,
  itm_civil_hat_12_mask,
  itm_civil_hat_13,
  itm_civil_hat_13_mask,
  itm_civil_hat_14,
  itm_civil_hat_14_mask,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,mercenary_face_1, mercenary_face_2],

#This troop is the troop marked as soldiers_end and town_walkers_begin
["town_walker_1","Imperial Citizen","Citizens", #Entenaii Empire
  tf_has_body,0,0,fac_commoners,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  
  itm_wooly_grey,
  itm_wooly_red,
  itm_wooly_green,
  itm_wooly_black,
  itm_wooly_tan,
  itm_wooly_blue,
  itm_wooly_grey_scarf,
  itm_wooly_red_scarf,
  itm_wooly_green_scarf,
  itm_wooly_black_scarf,
  itm_wooly_tan_scarf,
  itm_wooly_blue_scarf,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,man_face_young_1, man_face_old_2],
["town_walker_1w","Imperial Citizen","Citizens",
  tf_woman|tf_has_body,0,0,fac_commoners,
  [
  itm_civilian_outfit_1w,
  itm_civilian_outfit_2w,
  itm_civilian_outfit_3w,
  itm_civilian_outfit_4w,
  itm_civilian_outfit_5w,
  itm_civilian_outfit_6w,
  itm_civilian_outfit_7w,
  itm_civilian_outfit_8w,
  itm_civilian_outfit_9w,
  itm_civilian_outfit_10w,
  itm_civilian_outfit_11w,

  itm_veil_pink,
  itm_veil_cream,
  itm_veil_blue,
  itm_veil_blue_2,
  itm_veil_white,
  itm_veil_green,
  itm_veil_grey,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,woman_face_1,woman_face_2],
["town_walker_2","Dominioner","Dominioners", #Entenaii Dominion
  tf_has_body,0,0,fac_commoners,
  [
  itm_dominion_civilian_clothes_1,
  itm_dominion_civilian_clothes_2,
  itm_dominion_civilian_clothes_3,
  itm_dominion_civilian_clothes_4,
  itm_dominion_civilian_clothes_5,
  itm_dominion_civilian_clothes_6,
  itm_dominion_civilian_clothes_7,
  itm_dominion_civilian_clothes_8,
  itm_dominion_civilian_clothes_9,
  itm_dominion_civilian_clothes_10,
  itm_dominion_civilian_clothes_11,
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  
  itm_straw_hat_1,
  itm_straw_hat_2,
  itm_dominion_civ_hat_1,
  itm_wooly_grey,
  itm_wooly_red,
  itm_wooly_green,
  itm_wooly_black,
  itm_wooly_tan,
  itm_wooly_blue,
  itm_wooly_grey_scarf,
  itm_wooly_red_scarf,
  itm_wooly_green_scarf,
  itm_wooly_black_scarf,
  itm_wooly_tan_scarf,
  itm_wooly_blue_scarf,
  itm_bandit_hood_blk,
  itm_bandit_hood_blu,
  itm_bandit_hood_grn,
  itm_bandit_hood_red,
  itm_bandit_hood_wht,
  itm_bandit_hood_blk_scarf,
  itm_bandit_hood_blu_scarf,
  itm_bandit_hood_grn_scarf,
  itm_bandit_hood_red_scarf,
  itm_bandit_hood_wht_scarf,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,
  man_face_young_1, man_face_old_2],
["town_walker_2w","Dominioner","Dominioners",
  tf_woman|tf_has_body,0,0,fac_commoners,
  [
  itm_dominion_civilian_clothes_1,
  itm_dominion_civilian_clothes_2,
  itm_dominion_civilian_clothes_3,
  itm_dominion_civilian_clothes_4,
  itm_dominion_civilian_clothes_5,
  itm_dominion_civilian_clothes_6,
  itm_dominion_civilian_clothes_7,
  itm_dominion_civilian_clothes_8,
  itm_dominion_civilian_clothes_9,
  itm_dominion_civilian_clothes_10,
  itm_dominion_civilian_clothes_11,
  itm_dominion_dress_1,
  itm_dominion_dress_2,
  itm_dominion_dress_3,
  itm_civilian_outfit_8w,
  itm_civilian_outfit_9w,

  itm_straw_hat_1,
  itm_straw_hat_2,
  itm_dominion_civ_hat_1,
  itm_veil_pink,
  itm_veil_cream,
  itm_veil_blue,
  itm_veil_blue_2,
  itm_veil_white,
  itm_veil_green,
  itm_veil_grey,
  itm_bandit_hood_blk,
  itm_bandit_hood_blu,
  itm_bandit_hood_grn,
  itm_bandit_hood_red,
  itm_bandit_hood_wht,
  itm_bandit_hood_blk_scarf,
  itm_bandit_hood_blu_scarf,
  itm_bandit_hood_grn_scarf,
  itm_bandit_hood_red_scarf,
  itm_bandit_hood_wht_scarf,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,
  woman_face_1,woman_face_2],
["town_walker_3","Brochsman","Brochsmen", #Kingdom of Galvae
  tf_has_body,0,0,fac_commoners,
  [
  itm_gatheredcloaks1,
  itm_gatheredcloaks2,
  itm_gatheredcloaks3,
  itm_gatheredcloaks4,
  itm_gatheredcloaks5,
  itm_goatskin_tunic,
  
  itm_straw_hat_1,
  itm_straw_hat_2,
  itm_bandit_hood_blk,
  itm_bandit_hood_blu,
  itm_bandit_hood_grn,
  itm_bandit_hood_red,
  itm_bandit_hood_wht,
  itm_bandit_hood_blk_scarf,
  itm_bandit_hood_blu_scarf,
  itm_bandit_hood_grn_scarf,
  itm_bandit_hood_red_scarf,
  itm_bandit_hood_wht_scarf,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,man_face_young_1, man_face_old_2],
["town_walker_3w","Brochswoman","Brochswomen",
  tf_woman|tf_has_body,0,0,fac_commoners,
  [
  itm_gatheredcloaks1,
  itm_gatheredcloaks2,
  itm_gatheredcloaks3,
  itm_gatheredcloaks4,
  itm_gatheredcloaks5,
  itm_goatskin_tunic,
  itm_tartan_dress_1,
  itm_tartan_dress_2,
  itm_tartan_dress_3,
  itm_tartan_dress_4,
  itm_tartan_dress_5,
  itm_tartan_dress_6,
  
  itm_straw_hat_1,
  itm_straw_hat_2,
  itm_veil_pink,
  itm_veil_cream,
  itm_veil_blue,
  itm_veil_blue_2,
  itm_veil_white,
  itm_veil_green,
  itm_veil_grey,
  itm_bandit_hood_blk,
  itm_bandit_hood_blu,
  itm_bandit_hood_grn,
  itm_bandit_hood_red,
  itm_bandit_hood_wht,
  itm_bandit_hood_blk_scarf,
  itm_bandit_hood_blu_scarf,
  itm_bandit_hood_grn_scarf,
  itm_bandit_hood_red_scarf,
  itm_bandit_hood_wht_scarf,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,woman_face_1,woman_face_2],
["town_walker_4","Serf","Serfs", #Molvat-Berchav Union
  tf_has_body,0,0,fac_commoners,
  [
  itm_union_civ_1,
  itm_union_civ_2,
  itm_union_civ_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,

  itm_straw_hat_1,
  itm_straw_hat_2,
  itm_bandit_hood_blk,
  itm_bandit_hood_blu,
  itm_bandit_hood_grn,
  itm_bandit_hood_red,
  itm_bandit_hood_wht,
  itm_bandit_hood_blk_scarf,
  itm_bandit_hood_blu_scarf,
  itm_bandit_hood_grn_scarf,
  itm_bandit_hood_red_scarf,
  itm_bandit_hood_wht_scarf,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,
  man_face_young_1, man_face_old_2],
["town_walker_4w","Serf","Serfs",
  tf_woman|tf_has_body,0,0,fac_commoners,
  [
  itm_wool_dress_1,
  itm_wool_dress_2,
  itm_wool_dress_3,
  itm_wool_dress_4,
  itm_wool_dress_5,
  
  itm_straw_hat_1,
  itm_straw_hat_2,
  itm_veil_grey_2,
  itm_veil_cream_2,
  itm_veil_brown, 
  itm_veil_orange,
  itm_veil_striped,
  itm_bandit_hood_blk,
  itm_bandit_hood_blu,
  itm_bandit_hood_grn,
  itm_bandit_hood_red,
  itm_bandit_hood_wht,
  itm_bandit_hood_blk_scarf,
  itm_bandit_hood_blu_scarf,
  itm_bandit_hood_grn_scarf,
  itm_bandit_hood_red_scarf,
  itm_bandit_hood_wht_scarf,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,
  woman_face_1,woman_face_2],
["town_walker_5","Rulksman","Rulksmen", #Vitzland Territories
  tf_has_body,0,0,fac_commoners,
  [
  itm_peasant_shirt_1,
  itm_peasant_shirt_2,
  itm_peasant_shirt_3,
  itm_peasant_shirt_4,
  itm_peasant_shirt_5,
  itm_peasant_shirt_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,
  man_face_young_1, man_face_old_2],
["town_walker_5w","Rulkswoman","Rulkswomen",
  tf_woman|tf_has_body,0,0,fac_commoners,
  [
  itm_vitzland_dress_1,
  itm_vitzland_dress_2,
  itm_vitzland_dress_3,
  itm_vitzland_dress_4,
  itm_vitzland_dress_5,
  itm_vitzland_dress_6,
  itm_civilian_outfit_7w,
  itm_civilian_outfit_8w,
  itm_civilian_outfit_9w,
  itm_civilian_outfit_10w,
  itm_civilian_outfit_11w,
  
  itm_veil_grey_2,
  itm_veil_cream_2,
  itm_veil_brown, 
  itm_veil_orange,
  itm_veil_striped,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,
  woman_face_1,woman_face_2],
["town_walker_6","Citizi de Trezzo","Citizens de Trezzo", #Trezzo Republic
  tf_infected|tf_has_body,0,0,fac_commoners,
  [
  itm_republican_civ_1,
  itm_republican_civ_2,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,
  man_face_young_1, man_face_old_2],
["town_walker_6w","Citiza de Trezzo","Citizas de Trezzo",
  tf_woman|tf_has_body,0,0,fac_commoners,
  [
  itm_white_dress_1,
  itm_white_dress_2,
  
  itm_veil_pink,
  itm_veil_cream,
  itm_veil_white,
  itm_veil_grey,
  itm_veil_grey_2,
  itm_veil_cream_2,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,woman_face_1,woman_face_2],
["town_walker_7","Uda","Uda", #Itami Castedom
  tf_infected|tf_has_body,0,0,fac_commoners,
  [
  itm_republican_civ_1,
  itm_republican_civ_2,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,
  man_face_young_1, man_face_old_2],
["town_walker_7w","Uda","Uda",
  tf_woman|tf_has_body,0,0,fac_commoners,
  [
  itm_white_dress_1,
  itm_white_dress_2,
  
  itm_veil_pink,
  itm_veil_cream,
  itm_veil_white,
  itm_veil_grey,
  itm_veil_grey_2,
  itm_veil_cream_2,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,woman_face_1,woman_face_2],

#This troop is the troop marked as town_walkers_end and village_walkers_begin #not yet until assigning comp.

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
["spy_walker_1","Settler","Settlers",tf_has_body|tf_guarantee_helmet,0,0,fac_commoners,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,man_face_middle_1, man_face_old_2],
["spy_walker_1w","Settler","Settlers",tf_woman|tf_has_body|tf_guarantee_helmet,0,0,fac_commoners,
  [
  itm_civilian_outfit_1w,
  itm_civilian_outfit_2w,
  itm_civilian_outfit_3w,
  itm_civilian_outfit_4w,
  itm_civilian_outfit_5w,
  itm_civilian_outfit_6w,
  itm_civilian_outfit_7w,
  itm_civilian_outfit_8w,
  itm_civilian_outfit_9w,
  itm_civilian_outfit_10w,
  itm_civilian_outfit_11w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,woman_face_1,woman_face_2],
["spy_walker_2","Settler","Settlers",tf_has_body|tf_guarantee_helmet,0,0,fac_commoners,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,man_face_middle_1, man_face_old_2],
["spy_walker_2w","Settler","Settlers",tf_woman|tf_has_body|tf_guarantee_helmet,0,0,fac_commoners,
  [
  itm_civilian_outfit_1w,
  itm_civilian_outfit_2w,
  itm_civilian_outfit_3w,
  itm_civilian_outfit_4w,
  itm_civilian_outfit_5w,
  itm_civilian_outfit_6w,
  itm_civilian_outfit_7w,
  itm_civilian_outfit_8w,
  itm_civilian_outfit_9w,
  itm_civilian_outfit_10w,
  itm_civilian_outfit_11w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,woman_face_1,woman_face_2],
["spy_walker_3","Settler","Settlers",tf_has_body|tf_guarantee_helmet,0,0,fac_commoners,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,man_face_middle_1, man_face_old_2],
["spy_walker_3w","Settler","Settlers",tf_woman|tf_has_body|tf_guarantee_helmet,0,0,fac_commoners,
  [
  itm_civilian_outfit_1w,
  itm_civilian_outfit_2w,
  itm_civilian_outfit_3w,
  itm_civilian_outfit_4w,
  itm_civilian_outfit_5w,
  itm_civilian_outfit_6w,
  itm_civilian_outfit_7w,
  itm_civilian_outfit_8w,
  itm_civilian_outfit_9w,
  itm_civilian_outfit_10w,
  itm_civilian_outfit_11w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,woman_face_1,woman_face_2],
["spy_walker_4","Settler","Settlers",tf_has_body|tf_guarantee_helmet,0,0,fac_commoners,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,man_face_middle_1, man_face_old_2],
["spy_walker_4w","Settler","Settlers",tf_woman|tf_has_body|tf_guarantee_helmet,0,0,fac_commoners,
  [
  itm_civilian_outfit_1w,
  itm_civilian_outfit_2w,
  itm_civilian_outfit_3w,
  itm_civilian_outfit_4w,
  itm_civilian_outfit_5w,
  itm_civilian_outfit_6w,
  itm_civilian_outfit_7w,
  itm_civilian_outfit_8w,
  itm_civilian_outfit_9w,
  itm_civilian_outfit_10w,
  itm_civilian_outfit_11w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,woman_face_1,woman_face_2],
["spy_walker_5","Settler","Settlers",tf_has_body|tf_guarantee_helmet,0,0,fac_commoners,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,man_face_middle_1, man_face_old_2],
["spy_walker_5w","Settler","Settlers",tf_woman|tf_has_body|tf_guarantee_helmet,0,0,fac_commoners,
  [
  itm_civilian_outfit_1w,
  itm_civilian_outfit_2w,
  itm_civilian_outfit_3w,
  itm_civilian_outfit_4w,
  itm_civilian_outfit_5w,
  itm_civilian_outfit_6w,
  itm_civilian_outfit_7w,
  itm_civilian_outfit_8w,
  itm_civilian_outfit_9w,
  itm_civilian_outfit_10w,
  itm_civilian_outfit_11w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,woman_face_1,woman_face_2],
["spy_walker_6","Settler","Settlers",tf_infected|tf_has_body|tf_guarantee_helmet,0,0,fac_commoners,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,man_face_middle_1, man_face_old_2],
["spy_walker_6w","Settler","Settlers",tf_woman|tf_has_body|tf_guarantee_helmet,0,0,fac_commoners,
  [
  itm_civilian_outfit_1w,
  itm_civilian_outfit_2w,
  itm_civilian_outfit_3w,
  itm_civilian_outfit_4w,
  itm_civilian_outfit_5w,
  itm_civilian_outfit_6w,
  itm_civilian_outfit_7w,
  itm_civilian_outfit_8w,
  itm_civilian_outfit_9w,
  itm_civilian_outfit_10w,
  itm_civilian_outfit_11w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,woman_face_1,woman_face_2],
["spy_walker_7","Settler","Settlers",tf_infected|tf_has_body|tf_guarantee_helmet,0,0,fac_commoners,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,man_face_middle_1, man_face_old_2],
["spy_walker_7w","Settler","Settlers",tf_woman|tf_has_body|tf_guarantee_helmet,0,0,fac_commoners,
  [
  itm_civilian_outfit_1w,
  itm_civilian_outfit_2w,
  itm_civilian_outfit_3w,
  itm_civilian_outfit_4w,
  itm_civilian_outfit_5w,
  itm_civilian_outfit_6w,
  itm_civilian_outfit_7w,
  itm_civilian_outfit_8w,
  itm_civilian_outfit_9w,
  itm_civilian_outfit_10w,
  itm_civilian_outfit_11w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,woman_face_1,woman_face_2],
#This troop is the troop marked as spy_walkers_end

# Ransom brokers
["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_civilian_outfit_9,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_civilian_outfit_2,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_civilian_outfit_7,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_civilian_outfit_11,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_civilian_outfit_12,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_civilian_outfit_4,

  itm_straw_hat_2,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_civilian_outfit_5,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_civilian_outfit_6,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [
  itm_blunt_slug_ammo,
  itm_shotgun_riot,

  itm_civilian_outfit_8,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],

# Tavern travelers
["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [
  itm_civilian_outfit_4,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [
  itm_civilian_outfit_5,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [
  itm_civilian_outfit_6,
  
  itm_straw_hat_1,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [

  itm_civilian_outfit_7,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [

  itm_civilian_outfit_8,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [

  itm_civilian_outfit_9,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [
  itm_civilian_outfit_10,

  itm_bandit_hood_blu,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [

  itm_civilian_outfit_11,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [

  itm_civilian_outfit_12,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [

  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],

# Tavern booksellers
["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,
  [

  itm_civilian_outfit_2,
  
  itm_straw_hat_2,

  itm_book_tactics,
  itm_book_persuasion,
  itm_book_leadership,
  itm_book_training_reference,
  itm_book_surgery_reference,
  itm_book_prisoner_management,
  itm_book_inventory_management,
  itm_book_spotting,
  itm_book_looting,
  itm_book_shield,
  itm_book_trade_ledger
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,
  merchant_face_1,merchant_face_2],
["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,
  [

  itm_civilian_outfit_3,

  itm_book_wound_treatment_reference,
  itm_book_intelligence,
  itm_book_trade,
  itm_book_engineering,
  itm_book_weapon_mastery,
  itm_book_first_aid,
  itm_book_tracking,
  itm_book_pathfinding,
  itm_book_athletics,
  itm_book_power_strike,
  itm_book_trade_ledger
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1, merchant_face_2],

# Tavern minstrel
["tavern_minstrel_1","Wandering Musician","Musician",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_has_body, 0, reserved, fac_commoners,
  [

  itm_civilian_outfit_4,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["tavern_minstrel_2","Wandering Musician","Musician",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_has_body, 0, reserved, fac_commoners,
  [

  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["tavern_minstrel_3","Wandering Musician","Musician",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_has_body, 0, reserved, fac_commoners,
  [

  itm_civilian_outfit_10,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["tavern_minstrel_4","Wandering Musician","Musician",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_has_body, 0, reserved, fac_commoners,
  [
  itm_civilian_outfit_3,

  itm_bandit_hood_wht,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],
["tavern_minstrel_5","Wandering Musician","Musician",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_has_body, 0, reserved, fac_commoners,
  [

  itm_civilian_outfit_9,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1,merchant_face_1,merchant_face_2],

#NPC system changes begin
#Companions
["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp_m(320),lord_skills, 0x000000000010918a01f248377289467d],
["npc1","Declan Mac Fheargail","Declan",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
  [
  itm_cloak_1,
  itm_shepherds_crook,
  
  ]+companion_gear,
  str_8|agi_7|int_12|cha_7|level(3),wp_m(60),knows_tracker_npc|
  knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2,
  0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
["npc2","Rikiar Agila","Rikiar", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
  [
  itm_pistol_ammo,
  itm_vitzland_pistol,
  
  ]+companion_gear,
  str_7|agi_7|int_11|cha_6|level(1),wp_m(40),knows_merchant_npc|
  knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
  0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
["npc3","Gesgehe Dobega","Gesgehe",tf_woman|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
  [
  itm_hooded_cloak_1,
  ]+companion_gear,
  str_6|agi_9|int_11|cha_6|level(1),wp_m(20),knows_merchant_npc|
  knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
  0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
["npc4","Sir Hilmont Tranthem","Hilmont",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
  [
  itm_entenaii_uniform_parade,
  ]+companion_gear,
  str_10|agi_9|int_13|cha_10|level(10),wp_m(110),knows_warrior_npc|
  knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
  0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
["npc5","Yilmazok Emin","Yilmazok",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
  [
  itm_arrows,
  itm_arrows,
  
  itm_recurve_bow,   
  
  itm_kukri_old,  

  itm_yanizar_uniform_1,
  
  itm_yanizar_helmet_1,
  
  itm_leather_gloves,
  ],
  str_9|agi_9|int_12|cha_7|level(5),wp_m(90),knows_warrior_npc|
  knows_riding_2|knows_horse_archery_3|knows_power_draw_5|knows_leadership_2|knows_weapon_master_1,
  0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
["npc6","Giotto Fiocarda","Giotto",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
  [
  itm_republican_infantry_helmet,
  itm_ammo_belt_3,
  ]+companion_gear,
  str_10|agi_12|int_10|cha_5|level(6),wp_m(105),knows_warrior_npc|
  knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
["npc7","Xetina Gaciala","Xetina",tf_woman|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
  []+companion_gear,
  str_8|agi_9|int_10|cha_6|level(2),wp_m(80),knows_tracker_npc|
  knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
  0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
#kk4ever2000 custom companion
["npc8","Grigori","Grigori",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
  [
  itm_rifle_ammo,
  
  itm_molvat_bolt_action_rifle,
  
  itm_hatchet,
  
  itm_union_civ_2,
  
  itm_hood_brown_gasmask,
  
  itm_cloak_7,
  ],
  str_11|agi_12|int_8|cha_8|level(7),wp_m(150),knows_warrior_npc|
  knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_tactics_1,
  0x000000073f01f19866db2642648ab4ac00000000001f3ba40000000000000000],
#
["npc9","Galgalliel Abaoz","Galgalliel",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
  [
  itm_straw_hat_1,

  ]+companion_gear,
  str_11|agi_8|int_7|cha_8|level(2),wp_m(100),knows_warrior_npc|
  knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
  0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
["npc10","Hamonet, le Chasseu","Hamonet",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
  []+companion_gear,
  str_12|agi_8|int_9|cha_11|level(9),wp_m(105),knows_warrior_npc|
  knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
  0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
["npc11","Kakerine Rostav","Kakerine",tf_woman|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
  [
  itm_sharpened_stick,
  itm_union_coif,
  ]+companion_gear,
  str_8|agi_11|int_10|cha_10|level(8),wp_m(70),knows_merchant_npc|
  knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
  0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
#Nerzhul/Whiteling custom companion
["npc12","Renfield","Renfield",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
  [
  itm_renfield_suit,
  
  itm_renfield_glasses,
  
  itm_renfieldgauntlet,
  ],
  str_9|agi_7|int_17|cha_3|level(7),wp_m(120),   knows_merchant_npc|
  knows_ironflesh_1|knows_power_strike_1|knows_tracking_2|knows_engineer_4|knows_pathfinding_6,
  0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
#
["npc13","Aulus Volcatius Valgus","Aulus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
  [
  itm_scale_gauntlets,
  ]+companion_gear,
  str_7|agi_7|int_12|cha_8|level(3),wp_m(80),knows_warrior_npc|
  knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
  0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
["npc14","Philbert Jethro Askew","Philbert",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
  [
  itm_entenaii_gloves,
  ]+companion_gear,
  str_9|agi_8|int_11|cha_8|level(5),wp_m(100),knows_warrior_npc|
  knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
  0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
["npc15","Vorigan","Vorigan",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
  []+companion_gear,
  str_9|agi_9|int_12|cha_8|level(7),wp_m(80),knows_warrior_npc|
  knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
  0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
["npc16","Mide Ui Braoin","Mide",tf_woman|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
  [
  itm_cloak_7,
  itm_ornate_seax,
  itm_throwing_spears,
  
  itm_bandit_hood_blu_scarf,
  ]+companion_gear,
  str_7|agi_11|int_8|cha_7|level(2),wp_m(80),knows_tracker_npc|
  knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
  0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],
#NPC system changes end
## Alayen = Galgalliel Abaoz
## Artimenner = Vorigan
## Bashestur = Yilmazok Emin
## Borcha = Declan Mac Fheargail
## Bunduk = Hamonet, le Chasseu
## Deshavi = Xetina
## Firentis = Giotto Fiocarda
## Jeremus = Brouprix the Resurrector
## Katrin = Kakerine Rostav
## Klethi = Mide Ui Braoin
## Lezalit = Philbert Jethro Askew
## Marnid = Rikiar Agila
## Matheld = Tomasia Bassadoar
## Nizar = Aulus Volcatius Valgus
## Rolf = Sir Hilmont Tranthem
## Ymira = Gesgehe Dobega

##################################################################################################
#Faction Leaders
##################################################################################################
##Entenaii Empire
["kingdom_1_lord","Emperor Qillian","Qillian",tf_hero, 0,reserved,  fac_kingdom_1,
  [
  (itm_empire_revolver, imod_masterwork),
  (itm_pistol_ammo_4_pw, imod_large_bag),
  (itm_pistol_ammo_4_pw, imod_large_bag),
  
  (itm_trooper_sword, imod_balanced),
  
  itm_entenaii_armour_emperor,
  itm_entenaii_uniform_emperor,
  
  itm_entenaii_helmet_emperor,

  itm_entenaii_emperor_gauntlets,
  
  itm_cloak_emperor,
  ],
  king_attrib,wp_r(320),king_skills, 0x000000001c00102037d28dbb2b7136cb00000000001f6ad60000000000000000,swadian_face_young_1],
##Entenaii Dominion
["kingdom_2_lord","Governor-General Rosthaim","Rosthaim",  tf_hero, 0,reserved,  fac_kingdom_2,
  [
  (itm_dominion_shotgun, imod_masterwork),
  (itm_flameshot_ammo_pw, imod_large_bag),
  (itm_flameshot_ammo_pw, imod_large_bag),
  (itm_fanatic_staff, imod_balanced),
  
  (itm_dominion_armour_officer, imod_reinforced),
  (itm_dominion_uniform_officer, imod_reinforced),

  itm_dominion_governer_general_helmet,
  
  itm_dominion_governer_general_gauntlets,
  
  (itm_ammo_belt_1, imod_reinforced),
  ],
  king_attrib,wp_r(300),king_skills, 0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000, vaegir_face_old_2],
##Kingdom of Galvae
["kingdom_3_lord","King Seafra O Ceanndubhain","Seafra",  tf_hero, 0,reserved,  fac_kingdom_3,
  [
  (itm_galvae_lmg, imod_masterwork),
  (itm_mg_ammo_pw, imod_large_bag),
  (itm_galvae_shield_10, imod_reinforced),
  (itm_ornate_seax, imod_balanced),
  (itm_galvae_armour_officer, imod_reinforced),
  (itm_galvae_uniform_officer, imod_reinforced),
  
  itm_galvae_royal_helmet,

  itm_galvae_royal_gauntlets,
  
  itm_cloak_royal,
  ],
  king_attrib,wp_r(320),king_skills, 0x0000000cee0051cc44be2d14d370c65c00000000001ed6df0000000000000000,khergit_face_old_2],
##Molvat-Berchav Union
["kingdom_4_lord","Tzar Molvat","Molvat",  tf_hero, 0,reserved,  fac_kingdom_4,
  [
  (itm_molvat_assault_rifle, imod_masterwork),
  (itm_rifle_ammo_pw, imod_large_bag),
  (itm_rifle_ammo_pw, imod_large_bag),
  (itm_shashka, imod_balanced),
  
  (itm_union_armour_officer, imod_reinforced),
  (itm_union_uniform_officer, imod_reinforced),
  
  itm_union_tzar_helmet,

  itm_union_tzar_gauntlets,
  
  (itm_ammo_belt_1, imod_reinforced),
  ],
  king_attrib,wp_r(300),king_skills, 0x0000000e2c0c028a068e8c18557b12a500000000001c0fe80000000000000000, nord_face_older_2],
##Vitzland Territories
["kingdom_5_lord","Kaiser Von Ustabier","Ustabier",  tf_hero, 0,reserved,  fac_kingdom_5,
  [
  (itm_vitzland_smg, imod_masterwork),
  (itm_pistol_ammo_4_pw, imod_large_bag),
  (itm_pistol_ammo_4_pw, imod_large_bag),
  (itm_trooper_sword, imod_balanced),
  (itm_vitzland_armour_officer, imod_reinforced),
  (itm_vitzland_uniform_officer, imod_reinforced),
  
  itm_vitzland_kaiser_salet,

  itm_vitzland_kaiser_gauntlets,
  
  (itm_ammo_belt_1, imod_reinforced),
  ],
  king_attrib,wp_r(320),king_skills, 0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000, rhodok_face_old_2],
##Trezzo Republic
["kingdom_6_lord","Doge Volsoron","Volsoron",  tf_hero, 0,reserved,  fac_kingdom_6,
  [
  (itm_trezzo_smg, imod_masterwork),
  (itm_pistol_ammo_4_pw, imod_large_bag),
  (itm_pistol_ammo_4_pw, imod_large_bag),

  itm_doge_rapier,
  
  (itm_republican_uniform_officer, imod_reinforced),
  
  itm_republican_armour_doge,
  
  itm_republican_doge_helmet,
  
  itm_republican_doge_gauntlets,
  
  (itm_ammo_belt_1, imod_reinforced),
  ],
  king_attrib,wp_r(320),king_skills, 0x0000000a4b103354189c71d6d386e8ac00000000001e24eb0000000000000000, rhodok_face_old_2],
##Itami Castedom
["kingdom_7_lord","Kytra Inu-do","Inu-do",  tf_hero, 0,reserved,  fac_kingdom_7,
  [
  (itm_trezzo_smg, imod_masterwork),
  (itm_pistol_ammo_4_pw, imod_large_bag),
  (itm_pistol_ammo_4_pw, imod_large_bag),

  itm_doge_rapier,
  
  (itm_republican_uniform_officer, imod_reinforced),
  
  itm_republican_armour_doge,
  
  itm_itami_kytra_helmet,
  
  itm_republican_doge_gauntlets,
  
  (itm_ammo_belt_1, imod_reinforced),
  ],
  king_attrib,wp_r(320),king_skills, 0x0000000a4b103354189c71d6d386e8ac00000000001e24eb0000000000000000, rhodok_face_old_2],
#irregulars
["irregulars_lord","Leader Tredas","Tredas",  tf_hero, 0,reserved,  fac_irregulars,
  [
  (itm_irregular_smg_2, imod_masterwork),
  (itm_pistol_ammo_pw, imod_large_bag),
  (itm_pistol_ammo_pw, imod_large_bag),
  (itm_lowlander_sword, imod_balanced),
  
  itm_irregular_armour_leader,
  itm_irregular_uniform_leader,

  itm_irregular_leader_helmet,
  
  itm_irregular_leader_gauntlets,
  
  (itm_ammo_belt_1, imod_reinforced),
  ],
  king_attrib,wp_r(300),king_skills, 0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000, vaegir_face_old_2],
#Throd
["throd_lord","Throd","Throd",  tf_hero, 0,reserved,  fac_theocracy,
  [
  (itm_grenade_miasma, imod_large_bag),
  (itm_grenade_miasma, imod_large_bag),
  (itm_grenade_miasma, imod_large_bag),
  (itm_warhammer, imod_balanced),
  
  (itm_throd_shield, imod_reinforced),
  
  (itm_throd_robe_god, imod_reinforced),
  (itm_throd_robe_purple, imod_reinforced),

  (itm_throd_helmet_black, imod_reinforced),
  
  (itm_throd_gauntlets, imod_reinforced),
  ],
  king_attrib,wp_r(300),king_skills, 0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000, vaegir_face_old_2],
#

###################
##Faction Members##
###################
##Entenaii Empire
["knight_1_1", "Yeneral Marvin McKerras", "Marvin", tf_hero, 0, reserved,  fac_kingdom_1,
  [
  (itm_entenaii_beret, imod_lordly),
  (itm_ironclub, imod_masterwork),
  
  itm_entenaii_uniform_yeneral,
  ]+entenaii_lord_gear,
  lord_attrib,wp_m(330),lord_skills,0x0000000c3e08601414ab4dc6e39296b200000000001e231b0000000000000000, swadian_face_older_2],
["knight_1_2", "Volonel Warner Moore", "Warner", tf_hero, 0, reserved,  fac_kingdom_1,
  []+entenaii_lord_gear,
  lord_attrib,wp_m(340),lord_skills, 0x0000000c0f0c320627627238dcd6599400000000001c573d0000000000000000, swadian_face_young_2],
["knight_1_3", "Volonel Byron Wheeler", "Byron", tf_hero, 0, reserved,  fac_kingdom_1,
  []+entenaii_lord_gear,
  lord_attrib,wp_m(360),lord_skills, 0x0000000cb700210214ce89db276aa2f400000000001d36730000000000000000, swadian_face_young_2],
["knight_1_4", "Volonel Dominic Casey", "Dominic", tf_hero, 0, reserved,  fac_kingdom_1,
  []+entenaii_lord_gear,
  lord_attrib,wp_m(280),lord_skills, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000, swadian_face_older_2],
["knight_1_5", "Volonel Edmond Powlett", "Edmond", tf_hero, 0, reserved,  fac_kingdom_1,
  [
  (itm_entenaii_uniform_officer, imod_lordly),
  ]+entenaii_lord_gear,
  lord_attrib,wp_m(300),lord_skills, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000, swadian_face_older_2],
["knight_1_6", "Volonel Emmet Meredeth", "Emmet", tf_hero, 0, reserved,  fac_kingdom_1,
  []+entenaii_lord_gear,
  lord_attrib,wp_m(340),lord_skills, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000, swadian_face_older_2],
["knight_1_7", "Volonel Alfred Xavier", "Alfred", tf_hero, 0, reserved,  fac_kingdom_1,
  []+entenaii_lord_gear,
  lord_attrib,wp_m(390),lord_skills, 0x0000000c1e001500589dae4094aa291c00000000001e37a80000000000000000, swadian_face_young_2],
["knight_1_8", "Volonel Burrell Grain", "Burrell", tf_hero, 0, reserved,  fac_kingdom_1,
  []+entenaii_lord_gear,
  lord_attrib,wp_m(350),lord_skills, 0x0000000c330855054aa9aa431a48d74600000000001ed5240000000000000000, swadian_face_older_2],
["knight_1_9", "Volonel Hobson Delagney", "Hobson", tf_hero, 0, reserved,  fac_kingdom_1,
  []+entenaii_lord_gear,
  lord_attrib,wp_m(260),lord_skills, 0x0000000c0f08000458739a9a1476199800000000001fb6f10000000000000000, swadian_face_old_2],
["knight_1_10", "Volonel Arlie Fitzgerald", "Arlie", tf_hero, 0, reserved,  fac_kingdom_1,
  []+entenaii_lord_gear,
  lord_attrib,wp_m(290),lord_skills, 0x0000000c0610351048e325361d7236cd00000000001d532a0000000000000000, swadian_face_older_2],
["knight_1_11", "Volonel Maurice Foster", "Maurice", tf_hero, 0, reserved,  fac_kingdom_1,
  []+entenaii_lord_gear,
  lord_attrib,wp(220),lord_skills, 0x0000000c03104490280a8cb2a24196ab00000000001eb4dc0000000000000000, swadian_face_older_2],
["knight_1_12", "Volonel Ulysses Drogace", "Ulysses", tf_hero, 0, reserved,  fac_kingdom_1,
  []+entenaii_lord_gear,
  lord_attrib,wp(130),lord_skills, 0x0000000c2a0805442b2c6cc98c8dbaac00000000001d389b0000000000000000, swadian_face_older_2],
["knight_1_13", "Volonel Wilford Buckman", "Wilford", tf_hero, 0, reserved,  fac_kingdom_1,
  []+entenaii_lord_gear,
  lord_attrib,wp(160),lord_skills, 0x0000000c380c30c2392a8e5322a5392c00000000001e5c620000000000000000, swadian_face_older_2],
["knight_1_14", "Volonel Duncan Learmonth", "Duncan", tf_hero, 0, reserved,  fac_kingdom_1,
  []+entenaii_lord_gear,
  lord_attrib,wp(190),lord_skills, 0x0000000c3f10000532d45203954e192200000000001e47630000000000000000, swadian_face_older_2],
["knight_1_15", "Volonel Hoyt Oshea", "Hoyt", tf_hero, 0, reserved,  fac_kingdom_1,
  []+entenaii_lord_gear,
  lord_attrib,wp(140),lord_skills, 0x0000000c5c0840034895654c9b660c5d00000000001e34530000000000000000, swadian_face_young_2],
["knight_1_16", "Volonel Dorsey Bain", "Dorsey", tf_hero, 0, reserved,  fac_kingdom_1,
  [
  itm_arrows,
  itm_arrows,
  itm_long_bow,
  itm_scottish_claymore,
  itm_cloak_5,
  ]+entenaii_lord_gear,
  lord_attrib,wp(130),lord_skills, 0x000000095108144657a1ba3ad456e8cb00000000001e325a0000000000000000, swadian_face_young_2],
["knight_1_17", "Volonel Hillard Carnall", "Hillard", tf_hero, 0, reserved,  fac_kingdom_1,
  [
  (itm_entenaii_uniform_officer, imod_lordly),
  ]+entenaii_lord_gear,
  lord_attrib,wp(190),lord_skills, 0x0000000c010c42c14d9d6918bdb336e200000000001dd6a30000000000000000, swadian_face_young_2],
["knight_1_18", "Volonel Jerome Thompson", "Jerome", tf_hero, 0, reserved,  fac_kingdom_1,
  []+entenaii_lord_gear,
  lord_attrib,wp(210),lord_skills, 0x0000000c150045c6365d8565932a8d6400000000001ec6940000000000000000, swadian_face_young_2],
["knight_1_19", "Volonel Hermon Cochran", "Hermon", tf_hero, 0, reserved,  fac_kingdom_1,
  []+entenaii_lord_gear,  
  lord_attrib,wp(120),lord_skills, 0x00000008200012033d9b6d4a92ada53500000000001cc1180000000000000000, swadian_face_young_2],
["knight_1_20", "Volonel Elmer Hunniford", "Elmer", tf_hero, 0, reserved,  fac_kingdom_1,
  [
  (itm_entenaii_uniform_officer, imod_lordly),
  ]+entenaii_lord_gear,  
  lord_attrib,wp(150),lord_skills, 0x0000000c4d0840d24a9b2ab4ac2a332400000000001d34db0000000000000000, swadian_face_young_2],

##Entenaii Dominion
["knight_2_1", "Cleric-At-Arms Norman Crayford", "Norman", tf_hero, 0, reserved,  fac_kingdom_2,
  [
  (itm_fanatic_staff, imod_balanced),
  (itm_dominion_uniform_fanatic_noble, imod_lordly),
  (itm_dominion_fanatic_noble_mitre, imod_lordly),
  ]+dominion_lord_gear,
  lord_attrib,wp_m(230),lord_skills, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
["knight_2_2", "Psu-volonel Cornelius Pembroke", "Cornelius", tf_hero, 0, reserved,  fac_kingdom_2,
  []+dominion_lord_gear,
  lord_attrib,wp_m(260),lord_skills, 0x0000000c2a0015d249b68b46a98e176400000000001d95a40000000000000000, vaegir_face_old_2],
["knight_2_3", "Psu-volonel Jim Paulson", "Jim", tf_hero, 0, reserved,  fac_kingdom_2,
  []+dominion_lord_gear,
  lord_attrib,wp_m(290),lord_skills, 0x0000000c131031c546a38a2765b4c86000000000001e58d30000000000000000, vaegir_face_older_2],
["knight_2_4", "Psu-volonel Myer Bodkin", "Myer", tf_hero, 0, reserved,  fac_kingdom_2,
  []+dominion_lord_gear,
  lord_attrib,wp_m(320),lord_skills, 0x0000000c2f0832c748f272540d8ab65900000000001d34e60000000000000000, vaegir_face_older_2],
["knight_2_5", "Psu-volonel Terence Herridge", "Terence", tf_hero, 0, reserved,  fac_kingdom_2,
  []+dominion_lord_gear,
  lord_attrib,wp_m(350),lord_skills, 0x0000000e310061435d76bb5f55bad9ad00000000001ed8ec0000000000000000, vaegir_face_older_2],
["knight_2_6", "Psu-volonel Edwin Ellingham", "Edwin", tf_hero, 0, reserved,  fac_kingdom_2,
  [
  itm_dominion_armour_officer,
  ]+dominion_lord_gear,
  lord_attrib,wp_m(230),lord_skills, 0x0000000a0100421038da7157aa4e430a00000000001da8bc0000000000000000, vaegir_face_middle_2],
["knight_2_7", "Psu-volonel John Thomas", "John", tf_hero, 0, reserved,  fac_kingdom_2,
  []+dominion_lord_gear,
  lord_attrib,wp_m(260),lord_skills, 0x0000000c04100153335ba9390b2d277500000000001d89120000000000000000, vaegir_face_old_2],
["knight_2_8", "Psu-volonel Griffith Kestle", "Griffith", tf_hero, 0, reserved,  fac_kingdom_2,
  [
  (itm_fanatic_staff, imod_balanced),
  
  (itm_dominion_uniform_fanatic_officer_2, imod_lordly),
  ]+dominion_lord_gear,
  lord_attrib,wp_m(300),lord_skills, 0x0000000c00046581234e8da2cdd248db00000000001f569c0000000000000000, vaegir_face_older_2],
["knight_2_9", "Psu-volonel Clarence Nicholls", "Clarence", tf_hero, 0, reserved,  fac_kingdom_2,
  []+dominion_lord_gear,
  lord_attrib,wp_m(330),lord_skills, 0x0000000c160451d2136469c4d9b159ad00000000001e28f10000000000000000, vaegir_face_older_2],
["knight_2_10", "Psu-volonel Clifford Pardey", "Clifford", tf_hero, 0, reserved,  fac_kingdom_2,
  []+dominion_lord_gear,
  lord_attrib,wp_m(360),lord_skills, 0x0000000f7c00520e66b76edd5cd5eb6e00000000001f691e0000000000000000, vaegir_face_older_2],
["knight_2_11", "Psu-volonel Elias Gamblin", "Elias", tf_hero, 0, reserved,  fac_kingdom_2,
  []+dominion_lord_gear,
  lord_attrib,wp(130),lord_skills, 0x0000000c1d0821d236acd6991b74d69d00000000001e476c0000000000000000, vaegir_face_middle_2],
["knight_2_12", "Psu-volonel Allen Bunker", "Allen", tf_hero, 0, reserved,  fac_kingdom_2,
  []+dominion_lord_gear,
  lord_attrib,wp(170),lord_skills, 0x0000000c0f04024b2509d5d53944c6a300000000001d5b320000000000000000, vaegir_face_old_2],
["knight_2_13", "Psu-volonel Rowland Gambrill", "Rowland", tf_hero, 0, reserved,  fac_kingdom_2,
  []+dominion_lord_gear,
  lord_attrib,wp(190),lord_skills, 0x0000000c680432d3392230cb926d56ca00000000001da69b0000000000000000, vaegir_face_older_2],
["knight_2_14", "Psu-volonel Idris Searson", "Idris", tf_hero, 0, reserved,  fac_kingdom_2,
  []+dominion_lord_gear,
  lord_attrib,wp(220),lord_skills, 0x0000000c27046000471bd2e93375b52c00000000001dd5220000000000000000, vaegir_face_older_2],
["knight_2_15", "Psu-volonel Rees Lobb", "Rees", tf_hero, 0, reserved,  fac_kingdom_2,
  []+dominion_lord_gear,
  lord_attrib,wp(250),lord_skills, 0x0000000de50052123b6bb36de5d6eb7400000000001dd72c0000000000000000, vaegir_face_older_2],
["knight_2_16", "Psu-volonel Howard Collins", "Howard", tf_hero, 0, reserved,  fac_kingdom_2,
  [
  itm_dominion_uniform_fanatic_noble,
  ]+dominion_lord_gear,
  lord_attrib,wp(120),lord_skills, 0x000000085f00000539233512e287391d00000000001db7200000000000000000, vaegir_face_middle_2],
["knight_2_17", "Psu-volonel Moses Pemble", "Moses", tf_hero, 0, reserved,  fac_kingdom_2,
  []+dominion_lord_gear,
  lord_attrib,wp(150),lord_skills, 0x0000000a070c4387374bd19addd2a4ab00000000001e32cc0000000000000000, vaegir_face_old_2],
["knight_2_18", "Psu-volonel Joe Emerton", "Joe", tf_hero, 0, reserved,  fac_kingdom_2,
  []+dominion_lord_gear,
  lord_attrib,wp(180),lord_skills, 0x0000000b670012c23d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_older_2],
["knight_2_19", "Psu-volonel Murdo Giles", "Murdo", tf_hero, 0, reserved,  fac_kingdom_2,
  [
  itm_scale_gauntlets,
  ]+dominion_lord_gear,
  lord_attrib,wp(210),lord_skills, 0x0000000e070050853b0a6e4994ae272a00000000001db4e10000000000000000, vaegir_face_older_2],
["knight_2_20", "Psu-volonel Tom Rick", "Tom", tf_hero, 0, reserved,  fac_kingdom_2,
  []+dominion_lord_gear,
  lord_attrib,wp(240),lord_skills, 0x0000000f800021c63b0a6e4994ae272a00000000001db4e10000000000000000, vaegir_face_older_2],

##Kingdom of Galvae
["knight_3_1", "Prince Ardghal O Ceanndubhain", "Ardghal", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  (itm_scottish_claymore, imod_masterwork),
  itm_cloak_royal,
  ]+galvae_lord_gear,
  lord_attrib,wp_m(230),lord_skills|knows_trainer_3|knows_power_draw_4, 0x000000043000318b54b246b7094dc39c00000000001d31270000000000000000, khergit_face_middle_2],
["knight_3_2", "Lort Maolmordha Mac Phoil",  "Maolmordha", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_cloak_noble_2,
  ]+galvae_lord_gear,
  lord_attrib,wp_m(260),lord_skills|knows_power_draw_4, 0x0000000c280461004929b334ad632aa200000000001e05120000000000000000, khergit_face_old_2],
["knight_3_3", "Lort Molua O Forannain",  "Molua", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_cloak_noble_3,
  ]+galvae_lord_gear,
  lord_attrib,wp_m(290),lord_skills|knows_trainer_5|knows_power_draw_4, 0x0000000e880062c53b0a6e4994ae272a00000000001db4e10000000000000000, khergit_face_older_2],
["knight_3_4", "Lort Aoidhghean O Connagain", "Aoidhghean", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_buckshot_ammo_pw,
  itm_galvae_shotgun,
  
  itm_cloak_noble_4,
  ]+galvae_lord_gear,
  lord_attrib,wp_m(320),lord_skills|knows_power_draw_4, 0x0000000c23085386391b5ac72a96d95c00000000001e37230000000000000000, khergit_face_older_2],
["knight_3_5", "Lort Fiacha O Raighne",  "Fiacha", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_cloak_noble_5,
  ]+galvae_lord_gear,
  lord_attrib,wp_m(350),lord_skills|knows_power_draw_4, 0x0000000efe0051ca4b377b4964b6eb6500000000001f696c0000000000000000, khergit_face_older_2],
["knight_3_6", "Lort Brandubh Mac Maolain", "Brandubh", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_cloak_noble_6,
  ]+galvae_lord_gear,
  lord_attrib,wp_m(230),lord_skills|knows_power_draw_4, 0x00000006f600418b54b246b7094dc31a00000000001d37270000000000000000, khergit_face_middle_2],
["knight_3_7", "Lort Greagoir O Caoimh","Greagoir", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_cloak_noble_7,
  ]+galvae_lord_gear,
  lord_attrib,wp_m(260),lord_skills|knows_power_draw_4, 0x0000000bdd00510a44be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_old_2],
["knight_3_8", "Lort Daimhin O Peatain", "Daimhin", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_galvae_uniform_cavalry,
  itm_cloak_noble_8,
  ]+galvae_lord_gear,
  lord_attrib,wp_m(290),lord_skills|knows_power_draw_4, 0x0000000abc00518b5af4ab4b9c8e596400000000001dc76d0000000000000000, khergit_face_older_2],
["knight_3_9", "Lort Cianan O hIarfhlatha","Cianan", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_cloak_noble_9,
  ]+galvae_lord_gear,
  lord_attrib,wp_m(320),lord_skills|knows_power_draw_4, 0x0000000a180441c921a30ea68b54971500000000001e54db0000000000000000, khergit_face_older_2],
["knight_3_10", "Lort Daibhi O hIonmhaineain","Daibhi", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_cloak_noble_10,
  ]+galvae_lord_gear,
  lord_attrib,wp_m(350),lord_skills|knows_trainer_6|knows_power_draw_4, 0x0000000a3b00418c5b36c686d920a76100000000001c436f0000000000000000, khergit_face_older_2],
["knight_3_11", "Raicleach Ailin Mac Labhrainn", "Ailin", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  (itm_galvae_mask_knight, imod_lordly),
  itm_cloak_noble_11,
  ]+galvae_lord_gear,
  lord_attrib,wp(150),lord_skills|knows_power_draw_4, 0x00000007d100534b44962d14d370c65c00000000001ed6df0000000000000000, khergit_face_middle_2],
["knight_3_12", "Lort Cruimin Mac Adaim", "Cruimin", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_galvae_armour_officer,
  itm_cloak_noble_12,
  ]+galvae_lord_gear,
  lord_attrib,wp(190),lord_skills|knows_power_draw_4, 0x0000000bf400610c5b33d3c9258edb6c00000000001eb96d0000000000000000, khergit_face_old_2],
["knight_3_13", "Lort Bearchan O Ceanndubhain","Bearchan", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_cloak_noble_13,
  ]+galvae_lord_gear,
  lord_attrib,wp(200),lord_skills|knows_trainer_3|knows_power_draw_4, 0x0000000bfd0061c65b6eb33b25d2591d00000000001f58eb0000000000000000, khergit_face_older_2],
["knight_3_14", "Lort Beircheart Mac Raghnaill",  "Beircheart", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_cloak_noble_14,
  ]+galvae_lord_gear,
  lord_attrib,wp(300),lord_skills|knows_trainer_6|knows_power_draw_4, 0x0000000b6900514144be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_older_2],
["knight_3_15", "Lort Amalgith O Fearghuis", "Amalgith", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_cloak_noble_15,
  ]+galvae_lord_gear,
  lord_attrib,wp(240),lord_skills|knows_trainer_4|knows_power_draw_4, 0x0000000c360c524b6454465b59b9d93500000000001ea4860000000000000000, khergit_face_older_2],
["knight_3_16", "Lort Dabhog O hinreachtaigh","Dabhog", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_galvae_mask_helmet,
  
  itm_cloak_noble_1,
  ]+galvae_lord_gear,
  lord_attrib,wp(120),lord_skills|knows_power_draw_4, 0x0000000c350c418438ab85b75c61b8d300000000001d21530000000000000000, khergit_face_middle_2],
["knight_3_17", "Lort Aoidhghean O Hainbheain", "Aoidhghean", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_galvae_armour_cavalry,
  itm_cloak_noble_1,
  ]+galvae_lord_gear,
  lord_attrib,wp(150),lord_skills|knows_power_draw_4, 0x0000000c3c0821c647264ab6e68dc4d500000000001e42590000000000000000, khergit_face_old_2],
["knight_3_18", "Lort Gearoid O hAinle", "Gearoid", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_cloak_noble_1,
  ]+galvae_lord_gear,
  lord_attrib,wp(180),lord_skills|knows_trainer_4|knows_power_draw_4, 0x0000000c0810500347ae7acd0d3ad74a00000000001e289a0000000000000000, khergit_face_older_2],
["knight_3_19", "Lort Ainmire Mac Braonain","Ainmire", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_cloak_noble_1,
  ]+galvae_lord_gear,
  lord_attrib,wp(210),lord_skills|knows_trainer_5|knows_power_draw_4, 0x0000000c1500510528f50d52d20b152300000000001d66db0000000000000000, khergit_face_older_2],
["knight_3_20", "Lort Faolan O Conchuir","Faolan", tf_hero, 0, reserved,  fac_kingdom_3,
  [
  itm_cloak_noble_1,
  ]+galvae_lord_gear,
  lord_attrib,wp(240),lord_skills|knows_power_draw_4, 0x0000000f7800620d66b76edd5cd5eb6e00000000001f691e0000000000000000, khergit_face_older_2],

##Molvat-Berchav Union
["knight_4_1", "Tzarevich Srecko Pejakovski", "Srecko", tf_hero, 0, reserved,  fac_kingdom_4,
  [
  (itm_union_armour_brotherhood, imod_lordly),
  (itm_ravensbeak, imod_masterwork),
  ]+union_lord_gear,
  lord_attrib,wp_m(230),lord_skills, 0x0000000c13002254340eb1d91159392d00000000001eb75a0000000000000000, nord_face_middle_2],
["knight_4_2", "Pokovniz Sreten Lalic", "Sreten", tf_hero, 0, reserved,  fac_kingdom_4,
  []+union_lord_gear,
  lord_attrib,wp_m(260),lord_skills|knows_trainer_3, 0x0000000c1610218368e29744e9a5985b00000000001db2a10000000000000000, nord_face_old_2],
["knight_4_3", "Pokovniz Sergej Mandic", "Sergej", tf_hero, 0, reserved,  fac_kingdom_4,
  [
  (itm_union_armour_brotherhood, imod_lordly),
  ]+union_lord_gear,
  lord_attrib,wp_m(290),lord_skills, 0x0000000c03040289245a314b744b30a400000000001eb2a90000000000000000, nord_face_older_2],
["knight_4_4", "Pokovniz Jezdimir Urosevic", "Jezdimir", tf_hero, 0, reserved,  fac_kingdom_4,
  []+union_lord_gear,
  lord_attrib,wp_m(310),lord_skills, 0x0000000c3f1001ca3d6955b26a8939a300000000001e39b60000000000000000, nord_face_older_2],
["knight_4_5", "Pokovniz Vlada Markovic", "Vlada", tf_hero, 0, reserved,  fac_kingdom_4,
  []+union_lord_gear,
  lord_attrib,wp_m(350),lord_skills, 0x0000000ff508330546dc4a59422d450c00000000001e51340000000000000000, nord_face_older_2],
["knight_4_6", "Pokovniz Rasko Nestorovski", "Rasko", tf_hero, 0, reserved,  fac_kingdom_4,
  []+union_lord_gear,
  lord_attrib,wp_m(230),lord_skills, 0x00000005b00011813d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_middle_2],
["knight_4_7", "Pokovniz Stefan Brkic", "Stefan", tf_hero, 0, reserved,  fac_kingdom_4,
  [
  itm_scale_gauntlets,
  ]+union_lord_gear,
  lord_attrib,wp_m(260),lord_skills|knows_trainer_4, 0x00000006690002873d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_old_2],
["knight_4_8", "Pokovniz Uros Zivanovic", "Uros", tf_hero, 0, reserved,  fac_kingdom_4,
  [
  (itm_union_armour_brotherhood, imod_lordly),
  ]+union_lord_gear,
  lord_attrib,wp_m(290),lord_skills, 0x0000000f830051c53b026e4994ae272a00000000001db4e10000000000000000, nord_face_older_2],
["knight_4_9", "Pokovniz Ljubisa Vlahovic", "Ljubisa", tf_hero, 0, reserved,  fac_kingdom_4,
  []+union_lord_gear,
  lord_attrib,wp_m(320),lord_skills|knows_trainer_5|knows_power_draw_4, 0x00000000080c54c1345bd21349b1b67300000000001c90c80000000000000000, nord_face_older_2],
["knight_4_10", "Pokovniz Svetislav Darkovic", "Svetislav", tf_hero, 0, reserved,  fac_kingdom_4,
  []+union_lord_gear,
  lord_attrib,wp_m(350),lord_skills|knows_trainer_6, 0x000000084b0002063d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_older_2],
["knight_4_11", "Pokovniz Sinisa Zivic", "Sinisa", tf_hero, 0, reserved,  fac_kingdom_4,
  [
  itm_union_uniform_officer,
  ]+union_lord_gear,
  lord_attrib,wp(140),lord_skills, 0x000000002d100005471d4ae69ccacb1d00000000001dca550000000000000000, nord_face_middle_2],
["knight_4_12", "Pokovniz Radisa Stefanovic", "Radisa", tf_hero, 0, reserved,  fac_kingdom_4,
  []+union_lord_gear,
  lord_attrib,wp(200),lord_skills, 0x0000000b9500020824936cc51cb5bb2500000000001dd4d80000000000000000, nord_face_old_2],
["knight_4_13", "Pokovniz Doko Pap", "Doko", tf_hero, 0, reserved,  fac_kingdom_4,
  []+union_lord_gear,
  lord_attrib,wp(250),lord_skills|knows_trainer_3, 0x0000000a300012c439233512e287391d00000000001db7200000000000000000, nord_face_older_2],
["knight_4_14", "Pokovniz Borislav Borisavljevic", "Borislav", tf_hero, 0, reserved,  fac_kingdom_4,
  [
  itm_union_armour_officer,
  ]+union_lord_gear,
  lord_attrib,wp(200),lord_skills, 0x0000000c0700414f2cb6aa36ea50a69d00000000001dc55c0000000000000000, nord_face_older_2],
["knight_4_15", "Pokovniz Slavisa Vladic", "Slavisa", tf_hero, 0, reserved,  fac_kingdom_4,
  []+union_lord_gear,
  lord_attrib,wp(290),lord_skills|knows_trainer_6, 0x0000000d920801831715d1aa9221372300000000001ec6630000000000000000, nord_face_older_2],
["knight_4_16", "Pokovniz Kuzman Vujic", "Kuzman", tf_hero, 0, reserved,  fac_kingdom_4,
  [
  itm_bandit_fullhelm2,
  ]+union_lord_gear,
  lord_attrib,wp(120),lord_skills, 0x000000099700124239233512e287391d00000000001db7200000000000000000, nord_face_middle_2],
["knight_4_17", "Pokovniz Neven Velimirovic", "Neven", tf_hero, 0, reserved,  fac_kingdom_4,
  [
  itm_union_armour_brotherhood,
  ]+union_lord_gear,
  lord_attrib,wp(150),lord_skills|knows_trainer_4, 0x0000000c2f0442036d232a2324b5b81400000000001e55630000000000000000, nord_face_old_2],
["knight_4_18", "Pokovniz Stracimir Markovic", "Stracimir", tf_hero, 0, reserved,  fac_kingdom_4,
  [
  itm_union_uniform_officer,
  ]+union_lord_gear,
  lord_attrib,wp(180),lord_skills, 0x0000000c0d00118866e22e3d9735a72600000000001eacad0000000000000000, nord_face_older_2],
["knight_4_19", "Pokovniz Goran Stevanovic", "Goran", tf_hero, 0, reserved,  fac_kingdom_4,
  []+union_lord_gear,
  lord_attrib,wp(210),lord_skills|knows_trainer_5, 0x0000000c0308225124e26d4a6295965a00000000001d23e40000000000000000, nord_face_older_2],
["knight_4_20", "Pokovniz Sretomir Vasiljevic", "Sretomir", tf_hero, 0, reserved,  fac_kingdom_4,
  []+union_lord_gear,
  lord_attrib,wp(240),lord_skills, 0x0000000f630052813b6bb36de5d6eb7400000000001dd72c0000000000000000, nord_face_older_2],

##Vitzland Territories
["knight_5_1", "Vittunhaulto Nolte Guldins ", "Nolte", tf_hero, 0, reserved,  fac_kingdom_5,
  [
  (itm_vitzland_smg, imod_masterwork),
  (itm_pistol_ammo_pw, imod_large_bag),
  (itm_pistol_ammo_pw, imod_large_bag),
  (itm_flamberge, imod_balanced),
  
  (itm_vitzland_armour_cavalry, imod_reinforced),
  (itm_vitzland_uniform_cavalry, imod_reinforced),
  (itm_vitzland_salet_nolte, imod_lordly),
  
  (itm_ammo_belt_1, imod_reinforced),
  (itm_vitzland_gauntlets, imod_reinforced),
  ],
  lord_attrib,wp_m(330),lord_skills|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
["knight_5_2", "Kasier der Furst Laich Ustabier", "Laich", tf_hero, 0, reserved,  fac_kingdom_5,
  [
  (itm_vitzland_shotgun, imod_masterwork),
  (itm_buckshot_ammo_pw, imod_large_bag),
  (itm_buckshot_ammo_pw, imod_large_bag),
  (itm_axe1, imod_balanced),
  
  (itm_vitzland_armour_officer, imod_reinforced),
  (itm_vitzland_uniform_officer, imod_reinforced),
  (itm_vitzland_salet_ubersto, imod_lordly),
  (itm_vitzland_salet_ubersto_2, imod_lordly),
  (itm_ammo_belt_1, imod_reinforced),
  (itm_vitzland_gauntlets, imod_reinforced),
  ],
  lord_attrib,wp_m(260),lord_skills|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
["knight_5_3", "Ubersto Eilert Martins", "Eilert", tf_hero, 0, reserved,  fac_kingdom_5,
  []+vitzland_lord_gear,
  lord_attrib,wp_m(290),lord_skills, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
["knight_5_4", "Ubersto Tilicke Grauff", "Tilicke", tf_hero, 0, reserved,  fac_kingdom_5,
  [
  itm_vitzland_salet_1_gasmask,
  ]+vitzland_lord_gear,
  lord_attrib,wp_m(320),lord_skills, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
["knight_5_5", "Ubersto Michael Ortenberg", "Michael", tf_hero, 0, reserved,  fac_kingdom_5,
  []+vitzland_lord_gear,
  lord_attrib,wp_m(350),lord_skills, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
["knight_5_6", "Ubersto Tilcke Flissing", "Tilcke", tf_hero, 0, reserved,  fac_kingdom_5,
  [
  itm_bandit_fullhelm,
  ]+vitzland_lord_gear,
  lord_attrib,wp_m(230),lord_skills, 0x000000001100000648d24d36cd964b1d00000000001e2dac0000000000000000, rhodok_face_middle_2],
["knight_5_7", "Ubersto Lach Bergler", "Lach", tf_hero, 0, reserved,  fac_kingdom_5,
  []+vitzland_lord_gear,
  lord_attrib,wp_m(260),lord_skills, 0x0000000c3a0455c443d46e4c8b91291a00000000001ca51b0000000000000000, rhodok_face_old_2],
["knight_5_8", "Ubersto Teruckte Tylick Spon", "Tylick", tf_hero, 0, reserved,  fac_kingdom_5,
  [
  itm_grenade_stick_bundle,
  ]+vitzland_lord_gear,
  lord_attrib,wp_m(290),lord_skills|knows_trainer_3, 0x0000000c2c0844d42914d19b2369b4ea00000000001e331b0000000000000000, rhodok_face_older_2],
["knight_5_9", "Ubersto Hinrich Sifrid", "Hinrich", tf_hero, 0, reserved,  fac_kingdom_5,
  [
  itm_vitzland_salet_3_gasmask,
  ]+vitzland_lord_gear,
  lord_attrib,wp_m(320),lord_skills|knows_trainer_6, 0x00000000420430c32331b5551c4724a100000000001e39a40000000000000000, rhodok_face_older_2],
["knight_5_10", "Sevostopfesto Severin ssfrid", "Severin", tf_hero, 0, reserved,  fac_kingdom_5,
  [
  itm_grenade_stick_bundle,
  itm_grenade_stick_bundle,
  itm_grenade_stick_bundle,
  
  itm_vitzland_salet_1_gasmask,
  ]+vitzland_lord_gear,
  lord_attrib,wp_r(380),lord_skills|knows_trainer_4|knows_power_throw_5, 0x00000008e20011063d9b6d4a92ada53500000000001cc1180000000000000000, rhodok_face_older_2],
["knight_5_11", "Ubersto Ludecke Memminger", "Ludecke", tf_hero, 0, reserved,  fac_kingdom_5,
  [
  (itm_vitzland_uniform_officer_cuirass, imod_lordly),
  ]+vitzland_lord_gear,
  lord_attrib,wp(130),lord_skills, 0x0000000c170c14874752adb6eb3228d500000000001c955c0000000000000000, rhodok_face_middle_2],
["knight_5_12", "Ubersto Harmen Herr", "Harmen", tf_hero, 0, reserved,  fac_kingdom_5,
  [
  itm_gas_mask_ca_90,
  ]+vitzland_lord_gear,
  lord_attrib,wp(160),lord_skills|knows_trainer_5, 0x0000000c080c13d056ec8da85e3126ed00000000001d4ce60000000000000000, rhodok_face_old_2],
["knight_5_13", "Ubersto Christofer Ackermans", "Christofer", tf_hero, 0, reserved,  fac_kingdom_5,
  []+vitzland_lord_gear,
  lord_attrib,wp(190),lord_skills, 0x0000000cbf10100562a4954ae731588a00000000001d6b530000000000000000, rhodok_face_older_2],
["knight_5_14", "Ubersto Godeke Brugg", "Godeke", tf_hero, 0, reserved,  fac_kingdom_5,
  []+vitzland_lord_gear,
  lord_attrib,wp(220),lord_skills, 0x0000000c330805823baa77556c4e331a00000000001cb9110000000000000000, rhodok_face_older_2],
["knight_5_15", "Ubersto Eberd Murers", "Eberd", tf_hero, 0, reserved,  fac_kingdom_5,
  [
  (itm_vitzland_pistol, imod_balanced),
  ]+vitzland_lord_gear,
  lord_attrib,wp(250),lord_skills, 0x0000000d51000106370c4d4732b536de00000000001db9280000000000000000, rhodok_face_older_2],
["knight_5_16", "Ubersto Hermen Lippach", "Hermen", tf_hero, 0, reserved,  fac_kingdom_5,
  [
  itm_vitzland_uniform_officer_cuirass,
  ]+vitzland_lord_gear,
  lord_attrib,wp(120),lord_skills, 0x0000000c06046151435b5122a37756a400000000001c46e50000000000000000, rhodok_face_middle_2],
["knight_5_17", "Ubersto Theophilis Frs", "Theophilis", tf_hero, 0, reserved,  fac_kingdom_5,
  [
  itm_vitzland_salet_3_gasmask,
  ]+vitzland_lord_gear,
  lord_attrib,wp(150),lord_skills, 0x0000000c081001d3465c89a6a452356300000000001cda550000000000000000, rhodok_face_old_2],
["knight_5_18", "Ubersto Rudolf Stricher", "Rudolf", tf_hero, 0, reserved,  fac_kingdom_5,
  [
  itm_vitzland_uniform_officer,
  ]+vitzland_lord_gear,
  lord_attrib,wp(180),lord_skills, 0x0000000a3d0c13c3452aa967276dc95c00000000001dad350000000000000000, rhodok_face_older_2],
["knight_5_19", "Ubersto Jurgen Vischer", "Jurgen", tf_hero, 0, reserved,  fac_kingdom_5,
  [
  itm_vitzland_helmet_gasmask,
  itm_vitzland_armour_officer,
  ]+vitzland_lord_gear,
  lord_attrib,wp(210),lord_skills|knows_trainer_5, 0x0000000038043194092ab4b2d9adb44c00000000001e072c0000000000000000, rhodok_face_older_2],
["knight_5_20", "Ubersto Severin Bissler", "Severin", tf_hero, 0, reserved,  fac_kingdom_5,
  []+vitzland_lord_gear,
  lord_attrib,wp(240),lord_skills|knows_trainer_6, 0x000000003600420515a865b45c64d64c00000000001d544b0000000000000000, rhodok_face_older_2],

##Trezzo Republic
["knight_6_1", "Comisario-notte Fedele Vittoria", "Fedele", tf_hero, 0, reserved,  fac_kingdom_6,
  [
  (itm_trezzo_smg, imod_masterwork),
  (itm_pistol_ammo_pw, imod_large_bag),
  (itm_pistol_ammo_pw, imod_large_bag),
  (itm_estoc, imod_balanced),
  
  (itm_republican_armour_officer, imod_reinforced),
  (itm_republican_uniform_sergeant, imod_lordly),
  (itm_republican_noble_helmet, imod_lordly),
  
  (itm_ammo_belt_1, imod_reinforced),
  (itm_black_gloves, imod_lordly),
  ],
  lord_attrib,wp_m(330),lord_skills|knows_trainer_3, 0x00000000600c2084486195383349eae500000000001d16a30000000000000000, rhodok_face_middle_2],
["knight_6_2", "Mastri di Prexor Odidone Savaglio", "Odidone", tf_hero, 0, reserved,  fac_kingdom_6,
  [
  (itm_blunt_slug_ammo_pw, imod_large_bag),
  (itm_blunt_slug_ammo_pw, imod_large_bag),
  
  (itm_shotgun_riot, imod_masterwork),
  
  ]+republican_lord_gear,
  lord_attrib,wp_m(260),lord_skills|knows_trainer_4, 0x00000001380825d444cb68b92b8d3b1d00000000001dd71e0000000000000000, rhodok_face_old_2],
["knight_6_3", "Cauncili Sebastiano Vicari", "Sebastiano", tf_hero, 0, reserved,  fac_kingdom_6,
  []+republican_lord_gear,
  lord_attrib,wp_m(290),lord_skills, 0x000000002208428579723147247ad4e500000000001f14d40000000000000000, rhodok_face_older_2],
["knight_6_4", "Cauncili Adolfo Guidetti", "Adolfo", tf_hero, 0, reserved,  fac_kingdom_6,
  []+republican_lord_gear,
  lord_attrib,wp_m(320),lord_skills, 0x00000009bf084285050caa7d285be51a00000000001d11010000000000000000, rhodok_face_older_2],
["knight_6_5", "Cauncili Eliano Mira", "Eliano", tf_hero, 0, reserved,  fac_kingdom_6,
  []+republican_lord_gear,
  lord_attrib,wp_m(350),lord_skills, 0x000000002a084003330175aae175da9c00000000001e02150000000000000000, rhodok_face_older_2],
["knight_6_6", "Cauncili Giustiniano Salvato", "Giustiniano", tf_hero, 0, reserved,  fac_kingdom_6,
  [
  itm_republican_noble_helmet_2,
  ]+republican_lord_gear,
  lord_attrib,wp_m(230),lord_skills, 0x00000001830043834733294c89b128e200000000001259510000000000000000, rhodok_face_middle_2],
["knight_6_7", "Cauncili Almerigo Viselli", "Almerigo", tf_hero, 0, reserved,  fac_kingdom_6,
  [
  itm_republican_uniform_officer,
  ]+republican_lord_gear,
  lord_attrib,wp_m(260),lord_skills, 0x0000000cbf10434020504bbbda9135d500000000001f62380000000000000000, rhodok_face_old_2],
["knight_6_8", "Cauncili Gabino Faia", "Gabino", tf_hero, 0, reserved,  fac_kingdom_6,
  []+republican_lord_gear,
  lord_attrib,wp_m(290),lord_skills|knows_trainer_3, 0x0000000190044003336dcd3ca2cacae300000000001f47640000000000000000, rhodok_face_older_2],
["knight_6_9", "Cauncili Asterio De Rogatis", "Asterio", tf_hero, 0, reserved,  fac_kingdom_6,
  []+republican_lord_gear,
  lord_attrib,wp_m(320),lord_skills|knows_trainer_6, 0x0000000dde0040c4549dd5ca6f4dd56500000000001e291b0000000000000000, rhodok_face_older_2],
["knight_6_10", "Cauncili Omero Schiavi", "Omero", tf_hero, 0, reserved,  fac_kingdom_6,
  []+republican_lord_gear,
  lord_attrib,wp_m(350),lord_skills|knows_trainer_4, 0x00000001a60441c66ce99256b4ad4b3300000000001d392c0000000000000000, rhodok_face_older_2],
["knight_6_11", "Cauncili Urdino Lizzi", "Urdino", tf_hero, 0, reserved,  fac_kingdom_6,
  [
  itm_republican_noble_helmet_2,
  itm_republican_armour_officer,
  ]+republican_lord_gear,
  lord_attrib,wp(130),lord_skills, 0x0000000fff08134726c28af8dc96e4da00000000001e541d0000000000000000, rhodok_face_middle_2],
["knight_6_12", "Cauncili Agrippa Portera", "Agrippa", tf_hero, 0, reserved,  fac_kingdom_6,
  []+republican_lord_gear,
  lord_attrib,wp(160),lord_skills|knows_trainer_5, 0x0000000035104084635b74ba5491a7a400000000001e46d60000000000000000, rhodok_face_old_2],
["knight_6_13", "Cauncili Ursmaro Cima", "Ursmaro", tf_hero, 0, reserved,  fac_kingdom_6,
  []+republican_lord_gear,
  lord_attrib,wp(190),lord_skills, 0x00000000001021435b734d4ad94eba9400000000001eb8eb0000000000000000, rhodok_face_older_2],
["knight_6_14", "Cauncili Amedeo Colonna", "Amedeo", tf_hero, 0, reserved,  fac_kingdom_6,
  []+republican_lord_gear,
  lord_attrib,wp(220),lord_skills, 0x000000000c0c45c63a5b921ac22db8e200000000001cca530000000000000000, rhodok_face_older_2],
["knight_6_15", "Cauncili Agenore Colicchio", "Agenore", tf_hero, 0, reserved,  fac_kingdom_6,
  []+republican_lord_gear,
  lord_attrib,wp(250),lord_skills, 0x000000001b0c4185369a6938cecde95600000000001f25210000000000000000, rhodok_face_older_2],
["knight_6_16", "Cauncili Barnaba Borsari", "Barnaba", tf_hero, 0, reserved,  fac_kingdom_6,
  []+republican_lord_gear,
  lord_attrib,wp(120),lord_skills, 0x00000007770841c80a01e1c5eb51ffff00000000001f12d80000000000000000, rhodok_face_middle_2],
["knight_6_17", "Cauncili Taziano Corradino", "Taziano", tf_hero, 0, reserved,  fac_kingdom_6,
  [
  itm_republican_noble_helmet_2,
  ]+republican_lord_gear,
  lord_attrib,wp(150),lord_skills, 0x000000007f0462c32419f47a1aba8bcf00000000001e7e090000000000000000, rhodok_face_old_2],
["knight_6_18", "Cauncili Patroclo Corsello", "Patroclo", tf_hero, 0, reserved,  fac_kingdom_6,
  []+republican_lord_gear,
  lord_attrib,wp(180),lord_skills, 0x000000003410410070d975caac91aca500000000001c27530000000000000000, rhodok_face_older_2],
["knight_6_19", "Cauncili Colombo Todaro", "Colombo", tf_hero, 0, reserved,  fac_kingdom_6,
  []+republican_lord_gear,
  lord_attrib,wp(210),lord_skills|knows_trainer_5, 0x000000018a08618016ac36bc8b6e4a9900000000001dd45d0000000000000000, rhodok_face_older_2],
["knight_6_20", "Cauncili Leone Vellucci", "Leone", tf_hero, 0, reserved,  fac_kingdom_6,
  []+republican_lord_gear,
  lord_attrib,wp(240),lord_skills|knows_trainer_6, 0x00000001bd0040c0281a899ac956b94b00000000001ec8910000000000000000, rhodok_face_older_2],

#Itami Castedom
["knight_7_1", "Marmi Cui Li", "Cui", tf_hero, 0, reserved,  fac_kingdom_7,
  [
  ]+itami_lord_gear,
  lord_attrib,wp_m(330),lord_skills|knows_trainer_3, 0x00000000600c2084486195383349eae500000000001d16a30000000000000000, rhodok_face_middle_2],
["knight_7_2", "Shyia Qiao Feng", "Qiao", tf_hero, 0, reserved,  fac_kingdom_7,
  [
  ]+itami_lord_gear,
  lord_attrib,wp_m(260),lord_skills|knows_trainer_4, 0x00000001380825d444cb68b92b8d3b1d00000000001dd71e0000000000000000, rhodok_face_old_2],
["knight_7_3", "Shyia Zou Tai", "Zou", tf_hero, 0, reserved,  fac_kingdom_7,
  []+itami_lord_gear,
  lord_attrib,wp_m(290),lord_skills, 0x000000002208428579723147247ad4e500000000001f14d40000000000000000, rhodok_face_older_2],
["knight_7_4", "Shyia Xiang Zhong", "Xiang", tf_hero, 0, reserved,  fac_kingdom_7,
  []+itami_lord_gear,
  lord_attrib,wp_m(320),lord_skills, 0x00000009bf084285050caa7d285be51a00000000001d11010000000000000000, rhodok_face_older_2],
["knight_7_5", "Shyia Yin Ning", "Yin", tf_hero, 0, reserved,  fac_kingdom_7,
  []+itami_lord_gear,
  lord_attrib,wp_m(350),lord_skills, 0x000000002a084003330175aae175da9c00000000001e02150000000000000000, rhodok_face_older_2],
["knight_7_6", "Shyia Huo Lingxin", "Huo", tf_hero, 0, reserved,  fac_kingdom_7,
  [
  ]+itami_lord_gear,
  lord_attrib,wp_m(230),lord_skills, 0x00000001830043834733294c89b128e200000000001259510000000000000000, rhodok_face_middle_2],
["knight_7_7", "Shyia Lin Qing", "Lin", tf_hero, 0, reserved,  fac_kingdom_7,
  [
  ]+itami_lord_gear,
  lord_attrib,wp_m(260),lord_skills, 0x0000000cbf10434020504bbbda9135d500000000001f62380000000000000000, rhodok_face_old_2],
["knight_7_8", "Shyia Shi Wu", "Shi", tf_hero, 0, reserved,  fac_kingdom_7,
  []+itami_lord_gear,
  lord_attrib,wp_m(290),lord_skills|knows_trainer_3, 0x0000000190044003336dcd3ca2cacae300000000001f47640000000000000000, rhodok_face_older_2],
["knight_7_9", "Shyia Zhong Ming", "Zhong", tf_hero, 0, reserved,  fac_kingdom_7,
  []+itami_lord_gear,
  lord_attrib,wp_m(320),lord_skills|knows_trainer_6, 0x0000000dde0040c4549dd5ca6f4dd56500000000001e291b0000000000000000, rhodok_face_older_2],
["knight_7_10", "Shyia Lei Luoyang", "Lei", tf_hero, 0, reserved,  fac_kingdom_7,
  []+itami_lord_gear,
  lord_attrib,wp_m(350),lord_skills|knows_trainer_4, 0x00000001a60441c66ce99256b4ad4b3300000000001d392c0000000000000000, rhodok_face_older_2],

##Irregular
["knight_irregular_1", "Comrade Zestri", "Zestri", tf_hero, 0, reserved,  fac_irregulars,
  [
  itm_rifle_ammo_pw,
  itm_irregular_bolt_action_carbine,
  itm_trooper_sword,
  
  itm_irregular_armour_officer,
  itm_irregular_uniform_officer_1,
  
  itm_irregular_officer_helmet,
  
  itm_irregular_demi_gauntlets,
  ],
  lord_attrib,wp_m(230),lord_skills, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
["knight_irregular_2", "Comrade Yelta", "Yelta", tf_hero, 0, reserved,  fac_irregulars,
  [
  itm_rifle_ammo_pw,
  itm_irregular_bolt_action_carbine,
  itm_trooper_sword,
  
  itm_irregular_armour_officer,
  itm_irregular_uniform_officer_1,
  
  itm_irregular_officer_helmet,
  
  itm_irregular_demi_gauntlets,
  ],
  lord_attrib,wp_m(230),lord_skills, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
["knight_irregular_3", "Comrade Nasha", "Nasha", tf_hero, 0, reserved,  fac_irregulars,
  [
  itm_rifle_ammo_pw,
  itm_irregular_bolt_action_carbine,
  itm_trooper_sword,
  
  itm_irregular_armour_officer,
  itm_irregular_uniform_officer_1,
  
  itm_irregular_officer_helmet,
  
  itm_irregular_demi_gauntlets,
  ],
  lord_attrib,wp_m(230),lord_skills, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
["knight_irregular_4", "Comrade Varlmov", "Varlmov", tf_hero, 0, reserved,  fac_irregulars,
  [
  itm_rifle_ammo_pw,
  itm_irregular_bolt_action_carbine,
  itm_trooper_sword,
  
  itm_irregular_armour_officer,
  itm_irregular_uniform_officer_1,
  
  itm_irregular_officer_helmet,
  
  itm_irregular_demi_gauntlets,
  ],
  lord_attrib,wp_m(230),lord_skills, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
["knight_irregular_5", "Comrade Petron", "Petron", tf_hero, 0, reserved,  fac_irregulars,
  [
  itm_rifle_ammo_pw,
  itm_irregular_bolt_action_carbine,
  itm_trooper_sword,
  
  itm_irregular_armour_officer,
  itm_irregular_uniform_officer_1,
  
  itm_irregular_officer_helmet,
  
  itm_irregular_demi_gauntlets,
  ],
  lord_attrib,wp_m(230),lord_skills, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],

##Theocracy of Throd
["knight_throd_1", "Master Nivoy", "Nivoy", tf_hero, 0, reserved,  fac_theocracy,
  [
  itm_robe_6,
  ]+throd_lord_gear,
  lord_attrib,wp_m(230),lord_skills, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
["knight_throd_2", "Master Corvo", "Corvo", tf_hero, 0, reserved,  fac_theocracy,
  [
  itm_robe_5,
  ]+throd_lord_gear,
  lord_attrib,wp_m(230),lord_skills, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
["knight_throd_3", "Master Arc", "Arc", tf_hero, 0, reserved,  fac_theocracy,
  [
  itm_robe_4,
  ]+throd_lord_gear,
  lord_attrib,wp_m(230),lord_skills, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
["knight_throd_4", "Master Kalos", "Kalos", tf_hero, 0, reserved,  fac_theocracy,
  [
  itm_robe_3,
  ]+throd_lord_gear,
  lord_attrib,wp_m(230),lord_skills, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
["knight_throd_5", "Master Enpiter", "Enpiter", tf_hero, 0, reserved,  fac_theocracy,
  [
  itm_robe_2,
  ]+throd_lord_gear,
  lord_attrib,wp_m(230),lord_skills, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],

##################
##Faction Ladies##
##################
#
["knight_1_1_wife","Error - knight_1_1_wife should not appear in game","knight_1_1_wife",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
[],
def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
#

##Entenaii Empire
##Imperial Family
["kingdom_1_lady_1","Empress-Dowager Genavia","Genavia",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_entenaii_uniform_noble,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
["kingdom_1_lady_2","Empress-Consort Rachetta","Rachetta",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_entenaii_uniform_noble,
  ],         attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
["knight_1_lady_3","Empress-Kin Henriette","Henriette",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_dress_3,
  ],     attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
#
["knight_1_lady_4","Neliss Zetta Foy","Zetta",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_dress_2,

  ],     attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
["kingdom_l_lady_5","Neliss Beaulah Maltby","Beaulah",tf_hero|tf_randomize_face|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_dress_1,
  ],        attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_6","Neliss Ethyl Ocallaghan","Ethyl",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [

  itm_women_robe_6,
  ],        attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
["kingdom_1_lady_7","Neliss Oda Anderson","Oda",tf_hero|tf_randomize_face|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [

  itm_women_robe_5,
  ],        attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_8","Neliss Rilla Lette","Rilla",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [

  itm_entenaii_uniform_officer,

  ],        attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
["kingdom_1_lady_9","Neliss Aileen Callan","Aileen",tf_hero|tf_randomize_face|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [

  itm_women_robe_3,

  ],      attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_10","Neliss Catherine McArty","Catherine",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_entenaii_uniform_noble,

  ],      attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
["kingdom_1_lady_11","Neliss Zenobia Uleaven","Zenobia",tf_hero|tf_randomize_face|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_dress_2
  ],
  def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_12","Neliss Genevieve Shea","Genevieve",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_dress_1
  ],
  def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
["kingdom_l_lady_13","Neliss Phyllis Plundell","Phyllis",tf_hero|tf_randomize_face|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_dress_3
  ],
  def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_14","Neliss Leota Oakden","Leota",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_dress_4
  ],
  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
["kingdom_1_lady_15","Neliss Mamie Cowen","Mamie",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_dress_5
  ],
  def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_1_lady_16","Neliss Kathleen Beley","Kathleen",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_women_robe_1
  ],
  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
["kingdom_1_lady_17","Neliss Odile Campbell","Odile",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_entenaii_uniform_noble,
  ],
  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
["kingdom_1_lady_18","Neliss Elna Scott","Elna",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_women_robe_3
  ],
  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
["kingdom_1_lady_19","Neliss Carmella Teague","Carmella",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_entenaii_uniform_officer,
  ],
  def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
["kingdom_1_lady_20","Neliss Victoria Ames","Victoria",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,
  [
  itm_women_robe_5
  ],
  def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

##Entenaii Dominion
#Governer Family
["kingdom_2_lady_1","Matriarch Beatrice","Beatrice",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_fanatic_noble_mitre,
  itm_dominion_dress_1,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
["kingdom_2_lady_2","Governeress Catherine","Catherine",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_dress_2,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
#
["kingdom_2_lady_3","Psu-Neliss Margery","Margery",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_dress_3,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
["kingdom_2_lady_4","Psu-Neliss Teresa Henman","Teresa",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_uniform_officer,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
["kingdom_2_lady_5","Psu-Neliss Primula Ashpole","Primula",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_dress_2,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
["kingdom_2_lady_6","Psu-Neliss Nerissa Turner","Nerissa",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_dress_3,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
["kingdom_2_lady_7","Psu-Neliss Ada Stevenson","Ada",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_dress_1,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
["kingdom_2_lady_8","Psu-Neliss Celia Lemar","Celia",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_uniform_fanatic_noble,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
["kingdom_2_lady_9","Psu-Neliss Priscilla Sara","Priscilla",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_dress_3,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
["kingdom_2_lady_10","Psu-Neliss Margaret Blagg","Margaret",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_dress_1,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
["kingdom_2_lady_11","Psu-Neliss Rosella Flitter","Rosella",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_uniform_officer,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
["kingdom_2_lady_12","Psu-Neliss Joyce Bertrand","Joyce",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_dress_3,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
["kingdom_2_lady_13","Psu-Neliss Constance Webb","Constance",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_dress_1,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
["kingdom_2_lady_14","Psu-Neliss Carrie Defries","Carrie",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_uniform_fanatic_noble,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
["kingdom_2_lady_15","Psu-Neliss Madge Rutt","Madge",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_dress_3,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
["kingdom_2_lady_16","Psu-Neliss Wilhelmina Rosenburg","Wilhelmina",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_dress_1,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
["kingdom_2_lady_17","Psu-Neliss Alexandrina Harrison","Alexandrina",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_dress_2,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
["kingdom_2_lady_18","Psu-Neliss Johanna Cheater","Johanna",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_dress_3,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
["kingdom_2_lady_19","Psu-Neliss Rosa Whittemore","Rosa",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_dress_1,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
["kingdom_2_lady_20","Psu-Neliss Lilian Paling","Lilian",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,
  [
  itm_dominion_dress_2,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],

##Kingdom of Galvae
#Royal Family
["kingdom_3_lady_1","Queen-Mother Ainnir Mhic Niocaill","Ainnir",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_1,
  
  itm_galvae_taly_mask,
  itm_cloak_royal,
  ],attr_lvl_20,wp_2_m,knows_battle_1|knows_riding_2, khergit_woman_face_1],
["kingdom_3_lady_2","Queen-Consort Eavnat Nic Colla","Eavnat",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_galvae_uniform_officer,
  
  itm_galvae_taly_mask,
  itm_cloak_royal,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
["kingdom_3_lady_3","Princess Fionnghuala O Ceanndubhain","Fionnghuala",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_3,
  itm_galvae_armour_officer,

  itm_galvae_taly_mask,
  itm_cloak_royal,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, khergit_woman_face_2],
#
["kingdom_3_lady_4","Taly Mairona Mhic Cairbre","Mairona",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_4,
  
  itm_galvae_taly_mask,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
["kingdom_3_lady_5","Taly Darearca Nic Craith","Darearca",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_galvae_uniform_cavalry,

  itm_galve_veil_metal,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
["kingdom_3_lady_6","Taly Peigin Nic Cuinn","Peigin",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_6,

  itm_galvae_taly_mask,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
["kingdom_3_lady_7","Taly Dealla Mhic Giolla Comhghaill","Dealla",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_1,
  
  itm_galvae_mask_helmet,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
["kingdom_3_lady_8","Taly Curchach Nic Ceirin","Curchach",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_2,
  
  itm_galve_veil_metal,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
["kingdom_3_lady_9","Taly Tuilelaith Nic Dhuibh","Tuilelaith",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_3,
  
  itm_galvae_taly_mask,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
["kingdom_3_lady_10","Taly Nuala Ni hAthairne","Nuala",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_4,
  
  itm_galvae_taly_mask,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
["kingdom_3_lady_11","Taly Iuchra Mhic Uaid","Iuchra",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_5,
  
  itm_galvae_mask_helmet,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
["kingdom_3_lady_12","Taly ornait Nic Phadraig","ornait",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_6,
  
  itm_galvae_taly_mask,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
["kingdom_3_lady_13","Taly Fithir Ui Meirgin","Fithir",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_1,
  
  itm_galvae_taly_mask,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
["kingdom_3_lady_14","Taly Ciannait Nic Conaing","Ciannait",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_2,
  
  itm_galvae_taly_mask,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
["kingdom_3_lady_15","Taly Aodhnait Mhic Ceileachair","Aodhnait",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_ornate_seax,
  
  itm_wild_bodypaint_fem,
  
  itm_galvae_taly_mask,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
["kingdom_3_lady_16","Taly Cliona Mhic Cionaodha","Cliona",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_galvae_uniform_cavalry,
  
  itm_galvae_taly_mask,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
["kingdom_3_lady_17","Taly Neacht Nic Giolla Leith", "Neacht",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_5,
  
  itm_galvae_mask_helmet,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
["kingdom_3_lady_18","Taly Brid Mhic Giolla","Brid",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_6,
  
  itm_galvae_taly_mask,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
["kingdom_3_lady_19","Taly Clidna Nic Lughaidh","Clidna",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_1,
  
  itm_galvae_taly_mask,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
["kingdom_3_lady_20","Taly eabha Ui Dubhagain","eabha",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,
  [
  itm_tartan_dress_2,
  
  itm_galvae_taly_mask,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],

##Molvat-Berchav Union
#Tzar's Family
["kingdom_4_lady_1","Tzarkar Olga","Olga",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_1,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
["kingdom_4_lady_2","Tzarina Vojislava","Vojislava",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_2,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
["kingdom_4_lady_3","Tsarevna Miljana","Miljana",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_3,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
#
["kingdom_4_lady_4","Kovess Sandra Lazic","Sandra",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_4,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
["kingdom_4_lady_5","Kovess Darija Kostic","Darija",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_5,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
["kingdom_4_lady_6","Kovess Ivana Vasic","Ivana",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_1,
  ],        attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
["kingdom_4_lady_7","Kovess Sava Georgijevic","Sava",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_union_uniform_officer,
  ],     attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
["knight_4_2b_daughter_1","Kovess Slavica Evic","Slavica",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_3,
  ],     attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
["kingdom_4_lady_9","Kovess Bora Markovic","Bora",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_4,
  ],        attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
["knight_4_2c_wife_1","Kovess Nina Stefanovic","Nina",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_5,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
["kingdom_4_lady_11","Kovess Violeta Pajic","Violeta",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_1,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
["knight_4_2c_daughter","Kovess Darija Vladic","Darija",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_2,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
["knight_4_1b_wife","Kovess Zeljana Savicevic","Zeljana",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_3,
  itm_union_armour_officer,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
["kingdom_4_lady_14","Kovess Andrijana Carapic","Andrijana",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_4,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
["knight_4_1b_daughter","Kovess SlaDana Rajkovic","SlaDana",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_5,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
["knight_4_2b_daughter_2","Kovess Blagica Ristovski","Blagica",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_union_uniform_officer,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
["kingdom_4_lady_17","Kovess Dijana Lazarevic","Dijana",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_2,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
["knight_4_2c_wife_2","Kovess Jovana Golubovic","Jovana",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_3,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
["knight_4_1c_daughter","Kovess Sava Obradovic","Sava",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_4,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
["kingdom_4_lady_20","Kovess Dobrica Savic","Dobrica",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,
  [
  itm_wool_dress_5,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],

##Vitzland Territories
#
["kingdom_5_lady_1","Ubersta Anneke Schidholtz","Anneke",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_noble_dress_1,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
["kingdom_5_lady_2","Ubersta Maren von Tettingen","Maren",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_noble_dress_2,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
["kingdom_5_lady_3","Ubersta Cecilie Buss","Cecilie",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_noble_dress_3,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2,0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
["kingdom_5_lady_4","Ubersta Martha Wernhers","Martha",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_noble_dress_4,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
["kingdom_5_5_wife","Ubersta Metteken von Lorch","Metteken",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_noble_dress_5,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, swadian_woman_face_1],
["kingdom_5_2b_wife_1","Ubersta Ermel Nefen","Ermel",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_pistol_ammo,
  itm_vitzland_pistol,
  itm_vitzland_uniform_officer,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000000bf0400035913aa236b4d975a00000000001eb69c0000000000000000],
["kingdom_5_1c_daughter_1","Ubersta Madalen Zslerin","Madalen",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_noble_dress_1,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
["kingdom_5_2c_daughter_1","Ubersta Else Spiessmacherin","Else",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_noble_dress_2,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
["kingdom_5_1c_wife_1","Ubersta Eue Krantz","Eue",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_noble_dress_3,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
["kingdom_5_2c_wife_1","Ubersta Geken Dietschen","Geken",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_noble_dress_4,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
["kingdom_5_1c_daughter_2","Ubersta Dorothen von Lindenberg","Dorothen",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_helmet_gasmask,
  itm_vitzland_uniform_cavalry,
  ],
  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
["kingdom_5_2c_daughter_2","Ubersta Kunneke Talhain","Kunneke",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_armour_officer,
  itm_dress_1,
  ],
  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
["kingdom_5_1b_wife","Ubersta Birgitta Bletzen","Birgitta",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_noble_dress_5,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
["kingdom_5_2b_wife_2","Ubersta Reuss Truchtingen","Reuss",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_armour_officer,
  itm_vitzland_uniform_officer,
  ],
  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
["kingdom_5_1c_daughter_3","Ubersta Liepmayt von Undingen","Liepmayt",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_noble_dress_1,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
["kingdom_5_lady_16","Ubersta Alheit Fritlingen","Alheit",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_uniform_cavalry,
  ],
  def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
["kingdom_5_1c_wife_2","Ubersta Margaret Brendlins","Margaret",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_noble_dress_2,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
["kingdom_5_2c_wife_2","Ubersta Elen Nerers","Elen",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_noble_dress_3,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
["kingdom_5_1c_daughter_4","Ubersta Magdelenen Eberlin","Magdelenen",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_vitzland_noble_dress_4,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
["kingdom_5_lady_20","Ubersta Cecilia Voltz","Cecilia",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,
  [
  itm_pistol_ammo,
  itm_vitzland_pistol,
  itm_turk_broadsword_a,
  itm_vitzland_uniform_officer_cuirass,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],

##Trezzo Republic
#
["kingdom_6_lady_1","Cauncili-materno Imelda","Imelda",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_1,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
["kingdom_6_lady_2","Cauncili-consort Geltrude Corrao","Geltrude",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_2,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
["kingdom_6_lady_3","Cauncili-consort Fiorella Sorace","Fiorella",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_1,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
["kingdom_6_lady_4","Cauncili-consort Argelia De Caprio","Argelia",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_2,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
["kingdom_6_lady_5","Cauncili-consort Giada Bisesi","Giada",tf_hero|tf_randomize_face|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_1,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_6_lady_6","Cauncili-consort Manuela De Leo","Manuela",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_uniform_officer,
  itm_republican_armour_officer,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
["kingdom_6_lady_7","Cauncili-consort Antonella China","Antonella",tf_hero|tf_randomize_face|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_1,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_6_lady_8","Cauncili-consort Rosamunda Zingaro","Rosamunda",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_2,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
["kingdom_6_lady_9","Cauncili-consort Carmela Turri","Carmela",tf_hero|tf_randomize_face|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_1,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_6_lady_10","Cauncili-consort Palmira D'Antoni","Palmira",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_2,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
["kingdom_6_lady_11","Cauncili-consort Silvia Prinzi","Silvia",tf_hero|tf_randomize_face|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_uniform_officer,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_6_lady_12","Cauncili-consort Prospera Clara","Prospera",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_uniform_officer,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
["kingdom_6_lady_13","Cauncili-consort Iride Baldelli","Iride",tf_hero|tf_randomize_face|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_1,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_6_lady_14","Cauncili-consort Nives Vital","Nives",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_2,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
["kingdom_6_lady_15","Cauncili-consort Quartilla Bacigalupi","Quartilla",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_1,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_6_lady_16","Cauncili-consort Zaira Gennarelli","Zaira",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_2,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
["kingdom_6_lady_17","Cauncili-consort Valeriana Sorce","Valeriana",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_1,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
["kingdom_6_lady_18","Cauncili-consort Cornelia Uliano","Cornelia",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_2,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
["kingdom_6_lady_19","Cauncili-consort Fatima Simiele","Fatima",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_1,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
["kingdom_6_lady_20","Cauncili-consort Renata Loria","Renata",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,
  [
  itm_republican_consort_dress_2,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

##Itami Castedom
#
["kingdom_7_lady_1","Yasar Yuan Shui","Yuan",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
  [
  itm_republican_consort_dress_1,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
["kingdom_7_lady_2","Yasar Li Xiu","Li",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
  [
  itm_republican_consort_dress_2,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
["kingdom_7_lady_3","Yasar He Yawen","He",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
  [
  itm_republican_consort_dress_1,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
["kingdom_7_lady_4","Yasar Huang Bi","Huang",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
  [
  itm_republican_consort_dress_2,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
["kingdom_7_lady_5","Yasar Geng Bao","Geng",tf_hero|tf_randomize_face|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
  [
  itm_republican_consort_dress_1,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_7_lady_6","Yasar Zou Cai","Zou",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
  [
  itm_republican_uniform_officer,
  itm_republican_armour_officer,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
["kingdom_7_lady_7","Yasar Gao Yan","Gao",tf_hero|tf_randomize_face|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
  [
  itm_republican_consort_dress_1,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_7_lady_8","Yasar Pan Yazhu","Pan",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
  [
  itm_republican_consort_dress_2,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
["kingdom_7_lady_9","Yasar Shen Yang","Shen",tf_hero|tf_randomize_face|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
  [
  itm_republican_consort_dress_1,
  ],attr_lvl_10,wp_1_m,knows_battle_1|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
["kingdom_7_lady_10","Yasar Han Dan","Han",tf_hero|tf_woman|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,
  [
  itm_republican_consort_dress_2,
  ],def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],

["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[],attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000008318101f390c515555594],

#Seneschals
["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x00000000000c218501ef4f5d2ccb0026],
["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [

  itm_civilian_outfit_2,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x00000000000c03cc01cc34a9a467fdfd],
["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [

  itm_civilian_outfit_3,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x00000000000c500e01dbb2115a55f3cd],
["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [

  itm_civilian_outfit_4,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000008035201e6eebaf3f3eb2b],
["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [

  itm_civilian_outfit_5,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000000249101e7898999ac54c6],
["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [

  itm_civilian_outfit_6,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000010360b01cef8b57553d34e],
["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [

  itm_civilian_outfit_7,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000000018101f9487aa831dce4],
["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [

  itm_civilian_outfit_8,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000004715201ea236c60a2bcae],
["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [

  itm_civilian_outfit_9,

  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x00000000000440c601e1cd45cfb38550],
["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000010230c01ef41badb50465e],
["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000008061301fb89acfb95332f],
["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x00000000000c13ce01dc4723ab936c82],
["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000008548e01d952a9b25d6d5a],
["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000004728b01c293c694944b05],
["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000004728b01c293c694944b05],
["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000004728b01c293c694944b05],
["town_17_seneschal", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000004728b01c293c694944b05],
["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000004728b01c293c694944b05],
["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000004728b01c293c694944b05],
["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000004728b01c293c694944b05],
["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000004728b01c293c694944b05],
["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000004728b01c293c694944b05],
#
["town_23_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x00000000000c218501ef4f5d2ccb0026],
["town_24_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x00000000000c03cc01cc34a9a467fdfd],
["town_25_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x00000000000c500e01dbb2115a55f3cd],
["town_26_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000008035201e6eebaf3f3eb2b],
["town_27_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000000249101e7898999ac54c6],
["town_28_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000010360b01cef8b57553d34e],
["town_29_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000000018101f9487aa831dce4],
["town_30_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000004715201ea236c60a2bcae],
["town_31_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x00000000000440c601e1cd45cfb38550],
["town_32_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000010230c01ef41badb50465e],
["town_33_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000008061301fb89acfb95332f],
["town_34_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x00000000000c13ce01dc4723ab936c82],
["town_35_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000008548e01d952a9b25d6d5a],
["town_36_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000004728b01c293c694944b05],
#
#Castle Seneschal
["castle_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
["castle_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
["castle_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
["castle_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
["castle_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
["castle_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
["castle_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
["castle_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
["castle_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
["castle_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
["castle_11_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
["castle_12_seneschal", "{!}Castle 12 Seneschal", "{!}Castle 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
["castle_13_seneschal", "{!}Castle 13 Seneschal", "{!}Castle 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
["castle_14_seneschal", "{!}Castle 14 Seneschal", "{!}Castle 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
["castle_15_seneschal", "{!}Castle 15 Seneschal", "{!}Castle 15 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
["castle_16_seneschal", "{!}Castle 16 Seneschal", "{!}Castle 16 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
["castle_17_seneschal", "{!}Castle 17 Seneschal", "{!}Castle 17 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
["castle_18_seneschal", "{!}Castle 18 Seneschal", "{!}Castle 18 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
["castle_19_seneschal", "{!}Castle 19 Seneschal", "{!}Castle 19 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
["castle_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
["castle_21_seneschal", "{!}Castle 21 Seneschal", "{!}Castle 21 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_civilian_outfit_5],def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],

#
#Arena Masters
["town_1_arena_master", "Tournament Master","{!}Tournament Master",tf_hero, scn_arena_x|entry(52),reserved,   fac_commoners,
  [
  itm_civilian_outfit_1,
  itm_civilian_outfit_2,
  itm_civilian_outfit_3,
  itm_civilian_outfit_4,
  itm_civilian_outfit_5,
  itm_civilian_outfit_6,
  itm_civilian_outfit_7,
  itm_civilian_outfit_8,
  itm_civilian_outfit_9,
  itm_civilian_outfit_10,
  itm_civilian_outfit_11,
  itm_civilian_outfit_12,
  itm_civilian_outfit_13,
  itm_dominion_revolver,
  itm_pistol_ammo_4,
  itm_brassknuckles,
  ],
  attr_lvl_45,wp_6_m,knows_battle_6, 0x0000000cf600f41552db6eb3ab6db6db00000000001db6da0000000000000000],

#Armor Merchants
#arena_masters_end = zendar_armorer
["town_1_armorer","Armourer",  "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_1,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_2_armorer","Armourer",  "{!}Armourer",  tf_hero|tf_randomize_face|tf_woman|tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_1w,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_3_armorer","Armourer",  "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_2,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_4_armorer","Armourer",  "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_3,

  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_5_armorer","Armourer",  "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_4,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_6_armorer","Armourer",  "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_5,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_7_armorer","Armourer",  "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_6,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_8_armorer","Armourer",  "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_7,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_9_armorer","Armourer",  "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_8,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_10_armorer","Armourer", "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_9,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_11_armorer","Armourer", "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_10,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_12_armorer","Armourer", "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_11,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_13_armorer","Armourer", "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_12,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_14_armorer","Armourer", "{!}Armourer",  tf_hero|tf_randomize_face|tf_woman|tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_2w,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_15_armorer","Armourer", "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_13,
  
  itm_bandit_hood_wht_scarf,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_16_armorer","Armourer", "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_irregular_uniform_cavalry_1,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_17_armorer","Armourer", "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_dominion_uniform_yeoman,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_18_armorer","Armourer", "{!}Armourer",  tf_hero|tf_randomize_face|tf_woman|tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_3w,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_19_armorer","Armourer", "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_irregular_uniform_levy,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_20_armorer","Armourer", "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_irregular_uniform_officer_1,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_21_armorer","Armourer", "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_irregular_uniform_raider_1,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_22_armorer","Armourer", "{!}Armourer",  tf_hero|tf_randomize_face|tf_woman|tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_10w,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, woman_face_1, woman_face_2],
#
#["town_23_armorer","Armourer", "{!}Armourer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  # [
  # itm_irregular_uniform_guard_1,
  # ],
  # def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],

#Weapon merchants
["town_1_weaponsmith", "Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|tf_woman|tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_1w,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_2_weaponsmith", "Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_1,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_3_weaponsmith", "Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_13,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_4_weaponsmith", "Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_12,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_5_weaponsmith", "Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_irregular_uniform_officer_1,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_6_weaponsmith", "Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_11,
  
  itm_bandit_hood_red,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_7_weaponsmith", "Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_10,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_8_weaponsmith", "Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|tf_woman|tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_5w,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_9_weaponsmith", "Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_7,
  ],
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_10_weaponsmith","Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_4,
  ], 
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_11_weaponsmith","Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_9,
  ], 
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_12_weaponsmith","Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_10,
  ], 
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_13_weaponsmith","Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_11,
  ], 
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_14_weaponsmith","Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_1,
  ], 
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_15_weaponsmith","Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_irregular_uniform_cavalry_1,
  ], 
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_16_weaponsmith","Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_13,
  ], 
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_17_weaponsmith","Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_10,
  ], 
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_18_weaponsmith","Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_4,
  ], 
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_19_weaponsmith","Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_11,
  ], 
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_20_weaponsmith","Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_8,
  ], 
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_21_weaponsmith","Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_12,
  ], 
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_22_weaponsmith","Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  [
  itm_civilian_outfit_3,
  ], 
  def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
#
# ["town_23_weaponsmith","Gunsmith","{!}Gunsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,
  # [
  # itm_civilian_outfit_4,
  # ], 
  # def_attrib|level(12),wp_m(100),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],

#Tavern keepers
["town_1_tavernkeeper", "Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,
  [
  itm_civilian_outfit_1,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, mercenary_face_1, mercenary_face_2],
["town_2_tavernkeeper", "Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face,           scn_town_2_tavern|entry(9),0,   fac_commoners,
  [
  itm_civilian_outfit_2,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, mercenary_face_1, mercenary_face_2],
["town_3_tavernkeeper", "Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face|tf_woman, scn_town_3_tavern|entry(9),0,   fac_commoners,
  [
  itm_civilian_outfit_1w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, woman_face_1, woman_face_2],
["town_4_tavernkeeper", "Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,
  [
  itm_civilian_outfit_3,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, mercenary_face_1, mercenary_face_2],
["town_5_tavernkeeper", "Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face,           scn_town_5_tavern|entry(9),0,   fac_commoners,
  [
  itm_civilian_outfit_4,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, mercenary_face_1, mercenary_face_2],
["town_6_tavernkeeper", "Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face|tf_woman, scn_town_6_tavern|entry(9),0,   fac_commoners,
  [
  itm_civilian_outfit_2w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, woman_face_1, woman_face_2],
["town_7_tavernkeeper", "Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face|tf_woman, scn_town_7_tavern|entry(9),0,   fac_commoners,
  [
  itm_civilian_outfit_3w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, woman_face_1, woman_face_2],
["town_8_tavernkeeper", "Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,
  [
  itm_irregular_uniform_officer_1,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, mercenary_face_1, mercenary_face_2],
["town_9_tavernkeeper", "Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face|tf_woman, scn_town_9_tavern|entry(9),0,   fac_commoners,
  [
  itm_civilian_outfit_4w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, woman_face_1, woman_face_2],
["town_10_tavernkeeper","Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face|tf_woman, scn_town_10_tavern|entry(9),0,  fac_commoners,
  [
  itm_civilian_outfit_5w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, woman_face_1, woman_face_2],
["town_11_tavernkeeper","Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face|tf_woman, scn_town_11_tavern|entry(9),0,  fac_commoners,
  [
  itm_civilian_outfit_6w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, woman_face_1, woman_face_2],
["town_12_tavernkeeper","Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,
  [
  itm_civilian_outfit_5,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, mercenary_face_1, mercenary_face_2],
["town_13_tavernkeeper","Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face|tf_woman, scn_town_13_tavern|entry(9),0,  fac_commoners,
  [
  itm_civilian_outfit_7w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, woman_face_1, woman_face_2],
["town_14_tavernkeeper","Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face,           scn_town_14_tavern|entry(9),0,  fac_commoners,
  [
  itm_civilian_outfit_6,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, mercenary_face_1, mercenary_face_2],
["town_15_tavernkeeper","Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face|tf_woman, scn_town_15_tavern|entry(9),0,  fac_commoners,
  [
  itm_civilian_outfit_8w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, woman_face_1, woman_face_2],
["town_16_tavernkeeper","Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,
  [
  itm_civilian_outfit_7,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, mercenary_face_1, mercenary_face_2],
["town_17_tavernkeeper","Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face|tf_woman, scn_town_17_tavern|entry(9),0,  fac_commoners,
  [
  itm_civilian_outfit_9w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, woman_face_1, woman_face_2],
["town_18_tavernkeeper","Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,
  [
  itm_civilian_outfit_8,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, mercenary_face_1, mercenary_face_2],
["town_19_tavernkeeper","Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face|tf_woman, scn_town_19_tavern|entry(9),0,  fac_commoners,
  [
  itm_civilian_outfit_10w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, woman_face_1, woman_face_2],
["town_20_tavernkeeper","Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face,           scn_town_20_tavern|entry(9),0,  fac_commoners,
  [
  itm_civilian_outfit_9,
  
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, mercenary_face_1, mercenary_face_2],
["town_21_tavernkeeper","Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face|tf_woman, scn_town_21_tavern|entry(9),0,  fac_commoners,
  [
  itm_civilian_outfit_11w,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, woman_face_1, woman_face_2],
["town_22_tavernkeeper","Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face,           scn_town_22_tavern|entry(9),0,  fac_commoners,
  [
  itm_civilian_outfit_10,
  ],
  attr_lvl_10,wp_1_m,knows_battle_1, mercenary_face_1, mercenary_face_2],
#
# ["town_23_tavernkeeper", "Canteen_Owner","{!}Canteen_Owner",tf_hero|tf_randomize_face,           scn_town_23_tavern|entry(9),0,   fac_commoners,
  # [
  # itm_civilian_outfit_11,
  # ],
  # attr_lvl_10,wp_1_m,knows_battle_1, mercenary_face_1, mercenary_face_2],

#Goods Merchants
["town_1_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_2_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_3_merchant", "Merchant","{!}Merchant",tf_woman|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_4_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_5_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_6_merchant", "Merchant","{!}Merchant",tf_woman|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_7_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_8_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_9_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,
  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_10_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,
  [
  itm_irregular_uniform_guard_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_11_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,
  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_12_merchant","Merchant","{!}Merchant",tf_woman|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,
  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_13_merchant","Merchant","{!}Merchant",tf_woman|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,
  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_14_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_15_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_16_merchant","Merchant","{!}Merchant",tf_woman|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_17_merchant","Merchant","{!}Merchant",tf_woman|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_18_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_19_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_20_merchant","Merchant","{!}Merchant",tf_woman|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_21_merchant","Merchant","{!}Merchant",tf_woman|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_22_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_22_store|entry(9),0, fac_commoners,
  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
#
# ["town_23_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_23_store|entry(9),0, fac_commoners,
  # [
  # itm_poor_shirt_1,
  # ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
# #

#
["salt_mine_merchant","Foreman","Foreman",tf_hero|tf_randomize_face|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,
  [
  itm_sloppy_trench_coat,
  itm_iron_ore,itm_iron_ore,itm_iron_ore,itm_iron_ore,itm_iron_ore,itm_iron_ore,itm_iron_ore,itm_iron_ore,itm_iron_ore,itm_iron_ore,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_young_1, man_face_older_2],
#

#Town Alministrates
["town_1_mayor", "Provost", "{!}Provost", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  
  itm_admin_hat_blue,
  ],  attr_lvl_10,wp_1_m,knows_battle_1, man_face_middle_1, mercenary_face_2],
["town_2_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,

  itm_admin_hat_black,
  ],    attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_3_mayor", "Provost", "{!}Provost", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,

  itm_admin_hat_brown,
  ],  attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_4_mayor", "Gradonacelnik", "{!}Gradonacelnik", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_poor_shirt_1,
  
  itm_admin_hat_blue,
  ],      attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_5_mayor", "Provost", "{!}Provost", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,

  itm_admin_hat_black,
  ],    attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_6_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,

  itm_admin_hat_brown,
  ],    attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_7_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  
  itm_admin_hat_blue,
  ],    attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_8_mayor", "Alministrate", "{!}Alministrate", tf_woman|tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_tartan_dress_3,

  itm_admin_hat_black,
  ],attr_lvl_10,wp_1_m,knows_battle_1,  woman_face_1, woman_face_2],
["town_9_mayor", "Ar-bilidh", "{!}Ar-bilidh", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_galvae_bilidh_cloak,

  itm_admin_hat_brown,
  ],  attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_10_mayor", "Gradonacelnik", "{!}Gradonacelnik", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_poor_shirt_1,
  
  itm_admin_hat_blue,
  ],      attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_11_mayor", "Alministrate", "{!}Alministrate", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,

  itm_admin_hat_black,
  ],    attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_12_mayor", "Provost", "{!}Provost", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,

  itm_admin_hat_brown,
  ],  attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_13_mayor", "Alministrate", "{!}Alministrate", tf_woman|tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  
  itm_admin_hat_blue,
  ],    attr_lvl_10,wp_1_m,knows_battle_1,  woman_face_1, woman_face_2],
["town_14_mayor", "Gradonacelnik", "{!}Gradonacelnik", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,

  itm_admin_hat_black,
  ],      attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_15_mayor", "Ar-bilidh", "{!}Ar-bilidh", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_galvae_bilidh_cloak_red,

  itm_admin_hat_brown,
  ],    attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_16_mayor", "Ar-bilidh", "{!}Ar-bilidh", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_galvae_bilidh_cloak_green,
  
  itm_admin_hat_blue,
  ],  attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_17_mayor", "Gradonacelnik", "{!}Gradonacelnik", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_dominion_civilian_clothes_3,

  itm_admin_hat_black,
  ],   attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_18_mayor", "Mayor", "{!}Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,

  itm_admin_hat_brown,
  ],     attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_19_mayor", "Verwalter", "{!}Verwalter", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_poor_shirt_1,
  
  itm_admin_hat_blue,
  ],    attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_20_mayor", "Verwalter", "{!}Verwalter", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,

  itm_admin_hat_black,
  ],  attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_21_mayor", "Verwalter", "{!}Verwalter", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,

  itm_admin_hat_brown,
  ],    attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
["town_22_mayor", "Verwalter", "{!}Verwalter", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  itm_pistol_ammo,
  itm_vitzland_pistol,
  
  itm_sloppy_trench_coat,
  
  itm_admin_hat_blue,
  ],      attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
# ["town_23_mayor", "Provost", "{!}Provost", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,  [
  # itm_sloppy_trench_coat,

  # itm_admin_hat_black,
  # ],      attr_lvl_10,wp_1_m,knows_battle_1,  man_face_middle_1, mercenary_face_2],
# #

#Village elders
#entenaii
["village_1_elder", "Headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_irregular_uniform_guard_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["village_2_elder", "Headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_irregular_uniform_guard_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_3_elder", "Headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_4_elder", "Headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["village_5_elder", "Headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
["village_6_elder", "Headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_7_elder", "Headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_8_elder", "Headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["village_9_elder", "Headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
["village_10_elder","Headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_11_elder","Headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_12_elder","Headman", "{!}village_1_elder",tf_woman|tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, woman_face_1, woman_face_2],
["village_13_elder","Headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
#dominion
["village_14_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_dominion_civilian_clothes_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_15_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_dominion_civilian_clothes_2,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["village_16_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_17_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_18_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_19_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["village_20_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_21_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_22_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_irregular_uniform_guard_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_23_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_dominion_civilian_clothes_3,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["village_24_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_dominion_civilian_clothes_4,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_25_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
["village_26_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_dominion_civilian_clothes_5,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_27_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_dominion_civilian_clothes_6,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["village_28_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_dominion_civilian_clothes_7,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_29_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_dominion_civilian_clothes_8,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_30_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_dominion_civilian_clothes_9,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_31_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_dominion_civilian_clothes_10,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_32_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_dominion_civilian_clothes_11,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_33_elder","Psu-headman", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_dominion_civilian_clothes_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
#galvae
["village_34_elder","Cuarnaca", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_galvae_bilidh_cloak_green,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_35_elder","Cuarnaca", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_galvae_bilidh_cloak_red,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_36_elder","Cuarnaca", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_gatheredcloaks1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_37_elder","Cuarnaca", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_galvae_bilidh_cloak,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_38_elder","Cuarnaca", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_gatheredcloaks2,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_39_elder","Cuarnaca", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_gatheredcloaks3,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_40_elder","Cuarnaca", "{!}village_1_elder",tf_woman|tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_galvae_bilidh_cloak_green,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              woman_face_1, woman_face_2],
["village_41_elder","Cuarnaca", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_galvae_bilidh_cloak_red,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_42_elder","Cuarnaca", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_galvae_bilidh_cloak,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_43_elder","Cuarnaca", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_gatheredcloaks4,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_44_elder","Cuarnaca", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_gatheredcloaks5,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_45_elder","Cuarnaca", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_galvae_bilidh_cloak_green,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_46_elder","Cuarnaca", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_galvae_bilidh_cloak_red,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
#union
["village_47_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_union_civ_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_48_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_union_civ_2,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_49_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_50_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_51_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_union_civ_3,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_52_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_53_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_union_civ_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["village_54_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_union_civ_2,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_55_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_union_civ_3,
  
  itm_bandit_hood_red,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_56_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_57_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_union_civ_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_58_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_union_civ_2,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_59_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_union_civ_3,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_60_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_union_civ_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_61_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_union_civ_2,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_62_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_63_elder","Gezaratki", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_union_civ_3,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
#vitzland
["village_64_elder","Aufsicht", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_irregular_uniform_guard_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_65_elder","Aufsicht", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_irregular_uniform_guard_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_66_elder","Aufsicht", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_67_elder","Aufsicht", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_68_elder","Aufsicht", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_pistol_ammo,
  itm_vitzland_pistol,
  
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_69_elder","Aufsicht", "{!}village_1_elder",tf_woman|tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, woman_face_1,woman_face_2],
["village_70_elder","Aufsicht", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_71_elder","Aufsicht", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_72_elder","Aufsicht", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_73_elder","Aufsicht", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_74_elder","Aufsicht", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_75_elder","Aufsicht", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
#republic
["village_76_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_republican_civ_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_77_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_republican_civ_2,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_78_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_republican_civ_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_79_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_republican_civ_2,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_80_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_republican_civ_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_81_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_republican_civ_2,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_82_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_republican_civ_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_83_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_republican_civ_2,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_84_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_republican_civ_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_85_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_republican_civ_2,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_86_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_republican_civ_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_87_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_republican_civ_2,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
#extra
["village_88_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_89_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_90_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_91_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_92_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_93_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_94_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_95_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_96_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_97_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_98_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_99_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_100_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_101_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_102_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_103_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_104_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_poor_shirt_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_105_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_106_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_irregular_uniform_guard_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_107_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_irregular_uniform_guard_1,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_108_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_109_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_110_elder","Saporindente", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,  [
  itm_sloppy_trench_coat,
  ], def_attrib|level(12),wp_m(100),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
# Place extra merchants before this point
["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(12),wp_m(100),knows_inventory_management_10,0],

#Used for player enterprises
["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ],  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ],    attr_lvl_10,wp_1_m,knows_battle_1, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ],  attr_lvl_10,wp_1_m,knows_battle_1, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ],      attr_lvl_10,wp_1_m,knows_battle_1, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ],    attr_lvl_10,wp_1_m,knows_battle_1, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ],    attr_lvl_10,wp_1_m,knows_battle_1, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ],    attr_lvl_10,wp_1_m,knows_battle_1, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ],    attr_lvl_10,wp_1_m,knows_battle_1, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ], attr_lvl_10,wp_1_m,knows_battle_1, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ],      attr_lvl_10,wp_1_m,knows_battle_1, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_poor_shirt_1,
  ],    attr_lvl_10,wp_1_m,knows_battle_1, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ],  attr_lvl_10,wp_1_m,knows_battle_1, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ],    attr_lvl_10,wp_1_m,knows_battle_1, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ],      attr_lvl_10,wp_1_m,knows_battle_1, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_poor_shirt_1,
  ],      attr_lvl_10,wp_1_m,knows_battle_1, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ],     attr_lvl_10,wp_1_m,knows_battle_1, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
["town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ],      attr_lvl_10,wp_1_m,knows_battle_1, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
["town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_irregular_uniform_guard_1,
  ],      attr_lvl_10,wp_1_m,knows_battle_1, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
["town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_irregular_uniform_guard_1,
  ],      attr_lvl_10,wp_1_m,knows_battle_1, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
["town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_poor_shirt_1,
  ],      attr_lvl_10,wp_1_m,knows_battle_1, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
["town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_poor_shirt_1,
  ],      attr_lvl_10,wp_1_m,knows_battle_1, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
["town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  itm_sloppy_trench_coat,
  ],      attr_lvl_10,wp_1_m,knows_battle_1, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
#
# ["town_23_master_craftsman", "{!}Town 23 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,  [
  # itm_sloppy_trench_coat,
  # ],      attr_lvl_10,wp_1_m,knows_battle_1, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
# #
# Chests
["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
  [],def_attrib|level(18),wp_m(100),knows_common, 0],
["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
  [itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],
  def_attrib|level(18),wp_m(100),knows_common, 0],
["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
  [itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_bolts, itm_tutorial_throwing_daggers],
  def_attrib|level(18),wp_m(100),knows_common, 0],

#SB : move samurai back to Rivacheg (other chests were inaccessible)
["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp_m(100),knows_common, 0],
["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp_m(100),knows_common, 0],
["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp_m(100),knows_common, 0],

["intro_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_pistol_ammo, itm_pistol_ammo, itm_sausages],def_attrib|level(18),wp_m(100),knows_common, 0],
["intro_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_rifle_ammo, itm_rifle_ammo, itm_canned_meat, itm_wine_s],def_attrib|level(18),wp_m(100),knows_common, 0],


["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp_m(100),knows_inventory_management_10, 0],

# These are used as arrays in the scripts. #SB : give full inventory
["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp_m(100),knows_inventory_management_10, 0],
["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp_m(100),knows_inventory_management_10, 0],
["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp_m(100),knows_inventory_management_10, 0],

["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [],    lord_attrib,wp_m(230),lord_skills, 0x000000000008010b01f041a9249f65fd],

#Player history array
["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_has_body, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(12),wp_m(100),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_has_body, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(12),wp_m(100),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_has_body, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(12),wp_m(100),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_has_body, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(12),wp_m(100),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_has_body, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(12),wp_m(100),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_has_body, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(12),wp_m(100),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_has_body, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(12),wp_m(100),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_has_body, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(12),wp_m(100),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_has_body, 0,0, fac_commoners,[itm_butchering_knife],def_attrib|level(12),wp_m(100),knows_power_strike_1, merchant_face_1, merchant_face_2],

["swadian_merchant", "Tucker", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [  ],
  attr_lvl_10,wp_1_m,knows_battle_1, man_face_middle_1, mercenary_face_2],

["startup_merchants_end","startup_merchants_end","startup_merchants_end",tf_hero, 0,0, fac_commoners,
  [],def_attrib|level(12),wp_m(100),knows_inventory_management_10,0],

["intro_prisoner", "Prisoner", "Prisoner", tf_hero|tf_randomize_face, 0, reserved, fac_commoners,
  [itm_poor_shirt_1,itm_head_wrappings],attr_lvl_5,wp_common,knows_common, man_face_middle_1, mercenary_face_2],

["sea_raider_leader","Madman","Sea Raider Captains",tf_hero|tf_guarantee_all_wo_ranged,0,0,fac_outlaws,
  [itm_poor_shirt_1,itm_head_wrappings  ],
  def_attrib|level(24),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,mercenary_face_2, nord_face_old_2],

["looter_leader","Madman","Looters",tf_hero,0,0,fac_outlaws,
  [itm_poor_shirt_1,itm_head_wrappings  ],
  def_attrib|level(4),wp(20),knows_common,0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2],

  ["bandit_leaders_end","bandit_leaders_end","bandit_leaders_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,
  [],def_attrib|level(1),wp_m(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2, 0x00000000320410022d2595495491afa400000000001d9ae30000000000000000, mercenary_face_2],

["relative_of_merchants_end","relative_of_merchants_end","relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(12),wp_m(100),knows_inventory_management_10,0],

##diplomacy begin #SB : fixed plural name (hero name), TODO actually use name/gender in hiring dialogues
["dplmc_chamberlain","Chamberlain", "Chamberlain",
  tf_hero|tf_man,0,0,fac_commoners,
  [
  itm_sloppy_trench_coat,
  ],
  def_attrib|level(10), wp_m(100),knows_inventory_management_10,
  0x0000000dfc0c238838e571c8d469c91b00000000001e39230000000000000000],

["dplmc_constable","Constable","Constable",tf_hero|tf_man,0,0,fac_commoners,
  [
  itm_dplmc_coat_of_plates_red_constable,
  ],
  lord_attrib,wp_m(200),knows_common,
  0x0000000b4b1015054b1b4d591cba28d300000000001e472b0000000000000000],

["dplmc_chancellor","Diplomat","Diplomat",tf_hero|tf_man,0,0,fac_commoners,
  [
  itm_civilian_outfit_1,
  ],
  def_attrib|level(10), wp_m(100),knows_inventory_management_10,
  0x00000009a20c21cf491bad28a28628d400000000001e371a0000000000000000],

["dplmc_messenger","Messenger","Messengers",tf_mounted|tf_has_body|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
  [
  itm_civilian_outfit_1,
  ],
  def_attrib|agi_21|int_30|cha_21|level(25),wp_m(230),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,
  man_face_young_1,man_face_old_2],

["dplmc_scout","Scout","Scouts",tf_mounted|tf_has_body|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
  [
  itm_civilian_outfit_1,
  ],
  def_attrib|agi_21|int_30|cha_21|level(25),wp_m(230),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,
  man_face_young_1,man_face_old_2],
# recruiter kit begin
["dplmc_recruiter","Recruiter","Recruiter",tf_mounted|tf_has_body|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
  [
  itm_civilian_outfit_1,
  ],
  def_attrib|agi_21|int_30|cha_21|level(25),wp_m(230),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,
  swadian_face_young_1, swadian_face_old_2],
# recruiter kit end
##diplomacy end

# pseudo troops
["pseudo_troop_01","Gjalfrmarr","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0], #economy logger (plural name)
["pseudo_troop_02","Eydendr","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0], #player army logger (plural name)
["pseudo_troop_03","Gunnmas","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0], #bandits logger (plural name)
["pseudo_troop_04","Sundvargs","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["pseudo_troop_05","Unnswin","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["pseudo_troop_06","Bengrefill","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["pseudo_troop_07","Elgslagar","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["pseudo_troop_08","Arajo","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["pseudo_troop_09","Byrskids","pt",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["pseudo_troop_end","Second Outfit","pseudo_troop_end",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],

["scavenge_troop","Scavenge loot","Scavenge loot",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["scavenge_troop_wasteland","Scavenge loot","Scavenge loot",tf_hero,no_scene,reserved,fac_commoners,[
],def_attrib,0,knows_common|knows_inventory_management_10,0],
["scavenge_troop_forest","Scavenge loot","Scavenge loot",tf_hero,no_scene,reserved,fac_commoners,[
],def_attrib,0,knows_common|knows_inventory_management_10,0],
["scavenge_troop_city","Scavenge loot","Scavenge loot",tf_hero,no_scene,reserved,fac_commoners,[
],def_attrib,0,knows_common|knows_inventory_management_10,0],
["scavenge_troop_warehouse","Scavenge loot","Scavenge loot",tf_hero,no_scene,reserved,fac_commoners,[
],def_attrib,0,knows_common|knows_inventory_management_10,0],
["vehicle_troop","vehicle_troop","vehicle_troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["vehicle_garage","vehicle_garage","vehicle_garage",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
# ["workbench", "Workbench", "Workbench", tf_guarantee_boots|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves, 0, 0, fac_neutral,
  # [
  # itm_invisi_body,itm_invisi_head,itm_invisi_gloves,itm_invisi_boots
  # ],
  # def_attrib|level(12), wp_m(100),knows_inventory_management_10,0,0,"tools_mesh"],
# ["consume", "Consume", "Consume", tf_guarantee_boots|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves, 0, 0, fac_neutral,
  # [
  # itm_invisi_body,itm_invisi_head,itm_invisi_gloves,itm_invisi_boots
  # ],
  # def_attrib|level(12), wp_m(100),knows_inventory_management_10,0,0],
["wanted_sign", "Wanted Sign", "Wanted Sign", tf_guarantee_boots|tf_has_body|tf_guarantee_helmet|tf_guarantee_gloves, 0, 0, fac_neutral,
  [
  itm_invisi_body,itm_invisi_head,itm_invisi_gloves,itm_invisi_boots
  ],
  def_attrib|level(12), wp_m(100),knows_inventory_management_10,0,0],

["dog_companion","Dog","Dogs",tf_hero|tf_dummy|tf_guarantee_all,
  0,0,fac_commoners,
  [
  itm_dog_companion_horse,
  itm_dog_bite
  ],
  level(10)|str_5|agi_5, wp_polearm(50),knows_ironflesh_2|knows_riding_3,
  0, 0],
["bot_companion","Bot","Bots",tf_hero|tf_dummy|tf_guarantee_all,
  0,0,fac_commoners,
  [
  itm_bot_companion_horse
  ],
  level(10)|str_5|agi_5, wp(50),knows_ironflesh_2|knows_riding_2|knows_inventory_management_10,
  0, 0],

["car_mechanic","Auto Mechanic","Auto Mechanics",
  tf_has_body|tf_has_ranged,no_scene,0,fac_commoners,
  [
  itm_spanner,
  itm_crowbar,
  itm_wrench,
  itm_monkeywrench,
  itm_screwdriver,
  itm_screwdriver2,

  itm_mechanic,
  itm_mechanic_blue,
  itm_mechanic_brown,
  itm_mechanic_green,
  itm_mechanic_red,
  itm_fisher,
  itm_fisher_2,
  itm_fisher_3,

  itm_welder_mask,
  itm_welder_mask_ms,

  itm_bandana_camo,
  itm_bandana_black,
  itm_bandana_blue,
  itm_bandana_red,
  itm_bandana_green,
  itm_bandana_white,
  itm_goggles_1,
  itm_pistol_ammo,
  ]+revolvers,
  attr_lvl_15,wp_2_r,knows_battle_2,mercenary_face_1, mercenary_face_2],
["car_gunner","Auto Gunner","Auto Gunners",
  tf_has_body|tf_has_ranged|tf_allways_fall_dead|tf_mounted|tf_guarantee_all|tf_guarantee_horse,no_scene,0,fac_commoners,
  [
  itm_car,
  
  itm_mg_auto_cannon,
  
  itm_mg_ammo,
  itm_mg_ammo_pw,

  itm_knife,

  itm_irregular_uniform_regular,
  
  itm_black_gloves,
  ],
  attr_lvl_15,wp_2_r,knows_battle_2|knows_horse_archery_10,mercenary_face_1, mercenary_face_2],

["chopper_mechanic","Aeromobile_Mechanic","Aeromobile_Mechanics",
  tf_has_body|tf_has_ranged,no_scene,0,fac_commoners,
  [
  itm_spanner,
  itm_crowbar,
  itm_wrench,
  itm_monkeywrench,
  itm_screwdriver,
  itm_screwdriver2,

  itm_mechanic,
  itm_mechanic_blue,
  itm_mechanic_brown,
  itm_mechanic_green,
  itm_mechanic_red,
  itm_fisher,
  itm_fisher_2,
  itm_fisher_3,

  itm_welder_mask,
  itm_welder_mask_ms,

  itm_bandana_camo,
  itm_bandana_black,
  itm_bandana_blue,
  itm_bandana_red,
  itm_bandana_green,
  itm_bandana_white,
  itm_goggles_1,

  itm_pistol_ammo,
  ]+revolvers,
  attr_lvl_15,wp_2_r,knows_battle_2,mercenary_face_1, mercenary_face_2],

["chopper_pilot","Aeromobile_Pilot","Aeromobile_Pilots",
  tf_man_high|tf_has_body|tf_has_ranged|tf_allways_fall_dead|tf_guarantee_all,no_scene,0,fac_commoners,
  [
  itm_heli,
  
  (itm_mg_auto_cannon, imod_masterwork),
  itm_mg_ammo_pw,
  itm_mg_ammo_pw,
  
  itm_invisi_boots,
  itm_invisi_gloves,
  itm_invisi_head,
  ],
  str_24|agi_16|int_7|cha_7|level(60),wp_r(950),knows_battle_2|knows_riding_10|knows_horse_archery_10,mercenary_face_1, mercenary_face_2],

["bus_mechanic","bus_mechanic","bus_mechanic", #copy
  tf_has_body|tf_has_ranged,no_scene,0,fac_commoners,
  [


  ],
  attr_lvl_15,wp_2_m,knows_battle_2,mercenary_face_1, mercenary_face_2],
["bus_gunner","bus_gunner","bus_gunner", #copy
  tf_has_body|tf_has_ranged|tf_allways_fall_dead|tf_mounted|tf_guarantee_horse,no_scene,0,fac_commoners,
  [
  itm_bus,

  ],
  attr_lvl_15,wp_2_r,knows_battle_2,mercenary_face_1, mercenary_face_2],


]
# troops.extend(random_troop(i) for i in xrange(1000))
# troops.extend(random_troop_w(i) for i in xrange(250))
# # troops.extend(["player_%d" % i, "Player %d" % i, "None", tf_hero, 0, 0, 0, [], str_4|agi_4|int_4|cha_4, wp(15), 0, 0] for i in xrange(255)),
# # troops.extend(["custom_bandit_%d" % i, "Bandit Troop %d" % i, "None", tf_guarantee_armor, 0, 0, 0, [], str_4|agi_4|int_4|cha_4, wp_m(50), 0, mercenary_face_1, mercenary_face_2] for i in xrange(100)),
# # troops.extend(["custom_troop_%d" % i, "Custom Troop %d" % i, "None", tf_guarantee_armor, 0, 0, 0, [], str_4|agi_4|int_4|cha_4, wp_m(50), 0, mercenary_face_1, mercenary_face_2] for i in xrange(100)),
# # troops.extend(["custom_hero_%d" % i, "Custom Hero %d" % i, "None", tf_hero, 0, 0, 0, [], str_4|agi_4|int_4|cha_4, wp(50), 0, mercenary_face_1, mercenary_face_2] for i in xrange(100)),

#Troop upgrade declarations

#mercenaries
upgrade(troops,"traveler", "watchman")
upgrade(troops,"farmer", "watchman")
upgrade(troops,"watchman","caravan_guard")
upgrade(troops,"caravan_guard","mercenary_swordsman")
upgrade(troops,"mercenary_swordsman","hired_blade")
upgrade(troops,"hired_blade","sentinel")

#rangers
upgrade(troops,"scout","lookout")
upgrade(troops,"lookout","spotter")
upgrade(troops,"spotter","ranger")

#riders
upgrade(troops,"mercenary_horseman","mercenary_cavalry")

#sharpshooters
upgrade2(troops,"mercenary_gunslinger","mercenary_rifleman","mercenary_shotgunner")
upgrade(troops,"mercenary_rifleman","mercenary_sniper")
upgrade(troops,"mercenary_shotgunner","mercenary_grenadier")

#toughs
upgrade(troops,"mercenary_brawler","mercenary_powerfist")

#shadow_operative
upgrade2(troops,"shadow_operative_regular","shadow_operative_officer","shadow_operative_gunner")
upgrade2(troops,"shadow_operative_officer","shadow_operative_elite","shadow_operative_saboteur")
upgrade(troops,"shadow_operative_elite","shadow_operative_knight")

#yanizari
upgrade(troops,"mercenary_hunter","mercenary_archer")
upgrade(troops,"mercenary_horsearcher","sentinel_horsearcher")

#fallen_phalanx
upgrade(troops,"phalanx_fresh","phalanx_firstblood")
upgrade(troops,"phalanx_firstblood","phalanx_bloodied")
upgrade(troops,"phalanx_bloodied","phalanx_scarred")
upgrade(troops,"phalanx_scarred","phalanx_chosen")

#nomads
upgrade(troops,"nomad_wastrel","nomad_vagabond")
upgrade(troops,"nomad_vagabond","nomad_drifter")
upgrade(troops,"nomad_drifter","nomad_wanderer")

################
####Factions####
################
##Entenaii Empire
upgrade(troops,"f1_tier_0","f1_tier_1")
upgrade(troops,"f1_tier_1","f1_tier_2")
upgrade(troops,"f1_tier_2","f1_tier_3")
upgrade2(troops,"f1_tier_3","f1_tier_4","f1_tier_4_cavalry")
upgrade2(troops,"f1_tier_4","f1_tier_5","f1_tier_5_infantry")
upgrade(troops,"f1_tier_4_cavalry","f1_tier_5_cavalry")
upgrade2(troops,"f1_tier_5","f1_tier_6_sniper","f1_tier_6_specialist")
#guards
upgrade(troops,"f1_guard","f1_castle_guard")
upgrade(troops,"f1_castle_guard","f1_hall_guard")
#mech
upgrade(troops,"f1_mech","f1_mech_emperor")

##Entenaii Dominion
upgrade(troops,"f2_tier_0","f2_tier_1")
upgrade(troops,"f2_tier_1","f2_tier_2")
upgrade(troops,"f2_tier_2","f2_tier_3")
upgrade2(troops,"f2_tier_3","f2_fanatic","f2_tier_4")
upgrade2(troops,"f2_fanatic","f2_flamer","f2_rider")
upgrade(troops,"f2_tier_4","f2_tier_5")
#guards
upgrade(troops,"f2_guard","f2_castle_guard")
upgrade(troops,"f2_castle_guard","f2_hall_guard")

##Kingdom of Galvae
upgrade(troops,"f3_tier_0","f3_tier_1")
upgrade(troops,"f3_tier_1","f3_tier_2")
upgrade2(troops,"f3_tier_2","f3_tier_3","f3_rider")
upgrade2(troops,"f3_tier_3","f3_tier_4","f3_infantry")
upgrade(troops,"f3_rider","f3_vet_rider")
upgrade(troops,"f3_tier_4","f3_tier_5")
#guards
upgrade(troops,"f3_guard","f3_castle_guard")
upgrade(troops,"f3_castle_guard","f3_hall_guard")

##Molvat-Berchav Union
upgrade(troops,"f4_tier_0","f4_tier_1")
upgrade(troops,"f4_tier_1","f4_tier_2")
upgrade2(troops,"f4_tier_2","f4_tier_3b","f4_tier_3")
upgrade2(troops,"f4_tier_3b","f4_tier_4","f4_sniper")
upgrade(troops,"f4_tier_3","f4_tier_4_cavalry")
upgrade(troops,"f4_tier_4_cavalry","f4_tier_5_cavalry")
upgrade(troops,"f4_tier_5_cavalry","f4_tier_6_cavalry")
upgrade2(troops,"f4_tier_4","f4_tier_5","f4_flamer")
upgrade(troops,"f4_tier_5","f4_tier_6")
#guards
upgrade(troops,"f4_guard","f4_castle_guard")
upgrade(troops,"f4_castle_guard","f4_hall_guard")

##Vitzland Territories
upgrade(troops,"f5_tier_0","f5_tier_1")
upgrade(troops,"f5_tier_1","f5_tier_2")
upgrade2(troops,"f5_tier_2","f5_tier_3","f5_rider")
upgrade(troops,"f5_rider","f5_rider_vet")
upgrade2(troops,"f5_tier_3","f5_tier_4","f5_flamer")
upgrade2(troops,"f5_tier_4","f5_tier_5","f5_gunner")
upgrade(troops,"f5_tier_5","f5_tier_6")
#guards
upgrade(troops,"f5_guard","f5_castle_guard")
upgrade(troops,"f5_castle_guard","f5_hall_guard")

##Trezzo Republic
upgrade(troops,"f6_tier_0","f6_tier_1")
upgrade(troops,"f6_tier_1","f6_tier_2")
upgrade(troops,"f6_tier_2","f6_tier_3")
upgrade2(troops,"f6_tier_3","f6_tier_4","f6_rider")
upgrade2(troops,"f6_tier_4","f6_tier_5","f6_tier_5_engineer")
upgrade(troops,"f6_tier_5","f6_tier_6")
#guards
upgrade(troops,"f6_guard","f6_castle_guard")
upgrade(troops,"f6_castle_guard","f6_hall_guard")

##Itami Castedom
upgrade(troops,"f7_tier_0","f7_tier_1")
upgrade(troops,"f7_tier_1","f7_tier_2")
upgrade(troops,"f7_tier_2","f7_tier_3")
upgrade2(troops,"f7_tier_3","f7_tier_4","f7_rider")
upgrade2(troops,"f7_tier_4","f7_tier_5","f7_tier_5_engineer")
upgrade(troops,"f7_tier_5","f7_tier_6")
#guards
upgrade(troops,"f7_guard","f7_castle_guard")
upgrade(troops,"f7_castle_guard","f7_hall_guard")

##Irregular
upgrade(troops,"irregular_tier_0","irregular_tier_1")
upgrade(troops,"irregular_tier_1","irregular_tier_2")
upgrade(troops,"irregular_tier_2","irregular_tier_3")
upgrade2(troops,"irregular_tier_3","irregular_tier_4","irregular_rider")
upgrade(troops,"irregular_tier_4","irregular_tier_5")
#guards
upgrade(troops,"irregular_guard","irregular_castle_guard")
upgrade(troops,"irregular_castle_guard","irregular_hall_guard")

upgrade(troops,"throd_tier_0","throd_tier_1")
upgrade(troops,"throd_tier_1","throd_tier_2")
upgrade(troops,"throd_tier_2","throd_tier_3")
upgrade2(troops,"throd_tier_3","throd_tier_4","throd_rider")
upgrade(troops,"throd_tier_4","throd_tier_5")
#guards
upgrade(troops,"throd_guard","throd_castle_guard")
upgrade(troops,"throd_castle_guard","throd_hall_guard")

################

#bandits
upgrade(troops,"looter","bandit")
upgrade2(troops,"bandit","raider","thug")
upgrade2(troops,"raider","predator","marauder")
upgrade(troops,"predator","predator_legend")
upgrade(troops,"marauder","marauder_legend")
upgrade(troops,"thug","bandit_chief")

upgrade(troops,"wasteland_bandit","wasteland_raider")
upgrade2(troops,"wasteland_raider","wasteland_predator","wasteland_marauder")
upgrade(troops,"wasteland_predator","warlord")

#cannibal
upgrade(troops,"cannibal","cannibal_cruel")

#cultists
upgrade(troops,"cultist","fanatic")
upgrade(troops,"fanatic","zealot")

#infected
upgrade2(troops,"infected_1","infected_2","infected_6")
upgrade2(troops,"infected_2","infected_3","infected_4")
upgrade(troops,"infected_3","infected_5")
#boar
upgrade2(troops,"jackal_raider","jackal_predator","jackal_marauder")
upgrade(troops,"jackal_predator","jackal_chieftain")

#vigilante
upgrade(troops,"manhunter","manhunter_exp")
upgrade(troops,"manhunter_exp","manhunter_veteran")

#military_police
upgrade(troops,"military_police_trooper","military_police_sergeant")
upgrade(troops,"military_police_sergeant","military_police_officer")

#press gang
upgrade(troops,"slave_driver","slave_hunter")
upgrade(troops,"slave_hunter","slaver_chief")

#bounty hunter
upgrade(troops,"bounty_hunter","bounty_hunter_legend")

#candles
upgrade(troops,"traveler_w","follower_woman")
upgrade(troops,"peasant_woman","follower_woman")
upgrade(troops,"follower_woman","hunter_woman")
upgrade(troops,"hunter_woman","fighter_woman")
upgrade(troops,"fighter_woman","sword_sister")

#outlaw
upgrade(troops,"scavenger_violent","scavenger_vet_violent")
upgrade2(troops,"scavenger_vet_violent","scavenger_legend_violent","scavenger_power_violent")

upgrade2(troops,"gunslinger","assassin","gunner")
upgrade2(troops,"assassin","sniper","saboteur")
upgrade(troops,"sniper","assassin_sniper")

upgrade2(troops,"thief","criminal","slaver")
upgrade2(troops,"criminal","outlaw","highwayman")
upgrade2(troops,"slaver","bruiser","slasher")
upgrade(troops,"slasher","butcher_thug")
upgrade(troops,"bruiser","enforcer")

upgrade(troops,"ezeg","ezeg_raider")
upgrade(troops,"ezeg_raider","ezeg_corsair")
upgrade(troops,"ezeg_corsair","ezeg_pillager")

upgrade(troops,"techno_thief","criminal_escaped")
upgrade(troops,"criminal_escaped","smuggler")

#mutant
upgrade(troops,"feral_beastling","wolfclaw_mutant")
upgrade(troops,"wolfclaw_mutant","wolfclaw_mutant_big")
upgrade(troops,"ghoul","ghoul_scavenger")
upgrade(troops,"mutant_spider","mutant_spider_big")
upgrade(troops,"brute_mutant","tank_mutant")
upgrade2(troops,"acid_mutant","nark_mutant_1","spitter")

upgrade(troops,"risen","risen_tainted")
upgrade(troops,"risen_tainted","risen_cursed")

# modmerger_start version=201 type=2
try:
    component_name = "troops"
    var_set = { "troops" : troops }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
