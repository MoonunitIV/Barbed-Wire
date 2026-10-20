from module_constants import *
from ID_factions import *
from ID_sounds import *
from header_items import  *
from header_operations import *
from header_triggers import *

# from compiler import *
####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################
def heraldic(item_tableau):
  return (ti_on_init_item, [(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner", item_tableau,":agent_no",":troop_no")])
def add_mesh(item_meshes):
  cur_meshes = [(store_trigger_param_1,":agent_no"),(ge,":agent_no", 0)]
  for mesh in item_meshes if not isinstance(item_meshes, basestring) else [item_meshes]:
    cur_meshes.append((str_store_string, s1, mesh))
    cur_meshes.append((cur_item_add_mesh, s1))
  return (ti_on_init_item, cur_meshes)
def reskin(item_material):
  return (ti_on_init_item, [(str_store_string, s1, item_material),(cur_item_set_material, s1, 0),])
####################################################################################################################
bullet_impact = (ti_on_missile_hit, [
  (store_trigger_param_1,":shooter"),
  #(store_mission_timer_a, ":time"),
  #(val_add, ":time", 30),
  #(agent_set_slot, ":shooter", slot_agent_last_time_hit_enemy, ":time"),	#for leaving cover if not shot in a while
 
  (neg|is_currently_night),

  (set_fixed_point_multiplier, 100),
  (store_trigger_param_2,":struck"),
  (agent_get_position, pos10,":shooter"),
  (get_distance_between_positions_in_meters,":distance", pos1, pos10),
  # (val_div,":distance", 2),

  (call_script,"script_cf_bullet_collision_particle",":struck",":distance"),
  
    #robbery/rescue alert when shots land near npcs
	(eq,":shooter", "$g_player"),
	
	(this_or_next|eq,"$robbery_in_progress",1),
	(this_or_next|eq, "$talk_context", tc_prison_break),
	(this_or_next|party_slot_eq, "$current_town", slot_center_has_attacker,3),#make it work during bandit attack
	(eq, "$talk_context", tc_escape),
	#(agent_get_position, pos12, ":target"),
	
		
	# (str_store_agent_name, s23, ":shooter"),
	# (assign, reg21, ":shooter"),
	# (display_message, "@{s23} bullet impact", message_negative),
	
	(copy_position, pos12, pos1),
	(assign, ":ammo_type", "itm_buckshot_ammo"),
	
	(call_script, "script_hit_alerts_guards_panicks_civilians", ":shooter", ":ammo_type"),#needs target in pos12

  ])

smaller_bullet_impact = (ti_on_missile_hit, [
  (store_trigger_param_1,":shooter"),
  #(store_mission_timer_a, ":time"),
  #(val_add, ":time", 30),
 # (agent_set_slot, ":shooter", slot_agent_last_time_hit_enemy, ":time"),	#for leaving cover if not shot in a while
  
  (neg|is_currently_night),

  (set_fixed_point_multiplier, 100),
  (store_trigger_param_2,":struck"),
  (agent_get_position, pos10,":shooter"),
  (get_distance_between_positions_in_meters,":distance", pos1, pos10),
  (val_div,":distance", 2),
  # (val_div,":distance", 4),
  
  (call_script,"script_cf_bullet_collision_particle",":struck",":distance"),
  
    #robbery/rescue alert when shots land near npcs
	(eq,":shooter", "$g_player"),
	
	(this_or_next|eq,"$robbery_in_progress",1),
	(this_or_next|eq, "$talk_context", tc_prison_break),
	(this_or_next|party_slot_eq, "$current_town", slot_center_has_attacker,3),#make it work during bandit attack
	(eq, "$talk_context", tc_escape),
	#(agent_get_position, pos12, ":target"),
	
		
	# (str_store_agent_name, s23, ":shooter"),
	# (assign, reg21, ":shooter"),
	# (display_message, "@{s23} bullet impact", message_negative),
	
	(copy_position, pos12, pos1),
	(assign, ":ammo_type", "itm_buckshot_ammo"),
	
	(call_script, "script_hit_alerts_guards_panicks_civilians", ":shooter", ":ammo_type"),#needs target in pos12

  ])

ranged_weapon_triggers = (ti_on_weapon_attack, [
  (store_trigger_param_1,":shooter"),
  (store_mission_timer_a, ":time"),
  (val_add, ":time", 30),
  (agent_set_slot, ":shooter", slot_agent_last_time_hit_enemy, ":time"),	#for leaving cover if not shot in a while
  #(str_store_agent_name, s23, ":shooter"),
  #(assign, reg21, ":shooter"),
  #(assign, reg22, ":time"),
  #(display_message, "@{s23}{reg21} time is: {reg22}", message_negative),
  
  # #robbery/rescue alert when shooting
	# (eq,":shooter", "$g_player"),
	
	# (str_store_agent_name, s23, ":shooter"),
	# (assign, reg21, ":shooter"),
	# (assign, reg22, ":time"),
	# (display_message, "@{s23}{reg21} time is: {reg22}", message_negative),

	
	# (this_or_next|eq,"$robbery_in_progress",1),
	# (this_or_next|eq, "$talk_context", tc_prison_break),
	# (this_or_next|party_slot_eq, "$current_town", slot_center_has_attacker,3),#make it work during bandit attack
	# (eq, "$talk_context", tc_escape),
	# #(agent_get_position, pos12, ":target"),
	
	# (agent_get_wielded_item, ":wielded", ":shooter", 0),
	# #(gt, ":wielded", 0),
	# (gt, ":wielded", 0),
	# (assign, ":ammo_type", -1),
	# (try_begin),
		# (item_slot_eq, ":wielded", slot_item_ammo_type, ammo_pistol),
		# (assign, ":ammo_type", "itm_pistol_ammo"),
	  # (else_try),
		# (item_slot_eq, ":wielded", slot_item_ammo_type, ammo_rifle),
		# (assign, ":ammo_type", "itm_rifle_ammo"),
	  # (else_try),
		# (item_slot_eq, ":wielded", slot_item_ammo_type, ammo_shotgun),
		# (assign, ":ammo_type", "itm_buckshot_ammo_pw"),
	  # (else_try),
		# (item_slot_eq, ":wielded", slot_item_ammo_type, ammo_large_caliber),
		# (assign, ":ammo_type", "itm_large_caliber_ammo"),
	  # (else_try),
		# (item_slot_eq, ":wielded", slot_item_ammo_type, ammo_mg),
		# (assign, ":ammo_type", "itm_mg_ammo"),
	  # (else_try),
		# (item_slot_eq, ":wielded", slot_item_ammo_type, ammo_plasma),
		# (assign, ":ammo_type", "itm_plasma_ammo"),
	  # (else_try),
		# (is_between, ":wielded", grenades_begin, grenades_end),
		# (assign, ":ammo_type", "itm_flameammo"),
	  # (try_end),
	  
	# (gt, ":ammo_type", 0),
	
	# (agent_get_bone_position, pos22, ":shooter", hb_item_r, 1),
  # (agent_get_look_position, pos2, ":shooter"),
  # (position_copy_rotation, pos22, pos2),
  # (position_move_x, pos12, -8, 0),
  # (position_move_z, pos12, 11, 1),
	
	# (item_get_weapon_length, ":length", ":wielded"),
    # (position_move_y,pos22,":length"),
	
      # (cast_ray, ":unused", pos12, pos22),
	# (call_script, "script_hit_alerts_guards_panicks_civilians", ":shooter", ":ammo_type"),#needs target in pos12
  ])
  # (ti_on_init_item, [
    # (store_trigger_param_1,":agent"),
    # (store_trigger_param_2,":troop"),
    # (try_begin),
      # (gt,":agent",0),
      # (eq,":troop","trp_player"),
      # (str_store_string, s11,"@assault_remington_m4_marksman.1"),
      # (cur_item_add_mesh, s11),
    # (try_end),
# ])
  
scope_add = (ti_on_init_item, [
    (store_trigger_param_1,":shooter"),
    (store_trigger_param_2,":troop"),
    #(store_trigger_param_3,":item"),#doesn't work
    (try_begin),
      (gt,":shooter",0),
      (eq,":troop","trp_player"),
	  #(agent_get_wielded_item, ":item", ":shooter", 0), #doesn't work, added with NouH python script at bottom of file - krag
	  
	  # (try_begin),
		  # (str_store_string, s11,"@flashlight_addon_mesh"),
		  # (cur_item_add_mesh, s11),
		  # (str_store_string, s12,"@flashlight_addon_mesh_beam"),
		  # (cur_item_add_mesh, s12),
      # (try_end),
	  
	  (try_begin),
		  (item_slot_ge, ":item", slot_item_has_crafted_scope, 1),
		  #(eq,":troop","trp_player"),
		  #(neg|item_has_property, ":item", itp_couchable),
		  (item_get_type,  ":type", ":item"),
		   (try_begin),
			  (eq, ":type", itp_type_pistol),
			  (str_store_string, s11,"@scope_addon_mesh_pistol"),
			 (else_try), 
			  (is_between,":item", "itm_assault_ak47", itm_assault_ak47imp+1),
			  (str_store_string, s11,"@scope_addon_mesh_ak"),
			 (else_try), 
			  (this_or_next|eq,":item", "itm_rifle_plasma"),
			  (this_or_next|is_between,":item", lmg_begin, lmg_end),
			  (is_between,":item", a_rifle_begin, a_rifle_end),
			  (str_store_string, s11,"@scope_addon_mesh_assault"),
			 (else_try), 
			  (str_store_string, s11,"@scope_addon_mesh"),
		  (try_end),
		  (cur_item_add_mesh, s11),
      (try_end),
	  
	  (try_begin),
		  (item_slot_ge, ":item", slot_item_has_crafted_laser_sight, 1),
		  #(troop_is_hero,":troop"),
		   (item_get_type,  ":type", ":item"),
		   (try_begin),
			  (eq, ":type", itp_type_pistol),
			  (str_store_string, s11,"@laser_sight_addon_mesh_pistol"),
			  (try_begin),
				(is_currently_night),
				(store_current_scene, ":scene"),
				(neg|is_between,":scene", "scn_town_1_castle", "scn_town_1_alley"),
				(agent_get_item_slot, ":head_gear", ":shooter", ek_head),
				(eq, ":head_gear", "itm_upgrade_vision"),
				(is_between, ":head_gear", "itm_ach_full", "itm_army_cap_1"),
				
				(str_store_string, s12,"@laser_beam_addon_mesh_pistol_nv"),
			   (else_try),
				(str_store_string, s12,"@laser_beam_addon_mesh_pistol"),
			  (try_end),
			  
			 (else_try), 
			  (this_or_next|eq,":item", "itm_rifle_plasma"),
			  (this_or_next|is_between,":item", lmg_begin, lmg_end),
			  (is_between,":item", a_rifle_begin, a_rifle_end),
			  
			  (str_store_string, s11,"@laser_sight_addon_mesh_assault"),
			  (try_begin),
				(is_currently_night),
				(store_current_scene, ":scene"),
				(neg|is_between,":scene", "scn_town_1_castle", "scn_town_1_alley"),
				(agent_get_item_slot, ":head_gear", ":shooter", ek_head),
				(this_or_next|eq, ":head_gear", "itm_upgrade_vision"),
				#(this_or_next|eq, ":head_gear", "itm_helmet_gas_olive"),
				#(this_or_next|eq, ":head_gear", "itm_helmet_gas"),
				(is_between, ":head_gear", "itm_ach_full", "itm_army_cap_1"),
				
				(str_store_string, s12,"@laser_beam_addon_mesh_assault_nv"),
			   (else_try),
				(str_store_string, s12,"@laser_beam_addon_mesh_assault"),
			  (try_end),
			 (else_try), 
			  (this_or_next|is_between,":item", sniper_begin, sniper_end),
			  (is_between,":item", rifle_begin, rifle_end),
			  
			  (str_store_string, s11,"@laser_sight_addon_mesh_rifle"),
			  (try_begin),
				(is_currently_night),
				(store_current_scene, ":scene"),
				(neg|is_between,":scene", "scn_town_1_castle", "scn_town_1_alley"),
				(agent_get_item_slot, ":head_gear", ":shooter", ek_head),
				(this_or_next|eq, ":head_gear", "itm_upgrade_vision"),
				#(this_or_next|eq, ":head_gear", "itm_helmet_gas_olive"),
				#(this_or_next|eq, ":head_gear", "itm_helmet_gas"),
				(is_between, ":head_gear", "itm_ach_full", "itm_army_cap_1"),
				
				(str_store_string, s12,"@laser_beam_addon_mesh_rifle_nv"),
			   (else_try),
				(str_store_string, s12,"@laser_beam_addon_mesh_rifle"),
			  (try_end),
			 (else_try), 
			  (str_store_string, s11,"@laser_sight_addon_mesh"),
			  (try_begin),
				(is_currently_night),
				(store_current_scene, ":scene"),
				(neg|is_between,":scene", "scn_town_1_castle", "scn_town_1_alley"),
				(agent_get_item_slot, ":head_gear", ":shooter", ek_head),
				(this_or_next|eq, ":head_gear", "itm_upgrade_vision"),
				#(this_or_next|eq, ":head_gear", "itm_helmet_gas_olive"),
				#(this_or_next|eq, ":head_gear", "itm_helmet_gas"),
				(is_between, ":head_gear", "itm_ach_full", "itm_army_cap_1"),
				
				(str_store_string, s12,"@laser_beam_addon_mesh_nv"),
			   (else_try),
				(str_store_string, s12,"@laser_beam_addon_mesh"),
			  (try_end),
		  (try_end),
		  
		  (cur_item_add_mesh, s11),
		  (cur_item_add_mesh, s12),
      (try_end),
    (try_end),
	])
  
shotgun_fire_ai = (ti_on_weapon_attack,
   [
    (store_trigger_param_1,":shooter"),
    (neq,":shooter","$g_player"),#handled elsewhere
	
	#(agent_get_ammo, ":ammo", ":shooter", 1),
	(this_or_next|agent_has_item_equipped, ":shooter", "itm_buckshot_ammo_pw"),
	(agent_has_item_equipped, ":shooter", "itm_buckshot_ammo"),
	(agent_get_wielded_item, ":wielded", ":shooter", 0),
	(item_get_missile_speed, ":speed", ":wielded"),
	(val_mul, ":speed", 120),
	#(assign, ":speed", 10000), #this was for player
   # (copy_position,pos22,pos1),
	
	(set_fixed_point_multiplier,100),
	(agent_get_bone_position, pos22, ":shooter", hb_item_r, 1),
  (agent_get_look_position, pos2, ":shooter"),
  (position_copy_rotation, pos22, pos2),
  (position_move_x, pos12, -8, 0),
  (position_move_z, pos12, 11, 1),
	
	(item_get_weapon_length, ":length", ":wielded"),
    (position_move_y,pos22,":length"),
	
	(call_script, "script_gun_calculate_dispersion_ai", ":shooter", ":wielded"),
    (assign, ":dispersion", reg0),

    #(str_store_agent_name, s23, ":shooter"),
  #(assign, reg21, ":shooter"),
  #(assign, reg22, ":time"),
  #(display_message, "@{s23}{reg21} time is: {reg22}", message_negative),
   
    (try_for_range,":unused",0,9), 
        (copy_position,pos23,pos22),
        (store_random_in_range, ":y_rotation", 0, 36000),
	    (store_random_in_range, ":x_inaccuracy", 0, ":dispersion"),
	   
	    (position_rotate_y_floating, pos23, ":y_rotation"),
        (position_rotate_x_floating, pos23, ":x_inaccuracy"),
        (add_missile, ":shooter", pos23, ":speed", ":wielded", 0, "itm_buckshot_ammo", 0),
    (try_end),
    ])
	
####################################################################################################################
imodbits_none=0
imodbits_horse_basic=imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth=imodbit_tattered|imodbit_ragged|imodbit_sturdy|imodbit_thick|imodbit_hardened|imodbit_reinforced
imodbits_armor=imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude|imodbit_thick|imodbit_reinforced|imodbit_lordly
imodbits_polearm=imodbit_cracked|imodbit_bent|imodbit_balanced
imodbits_shield=imodbit_cracked|imodbit_battered|imodbit_thick|imodbit_reinforced
imodbits_sword=imodbit_rusty|imodbit_chipped|imodbit_balanced|imodbit_tempered
imodbits_sword_high=imodbit_rusty|imodbit_chipped|imodbit_balanced|imodbit_tempered|imodbit_masterwork
imodbits_mace=imodbit_rusty|imodbit_chipped|imodbit_balanced|imodbit_heavy
imodbits_bow=imodbit_cracked|imodbit_bent|imodbit_strong|imodbit_masterwork
imodbits_missile=imodbit_bent|imodbit_large_bag
imodbits_thrown=imodbit_bent|imodbit_heavy|imodbit_balanced|imodbit_large_bag
imodbits_gun=imodbit_cracked|imodbit_rusty|imodbit_balanced|imodbit_masterwork
imodbits_car=imodbit_rusty|imodbit_bent|imodbit_chipped|imodbit_battered|imodbit_poor|imodbit_crude|imodbit_old|imodbit_cheap #removed imodbit_cracked| as there's no function to repair them.... - krag

imodbits_horse_good=imodbit_spirited|imodbit_heavy
imodbits_good=imodbit_sturdy|imodbit_thick|imodbit_hardened|imodbit_reinforced
imodbits_bad=imodbit_rusty|imodbit_chipped|imodbit_tattered|imodbit_ragged|imodbit_cracked|imodbit_bent
####################################################################################################################
items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
["no_item","INVALID ITEM", [("dummy_mesh",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

##************************************************************************************************
## CLUSTER
##************************************************************************************************
["tutorial_spear","Spear",[("dummy_mesh",0)],itp_type_two_handed_wpn|itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_spear,0,weight(4.5)|spd_rtng(80)|weapon_length(158)|swing_damage(0,cut)|thrust_damage(19,pierce),imodbits_polearm],
["tutorial_club","Club",[("dummy_mesh",0)],itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_wooden_attack,itc_scimitar,0,weight(2.5)|spd_rtng(95)|weapon_length(95)|swing_damage(11,blunt),imodbits_none],
["tutorial_battle_axe","Battle_Axe",[("dummy_mesh",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry,itc_nodachi|itcf_carry_axe_back,0,weight(5)|spd_rtng(88)|weapon_length(108)|swing_damage(27,cut),imodbits_mace],
["tutorial_arrows","Arrows",[("dummy_mesh",0)],itp_type_arrows,itcf_carry_quiver_back,0,weight(3)|abundance(160)|weapon_length(95)|max_ammo(20),imodbits_missile],
["tutorial_bolts","Bolts",[("dummy_mesh",0)],itp_type_bolts,itcf_carry_quiver_right_vertical,0,weight(2.25)|weapon_length(55)|max_ammo(18),imodbits_missile],
["tutorial_short_bow","Short_Bow",[("dummy_mesh",0),],itp_type_bow|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back,0,weight(1)|spd_rtng(98)|shoot_speed(49)|thrust_damage(12,pierce),imodbits_bow],
["tutorial_crossbow","Crossbow",[("dummy_mesh",0)],itp_type_bow|itp_primary|itp_two_handed|itp_cant_reload_on_horseback,itcf_shoot_crossbow|itcf_carry_crossbow_back,0,weight(3)|spd_rtng(42)|shoot_speed(68)|thrust_damage(32,pierce)|max_ammo(1),imodbits_bow],
["tutorial_throwing_daggers","Throwing_Daggers",[("dummy_mesh",0)],itp_type_thrown|itp_primary,itcf_throw_knife,0,weight(3.5)|spd_rtng(102)|shoot_speed(25)|thrust_damage(16,cut)|max_ammo(14)|weapon_length(0),imodbits_missile],
["tutorial_saddle_horse","Saddle_Horse",[("dummy_mesh",0)],itp_type_horse,0,0,body_armor(3)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["tutorial_shield","Shield",[("dummy_mesh",0)],itp_type_shield|itp_wooden_parry,itcf_carry_kite_shield,118,weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield],
["tutorial_staff_no_attack","Staff",[("dummy_mesh",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9,weight(3.5)|spd_rtng(120)|weapon_length(115)|swing_damage(0,blunt)|thrust_damage(0,blunt),imodbits_none],
["tutorial_staff","Staff",[("dummy_mesh",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9,weight(3.5)|spd_rtng(120)|weapon_length(115)|swing_damage(16,blunt)|thrust_damage(16,blunt),imodbits_none],
["tutorial_sword","Sword",[("dummy_mesh",0)],itp_type_one_handed_wpn|itp_primary,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,0,weight(1.5)|spd_rtng(100)|weapon_length(102)|swing_damage(18,cut)|thrust_damage(15,pierce),imodbits_sword],
["tutorial_axe","Axe",[("dummy_mesh",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry,itc_nodachi|itcf_carry_axe_back,0,weight(4)|spd_rtng(91)|weapon_length(108)|swing_damage(19,cut),imodbits_mace],
["tutorial_dagger","Dagger",[("dummy_mesh",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary,itc_longsword,3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],
["horse_meat","Horse_Meat",[("raw_meat",0)],itp_type_goods|itp_consumable|itp_food,0,12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],
# Items before this point are hardwired and their order should not be changed!

##************************************************************************************************
## RANGED WEAPONS
##************************************************************************************************
#hit_points = frequency - lower = fast / ok this needs some balance testing for semi autos.
#body_armor = recoil per shot - higher = more recoil
#food_quality = sound
#accuracy = accuracy
#thrust_damage = damage
#spd_rtng = reload speed - higher = faster
#max_ammo = ammo gun can hold
#itp_has_bayonet = autofire
#itp_couchable = has scope

##pistol_1911 marks the start of ranged weapons in header_items and module_constants, MUST ALWAYS EXIST AND BE FIRST
##WARNING - to avoid compiling problems add new guns somewhere after the pistol_1911 item and before the buffer guns section. Don't add more than 9 new guns at most before compiling a couple of times. Compile regularly! - krag

# Pistols
["pistol_1911"," Pistol",[("pistol_1911", 0),], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  650, weapon_length(35)|weight(1.2)|accuracy(65)|spd_rtng(55)|shoot_speed(160)|max_ammo(7)|hit_points(500)|body_armor(4)|abundance(50)|food_quality(snd_colt1911)|thrust_damage(28, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

################
##Barbed Wire###
################
##Entenaii Empire
["empire_revolver","Entenaii Empire Revolver",[("webleymk6", 0),("pistol_holster1b",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  270, weapon_length(35)|weight(1.3)|accuracy(61)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(550)|body_armor(10)|abundance(25)|food_quality(snd_fire_huntingrevolver)|thrust_damage(28, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Entenaii Dominion
["dominion_revolver","Entenaii Dominion Revolver",[("webleybulldog", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  200, weapon_length(25)|weight(0.5)|accuracy(62)|spd_rtng(65)|shoot_speed(160)|max_ammo(5)|hit_points(550)|body_armor(10)|abundance(30)|food_quality(snd_fire_huntingrevolver)|thrust_damage(25, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["dominion_pistol","Entenaii_Dominion_Pistol",[("1935a", 0)],
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  650, weapon_length(25)|weight(1)|accuracy(88)|spd_rtng(70)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(4)|food_quality(snd_9mm_fire)|thrust_damage(24, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Kingdom of Galvae
["galvae_revolver","Galvae Revolver",[("rastgasser", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  300, weapon_length(35)|weight(1.3)|accuracy(63)|spd_rtng(35)|shoot_speed(165)|max_ammo(8)|hit_points(550)|body_armor(10)|abundance(25)|food_quality(snd_fire_huntingrevolver)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Molvat-Berchav Union
["molvat_revolver","Molvat Revolver",[("nagant", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  400, weapon_length(35)|weight(1.3)|accuracy(64)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(400)|body_armor(10)|abundance(25)|food_quality(snd_fire_huntingrevolver)|thrust_damage(26, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["molvat_pistol","Molvat_Pistol",[("pm", 0)],
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  650, weapon_length(25)|weight(1)|accuracy(88)|spd_rtng(70)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(4)|food_quality(snd_9mm_fire)|thrust_damage(24, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Vitzland Territories
["vitzland_pistol","Vitzland Pistol",[("mannlicherpistol1896", 0),], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  500, weapon_length(35)|weight(1.2)|accuracy(58)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(5)|food_quality(snd_mauser)|thrust_damage(27, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["vitzland_pistol_2","Vitzland Officer Pistol",[("c96", 0),], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  825, weapon_length(35)|weight(1.3)|accuracy(62)|spd_rtng(65)|shoot_speed(160)|max_ammo(10)|hit_points(500)|body_armor(4)|food_quality(snd_mauser)|thrust_damage(29, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["vitzland_pistol_2_w_butt","Vitzland Officer Pistol With Buttstock",[("c96_buttstock", 0),], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  950, weapon_length(35)|weight(1.7)|accuracy(68)|spd_rtng(62)|shoot_speed(160)|max_ammo(10)|hit_points(500)|body_armor(2)|food_quality(snd_mauser)|thrust_damage(30, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#
["vitzland_pistol_2_heirloom","Vitzland Heirloom_Pistol",[("c96_heirloom", 0),], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  1025, weapon_length(35)|weight(1.3)|accuracy(62)|spd_rtng(65)|shoot_speed(160)|max_ammo(10)|hit_points(500)|body_armor(4)|food_quality(snd_mauser)|thrust_damage(32, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#
["vitzland_kaiser_pistol","Kaiser Pistol",[("kaiserpistol", 0),], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  1700, weapon_length(35)|weight(1.3)|accuracy(72)|spd_rtng(75)|shoot_speed(160)|max_ammo(10)|hit_points(500)|body_armor(4)|food_quality(snd_mauser)|thrust_damage(34, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#

##Trezzo Republic
["trezzo_revolver","Trezzo Revolver",[("bodeo", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  750, weapon_length(35)|weight(1)|accuracy(70)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(480)|body_armor(9)|abundance(10)|food_quality(snd_fire_huntingrevolver)|thrust_damage(33, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["trezzo_pistol","Trezzo_Pistol",[("m1934", 0)],
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  650, weapon_length(25)|weight(1)|accuracy(88)|spd_rtng(70)|shoot_speed(160)|max_ammo(7)|hit_points(500)|body_armor(4)|food_quality(snd_9mm_fire)|thrust_damage(24, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["trezzo_revolver_custom","Trezzo Revolver",[("bodeo1", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  1300, weapon_length(35)|weight(1)|accuracy(75)|spd_rtng(67)|shoot_speed(160)|max_ammo(6)|hit_points(480)|body_armor(6)|abundance(10)|food_quality(snd_fire_huntingrevolver)|thrust_damage(38, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#

["trezzo_revolver_custom_2","Doge's_Revolver",[("bodeo2", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  3850, weapon_length(35)|weight(1)|accuracy(88)|spd_rtng(55)|shoot_speed(160)|max_ammo(6)|hit_points(200)|body_armor(4)|food_quality(snd_fire_huntingrevolver)|thrust_damage(48, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

#
##Itami Castedom
["itami_pistol","Itami Pistol",[("nambu94", 0),],
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  500, weapon_length(35)|weight(1.2)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(4)|food_quality(snd_mauser)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["itami_pistol_2","Itami Officer Pistol",[("nambu_type_141", 0),],
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  500, weapon_length(35)|weight(1.2)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(4)|food_quality(snd_mauser)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Bashide Confederacy
["bashide_pistol","Bashide Pistol",[("p38", 0),("p38holstered",ixmesh_carry)],
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  500, weapon_length(35)|weight(1.2)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(4)|food_quality(snd_mauser)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],


##irregular/other
["common_revolver_1","Revolver",[("colt1892", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  410, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(45)|food_quality(snd_fire_huntingrevolver)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_2","Revolver",[("enfieldmk1", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  405, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(30)|food_quality(snd_fire_huntingrevolver)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_3","Revolver",[("galand", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  420, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(45)|food_quality(snd_fire_huntingrevolver)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_4","Revolver",[("gasser", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  400, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(35)|food_quality(snd_fire_huntingrevolver)|thrust_damage(21, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_5","Revolver",[("mas1873", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  390, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(28)|food_quality(snd_fire_huntingrevolver)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_6","Revolver",[("mle_1892", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  402, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(30)|food_quality(snd_fire_huntingrevolver)|thrust_damage(21, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_7","Revolver",[("reichsrevolver1879", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  408, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(35)|food_quality(snd_fire_huntingrevolver)|thrust_damage(21, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_8","Revolver",[("smithwesson_no2", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  410, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(32)|food_quality(snd_fire_huntingrevolver)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_9","Revolver",[("sw_sh", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  422, weapon_length(35)|weight(1.3)|accuracy(65)|spd_rtng(68)|shoot_speed(162)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(25)|food_quality(snd_fire_huntingrevolver)|thrust_damage(25, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_10","Revolver",[("sw_sh_b", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  406, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(28)|food_quality(snd_fire_huntingrevolver)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#
["common_revolver_11","Revolver",[("bacon", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  410, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(45)|food_quality(snd_fire_huntingrevolver)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_12","Revolver",[("beaumont", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  405, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(30)|food_quality(snd_fire_huntingrevolver)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_13","Revolver",[("colt1849", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  420, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(45)|food_quality(snd_fire_huntingrevolver)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_14","Revolver",[("colt_dragoon", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  400, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(35)|food_quality(snd_fire_huntingrevolver)|thrust_damage(21, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_15","Revolver",[("colt_m1851_navy", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  390, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(28)|food_quality(snd_fire_huntingrevolver)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_16","Revolver",[("colt_m1860", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  402, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(30)|food_quality(snd_fire_huntingrevolver)|thrust_damage(21, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_17","Revolver",[("colt_m1873", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  408, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(35)|food_quality(snd_fire_huntingrevolver)|thrust_damage(21, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_18","Revolver",[("colt_walker", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  410, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(32)|food_quality(snd_fire_huntingrevolver)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_19","Revolver",[("lefaucheux", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  422, weapon_length(35)|weight(1.3)|accuracy(65)|spd_rtng(68)|shoot_speed(162)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(25)|food_quality(snd_fire_huntingrevolver)|thrust_damage(25, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_20","Revolver",[("lemat", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  406, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(28)|food_quality(snd_fire_huntingrevolver)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_21","Revolver",[("remington1", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  422, weapon_length(35)|weight(1.3)|accuracy(65)|spd_rtng(68)|shoot_speed(162)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(25)|food_quality(snd_fire_huntingrevolver)|thrust_damage(25, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_22","Revolver",[("savage_revolver", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  406, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(28)|food_quality(snd_fire_huntingrevolver)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_revolver_23","Revolver",[("webleypryse", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  406, weapon_length(35)|weight(1.3)|accuracy(60)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(28)|food_quality(snd_fire_huntingrevolver)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#

#special
["special_revolver_1","Heirloom_Revolver",[("reichsrevolver1879_heirloom", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  1000, weapon_length(35)|weight(1.5)|accuracy(70)|spd_rtng(70)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|food_quality(snd_fire_huntingrevolver)|thrust_damage(31, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["special_revolver_2","Heirloom_Revolver",[("colt1892_heirloom", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  1000, weapon_length(35)|weight(1.3)|accuracy(72)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(45)|food_quality(snd_fire_huntingrevolver)|thrust_damage(26, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["special_revolver_3","Heirloom_Revolver",[("colt1892_heirloom_2", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  1010, weapon_length(35)|weight(1.3)|accuracy(75)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(45)|food_quality(snd_fire_huntingrevolver)|thrust_damage(25, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["special_revolver_4","Heirloom_Revolver",[("mas1873_heirloom", 0),("pistol_holster1",ixmesh_carry)], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right|itcf_show_holster_when_drawn,
  1210, weapon_length(35)|weight(1.3)|accuracy(70)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(28)|food_quality(snd_fire_huntingrevolver)|thrust_damage(28, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

#
["crook_revolver_1","Crook_Revolver",[("apache", 0)], 
  itp_type_pistol|itp_primary|itp_merchandise|itp_next_item_as_melee, itcf_reload_pistol|itcf_carry_revolver_right,
  100, weapon_length(10)|weight(1)|accuracy(20)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(35)|food_quality(snd_fire_huntingrevolver)|thrust_damage(16, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["crook_revolver_1_alt","Crook_Revolver_alt",[("apache",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_unique, itc_dagger,
  150,weight(0.75)|spd_rtng(110)|weapon_length(35)|swing_damage(25,blunt)|thrust_damage(25,pierce),imodbits_sword_high],

#
["common_pistol_1","Pistol",[("ruby", 0)], itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  500, weapon_length(25)|weight(1)|accuracy(82)|spd_rtng(70)|shoot_speed(160)|max_ammo(9)|hit_points(500)|body_armor(4)|food_quality(snd_9mm_fire)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_pistol_2","Pistol",[("bergman", 0)], itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  520, weapon_length(25)|weight(1)|accuracy(85)|spd_rtng(70)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(4)|food_quality(snd_9mm_fire)|thrust_damage(24, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_pistol_3","Pistol",[("c93", 0)], itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  520, weapon_length(25)|weight(1)|accuracy(85)|spd_rtng(70)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(4)|food_quality(snd_9mm_fire)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_pistol_4","Pistol",[("fn1900", 0)], itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  520, weapon_length(25)|weight(1)|accuracy(85)|spd_rtng(70)|shoot_speed(160)|max_ammo(7)|hit_points(500)|body_armor(4)|food_quality(snd_9mm_fire)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_pistol_5","Pistol",[("luger", 0)], itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  600, weapon_length(25)|weight(1)|accuracy(86)|spd_rtng(70)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(4)|food_quality(snd_9mm_fire)|thrust_damage(25, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_pistol_6","Pistol",[("steyr", 0)], itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  610, weapon_length(25)|weight(1)|accuracy(86)|spd_rtng(70)|shoot_speed(160)|max_ammo(10)|hit_points(500)|body_armor(4)|food_quality(snd_9mm_fire)|thrust_damage(24, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_pistol_7","Pistol",[("tt33", 0)], itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  650, weapon_length(25)|weight(1)|accuracy(88)|spd_rtng(70)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(4)|food_quality(snd_9mm_fire)|thrust_damage(26, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_pistol_8","Pistol",[("frommerstop", 0)], itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  520, weapon_length(25)|weight(1)|accuracy(86)|spd_rtng(70)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(4)|food_quality(snd_9mm_fire)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_pistol_9","Pistol",[("lahti35", 0)], itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  520, weapon_length(25)|weight(1)|accuracy(86)|spd_rtng(70)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(4)|food_quality(snd_9mm_fire)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#

["special_pistol_1","Heirloom_Pistol",[("1911_heirloom", 0),], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  850, weapon_length(35)|weight(1.0)|accuracy(75)|spd_rtng(60)|shoot_speed(160)|max_ammo(7)|hit_points(450)|body_armor(4)|food_quality(snd_colt1911)|thrust_damage(32, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["special_pistol_2","Heirloom_Pistol",[("1911_heirloom_2", 0),], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  950, weapon_length(35)|weight(1.1)|accuracy(80)|spd_rtng(65)|shoot_speed(160)|max_ammo(7)|hit_points(400)|body_armor(4)|food_quality(snd_colt1911)|thrust_damage(35, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

#
["pistol_1911_2","Pistol",[("pistol_1911_2", 0),("pistol_1911_2_rusty",imodbit_cracked|imodbit_rusty),], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  600, weapon_length(35)|weight(1.2)|accuracy(85)|spd_rtng(55)|shoot_speed(160)|max_ammo(7)|hit_points(500)|body_armor(4)|food_quality(snd_colt1911)|thrust_damage(27, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_browning_hp_maesen","Pistol",[("1911", 0),], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  550, weapon_length(35)|weight(1.2)|accuracy(85)|spd_rtng(55)|shoot_speed(160)|max_ammo(13)|hit_points(500)|body_armor(4)|food_quality(snd_10mmpistolfire)|thrust_damage(26, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["pistol_walther_ppk","Pistol",[("pistol_walther_ppk", 0),("pistol_walther_ppk_worn",imodbit_cracked|imodbit_rusty),], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  520, weapon_length(12)|weight(1)|accuracy(85)|spd_rtng(70)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(4)|food_quality(snd_9mm_fire)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_walther_ppk_sil","Assassin Pistol",[("pistol_walther_ppk_sil", 0),], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  700, weapon_length(26)|weight(1)|accuracy(85)|spd_rtng(65)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(4)|food_quality(snd_silenced_fire)|thrust_damage(25, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["pistol_revolver_1","Revolver",[("pistol_revolver_1", 0),], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  300, weapon_length(35)|weight(1.3)|accuracy(70)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(25)|food_quality(snd_fire_huntingrevolver)|thrust_damage(26, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_revolver_2","Revolver",[("pistol_revolver_2", 0),], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  280, weapon_length(35)|weight(1.3)|accuracy(70)|spd_rtng(65)|shoot_speed(160)|max_ammo(6)|hit_points(500)|body_armor(10)|abundance(25)|food_quality(snd_fire_huntingrevolver)|thrust_damage(21, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_snubnosed_revolver","Short Revolver",[("pistol_snubnosed_revolver", 0),], 
  itp_type_pistol|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
  200, weapon_length(12)|weight(1)|accuracy(65)|spd_rtng(65)|shoot_speed(120)|max_ammo(6)|hit_points(500)|body_armor(6)|food_quality(snd_9mm_fire)|thrust_damage(29, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#
["pistol_colt_commander","XPistolX",[("pistol_colt_commander", 0),], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  250, weapon_length(35)|weight(1.1)|accuracy(85)|spd_rtng(60)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(4)|food_quality(snd_10mmpistolfire)|thrust_damage(36, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_dm_c96","XPistolX", [("pistol_dm_c96", 0),], itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  250, weapon_length(35)|weight(1.5)|accuracy(85)|spd_rtng(55)|shoot_speed(160)|max_ammo(10)|hit_points(500)|body_armor(4)|food_quality(snd_10mmpistolfire)|thrust_damage(36, pierce), imodbits_gun, []],
["pistol_enforcer","XPistolX",[("pistol_enforcer", 0),], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  350, weapon_length(35)|weight(1.5)|accuracy(85)|spd_rtng(55)|shoot_speed(160)|max_ammo(8)|hit_points(600)|body_armor(10)|food_quality(snd_deagle)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_n99","XPistolX",[("pistol_m3d_n99", 0),], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  350, weapon_length(35)|weight(3)|accuracy(90)|spd_rtng(50)|shoot_speed(160)|max_ammo(12)|hit_points(600)|body_armor(10)|food_quality(snd_10mmpistolfire)|thrust_damage(36, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_glock","XPistolX", [("pistol_glock", 0),], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  300, weapon_length(35)|weight(1.5)|accuracy(90)|spd_rtng(65)|shoot_speed(160)|max_ammo(17)|hit_points(500)|body_armor(4)|food_quality(snd_policepistolfire)|thrust_damage(31, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_maesen_d9","XPistolX",[("pistol_maesen_d9", 0),], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  300, weapon_length(35)|weight(1.5)|accuracy(85)|spd_rtng(60)|shoot_speed(160)|max_ammo(12)|hit_points(500)|body_armor(4)|food_quality(snd_10mmpistolfire)|thrust_damage(36, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_r22","XPistolX",[("pistol_r22", 0),], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  225, weapon_length(35)|weight(1.5)|accuracy(90)|spd_rtng(65)|shoot_speed(160)|max_ammo(10)|hit_points(500)|body_armor(2)|food_quality(snd_pistol22_fire)|thrust_damage(31, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_sig_p229","XPistolX",[("pistol_sig_p229", 0),], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  250, weapon_length(35)|weight(1.2)|accuracy(85)|spd_rtng(60)|shoot_speed(160)|max_ammo(15)|hit_points(500)|body_armor(4)|food_quality(snd_9mm_fire)|thrust_damage(36, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_sny45","XPistolX",[("pistol_sny45", 0),], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  275, weapon_length(35)|weight(1.5)|accuracy(85)|spd_rtng(60)|shoot_speed(160)|max_ammo(10)|hit_points(500)|body_armor(4)|food_quality(snd_10mmpistolfire)|thrust_damage(36, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_sw_629_2","XRevolverX",[("pistol_sw_629_2", 0),], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  300, weapon_length(35)|weight(1.5)|accuracy(80)|spd_rtng(65)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(8)|food_quality(snd_44revolv_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_sw_model_500","XRevolverX",[("pistol_sw_model_500", 0),], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  325, weapon_length(35)|weight(2.2)|accuracy(75)|spd_rtng(55)|shoot_speed(160)|max_ammo(5)|hit_points(500)|body_armor(12)|food_quality(snd_44revolv_fire)|thrust_damage(46, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_desert_eagle","XPistolX",[("pistol_desert_eagle", 0),], 
  itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  350, weapon_length(35)|weight(2.25)|accuracy(75)|spd_rtng(50)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(12)|food_quality(snd_deagle)|thrust_damage(46, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_cx33","XPistolX", [("pistol_cx33", 0),], itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  750, weapon_length(35)|weight(1.5)|accuracy(90)|spd_rtng(60)|shoot_speed(160)|max_ammo(20)|hit_points(500)|body_armor(2)|food_quality(snd_10mmpistolfire)|thrust_damage(36, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_dc17","XPistolX", [("pistol_dc17", 0),], itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
  150, weapon_length(35)|weight(1.5)|accuracy(85)|spd_rtng(55)|shoot_speed(160)|max_ammo(8)|hit_points(500)|body_armor(4)|food_quality(snd_44revolv_fire)|thrust_damage(31, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#

# SMGs
["smg_1","Submachine Gun", [("m3_shorten", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
  500, weapon_length(50)|weight(3)|accuracy(75)|spd_rtng(60)|shoot_speed(160)|max_ammo(20)|hit_points(75)|body_armor(8)|food_quality(snd_9mm_fire)|thrust_damage(21, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
################
##Barbed Wire###
################
##Entenaii Empire
["smg_sten","Entenaii Empire Submachine Gun",[("smg_sten", 0)], 
  itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
  450, weapon_length(64)|weight(3.2)|accuracy(58)|spd_rtng(60)|shoot_speed(160)|max_ammo(32)|hit_points(120)|body_armor(10)|food_quality(snd_mp40)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["smg_sten_silenced","Entenaii Empire Silenced Submachine Gun",[("smg_sten_silenced", 0)], 
  itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
  450, weapon_length(64)|weight(3.2)|accuracy(57)|spd_rtng(60)|shoot_speed(160)|max_ammo(32)|hit_points(120)|body_armor(10)|food_quality(snd_silenced_fire)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Entenaii Dominion
["dominion_smg","Entenaii Dominion Submachine Gun",[("mas38", 0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
500, weapon_length(50)|weight(3)|accuracy(58)|spd_rtng(60)|shoot_speed(160)|max_ammo(32)|hit_points(95)|body_armor(10)|food_quality(snd_mp40)|thrust_damage(25, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Kingdom of Galvae
["galvae_smg","Galvae_Submachine_Gun",[("erma", 0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
420, weapon_length(65)|weight(3.5)|accuracy(52)|spd_rtng(60)|shoot_speed(160)|max_ammo(32)|hit_points(150)|body_armor(10)|food_quality(snd_mp40)|thrust_damage(23, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Molvat-Berchav Union
["molvat_smg","Molvat Submachine Gun",[("ppsh41mag", 0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
600, weapon_length(60)|weight(3)|accuracy(52)|spd_rtng(50)|shoot_speed(160)|max_ammo(35)|hit_points(95)|body_armor(8)|food_quality(snd_mp40)|thrust_damage(26, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["molvat_smg_2","Molvat Submachine Gun With Drum Magazine",[("ppsh41drum", 0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
600, weapon_length(60)|weight(3)|accuracy(52)|spd_rtng(50)|shoot_speed(160)|max_ammo(71)|hit_points(95)|body_armor(8)|food_quality(snd_mp40)|thrust_damage(26, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["berchav_smg","Berchav Submachine Gun",[("ppd34", 0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
500, weapon_length(60)|weight(3.5)|accuracy(50)|spd_rtng(50)|shoot_speed(160)|max_ammo(25)|hit_points(110)|body_armor(8)|food_quality(snd_mp40)|thrust_damage(24, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Vitzland Territories
["vitzland_smg","Vitzland Submachine Gun",[("mp18", 0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
450, weapon_length(64)|weight(3.2)|accuracy(55)|spd_rtng(60)|shoot_speed(160)|max_ammo(32)|hit_points(120)|body_armor(10)|food_quality(snd_mp40)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["vitzland_smg_2","Vitzland Submachine Gun",[("volkssturmgewehr", 0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
450, weapon_length(64)|weight(3.5)|accuracy(50)|spd_rtng(60)|shoot_speed(160)|max_ammo(30)|hit_points(120)|body_armor(10)|food_quality(snd_mp40)|thrust_damage(20, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Trezzo Republic
["trezzo_smg","Trezzo Submachine Gun",[("beretta1918", 0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
750, weapon_length(50)|weight(3)|accuracy(56)|spd_rtng(60)|shoot_speed(160)|max_ammo(25)|hit_points(85)|body_armor(8)|food_quality(snd_mp5)|thrust_damage(27, pierce), imodbits_gun,[ranged_weapon_triggers,scope_add]],
["trezzo_smg_2","Trezzo Submachine Gun",[("m1938a", 0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
955, weapon_length(50)|weight(3)|accuracy(62)|spd_rtng(60)|shoot_speed(160)|max_ammo(30)|hit_points(85)|body_armor(8)|food_quality(snd_mp5)|thrust_damage(30, pierce), imodbits_gun,[ranged_weapon_triggers,scope_add]],

##Itami Castedom
["itami_smg","Itami_Submachine_Gun",[("type100", 0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
450, weapon_length(64)|weight(3)|accuracy(55)|spd_rtng(60)|shoot_speed(160)|max_ammo(30)|hit_points(120)|body_armor(10)|food_quality(snd_mp40)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["itami_smg_alt","Itami_Submachine_Gun", [("type100",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
450, weight(3)|spd_rtng(100)|weapon_length(64)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Bashide Confederacy
["bashide_smg","Bashide Submachine Gun",[("mp34", 0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
450, weapon_length(64)|weight(3.2)|accuracy(55)|spd_rtng(60)|shoot_speed(160)|max_ammo(32)|hit_points(120)|body_armor(10)|food_quality(snd_mp40)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["bashide_smg_2","Bashide Submachine Gun",[("mp41", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
500, weapon_length(50)|weight(3)|accuracy(58)|spd_rtng(60)|shoot_speed(160)|max_ammo(30)|hit_points(95)|body_armor(10)|food_quality(snd_mp40)|thrust_damage(29, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],


#irregular
["renegade_smg","Submachine Gun",[("peltiheikki_3", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
250, weapon_length(50)|weight(3)|accuracy(50)|spd_rtng(60)|shoot_speed(160)|max_ammo(20)|hit_points(95)|body_armor(10)|food_quality(snd_mp40)|thrust_damage(26, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["renegade_smg_2","Submachine Gun",[("suomikp_4", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
600, weapon_length(60)|weight(3)|accuracy(55)|spd_rtng(50)|shoot_speed(160)|max_ammo(71)|hit_points(95)|body_armor(8)|food_quality(snd_mp40)|thrust_damage(26, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#other
["smg_m31","Submachine Gun", [("smg_m31", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
600, weapon_length(60)|weight(3)|accuracy(54)|spd_rtng(50)|shoot_speed(160)|max_ammo(71)|hit_points(95)|body_armor(8)|food_quality(snd_mp40)|thrust_damage(26, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["smg_mp40","Submachine Gun",[("smg_mp40", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
500, weapon_length(50)|weight(3)|accuracy(58)|spd_rtng(60)|shoot_speed(160)|max_ammo(30)|hit_points(95)|body_armor(10)|food_quality(snd_mp40)|thrust_damage(29, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#
#
["smg_tommygun","Submachine Gun", [("thompsonsubmachinegun", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
500, weapon_length(56)|weight(3)|accuracy(55)|spd_rtng(60)|shoot_speed(160)|max_ammo(20)|hit_points(75)|body_armor(8)|food_quality(snd_thompson)|thrust_damage(31, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#
["smg_dm44","XSubmachine GunX", [("smg_dm44", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
550, weapon_length(50)|weight(3)|accuracy(80)|spd_rtng(55)|shoot_speed(160)|max_ammo(20)|hit_points(85)|body_armor(8)|food_quality(snd_9mm_fire)|thrust_damage(31, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["smg_mp5a3","XSubmachine GunX",
[("smg_mp5a3", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
750, weapon_length(50)|weight(3)|accuracy(75)|spd_rtng(60)|shoot_speed(160)|max_ammo(30)|hit_points(85)|body_armor(8)|food_quality(snd_mp5)|thrust_damage(37, pierce), imodbits_gun,[ranged_weapon_triggers,scope_add]],
["smg_uzi","XMachine PistolX",
[("smg_uzi", 0),], itp_type_pistol|itp_primary|itp_has_bayonet, itcf_reload_pistol|itcf_carry_revolver_right,
400, weapon_length(35)|weight(1.5)|accuracy(75)|spd_rtng(65)|shoot_speed(160)|max_ammo(20)|hit_points(65)|body_armor(10)|food_quality(snd_9mm_fire)|thrust_damage(31, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["smg_ap10","XMachine PistolX",
[("smg_ap-10", 0),], itp_type_pistol|itp_primary|itp_has_bayonet, itcf_reload_pistol|itcf_carry_revolver_right,
450, weapon_length(26)|weight(1.5)|accuracy(75)|spd_rtng(65)|shoot_speed(160)|max_ammo(20)|hit_points(100)|body_armor(10)|food_quality(snd_tec9)|thrust_damage(36, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["smg_tec9","XMachine PistolX",
[("smg_tec-9", 0),], itp_type_pistol|itp_primary|itp_has_bayonet, itcf_reload_pistol|itcf_carry_revolver_right,
500, weapon_length(35)|weight(1.5)|accuracy(75)|spd_rtng(65)|shoot_speed(160)|max_ammo(20)|hit_points(80)|body_armor(10)|food_quality(snd_tec9)|thrust_damage(31, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["smg_ump_45","XSubmachine GunX",
[("smg_ump_45", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
750, weapon_length(48)|weight(2.6)|accuracy(75)|spd_rtng(65)|shoot_speed(160)|max_ammo(25)|hit_points(85)|body_armor(8)|food_quality(snd_ump45)|thrust_damage(36, pierce), imodbits_gun,[ranged_weapon_triggers,scope_add]],
["smg_rusty_pistol","Makeshift Submachine Gun",
[("vietsmg", 0),],  itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
400, weapon_length(38)|weight(1.5)|accuracy(65)|spd_rtng(65)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(10)|food_quality(snd_mp40)|thrust_damage(31, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#

# Rifles
["rifle_arisaka","Bolt-Action_Rifle",
[("rifle_arisaka",0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
600, weapon_length(115)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#
################
##Barbed Wire###
################
##Entenaii Empire
["empire_bolt_action_rifle","Entenaii Empire Bolt-Action Rifle",[("smle",0)],
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
700, weapon_length(103)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(10)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["empire_bolt_action_rifle_bayonet","Entenaii Empire Bolt-Action Rifle with Bayonet",[("smle_w_bayonet",0)],
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
750, weapon_length(103)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(10)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["empire_bolt_action_rifle_bayonet_alt","Entenaii Empire Bolt-Action Rifle with Bayonet",[("smle_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
750, weight(5)|spd_rtng(90)|weapon_length(148)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["empire_bolt_action_carbine","Entenaii Empire Bolt-Action Carbine",[("smle_carbine",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
650, weapon_length(90)|weight(5)|accuracy(70)|spd_rtng(40)|shoot_speed(160)|max_ammo(10)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(39, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["empire_bolt_action_carbine_silent","Entenaii Empire Specialist Bolt-Action Carbine",[("delistecarbine",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
1000, weapon_length(91)|weight(5)|accuracy(85)|spd_rtng(50)|shoot_speed(160)|max_ammo(7)|hit_points(2800)|body_armor(30)|food_quality(snd_silenced_fire)|thrust_damage(65, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Entenaii Dominion
["dominion_bolt_action_rifle","Entenaii Dominion Bolt-Action Rifle",
[("metford",0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
500, weapon_length(116)|weight(5)|accuracy(73)|spd_rtng(45)|shoot_speed(160)|max_ammo(8)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(38, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["dominion_bolt_action_rifle_bayonet","Entenaii Dominion Bolt-Action Rifle with Bayonet",
[("metford_w_bayonet",0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
550, weapon_length(116)|weight(5)|accuracy(73)|spd_rtng(45)|shoot_speed(160)|max_ammo(8)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(38, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["dominion_bolt_action_rifle_bayonet_alt","Entenaii Dominion Bolt-Action Rifle with Bayonet", [("metford_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
550, weight(5)|spd_rtng(90)|weapon_length(161)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["dominion_bolt_action_carbine","Entenaii Dominion Bolt-Action Carbine",[("metford_carbine",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
450, weapon_length(115)|weight(5)|accuracy(67)|spd_rtng(45)|shoot_speed(160)|max_ammo(8)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(36, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["dominion_bolt_action_rifle_2","Entenaii Dominion Modern Bolt-Action Rifle",
[("mas36",0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
760, weapon_length(102)|weight (5)|accuracy(78)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],


##Kingdom of Galvae
["galvae_bolt_action_rifle","Galvae Bolt-Action Rifle",
[("krag",0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
780, weapon_length(112)|weight(8)|accuracy(76)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(39, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["galvae_bolt_action_rifle_bayonet","Galvae Bolt-Action Rifle with Bayonet",
[("krag_w_bayonet",0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
830, weapon_length(112)|weight(8)|accuracy(76)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(39, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["galvae_bolt_action_rifle_bayonet_alt","Galvae Bolt-Action Rifle with Bayonet", [("krag_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
830, weight(8)|spd_rtng(90)|weapon_length(157)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["galvae_bolt_action_carbine","Galvae Bolt-Action Carbine",[("krag_carbine",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
730, weapon_length(100)|weight(8)|accuracy(71)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(37, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Molvat-Berchav Union
["molvat_bolt_action_rifle","Molvat_Bolt-Action_Rifle",
[("mosin",0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
400, weapon_length(113)|weight(5)|accuracy(74)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(37, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["molvat_bolt_action_rifle_bayonet","Molvat_Bolt-Action_Rifle with Bayonet",
[("mosin_w_bayonet",0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
450, weapon_length(113)|weight(5)|accuracy(74)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(37, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["molvat_bolt_action_rifle_bayonet_alt","Molvat_Bolt-Action_Rifle with Bayonet", [("mosin_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
450, weight(3)|spd_rtng(90)|weapon_length(158)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["molvat_bolt_action_carbine","Molvat Bolt-Action Carbine",[("mosin_carbine",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
350, weapon_length(91)|weight(5)|accuracy(69)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(35, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["molvat_bolt_action_sawnoff","Molvat Bolt-Action Sawnoff",[("mosin_sawn-off",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
305, weapon_length(40)|weight(2)|accuracy(42)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(35, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],


#
["berchav_bolt_action_rifle","Berchav_Bolt-Action_Rifle",
[("ukkopekka3",0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
300, weapon_length(113)|weight(5)|accuracy(73)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(36, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["berchav_bolt_action_rifle_bayonet","Berchav_Bolt-Action_Rifle with Bayonet",
[("ukkopekka_b",0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
350, weapon_length(113)|weight(5)|accuracy(73)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(36, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["berchav_bolt_action_rifle_bayonet_alt","Berchav_Bolt-Action_Rifle with Bayonet", [("ukkopekka_b",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
350, weight(3)|spd_rtng(90)|weapon_length(158)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#
["molvat_semi_rifle","Molvat Semi-Automatic Rifle", [("svt38",0)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
700, weapon_length(115)|weight(7)|accuracy(67)|spd_rtng(50)|shoot_speed(160)|max_ammo(10)|hit_points(500)|body_armor(20)|food_quality(snd_trailcarbine_fire)|thrust_damage(36, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["molvat_semi_rifle_2","Molvat Marksman Rifle", [("svt40",0),("rifle_svt40",imodbit_cracked|imodbit_rusty)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
850, weapon_length(115)|weight(5)|accuracy(72)|spd_rtng(50)|shoot_speed(160)|max_ammo(10)|hit_points(500)|body_armor(20)|food_quality(snd_trailcarbine_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

#
##Vitzland Territories
["vitzland_bolt_action_rifle","Vitzland Bolt-Action_Rifle",[("gewehr88",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
500, weapon_length(117)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_gewehr_sniper)|thrust_damage(38, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["vitzland_bolt_action_rifle_bayonet","Vitzland Bolt-Action_Rifle with Bayonet",[("gewehr88_w_bayonet",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
550, weapon_length(117)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_gewehr_sniper)|thrust_damage(38, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["vitzland_bolt_action_rifle_bayonet_alt","Vitzland Bolt-Action_Rifle with Bayonet", [("gewehr88_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
550, weight(3)|spd_rtng(90)|weapon_length(162)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["vitzland_bolt_action_carbine","Vitzland Bolt-Action Carbine",[("gewehr88_carbine",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
450, weapon_length(90)|weight(3.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_gewehr_sniper)|thrust_damage(36, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#
["vitzland_bolt_action_rifle_2","Vitzland Modern Bolt-Action_Rifle",[("g98",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
600, weapon_length(117)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_gewehr_sniper)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["vitzland_bolt_action_rifle_bayonet_2","Vitzland Modern Bolt-Action_Rifle with Bayonet",[("g98_w_bayonet",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
650, weapon_length(117)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_gewehr_sniper)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["vitzland_bolt_action_rifle_bayonet_2_alt","Vitzland Modern Bolt-Action_Rifle with Bayonet", [("g98_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
650, weight(3)|spd_rtng(90)|weapon_length(162)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["vitzland_semi_rifle","Vitzland Semi-Automatic Rifle", [("g43",0)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
850, weapon_length(115)|weight(6.75)|accuracy(69)|spd_rtng(50)|shoot_speed(160)|max_ammo(10)|hit_points(500)|body_armor(20)|food_quality(snd_trailcarbine_fire)|thrust_damage(35, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Trezzo Republic
["trezzo_bolt_action_rifle","Trezzo Bolt-Action_Rifle",[("vetterli1887",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
1050, weapon_length(115)|weight(5)|accuracy(90)|spd_rtng(55)|shoot_speed(160)|max_ammo(4)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["trezzo_bolt_action_rifle_bayonet","Trezzo Bolt-Action_Rifle with Bayonet",[("vetterli1887_w_bayonet",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
1050, weapon_length(115)|weight(5)|accuracy(90)|spd_rtng(55)|shoot_speed(160)|max_ammo(4)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["trezzo_bolt_action_rifle_bayonet_alt","Trezzo Bolt-Action_Rifle with Bayonet", [("vetterli1887_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
1050, weight(3)|spd_rtng(90)|weapon_length(160)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["trezzo_bolt_action_carbine","Trezzo Bolt-Action Carbine",[("vetterli1887_carbine",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
950, weapon_length(94)|weight(3.5)|accuracy(85)|spd_rtng(55)|shoot_speed(160)|max_ammo(4)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["trezzo_bolt_action_rifle_2","Trezzo Modern Bolt-Action_Rifle",[("carcano1891",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
1150, weapon_length(115)|weight(5)|accuracy(90)|spd_rtng(55)|shoot_speed(160)|max_ammo(6)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(43, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["trezzo_bolt_action_rifle_bayonet_2","Trezzo Modern Bolt-Action_Rifle with Bayonet",[("carcano1891_w_bayonet",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
1150, weapon_length(115)|weight(5)|accuracy(90)|spd_rtng(55)|shoot_speed(160)|max_ammo(6)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(43, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["trezzo_bolt_action_rifle_bayonet_2_alt","Trezzo Modern Bolt-Action_Rifle with Bayonet", [("carcano1891_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
1150, weight(3)|spd_rtng(90)|weapon_length(160)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["trezzo_bolt_action_carbine_2","Trezzo Modern Bolt-Action Carbine",[("carcano1891_carbine",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
1050, weapon_length(94)|weight(3.5)|accuracy(85)|spd_rtng(55)|shoot_speed(160)|max_ammo(6)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(42, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

#
["trezzo_bolt_action_rifle_heritage_1","Heritage Trezzo Bolt-Action_Rifle",[("vetterli1887r",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
2050, weapon_length(115)|weight(5)|accuracy(95)|spd_rtng(65)|shoot_speed(160)|max_ammo(4)|hit_points(10000)|body_armor(25)|food_quality(snd_trailcarbine_fire)|thrust_damage(48, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["trezzo_bolt_action_rifle_heritage_1_bayonet","Heritage Trezzo Bolt-Action_Rifle with Bayonet",[("vetterli1887r_w_bayonet",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
2050, weapon_length(115)|weight(5)|accuracy(94)|spd_rtng(65)|shoot_speed(160)|max_ammo(4)|hit_points(10000)|body_armor(25)|food_quality(snd_trailcarbine_fire)|thrust_damage(48, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["trezzo_bolt_action_rifle_heritage_1_bayonet_alt","Heritage Trezzo Bolt-Action_Rifle with Bayonet", [("vetterli1887r_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
2050, weight(3)|spd_rtng(90)|weapon_length(160)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["trezzo_bolt_action_rifle_heritage_2","Heritage Trezzo Bolt-Action_Rifle",[("vetterli1887er",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
3050, weapon_length(115)|weight(5)|accuracy(98)|spd_rtng(65)|shoot_speed(160)|max_ammo(4)|hit_points(10000)|body_armor(20)|food_quality(snd_trailcarbine_fire)|thrust_damage(52, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["trezzo_bolt_action_rifle_heritage_2_bayonet","Heritage Trezzo Bolt-Action_Rifle with Bayonet",[("vetterli1887er_w_bayonet",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
3050, weapon_length(115)|weight(5)|accuracy(97)|spd_rtng(65)|shoot_speed(160)|max_ammo(4)|hit_points(10000)|body_armor(20)|food_quality(snd_trailcarbine_fire)|thrust_damage(52, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["trezzo_bolt_action_rifle_heritage_2_bayonet_alt","Heritage Trezzo Bolt-Action_Rifle with Bayonet", [("vetterli1887er_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
3050, weight(3)|spd_rtng(90)|weapon_length(160)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#

##Itami Castedom
["itami_bolt_action_rifle","Itami_Bolt-Action_Rifle",
[("fn24",0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
600, weapon_length(115)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["itami_bolt_action_rifle_bayonet","Itami Bolt-Action_Rifle with Bayonet",
[("fn24_w_b",0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
300, weapon_length(115)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["itami_bolt_action_rifle_bayonet_alt","Itami Bolt-Action_Rifle with Bayonet", [("fn24_w_b",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
350, weight(3)|spd_rtng(90)|weapon_length(160)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["itami_bolt_action_rifle_2","Itami_Officer_Bolt-Action_Rifle",
[("liao",0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
600, weapon_length(115)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]], 

##Bashide Confederacy
["bashide_bolt_action_rifle","Bashide Modern Bolt-Action_Rifle",[("mauser1893",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
600, weapon_length(117)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_gewehr_sniper)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["bashide_bolt_action_rifle_bayonet","Bashide Modern Bolt-Action_Rifle with Bayonet",[("mauser1893_w_bayonet",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
650, weapon_length(117)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_gewehr_sniper)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["bashide_bolt_action_rifle_bayonet_alt","Bashide Modern Bolt-Action_Rifle with Bayonet", [("mauser1893_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
650, weight(3)|spd_rtng(90)|weapon_length(162)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#
["bashide_bolt_action_rifle_2","Bashide Bolt-Action_Rifle",[("schoenauer",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
500, weapon_length(117)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_gewehr_sniper)|thrust_damage(38, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["bashide_bolt_action_rifle_bayonet_2","Bashide Bolt-Action_Rifle with Bayonet",[("schoenauer_w_bayonet",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
550, weapon_length(117)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_gewehr_sniper)|thrust_damage(38, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["bashide_bolt_action_rifle_bayonet_2_alt","Bashide Bolt-Action_Rifle with Bayonet", [("schoenauer_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
550, weight(3)|spd_rtng(90)|weapon_length(162)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["bashide_bolt_action_carbine_2","Bashide Bolt-Action Carbine",[("schoenauer_carbine",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
450, weapon_length(90)|weight(3.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_gewehr_sniper)|thrust_damage(36, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Renegade
["renegade_bolt_action_rifle","Bolt-Action_Rifle",[("beaumont1871_88",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
300, weapon_length(122)|weight(4.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(4)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(36, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["renegade_bolt_action_rifle_bayonet","Bolt-Action_Rifle with Bayonet",[("beaumont1871_88_w_bayonet",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
350, weapon_length(122)|weight(4.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(4)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(36, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["renegade_bolt_action_rifle_bayonet_alt","Bolt-Action_Rifle with Bayonet", [("beaumont1871_88_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
350, weight(3)|spd_rtng(90)|weapon_length(187)|thrust_damage(20, pierce)|swing_damage(22, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["renegade_bolt_action_carbine","Bolt-Action Carbine",[("beaumont1871_88_carbine",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
250, weapon_length(93)|weight(3.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(4)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(35, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Other
["common_bolt_action_rifle","Bolt-Action_Rifle",[("pystykorva_3",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
300, weapon_length(113)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(35, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_rifle_bayonet","Bolt-Action_Rifle with Bayonet",[("pystykorva_b",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
350, weapon_length(113)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(35, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_rifle_bayonet_alt","Bolt-Action_Rifle with Bayonet", [("pystykorva_b",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
350, weight(3)|spd_rtng(90)|weapon_length(158)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["common_bolt_action_rifle_1","Bolt-Action_Rifle",[("lebel1886",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
300, weapon_length(122)|weight(4.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(8)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(33, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_rifle_bayonet_1","Bolt-Action_Rifle with Bayonet",[("lebel1886_w_bayonet",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
350, weapon_length(122)|weight(4.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(8)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(33, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_rifle_bayonet_1_alt","Bolt-Action_Rifle with Bayonet", [("lebel1886_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
350, weight(3)|spd_rtng(90)|weapon_length(187)|thrust_damage(20, pierce)|swing_damage(22, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_carbine_1","Bolt-Action Carbine",[("lebel1886_carbine",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
250, weapon_length(93)|weight(3.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(8)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(31, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["common_bolt_action_rifle_2","Bolt-Action_Rifle",[("kropatschek",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
300, weapon_length(122)|weight(4.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(8)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(34, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_rifle_bayonet_2","Bolt-Action_Rifle with Bayonet",[("kropatschek_w_bayonet",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
350, weapon_length(122)|weight(4.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(8)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(34, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_rifle_bayonet_2_alt","Bolt-Action_Rifle with Bayonet", [("kropatschek_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
350, weight(3)|spd_rtng(90)|weapon_length(187)|thrust_damage(20, pierce)|swing_damage(22, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_carbine_2","Bolt-Action Carbine",[("kropatschek_carbine",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
250, weapon_length(93)|weight(3.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(8)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(32, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["common_bolt_action_rifle_3","Bolt-Action_Rifle",[("mannlicher",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
300, weapon_length(122)|weight(4.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(34, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_rifle_bayonet_3","Bolt-Action_Rifle with Bayonet",[("mannlicher_w_bayonet",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
350, weapon_length(122)|weight(4.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(34, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_rifle_bayonet_3_alt","Bolt-Action_Rifle with Bayonet", [("mannlicher_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
350, weight(3)|spd_rtng(90)|weapon_length(187)|thrust_damage(20, pierce)|swing_damage(22, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_carbine_3","Bolt-Action Carbine",[("mannlicher_carbine",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
250, weapon_length(93)|weight(3.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(32, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["common_bolt_action_rifle_4","Bolt-Action_Rifle",[("k98k",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
300, weapon_length(122)|weight(4.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(34, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_rifle_bayonet_4","Bolt-Action_Rifle with Bayonet",[("k98kbayonet",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
350, weapon_length(122)|weight(4.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(34, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_rifle_bayonet_4_alt","Bolt-Action_Rifle with Bayonet", [("k98kbayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
350, weight(3)|spd_rtng(90)|weapon_length(187)|thrust_damage(20, pierce)|swing_damage(22, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["common_bolt_action_rifle_5","Bolt-Action_Rifle",[("m41b",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
300, weapon_length(122)|weight(4.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(34, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],


#
#singleshot
["common_bolt_action_rifle_single","Single-Shot_Bolt-Action_Rifle", [("gras", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
200, weapon_length(131)|weight(5)|accuracy(65)|spd_rtng(25)|shoot_speed(160)|max_ammo(1)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(37, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_rifle_single_bayonet","Single-Shot_Bolt-Action_Rifle_with_Bayonet", [("gras_w_bayonet", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
250, weapon_length(131)|weight(5)|accuracy(65)|spd_rtng(25)|shoot_speed(160)|max_ammo(1)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(37, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_rifle_single_bayonet_alt","Single-Shot_Bolt-Action_Rifle_with_Bayonet", [("gras_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
150, weight(3)|spd_rtng(90)|weapon_length(187)|thrust_damage(20, pierce)|swing_damage(22, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["common_bolt_action_carbine_single","Single-Shot_Bolt-Action_Carbine", [("gras_carbine", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
200, weapon_length(99)|weight(5)|accuracy(65)|spd_rtng(25)|shoot_speed(160)|max_ammo(1)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(35, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["rifle_arisaka_b","Bolt-Action_Rifle with Bayonet",
[("rifle_arisaka_b",0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
300, weapon_length(115)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(10000)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["rifle_arisaka_b_alt","Bolt-Action_Rifle with Bayonet", [("rifle_arisaka_b",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
350, weight(3)|spd_rtng(90)|weapon_length(160)|thrust_damage(30, pierce)|swing_damage(32, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#

["rifle_m1_carbine","Semi-Automatic Carbine",
[("rifle_m1_carbine", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
950, weapon_length(74)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(15)|hit_points(500)|body_armor(25)|food_quality(snd_m1carbine)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

#
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#
["rifle_remington_model_700","Bolt-Action_Rifle", [("rifle_remington_model_700", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
630, weapon_length(115)|weight(5)|accuracy(80)|spd_rtng(30)|shoot_speed(160)|max_ammo(5)|hit_points(1800)|body_armor(35)|food_quality(snd_r700)|thrust_damage(65, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["rifle_remington_model_700_2","Bolt-Action_Rifle", [("remington_model_700", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
630, weapon_length(115)|weight(5)|accuracy(80)|spd_rtng(30)|shoot_speed(160)|max_ammo(5)|hit_points(1800)|body_armor(35)|food_quality(snd_r700)|thrust_damage(65, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["rifle_remington_model_700_3","Bolt-Action_Rifle", [("remington_horse", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
630, weapon_length(115)|weight(5)|accuracy(80)|spd_rtng(30)|shoot_speed(160)|max_ammo(5)|hit_points(1800)|body_armor(35)|food_quality(snd_r700)|thrust_damage(65, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["rifle_remington_model_700_4","Bolt-Action_Rifle", [("remington_rich", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
630, weapon_length(115)|weight(5)|accuracy(80)|spd_rtng(30)|shoot_speed(160)|max_ammo(5)|hit_points(1800)|body_armor(35)|food_quality(snd_r700)|thrust_damage(65, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["rifle_remington_model_700_5","Bolt-Action_Rifle", [("remington_special", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
630, weapon_length(115)|weight(5)|accuracy(80)|spd_rtng(30)|shoot_speed(160)|max_ammo(5)|hit_points(1800)|body_armor(35)|food_quality(snd_r700)|thrust_damage(65, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#
["horselord_carbine","Horselord_Bolt-Action_Carbine", [("short_remington_horse", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
690, weapon_length(79)|weight(4)|accuracy(78)|spd_rtng(35)|shoot_speed(160)|max_ammo(5)|hit_points(1200)|body_armor(35)|food_quality(snd_r700)|thrust_damage(62, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

#

["rifle_lever_action","Lever-Action Rifle", [("rifle_lever_action", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
400, weapon_length(81)|weight(5)|accuracy(70)|spd_rtng(45)|shoot_speed(160)|max_ammo(6)|hit_points(1800)|body_armor(30)|food_quality(snd_huntingrifle_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["rifle_m1_garand","Semi-Automatic Rifle With Bayonet", #(ammo: .30-06 Springfield) powerful rifle, used by US military for the duration of WW2, as the main infantry rifle. Semi-automatic, using an 8 bullet enbloc clip that automatically ejects from the inbuilt magazine, after the gun is fired empty, making an loud PING sound
[("rifle_m1_garand", 0)], itp_type_musket|itp_two_handed|itp_next_item_as_melee|itp_primary|itp_merchandise, itcf_reload_musket,
1100, weapon_length(81)|weight(5)|accuracy(85)|spd_rtng(50)|shoot_speed(160)|max_ammo(8)|hit_points(350)|body_armor(25)|food_quality(snd_garand_shot)|thrust_damage(50, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["rifle_m1_garand_bayonet","Semi-Automatic Rifle with Bayonet", [("rifle_m1_garand",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
1100, weight(3)|spd_rtng(90)|weapon_length(160)|thrust_damage(35, pierce)|swing_damage(34, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["rifle_m1_garand_alt","Semi-Automatic Rifle With Bayonet", #(ammo: .30-06 Springfield) A fictional alternative garand version, with shortened barrel and massively extended magazine, slightly less accurate
[("rifle_m1_garand_alt", 0)], itp_type_musket|itp_two_handed|itp_next_item_as_melee|itp_primary|itp_merchandise, itcf_reload_musket,
1420, weapon_length(81)|weight(5)|accuracy(78)|spd_rtng(50)|shoot_speed(160)|max_ammo(30)|hit_points(350)|body_armor(25)|food_quality(snd_garand_shot)|thrust_damage(50, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["rifle_m1_garand_alt_bayonet","Semi-Automatic Rifle with Bayonet", [("rifle_m1_garand_alt",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_musket_melee,
1420, weight(3)|spd_rtng(90)|weapon_length(140)|thrust_damage(35, pierce)|swing_damage(34, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],


["rifle_winchester","XWinchester_1866X", [("rifle_winchester", 0)], itp_type_musket|itp_two_handed|itp_primary, itcf_reload_musket,
350, weapon_length(115)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(13)|hit_points(1800)|body_armor(25)|food_quality(snd_huntingrifle_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["rifle_m14","XSemi-Automatic RifleX", #(ammo: 7.62*51) I owuld make this one semi auto only, or make a rare full auto variant, anyway full auto on 7,62*51 guns should be barelly usable past a very short range
[("rifle_m14", 0)], itp_type_musket|itp_two_handed|itp_primary, itcf_reload_musket,
350, weapon_length(81)|weight(5)|accuracy(70)|spd_rtng(50)|shoot_speed(160)|max_ammo(20)|hit_points(350)|body_armor(25)|food_quality(snd_huntingrifle_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["rifle_m14_scoped","XSemi-Automatic Rifle (Scoped)X", #(ammo: 7.62*51) I owuld make this one semi auto only, or make a rare full auto variant, anyway full auto on 7,62*51 guns should be barelly usable past a very short range
[("rifle_m14_scoped", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_couchable, itcf_reload_musket,
2600, weapon_length(81)|weight(5)|accuracy(75)|spd_rtng(50)|shoot_speed(160)|max_ammo(20)|hit_points(350)|body_armor(25)|food_quality(snd_huntingrifle_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["rifle_pa_bolt_action","Bolt-Action Rifle", [("rifle_pa_bolt-action", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
300, weapon_length(85)|weight(5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(5)|hit_points(1800)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["rifle_pa_musket","Old Rifle", [("rifle_pa_musket", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
200, weapon_length(85)|weight(5)|accuracy(65)|spd_rtng(25)|shoot_speed(160)|max_ammo(1)|hit_points(1800)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],


################### ;) ##########################
["rifle_moon","Moon's Rifle", [("svd",0)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
10000, weapon_length(115)|weight(3)|accuracy(87)|spd_rtng(70)|shoot_speed(160)|max_ammo(10)|hit_points(400)|body_armor(15)|food_quality(snd_trailcarbine_fire)|thrust_damage(50, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
################### ;) ##########################

["rifle_ruger_mini14","XSemi-Automatic CarbineX", # ammo : 5,56*45  this is pretty much like a m4 carbine, you can make it semi auto only for balance if you want a cheaper alternative to assault rifles
[("rifle_ruger_mini14", 0)], itp_type_musket|itp_two_handed|itp_primary, itcf_reload_musket,
350, weapon_length(81)|weight(5)|accuracy(75)|spd_rtng(55)|shoot_speed(160)|max_ammo(10)|hit_points(275)|body_armor(25)|food_quality(snd_huntingrifle_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],


# Assault Rifles
["assault_ak47","Assault Rifle", [("assault_ak47", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
500, weapon_length(75)|weight(5)|accuracy(60)|spd_rtng(55)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(15)|food_quality(snd_ak47)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
################
##Barbed Wire###
################
##Entenaii Empire

["entenaii_assault_rifle","Entenaii_Empire_Assault_Rifle", [("bar_carry", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
500, weapon_length(88)|weight(5)|accuracy(65)|spd_rtng(45)|shoot_speed(160)|max_ammo(20)|hit_points(100)|body_armor(20)|food_quality(snd_mg42)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Entenaii Dominion
["dominion_assault_rifle","Entenaii Dominion Assault Rifle", [("chauchat", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
800, weapon_length(104)|weight(10)|accuracy(65)|spd_rtng(45)|shoot_speed(160)|max_ammo(20)|hit_points(100)|body_armor(30)|food_quality(snd_assaultcarb_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["dominion_assault_rifle_special","Gilded Entenaii Dominion Assault Rifle", [("chauchat_heirloom", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1500, weapon_length(104)|weight(10)|accuracy(75)|spd_rtng(55)|shoot_speed(160)|max_ammo(20)|hit_points(80)|body_armor(25)|food_quality(snd_assaultcarb_fire)|thrust_damage(45, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],


##Kingdom of Galvae
["galvae_assault_rifle","Galvae Assault Rifle", [("lahti_saloranta", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
750, weapon_length(94)|weight(9)|accuracy(65)|spd_rtng(45)|shoot_speed(160)|max_ammo(20)|hit_points(100)|body_armor(30)|food_quality(snd_assaultcarb_fire)|thrust_damage(42, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
##Molvat-Berchav Union
["molvat_assault_rifle","Molvat Assault Rifle", [("fedorov", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
800, weapon_length(94)|weight(6)|accuracy(65)|spd_rtng(45)|shoot_speed(160)|max_ammo(20)|hit_points(100)|body_armor(30)|food_quality(snd_assaultcarb_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["berchav_assault_rifle","Berchav Assault Rifle", [("avs36", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
680, weapon_length(94)|weight(6)|accuracy(60)|spd_rtng(40)|shoot_speed(160)|max_ammo(15)|hit_points(100)|body_armor(30)|food_quality(snd_assaultcarb_fire)|thrust_damage(38, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
##Vitzland Territories
["vitzland_assault_rifle","Vitzland Assault Rifle", [("fg42", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
800, weapon_length(94)|weight(6)|accuracy(65)|spd_rtng(45)|shoot_speed(160)|max_ammo(20)|hit_points(100)|body_armor(30)|food_quality(snd_assaultcarb_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Trezzo Republic
["trezzo_assault_rifle","Trezzo Assault Rifle", [("cei_rigotti", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
985, weapon_length(99)|weight(5)|accuracy(66)|spd_rtng(42)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(30)|food_quality(snd_assaultcarb_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["trezzo_assault_rifle_bayonet","Trezzo Assault Rifle With Bayonet", [("cei_rigotti_w_bayonet", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_next_item_as_melee|itp_merchandise, itcf_reload_musket,
985, weapon_length(99)|weight(5)|accuracy(66)|spd_rtng(42)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(30)|food_quality(snd_assaultcarb_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["trezzo_assault_rifle_bayonet_alt","Trezzo Assault Rifle With Bayonet", [("cei_rigotti_w_bayonet",0)],
itp_type_polearm|itp_unique|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,
150, weight(3)|spd_rtng(90)|weapon_length(187)|thrust_damage(20, pierce)|swing_damage(22, cut), imodbits_gun, [ranged_weapon_triggers,scope_add]],


##Itami Castedom
["itami_assault_rifle","Itami Assault Rifle", [("zb26", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
800, weapon_length(94)|weight(6)|accuracy(65)|spd_rtng(45)|shoot_speed(160)|max_ammo(20)|hit_points(100)|body_armor(30)|food_quality(snd_assaultcarb_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Bashide Confederacy

#
["assault_ak47_black","XAssault Rifle", [("assault_ak47_black", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
600, weapon_length(75)|weight(5)|accuracy(60)|spd_rtng(55)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(15)|food_quality(snd_ak47)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["assault_ak47_silver","XAssault Rifle", [("assault_ak47_silver", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
750, weapon_length(75)|weight(5)|accuracy(60)|spd_rtng(55)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(15)|abundance(5)|food_quality(snd_ak47)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["assault_ak47_gold","XAssault Rifle", [("assault_ak47_gold", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1000, weapon_length(75)|weight(5)|accuracy(60)|spd_rtng(55)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(15)|abundance(1)|food_quality(snd_ak47)|thrust_damage(45, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["assault_ak47_scoped","XAssault Rifle (Scoped)", [("assault_ak47_scoped", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_couchable, itcf_reload_musket,
2850, weapon_length(75)|weight(5)|accuracy(75)|spd_rtng(55)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(15)|food_quality(snd_ak47)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["assault_ak47imp","XAssault Rifle", [("assault_ak47imp", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1000, weapon_length(75)|weight(5)|accuracy(60)|spd_rtng(45)|shoot_speed(160)|max_ammo(60)|hit_points(110)|body_armor(10)|food_quality(snd_ak47)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["assault_fn_scar_l","XAssault Rifle", [("assault_fn_scar_l", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
750, weapon_length(85)|weight(5)|accuracy(75)|spd_rtng(50)|shoot_speed(160)|max_ammo(20)|hit_points(100)|body_armor(10)|food_quality(snd_assault_modern_fire)|thrust_damage(42, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["assault_fn_scar_cqc","XAssault Rifle", [("assault_fn_scar_cqc", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
750, weapon_length(75)|weight(5)|accuracy(75)|spd_rtng(60)|shoot_speed(160)|max_ammo(20)|hit_points(90)|body_armor(10)|food_quality(snd_assault_modern_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["assault_g36","XAssault Rifle", [("assault_g36", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
600, weapon_length(75)|weight(5)|accuracy(65)|spd_rtng(50)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(10)|food_quality(snd_g36c)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["assault_g36c","XAssault Rifle", [("assault_g36c", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
600, weapon_length(60)|weight(5)|accuracy(65)|spd_rtng(60)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(10)|food_quality(snd_g36c)|thrust_damage(39, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["assault_m16a2","XAssault Rifle", [("assault_m16a2", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
750, weapon_length(100)|weight(5)|accuracy(75)|spd_rtng(60)|shoot_speed(160)|max_ammo(20)|hit_points(100)|body_armor(10)|food_quality(snd_assault_modern_fire)|thrust_damage(41, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["assault_m4a1","XAssault RifleX", [("assault_m4a1", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
800, weapon_length(85)|weight(5)|accuracy(75)|spd_rtng(55)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(10)|food_quality(snd_m4a1)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["assault_remington_m4","XAssault Rifle", [("assault_remington_m4", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
775, weapon_length(90)|weight(5)|accuracy(75)|spd_rtng(60)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(12)|food_quality(snd_assault_modern_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["assault_remington_m4_marksman","XAssault Rifle", [("assault_remington_m4_marksman", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_couchable, itcf_reload_musket,
2850, weapon_length(90)|weight(5)|accuracy(80)|spd_rtng(55)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(12)|food_quality(snd_assault_modern_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
##
["assault_service_rifle","Assault Rifle", [("ar10", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
550, weapon_length(103)|weight(5)|accuracy(65)|spd_rtng(50)|shoot_speed(160)|max_ammo(20)|hit_points(110)|body_armor(15)|food_quality(snd_assaultcarb_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
##
["assault_rab","XAssault Rifle", [("assault_rab", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
500, weapon_length(100)|weight(5)|accuracy(65)|spd_rtng(45)|shoot_speed(160)|max_ammo(20)|hit_points(100)|body_armor(30)|food_quality(snd_assaultcarb_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["assault_maesen_bullpup","XAssault Rifle", [("assault_maesen_bullpup", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
900, weapon_length(60)|weight(5)|accuracy(80)|spd_rtng(48)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(15)|food_quality(snd_m4a1)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["assault_maesen_bullpup_black","XAssault Rifle", [("assault_maesen_bullpup_black", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1100, weapon_length(60)|weight(4.5)|accuracy(83)|spd_rtng(50)|shoot_speed(160)|max_ammo(30)|hit_points(105)|body_armor(12)|food_quality(snd_m4a1)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

# Sniper Rifles
["sniper_old","Sniper_Rifle", [("remington_sniper", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_couchable|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
4100, weapon_length(99)|weight(5)|accuracy(95)|spd_rtng(35)|shoot_speed(160)|max_ammo(5)|hit_points(1800)|body_armor(30)|food_quality(snd_gewehr_sniper)|thrust_damage(65, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
################
##Barbed Wire###
################
##Entenaii Empire
["empire_sniper","Entenaii_Empire_Sniper_Rifle", [("smle_sniper", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_couchable|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
4000, weapon_length(103)|weight(5)|accuracy(95)|spd_rtng(45)|shoot_speed(160)|max_ammo(10)|hit_points(1800)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(65, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Entenaii Dominion
["dominion_sniper","Entenaii_Dominion_Sniper_Rifle", [("metford_sniper", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_couchable|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
4000, weapon_length(103)|weight(5)|accuracy(95)|spd_rtng(45)|shoot_speed(160)|max_ammo(6)|hit_points(1800)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(65, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["dominion_sniper_fanatic","Entenaii_Dominion_Fanatic_Sniper_Rifle", [("metford_sniper_blackened", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_couchable|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
4000, weapon_length(103)|weight(5)|accuracy(95)|spd_rtng(45)|shoot_speed(160)|max_ammo(8)|hit_points(1800)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(70, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Kingdom of Galvae

##Molvat-Berchav Union
["berchav_sniper","Berchav_Sniper_Rifle", [("ukkopekka_sniper", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_couchable|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
3750, weapon_length(113)|weight(6)|accuracy(92)|spd_rtng(49)|shoot_speed(160)|max_ammo(10)|hit_points(1700)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(58, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Vitzland Territories
##Trezzo Republic
##Itami Castedom
##Bashide Confederacy
["bashide_sniper","Bashide_Sniper_Rifle", [("schoenauer_sniper", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_couchable|itp_merchandise, itcf_reload_musket,
8150, weapon_length(101)|weight(5)|accuracy(99)|spd_rtng(30)|shoot_speed(160)|max_ammo(5)|hit_points(2000)|body_armor(35)|food_quality(snd_gewehr_sniper)|thrust_damage(68, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["bashide_sniper_elite","Gidon_Sniper_Rifle", [("schoenauer_sniper_camo", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_couchable|itp_merchandise, itcf_reload_musket,
8150, weapon_length(101)|weight(5)|accuracy(99)|spd_rtng(30)|shoot_speed(160)|max_ammo(5)|hit_points(2000)|body_armor(35)|food_quality(snd_gewehr_sniper)|thrust_damage(80, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
#Renegades
#Throd
["throd_sniper","Theocracy_Sniper_Rifle", [("metford_sniper_throd", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_couchable|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
4000, weapon_length(103)|weight(5)|accuracy(95)|spd_rtng(45)|shoot_speed(160)|max_ammo(6)|hit_points(1800)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(65, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["throd_sniper_blessed","Theocracy_Blessed_Sniper_Rifle", [("metford_sniper_fancy", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_couchable|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
4000, weapon_length(103)|weight(5)|accuracy(95)|spd_rtng(45)|shoot_speed(160)|max_ammo(10)|hit_points(1800)|body_armor(30)|food_quality(snd_trailcarbine_fire)|thrust_damage(85, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

#
["sniper_m24","Sniper_Rifle", [("m1903", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_couchable|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
8150, weapon_length(101)|weight(5)|accuracy(99)|spd_rtng(30)|shoot_speed(160)|max_ammo(5)|hit_points(2000)|body_armor(35)|food_quality(snd_gewehr_sniper)|thrust_damage(72, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

# Shotguns
["shotgun_old","Trench Gun", [("shotgun_old", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
600, weapon_length(75)|weight(7.5)|accuracy(50)|spd_rtng(65)|shoot_speed(160)|max_ammo(8)|hit_points(1800)|body_armor(25)|food_quality(snd_huntingshotgun_fire)|thrust_damage(25, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],
################
##Barbed Wire###
################
##Entenaii Empire
["entenaii_shotgun","Entenaii_Empire_Trench_Gun", [("winchester_m1897", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
550, weapon_length(75)|weight(7.5)|accuracy(50)|spd_rtng(65)|shoot_speed(160)|max_ammo(8)|hit_points(1800)|body_armor(25)|food_quality(snd_huntingshotgun_fire)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],

##Entenaii Dominion
["dominion_shotgun","Entenaii_Dominion_Trench_Gun", [("spencer_m1882", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
675, weapon_length(75)|weight(7.5)|accuracy(50)|spd_rtng(65)|shoot_speed(160)|max_ammo(8)|hit_points(1800)|body_armor(25)|food_quality(snd_huntingshotgun_fire)|thrust_damage(24, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],

##Kingdom of Galvae
["galvae_shotgun","Galvae_Trench_Gun", [("remington_model_31", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
550, weapon_length(75)|weight(7.5)|accuracy(50)|spd_rtng(65)|shoot_speed(160)|max_ammo(8)|hit_points(1800)|body_armor(25)|food_quality(snd_huntingshotgun_fire)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],

##Molvat-Berchav Union
##Vitzland Territories
["vitzland_sawnoff","Vitzland_Sawnoff_Triplebarrel_Shotgun", [("sawed_pirateout", 0),], itp_type_pistol|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
1000, weapon_length(65)|weight(5)|accuracy(50)|spd_rtng(90)|shoot_speed(160)|max_ammo(3)|hit_points(1800)|body_armor(25)|food_quality(snd_sawedoffshotgun_fire)|thrust_damage(30, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],
["vitzland_shotgun","Vitzland_Triplebarrel_Shotgun", [("tripleshotgun", 0),], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
420, weapon_length(85)|weight(3.5)|accuracy(60)|spd_rtng(75)|shoot_speed(160)|max_ammo(3)|hit_points(1800)|body_armor(25)|food_quality(snd_huntingshotgun_fire)|thrust_damage(34, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],

##Trezzo Republic
##Itami Castedom
##Bashide Confederacy

#other
["hunting_shotgun","Hunting Shotgun", [("browning_cynergy", 0),], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
460, weapon_length(85)|weight(3.5)|accuracy(50)|spd_rtng(75)|shoot_speed(160)|max_ammo(2)|hit_points(1800)|body_armor(25)|food_quality(snd_huntingshotgun_fire)|thrust_damage(20, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],
["double_barrel_shotgun","Double_Barrel_Shotgun", [("shotgun_doublebarrel", 0),], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
420, weapon_length(85)|weight(3.5)|accuracy(50)|spd_rtng(75)|shoot_speed(160)|max_ammo(2)|hit_points(1800)|body_armor(25)|food_quality(snd_huntingshotgun_fire)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],
["double_barrel_shotgun_short","Short_Double_Barrel_Shotgun", [("shotgun_doublebarrel_short", 0),], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
410, weapon_length(65)|weight(2.5)|accuracy(40)|spd_rtng(75)|shoot_speed(160)|max_ammo(2)|hit_points(1800)|body_armor(25)|food_quality(snd_sawedoffshotgun_fire)|thrust_damage(22, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],
["double_barrel_shotgun_antique","Antique_Double_Barrel_Shotgun", [("shotgun_caplock", 0),], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
420, weapon_length(80)|weight(4.5)|accuracy(40)|spd_rtng(70)|shoot_speed(160)|max_ammo(2)|hit_points(4000)|body_armor(45)|food_quality(snd_huntingshotgun_fire)|thrust_damage(20, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],

#
["shotgun_sawnoff","Sawnoff Doublebarrel Shotgun", [("shotgun_sawnoff", 0),], itp_type_pistol|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
405, weapon_length(85)|weight(5)|accuracy(40)|spd_rtng(75)|shoot_speed(160)|max_ammo(2)|hit_points(800)|body_armor(25)|food_quality(snd_sawedoffshotgun_fire)|thrust_damage(18, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],
["shotgun_short_old","Short Trench Gun", [("shotgun_short_old", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
450, weapon_length(61)|weight(5)|accuracy(40)|spd_rtng(70)|shoot_speed(160)|max_ammo(6)|hit_points(900)|body_armor(25)|food_quality(snd_huntingshotgun_fire)|thrust_damage(18, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],

["shotgun_aa12","XHell GunX", [("shotgun_aa12", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1000, weapon_length(50)|weight(8)|accuracy(50)|spd_rtng(70)|shoot_speed(160)|max_ammo(20)|hit_points(200)|body_armor(25)|food_quality(snd_shotguncombat_fire)|thrust_damage(15, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],
#
["shotgun_benelli_m4","Semi-Automatic_Shotgun", [("browning_auto", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
750, weapon_length(85)|weight(5)|accuracy(50)|spd_rtng(65)|shoot_speed(160)|max_ammo(5)|hit_points(1800)|body_armor(25)|food_quality(snd_riotshotgun_fire)|thrust_damage(16, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],
#
["shotgun_maesen_spas12","XTrench Gun", [("shotgun_maesen_spas12", 0)], itp_type_musket|itp_two_handed|itp_primary, itcf_reload_musket,
750, weapon_length(85)|weight(5)|accuracy(50)|spd_rtng(70)|shoot_speed(160)|max_ammo(8)|hit_points(1800)|body_armor(25)|food_quality(snd_shotguncombat_fire)|thrust_damage(15, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],

["shotgun_handcannon","Makeshift Trench Gun", [("shotgun_handcannon", 0),], itp_type_pistol|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_pistol|itcf_carry_revolver_right,
350, weapon_length(85)|weight(7.5)|accuracy(40)|spd_rtng(70)|shoot_speed(160)|max_ammo(2)|hit_points(900)|body_armor(30)|food_quality(snd_sawedoffshotgun_fire)|thrust_damage(16, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],

["shotgun_short","XShort Trench GunX", [("shotgun_short", 0)], itp_type_musket|itp_two_handed|itp_primary, itcf_reload_musket,
750, weapon_length(65)|weight(5)|accuracy(50)|spd_rtng(70)|shoot_speed(160)|max_ammo(6)|hit_points(700)|body_armor(25)|food_quality(snd_riotshotgun_fire)|thrust_damage(16, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],

["shotgun_toz87","Trench Gun", [("shotgun_toz87", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
500, weapon_length(75)|weight(7.5)|accuracy(50)|spd_rtng(65)|shoot_speed(160)|max_ammo(8)|hit_points(1800)|body_armor(25)|food_quality(snd_huntingshotgun_fire)|thrust_damage(25, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],

#Blunt_Shotgun
["shotgun_riot","Riot Gun", [("shotgun_riot", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_merchandise, itcf_reload_musket,
950, weapon_length(75)|weight(7.5)|accuracy(50)|spd_rtng(65)|shoot_speed(160)|max_ammo(8)|hit_points(1800)|body_armor(25)|food_quality(snd_riotshotgun_fire)|thrust_damage(22, blunt), imodbits_gun, [ranged_weapon_triggers,scope_add,shotgun_fire_ai]],

# Big Guns
# LMGs
["lmg_pkm_hip","XLight Machine GunX", [("lmg_pkm", 0)], itp_type_musket|itp_next_item_as_melee|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1250, weapon_length(95)|weight(10)|accuracy(70)|spd_rtng(40)|shoot_speed(160)|max_ammo(100)|hit_points(100)|body_armor(19)|food_quality(snd_m249)|thrust_damage(45, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["lmg_pkm","XLight Machine GunX", [("lmg_pkm", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1250, weapon_length(95)|weight(10)|accuracy(65)|spd_rtng(40)|shoot_speed(160)|max_ammo(100)|hit_points(100)|body_armor(3)|food_quality(snd_m249)|thrust_damage(45, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
################
##Barbed Wire###
################
##Entenaii Empire
["entenaii_empire_lmg_hip","Entenaii Empire Light Machine Gun", [("lewis", 0)], itp_type_musket|itp_next_item_as_melee|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
1300, weapon_length(118)|weight(14)|accuracy(85)|spd_rtng(40)|shoot_speed(160)|max_ammo(97)|hit_points(90)|body_armor(18)|food_quality(snd_type99)|thrust_damage(43, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["entenaii_empire_lmg","Entenaii Empire Light Machine Gun", [("lewis", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1300, weapon_length(118)|weight(14)|accuracy(65)|spd_rtng(40)|shoot_speed(160)|max_ammo(97)|hit_points(90)|body_armor(1)|food_quality(snd_type99)|thrust_damage(43, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Entenaii Dominion
["entenaii_dominion_lmg_hip","Entenaii Dominion Light Machine Gun", [("hotchkiss1909", 0)], itp_type_musket|itp_next_item_as_melee|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
930, weapon_length(113)|weight(12)|accuracy(70)|spd_rtng(40)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(19)|food_quality(snd_m249)|thrust_damage(45, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["entenaii_dominion_lmg","Entenaii Dominion Light Machine Gun", [("hotchkiss1909", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
930, weapon_length(113)|weight(12)|accuracy(65)|spd_rtng(40)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(3)|food_quality(snd_m249)|thrust_damage(45, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Kingdom of Galvae
["galvae_lmg_hip","Galvae Light Machine Gun", [("madsen", 0)], itp_type_musket|itp_next_item_as_melee|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
1150, weapon_length(104)|weight(10)|accuracy(85)|spd_rtng(40)|shoot_speed(160)|max_ammo(30)|hit_points(90)|body_armor(18)|food_quality(snd_type99)|thrust_damage(43, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["galvae_lmg","Galvae Light Machine Gun", [("madsen", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1150, weapon_length(104)|weight(10)|accuracy(65)|spd_rtng(40)|shoot_speed(160)|max_ammo(30)|hit_points(90)|body_armor(1)|food_quality(snd_type99)|thrust_damage(43, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Molvat-Berchav Union
["molvat_lmg_hip","Molvat Light Machine Gun", [("dp27_alt", 0)], itp_type_musket|itp_next_item_as_melee|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
1050, weapon_length(118)|weight(14)|accuracy(85)|spd_rtng(40)|shoot_speed(160)|max_ammo(47)|hit_points(90)|body_armor(18)|food_quality(snd_type99)|thrust_damage(43, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["molvat_lmg","Molvat Light Machine Gun", [("dp27", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1050, weapon_length(118)|weight(14)|accuracy(65)|spd_rtng(40)|shoot_speed(160)|max_ammo(47)|hit_points(90)|body_armor(1)|food_quality(snd_type99)|thrust_damage(43, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Vitzland Territories
["vitzland_lmg_hip","Vitzland Light Machine Gun", [("mg0815", 0)], itp_type_musket|itp_next_item_as_melee|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
1500, weapon_length(95)|weight(18)|accuracy(40)|spd_rtng(40)|shoot_speed(160)|max_ammo(200)|hit_points(100)|body_armor(19)|food_quality(snd_m249)|thrust_damage(44, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["vitzland_lmg","Vitzland Light Machine Gun", [("mg0815", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1500, weapon_length(95)|weight(18)|accuracy(65)|spd_rtng(40)|shoot_speed(160)|max_ammo(200)|hit_points(100)|body_armor(3)|food_quality(snd_m249)|thrust_damage(44, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["vitzland_lmg_2_hip","Vitzland Light Machine Gun", [("m15st61", 0)], itp_type_musket|itp_next_item_as_melee|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
1500, weapon_length(95)|weight(18)|accuracy(40)|spd_rtng(40)|shoot_speed(160)|max_ammo(75)|hit_points(100)|body_armor(19)|food_quality(snd_m249)|thrust_damage(45, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["vitzland_lmg_2","Vitzland Light Machine Gun", [("m15st61", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1500, weapon_length(95)|weight(18)|accuracy(65)|spd_rtng(40)|shoot_speed(160)|max_ammo(75)|hit_points(100)|body_armor(3)|food_quality(snd_m249)|thrust_damage(45, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Trezzo Republic
["trezzo_lmg_hip","Trezzo Light Machine Gun", [("bredam30", 0)], itp_type_musket|itp_next_item_as_melee|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
930, weapon_length(113)|weight(12)|accuracy(70)|spd_rtng(40)|shoot_speed(160)|max_ammo(20)|hit_points(100)|body_armor(19)|food_quality(snd_m249)|thrust_damage(43, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["trezzo_lmg","Trezzo Light Machine Gun", [("bredam30", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
930, weapon_length(113)|weight(12)|accuracy(65)|spd_rtng(40)|shoot_speed(160)|max_ammo(20)|hit_points(100)|body_armor(3)|food_quality(snd_m249)|thrust_damage(43, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],


##Itami Castedom
["itami_lmg_hip","Itami Light Machine Gun", [("waibazi", 0)], itp_type_musket|itp_next_item_as_melee|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
930, weapon_length(113)|weight(12)|accuracy(70)|spd_rtng(40)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(19)|food_quality(snd_m249)|thrust_damage(45, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["itami_lmg","Itami Light Machine Gun", [("waibazi", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
930, weapon_length(113)|weight(12)|accuracy(65)|spd_rtng(40)|shoot_speed(160)|max_ammo(30)|hit_points(100)|body_armor(3)|food_quality(snd_m249)|thrust_damage(45, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

##Bashide Confederacy
["bashide_lmg_hip","Bashide_Light_Machine_Gun", [("mg13", 0)], itp_type_musket|itp_next_item_as_melee|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
1500, weapon_length(95)|weight(11)|accuracy(40)|spd_rtng(40)|shoot_speed(160)|max_ammo(25)|hit_points(100)|body_armor(19)|food_quality(snd_m249)|thrust_damage(38, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["bashide_lmg","Bashide_Light_Machine_Gun", [("mg13bp", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1500, weapon_length(95)|weight(11)|accuracy(65)|spd_rtng(40)|shoot_speed(160)|max_ammo(25)|hit_points(100)|body_armor(3)|food_quality(snd_m249)|thrust_damage(38, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

#
["shadow_lmg_hip","Shadow_Operative_Light_Machine_Gun", [("mg34_lmg_carry", 0)], itp_type_musket|itp_next_item_as_melee|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
1500, weapon_length(95)|weight(12)|accuracy(40)|spd_rtng(40)|shoot_speed(160)|max_ammo(50)|hit_points(50)|body_armor(19)|food_quality(snd_m249)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["shadow_lmg","Shadow_Operative_Light_Machine_Gun", [("mg34_lmg", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1500, weapon_length(95)|weight(12)|accuracy(65)|spd_rtng(40)|shoot_speed(160)|max_ammo(50)|hit_points(50)|body_armor(3)|food_quality(snd_m249)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["shadow_lmg_2_hip","Shadow_Operative_Light_Machine_Gun", [("mg42_lmg_carry", 0)], itp_type_musket|itp_next_item_as_melee|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
1800, weapon_length(95)|weight(12)|accuracy(50)|spd_rtng(40)|shoot_speed(160)|max_ammo(50)|hit_points(40)|body_armor(19)|food_quality(snd_m249)|thrust_damage(42, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["shadow_lmg_2","Shadow_Operative_Light_Machine_Gun", [("mg42_lmg", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1800, weapon_length(95)|weight(12)|accuracy(75)|spd_rtng(40)|shoot_speed(160)|max_ammo(50)|hit_points(40)|body_armor(3)|food_quality(snd_m249)|thrust_damage(42, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

#
["lmg_type_99_hip","Itami Light Machine Gun", [("lmg_type_99", 0)], itp_type_musket|itp_next_item_as_melee|itp_two_handed|itp_primary|itp_has_bayonet|itp_merchandise, itcf_reload_musket,
1250, weapon_length(102)|weight(7.5)|accuracy(85)|spd_rtng(40)|shoot_speed(160)|max_ammo(30)|hit_points(90)|body_armor(18)|food_quality(snd_type99)|thrust_damage(43, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["lmg_type_99","Itami Light Machine Gun", [("lmg_type_99", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
1250, weapon_length(102)|weight(7.5)|accuracy(65)|spd_rtng(40)|shoot_speed(160)|max_ammo(30)|hit_points(90)|body_armor(1)|food_quality(snd_type99)|thrust_damage(43, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

# Minigun
["mg_gatling_cannon","HMG", [("maxim", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
9500, weapon_length(95)|weight(50)|accuracy(70)|spd_rtng(25)|shoot_speed(160)|max_ammo(500)|hit_points(80)|body_armor(5)|abundance(8)|food_quality(snd_autorifle_fire)|thrust_damage(30, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

#Vickers
["mg_heavy_1","HMG", [("vickers_handheld", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
6500, weapon_length(95)|weight(50)|accuracy(70)|spd_rtng(25)|shoot_speed(160)|max_ammo(500)|hit_points(130)|body_armor(5)|abundance(8)|food_quality(snd_autorifle_fire)|thrust_damage(30, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

#mg_tyrant
["mg_tyrant","HMG_tyrant", [("dummy_mesh", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet|itp_unique|itp_no_pick_up_from_ground, itcf_reload_musket,
10000, weapon_length(20)|weight(40)|accuracy(60)|spd_rtng(35)|shoot_speed(160)|max_ammo(500)|hit_points(100)|body_armor(20)|food_quality(snd_autorifle_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

# Auto Cannon
["mg_auto_cannon","HMG", [("type_3", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
12500, weapon_length(140)|weight(30)|accuracy(70)|spd_rtng(35)|shoot_speed(160)|max_ammo(500)|hit_points(100)|body_armor(20)|abundance(10)|food_quality(snd_autorifle_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

# Energy Weapons
# Pistols
["pistol_plasma","Experimental Pistol", [("pistol_plasma", 0),], itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
1250, weapon_length(20)|weight(1.5)|accuracy(80)|spd_rtng(55)|shoot_speed(160)|max_ammo(20)|hit_points(150)|body_armor(8)|abundance(50)|food_quality(snd_plasmapistol_fire)|thrust_damage(40, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
["pistol_plasma_heavy","Heavy Experimental Pistol", [("pistol_plasma_heavy", 0),], itp_type_pistol|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
1250, weapon_length(32)|weight(2.5)|accuracy(75)|spd_rtng(50)|shoot_speed(160)|max_ammo(25)|hit_points(200)|body_armor(10)|abundance(50)|food_quality(snd_plasmapistol_fire)|thrust_damage(45, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
# Rifles
["rifle_plasma","Experimental Rifle", [("rifle_plasma", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
2500, weapon_length(48)|weight(3.5)|accuracy(75)|spd_rtng(45)|shoot_speed(160)|max_ammo(40)|hit_points(250)|body_armor(15)|abundance(50)|food_quality(snd_plasmarifle_fire)|thrust_damage(50, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],
# Special
# Flamer
["flamethrower","Flamethrower", [("m2projector", 0)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
750, weapon_length(85)|weight(5)|accuracy(50)|spd_rtng(70)|shoot_speed(30)|max_ammo(30)|hit_points(200)|body_armor(15)|food_quality(snd_flamer_fire)|thrust_damage(35, cut), imodbits_none, [
   (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (gt,":agent",0),
       (set_position_delta,0,27,0),
       (particle_system_add_new,"psys_candle_light"),
      # (set_current_color, 150, 130, 70),
      # (add_point_light, 10, 30),
      #(particle_system_burst,"psys_candle_light_small", pos11, 5), # used for visualization
      ]),
    (ti_on_weapon_attack, [
      (store_trigger_param_1,":agent"),
      (neq,":agent","$g_player"),

      (call_script,"script_flamer_fire", pos1,":agent"),
	  (store_mission_timer_a, ":time"),
	  
	  (val_add, ":time", 30),
	  (agent_set_slot, ":agent", slot_agent_last_time_hit_enemy, ":time"),
	  ]),
   ]],   
   
["flamethrower_vitzland","Flamelauncher", [("handflammpatrone", 0)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary, itcf_reload_musket,
750, weapon_length(85)|weight(5)|accuracy(50)|spd_rtng(70)|shoot_speed(30)|max_ammo(1)|hit_points(200)|body_armor(15)|food_quality(snd_flamer_fire)|thrust_damage(35, cut), imodbits_none, [
   (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (gt,":agent",0),
       (set_position_delta,0,27,0),
       (particle_system_add_new,"psys_candle_light"),
      # (set_current_color, 150, 130, 70),
      # (add_point_light, 10, 30),
      #(particle_system_burst,"psys_candle_light_small", pos11, 5), # used for visualization
      ]),
    (ti_on_weapon_attack, [
      (store_trigger_param_1,":agent"),
      (neq,":agent","$g_player"),

      (call_script,"script_flamer_fire", pos1,":agent"),
	  (store_mission_timer_a, ":time"),
	  
	  (val_add, ":time", 30),
	  (agent_set_slot, ":agent", slot_agent_last_time_hit_enemy, ":time"),
	  ]),
   ]],
["flamethrower_vitzland_pistol","Pistol_Flamelauncher", [("double_flaregun", 0)], itp_type_pistol|itp_merchandise|itp_two_handed|itp_primary, itcf_reload_pistol|itcf_carry_revolver_right,
750, weapon_length(35)|weight(2.5)|accuracy(50)|spd_rtng(70)|shoot_speed(30)|max_ammo(2)|hit_points(200)|body_armor(15)|food_quality(snd_flamer_fire)|thrust_damage(20, cut), imodbits_none, [
   (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (gt,":agent",0),
       (set_position_delta,0,27,0),
       (particle_system_add_new,"psys_candle_light"),
      # (set_current_color, 150, 130, 70),
      # (add_point_light, 10, 30),
      #(particle_system_burst,"psys_candle_light_small", pos11, 5), # used for visualization
      ]),
    (ti_on_weapon_attack, [
      (store_trigger_param_1,":agent"),
      (neq,":agent","$g_player"),

      (call_script,"script_flamer_fire", pos1,":agent"),
	  (store_mission_timer_a, ":time"),
	  
	  (val_add, ":time", 30),
	  (agent_set_slot, ":agent", slot_agent_last_time_hit_enemy, ":time"),
	  ]),
   ]],

["flamethrower_union","Flamethrower", [("roks_projector", 0)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
750, weapon_length(85)|weight(5)|accuracy(50)|spd_rtng(70)|shoot_speed(30)|max_ammo(30)|hit_points(200)|body_armor(15)|food_quality(snd_flamer_fire)|thrust_damage(35, cut), imodbits_none, [
   (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (gt,":agent",0),
       (set_position_delta,0,27,0),
       (particle_system_add_new,"psys_candle_light"),
      # (set_current_color, 150, 130, 70),
      # (add_point_light, 10, 30),
      #(particle_system_burst,"psys_candle_light_small", pos11, 5), # used for visualization
      ]),
    (ti_on_weapon_attack, [
      (store_trigger_param_1,":agent"),
      (neq,":agent","$g_player"),

      (call_script,"script_flamer_fire", pos1,":agent"),
	  (store_mission_timer_a, ":time"),
	  
	  (val_add, ":time", 30),
	  (agent_set_slot, ":agent", slot_agent_last_time_hit_enemy, ":time"),
	  ]),
   ]],
#
["flamethrower_ashmaker","Ashmaker_Flamethrower", [("ash_flamethrower", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
750, weapon_length(85)|weight(5)|accuracy(50)|spd_rtng(70)|shoot_speed(30)|max_ammo(30)|hit_points(200)|body_armor(15)|food_quality(snd_flamer_fire)|thrust_damage(37, cut), imodbits_none, [
   (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (gt,":agent",0),
       (set_position_delta,0,27,0),
       (particle_system_add_new,"psys_candle_light"),
      # (set_current_color, 150, 130, 70),
      # (add_point_light, 10, 30),
      #(particle_system_burst,"psys_candle_light_small", pos11, 5), # used for visualization
      ]),
    (ti_on_weapon_attack, [
      (store_trigger_param_1,":agent"),
      (neq,":agent","$g_player"),

      (call_script,"script_flamer_fire", pos1,":agent"),
	  (store_mission_timer_a, ":time"),
	  
	  (val_add, ":time", 30),
	  (agent_set_slot, ":agent", slot_agent_last_time_hit_enemy, ":time"),
	  ]),
   ]],   
#
["flamethrower_bashide","Flamethrower", [("flamethrower_1", 0)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_has_bayonet, itcf_reload_musket,
750, weapon_length(85)|weight(5)|accuracy(50)|spd_rtng(70)|shoot_speed(30)|max_ammo(30)|hit_points(200)|body_armor(15)|food_quality(snd_flamer_fire)|thrust_damage(35, cut), imodbits_none, [
   (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (gt,":agent",0),
       (set_position_delta,0,27,0),
       (particle_system_add_new,"psys_candle_light"),
      # (set_current_color, 150, 130, 70),
      # (add_point_light, 10, 30),
      #(particle_system_burst,"psys_candle_light_small", pos11, 5), # used for visualization
      ]),
    (ti_on_weapon_attack, [
      (store_trigger_param_1,":agent"),
      (neq,":agent","$g_player"),

      (call_script,"script_flamer_fire", pos1,":agent"),
	  (store_mission_timer_a, ":time"),
	  
	  (val_add, ":time", 30),
	  (agent_set_slot, ":agent", slot_agent_last_time_hit_enemy, ":time"),
	  ]),
   ]],   
#

# mech_weapons
["cannon_tyrant","Tyrant-class_Artillery_Cannon", [("tyrant_cannon", 0)], itp_type_musket|itp_two_handed|itp_primary|itp_unique|itp_no_pick_up_from_ground, itcf_reload_musket,
9500, weapon_length(20)|weight(50)|accuracy(40)|spd_rtng(50)|shoot_speed(100)|max_ammo(1)|hit_points(8000)|body_armor(100)|food_quality(snd_rpgshot)|thrust_damage(100, pierce), imodbits_none, [ranged_weapon_triggers,scope_add]],

#
["entenaii_antitank_rifle","Entenaii_Anti-tank_Rifle",[("boys",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
2500, weapon_length(120)|weight(10)|accuracy(55)|spd_rtng(25)|shoot_speed(160)|max_ammo(5)|hit_points(50000)|body_armor(80)|food_quality(snd_gewehr_sniper)|thrust_damage(120, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["union_antitank_rifle","Vitzland_Anti-tank_Rifle",[("ptrd-41",0)],
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
2500, weapon_length(117)|weight(10)|accuracy(55)|spd_rtng(25)|shoot_speed(160)|max_ammo(1)|hit_points(50000)|body_armor(80)|food_quality(snd_gewehr_sniper)|thrust_damage(120, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["vitzland_antitank_rifle","Vitzland_Anti-tank_Rifle",[("tankgewehr",0)], 
itp_type_musket|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_merchandise, itcf_reload_musket,
2500, weapon_length(117)|weight(10)|accuracy(55)|spd_rtng(25)|shoot_speed(160)|max_ammo(1)|hit_points(50000)|body_armor(80)|food_quality(snd_gewehr_sniper)|thrust_damage(120, pierce), imodbits_gun, [ranged_weapon_triggers,scope_add]],

["itami_grenadelauncher","Itami Grenade Launcher", [("chinalake", 0)], itp_type_musket|itp_two_handed|itp_primary, itcf_reload_musket,
1000, weapon_length(50)|weight(5)|accuracy(60)|spd_rtng(50)|shoot_speed(100)|max_ammo(3)|hit_points(8000)|body_armor(100)|food_quality(snd_sawedoffshotgun_fire)|thrust_damage(30, pierce), imodbits_none, [ranged_weapon_triggers,scope_add]],

["rocketlauncher","Rocket Launcher", [("rpg_1", 0)], itp_type_musket|itp_two_handed|itp_primary, itcf_reload_musket,
9500, weapon_length(20)|weight(50)|accuracy(50)|spd_rtng(50)|shoot_speed(100)|max_ammo(1)|hit_points(8000)|body_armor(100)|food_quality(snd_rpgshot)|thrust_damage(100, pierce), imodbits_none, [ranged_weapon_triggers,scope_add]],

##WARNING - to avoid compiling problems add new guns somewhere before this buffer section. Don't add more than 9 new guns at most before compiling a couple of times. Compile regularly! - krag
   
["buffer_gun_1","buffer_gun", [("dummy_mesh", 0)], itp_type_musket|itp_unique|itp_two_handed|itp_primary, itcf_reload_musket, 1, weight(1)|accuracy(1)|spd_rtng(1)|shoot_speed(1)|max_ammo(1)|thrust_damage(1, cut), imodbits_none, []],
["buffer_gun_2","buffer_gun", [("dummy_mesh", 0)], itp_type_musket|itp_unique|itp_two_handed|itp_primary, itcf_reload_musket, 1, weight(1)|accuracy(1)|spd_rtng(1)|shoot_speed(1)|max_ammo(1)|thrust_damage(1, cut), imodbits_none, []],
["buffer_gun_3","buffer_gun", [("dummy_mesh", 0)], itp_type_musket|itp_unique|itp_two_handed|itp_primary, itcf_reload_musket, 1, weight(1)|accuracy(1)|spd_rtng(1)|shoot_speed(1)|max_ammo(1)|thrust_damage(1, cut), imodbits_none, []],
["buffer_gun_4","buffer_gun", [("dummy_mesh", 0)], itp_type_musket|itp_unique|itp_two_handed|itp_primary, itcf_reload_musket, 1, weight(1)|accuracy(1)|spd_rtng(1)|shoot_speed(1)|max_ammo(1)|thrust_damage(1, cut), imodbits_none, []],
["buffer_gun_5","buffer_gun", [("dummy_mesh", 0)], itp_type_musket|itp_unique|itp_two_handed|itp_primary, itcf_reload_musket, 1, weight(1)|accuracy(1)|spd_rtng(1)|shoot_speed(1)|max_ammo(1)|thrust_damage(1, cut), imodbits_none, []],
["buffer_gun_6","buffer_gun", [("dummy_mesh", 0)], itp_type_musket|itp_unique|itp_two_handed|itp_primary, itcf_reload_musket, 1, weight(1)|accuracy(1)|spd_rtng(1)|shoot_speed(1)|max_ammo(1)|thrust_damage(1, cut), imodbits_none, []],
["buffer_gun_7","buffer_gun", [("dummy_mesh", 0)], itp_type_musket|itp_unique|itp_two_handed|itp_primary, itcf_reload_musket, 1, weight(1)|accuracy(1)|spd_rtng(1)|shoot_speed(1)|max_ammo(1)|thrust_damage(1, cut), imodbits_none, []],
["buffer_gun_8","buffer_gun", [("dummy_mesh", 0)], itp_type_musket|itp_unique|itp_two_handed|itp_primary, itcf_reload_musket, 1, weight(1)|accuracy(1)|spd_rtng(1)|shoot_speed(1)|max_ammo(1)|thrust_damage(1, cut), imodbits_none, []],
["buffer_gun_9","buffer_gun", [("dummy_mesh", 0)], itp_type_musket|itp_unique|itp_two_handed|itp_primary, itcf_reload_musket, 1, weight(1)|accuracy(1)|spd_rtng(1)|shoot_speed(1)|max_ammo(1)|thrust_damage(1, cut), imodbits_none, []],
["buffer_gun_10","buffer_gun", [("dummy_mesh", 0)], itp_type_musket|itp_unique|itp_two_handed|itp_primary, itcf_reload_musket, 1, weight(1)|accuracy(1)|spd_rtng(1)|shoot_speed(1)|max_ammo(1)|thrust_damage(1, cut), imodbits_none, []],

#GUNS END
["rpg","GUNS END", [("dummy_mesh", 0)], itp_type_musket|itp_two_handed|itp_primary, itcf_reload_musket,
9500, weapon_length(20)|weight(50)|accuracy(40)|spd_rtng(50)|shoot_speed(100)|max_ammo(1)|hit_points(8000)|body_armor(100)|food_quality(snd_rpgshot)|thrust_damage(100, pierce), imodbits_none, [ranged_weapon_triggers,scope_add]],
	  
##rpg marks the end of guns in header_items and module_constants, must always exist and be last - krag

##WARNING - to avoid compiling problems add new guns BEFORE the buffer section above. Don't add more than 9 new guns before compiling a couple of times - krag

############
##Throwing##
############
# Grenades
["grenade","Grenades", [("grenade", 0)], itp_type_thrown|itp_primary|itp_secondary|itp_merchandise, itcf_throw_stone,
1660, weight(3.5)|abundance(80)|spd_rtng(97)|shoot_speed(30)|weapon_length(8)|max_ammo(3)|thrust_damage(45, cut), imodbits_missile, [ranged_weapon_triggers,
    (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (call_script,"script_create_explosion", pos1,":agent","itm_grenade", 1000, 75, 105, 0), #5 75
    ]),
	# (ti_on_weapon_attack, [
      # (store_trigger_param_1,":agent"),
      # (agent_get_wielded_item, ":wielded", ":agent", 0),
	  # (agent_get_ammo, ":ammo", ":agent", 1),
	  # (val_sub, ":ammo", 1),
	  # (agent_set_ammo, ":agent", ":wielded", ":ammo"),
    # ]),
	]],#the all formerly had |itp_remove_item_on_use but seemed inconsistent

["grenade_2","Grenades", [("mills", 0)], itp_type_thrown|itp_primary|itp_secondary|itp_merchandise, itcf_throw_stone,
1660, weight(3.5)|abundance(80)|spd_rtng(97)|shoot_speed(30)|weapon_length(8)|max_ammo(3)|thrust_damage(45, cut), imodbits_missile, [ranged_weapon_triggers,
    (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (call_script,"script_create_explosion", pos1,":agent","itm_grenade_2", 1000, 75, 105, 0), #5 75
    ]),
	# (ti_on_weapon_attack, [
      # (store_trigger_param_1,":agent"),
      # (agent_get_wielded_item, ":wielded", ":agent", 0),
	  # (agent_get_ammo, ":ammo", ":agent", 1),
	  # (val_sub, ":ammo", 1),
	  # (agent_set_ammo, ":agent", ":wielded", ":ammo"),
    # ]),
	]],#the all formerly had |itp_remove_item_on_use but seemed inconsistent

["grenade_stick","Stick Grenades", [("grenade_stick", 0)], itp_type_thrown|itp_primary|itp_merchandise, itcf_throw_stone,
1260, weight(3.5)|abundance(80)|spd_rtng(97)|shoot_speed(30)|weapon_length(8)|max_ammo(3)|thrust_damage(35, cut), imodbits_missile, [ranged_weapon_triggers,
    (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (call_script,"script_create_explosion", pos1,":agent","itm_grenade_stick", 1000, 75, 105, 0), #5 75
    ]),]],
    
["grenade_dyna","Dynamite_Stick", [("dyna", 0)], itp_type_thrown|itp_primary|itp_merchandise, itcf_throw_stone,
1260, weight(3.5)|abundance(80)|spd_rtng(97)|shoot_speed(30)|weapon_length(8)|max_ammo(3)|thrust_damage(35, cut), imodbits_missile, [ranged_weapon_triggers,
    (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (call_script,"script_create_explosion", pos1,":agent","itm_grenade_dyna", 1000, 75, 105, 0), #5 75
    ]),]],

["grenade_stick_2","Stick Grenades", [("rg12", 0)], itp_type_thrown|itp_primary|itp_merchandise, itcf_throw_stone,
1260, weight(3.5)|abundance(80)|spd_rtng(97)|shoot_speed(30)|weapon_length(8)|max_ammo(3)|thrust_damage(35, cut), imodbits_missile, [ranged_weapon_triggers,
    (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (call_script,"script_create_explosion", pos1,":agent","itm_grenade_stick_2", 1000, 75, 105, 0), #5 75
    ]),]],

["grenade_stick_bundle","Stick_Grenade_Bundle", [("grenade_stick_bundle", 0)], itp_type_thrown|itp_primary|itp_merchandise, itcf_throw_stone,
5050, weight(9)|abundance(10)|spd_rtng(88)|shoot_speed(18)|weapon_length(8)|max_ammo(1)|thrust_damage(175, cut), imodbits_missile, [ranged_weapon_triggers,
    (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (call_script,"script_create_explosion", pos1,":agent","itm_grenade_stick_bundle", 1000, 100, 150, 0), #5 75
    ]),]],
    
["hand_torpedo","Torpedo", [("bangalore", 0)], itp_type_thrown|itp_primary|itp_merchandise, itcf_throw_javelin,
5050, weight(9)|abundance(10)|spd_rtng(88)|shoot_speed(18)|weapon_length(8)|max_ammo(1)|thrust_damage(150, cut), imodbits_missile, [ranged_weapon_triggers,
    (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (call_script,"script_create_explosion", pos1,":agent","itm_hand_torpedo", 1000, 100, 150, 0), #5 75
    ]),]],

# Frag grenade
["grenade_frag","Fragmentation Grenades", [("grenade_frag", 0)], itp_type_thrown|itp_primary|itp_merchandise, itcf_throw_stone,
1430, weight(3.5)|abundance(80)|spd_rtng(97)|shoot_speed(30)|weapon_length(8)|max_ammo(3)|thrust_damage(40, cut), imodbits_missile, [ranged_weapon_triggers,
    (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (call_script,"script_create_explosion", pos1,":agent","itm_grenade_frag", 1000, 80, 110, 0),
      ]),]],

["grenade_smoke","Smoke Grenades", [("grenade_smoke", 0)], itp_type_thrown|itp_secondary, itcf_throw_stone,
730, weight(3.5)|abundance(80)|spd_rtng(97)|shoot_speed(30)|weapon_length(8)|max_ammo(3)|thrust_damage(10, blunt), imodbits_missile, [ranged_weapon_triggers,
    (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (assign,"$smokeg_thrown", 1),
      (call_script,"script_smoke_grenade", pos1,":agent", 2000),
    ]),]],

["grenade_flash","Flash Grenades", [("grenade_flash", 0)], itp_type_thrown|itp_secondary, itcf_throw_stone,
830, weight(3.5)|abundance(80)|spd_rtng(97)|shoot_speed(30)|weapon_length(8)|max_ammo(3)|thrust_damage(10, blunt), imodbits_missile, [ranged_weapon_triggers,
    (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (assign,"$flashbang_thrown", 1),
      (call_script,"script_flash_bang", pos1,":agent", 1000, 1),
    ]),]],

# Molotov cocktail
["grenade_molotov","Firebomb", [("grenade_molotov", 0)], itp_type_thrown|itp_primary|itp_merchandise, itcf_throw_stone,
930, weight(3.5)|spd_rtng(97)|shoot_speed(30)|weapon_length(8)|max_ammo(3)|thrust_damage(30, cut), imodbits_missile, [ranged_weapon_triggers,
    (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (call_script,"script_create_explosion", pos1,":agent","itm_grenade_molotov", 1000, 55, 85, 0),
    ]),]],
["grenade_molotov_ashmaker","Ashmaker_Firebomb", [("ashmaker_molotov", 0)], itp_type_thrown|itp_primary|itp_merchandise, itcf_throw_stone,
1130, weight(3.5)|spd_rtng(98)|shoot_speed(30)|weapon_length(8)|max_ammo(4)|thrust_damage(30, cut), imodbits_missile, [ranged_weapon_triggers,
    (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (call_script,"script_create_explosion", pos1,":agent","itm_grenade_molotov_ashmaker", 1000, 60, 95, 0),
    ]),]],

#miasma grenade - creates Trench Zombies
["grenade_miasma","Miasma Grenades", [("biogrenade", 0)], itp_type_thrown|itp_secondary, itcf_throw_stone,
4000, weight(3.5)|abundance(10)|spd_rtng(97)|shoot_speed(30)|weapon_length(8)|max_ammo(2)|thrust_damage(10, blunt), imodbits_missile, [ranged_weapon_triggers,
    (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (assign,"$smokeg_thrown", 1),
      (call_script,"script_miasma_grenade", pos1,":agent", 2000),
    ]),]],
    
#other throwing
    
# Stone
["stones",        "Stones", [("throwing_stone",0)], itp_type_thrown|itp_primary|itp_next_item_as_melee|itp_merchandise, itcf_throw_stone,
  1 , weight(4)|accuracy(65)|spd_rtng(97) | shoot_speed(30) | thrust_damage(15 ,  blunt)|max_ammo(18)|weapon_length(8),imodbit_large_bag ],
["stones_alt",        "Stones", [("throwing_stone",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_scimitar,
  1 , weight(1)|spd_rtng(97) | weapon_length(10)|swing_damage(15 , blunt),imodbits_none ],

# Spear
["throwing_spears",        "Throwing Spears", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee|itp_merchandise ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
  525 , weight(3)|accuracy(65)|spd_rtng(87) | shoot_speed(22) | thrust_damage(44 ,  pierce)|max_ammo(4)|weapon_length(65),imodbits_thrown ],
["throwing_spear_melee",        "Throwing Spear", [("javelin",0),("javelins_quiver_new", ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_wooden_parry , itcf_thrust_onehanded,
  525 , weight(1)|spd_rtng(91) | swing_damage(18, cut) | thrust_damage(23 ,  pierce)|weapon_length(75),imodbits_thrown ],

["throwing_metal_spears",        "Throwing Metal Spears", [("metal_javelin",0)], itp_type_thrown |itp_primary|itp_next_item_as_melee|itp_merchandise ,itcf_throw_javelin,
  525 , weight(3)|accuracy(65)|spd_rtng(92) | shoot_speed(27) | thrust_damage(44 ,  pierce)|max_ammo(4)|weapon_length(39),imodbits_thrown ],
["throwing_metal_spear_melee",        "Throwing Metal Spear", [("metal_javelin",0)],itp_type_one_handed_wpn|itp_primary , itcf_thrust_onehanded,
  525 , weight(1)|spd_rtng(96) | swing_damage(18, cut) | thrust_damage(20 ,  pierce)|weapon_length(49),imodbits_thrown ],

#Throwing knife
["throwing_knives","Throwing Knives",[("throwing_knife",0)],itp_type_thrown|itp_primary|itp_merchandise,itcf_throw_knife,
  76,weight(2.5)|accuracy(65)|spd_rtng(121)|shoot_speed(25)|thrust_damage(19,cut)|max_ammo(14)|weapon_length(0),imodbits_thrown,[]],
["darts","Darts",[("dart_b",0),("dart_b_bag",ixmesh_carry)],itp_type_thrown|itp_primary|itp_merchandise,itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn,
  155,weight(4)|accuracy(65)|spd_rtng(95)|shoot_speed(28)|thrust_damage(22,pierce)|max_ammo(7)|weapon_length(32),imodbits_thrown],
["shuriken","Shuriken",[("shuriken",0)],itp_type_thrown|itp_primary,itcf_throw_knife,
  250,weight(1)|accuracy(65)|spd_rtng(125)|shoot_speed(30)|thrust_damage(25,pierce)|max_ammo(10)|weapon_length(11),imodbits_thrown],

# Throwing axes
["throwing_axes","Throwing_Axes",[("throwing_axe",0)],itp_type_thrown|itp_primary|itp_next_item_as_melee|itp_merchandise,itcf_throw_axe,
  500,weight(5)|accuracy(65)|spd_rtng(98)|shoot_speed(18)|thrust_damage(45,cut)|max_ammo(5)|weapon_length(46),imodbits_thrown],
["throwing_axes_melee","Throwing_Axe",[("throwing_axe",0)],itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield,itc_scimitar,
  500,weight(1)|spd_rtng(98)|swing_damage(30,cut)|weapon_length(46),imodbits_thrown],

#
["bolas","Bolas", [("throwing_stone",0)], itp_type_thrown|itp_primary|itp_merchandise, itcf_throw_stone,
  100,weight(3)|accuracy(72)|spd_rtng(94)|shoot_speed(30)|thrust_damage(30,blunt)|max_ammo(5)|weapon_length(8),imodbit_large_bag ],

["throwing_chains","throwing_Chain",[("throwing_chain",0)],itp_type_thrown|itp_primary|itp_unique,itcf_throw_knife,
  250,weight(1)|accuracy(65)|spd_rtng(125)|shoot_speed(30)|thrust_damage(45,blunt)|max_ammo(20)|weapon_length(11),imodbits_thrown],
#

# Bows
["short_bow", "Short Bow", [("short_bow_new",0),("short_bow_new_carry",ixmesh_carry)], itp_primary|itp_type_bow|itp_two_handed|itp_next_item_as_melee|itp_merchandise, itcf_shoot_bow|itcf_carry_bow_back, 
  58 , weight(1)|difficulty(1)|spd_rtng(97) | shoot_speed(55) | thrust_damage(18 ,  pierce  ),imodbits_bow, [ranged_weapon_triggers]],
["short_bow_alt_mode", "Short Bow", [("short_bow_new",0),("short_bow_new_carry",ixmesh_carry)], itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,
  0,weight(1)|spd_rtng(97)|weapon_length(74)|swing_damage(18,blunt)|thrust_damage(18,blunt),imodbits_polearm], 

["recurve_bow", "Recurve Bow", [("nomad_bow_new",0),("nomad_bow_new_case",ixmesh_carry)], itp_primary|itp_type_bow|itp_two_handed|itp_next_item_as_melee|itp_merchandise, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
  164 , weight(1.25)|difficulty(2)|spd_rtng(94) | shoot_speed(56) | thrust_damage(20 ,  pierce),imodbits_bow, [ranged_weapon_triggers]],
["recurve_bow_alt_mode", "Recurve Bow", [("nomad_bow_new",0),("nomad_bow_new_case",ixmesh_carry)], itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,
  0,weight(1)|spd_rtng(94)|weapon_length(49)|swing_damage(20,blunt)|thrust_damage(20,blunt),imodbits_polearm],

["hunting_bow", "Hunting Bow", [("hunting_bow_new",0),("hunting_bow_new_carry",ixmesh_carry)], itp_primary|itp_type_bow|itp_two_handed|itp_next_item_as_melee|itp_merchandise, itcf_shoot_bow|itcf_carry_bow_back, 
  17 , weight(1)|difficulty(0)|spd_rtng(100) | shoot_speed(52) | thrust_damage(15 ,  pierce),imodbits_bow, [ranged_weapon_triggers]],
["hunting_bow_alt_mode", "Hunting Bow", [("hunting_bow_new",0),("hunting_bow_new_carry",ixmesh_carry)], itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,
  0,weight(1)|spd_rtng(100)|weapon_length(86)|swing_damage(15,blunt)|thrust_damage(15,blunt),imodbits_polearm],

["skirmisher_bow", "Skirmisher Bow", [("khergit_bow_new",0),("khergit_bow_new_case",ixmesh_carry)], itp_primary|itp_type_bow|itp_two_handed|itp_next_item_as_melee, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
  269 , weight(1.25)|difficulty(3)|spd_rtng(90) | shoot_speed(57) | thrust_damage(21 ,pierce),imodbits_bow,[ranged_weapon_triggers]],
["skirmisher_bow_alt_mode", "Skirmisher Bow", [("khergit_bow_new",0),("khergit_bow_new_case",ixmesh_carry)], itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,
  40,weight(1)|spd_rtng(90)|weapon_length(57)|swing_damage(21,blunt)|thrust_damage(21,blunt),imodbits_polearm],

["rider_bow", "Rider Bow", [("strong_bow_new",0),("strong_bow_new_case",ixmesh_carry)], itp_primary|itp_type_bow|itp_two_handed|itp_next_item_as_melee, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
  437 , weight(1.25)|difficulty(3)|spd_rtng(88) | shoot_speed(58) | thrust_damage(23 ,pierce),imodbits_bow, [ranged_weapon_triggers]],
["rider_bow_alt_mode", "Rider Bow", [("strong_bow_new",0),("strong_bow_new_case",ixmesh_carry)], itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,
  40,weight(1)|spd_rtng(88)|weapon_length(55)|swing_damage(23,blunt)|thrust_damage(23,blunt),imodbits_polearm],

["reflex_bow", "Reflex Bow", [("war_bow_new",0),("war_bow_new_carry",ixmesh_carry)], itp_primary|itp_type_bow|itp_two_handed|itp_next_item_as_melee, itcf_shoot_bow|itcf_carry_bow_back, 
  728 , weight(1.5)|difficulty(4)|spd_rtng(84) | shoot_speed(59) | thrust_damage(25 ,pierce),imodbits_bow,[ranged_weapon_triggers]],
["reflex_bow_alt_mode", "Reflex Bow alt mode", [("war_bow_new",0),("war_bow_new_carry",ixmesh_carry)], itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,
  40,weight(1)|spd_rtng(84)|weapon_length(94)|swing_damage(25,blunt)|thrust_damage(25,blunt),imodbits_polearm],

["long_bow", "Long Bow", [("long_bow_new",0),("long_bow_new_carry",ixmesh_carry)], itp_primary|itp_type_bow|itp_two_handed|itp_next_item_as_melee, itcf_shoot_bow|itcf_carry_bow_back, 
  145 , weight(1.75)|difficulty(3)|spd_rtng(79) | shoot_speed(56) | thrust_damage(22 ,  pierce),imodbits_bow, [ranged_weapon_triggers]],
["long_bow_alt_mode", "Long Bow alt mode", [("long_bow_new",0),("long_bow_new_carry",ixmesh_carry)], itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,
  40,weight(1)|spd_rtng(79)|weapon_length(95)|swing_damage(22,blunt)|thrust_damage(22,blunt),imodbits_polearm],

["ossi_bow", "Os-si_Bow", [("ossi_bow",0),("ossi_bow_carry",ixmesh_carry)], itp_primary|itp_type_bow|itp_two_handed|itp_next_item_as_melee|itp_unique, itcf_shoot_bow|itcf_carry_bow_back, 
  10000 , weight(1.5)|difficulty(4)|spd_rtng(105) | shoot_speed(100) | thrust_damage(45 ,pierce),imodbits_bow, [ranged_weapon_triggers]],
["ossi_bow_alt", "Os-si_Bow_alt", [("ossi_bow",0),("ossi_bow_carry",ixmesh_carry)], itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,
  40,weight(1)|spd_rtng(84)|weapon_length(94)|swing_damage(33,blunt)|thrust_damage(33,blunt),imodbits_polearm],

# Others
["spanner","Combination Wrench", [("spanner",0)], itp_type_thrown|itp_primary|itp_next_item_as_melee, itcf_throw_knife,
  76 , weight(1)|accuracy(65)|spd_rtng(121) | shoot_speed(25) | thrust_damage(19 ,  blunt)|max_ammo(14)|weapon_length(30),imodbit_large_bag ],
["spanner_alt","Combination Wrench", [("spanner_melee",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_scimitar,
  76, weight(1)|spd_rtng(121) | weapon_length(30)|swing_damage(19 , blunt),imodbits_none ],

# Dynamite
["dynamite","Dynamite", [("dynamite", 0)], itp_type_one_handed_wpn|itp_secondary|itp_no_pick_up_from_ground|itp_unique, itcf_carry_axe_left_hip|itc_cleaver,
  27, weight(3)|spd_rtng(99)|weapon_length(30)|thrust_damage(0, pierce)|swing_damage(10, blunt), imodbits_none, [
  (ti_on_weapon_attack, [
      (store_trigger_param_1,":agent"),
      (call_script,"script_create_explosion", pos1,":agent", 1000, 50, 75, 1),
    ]),]],

##dynamite marks the end of ranged_weapons in header_items and module_constants, must always exist and be last - krag

##WARNING - to avoid compiling problems add new guns BEFORE the buffer guns section above. Don't add more than 10 new guns before compiling a couple of times - krag
	  
##************************************************************************************************
## ARENA
##************************************************************************************************
# ["arena_shield_red","Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
# ["arena_shield_blue","Shield", [("arena_shield_blue",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
# ["arena_shield_green","Shield", [("arena_shield_green",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
# ["arena_shield_yellow","Shield", [("arena_shield_yellow",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_tunic_white","Arena Tunic White", [("shirtb",0)], itp_type_body_armor |itp_covers_legs ,0, 47 , weight(2)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_red","Arena Tunic Red", [("shirtc",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_blue","Arena Tunic Blue", [("shirtd",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_green","Arena Tunic Green", [("shirte",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_yellow","Arena Tunic Yellow", [("armor_8",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|body_armor(16)|leg_armor(6), imodbits_cloth ],

##************************************************************************************************
## BOOKS
##************************************************************************************************
#This book must be at the beginning of readable books
["book_tactics","Tactics", [("new_book",0)], itp_type_book|itp_merchandise, 0, 4000,weight(2),imodbits_none],
["book_persuasion","Persuasion", [("new_book2",0)], itp_type_book|itp_merchandise, 0, 5000,weight(2),imodbits_none],
["book_leadership","Leadership", [("new_book3",0)], itp_type_book|itp_merchandise, 0, 4200,weight(2),imodbits_none],
["book_intelligence","Also sprach Zarathustra: Ein Buch fur Alle und Keinen", [("new_book4",0)], itp_type_book|itp_merchandise, 0, 2900,weight(2),imodbits_none],
["book_trade","Trade", [("new_book5",0)], itp_type_book|itp_merchandise, 0, 3100,weight(2),imodbits_none],
["book_weapon_mastery","Weapon Master", [("book_open",0)], itp_type_book|itp_merchandise, 0, 4200,weight(2),imodbits_none],
["book_engineering","Engineer", [("new_book",0)], itp_type_book|itp_merchandise, 0, 4000,weight(2),imodbits_none],
["book_prisoner_management","Prison Management", [("new_book2",0)], itp_type_book|itp_merchandise, 0, 4000,weight(2),imodbits_none],
["book_first_aid","First Aid", [("new_book3",0)], itp_type_book|itp_merchandise, 0, 4000,weight(2),imodbits_none],
["book_inventory_management","Inventory Management", [("new_book4",0)], itp_type_book|itp_merchandise, 0, 4000,weight(2),imodbits_none],
["book_tracking","Tracking", [("new_book5",0)], itp_type_book|itp_merchandise, 0, 4000,weight(2),imodbits_none],
["book_spotting","Spotting", [("book_open",0)], itp_type_book|itp_merchandise, 0, 4000,weight(2),imodbits_none],
["book_pathfinding","Pathfinding", [("new_book",0)], itp_type_book|itp_merchandise, 0, 4000,weight(2),imodbits_none],
["book_looting","Looting", [("new_book2",0)], itp_type_book|itp_merchandise, 0, 4000,weight(2),imodbits_none],
["book_athletics","Athletics", [("new_book3",0)], itp_type_book|itp_merchandise, 0, 4000,weight(2),imodbits_none],
["book_shield","Prowess", [("new_book4",0)], itp_type_book|itp_merchandise, 0, 4000,weight(2),imodbits_none],
["book_power_strike","Power Strike", [("book_open",0)], itp_type_book|itp_merchandise, 0, 4000,weight(2),imodbits_none],
["book_ironflesh","Ironflesh", [("new_book",0)], itp_type_book|itp_merchandise, 0, 4000,weight(2),imodbits_none],
#Reference books
#This book must be at the beginning of reference books
["book_wound_treatment_reference","Wound Treatment", [("book_open",0)], itp_type_book|itp_merchandise, 0, 3500,weight(2),imodbits_none],
["book_training_reference","Trainer", [("book_open",0)], itp_type_book|itp_merchandise, 0, 3500,weight(2),imodbits_none],
["book_surgery_reference","Surgery", [("book_open",0)], itp_type_book|itp_merchandise, 0, 3500,weight(2),imodbits_none],
["book_trade_ledger","Merchant's Ledger", [("book_open",0)], itp_type_book|itp_merchandise, 0, 500,weight(2),imodbits_none],

##************************************************************************************************
## TRADE
##************************************************************************************************
#other trade goods (first one is spice)
["salt","Salt", [("salt_crate",0)], itp_type_goods|itp_merchandise, 0,
255,weight(50),imodbits_none],

["raw_flax","Hemp", [("raw_flax",0)], itp_type_goods|itp_merchandise, 0,
150,weight(40)|abundance(75),imodbits_none],
["linen","Linen", [("linen",0)], itp_type_goods|itp_merchandise, 0,
250,weight(40)|abundance(50),imodbits_none],

["wool","Wool", [("wool_crate",0)], itp_type_goods|itp_merchandise, 0,
130,weight(40)|abundance(50)|food_quality(50),imodbits_none],
["wool_cloth","Wool Cloth", [("wool_cloth",0)], itp_type_goods|itp_merchandise, 0,
250,weight(40)|abundance(50)|food_quality(200),imodbits_none],

["iron","Iron", [("iron",0)], itp_type_goods|itp_merchandise, 0,
264,weight(60)|abundance(75)|food_quality(100),imodbits_none],
["tools","Tools", [("toolset",0)], itp_type_goods|itp_merchandise, 0,
410,weight(50)|food_quality(200),imodbits_none],

["raw_leather","Hides", [("leatherwork_inventory",0)], itp_type_goods|itp_merchandise, 0,
120,weight(40)|abundance(50)|food_quality(50),imodbits_none],

["furs","Furs", [("fur_pack",0)], itp_type_goods|itp_merchandise, 0,
391,weight(40)|abundance(50)|food_quality(50),imodbits_none],

["grain","Grain", [("grain_crate", 0)], itp_type_goods|itp_merchandise, 0,
50, weight(30)|abundance(75)|food_quality(50), imodbits_none, []],
###############
##Brytenwalda##
###############
["spice","Spice", [("spice_sack",0)], itp_type_goods|itp_merchandise, 0, 780,weight(40)|abundance(10),imodbits_none,[],],

["oil","Oil", [("olive_oil",0)], itp_type_goods|itp_merchandise, 0, 650,weight(50)|abundance(10),imodbits_none,[],],

["pottery","Pottery", [("jug",0)], itp_type_goods|itp_merchandise, 0, 200,weight(50)|abundance(90),imodbits_none,[],],

["raw_silk","Textile", [("raw_silk_bundle",0)], itp_type_goods|itp_merchandise, 0, 1000,weight(30)|abundance(10),imodbits_none,[],],
["raw_dyes","Dyes", [("dyes",0)], itp_type_goods|itp_merchandise, 0, 400,weight(10)|abundance(50),imodbits_none,[],],
["velvet","Fine Cloth", [("velvet",0)], itp_type_goods|itp_merchandise, 0, 425,weight(40)|abundance(30),imodbits_none,[],],

["stone","Stone", [("iron_bar",0)], itp_type_goods|itp_merchandise, 0,104,weight(60)|abundance(10),imodbits_none,[],],

["leatherwork","Leatherwork", [("leatherwork_frame",0)], itp_type_goods|itp_merchandise, 0, 400,weight(40)|abundance(90),imodbits_none,[],],

["iron_ore","Iron_Ore", [("ore_iron",0)], itp_type_goods|itp_merchandise, 0, 320,weight(60)|abundance(10),imodbits_none,[],],
["silver_ore","Silver_Ore", [("ore_silver",0)], itp_type_goods|itp_merchandise, 0, 320,weight(60)|abundance(10),imodbits_none,[],],
["gold_ore","Gold_Ore", [("ore_gold",0)], itp_type_goods|itp_merchandise, 0, 320,weight(60)|abundance(10),imodbits_none,[],],

["mead","Mead", [("ale_barrel",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0, 310,weight(30)|abundance(10)|food_quality(30)|max_ammo(5),imodbits_none,[],],

["apples","Fruit", [("apple_basket",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0, 40,weight(20)|abundance(110)|food_quality(40)|max_ammo(5),imodbits_none],
["raw_grapes","Grapes", [("grapes_inventory",0)], itp_consumable|itp_type_goods|itp_merchandise, 0, 75,weight(40)|abundance(60)|food_quality(10)|max_ammo(3),imodbits_none], #x2 for wine
["raw_olives","Olives", [("olive_inventory",0)], itp_consumable|itp_type_goods|itp_merchandise, 0, 150,weight(40)|abundance(60)|food_quality(10)|max_ammo(3),imodbits_none], #x3 for oil

["chicken","Chicken", [("chicken",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0, 65,weight(10)|abundance(110)|food_quality(40)|max_ammo(5),imodbits_none],
["pork","Pork", [("pork",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0, 89,weight(15)|abundance(100)|food_quality(70)|max_ammo(5),imodbits_none],

######################################################################

##########
##HORSES##
##########
["sumpter_horse","Sumpter Horse", [("sumpter_horse",0)], itp_type_horse, 0,
134,abundance(50)|hit_points(100)|body_armor(14)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100),imodbits_horse_basic],
["saddle_horse","Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0,
240,abundance(50)|hit_points(100)|body_armor(8)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104),imodbits_horse_basic],
["steppe_horse","Steppe Horse", [("steppe_horse",0)], itp_type_horse, 0,
192,abundance(50)|hit_points(120)|body_armor(10)|horse_speed(40)|horse_maneuver(51)|horse_charge(8)|horse_scale(98),imodbits_horse_basic, [], []],
["courser","Courser", [("courser",0)], itp_type_horse, 0,
600,abundance(50)|body_armor(12)|hit_points(110)|horse_speed(50)|horse_maneuver(44)|horse_charge(12)|horse_scale(106),imodbits_horse_good|imodbit_champion],
["hunter","Hunter", [("hunting_horse",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0,
810,abundance(50)|hit_points(160)|body_armor(18)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108),imodbits_horse_good|imodbit_champion],

################
##Barbed Wire###
################
##Entenaii Empire
["entenaii_horse_1","Imperial_Horse", [("entenaii_horse_1",0)], itp_type_horse|itp_merchandise, 0, 
  350,abundance(50)|hit_points(70)|body_armor(10)|difficulty(1)|horse_speed(39)|horse_maneuver(40)|horse_charge(6)|horse_scale(91),imodbits_horse_basic],
["entenaii_horse_2","Imperial_Horse", [("entenaii_horse_2",0)], itp_type_horse|itp_merchandise, 0, 
  400,abundance(40)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(40)|horse_maneuver(41)|horse_charge(7)|horse_scale(91),imodbits_horse_basic],
["entenaii_horse_3","Imperial_Horse", [("entenaii_horse_3",0)], itp_type_horse|itp_merchandise, 0, 
  700,abundance(30)|hit_points(75)|body_armor(12)|difficulty(2)|horse_speed(42)|horse_maneuver(44)|horse_charge(8)|horse_scale(91),imodbits_horse_basic],
["entenaii_horse_4","Imperial_Horse", [("entenaii_horse_4",0)], itp_type_horse|itp_merchandise, 0, 
  1000,abundance(20)|hit_points(82)|body_armor(13)|difficulty(3)|horse_speed(43)|horse_maneuver(45)|horse_charge(9)|horse_scale(91),imodbits_horse_basic],
["entenaii_horse_5","Imperial_Horse", [("entenaii_horse_5",0)], itp_type_horse|itp_merchandise, 0, 
  1700,abundance(10)|hit_points(99)|body_armor(15)|difficulty(4)|horse_speed(47)|horse_maneuver(46)|horse_charge(16)|horse_scale(91),imodbits_horse_basic],

["entenaii_horse_1_gas","Imperial_Horse", [("entenaii_horse_1_gas",0)], itp_type_horse|itp_merchandise, 0, 
  350,abundance(50)|hit_points(70)|body_armor(10)|difficulty(1)|horse_speed(39)|horse_maneuver(40)|horse_charge(6)|horse_scale(91),imodbits_horse_basic],
["entenaii_horse_2_gas","Imperial_Horse", [("entenaii_horse_2_gas",0)], itp_type_horse|itp_merchandise, 0, 
  400,abundance(40)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(40)|horse_maneuver(41)|horse_charge(7)|horse_scale(91),imodbits_horse_basic],
["entenaii_horse_3_gas","Imperial_Horse", [("entenaii_horse_3_gas",0)], itp_type_horse|itp_merchandise, 0, 
  700,abundance(30)|hit_points(75)|body_armor(12)|difficulty(2)|horse_speed(42)|horse_maneuver(44)|horse_charge(8)|horse_scale(91),imodbits_horse_basic],
["entenaii_horse_4_gas","Imperial_Horse", [("entenaii_horse_4_gas",0)], itp_type_horse|itp_merchandise, 0, 
  1000,abundance(20)|hit_points(82)|body_armor(13)|difficulty(3)|horse_speed(43)|horse_maneuver(45)|horse_charge(9)|horse_scale(91),imodbits_horse_basic],
["entenaii_horse_5_gas","Imperial_Horse", [("entenaii_horse_5_gas",0)], itp_type_horse|itp_merchandise, 0, 
  1700,abundance(10)|hit_points(99)|body_armor(15)|difficulty(4)|horse_speed(47)|horse_maneuver(46)|horse_charge(16)|horse_scale(91),imodbits_horse_basic],

##Entenaii Dominion

##Kingdom of Galvae
["galvae_horse_1","Fancra", [("galvae_horse_1",0)], itp_type_horse|itp_merchandise, 0, 
  1200,abundance(40)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(44)|horse_maneuver(40)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["galvae_horse_2","Fancra", [("galvae_horse_2",0)], itp_type_horse|itp_merchandise, 0, 
  1300,abundance(40)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(40)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],

["galvae_horse_1_gas","Fancra", [("galvae_horse_1_gas",0)], itp_type_horse|itp_merchandise, 0, 
  1200,abundance(40)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(44)|horse_maneuver(40)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["galvae_horse_2_gas","Fancra", [("galvae_horse_2_gas",0)], itp_type_horse|itp_merchandise, 0, 
  1300,abundance(40)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(40)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],

##Molvat-Berchav Union
["pony","Pony", [("rus_horse",0)], itp_type_horse|itp_merchandise, 0, 
  800,abundance(50)|hit_points(60)|body_armor(5)|difficulty(1)|horse_speed(37)|horse_maneuver(36)|horse_charge(9)|horse_scale(86),imodbits_horse_basic],
["culsar_horse_1","Karachay", [("hussar_horse",0)], itp_type_horse|itp_merchandise, 0,
  1800,abundance(30)|hit_points(150)|body_armor(12)|difficulty(2)|horse_speed(50)|horse_maneuver(48)|horse_charge(20)|horse_scale(108),imodbits_horse_good|imodbit_champion],
["culsar_horse_2","Karachay", [("hussar_horse_2",0)], itp_type_horse|itp_merchandise, 0,
  2000,abundance(15)|hit_points(200)|body_armor(15)|difficulty(3)|horse_speed(52)|horse_maneuver(53)|horse_charge(25)|horse_scale(108),imodbits_horse_good|imodbit_champion],
["culsar_horse_3","Karachay", [("hussar_horse_3",0)], itp_type_horse, 0,
  2200,abundance(5)|hit_points(300)|body_armor(18)|difficulty(4)|horse_speed(55)|horse_maneuver(55)|horse_charge(30)|horse_scale(108),imodbits_horse_good|imodbit_champion],
["ravga_horse","Ravga Steed", [("barf_skeletal_horse",0)], itp_type_horse, 0, 
  3300,body_armor(35)|hit_points(450)|difficulty(3)|horse_speed(37)|horse_maneuver(33)|horse_charge(19)|horse_scale(100),imodbits_horse_good|imodbit_champion],

##Vitzland Territories
["vitzland_horse_1","Rottaler", [("vitzland_horse_1",0)], itp_type_horse|itp_merchandise, 0, 
  1000,abundance(50)|hit_points(100)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(12)|horse_scale(91),imodbits_horse_basic|imodbit_champion],
["vitzland_horse_2","Rottaler", [("vitzland_horse_2",0)], itp_type_horse|itp_merchandise, 0, 
  1120,abundance(20)|hit_points(110)|body_armor(11)|difficulty(1)|horse_speed(44)|horse_maneuver(45)|horse_charge(15)|horse_scale(91),imodbits_horse_basic|imodbit_champion],
["vitzland_horse_3","Rottaler", [("vitzland_horse_3",0)], itp_type_horse|itp_merchandise, 0, 
  1500,abundance(10)|hit_points(145)|body_armor(12)|difficulty(2)|horse_speed(47)|horse_maneuver(47)|horse_charge(18)|horse_scale(90),imodbits_horse_basic|imodbit_champion],

["vitzland_horse_1_gas","Rottaler", [("vitzland_horse_1_gas",0)], itp_type_horse|itp_merchandise, 0, 
  1000,abundance(50)|hit_points(100)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(12)|horse_scale(91),imodbits_horse_basic|imodbit_champion],
["vitzland_horse_2_gas","Rottaler", [("vitzland_horse_2_gas",0)], itp_type_horse|itp_merchandise, 0, 
  1120,abundance(20)|hit_points(110)|body_armor(11)|difficulty(1)|horse_speed(44)|horse_maneuver(45)|horse_charge(15)|horse_scale(91),imodbits_horse_basic|imodbit_champion],
["vitzland_horse_3_gas","Rottaler", [("vitzland_horse_3_gas",0)], itp_type_horse|itp_merchandise, 0, 
  1500,abundance(10)|hit_points(145)|body_armor(12)|difficulty(2)|horse_speed(47)|horse_maneuver(47)|horse_charge(18)|horse_scale(90),imodbits_horse_basic|imodbit_champion],

##Trezzo Republic
["trezzo_horse_1","Hippika", [("trezzo_horse_1",0)], itp_type_horse|itp_merchandise, 0, 
  1000,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["trezzo_horse_2","Hippika", [("trezzo_horse_2",0)], itp_type_horse|itp_merchandise, 0, 
  1000,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(10)|horse_scale(90),imodbits_horse_basic],
["trezzo_horse_3","Hippika", [("trezzo_horse_3",0)], itp_type_horse|itp_merchandise, 0, 
  1000,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["trezzo_horse_4","Hippika", [("trezzo_horse_4",0)], itp_type_horse|itp_merchandise, 0, 
  1000,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],

["trezzo_horse_1_gas","Hippika", [("trezzo_horse_1_gas",0)], itp_type_horse|itp_merchandise, 0, 
  1000,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["trezzo_horse_2_gas","Hippika", [("trezzo_horse_2_gas",0)], itp_type_horse|itp_merchandise, 0, 
  1000,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(10)|horse_scale(90),imodbits_horse_basic],
["trezzo_horse_3_gas","Hippika", [("trezzo_horse_3_gas",0)], itp_type_horse|itp_merchandise, 0, 
  1000,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["trezzo_horse_4_gas","Hippika", [("trezzo_horse_4_gas",0)], itp_type_horse|itp_merchandise, 0, 
  1000,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],

["vencudi_steed_1","Vencudi_Cryonno ", [("vencudi_steed_1",0)], itp_type_horse, 0, 
  3000,abundance(30)|hit_points(113)|body_armor(20)|difficulty(3)|horse_speed(45)|horse_maneuver(42)|horse_charge(20)|horse_scale(90),imodbits_horse_good|imodbit_champion],
["vencudi_steed_2","Vencudi_Cryonno", [("vencudi_steed_2",0)], itp_type_horse, 0, 
  3500,abundance(30)|hit_points(151)|body_armor(23)|difficulty(3)|horse_speed(46)|horse_maneuver(43)|horse_charge(22)|horse_scale(91),imodbits_horse_good|imodbit_champion],
["vencudi_steed_3","Vencudi_Cryonno", [("vencudi_steed_3",0)], itp_type_horse, 0, 
  4000,abundance(30)|hit_points(178)|body_armor(27)|difficulty(4)|horse_speed(47)|horse_maneuver(44)|horse_charge(24)|horse_scale(91),imodbits_horse_good|imodbit_champion],

##Itami Castedom
["itami_horse_1","Itami Horse", [("foreign_horse_1",0)], itp_type_horse|itp_merchandise, 0, 
  600,abundance(10)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(40)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["itami_horse_2","Itami Horse", [("foreign_horse_2",0)], itp_type_horse|itp_merchandise, 0, 
  700,abundance(10)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(40)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],

## Bashide Confederacy ##
["bashide_horse_1","Bashide Horse", [("horse_tyrk_a",0)], itp_type_horse|itp_merchandise, 0, 
  600,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(40)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["bashide_horse_2","Bashide Horse", [("horse_tyrk_b",0)], itp_type_horse|itp_merchandise, 0, 
  600,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(40)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["bashide_horse_3","Bashide Horse", [("horse_tyrk_c",0)], itp_type_horse|itp_merchandise, 0, 
  600,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(40)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["bashide_horse_4","Bashide Horse", [("horse_tyrk_d",0)], itp_type_horse|itp_merchandise, 0, 
  600,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(40)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["bashide_horse_5","Bashide Horse", [("horse_tyrk_e",0)], itp_type_horse|itp_merchandise, 0, 
  600,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(40)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],

["camel_1", "Camel", [("camel",0)], itp_type_horse|itp_merchandise, 0, 
  1310, abundance(20)|hit_points(200)|body_armor(10)|difficulty(3)|horse_speed(47)|horse_maneuver(43)|horse_charge(25)|horse_scale(108), imodbits_horse_good|imodbit_champion],
["camel_2", "Camel", [("camel2",0)], itp_type_horse|itp_merchandise, 0, 
  1810, abundance(15)|hit_points(225)|body_armor(15)|difficulty(3)|horse_speed(48)|horse_maneuver(45)|horse_charge(28)|horse_scale(108), imodbits_horse_good|imodbit_champion],
["camel_3", "Camel", [("camel3",0)], itp_type_horse, 0, 
  3500, abundance(5)|hit_points(275)|body_armor(20)|difficulty(3)|horse_speed(49)|horse_maneuver(46)|horse_charge(32)|horse_scale(108), imodbits_horse_good|imodbit_champion],


##irregular

#throd
["ghoul_horse","Throd_Horse", [("ghoul_horse",0)], itp_type_horse, 0, 
  3300,body_armor(35)|hit_points(450)|difficulty(3)|horse_speed(37)|horse_maneuver(33)|horse_charge(19)|horse_scale(100),imodbits_horse_good|imodbit_champion],
["ghoul_horse_2","Throd_Horse", [("ghoul_horse_2",0)], itp_type_horse, 0, 
  3000,body_armor(33)|hit_points(440)|difficulty(3)|horse_speed(35)|horse_maneuver(35)|horse_charge(20)|horse_scale(100),imodbits_horse_good|imodbit_champion],

#other
["pack_horse","Pack Horse", [("pack_horse",0)], itp_type_horse|itp_merchandise, 0, 
  400,abundance(20)|body_armor(5)|hit_points(90)|difficulty(1)|horse_speed(32)|horse_maneuver(31)|horse_charge(2)|horse_scale(94),imodbits_horse_basic],
["donkey_1","Donkey", [("donkey_mount",0)], itp_type_horse|itp_merchandise, 0, 
  800,abundance(80)|hit_points(55)|body_armor(7)|difficulty(0)|horse_speed(32)|horse_maneuver(33)|horse_charge(8)|horse_scale(79),imodbits_horse_basic],
["donkey_2","Donkey", [("donkey_mount2",0)], itp_type_horse|itp_merchandise, 0, 
  800,abundance(80)|hit_points(55)|body_armor(7)|difficulty(0)|horse_speed(32)|horse_maneuver(33)|horse_charge(8)|horse_scale(79),imodbits_horse_basic],
["mule","Mule", [("mule",0)], itp_type_horse|itp_merchandise, 0, 
  1050,abundance(70)|hit_points(65)|body_armor(10)|difficulty(0)|horse_speed(35)|horse_maneuver(35)|horse_charge(8)|horse_scale(86),imodbits_horse_basic],

["invisi_horse","Invisible Horse", [("empty",0)], itp_type_horse|itp_unique, 0,
1,body_armor(0)|hit_points(1)|horse_speed(50)|horse_maneuver(44)|horse_charge(0)|horse_scale(106),imodbits_none],

#cannibal
["canibal_horse_1","Flesh_Barded_Steed", [("canibal_horse_short",0)], itp_type_horse, 0, 
  1000,abundance(50)|hit_points(100)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(12)|horse_scale(91),imodbits_horse_basic|imodbit_champion],
["canibal_horse_2","Flesh_Barded_Steed", [("canibal_horse_long",0)], itp_type_horse, 0, 
  1120,abundance(20)|hit_points(110)|body_armor(11)|difficulty(1)|horse_speed(44)|horse_maneuver(45)|horse_charge(15)|horse_scale(91),imodbits_horse_basic|imodbit_champion],
["canibal_horse_3","Flesh_Barded_Steed", [("canibal_horse_demon",0)], itp_type_horse, 0, 
  1500,abundance(10)|hit_points(145)|body_armor(12)|difficulty(2)|horse_speed(47)|horse_maneuver(47)|horse_charge(18)|horse_scale(90),imodbits_horse_basic|imodbit_champion],

#

##Armoured##
["trench_steed_1","Trench_Steed", [("trench_steed_1",0)], itp_type_horse|itp_merchandise, 0, 
  5200,abundance(5)|body_armor(35)|hit_points(150)|difficulty(3)|horse_speed(36)|horse_maneuver(34)|horse_charge(25)|horse_scale(99),imodbits_horse_basic],
["trench_steed_2","Trench_Steed", [("trench_steed_2",0)], itp_type_horse|itp_merchandise, 0, 
  9200,abundance(5)|body_armor(65)|hit_points(350)|difficulty(3)|horse_speed(35)|horse_maneuver(33)|horse_charge(32)|horse_scale(99),imodbits_horse_basic],

["raider_horse_armoured_1","Armoured_Raider_Horse", [("raider_horse_armoured_1",0)], itp_type_horse|itp_merchandise, 0, 
  4200,abundance(5)|body_armor(30)|hit_points(130)|difficulty(4)|horse_speed(32)|horse_maneuver(31)|horse_charge(22)|horse_scale(99),imodbits_horse_basic],


#Other
["swift_horse_1","Swift_Horse", [("swift_horse_1",0)], itp_type_horse|itp_merchandise, 0, 1200,abundance(45)|body_armor(12)|hit_points(90)|difficulty(2)|horse_speed(43)|horse_maneuver(40)|horse_charge(13)|horse_scale(94),imodbits_horse_basic],
["swift_horse_2","Swift_Horse", [("swift_horse_2",0)], itp_type_horse|itp_merchandise, 0, 1200,abundance(45)|body_armor(12)|hit_points(90)|difficulty(2)|horse_speed(44)|horse_maneuver(40)|horse_charge(13)|horse_scale(94),imodbits_horse_basic],
["swift_horse_3","Swift_Horse", [("swift_horse_3",0)], itp_type_horse|itp_merchandise, 0, 1200,abundance(45)|body_armor(12)|hit_points(90)|difficulty(2)|horse_speed(43)|horse_maneuver(40)|horse_charge(13)|horse_scale(94),imodbits_horse_basic],
["swift_horse_4","Swift_Horse", [("swift_horse_4",0)], itp_type_horse|itp_merchandise, 0, 1200,abundance(45)|body_armor(12)|hit_points(90)|difficulty(2)|horse_speed(46)|horse_maneuver(40)|horse_charge(13)|horse_scale(93),imodbits_horse_basic],
["swift_horse_5","Swift_Horse", [("swift_horse_5",0)], itp_type_horse|itp_merchandise, 0, 1200,abundance(45)|body_armor(12)|hit_points(90)|difficulty(2)|horse_speed(43)|horse_maneuver(40)|horse_charge(13)|horse_scale(94),imodbits_horse_basic],
["swift_horse_6","Swift_Horse", [("swift_horse_6",0)], itp_type_horse|itp_merchandise, 0, 1200,abundance(45)|body_armor(12)|hit_points(90)|difficulty(2)|horse_speed(42)|horse_maneuver(40)|horse_charge(13)|horse_scale(94),imodbits_horse_basic],

["tundra_horse_1","Tundra_Horse", [("tundra_horse_1",0)], itp_type_horse|itp_merchandise, 0, 1000,abundance(20)|body_armor(16)|hit_points(90)|difficulty(2)|horse_speed(36)|horse_maneuver(50)|horse_charge(17)|horse_scale(94),imodbits_horse_basic],

["plains_horse_1","Plains_Horse", [("plains_horse_1",0)], itp_type_horse|itp_merchandise, 0, 1000,abundance(50)|body_armor(15)|hit_points(100)|difficulty(1)|horse_speed(38)|horse_maneuver(38)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["plains_horse_2","Plains_Horse", [("plains_horse_2",0)], itp_type_horse|itp_merchandise, 0, 1000,abundance(50)|body_armor(15)|hit_points(100)|difficulty(1)|horse_speed(38)|horse_maneuver(38)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["plains_horse_3","Plains_Horse", [("plains_horse_3",0)], itp_type_horse|itp_merchandise, 0, 1000,abundance(50)|body_armor(15)|hit_points(100)|difficulty(1)|horse_speed(38)|horse_maneuver(38)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["plains_horse_4","Plains_Horse", [("plains_horse_4",0)], itp_type_horse|itp_merchandise, 0, 1000,abundance(50)|body_armor(15)|hit_points(100)|difficulty(1)|horse_speed(38)|horse_maneuver(38)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["plains_horse_5","Plains_Horse", [("plains_horse_5",0)], itp_type_horse|itp_merchandise, 0, 1000,abundance(50)|body_armor(15)|hit_points(100)|difficulty(1)|horse_speed(38)|horse_maneuver(38)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],

["mountain_horse_1","Mountain_Horse", [("mountain_horse_1",0)], itp_type_horse|itp_merchandise, 0, 1100,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["mountain_horse_2","Mountain_Horse", [("mountain_horse_2",0)], itp_type_horse|itp_merchandise, 0, 1100,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(10)|horse_scale(90),imodbits_horse_basic],
["mountain_horse_3","Mountain_Horse", [("mountain_horse_3",0)], itp_type_horse|itp_merchandise, 0, 1100,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["mountain_horse_4","Mountain_Horse", [("mountain_horse_4",0)], itp_type_horse|itp_merchandise, 0, 1100,abundance(30)|body_armor(16)|hit_points(90)|difficulty(2)|horse_speed(36)|horse_maneuver(35)|horse_charge(17)|horse_scale(94),imodbits_horse_basic],
["mountain_horse_5","Mountain_Horse", [("mountain_horse_5",0)], itp_type_horse|itp_merchandise, 0, 1100,abundance(30)|body_armor(16)|hit_points(90)|difficulty(2)|horse_speed(36)|horse_maneuver(35)|horse_charge(17)|horse_scale(94),imodbits_horse_basic],
["mountain_horse_6","Mountain_Horse", [("mountain_horse_6",0)], itp_type_horse|itp_merchandise, 0, 1100,abundance(30)|body_armor(16)|hit_points(90)|difficulty(2)|horse_speed(36)|horse_maneuver(35)|horse_charge(17)|horse_scale(94),imodbits_horse_basic],
["mountain_horse_7","Mountain_Horse", [("mountain_horse_7",0)], itp_type_horse|itp_merchandise, 0, 1100,abundance(30)|body_armor(16)|hit_points(90)|difficulty(2)|horse_speed(36)|horse_maneuver(35)|horse_charge(17)|horse_scale(94),imodbits_horse_basic],
["mountain_horse_8","Mountain_Horse", [("mountain_horse_8",0)], itp_type_horse|itp_merchandise, 0, 1100,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(10)|horse_scale(90),imodbits_horse_basic],
["mountain_horse_9","Mountain_Horse", [("mountain_horse_9",0)], itp_type_horse|itp_merchandise, 0, 1100,abundance(30)|body_armor(16)|hit_points(90)|difficulty(2)|horse_speed(36)|horse_maneuver(35)|horse_charge(17)|horse_scale(94),imodbits_horse_basic],
["mountain_horse_10","Mountain_Horse", [("mountain_horse_10",0)], itp_type_horse|itp_merchandise, 0, 1100,abundance(30)|body_armor(16)|hit_points(90)|difficulty(2)|horse_speed(36)|horse_maneuver(35)|horse_charge(17)|horse_scale(94),imodbits_horse_basic],

#Courser
["palfrey_1","Palfrey", [("WSumpterChestnut",0)], itp_type_horse|itp_merchandise, 0, 2400,abundance(10)|hit_points(80)|body_armor(12)|difficulty(3)|horse_speed(46)|horse_maneuver(44)|horse_charge(12)|horse_scale(88),imodbits_horse_basic|imodbit_champion],
["palfrey_2","Palfrey", [("WSumpterBrown",0)], itp_type_horse|itp_merchandise, 0, 2400,abundance(10)|hit_points(85)|body_armor(12)|difficulty(3)|horse_speed(46)|horse_maneuver(44)|horse_charge(12)|horse_scale(88),imodbits_horse_basic|imodbit_champion],

["wild_horse_1","Wild_Horse", [("wild_horse_a",0)], itp_type_horse|itp_merchandise, 0, 1000,abundance(50)|body_armor(15)|hit_points(100)|difficulty(1)|horse_speed(38)|horse_maneuver(38)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["wild_horse_2","Wild_Horse", [("wild_horse_b",0)], itp_type_horse|itp_merchandise, 0, 1000,abundance(50)|body_armor(15)|hit_points(100)|difficulty(1)|horse_speed(38)|horse_maneuver(38)|horse_charge(10)|horse_scale(94),imodbits_horse_basic],
["wild_horse_3","Wild_Horse", [("wild_horse_c",0)], itp_type_horse|itp_merchandise, 0, 1000,abundance(50)|body_armor(15)|hit_points(100)|difficulty(1)|horse_speed(38)|horse_maneuver(38)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],

["foreign_horse_1","yanizar Horse", [("foreign_horse_1",0)], itp_type_horse|itp_merchandise, 0, 
  600,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(40)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
["foreign_horse_2","yanizar Horse", [("foreign_horse_2",0)], itp_type_horse|itp_merchandise, 0, 
  700,abundance(30)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(40)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],

############
##Vehicles##
############
["pickup_a","Civilian Car", [("map_pickup_a",0)], itp_type_goods|itp_merchandise, 0,
2500,weight(0)|abundance(25)|food_quality(500),imodbits_car],
["pickup_b","Civilian Car", [("map_pickup_b",0)], itp_type_goods|itp_merchandise, 0,
2500,weight(0)|abundance(25)|food_quality(500),imodbits_car],
["pickup_c","Civilian Car", [("map_pickup_c",0)], itp_type_goods|itp_merchandise, 0,
2500,weight(0)|abundance(25)|food_quality(500),imodbits_car],
["jeep_beige","Military Truck", [("map_jeep_beige",0)], itp_type_goods|itp_merchandise, 0,
3500,weight(0)|food_quality(500),imodbits_car],
["jeep_black","Military Truck", [("map_jeep_black",0)], itp_type_goods|itp_merchandise, 0,
3500,weight(0)|food_quality(500),imodbits_car],
["jeep_green","Military Truck", [("map_jeep_green",0)], itp_type_goods|itp_merchandise, 0,
3500,weight(0)|food_quality(500),imodbits_car],
["jeep_greenb","Military Truck", [("map_jeep_greenb",0)], itp_type_goods|itp_merchandise, 0,
3500,weight(0)|food_quality(500),imodbits_car],
["jeep_tan","Military Truck", [("map_jeep_tan",0)], itp_type_goods|itp_merchandise, 0,
3500,weight(0)|food_quality(500),imodbits_car],

#misc

["gasoline","Fuel_Cans", [("jerrycan_green",0)], itp_type_goods|itp_consumable|itp_merchandise, 0,
500,weight(50)|abundance(75)|max_ammo(250)|food_quality(100),imodbits_none],

["bandage","Bandage", [("bandage",0)], itp_type_goods|itp_consumable|itp_merchandise, 0,
100,weight(0.1)|max_ammo(5)|food_quality(100),imodbits_none],
["medkit","Med-Kit", [("boxmedic",0)], itp_type_goods|itp_consumable|itp_merchandise, 0,
500,weight(0.5)|abundance(50)|max_ammo(5)|food_quality(200),imodbits_none],
["medicine","Medicine", [("medi_combined",0)], itp_type_goods|itp_consumable|itp_merchandise, 0,
250,weight(0.1)|abundance(50)|max_ammo(5)|food_quality(200),imodbits_none],

["drug_1","Miracle Drug", [("syringe",0)], itp_type_goods|itp_consumable, 0,
500,weight(0.1)|max_ammo(1)|food_quality(0),imodbits_none],

["rad_mushrooms","Strange Mushrooms", [("mushroom_a",0)], itp_type_goods|itp_consumable, 0,
150,weight(0.1)|max_ammo(10)|food_quality(0),imodbits_none],
["moonshine","Moonshine", [("moonshine",0)], itp_type_goods|itp_consumable|itp_merchandise, 0,
350,weight(0.1)|max_ammo(5)|food_quality(0),imodbits_none],

["tech_parts","Hardware", [("tech_parts",0)], itp_type_goods, 0,
500,weight(1)|abundance(25)|food_quality(10),imodbits_none],	#removed merch flag as unused currently

["empty_bottles","Empty Bottles", [("empty_bottles",0)], itp_type_goods|itp_merchandise, 0,
25,weight(1)|abundance(75)|food_quality(0),imodbits_none],
["empty_oil_barrels","Empty Barrel", [("oil",0)], itp_type_goods|itp_merchandise, 0,
50,weight(5)|abundance(75)|food_quality(0),imodbits_none],

# ["generator","Generator", [("global_generator",0)], itp_type_goods, 0,
# 1000,weight(60)|abundance(25)|food_quality(300),imodbits_none],

["wood","Wood", [("prt_wood", 0)], itp_type_goods|itp_merchandise, 0,
250, weight(40)|food_quality(50), imodbits_none, []],
["metal","Metal", [("metal_obj", 0)], itp_type_goods, 0,
250, weight(40)|food_quality(50), imodbits_none, []],	#removed merch flag as unused currently
# ["nails","Nails", [("nails", 0)], itp_type_goods, 0,
# 30, weight(1)|abundance(50)|food_quality(50), imodbits_none, []],
# ["screws","Screws", [("screws", 0)], itp_type_goods, 0,
# 35, weight(1)|abundance(50)|food_quality(50), imodbits_none, []],
# ["tape","Tape", [("tape", 0)], itp_type_goods, 0,
# 25, weight(0.25)|abundance(50)|food_quality(50), imodbits_none, []],
["steel","Steel", [("steel",0)], itp_type_goods, 0,
528,weight(60)|abundance(25)|food_quality(50),imodbits_none],	#removed merch flag as unused currently

["miasma_ore","Miasma_Ore", [("ore3",0)], itp_type_goods, 0,
375,weight(60)|abundance(50)|food_quality(0),imodbits_none],	#removed merch flag as unused currently
["miasma_essence","Misama_Essence", [("miasma_essence",0)], itp_type_goods, 0,
700,weight(10)|abundance(25)|food_quality(0),imodbits_none],	#removed merch flag as unused currently
["aldrinium","Aldrinium", [("aldrinium",0)], itp_type_goods, 0,
1000,weight(10)|abundance(10)|food_quality(0),imodbits_none],	#removed merch flag as unused currently

["generic_weapon_blueprint","Weapon_Blueprint", [("blueprint_1",0)], itp_type_goods, 0,
500,weight(1)|abundance(5)|food_quality(50),imodbits_none],
["generic_armour_blueprint","Armour_Blueprint", [("blueprint_2",0)], itp_type_goods, 0,
500,weight(1)|abundance(5)|food_quality(50),imodbits_none],
["generic_helmet_blueprint","Helmet_Blueprint", [("blueprint_3",0)], itp_type_goods, 0,
500,weight(1)|abundance(5)|food_quality(50),imodbits_none],

["propane","Kerosene", [("propanetank_lod01",0)], itp_type_goods|itp_merchandise, 0,
500,weight(20)|abundance(50)|food_quality(100),imodbits_none],

["car_parts","Mechanical_parts", [("car_parts",0)], itp_type_goods, 0,
500,weight(20)|abundance(50)|food_quality(50),imodbits_none],

["tents","Tents", [("camp_tent",0)], itp_type_goods|itp_merchandise, 0,
250,weight(20)|abundance(75)|food_quality(500),imodbits_none],

["fishing","Fishing Equipment", [("fishing_a",0)], itp_type_goods|itp_merchandise, 0,
250,weight(2.5)|abundance(75)|food_quality(100),imodbits_none],

["shells","Shells", [("shells",0)], itp_type_goods|itp_merchandise, 0,
100,weight(50)|abundance(75)|food_quality(0),imodbits_none],

#reloading_items
#pistol
["pistol_ammo_empty","Spent_Pistol/SMG_Rounds", [("ammo_pistol_1_empty",0)], itp_type_goods, 0,
10,weight(0.1)|food_quality(0),imodbits_none],
["rifle_ammo_empty","Spent_Rifle_Rounds", [("ammo_rifle_1_empty",0)], itp_type_goods, 0,
20,weight(0.1)|food_quality(0),imodbits_none],
["large_caliber_ammo_empty","Spent_Large_Caliber_Rounds", [("ammo_large_4_empty",0)], itp_type_goods, 0,
50,weight(0.1)|food_quality(0),imodbits_none],
["shotgun_ammo_empty","Spent_Shotgun_Shell", [("shell_shotgun",0)], itp_type_goods, 0,
25,weight(0.1)|food_quality(0),imodbits_none],

#foods
["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
140,weight(1)|abundance(75)|food_quality(70)|max_ammo(12),imodbits_none],
["cheese","Cheese", [("cheese_b",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
240,weight(1)|abundance(25)|food_quality(80)|max_ammo(13),imodbits_none],
["sausages","Sausages", [("sausages",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
150,weight(1)|abundance(75)|food_quality(50)|max_ammo(13),imodbits_none],
["cabbages","Cabbages", [("cabbage",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
120,weight(1)|abundance(50)|food_quality(60)|max_ammo(12),imodbits_none],
["dried_meat","Dried Meat", [("smoked_meat",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
450,weight(1)|abundance(75)|food_quality(90)|max_ammo(15),imodbits_none],
["cattle_meat","Beef", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
300,weight(1)|abundance(75)|food_quality(100)|max_ammo(13),imodbits_none],
["jerky","Jerky", [("smoked_meat",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
80,weight(1)|abundance(75)|food_quality(80)|max_ammo(11),imodbits_none],
["bread","Bread", [("bread_a",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
140,weight(1)|abundance(75)|food_quality(70)|max_ammo(12),imodbits_none],
["rice","Rice", [("wheat_sack",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
300,weight(1)|abundance(75)|food_quality(60)|max_ammo(15),imodbits_none],
["honey","Honey", [("honey_barrel",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
400,weight(5)|abundance(10)|food_quality(40)|max_ammo(20),imodbits_none],

["canned_beans","Rations (Beans)", [("ration_box",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
100,weight(10)|abundance(10)|food_quality(30)|max_ammo(50),imodbits_none],
["canned_fish","Rations (Chicken)", [("ration_box",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
100,weight(10)|abundance(10)|food_quality(20)|max_ammo(50),imodbits_none],
["canned_fruits","Rations (Fruit)", [("ration_box",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
100,weight(10)|abundance(10)|food_quality(20)|max_ammo(50),imodbits_none],
["canned_meat","Rations (Beef)", [("ration_box",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
100,weight(10)|abundance(10)|food_quality(20)|max_ammo(50),imodbits_none],
["canned_milk","Rations (Confectionary)", [("ration_box",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
100,weight(10)|abundance(10)|food_quality(10)|max_ammo(50),imodbits_none],
["canned_soup","Rations (Pasta)", [("ration_box",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
100,weight(10)|abundance(10)|food_quality(10)|max_ammo(50),imodbits_none],
["canned_veg","Rations (Vegetables)", [("ration_box",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
100,weight(10)|abundance(10)|food_quality(10)|max_ammo(50),imodbits_none],

["human_meat","Raw Flesh", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 
  80,weight(2)|abundance(0)|food_quality(120)|max_ammo(15),imodbits_none],

#drink
["clean_water","Clean_Water_Ration", [("fresh_canteen", 0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
250, weight(5)|abundance(50)|food_quality(50)|max_ammo(15),imodbits_none],
["water","Water_Ration", [("issued_canteen", 0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
50, weight(5)|abundance(75)|food_quality(10)|max_ammo(15),imodbits_none],
["dirty_water","Dirty_Water_Ration", [("rusty_canteen", 0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
25, weight(5)|food_quality(0)|max_ammo(15),imodbits_none],

["wine","Wine Barrel", [("wine_barrel",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
500,weight(30)|abundance(50)|food_quality(50)|max_ammo(20),imodbits_none],
["ale","Ale Barrel", [("ale_barrel",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
250,weight(30)|abundance(50)|food_quality(25)|max_ammo(20),imodbits_none],

["wine_s","Wine", [("wine_bottles",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
150,weight(1)|abundance(75)|food_quality(50)|max_ammo(13),imodbits_none],
["ale_s","Ale", [("ale_bottle",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
75,weight(1)|abundance(75)|food_quality(25)|max_ammo(13),imodbits_none],

["butter","Milk", [("butter_pot",0)], itp_type_goods|itp_consumable|itp_food|itp_merchandise, 0,
30,weight(1)|abundance(25)|food_quality(10)|max_ammo(13),imodbits_none],


#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************
# Quest Items
["siege_supply","Supplies", [("oil",0)], itp_type_goods, 0, 96,weight(40)|abundance(70),imodbits_none],
["quest_wine","Wine", [("wine_barrel",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],
["trade_item","Trade_Item", [("ale_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],

#blueprints



#
##************************************************************************************************
## AMMO
##************************************************************************************************
#arrows
["arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 
  72,weight(3)|abundance(40)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(30),imodbits_missile],
["ezeg_arrows","Ezeg_Arrows", [("barbed_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
  124,weight(3)|abundance(20)|weapon_length(95)|thrust_damage(2,pierce)|max_ammo(30),imodbits_missile],
["yanizar_arrows","yanizar_Arrows", [("barbed_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
  410,weight(3.5)|abundance(10)|weapon_length(95)|thrust_damage(3,pierce)|max_ammo(30),imodbits_missile],
#
["ossi_arrows","Os-si_Arrows", [("ossi_arrow",0),("flying_missile",ixmesh_flying_ammo),("ossi_quiver", ixmesh_carry)], itp_type_arrows|itp_unique, itcf_carry_quiver_back_right, 
  4000,weight(1)|weapon_length(91)|thrust_damage(25,pierce)|max_ammo(100),imodbits_missile],
#
#pistol_ammo
["pistol_ammo","Recycled_Full_Metal_Jacket_Pistol/SMG_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_pistol_1_recycled",ixmesh_inventory),("ammo_pistol_1_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  100,weight(2.25)|abundance(100)|weapon_length(3)|thrust_damage(2,cut)|max_ammo(60),imodbits_missile,[bullet_impact]],
["pistol_ammo_pw","Factory_Full_Metal_Jacket_Pistol/SMG_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_pistol_1",ixmesh_inventory),("ammo_pistol_1",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_can_penetrate_shield|itp_merchandise,0,
  200,weight(2.25)|abundance(50)|weapon_length(3)|thrust_damage(4,cut)|max_ammo(50),imodbits_missile,[bullet_impact]],

["pistol_ammo_2","Recycled_Hollow-Point_Pistol/SMG_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_pistol_2_recycled",ixmesh_inventory),("ammo_pistol_2_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_merchandise,0,
  110,weight(3)|abundance(80)|weapon_length(3)|thrust_damage(2,blunt)|max_ammo(60),imodbits_missile,[bullet_impact]],
["pistol_ammo_2_pw","Factory_Hollow-Point_Pistol/SMG_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_pistol_2",ixmesh_inventory),("ammo_pistol_2",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_merchandise,0,
  220,weight(3)|abundance(40)|weapon_length(3)|thrust_damage(4,blunt)|max_ammo(50),imodbits_missile,[bullet_impact]],

["pistol_ammo_3","Recycled_Hollow-Base_Pistol/SMG_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_pistol_3_recycled",ixmesh_inventory),("ammo_pistol_3_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  110,weight(2.25)|abundance(100)|weapon_length(5)|thrust_damage(2,cut)|max_ammo(60),imodbits_missile,[bullet_impact]],
["pistol_ammo_3_pw","Factory_Hollow-Base_Pistol/SMG_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_pistol_3",ixmesh_inventory),("ammo_pistol_3",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_can_penetrate_shield|itp_merchandise,0,
  220,weight(2.25)|abundance(50)|weapon_length(5)|thrust_damage(4,cut)|max_ammo(50),imodbits_missile,[bullet_impact]],

["pistol_ammo_4","Recycled_Armour-Piercing_Pistol/SMG_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_pistol_4_recycled",ixmesh_inventory),("ammo_pistol_4_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_extra_penetration|itp_merchandise,0,
  150,weight(2.25)|abundance(80)|weapon_length(3)|thrust_damage(2,pierce)|max_ammo(45),imodbits_missile,[bullet_impact]],
["pistol_ammo_4_pw","Factory_Armour-Piercing_Pistol/SMG_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_pistol_4",ixmesh_inventory),("ammo_pistol_4",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_can_penetrate_shield|itp_extra_penetration|itp_merchandise,0,
  250,weight(2.25)|abundance(30)|weapon_length(3)|thrust_damage(4,pierce)|max_ammo(35),imodbits_missile,[bullet_impact]],

["pistol_ammo_5","Recycled_Lightened_Pistol/SMG_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_pistol_5_recycled",ixmesh_inventory),("ammo_pistol_5_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  110,weight(1.25)|abundance(90)|weapon_length(3)|thrust_damage(2,cut)|max_ammo(60),imodbits_missile,[bullet_impact]],
["pistol_ammo_5_pw","Factory_Lightened_Pistol/SMG_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_pistol_5",ixmesh_inventory),("ammo_pistol_5",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_can_penetrate_shield|itp_merchandise,0,
  220,weight(1.25)|abundance(45)|weapon_length(3)|thrust_damage(4,cut)|max_ammo(50),imodbits_missile,[bullet_impact]],

["pistol_ammo_6","Recycled_Low_Powered_Pistol/SMG_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_pistol_6_recycled",ixmesh_inventory),("ammo_pistol_6_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  50,weight(2.25)|abundance(100)|weapon_length(1)|thrust_damage(1,cut)|max_ammo(70),imodbits_missile,[bullet_impact]],
["pistol_ammo_6_pw","Factory_Low_Powered_Pistol/SMG_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_pistol_6",ixmesh_inventory),("ammo_pistol_6",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_can_penetrate_shield|itp_merchandise,0,
  100,weight(2.25)|abundance(50)|weapon_length(1)|thrust_damage(2,cut)|max_ammo(60),imodbits_missile,[bullet_impact]],
#
["pistol_ammo_miasma","Miasma_Infused_Pistol/SMG_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_pistol_miasma",ixmesh_inventory),("ammo_pistol_miasma",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_can_penetrate_shield|itp_merchandise,0,
  2800,weight(5)|abundance(5)|weapon_length(3)|thrust_damage(5,cut)|max_ammo(30),imodbits_missile,[bullet_impact]],

#
#rifle_ammo
["rifle_ammo","Recycled_Full_Metal_Jacket_Rifle_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_rifle_1_recycled",ixmesh_inventory),("ammo_rifle_1_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  200,weight(3)|abundance(90)|weapon_length(3)|thrust_damage(3,cut)|max_ammo(60),imodbits_missile,[bullet_impact]],
["rifle_ammo_pw","Factory_Full_Metal_Jacket_Rifle_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_rifle_1",ixmesh_inventory),("ammo_rifle_1",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_can_penetrate_shield|itp_merchandise,0,
  300,weight(3)|abundance(45)|weapon_length(3)|thrust_damage(5,cut)|max_ammo(50),imodbits_missile,[bullet_impact]],

["rifle_ammo_2","Recycled_Armour-Piercing_Rifle_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_rifle_2_recycled",ixmesh_inventory),("ammo_rifle_2_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_extra_penetration|itp_merchandise,0,
  300,weight(3)|abundance(70)|weapon_length(3)|thrust_damage(3,pierce)|max_ammo(60),imodbits_missile,[bullet_impact]],
["rifle_ammo_2_pw","Factory_Armour-Piercing_Rifle_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_rifle_2",ixmesh_inventory),("ammo_rifle_2",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_can_penetrate_shield|itp_extra_penetration|itp_merchandise,0,
  400,weight(3)|abundance(25)|weapon_length(3)|thrust_damage(5,pierce)|max_ammo(50),imodbits_missile,[bullet_impact]],

["rifle_ammo_3","Recycled_Hollow-Base_Rifle_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_rifle_3_recycled",ixmesh_inventory),("ammo_rifle_3_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  220,weight(3)|abundance(90)|weapon_length(5)|thrust_damage(3,cut)|max_ammo(60),imodbits_missile,[bullet_impact]],
["rifle_ammo_3_pw","Factory_Hollow-Base_Rifle_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_rifle_3",ixmesh_inventory),("ammo_rifle_3",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_can_penetrate_shield|itp_merchandise,0,
  330,weight(3)|abundance(45)|weapon_length(5)|thrust_damage(5,cut)|max_ammo(50),imodbits_missile,[bullet_impact]],

["rifle_ammo_4","Recycled_Low_Powered_Rifle_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_rifle_4_recycled",ixmesh_inventory),("ammo_rifle_4_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  100,weight(3)|abundance(90)|weapon_length(3)|thrust_damage(2,cut)|max_ammo(70),imodbits_missile,[bullet_impact]],
["rifle_ammo_4_pw","Factory_Low_Powered_Rifle_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_rifle_4",ixmesh_inventory),("ammo_rifle_4",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_can_penetrate_shield|itp_merchandise,0,
  250,weight(3)|abundance(45)|weapon_length(3)|thrust_damage(4,cut)|max_ammo(60),imodbits_missile,[bullet_impact]],

["rifle_ammo_5","Recycled_Hollow-Point_Rifle_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_rifle_5_recycled",ixmesh_inventory),("ammo_rifle_5_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_merchandise,0,
  220,weight(3.75)|abundance(90)|weapon_length(3)|thrust_damage(3,blunt)|max_ammo(60),imodbits_missile,[bullet_impact]],
["rifle_ammo_5_pw","Factory_Hollow-Point_Rifle_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_rifle_5",ixmesh_inventory),("ammo_rifle_5",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_merchandise,0,
  330,weight(3.75)|abundance(45)|weapon_length(3)|thrust_damage(5,blunt)|max_ammo(50),imodbits_missile,[bullet_impact]],

["rifle_ammo_6","Recycled_Lightened_Rifle_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_rifle_6_recycled",ixmesh_inventory),("ammo_rifle_6_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  220,weight(2)|abundance(90)|weapon_length(3)|thrust_damage(3,cut)|max_ammo(60),imodbits_missile,[bullet_impact]],
["rifle_ammo_6_pw","Factory_Lightened_Rifle_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_rifle_6",ixmesh_inventory),("ammo_rifle_6",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_can_penetrate_shield|itp_merchandise,0,
  330,weight(2)|abundance(45)|weapon_length(3)|thrust_damage(5,cut)|max_ammo(50),imodbits_missile,[bullet_impact]],

#
#large_caliber_ammo
["large_caliber_ammo","Recycled_Full_Metal_Jacket_Large_Caliber_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_large_1_recycled",ixmesh_inventory),("ammo_large_1_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  300,weight(3.5)|abundance(75)|weapon_length(3)|thrust_damage(5,cut)|max_ammo(30),imodbits_missile,[bullet_impact]],
["large_caliber_ammo_pw","Factory_Full_Metal_Jacket_Large_Caliber_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_large_1",ixmesh_inventory),("ammo_large_1",ixmesh_carry)],
  itp_type_bullets|itp_can_penetrate_shield|itp_merchandise,0,
  400,weight(3.5)|abundance(40)|weapon_length(3)|thrust_damage(7,cut)|max_ammo(20),imodbits_missile,[bullet_impact]],

["large_caliber_ammo_2","Recycled_Hollow-Base_Large_Caliber_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_large_2_recycled",ixmesh_inventory),("ammo_large_2_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  330,weight(3.5)|abundance(75)|weapon_length(5)|thrust_damage(5,cut)|max_ammo(30),imodbits_missile,[bullet_impact]],
["large_caliber_ammo_2_pw","Factory_Hollow-Base_Large_Caliber_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_large_2",ixmesh_inventory),("ammo_large_2",ixmesh_carry)],
  itp_type_bullets|itp_can_penetrate_shield|itp_merchandise,0,
  440,weight(3.5)|abundance(40)|weapon_length(5)|thrust_damage(7,cut)|max_ammo(20),imodbits_missile,[bullet_impact]],

["large_caliber_ammo_3","Recycled_Hollow-Point_Large_Caliber_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_large_3_recycled",ixmesh_inventory),("ammo_large_3_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  330,weight(4.25)|abundance(75)|weapon_length(3)|thrust_damage(5,blunt)|max_ammo(30),imodbits_missile,[bullet_impact]],
["large_caliber_ammo_3_pw","Factory_Hollow-Point_Large_Caliber_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_large_3",ixmesh_inventory),("ammo_large_3",ixmesh_carry)],
  itp_type_bullets|itp_can_penetrate_shield|itp_merchandise,0,
  440,weight(4.25)|abundance(40)|weapon_length(3)|thrust_damage(7,blunt)|max_ammo(20),imodbits_missile,[bullet_impact]],

["large_caliber_ammo_4","Recycled_Armour-Piercing_Large_Caliber_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_large_4_recycled",ixmesh_inventory),("ammo_large_4_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_extra_penetration|itp_merchandise,0,
  500,weight(3.5)|abundance(55)|weapon_length(3)|thrust_damage(5,pierce)|max_ammo(30),imodbits_missile,[bullet_impact]],
["large_caliber_ammo_4_pw","Factory_Armour-Piercing_Large_Caliber_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_large_4",ixmesh_inventory),("ammo_large_4",ixmesh_carry)],
  itp_type_bullets|itp_can_penetrate_shield|itp_extra_penetration|itp_merchandise,0,
  600,weight(3.5)|abundance(20)|weapon_length(3)|thrust_damage(7,pierce)|max_ammo(20),imodbits_missile,[bullet_impact]],

["large_caliber_ammo_5","Recycled_Incendiary_Large_Caliber_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_large_5_recycled",ixmesh_inventory),("ammo_large_5_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  500,weight(3.5)|abundance(55)|weapon_length(3)|thrust_damage(7,cut)|max_ammo(30),imodbits_missile,[
  (ti_on_missile_hit,[(particle_system_add_new,"psys_fireplace_fire_big"),]),]],
["large_caliber_ammo_5_pw","Factory_Incendiary_Large_Caliber_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("ammo_large_5",ixmesh_inventory),("ammo_large_5",ixmesh_carry)],
  itp_type_bullets|itp_can_penetrate_shield|itp_merchandise,0,
  600,weight(3.5)|abundance(20)|weapon_length(3)|thrust_damage(9,cut)|max_ammo(20),imodbits_missile,[
  (ti_on_missile_hit,[(particle_system_add_new,"psys_fireplace_fire_big"),]),]],
#
#shotgun_ammo
["buckshot_ammo","Recycled_Shotgun_Buckshot_Rounds",
  [("buckshot_missile",ixmesh_flying_ammo),("ammo_5_buckshot_recycled",ixmesh_inventory),("ammo_5_buckshot_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  225,weight(2.25)|abundance(80)|weapon_length(3)|thrust_damage(1,cut)|max_ammo(55),imodbits_missile,[smaller_bullet_impact]],
["buckshot_ammo_pw","Factory_Shotgun_Buckshot_Rounds",
  [("buckshot_missile",ixmesh_flying_ammo),("ammo_5_buckshot",ixmesh_inventory),("ammo_5_buckshot",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_can_penetrate_shield|itp_merchandise,0,
  325,weight(2.25)|abundance(40)|weapon_length(3)|thrust_damage(3,cut)|max_ammo(45),imodbits_missile,[smaller_bullet_impact]],

["slug_ammo","Recycled_Shotgun_Slug_Rounds",
  [("buckshot_missile",ixmesh_flying_ammo),("ammo_5_recycled",ixmesh_inventory),("ammo_5_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  225,weight(2.25)|abundance(80)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(35),imodbits_missile,[smaller_bullet_impact]],
["slug_ammo_pw","Factory_Shotgun_Slug_Rounds",
  [("buckshot_missile",ixmesh_flying_ammo),("ammo_5",ixmesh_inventory),("ammo_5",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_can_penetrate_shield|itp_merchandise,0,
  325,weight(2.25)|abundance(40)|weapon_length(3)|thrust_damage(3,pierce)|max_ammo(25),imodbits_missile,[smaller_bullet_impact]],

["flameshot_ammo","Recycled_Shotgun_Incendiary_Buckshot_Rounds",
  [("buckshot_missile",ixmesh_flying_ammo),("ammo_5_buckshot_recycled",ixmesh_inventory),("ammo_5_buckshot_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_merchandise,0,
  725,weight(3.25)|abundance(80)|weapon_length(3)|thrust_damage(5,cut)|max_ammo(30),imodbits_missile,[
  (ti_on_missile_hit,[(particle_system_add_new,"psys_fireplace_fire_big"),]),]],
["flameshot_ammo_pw","Factory_Shotgun_Incendiary_Buckshot_Rounds",
  [("buckshot_missile",ixmesh_flying_ammo),("ammo_5_buckshot",ixmesh_inventory),("ammo_5_buckshot",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_merchandise,0,
  925,weight(3.25)|abundance(40)|weapon_length(3)|thrust_damage(10,cut)|max_ammo(20),imodbits_missile,[
  (ti_on_missile_hit,[(particle_system_add_new,"psys_fireplace_fire_big"),]),]],
#
#riot_ammo
["blunt_slug_ammo","Recycled_Shotgun_Baton_Rounds",
  [("buckshot_missile",ixmesh_flying_ammo),("ammo_5_recycled",ixmesh_inventory),("ammo_5_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  325,weight(2.25)|abundance(60)|weapon_length(3)|thrust_damage(1,blunt)|max_ammo(35),imodbits_missile,[smaller_bullet_impact]],
["blunt_slug_ammo_pw","Factory_Shotgun_Baton_Rounds",
  [("buckshot_missile",ixmesh_flying_ammo),("ammo_5",ixmesh_inventory),("ammo_5",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_can_penetrate_shield|itp_merchandise,0,
  425,weight(2.25)|abundance(20)|weapon_length(3)|thrust_damage(3,blunt)|max_ammo(25),imodbits_missile,[smaller_bullet_impact]],
#
#mg_ammo
["mg_ammo","Recycled_MG_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("cartridge_new_recycled",ixmesh_inventory),("cartridge_new_recycled",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield|itp_merchandise,0,
  1000,weight(12.25)|abundance(70)|weapon_length(3)|thrust_damage(5,cut)|max_ammo(250),imodbit_bent,[bullet_impact]],	#removed large bag as causes unlimited bullets somehow
["mg_ammo_pw","Factory_MG_Rounds",
  [("bullet_missile",ixmesh_flying_ammo),("cartridge_new",ixmesh_inventory),("cartridge_new",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_can_penetrate_shield|itp_merchandise,0,
  1500,weight(12.25)|abundance(35)|weapon_length(3)|thrust_damage(7,cut)|max_ammo(250),imodbit_bent,[bullet_impact]],
#
#special
["plasma_ammo","Experimental_Rounds",
  [("swy_blasterbolt_green_alpha",ixmesh_flying_ammo),("magazines_1",ixmesh_inventory),("magazines_1",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield,0,
  500,weight(2.25)|abundance(50)|weapon_length(3)|thrust_damage(7,pierce)|max_ammo(50),imodbits_missile,[]],
#
["artillery_ammo","Artillery_Shells",
  [("cannonball_3lb",ixmesh_flying_ammo),("cannonball_3lb",ixmesh_inventory),("cannonball_3lb",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield,0,
  500,weight(40)|weapon_length(3)|thrust_damage(30,cut)|max_ammo(10),imodbits_missile,[
  (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (call_script,"script_create_explosion", pos1,":agent","itm_artillery_ammo", 1000, 75, 105, 1),
    ]),]],
#
["rocket_ammo","Rockets",
  [("rocket_missile",ixmesh_flying_ammo),("rockets_1",ixmesh_inventory),("rockets_1",ixmesh_carry)],
  itp_type_bullets|itp_ignore_gravity|itp_default_ammo|itp_can_penetrate_shield,0,
  500,weight(40)|weapon_length(3)|thrust_damage(30,cut)|max_ammo(3),imodbits_missile,[
  (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (call_script,"script_create_explosion", pos1,":agent","itm_rocket_ammo", 1000, 35, 85, 1),
    ]),]],
["grenade_ammo","Grenade",
  [("cannonball_3lb",ixmesh_flying_ammo),("cannonball_3lb",ixmesh_inventory),("cannonball_3lb",ixmesh_carry)],
  itp_type_bullets|itp_can_penetrate_shield,0,
  500,weight(40)|weapon_length(3)|thrust_damage(30,cut)|max_ammo(12),imodbits_missile,[
  (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (call_script,"script_create_explosion", pos1,":agent","itm_grenade_ammo", 800, 25, 55, 1),
    ]),]],
#
#flame_ammo
["flameammo","Flamethrower_Fuel",
  [("ammobelt",0),("ammobelt",ixmesh_inventory),("dummy_mesh",ixmesh_flying_ammo),("ammobelt",ixmesh_carry),("ammobelt_2",imodbit_large_bag)],
  itp_type_bullets|itp_merchandise|itp_default_ammo,0,
  150,weight(2.25)|abundance(75)|weapon_length(3)|max_ammo(150)|thrust_damage(25,cut),imodbits_missile,[
  (ti_on_missile_hit,[(particle_system_add_new,"psys_fireplace_fire_big"),]),]],
#
["flameammo_burst","Flameburst_Cartridges",
  [("ammobelt",0),("ammobelt",ixmesh_inventory),("grenade_molotov",ixmesh_flying_ammo),("ammobelt",ixmesh_carry),("ammobelt_2",imodbit_large_bag)],
  itp_type_bullets|itp_merchandise|itp_default_ammo,0,
  480,weight(2.25)|abundance(35)|weapon_length(3)|max_ammo(20)|thrust_damage(25,cut),imodbits_missile,[
  (ti_on_missile_hit, [
      (store_trigger_param_1,":agent"),
      (particle_system_add_new,"psys_fireplace_fire_big"),
      (call_script,"script_create_explosion", pos1,":agent","itm_flameammo_burst", 600, 25, 65, 1),
    ]),]],
#
##************************************************************************************************
## OUTFITS
##************************************************************************************************
["bride_dress","Bride_Dress",[("bride_dress",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1,weight(3)|body_armor(10)|leg_armor(10),0],
["bride_crown","Crown_of_Flowers",[("bride_crown",0)],itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian|itp_attach_armature,0,
  1,weight(0.5)|head_armor(4)|body_armor(0),0],
["formal","Formal Suit", [("formal", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  1, weight(1)|body_armor(10)|leg_armor(10), 0, [], []],

###################################################################################
##HANDSLOT##
##################################################################################
["leather_gloves","Leather_Gloves",[("leather_gloves_L",0)],itp_type_hand_armor|itp_merchandise,0,
  125,weight(0.25)|body_armor(2),imodbits_cloth],
["leather_gloves_metal","Leather_Gloves_with_Metal_Protection",[("leather_gloves_metal_L",0),("leather_gloves_metal_rusty_L",imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude)],itp_type_hand_armor|itp_merchandise,0,
  300,weight(1.5)|body_armor(5)|abundance(90),imodbits_cloth],
["black_gloves","Leather_Gloves",[("gloves_black_L",0)],itp_type_hand_armor|itp_merchandise,0,
  125,weight(0.25)|body_armor(2),imodbits_cloth],
["black_gloves_metal","Leather_Gloves_with_Metal_Protection",[("gloves_black_metal_L",0),("gloves_black_metal_rusty_L",imodbit_cracked|imodbit_rusty|imodbit_battered|imodbit_crude)],itp_type_hand_armor|itp_merchandise,0,
  300,weight(1.5)|body_armor(5)|abundance(90),imodbits_cloth],
["hazard_gloves","Hazard_Unit_Gloves",[("hazard_unit_gloves_L",0)],itp_type_hand_armor,0,
  650,weight(2.5)|body_armor(8)|abundance(10),imodbits_armor],

################
##Barbed Wire###
################
##Entenaii Empire
["entenaii_gloves","Entenaii_Empire_Gloves",[("entenaii_gloves_L",0)],itp_type_hand_armor|itp_merchandise,0,
  125,weight(0.25)|body_armor(2),imodbits_cloth],
["entenaii_demi_gauntlets","Entenaii_Empire_Demi_Gauntlets",[("entenaii_demi_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  300,weight(1.5)|body_armor(5)|abundance(60),imodbits_armor],
["entenaii_gauntlets","Entenaii_Empire_Gauntlets",[("entenaii_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  650,weight(2.5)|body_armor(8)|abundance(10),imodbits_armor],
#
["entenaii_emperor_gauntlets","Emperor_Gauntlets",[("entenaii_emperor_gauntlets_L",0)],itp_type_hand_armor,0,
  1000,weight(2.5)|body_armor(12),imodbits_armor],

##Entenaii Dominion
["dominion_gloves","Entenaii_Dominion_Gloves",[("dominion_gloves_L",0)],itp_type_hand_armor|itp_merchandise,0,
  125,weight(0.25)|body_armor(2),imodbits_cloth],
["dominion_demi_gauntlets","Entenaii_Dominion_Demi_Gauntlets",[("dominion_demi_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  300,weight(1.5)|body_armor(5)|abundance(60),imodbits_armor],
["dominion_gauntlets","Entenaii_Dominion_Gauntlets",[("dominion_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  650,weight(2.5)|body_armor(8)|abundance(10),imodbits_armor],
["beastling_hands","Beastling_Hands",[("beastling_1_hand_L",0)],itp_type_hand_armor|itp_unique,0,
  1000,weight(0)|body_armor(10),imodbits_none],
#
["dominion_governer_general_gauntlets","Governer_General_Gauntlets",[("dominion_gauntlets_L",0)],itp_type_hand_armor,0,
  1000,weight(2.5)|body_armor(10),imodbits_armor],

##Kingdom of Galvae
["galvae_gloves","Galvae_Gloves",[("galvae_gloves_L",0)],itp_type_hand_armor|itp_merchandise,0,
  125,weight(0.25)|body_armor(2),imodbits_cloth],
["galvae_demi_gauntlets","Galvae_Demi_Gauntlets",[("galvae_demi_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  300,weight(1.5)|body_armor(5)|abundance(60),imodbits_armor],
["galvae_gauntlets","Galvae_Gauntlets",[("galvae_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  650,weight(2.5)|body_armor(8)|abundance(10),imodbits_armor],
["galvae_tanfen_gauntlets","Galvae_Tanfen_Gauntlets",[("galvae_falcon_fist_L",0)],itp_type_hand_armor|itp_unique,0,
  1000,weight(1.5)|body_armor(10),imodbits_armor],
#
["galvae_royal_gauntlets","Royal_Gauntlets",[("galvae_gauntlets_L",0)],itp_type_hand_armor,0,
  1000,weight(2.5)|body_armor(10),imodbits_armor],

##Molvat-Berchav Union
["union_gloves","Union_Gloves",[("union_gloves_L",0)],itp_type_hand_armor|itp_merchandise,0,
  125,weight(0.25)|body_armor(2),imodbits_cloth],
["union_mittens","Union_Mittens",[("union_mittens_L",0)],itp_type_hand_armor|itp_merchandise,0,
  175,weight(1)|body_armor(3),imodbits_cloth],
["union_demi_gauntlets","Union_Demi_Gauntlets",[("union_demi_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  300,weight(1.5)|body_armor(5)|abundance(60),imodbits_armor],
["union_gauntlets","Union_Gauntlets",[("union_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  650,weight(2.5)|body_armor(8)|abundance(10),imodbits_armor],
["ravga_gauntlets","Ravga_Gauntlets",[("ravga_gauntlet_L",0)],itp_type_hand_armor|itp_unique,0,
  1000,weight(3)|body_armor(10),imodbits_armor],
#
["union_tzar_gauntlets","Tzar_Gauntlets",[("union_gauntlets_L",0)],itp_type_hand_armor,0,
  1000,weight(2.5)|body_armor(10),imodbits_armor],

##Vitzland Territories
["vitzland_gloves","Vitzland_Gloves",[("vitzland_gloves_L",0)],itp_type_hand_armor|itp_merchandise,0,
  125,weight(0.25)|body_armor(2),imodbits_cloth],
["vitzland_demi_gauntlets","Vitzland_Demi_Gauntlets",[("vitzland_demi_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  300,weight(1.5)|body_armor(5)|abundance(60),imodbits_armor],
["vitzland_gauntlets","Vitzland_Gauntlets",[("vitzland_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  650,weight(2.5)|body_armor(8)|abundance(10),imodbits_armor],
["nachman_gauntlets","Nachman_Gauntlets",[("nactman_gauntlets_L",0)],itp_type_hand_armor|itp_unique,0,
  1000,weight(2.5)|body_armor(10),imodbits_armor],
#
["vitzland_kaiser_gauntlets","Kaiser_Gauntlets",[("vitzland_gauntlets_L",0)],itp_type_hand_armor,0,
  1000,weight(2.5)|body_armor(10),imodbits_armor],

##Trezzo Republic
["republican_gloves","Republican_Gloves",[("republican_white_gloves_L",0)],itp_type_hand_armor|itp_merchandise,0,
  200,weight(0.25)|body_armor(3),imodbits_cloth],
["republican_gloves_2","Republican_Gloves",[("republican_buff_gloves_L",0)],itp_type_hand_armor|itp_merchandise,0,
  200,weight(0.25)|body_armor(3),imodbits_cloth],
["republican_demi_gauntlets","Republican_Mail_Gauntlets",[("republican_demi_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  400,weight(1.5)|body_armor(6)|abundance(60),imodbits_armor],
["republican_gauntlets","Republican_Gauntlets",[("republican_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  850,weight(2.5)|body_armor(9)|abundance(10),imodbits_armor],
["servo_cav_gauntlets","Republican_Spider_Gloves",[("republican_gloves_noble_L",0)],itp_type_hand_armor|itp_unique,0,
  1250,weight(1.5)|body_armor(11),imodbits_cloth],
#
["republican_doge_gauntlets","Doge_Gauntlets",[("republican_gauntlets_L",0)],itp_type_hand_armor,0,
  2500,weight(3.5)|body_armor(12),imodbits_armor],

##Itami Castedom
["itami_gloves","Itami_Gloves",[("itami_gloves_L",0)],itp_type_hand_armor|itp_merchandise,0,
  50,weight(0.25)|body_armor(2),imodbits_cloth],
["itami_demi_gauntlets","Itami_Demi_Gauntlets",[("gloves_kote_1_L",0)],itp_type_hand_armor|itp_merchandise,0,
  125,weight(1.5)|body_armor(5)|abundance(60),imodbits_armor],
["itami_gauntlets","Itami_Gauntlets",[("itami_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  500,weight(2.5)|body_armor(8)|abundance(10),imodbits_armor],
["itami_terror_gauntlets","Itami_Terror_Gauntlets",[("itami_gloves_noble_L",0)],itp_type_hand_armor|itp_unique,0,
  900,weight(0.5)|body_armor(3),imodbits_cloth],
#
["itami_kytra_gauntlets","Kytra_Gauntlets",[("itami_kytra_gauntlets_L",0)],itp_type_hand_armor,0,
  1000,weight(2.5)|body_armor(10),imodbits_armor],
  
##Bashide Confederacy
["bashide_gloves","Bashide_Gloves",[("bashide_gloves_L",0)],itp_type_hand_armor|itp_merchandise,0,
  50,weight(0.25)|body_armor(2),imodbits_cloth],
["bashide_gloves_b","Bashide_Noble_Gloves",[("bashide_gloves_b_L",0)],itp_type_hand_armor|itp_merchandise,0,
  50,weight(0.25)|body_armor(2),imodbits_cloth],
["bashide_gloves_c","Gidon_Gloves",[("bashide_gloves_c_L",0)],itp_type_hand_armor|itp_merchandise,0,
  50,weight(0.25)|body_armor(2),imodbits_cloth],

["bashide_demi_gauntlets","Bashide_Demi_Gauntlets",[("bashide_gauntlets_splint_scale_L",0)],itp_type_hand_armor|itp_merchandise,0,
  125,weight(1.5)|body_armor(5)|abundance(60),imodbits_armor],
["bashide_gauntlets","Bashide_Gauntlets",[("bashide_gauntlets_studded_L",0)],itp_type_hand_armor|itp_merchandise,0,
  500,weight(2.5)|body_armor(8)|abundance(10),imodbits_armor],
["bashide_terror_gauntlets","Bashide_Terror_Gauntlets",[("bashide_gauntlets_splint_L",0)],itp_type_hand_armor|itp_unique,0,
  900,weight(0.5)|body_armor(3),imodbits_cloth],
#
["bashide_alran_gauntlets","Alran_Gauntlets",[("bashide_alran_gauntlets_L",0)],itp_type_hand_armor,0,
  1000,weight(2.5)|body_armor(10),imodbits_armor],
#

##Renegade
["renegade_gloves","Renegade_Gloves",[("leather_gloves_L",0)],itp_type_hand_armor|itp_merchandise,0,
  50,weight(0.25)|body_armor(2),imodbits_cloth],
["renegade_demi_gauntlets","Renegade_Demi_Gauntlets",[("leather_gloves_metal_L",0)],itp_type_hand_armor|itp_merchandise,0,
  125,weight(1.5)|body_armor(5)|abundance(60),imodbits_armor],
["renegade_gauntlets","Renegade_Gauntlets",[("hazard_unit_gloves_L",0)],itp_type_hand_armor|itp_merchandise,0,
  500,weight(2.5)|body_armor(8)|abundance(10),imodbits_armor],
#
["renegade_leader_gauntlets","Leader_Gauntlets",[("hazard_unit_gloves_L",0)],itp_type_hand_armor,0,
  1000,weight(2.5)|body_armor(10),imodbits_armor],

#Throd
["throd_gauntlets","Throd_Gauntlets",[("throd_gauntlets_L",0)],itp_type_hand_armor,0,
  500,weight(4)|body_armor(9)|abundance(10),imodbits_armor],

#Other
["bandit_gloves","Gloves",[("bandit_gloves_L",0)],itp_type_hand_armor|itp_merchandise,0,
  40,weight(0.25)|body_armor(1),imodbits_cloth],
["white_gloves","Gloves",[("gloves_white_L",0)],itp_type_hand_armor|itp_merchandise,0,
  40,weight(0.25)|body_armor(1),imodbits_cloth],

#
["neutral_gloves","Gloves",[("neutral_glove_L",0)],itp_type_hand_armor|itp_merchandise,0,
  40,weight(0.25)|body_armor(1),imodbits_cloth],
["neutral_mail_mittens","Mail_Mittens",[("neutral_mail_mitten_L",0)],itp_type_hand_armor|itp_merchandise,0,
  100,weight(1.5)|body_armor(4)|abundance(60),imodbits_armor],
["neutral_gauntlets","Gauntlets",[("neutral_gauntlet_L",0)],itp_type_hand_armor|itp_merchandise,0,
  250,weight(2.5)|body_armor(7)|abundance(10),imodbits_armor],
#
["cannibal_hands","Cannibal_Hands",[("cannibal_hand_L",0)],itp_type_hand_armor|itp_unique,0,
  500,weight(0)|body_armor(5),imodbits_none],
#
["night_raider_gloves","Night_Raider_Gloves",[("twilight_gloves_L",0)],itp_type_hand_armor|itp_merchandise,0,
  40,weight(0.25)|body_armor(3)|abundance(40),imodbits_cloth],
["night_raider_mail_mittens","Mail_Mittens",[("neutral_mail_mitten_L",0)],itp_type_hand_armor|itp_merchandise,0,
  100,weight(1.5)|body_armor(8)|abundance(20),imodbits_armor],
["night_raider_gauntlets","Night_Raider_Gauntlets",[("night_raider_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  250,weight(2.5)|body_armor(11)|abundance(10),imodbits_armor],
#
["blackgod_knight_gauntlets","Night_Raider_Gauntlets",[("blackgod_knight_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  250,weight(2.5)|body_armor(12)|abundance(10),imodbits_armor],
#
#totem
["bear_gauntlets","Bear_Gauntlets",[("beargauntlets_L",0)],itp_type_hand_armor,0,
  200,weight(2)|body_armor(6)|abundance(10),imodbits_armor],
["bear_gauntlets_dark","Bear_Gauntlets",[("beargauntlets_dark_L",0)],itp_type_hand_armor,0,
  250,weight(2.5)|body_armor(8)|abundance(10),imodbits_armor],
#
["cursed_one_gauntlets","Cursed_One_Gauntlets",[("cursed_one_gauntlets_L",0)],itp_type_hand_armor,0,
  1050,weight(8)|body_armor(14),imodbits_armor],
#
["handwraps","Handwraps",[("handwraps_L",0)],itp_type_hand_armor|itp_merchandise,0,
  50,weight(0.25)|body_armor(1),imodbits_cloth],
["handwraps_black","Handwraps",[("handwraps_black_L",0)],itp_type_hand_armor|itp_merchandise,0,
  50,weight(0.25)|body_armor(1),imodbits_cloth],
["scale_gauntlets","Scale_Gauntlets",[("scale_gauntlets_L",0)],itp_type_hand_armor|itp_merchandise,0,
  225,weight(1.85)|body_armor(6)|abundance(55),imodbits_armor],

###################################################################################
##FOOTSLOT##
##################################################################################
["backpack_ammo","Large_Rucksack",[("backpack_ammo",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  250,weight(2.5)|body_armor(3)|abundance(10),imodbits_cloth],
["rucksack_entenaii","Rucksack",[("rucksack_entenaii",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  125,weight(2.5)|body_armor(1)|abundance(30),imodbits_cloth],
["rucksack_dominion","Rucksack",[("rucksack_dominion",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  125,weight(2.5)|body_armor(1)|abundance(30),imodbits_cloth],
["rucksack_galvae","Rucksack",[("rucksack_galvae",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  125,weight(2.5)|body_armor(1)|abundance(30),imodbits_cloth],
["rucksack_union","Rucksack",[("rucksack_union",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  125,weight(2.5)|body_armor(1)|abundance(30),imodbits_cloth],
["rucksack_vitzland","Rucksack",[("rucksack_vitzland",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  125,weight(2.5)|body_armor(1)|abundance(30),imodbits_cloth],
["rucksack_trezzo","Rucksack",[("rucksack_trezzo",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  125,weight(2.5)|body_armor(1)|abundance(30),imodbits_cloth],
  
#
["upgrade_exo","Exo-Skeleton",[("upgrade_exo",0)],itp_type_foot_armor|itp_attach_armature,0,
  19000,weight(0)|body_armor(20)|leg_armor(10)|abundance(15),imodbits_armor],
#

################
##Barbed Wire###
################
##Entenaii Empire
["cloak_emperor", "Emperor Cloak", [("cloak_emperor",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  2000 , weight(1)|head_armor(5)|body_armor(20)|leg_armor(10) ,imodbits_cloth,[], ],
["extra_armour_entenaii","Entenaii_Extra_Armour_Plate",[("extra_armour_entenaii",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  600,weight(4.5)|body_armor(8),imodbits_armor],

##Entenaii Dominion
["cloak_fanatic", "Fanatic_Cloak", [("dominion_fanatic_cloak",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  1000 , weight(1)|head_armor(5)|body_armor(10)|leg_armor(5) ,imodbits_cloth,[], ],
["extra_armour_dominion","Dominion_Extra_Armour_Plate",[("extra_armour_dominion",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  600,weight(4.5)|body_armor(8),imodbits_armor],

##Kingdom of Galvae
["cloak_royal", "Royal Cloak", [("BL_coat19c",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  2000 , weight(1)|head_armor(5)|body_armor(20)|leg_armor(10) ,imodbits_cloth,[], ],
#
["cloak_noble_1", "Noble Cloak", [("BL_coat11c",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  500 , weight(2)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,],
["cloak_noble_2", "Noble Cloak", [("BL_coat12b",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  500 , weight(2)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,],
["cloak_noble_3", "Noble_Cloak", [("BL_coat03c",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  580 , weight(2)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,[], ],
["cloak_noble_4", "Noble_Cloak", [("BL_coat06b",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  580 , weight(2)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,[], ],
["cloak_noble_5", "Noble_Cloak", [("BL_coat06c",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  580 , weight(2)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,[], ],
["cloak_noble_6", "Noble_Cloak", [("BL_coat08c",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  580 , weight(2)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,[], ],
["cloak_noble_7", "Noble_Cloak", [("BL_coat09b",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  580 , weight(2)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,[], ],
["cloak_noble_8", "Noble_Cloak", [("BL_coat16",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  580 , weight(1)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,[], ],
["cloak_noble_9", "Noble_Cloak", [("BL_coat14b",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,[], ],
["cloak_noble_10", "Noble_Cloak", [("BL_coat03b",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  193 , weight(2)|abundance(100)|head_armor(1)|body_armor(5)|leg_armor(3) ,imodbits_cloth ],
["cloak_noble_11", "Noble_Cloak", [("BL_coat03b",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  580 , weight(2)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,[], ],
["cloak_noble_12", "Noble_Cloak", [("BL_coat01b",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,[], ],
["cloak_noble_13", "Noble_Cloak", [("BL_coat01c",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,[], ],
["cloak_noble_14", "Noble_Cloak", [("BL_coat02b",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,[], ],
["cloak_noble_15", "Noble_Cloak", [("BL_coat02c",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  580 , weight(1)|abundance(50)|head_armor(1)|body_armor(10)|leg_armor(5) ,imodbits_cloth,[], ],
#
["cloak_1", "Cloak", [("BL_coat12",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian|itp_merchandise,0, 
  200,weight(1)|abundance(80)|head_armor(0)|body_armor(5)|leg_armor(5),imodbits_cloth,],
["cloak_2", "Cloak", [("BL_coat14",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian|itp_merchandise,0, 
  200,weight(1)|abundance(80)|head_armor(0)|body_armor(5)|leg_armor(5),imodbits_cloth,],
["cloak_3", "Cloak", [("BL_coat19",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian|itp_merchandise,0, 
  200,weight(1)|abundance(80)|head_armor(0)|body_armor(5)|leg_armor(5),imodbits_cloth,],
["cloak_4", "Cloak", [("BL_coat011",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian|itp_merchandise,0, 
  200,weight(1)|abundance(80)|head_armor(0)|body_armor(5)|leg_armor(5),imodbits_cloth,],
["cloak_5", "Cloak", [("BL_coat03",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian|itp_merchandise,0, 
  200,weight(1)|abundance(80)|head_armor(0)|body_armor(5)|leg_armor(5),imodbits_cloth,],
["cloak_6", "Cloak", [("BL_coat011",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian|itp_merchandise,0, 
  200,weight(1)|abundance(80)|head_armor(0)|body_armor(5)|leg_armor(5),imodbits_cloth,],
["cloak_7", "Cloak", [("BL_coat01",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian|itp_merchandise,0, 
  200,weight(1)|abundance(80)|head_armor(0)|body_armor(5)|leg_armor(5),imodbits_cloth,],
["cloak_8", "Cloak", [("BL_coat02",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian|itp_merchandise,0, 
  200,weight(1)|abundance(80)|head_armor(0)|body_armor(5)|leg_armor(5),imodbits_cloth,],
["cloak_9", "Cloak", [("BL_coat04",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian|itp_merchandise,0, 
  200,weight(1)|abundance(80)|head_armor(0)|body_armor(5)|leg_armor(5),imodbits_cloth,],
["cloak_10", "Cloak", [("BL_coat13",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian|itp_merchandise,0, 
  200,weight(1)|abundance(80)|head_armor(0)|body_armor(5)|leg_armor(5),imodbits_cloth,],
#
["extra_armour_galvae","Galvae_Extra_Armour_Plate",[("extra_armour_galvae",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  600,weight(4.5)|body_armor(8),imodbits_armor],

##Molvat-Berchav Union
["extra_armour_union","Union_Extra_Armour_Plate",[("extra_armour_union",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  600,weight(4.5)|body_armor(8),imodbits_armor],

##Vitzland Territories
["extra_armour_vitzland_1","Vitzland_Extra_Armour_Plate",[("extra_armour_vitzland_1",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  600,weight(4.5)|body_armor(8),imodbits_armor],
["extra_armour_vitzland_2","Vitzland_Trench_Raider_Extra_Armour_Plate",[("extra_armour_vitzland_2",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  600,weight(4.5)|body_armor(8),imodbits_armor],

##Trezzo Republic
["extra_armour_republican","Republican_Extra_Armour_Plate",[("extra_armour_republican",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  600,weight(4.5)|body_armor(8),imodbits_armor],

##Itami Castedom
["extra_armour_itami","Itami_Extra_Armour_Plate",[("extra_armour_itami",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  600,weight(4.5)|body_armor(8),imodbits_armor],
["itami_amura_black_pads","Itami_Amura_Armour_Pads",[("itami_amura_black_pads",0)],itp_type_foot_armor|itp_attach_armature,0,
  1500,weight(1.5)|body_armor(12),imodbits_armor],
["itami_amura_red_pads","Itami_Amura_Armour_Pads",[("itami_amura_red_pads",0)],itp_type_foot_armor|itp_attach_armature,0,
  1000,weight(1.5)|body_armor(10),imodbits_armor],

##Bashide Confederacy
["extra_armour_bashide","Bashide_Extra_Armour_Plate",[("extra_armour_bashide",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  600,weight(4.5)|body_armor(8),imodbits_armor],

##Renegades
["capelet_grey", "Grey_Capelet", [("capelet_grey",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian|itp_merchandise,0, 
  210,weight(1)|abundance(80)|head_armor(5)|body_armor(5),imodbits_cloth,],
["extra_armour","Extra_Armour_Plate",[("extra_armour",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  600,weight(4.5)|body_armor(8),imodbits_armor],

##Theocracy of Throd
["extra_armour_throd","Throd_Extra_Armour_Plate",[("extra_armour",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  600,weight(4.5)|body_armor(8),imodbits_armor],

#other
["boar_cloak", "Boar_Cloak", [("BL_boar_fur",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  300 , weight(1.5)|abundance(10)|head_armor(0)|body_armor(15)|leg_armor(0)|difficulty(4) ,imodbits_cloth,[],],
["jackal_cloak", "Jackal_Cloak", [("jackal_cloak",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  300 , weight(1.5)|abundance(10)|head_armor(0)|body_armor(15)|leg_armor(0)|difficulty(4) ,imodbits_cloth,[],],
["wolf_cloak", "Wolf_Cloak", [("wolf_cloak",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  300 , weight(1.5)|abundance(10)|head_armor(0)|body_armor(15)|leg_armor(0)|difficulty(4) ,imodbits_cloth,[],],

["white_fur_collar", "White_Fur_Collar", [("white_fur_collar",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian|itp_merchandise,0, 
  100 , weight(0.5)|abundance(40)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(4) ,imodbits_cloth,[],],
["slave_neck_chain", "Slave_Chain", [("slave_neck_chain",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian,0, 
  1 , weight(50)|head_armor(2)|body_armor(2)|leg_armor(0)|difficulty(4) ,imodbits_none,[],],

["leather_capelet", "Leather_Capelet", [("leather_capelet",0)], itp_type_foot_armor|itp_attach_armature|itp_civilian|itp_merchandise,0, 
  210,weight(1)|abundance(80)|head_armor(5)|body_armor(5),imodbits_cloth,],
["extra_armour_cult","Cultist_Extra_Armour_Plate",[("extra_armour_cult",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  600,weight(4.5)|body_armor(8),imodbits_armor],


#auxillary
["aux_armour_1","Knees and Elbow Pads",[("metal_knee_and_elbow_pads",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  125,weight(2.5)|body_armor(5),imodbits_armor],
["medic_pack","Medic_Pack",[("medic_pack",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  125,weight(2.5)|body_armor(1),imodbits_armor],


["extra_armour_outlaw_1","Extra_Armour_Plate",[("extra_armour_outlaw_1",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  600,weight(4.5)|body_armor(8),imodbits_armor],
["extra_armour_outlaw_2","Extra_Armour_Plate",[("extra_armour_outlaw_2",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  600,weight(4.5)|body_armor(9),imodbits_armor],
["extra_armour_outlaw_3","Extra_Armour_Plate",[("extra_armour_outlaw_3",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  600,weight(4.5)|body_armor(10),imodbits_armor],

#ammo_belts
["ammo_belt_1","Ammo Belt",[("bandolier_neck_1",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  125,weight(2.5)|body_armor(5),imodbits_armor],
["ammo_belt_2","Ammo Belt",[("bandolier_shoulder_1",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  125,weight(2.5)|body_armor(5),imodbits_armor],
["ammo_belt_3","Ammo Belt",[("bandolier_shoulder_2",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  125,weight(2.5)|body_armor(5),imodbits_armor],
["ammo_belt_4","Ammo Belt",[("bandolier_shoulder_3",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  125,weight(2.5)|body_armor(5),imodbits_armor],

["ammo_belt_5","Ammo Belt",[("bandolier_outlaw",0)],itp_type_foot_armor|itp_attach_armature|itp_merchandise,0,
  125,weight(2.5)|body_armor(8),imodbits_armor],


#flamethrower_backpacks
["flamethrower_backpack","Flamethrower_Backpack",[("m2backpack",0),("m2backpack",ixmesh_inventory)],itp_type_foot_armor|itp_attach_armature,0,
  350,weight(5)|body_armor(10),imodbits_armor],
["flamethrower_backpack_union","Union_Flamethrower_Backpack",[("roks_backpack",0),("roks_backpack",ixmesh_inventory)],itp_type_foot_armor|itp_attach_armature,0,
  350,weight(5)|body_armor(10),imodbits_armor],
#
###################################################################################
##BODYSLOT##
##################################################################################
["army_shirt_1","Army_Shirt", [("shirtb", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  875, weight(3.5)|body_armor(15)|leg_armor(20), imodbits_cloth, []],

#civ
["doctor","Surgeon's_Outfit", [("doctor", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  500, weight(1.5)|body_armor(10)|leg_armor(10), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@shoes_brown"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@shoes_black"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],

["fisher","Crafter_Suit", [("fisher", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  875, weight(3.5)|body_armor(15)|leg_armor(20), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@shoes_brown"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@shoes_black"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["fisher_2","Crafter_Suit", [("fisher_2", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  875, weight(3.5)|body_armor(15)|leg_armor(20), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@shoes_brown"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@shoes_black"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["fisher_3","Crafter_Suit", [("fisher_3", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  875, weight(3.5)|body_armor(15)|leg_armor(20), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@shoes_brown"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@shoes_black"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["frock_1","Fancy_Frock_Coat", [("frock_1", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  900, weight(3)|body_armor(15)|leg_armor(12), imodbits_cloth,[
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@shoes_brown"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@shoes_black"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["frock_2","Simple_Frock_Coat", [("frock_2", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  675, weight(3)|body_armor(15)|leg_armor(12), imodbits_cloth,[
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@shoes_brown"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@shoes_black"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],

#totem
["jackal_tattoo_1","Jackal_Tattoos", [("jackal_tattoo", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  375, weight(1.5)|body_armor(10)|leg_armor(20), imodbits_cloth, []],
["jackal_tattoo_2","Jackal_Tattoos", [("jackal_top_2", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  375, weight(1.5)|body_armor(10)|leg_armor(20), imodbits_cloth, []],

["boar_tattoo_1","Boar_Tattoos", [("boar_tattoo", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  375, weight(1.5)|body_armor(10)|leg_armor(20), imodbits_cloth, []],
  
["bear_tattoo_1","Bear_Tattoos", [("bear_tattoo", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  375, weight(1.5)|body_armor(10)|leg_armor(20), imodbits_cloth, []],

["goat_tattoo_1","Goat_Tattoos", [("goat_tattoo", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  375, weight(1.5)|body_armor(10)|leg_armor(20), imodbits_cloth, []],

["wolf_tattoo_1","Wolf_Tattoos", [("wolf_tattoo", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  375, weight(1.5)|body_armor(10)|leg_armor(20), imodbits_cloth, []],
#

["mechanic","Mechanic suit", [("mechanic", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  750, weight(3)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 3),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string, s11,"@shoes_brown"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string, s11,"@shoes_black"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string, s11,"@shoes_converse"),
        (try_end),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@shoes_brown"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["mechanic_blue","Mechanic suit", [("mechanic_blue", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  750, weight(3)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 3),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string, s11,"@shoes_brown"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string, s11,"@shoes_black"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string, s11,"@shoes_converse"),
        (try_end),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@shoes_brown"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["mechanic_brown","Mechanic suit", [("mechanic_brown", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  750, weight(3)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 3),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string, s11,"@shoes_brown"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string, s11,"@shoes_black"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string, s11,"@shoes_converse"),
        (try_end),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@shoes_brown"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["mechanic_green","Mechanic suit", [("mechanic_green", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  750, weight(3)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 3),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string, s11,"@shoes_brown"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string, s11,"@shoes_black"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string, s11,"@shoes_converse"),
        (try_end),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@shoes_brown"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["mechanic_red","Mechanic suit", [("mechanic_red", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  750, weight(3)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 3),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string, s11,"@shoes_brown"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string, s11,"@shoes_black"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string, s11,"@shoes_converse"),
        (try_end),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@shoes_brown"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],

["robe_1","Robe",[("robe_1",0),("robe_diry_1",imodbit_tattered|imodbit_ragged)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  250,weight(2.5)|body_armor(10)|leg_armor(10),imodbits_cloth],
["robe_2","Robe",[("robe_2",0),("robe_diry_2",imodbit_tattered|imodbit_ragged)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  250,weight(2.5)|body_armor(10)|leg_armor(10),imodbits_cloth],
["robe_3","Robe",[("robe_3",0),("robe_diry_3",imodbit_tattered|imodbit_ragged)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  250,weight(2.5)|body_armor(10)|leg_armor(10),imodbits_cloth],
["robe_4","Robe",[("robe_4",0),("robe_diry_4",imodbit_tattered|imodbit_ragged)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  250,weight(2.5)|body_armor(10)|leg_armor(10),imodbits_cloth],
["robe_5","Robe",[("robe_5",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1250,weight(2.5)|body_armor(10)|leg_armor(10),imodbits_cloth],
["robe_6","Robe",[("robe_6",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  250,weight(2.5)|body_armor(10)|leg_armor(10),imodbits_cloth],
["robe_armoured_rusty_1","Scrap Breastplate Robe",[("robe_armoured_rusty_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  650,weight(14.5)|body_armor(30)|leg_armor(12),imodbits_armor],
["robe_armoured_1","Metal Breastplate Robe",[("robe_armoured_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1950,weight(12.5)|body_armor(40)|leg_armor(15),imodbits_armor],
  
["robe_armoured_heavy_white","White Robe with Heavy Armor", [("robe_armoured_heavy_white", 0)], itp_type_body_armor|itp_covers_legs, 0,
  4200, weight(13)|abundance(10)|body_armor(40)|leg_armor(20), imodbits_armor],
["robe_armoured_heavy_red","Red Robe with Heavy Armor", [("robe_armoured_heavy_red", 0)], itp_type_body_armor|itp_covers_legs, 0,
  4200, weight(13)|abundance(10)|body_armor(40)|leg_armor(20), imodbits_armor],
["robe_armoured_heavy_purple","Purple Robe with Heavy Armor", [("robe_armoured_heavy_purple", 0)], itp_type_body_armor|itp_covers_legs, 0,
  12200, weight(13)|abundance(1)|body_armor(50)|leg_armor(30), imodbits_armor],

["sloppy_trench_coat","Trench_Coat", [("sloppy_trench_coat", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],

["tavern_apron","Shirt_with_Apron", [("tavern_apron", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  250, weight(2)|body_armor(10)|leg_armor(10), imodbits_cloth,[
    (ti_on_init_item, [
      (str_store_string, s11,"@boots_1"),
      (cur_item_add_mesh, s11),]),]],

#women
["dress_1","Dress",[("dress_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(1.5)|body_armor(10)|leg_armor(10),imodbits_cloth,[
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_3"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_4"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["dress_2","Dress",[("dress_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(1.5)|body_armor(10)|leg_armor(10),imodbits_cloth,[
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_3"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_4"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["dress_3","Dress",[("dress_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(1.5)|body_armor(10)|leg_armor(10),imodbits_cloth,[
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_3"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_4"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["dress_4","Dress",[("dress_4",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(1.5)|body_armor(10)|leg_armor(10),imodbits_cloth,[
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_3"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_4"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["dress_5","Dress",[("dress_5",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(1.5)|body_armor(10)|leg_armor(10),imodbits_cloth,[
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_3"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_4"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],

["women_robe_1","Robe",[("women_robe_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(1.5)|body_armor(10)|leg_armor(10),imodbits_cloth,[
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_5"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["women_robe_2","Robe",[("women_robe_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(1.5)|body_armor(10)|leg_armor(10),imodbits_cloth,[
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_5"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["women_robe_3","Robe",[("women_robe_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(1.5)|body_armor(10)|leg_armor(10),imodbits_cloth,[
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_5"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["women_robe_4","Robe",[("women_robe_4",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(1.5)|body_armor(10)|leg_armor(10),imodbits_cloth,[
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_5"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["women_robe_5","Robe",[("women_robe_5",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(1.5)|body_armor(10)|leg_armor(10),imodbits_cloth,[
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_5"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],
["women_robe_6","Robe",[("women_robe_6",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(1.5)|body_armor(10)|leg_armor(10),imodbits_cloth,[
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_5"),
        (cur_item_add_mesh, s11),
      (try_end),]),]],

##################################################################################
##FACTIONS##
##################################################################################

##Entenaii Empire ##
["entenaii_uniform_levy","Entenaii Empire Levy Uniform",[("entenaii_uniform",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(2)|abundance(100)|body_armor(10)|leg_armor(10),imodbits_cloth,[]],
["entenaii_uniform_private","Entenaii Empire Uniform",[("entenaii_uniform_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  200,weight(3)|abundance(90)|body_armor(15)|leg_armor(15),imodbits_cloth,[]],
["entenaii_uniform_private_2nd","Entenaii Empire Private Uniform",[("entenaii_uniform_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  400,weight(10)|abundance(90)|body_armor(18)|leg_armor(16),imodbits_cloth,[]],
["entenaii_uniform_private_1st","Entenaii Empire Private Uniform",[("entenaii_uniform_4",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  600,weight(10)|abundance(80)|body_armor(20)|leg_armor(18),imodbits_cloth,[]],
["entenaii_uniform_specialist","Entenaii Empire Specialist Uniform",[("entenaii_uniform_specialist",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(10)|abundance(100)|body_armor(15)|leg_armor(15),imodbits_cloth,[]],
["entenaii_uniform_sergeant","Entenaii Empire Uniform",[("entenaii_uniform_6",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  800,weight(12)|abundance(50)|body_armor(20)|leg_armor(15),imodbits_cloth,[]],
["entenaii_uniform_cavalry","Entenaii Empire Cavalry Uniform",[("entenaii_cuirass_cavalry",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1000,weight(12)|abundance(50)|body_armor(30)|leg_armor(30)|difficulty(8),imodbits_armor,[]],
["entenaii_uniform_raider","Entenaii Empire Uniform",[("entenaii_uniform_5",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(12)|abundance(50)|body_armor(25)|leg_armor(20),imodbits_cloth,[]],
["entenaii_uniform_officer","Entenaii Empire Officer Uniform",[("entenaii_coat",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1500,weight(12)|abundance(20)|body_armor(20)|leg_armor(15),imodbits_cloth,[]],
["entenaii_uniform_officer_2","Entenaii Empire Officer Uniform",[("entenaii_coat_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1500,weight(12)|abundance(20)|body_armor(20)|leg_armor(15),imodbits_cloth,[]],
["entenaii_uniform_guard","Entenaii Empire Guard Cuirass",[("entenaii_cuirass",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(30)|leg_armor(15)|difficulty(8),imodbits_armor,[]],

["entenaii_armour","Entenaii Empire Armour",[("entenaii_full_plate",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(45)|leg_armor(45)|difficulty(12),imodbits_armor,[]],
["entenaii_armour_officer","Entenaii Empire Officer Armour",[("entenaii_full_plate_2",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(50)|leg_armor(50)|difficulty(15),imodbits_armor,[]],

["entenaii_uniform_parade","Entenaii Empire Parade Uniform",[("entenaii_parade_uniform",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1000,weight(12)|abundance(10)|body_armor(20)|leg_armor(15)|difficulty(4),imodbits_cloth,[]],
["entenaii_uniform_noble","Entenaii Empire Noble Uniform",[("entenaii_coat_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  3850,weight(14)|body_armor(24)|leg_armor(18),imodbits_cloth,[]],
#
["entenaii_automaton_body","Soldier_Automaton",[("s_automaton",0)],itp_type_body_armor|itp_covers_legs|itp_covers_head|itp_civilian|itp_unique,0,
  10000,weight(40)|head_armor(45)|body_armor(45)|leg_armor(45)|difficulty(20),imodbits_armor,[]],
["entenaii_automaton_heavy_body","Heavy_Soldier_Automaton",[("h_automaton",0)],itp_type_body_armor|itp_covers_legs|itp_covers_head|itp_civilian|itp_unique,0,
  40000,weight(50)|head_armor(65)|body_armor(65)|leg_armor(65)|difficulty(20),imodbits_armor,[]],

#
["entenaii_uniform_yeneral","Entenaii_Empire_Yeneral_Uniform",[("entenaii_uniform_yeneral",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  4000,weight(14)|body_armor(25)|leg_armor(20),imodbits_cloth,[]],
#
["entenaii_uniform_emperor","Emperor_Uniform",[("entenaii_uniform_emperor",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique,0,
  14500,weight(9)|body_armor(38)|leg_armor(32),imodbits_cloth,[]],
["entenaii_armour_emperor","Emperor_Armour",[("entenaii_armour_emperor",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,
  20000,weight(31)|body_armor(55)|leg_armor(55)|difficulty(15),imodbits_armor,[]],
  
##Entenaii Dominion
["dominion_uniform_levy","Dominion_Militia_Levy_Uniform",[("dominion_uniform_levy",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(2)|abundance(100)|body_armor(10)|leg_armor(10),imodbits_cloth,[]],
["dominion_uniform_recruit","Dominion_Militia_Recruit_Uniform",[("dominion_uniform_recruit",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  200,weight(3)|abundance(90)|body_armor(12)|leg_armor(10),imodbits_cloth,[]],
["dominion_uniform_yeoman","Dominion_Militia_Yeoman_Uniform",[("dominion_uniform_yeoman",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  400,weight(4)|abundance(80)|body_armor(15)|leg_armor(12),imodbits_cloth,[]],
["dominion_uniform_infantry","Dominion_Militia_Regular_Uniform",[("dominion_uniform_infantry",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  600,weight(5)|abundance(70)|body_armor(17)|leg_armor(15),imodbits_cloth,[]],
["dominion_uniform_veteran","Dominion_Militia_Veteran_Uniform",[("dominion_uniform_veteran",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  800,weight(6)|abundance(60)|body_armor(20)|leg_armor(15),imodbits_cloth,[]],
#
["dominion_uniform_officer","Dominion_Militia_Officer_Uniform",[("dominion_uniform_officer",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1500,weight(8)|abundance(40)|body_armor(25)|leg_armor(17),imodbits_cloth,[]],
#
["dominion_uniform_rough_rider","Dominion_Militia_Rough-rider_Uniform",[("dominion_uniform_rough_rider",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  4000,weight(15)|abundance(50)|body_armor(30)|leg_armor(30)|difficulty(8),imodbits_armor,[]],


["dominion_uniform_fanatic_noble", "Dominion Fanatic Noble Uniform", [("dominion_uniform_fanatic_noble",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  11000 , weight(10)|abundance(1)|body_armor(40)|leg_armor(40),imodbits_cloth,[]],
#
["dominion_uniform_prison_guard","Dominion_Prison_Guard_Cuirass",[("dominion_uniform_prison_guard",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  2000,weight(13)|abundance(20)|body_armor(30)|leg_armor(15)|difficulty(8),imodbits_armor,[]],
["dominion_uniform_guard","Dominion_Guard_Cuirass",[("dominion_uniform_guard",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  3000,weight(15)|abundance(20)|body_armor(34)|leg_armor(20)|difficulty(9),imodbits_armor,[]],
["dominion_uniform_viceregal_guard","Dominion_Viceregal_Guard_Cuirass",[("dominion_uniform_viceregal_guard",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(38)|leg_armor(25)|difficulty(10),imodbits_armor,[]],
#
["dominion_armour","Dominion_Militia_Armour",[("dominion_armour",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(26)|abundance(10)|body_armor(45)|leg_armor(45)|difficulty(12),imodbits_armor,[]],
["dominion_armour_officer","Dominion_Officer_Armour",[("dominion_armour_officer",0)],itp_type_body_armor|itp_covers_legs,0,
  15000,weight(28)|abundance(10)|body_armor(50)|leg_armor(50)|difficulty(15),imodbits_armor,[]],
#
["dominion_uniform_fanatic","Dominion Fanatic Uniform",[("dominion_uniform_fanatic",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  700,weight(10)|abundance(50)|body_armor(30)|leg_armor(30),imodbits_cloth,[]],
["dominion_uniform_fanatic_furnacestoker", "Dominion Fanatic Furnacestoker Uniform", [("dominion_uniform_fanatic_furnacestoker",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1500 , weight(10)|abundance(10)|body_armor(32)|leg_armor(32),imodbits_armor,[]],
["dominion_uniform_fanatic_immolator", "Dominion Fanatic Immolator Uniform", [("dominion_uniform_fanatic_immolator",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1750 , weight(10)|abundance(10)|body_armor(36)|leg_armor(36),imodbits_armor,[]],
#
["dominion_condemned_body","Condemned_Body",[("condemned_body",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,
  0,weight(1)|body_armor(70)|leg_armor(70)|head_armor(70)|difficulty(20),imodbits_none,[]],
#
["dominion_uniform_governer_general", "Governer_General_Uniform", [("dominion_uniform_fanatic_noble",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique,0,
  11000 , weight(7)|abundance(1)|body_armor(30)|leg_armor(20),imodbits_cloth,[]],
["dominion_armour_governer_general","Governer_General_Armour",[("dominion_armour_governer_general",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,
  20000,weight(30)|abundance(10)|body_armor(55)|leg_armor(55)|difficulty(15),imodbits_armor,[]],
#

##Kingdom of Galvae
["galvae_uniform_levy","Galvae Levy Uniform",[("galvae_uniform_levy",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(10)|abundance(100)|body_armor(10)|leg_armor(10),imodbits_cloth,[]],
["galvae_uniform_regular","Galvae Uniform",[("galvae_uniform",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(10)|abundance(100)|body_armor(15)|leg_armor(15),imodbits_cloth,[]],
["galvae_uniform_sergeant","Galvae Sergeant Uniform",[("galvae_uniform_guard",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  800,weight(12)|abundance(50)|body_armor(20)|leg_armor(15),imodbits_cloth,[]],
["galvae_uniform_cavalry","Galvae Cavalry Uniform",[("galvae_uniform_cavalry",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  750,weight(12)|abundance(50)|body_armor(20)|leg_armor(15),imodbits_cloth,[]],
["galvae_uniform_raider","Galvae Uniform",[("galvae_uniform_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(12)|abundance(50)|body_armor(25)|leg_armor(20),imodbits_cloth,[]],
["galvae_uniform_officer","Galvae Officer Uniform",[("galvae_uniform_officer",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  3500,weight(12)|abundance(20)|body_armor(20)|leg_armor(15),imodbits_cloth,[]],
["galvae_uniform_guard","Galvae Guard Cuirass",[("galvae_cuirass_guard",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(30)|leg_armor(15)|difficulty(8),imodbits_armor,[]],
["galvae_uniform_officer_cuirass","Galvae Officer Cuirass",[("galvae_cuirass_officer",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(30)|leg_armor(15)|difficulty(8),imodbits_armor,[]],
["galvae_armour","Galvae Armour",[("galvae_armour",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(45)|leg_armor(45)|difficulty(12),imodbits_armor,[]],
["galvae_armour_officer","Galvae Officer Armour",[("galvae_armour_officer",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(50)|leg_armor(50)|difficulty(15),imodbits_armor,[]],
["galvae_armour_cavalry","Galvae Cavalry Cuirass",[("galvae_cuirass_cavalry",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1000,weight(18)|abundance(50)|body_armor(27)|leg_armor(20)|difficulty(8),imodbits_armor,[]],
["galvae_ossi","Galvae Ossi", [("ossi", 0)], itp_type_body_armor|itp_covers_legs|itp_covers_head|itp_doesnt_cover_hair|itp_civilian|itp_unique, 0,
  0, weight(1)|head_armor(55)|body_armor(75)|leg_armor(55), imodbits_armor, []],
#
["galvae_uniform_royal","Royal_Uniform",[("galvae_uniform_officer",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique,0,
  13500,weight(12)|abundance(20)|body_armor(30)|leg_armor(25),imodbits_cloth,[]],
["galvae_armour_royal","Royal_Armour",[("galvae_armour_officer",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,
  10000,weight(30)|abundance(10)|body_armor(55)|leg_armor(55)|difficulty(15),imodbits_armor,[]],


##Molvat-Berchav Union
["union_uniform_levy","Union Levy Uniform",[("union_uniform_levy",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(10)|abundance(100)|body_armor(10)|leg_armor(10),imodbits_cloth,[]],
["union_uniform_regular","Union_Recruit_Uniform",[("union_uniform",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  300,weight(10)|abundance(100)|body_armor(15)|leg_armor(15),imodbits_cloth,[]],
["union_uniform_yeoman","Union_Yeoman_Uniform",[("union_uniform_yeoman",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  500,weight(10)|abundance(100)|body_armor(20)|leg_armor(15),imodbits_cloth,[]],
["union_uniform_light_infantry","Union_Light_Infantry_Uniform",[("union_uniform_infantry",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  850,weight(10)|abundance(100)|body_armor(18)|leg_armor(18),imodbits_cloth,[]],
["union_uniform_rifleman","Union_Rifleman_Uniform",[("union_uniform_rifleman",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  1000,weight(10)|abundance(100)|body_armor(20)|leg_armor(20),imodbits_cloth,[]],
["union_uniform_sergeant","Union Sergeant Uniform",[("union_uniform_sergeant",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  800,weight(12)|abundance(50)|body_armor(20)|leg_armor(15),imodbits_cloth,[]],
["union_uniform_cavalry","Union Culsar Uniform",[("union_uniform_hussar",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  650,weight(12)|abundance(50)|body_armor(25)|leg_armor(20),imodbits_cloth,[]],
["union_uniform_raider","Union_Raider_Uniform",[("union_uniform_stormtrooper",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(12)|abundance(50)|body_armor(25)|leg_armor(20),imodbits_cloth,[]],
["union_uniform_sniper","Union_Snowstalker_Uniform",[("union_snowstalker",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  800,weight(12)|abundance(30)|body_armor(25)|leg_armor(20),imodbits_cloth,[]],
["union_uniform_officer","Union Hetman Uniform",[("union_uniform_officer",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  3500,weight(12)|abundance(20)|body_armor(20)|leg_armor(15),imodbits_cloth,[]],
["union_uniform_guard","Union Guard Cuirass",[("union_uniform_cuirass",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(30)|leg_armor(15)|difficulty(8),imodbits_armor,[]],

["union_uniform_cavalry_cuirass","Union Culsar Cuirass",[("union_cuirass_hussar",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(30)|leg_armor(15)|difficulty(8),imodbits_armor,[]],
["union_uniform_cavalry_vet_cuirass","Union Veteran Culsar Cuirass",[("union_cuirass_vet_hussar",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  6000,weight(18)|abundance(15)|body_armor(35)|leg_armor(18)|difficulty(8),imodbits_armor,[]],

#
["union_armour","Union Armour",[("union_armour",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(45)|leg_armor(45)|difficulty(12),imodbits_armor,[]],
["union_armour_brotherhood","Union Brotherhood Armour",[("union_armour_brotherhood",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(45)|leg_armor(45)|difficulty(12),imodbits_armor,[]],
["union_armour_officer","Union Hetman Armour",[("union_armour_officer",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(50)|leg_armor(50)|difficulty(15),imodbits_armor,[]],
#
["union_uniform_marine","Union_Marine_Uniform",[("marine_uniform",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1000,weight(10)|abundance(20)|body_armor(28)|leg_armor(22),imodbits_cloth,[]],
["union_uniform_marine_cuirass","Union_Marine_Cuirass",[("marine_uniform_cuirass",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(16)|abundance(10)|body_armor(34)|leg_armor(25)|difficulty(8),imodbits_armor,[]],
#
["union_ravga_armour","Union Ravga Uniform",[("union_uniform_stormtrooper",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique,0,
  500,weight(12)|abundance(50)|body_armor(25)|leg_armor(20),imodbits_cloth,[]],
#
["union_uniform_tzar","Tzar_Uniform",[("union_uniform_officer",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique,0,
  13500,weight(12)|abundance(20)|body_armor(30)|leg_armor(25),imodbits_cloth,[]],
["union_armour_tzar","Tzar_Armour",[("union_armour_bear",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,
  20000,weight(30)|abundance(10)|body_armor(55)|leg_armor(55)|difficulty(15),imodbits_armor,[]],

##Vitzland Territories
["vitzland_uniform_levy","Vitzland Levy Uniform",[("vitzland_uniform_levy",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(10)|abundance(100)|body_armor(10)|leg_armor(10),imodbits_cloth,[]],
["vitzland_uniform_regular","Vitzland Uniform",[("vitzland_uniform",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(10)|abundance(100)|body_armor(15)|leg_armor(15),imodbits_cloth,[]],
["vitzland_uniform_sergeant","Vitzland Sergeant Uniform",[("vitzland_uniform",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  800,weight(12)|abundance(50)|body_armor(20)|leg_armor(15)|difficulty(4),imodbits_cloth,[]],
["vitzland_uniform_cavalry","Vitzland Cavalry Uniform",[("vitzland_uniform_cavalry",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  650,weight(12)|abundance(50)|body_armor(25)|leg_armor(20)|difficulty(5),imodbits_cloth,[]],
["vitzland_uniform_raider","Vitzland Uniform",[("vitzland_uniform_lifeguard",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(12)|abundance(50)|body_armor(25)|leg_armor(20)|difficulty(5),imodbits_cloth,[]],
["vitzland_uniform_gunner","Vitzland_Gunner_Uniform",[("vitzland_uniform_gunner",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(12)|abundance(50)|body_armor(25)|leg_armor(20)|difficulty(5),imodbits_cloth,[]],
  
["vitzland_uniform_officer","Vitzland Officer Uniform",[("vitzland_uniform_officer",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  3500,weight(12)|abundance(20)|body_armor(20)|leg_armor(15)|difficulty(5),imodbits_cloth,[]],
["vitzland_uniform_guard","Vitzland Guard Cuirass",[("vitzland_uniform_cuirass",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(30)|leg_armor(15)|difficulty(8),imodbits_armor,[]],
["vitzland_uniform_cavalry_cuirass","Vitzland Cavalry Cuirass",[("vitzland_uniform_cuirass_cav",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(30)|leg_armor(15)|difficulty(8),imodbits_armor,[]],
["vitzland_uniform_officer_cuirass","Vitzland Officer Cuirass",[("vitzland_uniform_cuirass_officer",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(30)|leg_armor(15)|difficulty(8),imodbits_armor,[]],
#
["vitzland_armour","Vitzland Armour",[("vitzland_armour",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(45)|leg_armor(45)|difficulty(12),imodbits_armor,[]],
["vitzland_armour_officer","Vitzland Officer Armour",[("vitzland_armour_noble",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(50)|leg_armor(50)|difficulty(15),imodbits_armor,[]],
["vitzland_armour_cavalry","Vitzland Cavalry Armour",[("vitzland_armour_cav",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(45)|leg_armor(45)|difficulty(12),imodbits_armor,[]],
#
["vitzland_landansquet_1","Vitzland_Landansquet_Cuirass",[("vitzland_landansquet_1",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(21)|abundance(2)|body_armor(40)|leg_armor(38)|difficulty(10),imodbits_armor,[]],
["vitzland_landansquet_2","Vitzland_Landansquet_Light_Armour",[("vitzland_landansquet_2",0)],itp_type_body_armor|itp_covers_legs,0,
  12000,weight(23)|abundance(3)|body_armor(45)|leg_armor(42)|difficulty(11),imodbits_armor,[]],
["vitzland_landansquet_3","Vitzland_Landansquet_Heavy_Armour",[("vitzland_landansquet_3",0)],itp_type_body_armor|itp_covers_legs,0,
  15000,weight(25)|abundance(4)|body_armor(48)|leg_armor(45)|difficulty(12),imodbits_armor,[]],
#
["vitzland_nactman_armour","Nactman_Armour", [("nactman_armour", 0)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_civilian|itp_unique, 0,
  0, weight(1)|head_armor(30)|body_armor(40)|leg_armor(20), imodbits_armor, []],
#
["vitzland_uniform_kaiser","Kaiser_Uniform",[("vitzland_kaiser_outfit",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique,0,
  13500,weight(12)|abundance(20)|body_armor(30)|leg_armor(25)|difficulty(5),imodbits_cloth,[]],
["vitzland_armour_kaiser","Kaiser_Armour",[("vitzland_armour_kaiser",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,
  20000,weight(30)|abundance(10)|body_armor(55)|leg_armor(55)|difficulty(15),imodbits_armor,[]],

##Trezzo Republic
["republican_uniform_levy","Republican Levy Uniform",[("republican_uniform_levy",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(10)|abundance(100)|body_armor(10)|leg_armor(10),imodbits_cloth,[]],
["republican_uniform_regular","Republican Uniform",[("republican_uniform",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(10)|abundance(100)|body_armor(15)|leg_armor(15),imodbits_cloth,[]],
["republican_uniform_sergeant","Republican Veteran Uniform",[("republican_uniform_cleric",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  800,weight(12)|abundance(50)|body_armor(20)|leg_armor(15)|difficulty(4),imodbits_cloth,[]],
["republican_uniform_cavalry","Republican Cavalry Uniform",[("republican_uniform_cavalry",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  650,weight(12)|abundance(50)|body_armor(25)|leg_armor(20)|difficulty(5),imodbits_cloth,[]],
["republican_uniform_raider","Republican Canorale Uniform",[("republican_uniform_guard",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(12)|abundance(50)|body_armor(25)|leg_armor(20)|difficulty(5),imodbits_cloth,[]],
["republican_uniform_officer","Republican Officer Uniform",[("republican_uniform_officer",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  3500,weight(12)|abundance(20)|body_armor(20)|leg_armor(15)|difficulty(5),imodbits_cloth,[]],
["republican_uniform_guard","Republican Vardina Guarde Cuirass",[("republican_uniform_cuirass_guard",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  7000,weight(18)|abundance(20)|body_armor(36)|leg_armor(18)|difficulty(8),imodbits_armor,[]],
["republican_uniform_guard_castle","Republican Caratri Guarde Cuirass",[("republican_uniform_cuirass_guard_castle",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(32)|leg_armor(15)|difficulty(8),imodbits_armor,[]],
["republican_uniform_guard_hall","Republican Bellemeria Guarde Cuirass",[("republican_uniform_cuirass_guard_hall",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  10000,weight(18)|abundance(20)|body_armor(40)|leg_armor(22)|difficulty(8),imodbits_armor,[]],
["republican_uniform_officer_cuirass","Republican Officer Cuirass",[("republican_uniform_cuirass_officer",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(30)|leg_armor(15)|difficulty(8),imodbits_armor,[]],
["republican_armour","Republican Armour",[("republican_armour",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(45)|leg_armor(45)|difficulty(12),imodbits_armor,[]],
["republican_armour_officer","Republican Officer Armour",[("republican_armour_officer",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(50)|leg_armor(50)|difficulty(15),imodbits_armor,[]],
#
["republican_vencudi_uniform_1","Republican_Vencudi_Diti_Uniform",[("republican_vencudi_uniform_1",0)],itp_type_body_armor|itp_covers_legs,0,
  18000,weight(14)|body_armor(38)|leg_armor(40)|difficulty(8),imodbits_armor,[]],
["republican_vencudi_uniform_2","Republican_Vencudi_Becagi_Uniform",[("republican_vencudi_uniform_2",0)],itp_type_body_armor|itp_covers_legs,0,
  22000,weight(17)|body_armor(42)|leg_armor(41)|difficulty(9),imodbits_armor,[]],
["republican_vencudi_uniform_3","Republican_Vencudi_Conkera_Uniform",[("republican_vencudi_uniform_3",0)],itp_type_body_armor|itp_covers_legs,0,
  27000,weight(20)|body_armor(47)|leg_armor(43)|difficulty(10),imodbits_armor,[]],
#
["republican_servo_spider_uniform","Republican Cavalry Uniform",[("republican_uniform_cavalry",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  650,weight(12)|abundance(50)|body_armor(25)|leg_armor(20)|difficulty(5),imodbits_cloth,[]],
#
["republican_uniform_doge","Doge_Uniform",[("republican_uniform_officer",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique,0,
  13500,weight(12)|abundance(20)|body_armor(30)|leg_armor(25)|difficulty(5),imodbits_cloth,[]],
["republican_armour_doge","Doge_Armour",[("republican_armour_doge",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,
  50000,weight(32)|body_armor(75)|leg_armor(60)|difficulty(18),imodbits_armor,[]],

##Itami Castedom
["itami_uniform_levy","Itami Levy Uniform",[("itami_infantry_tosa",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(10)|abundance(100)|body_armor(10)|leg_armor(10),imodbits_cloth,[]],
["itami_uniform_regular","Itami Uniform",[("itami_rifle_tosa",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(10)|abundance(100)|body_armor(15)|leg_armor(15),imodbits_cloth,[]],
["itami_uniform_sergeant","Itami Veteran Uniform",[("itami_infantry_satsuma_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  800,weight(12)|abundance(50)|body_armor(20)|leg_armor(15)|difficulty(4),imodbits_cloth,[]],
["itami_uniform_cavalry","Itami Cavalry Uniform",[("itami_cav_guard_sarge",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  650,weight(12)|abundance(50)|body_armor(25)|leg_armor(20)|difficulty(5),imodbits_cloth,[]],
["itami_uniform_raider","Itami Raider Uniform",[("itami_sapper",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(12)|abundance(50)|body_armor(25)|leg_armor(20)|difficulty(5),imodbits_cloth,[]],
["itami_uniform_officer","Itami Officer Uniform",[("itami_infantry_tosa_officer",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  3500,weight(12)|abundance(20)|body_armor(20)|leg_armor(15)|difficulty(5),imodbits_cloth,[]],
#
["itami_uniform_guard","Itami Guard Cuirass",[("itami_uniform_cuirass_guard",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  7000,weight(18)|abundance(20)|body_armor(36)|leg_armor(18)|difficulty(8),imodbits_armor,[]],
["itami_uniform_guard_castle","Itami Castle Guarde Cuirass",[("itami_uniform_cuirass_guard_castle",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(32)|leg_armor(15)|difficulty(8),imodbits_armor,[]],
["itami_uniform_guard_hall","Itami Hall Guard Cuirass",[("itami_uniform_cuirass_guard_hall",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  10000,weight(18)|abundance(20)|body_armor(40)|leg_armor(22)|difficulty(8),imodbits_armor,[]],
#
["itami_uniform_officer_cuirass","Itami Officer Cuirass",[("itami_uniform_cuirass_guard_castle",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(30)|leg_armor(15)|difficulty(8),imodbits_armor,[]],
["itami_armour","Itami Armour",[("itami_uniform_cuirass_guard_hall",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(45)|leg_armor(45)|difficulty(12),imodbits_armor,[]],
["itami_armour_officer","Itami Officer Armour",[("itami_uniform_cuirass_guard_hall",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(50)|leg_armor(50)|difficulty(15),imodbits_armor,[]],
#
["itami_amura_bloodblade","Itami_Bloodblade_Armour",[("itami_amura_bloodblade",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  15000,weight(25)|body_armor(50)|leg_armor(45)|difficulty(11),imodbits_armor,[]],
["itami_amura_bloodblade_2","Itami_Bloodblade_Armour",[("itami_amura_bloodblade_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  16000,weight(26)|body_armor(51)|leg_armor(46)|difficulty(11),imodbits_armor,[]],
["itami_amura_jetblade","Itami_Jetblade_Armour",[("itami_amura_jetblade",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  18000,weight(28)|body_armor(53)|leg_armor(49)|difficulty(12),imodbits_armor,[]],
["itami_amura_jetblade_2","Itami_Jetblade_Armour",[("itami_amura_jetblade_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  19000,weight(29)|body_armor(54)|leg_armor(50)|difficulty(12),imodbits_armor,[]],
["itami_amura_glassblade","Itami_Glassblade_Armour",[("itami_amura_glassblade",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  22000,weight(30)|body_armor(60)|leg_armor(55)|difficulty(14),imodbits_armor,[]],

#
["itami_uniform_kytra","Kytra_Uniform",[("itami_general",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique,0,
  13500,weight(12)|abundance(20)|body_armor(30)|leg_armor(25)|difficulty(5),imodbits_cloth,[]],
["itami_armour_kytra","Kytra_Armour",[("itami_armour_kytra",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,
  50000,weight(32)|body_armor(75)|leg_armor(60)|difficulty(18),imodbits_armor,[]],

##Bashide Confederacy
["bashide_uniform_levy","Bashide Levy Uniform",[("bashide_militia_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(10)|abundance(100)|body_armor(10)|leg_armor(10),imodbits_cloth,[]],
["bashide_uniform_regular","Bashide Uniform",[("bashide_regular_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(10)|abundance(100)|body_armor(15)|leg_armor(15),imodbits_cloth,[]],
["bashide_uniform_sergeant","Bashide Veteran Uniform",[("bashide_regular_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  800,weight(12)|abundance(50)|body_armor(20)|leg_armor(15)|difficulty(4),imodbits_cloth,[]],
["bashide_uniform_cavalry","Bashide Cavalry Uniform",[("bashide_red",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  650,weight(12)|abundance(50)|body_armor(25)|leg_armor(20)|difficulty(5),imodbits_cloth,[]],
["bashide_uniform_raider","Bashide Raider Uniform",[("bashide_black",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(12)|abundance(50)|body_armor(25)|leg_armor(20)|difficulty(5),imodbits_cloth,[]],
["bashide_uniform_officer","Bashide Officer Uniform",[("bashide_white",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  3500,weight(12)|abundance(20)|body_armor(20)|leg_armor(15)|difficulty(5),imodbits_cloth,[]],
#
["bashide_uniform_guard","Bashide Guard Cuirass",[("bashide_uniform_cuirass_guard",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  7000,weight(18)|abundance(20)|body_armor(36)|leg_armor(18)|difficulty(8),imodbits_armor,[]],
["bashide_uniform_guard_castle","Bashide Castle Guarde Cuirass",[("bashide_uniform_cuirass_guard_castle",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(32)|leg_armor(15)|difficulty(8),imodbits_armor,[]],
["bashide_uniform_guard_hall","Bashide Hall Guard Cuirass",[("bashide_uniform_cuirass_guard_hall",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  10000,weight(18)|abundance(20)|body_armor(40)|leg_armor(22)|difficulty(8),imodbits_armor,[]],
#
["bashide_uniform_officer_cuirass","Bashide Officer Cuirass",[("bashide_uniform_cuirass_guard_castle",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(30)|leg_armor(15)|difficulty(8),imodbits_armor,[]],
["bashide_uniform_cavalry_cuirass","Bashide Cavalry Cuirass",[("bashide_lancer_uniform",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  5000,weight(18)|abundance(20)|body_armor(30)|leg_armor(15)|difficulty(8),imodbits_armor,[]],
["bashide_armour","Bashide Armour",[("bashide_uniform_cuirass_guard_hall",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(45)|leg_armor(45)|difficulty(12),imodbits_armor,[]],
["bashide_armour_officer","Bashide Officer Armour",[("bashide_uniform_cuirass_guard_hall",0)],itp_type_body_armor|itp_covers_legs,0,
  10000,weight(30)|abundance(10)|body_armor(50)|leg_armor(50)|difficulty(15),imodbits_armor,[]],
#
["bashide_uniform_gidon_1","Gidon Uniform",[("bashide_black",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1000,weight(8)|body_armor(30)|leg_armor(28)|difficulty(7),imodbits_cloth,[]],

#
["bashide_uniform_alran","Alran_Uniform",[("bashide_general",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique,0,
  13500,weight(12)|abundance(20)|body_armor(30)|leg_armor(25)|difficulty(5),imodbits_cloth,[]],
["bashide_armour_alran","Alran_Armour",[("bashide_armour_alran",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,
  50000,weight(32)|body_armor(75)|leg_armor(60)|difficulty(18),imodbits_armor,[]],
#

##Renegade
["renegade_uniform_levy","Renegade Levy Uniform",[("renegade_uniform",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(10)|abundance(100)|body_armor(10)|leg_armor(10),imodbits_cloth,[]],
["renegade_uniform_regular","Renegade Uniform",[("renegade_uniform",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(10)|abundance(100)|body_armor(15)|leg_armor(15),imodbits_cloth,[]],
["renegade_uniform_sergeant_1","Renegade Sergeant Uniform",[("renegade_uniform_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  800,weight(12)|abundance(50)|body_armor(20)|leg_armor(15)|difficulty(4),imodbits_cloth,[]],
["renegade_uniform_cavalry_1","Renegade Cavalry Uniform",[("renegade_uniform_cuirass",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  650,weight(12)|abundance(50)|body_armor(25)|leg_armor(20)|difficulty(5),imodbits_armor,[]],
["renegade_uniform_raider_1","Renegade_Raider_Uniform",[("renegade_uniform_4",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  500,weight(12)|abundance(50)|body_armor(22)|leg_armor(18)|difficulty(5),imodbits_cloth,[]],
["renegade_uniform_officer_1","Renegade Officer Uniform",[("renegade_uniform_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  3500,weight(12)|abundance(20)|body_armor(20)|leg_armor(15)|difficulty(5),imodbits_cloth,[]],
["renegade_uniform_guard_1","Renegade Guard Cuirass",[("renegade_uniform_cuirass",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  5000,weight(18)|abundance(20)|body_armor(30)|leg_armor(15)|difficulty(8),imodbits_armor,[]],
["renegade_armour","Renegade Armour",[("renegade_armour",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,
  10000,weight(30)|abundance(10)|body_armor(45)|leg_armor(45)|difficulty(12),imodbits_armor,[]],
["renegade_armour_officer","Renegade Officer Armour",[("renegade_armour_officer",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,
  10000,weight(30)|abundance(10)|body_armor(50)|leg_armor(50)|difficulty(15),imodbits_armor,[]],
["renegade_armour_cavalry","Renegade Cavalry Armour",[("renegade_armour_cavalry",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,
  10000,weight(30)|abundance(10)|body_armor(45)|leg_armor(45)|difficulty(12),imodbits_armor,[]],
["renegade_beastling_armour","Beastling_Armour", [("beastling_2_body", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique, 0,
  0, weight(1)|head_armor(30)|body_armor(40)|leg_armor(20),imodbits_armor, []],
#
["renegade_uniform_leader","Leader_Uniform",[("renegade_uniform_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  12000,weight(12)|abundance(20)|body_armor(28)|leg_armor(22)|difficulty(5),imodbits_cloth,[]],
["renegade_armour_leader","Leader_Armour",[("renegade_armour_officer",0)],itp_type_body_armor|itp_covers_legs,0,
  18000,weight(30)|abundance(10)|body_armor(54)|leg_armor(54)|difficulty(15),imodbits_armor,[]],
#
["renegade_uniform_guerilla","Renegade Guerilla Uniform",[("renegade_uniform_guerilla",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  6500,weight(8)|abundance(10)|body_armor(30)|leg_armor(25)|difficulty(5),imodbits_cloth,[]],
["renegade_uniform_guerilla_2","Renegade Guerilla Uniform",[("renegade_uniform_guerilla_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  8500,weight(9)|abundance(5)|body_armor(35)|leg_armor(30)|difficulty(5),imodbits_cloth,[]],
["renegade_uniform_guerilla_3","Renegade Guerilla Uniform",[("renegade_uniform_guerilla_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  9500,weight(12)|abundance(5)|body_armor(40)|leg_armor(40)|difficulty(9),imodbits_cloth,[]],


#Theocracy
["throd_robe_black","Robe",[("throd_robe_black",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  250,weight(2.5)|body_armor(10)|leg_armor(10),imodbits_cloth],
["throd_robe_grey","Robe",[("throd_robe_grey",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  250,weight(2.5)|body_armor(10)|leg_armor(10),imodbits_cloth],
["throd_robe_purple","Robe",[("throd_robe_purple",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1000,weight(5)|body_armor(20)|leg_armor(15),imodbits_cloth],  
  
["throd_robe_armoured","Armoured_Robe",[("throd_robe_armoured",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  2500,weight(15.5)|body_armor(32)|leg_armor(22),imodbits_armor],
["throd_robe_armoured_heavy_1","Heavy_Armoured_Robe",[("throd_robe_armoured_heavy_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  4500,weight(18.5)|body_armor(37)|leg_armor(26),imodbits_armor],
["throd_robe_armoured_heavy_2","Heavy_Armoured_Robe",[("throd_robe_armoured_heavy_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  8400,weight(25.5)|body_armor(48)|leg_armor(32),imodbits_armor],

["throd_church_guard_1","Throd_Church_Armour",[("throd_church_guard_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  2500,weight(15.5)|body_armor(32)|leg_armor(22),imodbits_armor],
["throd_church_guard_2","Throd_Church_Armour",[("throd_church_guard_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  4500,weight(18.5)|body_armor(37)|leg_armor(26),imodbits_armor],
["throd_church_guard_3","Throd_Church_Armour",[("throd_church_guard_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  8400,weight(25.5)|body_armor(48)|leg_armor(32),imodbits_armor],

["ghoul_armour_light","Ghoul_Body", [("ghoul_armour_light", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique, 0,
  0, weight(7)|head_armor(20)|body_armor(29)|leg_armor(24), imodbits_armor, []],
["ghoul_armour_light2","Ghoul_Body", [("ghoul_armour_light2", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique, 0,
  0, weight(8)|head_armor(21)|body_armor(30)|leg_armor(25), imodbits_armor, []],
["ghoul_armour_medium","Ghoul_Body", [("ghoul_armour_medium", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique, 0,
  0, weight(10)|head_armor(30)|body_armor(36)|leg_armor(28), imodbits_armor, []],
["ghoul_armour_heavy","Ghoul_Body", [("ghoul_armour_heavy", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique, 0,
  0, weight(14)|head_armor(35)|body_armor(40)|leg_armor(32), imodbits_armor, []],

["throd_robe_theocracy","Theocracy_Robe",[("throd_robe_theocracy",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1000,weight(5)|body_armor(20)|leg_armor(15),imodbits_cloth],  

["throd_robe_cornucopia","Throd_Robe",[("throd_robe_cornucopia",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1200,weight(5)|body_armor(25)|leg_armor(15),imodbits_cloth],  
["throd_robe_god","Throd_Robe",[("throd_robe_god",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,
  25000,weight(22.5)|body_armor(75)|leg_armor(40),imodbits_armor],

##################################################################################
##FACTIONS END##
##################################################################################

##############
## Civilian ##
##############
##Entenaii Empire
##Entenaii Dominion
["dominion_civilian_clothes_1", "Dominion_Civilian_Clothes", [("Kaftan_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  210 , weight(3)|abundance(40)|head_armor(0)|body_armor(12)|leg_armor(3)|difficulty(4) ,imodbits_cloth,[]],
["dominion_civilian_clothes_2", "Dominion_Civilian_Clothes", [("Kaftan",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  210 , weight(3)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(3)|difficulty(4) ,imodbits_cloth,[]],
["dominion_civilian_clothes_3", "Dominion_Civilian_Clothes", [("Kaftan4",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  210 , weight(3)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(3)|difficulty(4) ,imodbits_cloth,[]],
["dominion_civilian_clothes_4", "Dominion_Civilian_Clothes", [("kaftanh",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  210 , weight(3)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(3)|difficulty(4) ,imodbits_cloth,[]],
["dominion_civilian_clothes_5", "Dominion_Civilian_Clothes", [("kaftani",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  210 , weight(3)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(3)|difficulty(4) ,imodbits_cloth,[]],

["dominion_dress_1", "Dominion_Dress", [("dominion_dress_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["dominion_dress_2", "Dominion_Dress", [("dominion_dress_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["dominion_dress_3", "Dominion_Dress", [("dominion_dress_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

##Kingdom of Galvae
["galvae_bilidh_cloak", "Ar-bilidh_Cloak", [("galvae_bilidh_cloak",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  240 , weight(3)|abundance(30)|body_armor(15)|leg_armor(10),imodbits_cloth, [
  (ti_on_init_item, [
  (str_store_string, s11,"@galvae_shoes_3"),
  (cur_item_add_mesh, s11),]),]], 
["galvae_bilidh_cloak_red", "Ar-bilidh_Cloak", [("galvae_bilidh_cloak_red",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  240 , weight(3)|abundance(30)|body_armor(14)|leg_armor(10),imodbits_cloth, [
  (ti_on_init_item, [
  (str_store_string, s11,"@galvae_shoes_3"),
  (cur_item_add_mesh, s11),]),]], 
["galvae_bilidh_cloak_green", "Ar-bilidh_Cloak", [("galvae_bilidh_cloak_green",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  240 , weight(3)|abundance(30)|body_armor(16)|leg_armor(10),imodbits_cloth, [
  (ti_on_init_item, [
  (str_store_string, s11,"@galvae_shoes_3"),
  (cur_item_add_mesh, s11),]),]], 

["gatheredcloaks1", "Gathered_Cloak", [("gatheredcloak1",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  120 , weight(2)|abundance(60)|body_armor(13)|leg_armor(6),imodbits_cloth,[]],
["gatheredcloaks2", "Gathered_Cloak", [("gatheredcloak2",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  120 , weight(2)|abundance(60)|body_armor(14)|leg_armor(6),imodbits_cloth,[]],
["gatheredcloaks3", "Gathered_Cloak", [("gatheredcloak3",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  120 , weight(2)|abundance(60)|body_armor(12)|leg_armor(6),imodbits_cloth,[]],
["gatheredcloaks4", "Gathered_Cloak", [("gatheredcloak4",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  120 , weight(2)|abundance(60)|body_armor(12)|leg_armor(6),imodbits_cloth,[]],
["gatheredcloaks5", "Gathered_Cloak", [("gatheredcloak5",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  120 , weight(2)|abundance(60)|body_armor(12)|leg_armor(6),imodbits_cloth,[]],

["tartan_dress_1", "Galvae Dress", [("pictishdressazul",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  150 , weight(3)|abundance(60)|body_armor(10)|leg_armor(5),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@galvae_shoes_1"),
  (cur_item_add_mesh, s11),]),]],
["tartan_dress_2", "Galvae Dress", [("pictishdress2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  150 , weight(3)|abundance(60)|body_armor(10)|leg_armor(5),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@galvae_shoes_1"),
  (cur_item_add_mesh, s11),]),]],
["tartan_dress_3", "Galvae Dress", [("pictishdress3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  150 , weight(3)|abundance(60)|body_armor(10)|leg_armor(5),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@galvae_shoes_1"),
  (cur_item_add_mesh, s11),]),]],
["tartan_dress_4", "Galvae Dress", [("pictishdress1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  150 , weight(3)|abundance(60)|body_armor(10)|leg_armor(5),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@galvae_shoes_1"),
  (cur_item_add_mesh, s11),]),]],
["tartan_dress_5", "Galvae Dress", [("pictishdressverde",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  150 , weight(3)|abundance(60)|body_armor(10)|leg_armor(5),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@galvae_shoes_1"),
  (cur_item_add_mesh, s11),]),]],
["tartan_dress_6", "Galvae Dress", [("pictishdress",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  150 , weight(3)|abundance(60)|body_armor(10)|leg_armor(5),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@galvae_shoes_1"),
  (cur_item_add_mesh, s11),]),]],

["galvae_royal_dress", "Galvae_Royal_Dress", [("galvae_royal_dress",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  150 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@galvae_shoes_3"),
  (cur_item_add_mesh, s11),]),]],

##Molvat-Berchav Union
["union_civ_1","Union_Civilian_Clothes", [("union_civ_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  85 , weight(2.5)|body_armor(8)|leg_armor(6), imodbits_none,[]],
["union_civ_2","Union_Civilian_Clothes", [("union_civ_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  85 , weight(2.5)|body_armor(8)|leg_armor(6), imodbits_none,[]],
["union_civ_3","Union_Civilian_Clothes", [("union_civ_3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  85 , weight(2.5)|body_armor(8)|leg_armor(6), imodbits_none,[]],
["union_civ_4","Union_Civilian_Clothes", [("union_civ_4",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  85 , weight(2.5)|body_armor(8)|leg_armor(6), imodbits_none,[]],

["union_civ_rich_1","Union_Rich_Civilian_Clothes", [("union_civ_rich_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  125 , weight(2.5)|body_armor(9)|leg_armor(7), imodbits_none,[]],
["union_civ_rich_2","Union_Rich_Civilian_Clothes", [("union_civ_rich_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  125 , weight(2.5)|body_armor(9)|leg_armor(7), imodbits_none,[]],

["wool_dress_1", "Union Dress", [("briton_dress",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  100 , weight(3)|abundance(100)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["wool_dress_2", "Union Dress", [("briton_dress_b",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  200 , weight(3)|abundance(100)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["wool_dress_3", "Union Dress", [("briton_dress_c",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  200 , weight(3)|abundance(100)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["wool_dress_4", "Union Dress", [("briton_dress_d",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  200 , weight(3)|abundance(100)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["wool_dress_5", "Union Dress", [("briton_dress_e",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  200 , weight(3)|abundance(100)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

##Vitzland Territories
["vitzland_dress_1", "Vitzland Dress", [("vitzland_dress_civilian_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  150 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["vitzland_dress_2", "Vitzland Dress", [("vitzland_dress_civilian_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  150 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["vitzland_dress_3", "Vitzland Dress", [("vitzland_dress_civilian_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  150 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["vitzland_dress_4", "Vitzland Dress", [("vitzland_dress_civilian_4",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  150 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["vitzland_dress_5", "Vitzland Dress", [("vitzland_dress_civilian_5",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  150 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["vitzland_dress_6", "Vitzland Dress", [("vitzland_dress_civilian_6",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  150 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

["vitzland_noble_dress_1", "Vitzland_Noble_Dress", [("vitzland_dress_noble_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
  500 , weight(3)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["vitzland_noble_dress_2", "Vitzland_Noble_Dress", [("vitzland_dress_noble_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
  500 , weight(3)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["vitzland_noble_dress_3", "Vitzland_Noble_Dress", [("vitzland_dress_noble_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
  500 , weight(3)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["vitzland_noble_dress_4", "Vitzland_Noble_Dress", [("vitzland_dress_noble_4",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
  500 , weight(3)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["vitzland_noble_dress_5", "Vitzland_Noble_Dress", [("vitzland_dress_noble_5",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  500 , weight(3)|abundance(10)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

##Trezzo Republic
["republican_civ_1","Republican_Civilian_Clothes", [("republican_civ_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["republican_civ_2","Republican_Civilian_Clothes", [("republican_civ_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

["white_dress_1", "Republican_Dress", [("kenttunik",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["white_dress_2", "Republican_Dress", [("tunikwjac1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0, 
  500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

["republican_consort_dress_1", "Republican_Consort_Dress", [("republican_consort_dress_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
  1000 , weight(3)|abundance(10)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["republican_consort_dress_2", "Republican_Consort_Dress", [("republican_consort_dress_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
  1000 , weight(3)|abundance(10)|head_armor(0)|body_armor(20)|leg_armor(20)|difficulty(0) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

##Itami Castedom
["itami_civ_1","Itami_Civilian_Clothes", [("itami_civ_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[]],
["itami_civ_2","Itami_Civilian_Clothes", [("itami_civ_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[]],

##Renegade

##Other
["civilian_outfit_1","Civilian Clothes", [("sayazn_long_waistcoat_brown",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[]],
["civilian_outfit_2","Civilian Clothes", [("jacobhinds_long_waistcoat",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[]],
["civilian_outfit_3","Civilian Clothes", [("jacobhinds_long_waistcoat_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[]],
["civilian_outfit_4","Civilian Clothes", [("civilian_outfit_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[]],
["civilian_outfit_5","Civilian Clothes", [("civilian_outfit_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["civilian_outfit_6","Civilian Clothes", [("sayazn_waistcoat_man_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["civilian_outfit_7","Civilian Clothes", [("sayazn_waistcoat_man_3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["civilian_outfit_8","Civilian Clothes", [("dueling_shirt",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["civilian_outfit_9","Civilian Clothes", [("peasant_costume_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["civilian_outfit_10","Civilian Clothes", [("peasant_costume_c",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
#female
["civilian_outfit_1w","Civilian Woman Clothes", [("sayazn_peasant_dress_4",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["civilian_outfit_2w","Civilian Woman Clothes", [("sayazn_waistcoat_dress_striped",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["civilian_outfit_3w","Civilian Woman Clothes", [("sayazn_ishtar_peasant_dress_3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["civilian_outfit_4w","Civilian Woman Clothes", [("sayazn_ishtar_peasant_dress_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["civilian_outfit_5w","Civilian Woman Clothes", [("sayazn_waistcoat_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["civilian_outfit_6w","Civilian Woman Clothes", [("sayazn_waistcoat_dress_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["civilian_outfit_7w","Civilian Woman Clothes", [("sayazn_waistcoat_dress_3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["civilian_outfit_8w","Civilian Woman Clothes", [("sayazn_peasant_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["civilian_outfit_9w","Civilian Woman Clothes", [("sayazn_peasant_dress_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["civilian_outfit_10w","Civilian Woman Clothes", [("sayazn_peasant_dress_3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

#peasant
["peasant_shirt_1", "Peasant_Shirt", [("shirtb",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["peasant_shirt_2", "Peasant_Shirt", [("shirtc",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["peasant_shirt_3", "Peasant_Shirt", [("shirtd",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["peasant_shirt_4", "Peasant_Shirt", [("shirte",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["peasant_shirt_5", "Peasant_Shirt", [("armor_8",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["peasant_shirt_6", "Peasant_Shirt", [("armor_9",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  50 , weight(2)|body_armor(5)|leg_armor(5), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

#adventurer
["adventurer_black","Adventurer_Outfit", [("adventurer_black", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_blue","Adventurer_Outfit", [("adventurer_blue", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_blue_red","Adventurer_Outfit", [("adventurer_blue_red", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_blue_yellow","Adventurer_Outfit", [("adventurer_blue_yellow", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_brown","Adventurer_Outfit", [("adventurer_brown", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_green","Adventurer_Outfit", [("adventurer_green", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_grey","Adventurer_Outfit", [("adventurer_grey", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_grey_2","Adventurer_Outfit", [("adventurer_grey_2", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_orange","Adventurer_Outfit", [("adventurer_orange", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_red","Adventurer_Outfit", [("adventurer_red", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_red_yellow","Adventurer_Outfit", [("adventurer_red_yellow", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_yellow","Adventurer_Outfit", [("adventurer_yellow", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],

#adventurer_rough
["adventurer_rough_black","Adventurer_Outfit", [("adventurer_rough_black", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  400, weight(4)|body_armor(18)|leg_armor(16), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_rough_blue","Adventurer_Outfit", [("adventurer_rough_blue", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  400, weight(4)|body_armor(18)|leg_armor(16), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_rough_blue_red","Adventurer_Outfit", [("adventurer_rough_blue_red", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  400, weight(4)|body_armor(18)|leg_armor(16), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_rough_brown","Adventurer_Outfit", [("adventurer_rough_brown", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  400, weight(4)|body_armor(18)|leg_armor(16), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_rough_cream","Adventurer_Outfit", [("adventurer_rough_cream", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  400, weight(4)|body_armor(18)|leg_armor(16), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_rough_green","Adventurer_Outfit", [("adventurer_rough_green", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  400, weight(4)|body_armor(18)|leg_armor(16), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],

["adventurer_bravado_grey","Adventurer_Bravado_Outfit", [("adventurer_bravado_grey", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  450, weight(4)|body_armor(20)|leg_armor(17), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_bravado_blue","Adventurer_Bravado_Outfit", [("adventurer_bravado_blue", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  450, weight(4)|body_armor(20)|leg_armor(17), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],

#adventurer_rich
["adventurer_rich_black","Rich_Adventurer_Outfit", [("adventurer_rich_black", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  500, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_rich_blue","Rich_Adventurer_Outfit", [("adventurer_rich_blue", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  500, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_rich_grey","Rich_Adventurer_Outfit", [("adventurer_rich_grey", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  500, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_rich_light_blue","Rich_Adventurer_Outfit", [("adventurer_rich_light_blue", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  500, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_rich_orange","Rich_Adventurer_Outfit", [("adventurer_rich_orange", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  500, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_rich_red","Rich_Adventurer_Outfit", [("adventurer_rich_red", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  500, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_rich_white","Rich_Adventurer_Outfit", [("adventurer_rich_white", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  500, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],

#adventurer_foreign
["adventurer_foreign_bashide_1","Bashide_Adventurer_Outfit", [("adventurer_foreign_bashide_1", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_foreign_bashide_2","Bashide_Adventurer_Outfit", [("adventurer_foreign_bashide_2", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_foreign_shonson_1","Shonson_Adventurer_Outfit", [("adventurer_foreign_shonson_1", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_foreign_shonson_2","Shonson_Adventurer_Outfit", [("adventurer_foreign_shonson_2", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_foreign_quvair_1","Quvair_Adventurer_Outfit", [("adventurer_foreign_quvair_1", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_foreign_laloch_1","Laloch_Adventurer_Outfit", [("adventurer_foreign_laloch_1", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_foreign_laloch_2","Laloch_Adventurer_Outfit", [("adventurer_foreign_laloch_2", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_foreign_istak_1","Istak_Adventurer_Outfit", [("adventurer_foreign_istak_1", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_foreign_istak_2","Istak_Adventurer_Outfit", [("adventurer_foreign_istak_2", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_foreign_kesoki_1","Kesoki_Adventurer_Outfit", [("adventurer_foreign_kesoki_1", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["adventurer_foreign_kesoki_2","Kesoki_Adventurer_Outfit", [("adventurer_foreign_kesoki_2", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
#adventurer_armour

#adventurer_woman
["adventurer_dress_1","Adventurer_Outfit", [("jacobhinds_bandit_dress_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  345 , weight(4)|body_armor(13)|leg_armor(13), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["adventurer_dress_2","Adventurer_Outfit", [("jacobhinds_bandit_dress_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  375 , weight(4)|body_armor(14)|leg_armor(13), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["adventurer_dress_3","Adventurer_Outfit", [("jacobhinds_bandit_dress_3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  400 , weight(4)|body_armor(15)|leg_armor(14), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["adventurer_dress_4","Adventurer_Outfit", [("jacobhinds_bandit_dress_4",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  420 , weight(5)|body_armor(16)|leg_armor(15), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
  
#adventurer_female_armour
["adventurer_dress_armour_1","Adventurer_Armour", [("adventurer_dress_armour_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  950 , weight(8)|body_armor(30)|leg_armor(20), imodbits_none,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

#candles
["candle_outfit_red","Red_Candle_Outfit", [("red_candle_uniform",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  375 , weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth,[]],
["candle_outfit_blue","Blue_Candle_Outfit", [("blue_candle_uniform",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  550 , weight(5)|body_armor(20)|leg_armor(20), imodbits_cloth,[]],
["candle_outfit_black","Black_Candle_Outfit", [("black_candle_uniform",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  950 , weight(6)|body_armor(28)|leg_armor(25), imodbits_cloth,[]],
["candle_outfit_black_2","Black_Candle_Rider_Outfit", [("black_candle_uniform_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  950 , weight(4)|body_armor(27)|leg_armor(24), imodbits_cloth,[]],
["candle_armour_black","Black_Candle_Armour", [("black_candle_armour",0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  1650 , weight(12)|body_armor(35)|leg_armor(28), imodbits_armor,[]],

#shadow_operative
["shadow_operative_uniform_regular","Shadow_Operative_Uniform", [("shadow_operative_uniform_4", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  375, weight(4)|body_armor(15)|leg_armor(15), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["shadow_operative_uniform_officer","Shadow_Operative_Officer_Uniform", [("shadow_operative_uniform_5", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  500, weight(5)|body_armor(17)|leg_armor(17), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["shadow_operative_uniform_saboteur","Shadow_Operative_Saboteur_Uniform", [("shadow_operative_uniform_1", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  770, weight(12)|body_armor(20)|leg_armor(18), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["shadow_operative_uniform_gunner","Shadow_Operative_Support_Uniform", [("shadow_operative_uniform_2", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  1000, weight(8)|body_armor(18)|leg_armor(18), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 2),
        (eq,":rnd",1),
        (str_store_string, s11,"@boots_1"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s11,"@boots_2"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["shadow_operative_uniform_elite","Shadow_Operative_Elite_Uniform", [("shadow_operative_elite", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  17000, weight(11)|body_armor(38)|leg_armor(25), imodbits_armor, []],

["shadow_operative_armour","Shadow_Operative_Armour", [("shadow_operative_knight_1", 0)], itp_type_body_armor|itp_covers_legs, 0,
  150000, weight(25)|body_armor(68)|leg_armor(48), imodbits_armor, []],

#destroyed shadow operative
["shadow_operative_uniform_remnant","Shadow_Operative_Remnant_Uniform", [("shadow_remnant_cuirass", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  7000, weight(11)|body_armor(22)|leg_armor(18), imodbits_armor, []],

##wild_bodypaint##
["wild_bodypaint_1", "Bodypaint", [("dummy_mesh",0)],itp_unique|itp_type_body_armor|itp_civilian|itp_covers_legs ,0,
  100 , weight(0.5)|abundance(10)|body_armor(10)|leg_armor(5), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 19),
        (eq,":rnd",1),
        (str_store_string, s12,"@2celtbody"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",2),
        (str_store_string, s12,"@war_paint_two"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",3),
        (str_store_string, s12,"@3celtbody"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",4),
        (str_store_string, s12,"@5celtbody"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",5),
        (str_store_string, s12,"@6celtbody"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",6),
        (str_store_string, s12,"@BL_Body01_male"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",7),
        (str_store_string, s12,"@BL_Body02_male"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",8),
        (str_store_string, s12,"@BL_Body03_male"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",9),
        (str_store_string, s12,"@war_paintus_3"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",10),
        (str_store_string, s12,"@war_paintus_4"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",11),
        (str_store_string, s12,"@BL_Body04_male"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",12),
        (str_store_string, s12,"@BL_Body07_male"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",13),
        (str_store_string, s12,"@war_paintus_7"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",14),
        (str_store_string, s12,"@war_paintus_8"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",15),
        (str_store_string, s12,"@war_paintus_10"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",16),
        (str_store_string, s12,"@war_paintus_11"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",17),
        (str_store_string, s12,"@BL_Body09_male"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",18),
        (str_store_string, s12,"@war_paintus"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s12,"@BL_Body08_male"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],
["wild_bodypaint_2", "Bodypaint", [("dummy_mesh",0)],itp_unique|itp_type_body_armor|itp_civilian|itp_covers_legs ,0,
  200 , weight(0.5)|abundance(10)|body_armor(12)|leg_armor(8), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 19),
        (eq,":rnd",1),
        (str_store_string, s12,"@BL_Celts01COAT"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",2),
        (str_store_string, s12,"@BL_Celts02COAT"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",3),
        (str_store_string, s12,"@BL_Celts03COAT"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",4),
        (str_store_string, s12,"@BL_Celts04COAT"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",5),
        (str_store_string, s12,"@BL_Celts05COAT"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",6),
        (str_store_string, s12,"@BL_Celts06COAT"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",7),
        (str_store_string, s12,"@BL_Celts07COAT"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",8),
        (str_store_string, s12,"@BL_Celts08COAT"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",9),
        (str_store_string, s12,"@BL_Celts01"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",10),
        (str_store_string, s12,"@BL_Celts11"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",11),
        (str_store_string, s12,"@BL_Celts02"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",12),
        (str_store_string, s12,"@BL_Celts03"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",13),
        (str_store_string, s12,"@BL_Celts04"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",14),
        (str_store_string, s12,"@BL_Celts05"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",15),
        (str_store_string, s12,"@BL_Celts06"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",16),
        (str_store_string, s12,"@BL_Celts07"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",17),
        (str_store_string, s12,"@BL_Celts08"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",18),
        (str_store_string, s12,"@BL_Celts09"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s12,"@BL_Celts10"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],

["wild_bodypaint_fem", "Bodypaint", [("dummy_mesh",0)],itp_unique|itp_type_body_armor|itp_civilian|itp_covers_legs ,0,
  100 , weight(0.5)|abundance(10)|body_armor(10)|leg_armor(5), imodbits_cloth, [
    (ti_on_init_item, [
      (store_trigger_param_1,":agent"),
      (store_trigger_param_2,":troop"),
      (try_begin),
        (ge,":agent",0),
        (lt,":troop",heroes_begin),
        (gt,":troop",0),
        (store_random_in_range,":rnd", 0, 5),
        (eq,":rnd",1),
        (str_store_string, s12,"@picta1"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",2),
        (str_store_string, s12,"@picta2"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (eq,":rnd",3),
        (str_store_string, s12,"@picta3"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (else_try),
        (str_store_string, s12,"@picta4"),
        (cur_item_add_mesh, s12),
        (str_store_string, s11,"@bare_legs_blue"),
        (cur_item_add_mesh, s11),
      (try_end),
      ]),]],

#smith
["leather_vest_1", "Leather over Tunic", [("saxon_leather_vest_green",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 
  820 , weight(4)|abundance(60)|head_armor(0)|body_armor(23)|leg_armor(2)|difficulty(6) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["leather_vest_2", "Leather over Tunic", [("saxon_leather_vest_blue",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 
  820 , weight(4)|abundance(60)|head_armor(0)|body_armor(23)|leg_armor(2)|difficulty(6) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["leather_vest_3", "Leather over Tunic", [("saxon_leather_vest_red",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 
  820 , weight(4)|abundance(60)|head_armor(0)|body_armor(23)|leg_armor(2)|difficulty(6) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

#misc
["goatskin_tunic", "Goat_Skin_Tunic", [("goatist_tunic",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 
  1160 , weight(4)|abundance(20)|head_armor(0)|body_armor(22)|leg_armor(12)|difficulty(6) ,imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["bear_warrior_totem", "Bear_Warrior_Totem_Armour", [("bear_warrior_totem",0),("bear_warrior_totem_rust",imodbit_cracked|imodbit_rusty)],  itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 
  1160 , weight(12)|body_armor(35)|leg_armor(25)|difficulty(6) ,imodbits_armor,[]],

#fallen_phalanx
["phalanx_uniform_1","Fresh_Fallen_Phalanx_Uniform",[("phalanx_trooper_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  500,weight(12)|body_armor(25)|leg_armor(20),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["phalanx_uniform_2","Firstblood_Fallen_Phalanx_Uniform",[("phalanx_trooper_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  800,weight(14)|body_armor(30)|leg_armor(25),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["phalanx_uniform_3","Bloodied_Fallen_Phalanx_Uniform",[("phalanx_trooper_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1000,weight(14)|body_armor(35)|leg_armor(30),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["phalanx_uniform_4","Scarred_Fallen_Phalanx_Uniform",[("phalanx_trooper_4",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1300,weight(15)|body_armor(40)|leg_armor(35),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["phalanx_uniform_5","Chosen_Fallen_Phalanx_Uniform",[("phalanx_trooper_5",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1800,weight(17)|body_armor(45)|leg_armor(40),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
#
["phalanx_flamer_1","Flamer_Fallen_Phalanx_Uniform",[("phalanx_flamer_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  800,weight(14)|body_armor(30)|leg_armor(25),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
#
["renfield_suit","Renfield's_Suit", [("renfield_suit", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0,
  312, weight(1.75)|body_armor(15)|leg_armor(15), imodbits_cloth, [
  (ti_on_init_item, [
  (str_store_string, s12,"@shoes_black"),
  (cur_item_add_mesh, s12),]),]],

#mercenary

["yanizar_uniform_1","yanizar Uniform",[("yanizar_uniform_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(10)|abundance(30)|body_armor(18)|leg_armor(15)|difficulty(4),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["yanizar_uniform_2","yanizar Uniform",[("janichareteksiz",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  300,weight(10)|abundance(20)|body_armor(20)|leg_armor(18)|difficulty(4),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

["mercenary_coat_1","Mercenary_Coat",[("mercenary_coat",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  700,weight(12)|body_armor(27)|leg_armor(25),imodbits_cloth,[]],
["mercenary_coat_2","Mercenary_Coat",[("mercenary_coat_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  900,weight(14)|body_armor(30)|leg_armor(28),imodbits_cloth,[]],
["mercenary_coat_3","Mercenary_Coat",[("mercenary_coat_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1000,weight(14)|body_armor(32)|leg_armor(30),imodbits_cloth,[]],
["mercenary_coat_4","Mercenary_Coat",[("mercenary_coat_4",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1200,weight(14)|body_armor(34)|leg_armor(31),imodbits_cloth,[]],

["mercenary_cuirass","Mercenary_Cuirass",[("mercenary_cuirass",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1300,weight(15)|body_armor(38)|leg_armor(36),imodbits_armor,[]],
["mercenary_cuirass_2","Mercenary_Cuirass",[("mercenary_cuirass_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1500,weight(15)|body_armor(42)|leg_armor(38),imodbits_armor,[]],
["mercenary_cuirass_3","Mercenary_Cuirass",[("mercenary_cuirass_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1600,weight(15)|body_armor(45)|leg_armor(40),imodbits_armor,[]],
["mercenary_cuirass_4","Mercenary_Cuirass",[("mercenary_cuirass_4",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1700,weight(15)|body_armor(46)|leg_armor(41),imodbits_armor,[]],

["mercenary_armour","Mercenary_Armour",[("mercenary_cuirass_heavy",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1800,weight(17)|body_armor(48)|leg_armor(44),imodbits_armor,[]],
["mercenary_armour_2","Mercenary_Armour",[("mercenary_cuirass_heavy_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  2100,weight(17)|body_armor(50)|leg_armor(48),imodbits_armor,[]],
["mercenary_armour_3","Mercenary_Armour",[("mercenary_cuirass_heavy_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1800,weight(17)|body_armor(52)|leg_armor(50),imodbits_armor,[]],
["mercenary_armour_4","Mercenary_Armour",[("mercenary_cuirass_heavy_4",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  2100,weight(17)|body_armor(55)|leg_armor(51),imodbits_armor,[]],

["trench_esquire_armour","Trench_Esquire_Armour",[("trench_esquire_armour_1",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,
  8000,weight(22)|abundance(25)|body_armor(40)|leg_armor(36)|difficulty(11),imodbits_armor,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_5"),
  (cur_item_add_mesh, s11),]),]],

["trench_knight_plate_1","Trench_Knight_Plate",[("trench_knight_plate_1",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,
  10000,weight(30)|abundance(15)|body_armor(48)|leg_armor(42)|difficulty(15),imodbits_armor,[]],
["trench_knight_plate_2","Trench_Knight_Plate",[("trench_knight_plate_2",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,
  13000,weight(30)|abundance(10)|body_armor(52)|leg_armor(45)|difficulty(18),imodbits_armor,[]],
["trench_knight_plate_3","Trench_Knight_Plate",[("trench_knight_plate_3",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,
  18000,weight(30)|abundance(5)|body_armor(56)|leg_armor(50)|difficulty(18),imodbits_armor,[]],

["military_police_uniform_1","Military_Police_Uniform_1",[("military_police_uniform_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  700,weight(10)|body_armor(27)|leg_armor(25),imodbits_cloth,[]],
["military_police_uniform_2","Military_Police_Uniform_1",[("military_police_uniform_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  900,weight(11)|body_armor(30)|leg_armor(28),imodbits_cloth,[]],
["military_police_uniform_3","Military_Police_Uniform_1",[("military_police_uniform_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  1000,weight(12)|body_armor(34)|leg_armor(30),imodbits_cloth,[]],


#bandit
["poor_shirt_1", "Poor Shirt", [("shirt_a",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0,
  110 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]], 
["poor_shirt_2", "Poorman Tunic", [("BL_TunicR01_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["poor_shirt_3", "Poorman Robe", [("leper_robe",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth],
["poor_shirt_4", "Dirty Tunic", [("dirty_cloth",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  210 , weight(0.5)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["poor_shirt_5", "Poor Shirt", [("dirty_cloth_2",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0,
  110 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]], 
["poor_shirt_6", "Beggar Clothes", [("dirty_cloth_3",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0,
  50 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(1), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]], 

["bandit_1", "Bandit_Clothes", [("balt_fur_b",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0,
  200 , weight(1)|abundance(80)|body_armor(12)|leg_armor(4), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]], 
["bandit_2", "Bandit_Clothes", [("balt_fur_a",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0,
  200 , weight(1)|abundance(80)|body_armor(12)|leg_armor(4), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["bandit_3", "Bandit_Leather", [("balt_leather",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0,
  350 , weight(2)|abundance(60)|body_armor(18)|leg_armor(10), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["bandit_4", "Bandit_Leather", [("balt_leather_b",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0,
  350 , weight(2)|abundance(60)|body_armor(18)|leg_armor(10), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["bandit_5", "Bandit_Lamellar", [("balt_lamellar",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0,
  650 , weight(3.5)|abundance(40)|body_armor(24)|leg_armor(15), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

["northern_bandit_1", "Bandit_Clothes", [("bakak",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0,
  260 , weight(1.5)|abundance(70)|body_armor(15)|leg_armor(7), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]], 

["swamp_bandit_1", "Bandit_Clothes", [("swamp_bandit_1",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0,
  230 , weight(1.5)|abundance(70)|body_armor(12)|leg_armor(7), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@foot_wrapping"),
  (cur_item_add_mesh, s11),]),]], 
["swamp_bandit_2", "Bandit_Clothes", [("swamp_bandit_2",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0,
  240 , weight(1.5)|abundance(70)|body_armor(13)|leg_armor(7), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@foot_wrapping"),
  (cur_item_add_mesh, s11),]),]], 
["swamp_bandit_3", "Bandit_Clothes", [("swamp_bandit_3",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0,
  240 , weight(1.5)|abundance(70)|body_armor(13)|leg_armor(7), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@foot_wrapping"),
  (cur_item_add_mesh, s11),]),]], 
["swamp_bandit_4", "Bandit_Clothes", [("swamp_bandit_4",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0,
  250 , weight(1.5)|abundance(70)|body_armor(14)|leg_armor(7), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@foot_wrapping"),
  (cur_item_add_mesh, s11),]),]], 

["swamp_bandit_medium_armour_1", "Medium_Bandit_Armour", [("swamp_bandit_medium_armour_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  400 , weight(12)|abundance(40)|body_armor(32)|leg_armor(18), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@sandal_wrapping"),
  (cur_item_add_mesh, s11),]),]],
["swamp_bandit_medium_armour_2", "Medium_Bandit_Armour", [("swamp_bandit_medium_armour_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  475 , weight(12)|abundance(40)|body_armor(30)|leg_armor(16), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@sandal_wrapping"),
  (cur_item_add_mesh, s11),]),]],
["swamp_bandit_medium_armour_3", "Medium_Bandit_Armour", [("swamp_bandit_medium_armour_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  500 , weight(12)|abundance(40)|body_armor(31)|leg_armor(20), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@sandal_wrapping"),
  (cur_item_add_mesh, s11),]),]],

["swamp_bandit_cuirass_1", "Bandit_Plate Cuirass", [("swamp_bandit_cuirass_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  755 , weight(14)|abundance(25)|body_armor(35)|leg_armor(24), imodbits_armor,[
  (ti_on_init_item, [
  (str_store_string, s11,"@sandal_boots"),
  (cur_item_add_mesh, s11),]),]],
["swamp_bandit_legend_cuirass", "Bandit_Tiger Cuirass", [("swamp_bandit_legend_cuirass",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  755 , weight(14)|abundance(25)|body_armor(35)|leg_armor(24), imodbits_armor,[
  (ti_on_init_item, [
  (str_store_string, s11,"@sandal_boots"),
  (cur_item_add_mesh, s11),]),]],

["swamp_bandit_heavy_armour_1", "Bandit_Lamellar_Plate_Armour", [("swamp_bandit_heavy_armour_1",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise ,0, 
  2000 , weight(20)|abundance(40)|body_armor(38)|leg_armor(22), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@sandal_boots"),
  (cur_item_add_mesh, s11),]),]],
["swamp_bandit_heavy_armour_2", "Bandit_Lamellar_Plate_Armour", [("swamp_bandit_heavy_armour_2",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise ,0, 
  2000 , weight(20)|abundance(40)|body_armor(38)|leg_armor(22), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@sandal_boots"),
  (cur_item_add_mesh, s11),]),]],

["light_bandit_armour_1", "Light_Bandit_Armour", [("light_bandit_armour_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  320 , weight(10.5)|abundance(40)|body_armor(20)|leg_armor(14), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["light_bandit_armour_2", "Light_Bandit_Armour", [("light_bandit_armour_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  375 , weight(10.5)|abundance(40)|body_armor(21)|leg_armor(17), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["light_bandit_cuirass_1", "Light_Bandit_Cuirass", [("light_bandit_cuirass_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  300 , weight(8.5)|abundance(40)|body_armor(20)|leg_armor(12), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

["medium_bandit_cuirass_1", "Medium_Bandit_Cuirass", [("medium_bandit_cuirass_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  400 , weight(12)|abundance(40)|body_armor(32)|leg_armor(18), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_5"),
  (cur_item_add_mesh, s11),]),]],
["medium_bandit_cuirass_2", "Medium_Bandit_Cuirass", [("medium_bandit_cuirass_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  475 , weight(12)|abundance(40)|body_armor(30)|leg_armor(16), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_5"),
  (cur_item_add_mesh, s11),]),]],
["medium_bandit_cuirass_3", "Medium_Bandit_Cuirass", [("medium_bandit_cuirass_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  500 , weight(12)|abundance(40)|body_armor(31)|leg_armor(20), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_5"),
  (cur_item_add_mesh, s11),]),]],
["medium_bandit_cuirass_4", "Medium_Bandit_Cuirass", [("medium_bandit_cuirass_4",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  550 , weight(12)|abundance(40)|body_armor(32)|leg_armor(21), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_5"),
  (cur_item_add_mesh, s11),]),]],

["bandit_plate_cuirass_1", "Bandit_Plate Cuirass", [("bandit_plate_cuirass_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  755 , weight(14)|abundance(25)|body_armor(35)|leg_armor(24), imodbits_armor,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_5"),
  (cur_item_add_mesh, s11),]),]],
["bandit_plate_cuirass_2", "Bandit_Plate Cuirass", [("bandit_plate_cuirass_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  755 , weight(14)|abundance(25)|body_armor(35)|leg_armor(24), imodbits_armor,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_5"),
  (cur_item_add_mesh, s11),]),]],
["bandit_plate_cuirass_3", "Bandit_Plate Cuirass", [("bandit_plate_cuirass_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  755 , weight(14)|abundance(25)|body_armor(35)|leg_armor(24), imodbits_armor,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_5"),
  (cur_item_add_mesh, s11),]),]],
["bandit_plate_cuirass_4", "Bandit_Plate Cuirass", [("bandit_plate_cuirass_4",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  755 , weight(14)|abundance(25)|body_armor(35)|leg_armor(24), imodbits_armor,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_5"),
  (cur_item_add_mesh, s11),]),]],
["bandit_plate_cuirass_5", "Bandit_Plate Cuirass", [("bandit_plate_cuirass_5",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  925 , weight(14.5)|abundance(20)|body_armor(37)|leg_armor(25), imodbits_armor,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_5"),
  (cur_item_add_mesh, s11),]),]],

["bandit_scale_shirt_1", "Bandit_Scale_Shirt", [("bandit_scale_shirt_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise ,0, 
  1000 , weight(18)|abundance(40)|body_armor(35)|leg_armor(20), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_5"),
  (cur_item_add_mesh, s11),]),]],
["bandit_scale_armour_1", "Bandit_Scale_Armour", [("bandit_scale_armour_1",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise ,0, 
  2000 , weight(20)|abundance(40)|body_armor(38)|leg_armor(22), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_5"),
  (cur_item_add_mesh, s11),]),]],

["heavy_bandit_armour","Heavy_Bandit_Armour",[("heavy_bandit_armour",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,
  8500,weight(30)|abundance(10)|body_armor(44)|leg_armor(35)|difficulty(12),imodbits_armor,[
  (ti_on_init_item, [
  (str_store_string, s11,"@splinted_greaves_spurs"),
  (cur_item_add_mesh, s11),]),]],
["heavy_bandit_armour_rusty","Heavy_Bandit_Armour_Rusty",[("heavy_bandit_armour_rusty",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,
  7000,weight(29.5)|abundance(10)|body_armor(39)|leg_armor(30)|difficulty(12),imodbits_armor,[
  (ti_on_init_item, [
  (str_store_string, s11,"@splinted_greaves_spurs"),
  (cur_item_add_mesh, s11),]),]],
["heavy_bandit_armour_burnt","Heavy_Bandit_Armour_Burnt",[("heavy_bandit_armour_burnt",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,
  5000,weight(29)|abundance(10)|body_armor(36)|leg_armor(25)|difficulty(12),imodbits_armor,[
  (ti_on_init_item, [
  (str_store_string, s11,"@splinted_greaves_spurs"),
  (cur_item_add_mesh, s11),]),]],

#
["dead_flower_armour","Dead_Flower_Armour",[("dead_flower_armour",0)],itp_type_body_armor|itp_covers_legs|itp_unique,0,
  9900,weight(30)|body_armor(48)|leg_armor(38)|difficulty(14),imodbits_armor,[]],
#
#cannibal
["cannibal_vest", "cannibal_vest", [("cannibal_vest",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
  400 , weight(2)|body_armor(18)|leg_armor(10), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]], 
["cannibal_vest_cult", "cannibal_vest", [("cannibal_vest_cult",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
  800 , weight(2.5)|body_armor(20)|leg_armor(16), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]], 

["cannibal_vest_bones", "cannibal_vest", [("cannibal_vest_bones",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
  1200 , weight(4)|body_armor(28)|leg_armor(24), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["cannibal_vest_cult_bones", "cannibal_vest", [("cannibal_vest_cult_bones",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
  1700 , weight(5)|body_armor(35)|leg_armor(29), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

["cannibal_vest_mutant", "cannibal_vest", [("cannibal_vest_mutant",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
  2350 , weight(4)|body_armor(44)|leg_armor(30), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["cannibal_vest_miasma", "cannibal_vest", [("cannibal_vest_miasma",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
  3500 , weight(4.5)|body_armor(52)|leg_armor(38), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["cannibal_vest_demon", "cannibal_vest", [("cannibal_vest_demon",0)],  itp_type_body_armor|itp_covers_legs|itp_civilian ,0,
  6500 , weight(6.5)|body_armor(75)|leg_armor(54), imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

#
#ezeg
["ezeg_uniform_1","Ezeg Uniform",[("ezeg_uniform_1",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  100,weight(9)|abundance(30)|body_armor(18)|leg_armor(15)|difficulty(4),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["ezeg_uniform_2","Ezeg Uniform",[("ezeg_uniform_2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  300,weight(10)|abundance(20)|body_armor(20)|leg_armor(18)|difficulty(4),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],
["ezeg_uniform_3","Ezeg Uniform",[("ezeg_uniform_3",0)],itp_type_body_armor|itp_covers_legs|itp_civilian|itp_merchandise,0,
  800,weight(11)|abundance(20)|body_armor(25)|leg_armor(22)|difficulty(5),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_1"),
  (cur_item_add_mesh, s11),]),]],

#ashmaker
["ashmaker_robe","Ashmaker_Robe",[("ashmaker_robe",0)],itp_type_body_armor|itp_covers_legs|itp_covers_head,0,
  4250,weight(10)|head_armor(34)|body_armor(36)|leg_armor(30)|difficulty(8),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_5"),
  (cur_item_add_mesh, s11),]),]],

#munition_bandit
["munition_bandit_armour","Munition_Bandit_Armour",[("munition_bandit_armour",0)],itp_type_body_armor|itp_covers_legs,0,
  9550,weight(30)|body_armor(48)|leg_armor(45)|difficulty(12),imodbits_armor,[]],

#horselords
#empty_ones
["empty_one_uniform","Empty_One_Uniform",[("empty_one_cloak",0)],itp_type_body_armor|itp_covers_legs,0,
  550,weight(3)|body_armor(28)|leg_armor(25),imodbits_cloth,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_5"),
  (cur_item_add_mesh, s11),]),]],


#night_raiders
["night_raider_esquire_armour","Night_Raider_Esquire_Armour",[("night_raider_esquire",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,
  8000,weight(22)|abundance(25)|body_armor(40)|leg_armor(36)|difficulty(11),imodbits_armor,[
  (ti_on_init_item, [
  (str_store_string, s11,"@boots_5"),
  (cur_item_add_mesh, s11),]),]],

["night_raider_armour","Night_Raider_Armour",[("night_raider_armour",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,
  10000,weight(30)|abundance(15)|body_armor(48)|leg_armor(42)|difficulty(15),imodbits_armor,[
  (ti_on_init_item, [
  (str_store_string, s11,"@splinted_greaves_spurs"),
  (cur_item_add_mesh, s11),]),]],
["night_raider_armour_2","Night_Raider_Armour",[("coffin_armour",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,
  13000,weight(30)|abundance(10)|body_armor(52)|leg_armor(45)|difficulty(18),imodbits_armor,[
  (ti_on_init_item, [
  (str_store_string, s11,"@splinted_greaves_spurs"),
  (cur_item_add_mesh, s11),]),]],
["night_raider_armour_3","Night_Raider_Armour",[("blackgod_knight",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,
  18000,weight(30)|abundance(5)|body_armor(56)|leg_armor(50)|difficulty(18),imodbits_armor,[]],

["night_raider_armour_4","Night_Raider_Armour",[("hell_armour",0)],itp_type_body_armor|itp_covers_legs|itp_merchandise,0,
  22000,weight(30)|abundance(1)|body_armor(59)|leg_armor(52)|difficulty(18),imodbits_armor,[]],
#

###################################################################################
##HEADSLOT##
##################################################################################

["ach_full","Heavy_Advanced_Combat_Helmet_with_Shades",[("ach_full",0)],itp_type_head_armor|itp_has_bayonet,0,
  3125,weight(3)|head_armor(45),imodbits_armor,[]],

["army_cap_1","Army_Cap_with_Combat_Shades",[("army_cap_1",0)],itp_type_head_armor|itp_civilian,0,
  125,weight(0.25)|head_armor(5),imodbits_cloth,[]],

["balaclava_black","Balaclava", [("balaclava_black", 0)], itp_type_head_armor|itp_covers_beard, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,[]],
["balaclava_green","Balaclava", [("balaclava_green", 0)], itp_type_head_armor|itp_covers_beard, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,[]],
["balaclava_grey","Balaclava", [("balaclava_grey", 0)], itp_type_head_armor|itp_covers_beard, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,[]],
["balaclava_tan","Balaclava", [("balaclava_tan", 0)], itp_type_head_armor|itp_covers_beard, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,[]],

["bandana_camo_goggles","Bandana_with_Goggles", [("bandana_camo", 0)], itp_type_head_armor|itp_civilian, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),]),]],
["bandana_camo","Bandana", [("bandana_camo", 0)], itp_type_head_armor|itp_civilian|itp_covers_beard, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,[]],
["bandana_black_goggles","Bandana_with_Goggles", [("bandana_black", 0)], itp_type_head_armor|itp_civilian, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),]),]],
["bandana_black","Bandana", [("bandana_black", 0)], itp_type_head_armor|itp_civilian|itp_covers_beard, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,[]],
["bandana_blue_goggles","Bandana_with_Goggles", [("bandana_blue", 0)], itp_type_head_armor|itp_civilian, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),]),]],
["bandana_blue","Bandana", [("bandana_blue", 0)], itp_type_head_armor|itp_civilian|itp_covers_beard, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,[]],
["bandana_red_goggles","Bandana_with_Goggles", [("bandana_red", 0)], itp_type_head_armor|itp_civilian, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),]),]],
["bandana_red","Bandana", [("bandana_red", 0)], itp_type_head_armor|itp_civilian|itp_covers_beard, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,[]],
["bandana_green_goggles","Bandana_with_Goggles", [("bandana_green", 0)], itp_type_head_armor|itp_civilian, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),]),]],
["bandana_green","Bandana", [("bandana_green", 0)], itp_type_head_armor|itp_civilian|itp_covers_beard, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,[]],
["bandana_white_goggles","Bandana_with_Goggles", [("bandana_white", 0)], itp_type_head_armor|itp_civilian, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),]),]],
["bandana_white","Bandana", [("bandana_white", 0)], itp_type_head_armor|itp_civilian|itp_covers_beard, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,[]],

["beret_black","Beret",[("beret_black",0)],itp_type_head_armor|itp_civilian,0,
  375,weight(0.5)|head_armor(15),imodbits_cloth,[]],
["beret_green","Beret",[("beret_green",0)],itp_type_head_armor|itp_civilian,0,
  375,weight(0.5)|head_armor(15),imodbits_cloth,[]],
["beret_grey","Beret_with_Goggles_and_Feather",[("beret_grey",0)],itp_type_head_armor|itp_civilian,0,
  375,weight(0.5)|head_armor(15),imodbits_cloth,[]],
["beret_red","Beret_with_Goggles_and_Feather",[("beret_red",0)],itp_type_head_armor|itp_civilian,0,
  375,weight(0.5)|head_armor(15),imodbits_cloth,[]],
["beret_tan","Beret_with_Goggles_and_Feather",[("beret_tan",0)],itp_type_head_armor|itp_civilian,0,
  375,weight(0.5)|head_armor(15),imodbits_cloth,[]],

["beret_black_face_cover","Beret_with_Face_Cover",[("dummy_mesh",0)],itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  400,weight(0.6)|head_armor(16),imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@beret_black"),
    (str_store_string, s4,"@upgrade_face_cover"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s4),
    ]),]],
["beret_green_face_cover","Beret_with_Face_Cover",[("dummy_mesh",0)],itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  400,weight(0.6)|head_armor(16),imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@beret_green"),
    (str_store_string, s4,"@upgrade_face_cover"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s4),
    ]),]],
["beret_grey_face_cover","Beret_with_Face_Cover",[("dummy_mesh",0)],itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  400,weight(0.6)|head_armor(16),imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@beret_grey"),
    (str_store_string, s4,"@upgrade_face_cover"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s4),
    ]),]],
["beret_red_face_cover","Beret_with_Face_Cover",[("dummy_mesh",0)],itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  400,weight(0.6)|head_armor(16),imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@beret_red"),
    (str_store_string, s4,"@upgrade_face_cover"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s4),
    ]),]],
["beret_tan_face_cover","Beret_with_Face_Cover",[("dummy_mesh",0)],itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  400,weight(0.6)|head_armor(16),imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@beret_tan"),
    (str_store_string, s4,"@upgrade_face_cover"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s4),
    ]),]],

["brodie","Brodie_Helmet", [("brodie", 0)], itp_type_head_armor|itp_merchandise, 0,
  625, weight(2.5)|head_armor(25), imodbits_armor,[]],
["brodie_gasmask","Brodie_Helmet_with_Gas_Mask", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_merchandise, 0,
  875, weight(2.5)|head_armor(35), imodbits_armor,
  [(ti_on_init_item,[
    (str_store_string, s1,"@brodie"),
    (str_store_string, s3,"@upgrade_stormchaser"),
    (str_store_string, s2,"@gas_mask_ca_90"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s3),
    (cur_item_add_mesh, s2),]),]],
["brodie_face_cover","Brodie_Helmet_with_Goggles_and_Face_Cover", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_merchandise, 0,
  650, weight(2.75)|head_armor(26), imodbits_armor,
  [(ti_on_init_item,[
    (str_store_string, s1,"@brodie"),
    (str_store_string, s2,"@upgrade_goggle"),
    (str_store_string, s3,"@upgrade_face_cover"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),    
    (cur_item_add_mesh, s3),]),]],

["bucket_helm","Makeshift_Bucket_Helmet",[("bucket_helm",0)],itp_type_head_armor|itp_merchandise,0,
  250,weight(5)|head_armor(20),imodbits_armor,[]],
["bucket_helm_black","Makeshift_Bucket_Helmet_Blackened",[("bucket_helm_black",0)],itp_type_head_armor|itp_merchandise,0,
  300,weight(5)|head_armor(22),imodbits_armor,[]],
["bucket_helm_horns","Makeshift_Bucket_Helmet_Horned",[("bucket_helm_horns",0)],itp_type_head_armor,0,
  450,weight(5.5)|head_armor(28),imodbits_armor,[]],
["bucket_helm_black_horns","Makeshift_Bucket_Helmet_Blackened_Horned",[("bucket_helm_black_horns",0)],itp_type_head_armor,0,
  650,weight(6)|head_armor(30),imodbits_armor,[]],

["camouflage_helmet","Camouflage_Helmet",[("camouflage_helmet",0)],itp_type_head_armor,0,
  765,weight(3)|head_armor(22),imodbits_armor,[]],

["civil_hat_1","Hat", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian,0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_1"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),

    (store_random_in_range,":rnd", 0, 5),
    (eq,":rnd",1),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s2),]),]],
["civil_hat_1b","Hat", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian,0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_1b"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),

    (store_random_in_range,":rnd", 0, 5),
    (eq,":rnd",1),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s2),]),]],
["civil_hat_1c","Hat", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian,0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_1c"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),

    (store_random_in_range,":rnd", 0, 5),
    (eq,":rnd",1),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s2),]),]],
["civil_hat_1d","Hat", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian,0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_1d"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),

    (store_random_in_range,":rnd", 0, 5),
    (eq,":rnd",1),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s2),]),]],
["civil_hat_2","Hat", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian,0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_2"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),

    (store_random_in_range,":rnd", 0, 5),
    (eq,":rnd",1),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s2),]),]],
["civil_hat_3","Hat", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian,0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_3"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),

    (store_random_in_range,":rnd", 0, 5),
    (eq,":rnd",1),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s2),]),]],
["civil_hat_4","Hat", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian,0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_4"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),

    (store_random_in_range,":rnd", 0, 5),
    (eq,":rnd",1),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s2),]),]],
["civil_hat_5","Hat", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian,0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_5"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),

    (store_random_in_range,":rnd", 0, 5),
    (eq,":rnd",1),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s2),]),]],
["civil_hat_7","Hat", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian,0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_7"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),

    (store_random_in_range,":rnd", 0, 5),
    (eq,":rnd",1),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s2),]),]],
["civil_hat_9","Hat", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian,0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_9"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),

    (store_random_in_range,":rnd", 0, 5),
    (eq,":rnd",1),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s2),]),]],
["civil_hat_10","Hat", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian,0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_10"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),

    (store_random_in_range,":rnd", 0, 5),
    (eq,":rnd",1),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s2),]),]],
["civil_hat_11","Hat", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian,0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_11"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),

    (store_random_in_range,":rnd", 0, 5),
    (eq,":rnd",1),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s2),]),]],
["civil_hat_12","Hat", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian,0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_12"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),

    (store_random_in_range,":rnd", 0, 5),
    (eq,":rnd",1),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s2),]),]],
["civil_hat_13","Hat", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian,0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_13"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),

    (store_random_in_range,":rnd", 0, 5),
    (eq,":rnd",1),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s2),]),]],
["civil_hat_14","Hat", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian,0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_14"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),

    (store_random_in_range,":rnd", 0, 5),
    (eq,":rnd",1),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s2),]),]],
["civil_hat_1_mask","Hat_with_Mask", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  150, weight(0.5)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_1"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["civil_hat_1b_mask","Hat_with_Mask", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  150, weight(0.5)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_1b"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["civil_hat_1c_mask","Hat_with_Mask", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  150, weight(0.5)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_1c"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["civil_hat_1d_mask","Hat_with_Mask", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  150, weight(0.5)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_1d"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["civil_hat_2_mask","Hat_with_Mask", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  150, weight(0.5)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_2"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["civil_hat_3_mask","Hat_with_Mask", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  150, weight(0.5)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_3"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["civil_hat_4_mask","Hat_with_Mask", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  150, weight(0.5)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_4"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["civil_hat_5_mask","Hat_with_Mask", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  150, weight(0.5)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_5"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["civil_hat_7_mask","Hat_with_Mask", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  150, weight(0.5)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_7"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["civil_hat_9_mask","Hat_with_Mask", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  150, weight(0.5)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_9"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["civil_hat_10_mask","Hat_with_Mask", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  150, weight(0.5)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_10"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["civil_hat_11_mask","Hat_with_Mask", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  150, weight(0.5)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_11"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["civil_hat_12_mask","Hat_with_Mask", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  150, weight(0.5)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_12"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["civil_hat_13_mask","Hat_with_Mask", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  150, weight(0.5)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_13"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["civil_hat_14_mask","Hat_with_Mask", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard,0,
  150, weight(0.5)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@civil_hat_14"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],

["commander_cap_1","Commander_Cap", [("commander_cap_1", 0)],itp_type_head_armor|itp_civilian,0,
  500, weight(0.5)|head_armor(10), imodbits_cloth,[]],

["doctor_head","Surgeon Mask", [("dummy_mesh", 0)], itp_type_head_armor|itp_civilian|itp_covers_beard, 0,
  50, weight(0.1)|head_armor(1), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (cur_item_add_mesh, "@doctor_head"),
    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),
    (store_random_in_range,":rnd", 0, 3),
    (eq,":rnd",1),
    (cur_item_add_mesh, "@upgrade_goggle"),]),]],

["gas_mask","Gas_Mask", [("gas_mask", 0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_covers_beard, 0,
  375, weight(0.5)|head_armor(15), imodbits_cloth,[]],
["gas_mask_ww","Gas_Mask", [("gas_mask_ww", 0)], itp_type_head_armor|itp_covers_head, 0,
  250, weight(0.5)|head_armor(10), imodbits_cloth, []],
["gas_mask_ca_90","Vitzland Gas_Mask", [("gas_mask_ca_90", 0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_covers_beard, 0,
  375, weight(0.5)|head_armor(15), imodbits_cloth, []],
#
["gas_mask_m40","M40_Gas_Mask", [("gas_mask_m40_combined", 0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_covers_beard, 0,
  375, weight(0.5)|head_armor(15), imodbits_cloth,[]],
["gas_mask_xm40","XM40_Gas_Mask", [("gas_mask_xm40_combined", 0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_covers_beard, 0,
  375, weight(0.5)|head_armor(15), imodbits_cloth,[]],
#
["gas_mask_brown_01","Union Gas Mask", [("gas_mask_brown_01", 0)], itp_type_head_armor|itp_covers_head, 0,
  300, weight(0.5)|head_armor(12), imodbits_cloth, []],

["goggles_1","Goggles", [("goggles_1", 0)],itp_type_head_armor|itp_doesnt_cover_hair|itp_merchandise, 0,
  250, weight(0.5)|head_armor(10), imodbits_cloth,[]],
["goggles_1_face_cover","Goggles_with_Face_Cover", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_doesnt_cover_hair|itp_covers_beard|itp_merchandise, 0,
  275, weight(0.6)|head_armor(11), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@goggles_1"),
    (str_store_string, s2,"@upgrade_face_cover"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),]),]],
["goggles_2","Goggles_(No_Lenses)", [("goggles_2", 0)],itp_type_head_armor|itp_doesnt_cover_hair|itp_merchandise, 0,
  225, weight(0.4)|head_armor(9), imodbits_cloth,[]],
["goggles_2_face_cover","Goggles_(No_Lenses)_with_Face_Cover", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_doesnt_cover_hair|itp_covers_beard|itp_merchandise, 0,
  250, weight(0.6)|head_armor(10), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@goggles_2"),
    (str_store_string, s2,"@upgrade_face_cover"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),]),]],

#
["renfield_glasses","Renfield's_Glasses", [("renfield_glasses", 0)],
  itp_type_head_armor|itp_doesnt_cover_hair, 0,
  250, weight(0.5)|head_armor(2), imodbits_cloth,[]],
#

["head_wrappings","Head Wrapping",[("head_wrapping",0)],
  itp_type_head_armor|itp_fit_to_head|itp_covers_hair_partially|itp_civilian|itp_merchandise,0,
  75, weight(0.25)|head_armor(5),imodbits_cloth],

["headband_black","Headband_with_Goggles", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_covers_hair_partially|itp_civilian, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@headband_black"),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),]),]],
["headband_black_scarf","Headband_with_Goggles_and_Face_Scarf", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_covers_hair_partially|itp_civilian|itp_covers_beard, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@headband_black"),
    (str_store_string, s2,"@upgrade_goggle"),
    (str_store_string, s3,"@upgrade_mask_1"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),
    (cur_item_add_mesh, s3),]),]],
["headband_white","Headband_with_Goggles", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_covers_hair_partially|itp_civilian, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@headband_white"),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),]),]],
["headband_white_scarf","Headband_with_Goggles_and_Face_Scarf", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_covers_hair_partially|itp_civilian|itp_covers_beard, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@headband_white"),
    (str_store_string, s2,"@upgrade_goggle"),
    (str_store_string, s4,"@upgrade_mask_1"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),
    (cur_item_add_mesh, s4),]),]],
["headband_red","Headband_with_Goggles", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_covers_hair_partially|itp_civilian, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@headband_red"),
    (str_store_string, s2,"@upgrade_goggle"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),]),]],
["headband_red_scarf","Headband_with_Goggles_and_Face_Scarf", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_covers_hair_partially|itp_civilian|itp_covers_beard, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@headband_red"),
    (str_store_string, s2,"@upgrade_goggle"),
    (str_store_string, s4,"@upgrade_mask_1"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),
    (cur_item_add_mesh, s4),]),]],
["headband_blue","Headband_with_Goggles", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_covers_hair_partially|itp_civilian, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
  (str_store_string, s1,"@headband_blue"),
  (str_store_string, s2,"@upgrade_goggle"),
  (cur_item_add_mesh, s1),
  (cur_item_add_mesh, s2),]),]],
["headband_blue_scarf","Headband_with_Goggles_and_Face_Scarf", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_covers_hair_partially|itp_civilian|itp_covers_beard, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
  (str_store_string, s1,"@headband_blue"),
  (str_store_string, s2,"@upgrade_goggle"),
  (str_store_string, s4,"@upgrade_mask_1"),
  (cur_item_add_mesh, s1),
  (cur_item_add_mesh, s2),
  (cur_item_add_mesh, s4),]),]],
["headband_camo","Headband_with_Goggles", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_covers_hair_partially|itp_civilian, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
  (str_store_string, s1,"@headband_camo"),
  (str_store_string, s2,"@upgrade_goggle"),
  (cur_item_add_mesh, s1),
  (cur_item_add_mesh, s2),]),]],
["headband_camo_scarf","Headband_with_Goggles_and_Face_Scarf", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_covers_hair_partially|itp_civilian|itp_covers_beard, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
  (str_store_string, s1,"@headband_camo"),
  (str_store_string, s2,"@upgrade_goggle"),
  (str_store_string, s4,"@upgrade_mask_1"),
  (cur_item_add_mesh, s1),
  (cur_item_add_mesh, s2),
  (cur_item_add_mesh, s4),]),]],
["headband_green","Headband_with_Goggles", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_covers_hair_partially|itp_civilian, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
  (str_store_string, s1,"@headband_green"),
  (str_store_string, s2,"@upgrade_goggle"),
  (cur_item_add_mesh, s1),
  (cur_item_add_mesh, s2),]),]],
["headband_green_scarf","Headband_with_Goggles_and_Face_Scarf", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_covers_hair_partially|itp_civilian|itp_covers_beard, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@headband_green"),
    (str_store_string, s2,"@upgrade_goggle"),
    (str_store_string, s4,"@upgrade_mask_1"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),
    (cur_item_add_mesh, s4),]),]],
["headband_pink","Headband_with_Goggles", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_covers_hair_partially|itp_civilian, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
  (str_store_string, s1,"@headband_pink"),
  (str_store_string, s2,"@upgrade_goggle"),
  (cur_item_add_mesh, s1),
  (cur_item_add_mesh, s2),]),]],
["headband_pink_scarf","Headband_with_Goggles_and_Face_Scarf", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_covers_hair_partially|itp_civilian|itp_covers_beard, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
  (str_store_string, s1,"@headband_pink"),
  (str_store_string, s2,"@upgrade_goggle"),
  (str_store_string, s4,"@upgrade_mask_1"),
  (cur_item_add_mesh, s1),
  (cur_item_add_mesh, s2),
  (cur_item_add_mesh, s4),]),]],

["hood_1","Hood",[("hood_1",0),("hood_diry_1",imodbit_tattered|imodbit_ragged)],itp_type_head_armor|itp_civilian|itp_attach_armature|itp_merchandise,0,
  125,weight(0.5)|head_armor(5)|body_armor(0),imodbits_cloth],
["hood_2","Hood",[("hood_2",0),("hood_diry_2",imodbit_tattered|imodbit_ragged)],itp_type_head_armor|itp_civilian|itp_attach_armature|itp_merchandise,0,
  125,weight(0.5)|head_armor(5)|body_armor(0),imodbits_cloth],
["hood_3","Hood",[("hood_3",0),("hood_diry_3",imodbit_tattered|imodbit_ragged)],itp_type_head_armor|itp_civilian|itp_attach_armature|itp_merchandise,0,
  125,weight(0.5)|head_armor(5)|body_armor(0),imodbits_cloth],
["hood_4","Hood",[("hood_4",0),("hood_diry_4",imodbit_tattered|imodbit_ragged)],itp_type_head_armor|itp_civilian|itp_attach_armature|itp_merchandise,0,
  125,weight(0.5)|head_armor(5)|body_armor(0),imodbits_cloth],
["hood_5","Hood",[("hood_5",0)],itp_type_head_armor|itp_attach_armature|itp_merchandise,0,
  1125,weight(0.5)|head_armor(6)|body_armor(0),imodbits_cloth],
["hood_6","Hood",[("hood_6",0)],itp_type_head_armor|itp_civilian|itp_attach_armature|itp_merchandise,0,
  1125,weight(0.5)|head_armor(6)|body_armor(0),imodbits_cloth],

["hood_brown_gasmask","Hood with Brown Gasmask",[("hood_brown_gasmask",0)],itp_type_head_armor|itp_attach_armature|itp_covers_head|itp_merchandise,0,
  425,weight(1.0)|head_armor(18)|body_armor(0),imodbits_cloth],

["hood_with_xm17","Hood with M17 Gasmask",[("hood_with_XM17",0)],itp_type_head_armor|itp_attach_armature|itp_covers_head|itp_merchandise,0,
  625,weight(1.5)|head_armor(21)|body_armor(0),imodbits_cloth],

["hood_white_helmet_black","Black Helmet with White Hood",[("hood_white_helmet_black",0)],itp_type_head_armor|itp_attach_armature,0,
  1250, weight(6)|head_armor(42), imodbits_armor],

["hood_red_helmet_black","Black Helmet with Red Hood",[("hood_red_helmet_black",0)],itp_type_head_armor|itp_attach_armature,0,
  1250, weight(6)|head_armor(42), imodbits_armor],

["hood_black","Hood", [("hood_black", 0)],
  itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,[]],
["hood_black_scarf","Hood_with_Face_Scarf", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard|itp_merchandise, 0,
  150, weight(0.6)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@hood_black"),
    (str_store_string, s2,"@upgrade_mask_1"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),]),]],
["hood_white","Hood", [("hood_white", 0)],
  itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,[]],
["hood_white_scarf","Hood_with_Face_Scarf", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard|itp_merchandise, 0,
  150, weight(0.6)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@hood_white"),
    (str_store_string, s2,"@upgrade_mask_1"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),]),]],
["hood_red","Hood", [("hood_red", 0)],
  itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,[]],
["hood_red_scarf","Hood_with_Face_Scarf", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard|itp_merchandise, 0,
  150, weight(0.6)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@hood_red"),
    (str_store_string, s2,"@upgrade_mask_1"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),]),]],

["jackal_helm_1","Jackal_Hood", [("jackal_helm_1", 0)], itp_type_head_armor|itp_attach_armature, 0,
  375, weight(2.5)|head_armor(15), imodbits_cloth, []],
["jackal_helm_1b","Jackal_Hood_with_Goggles", [("jackal_helm_1b", 0)], itp_type_head_armor|itp_attach_armature, 0,
  400, weight(3.0)|head_armor(18), imodbits_cloth, []],

["pot_helmet","Steel_Pot_Helmet", [("pot_helmet", 0)], itp_type_head_armor|itp_merchandise, 0,
  625, weight(2.5)|head_armor(25), imodbits_armor,[]],
["pot_helmet_goggles","Steel_Pot_Helmet_with_Goggles", [("dummy_mesh", 0)], itp_type_head_armor|itp_merchandise, 0,
  625, weight(2.5)|head_armor(25), imodbits_armor,
  [(ti_on_init_item,[
    (str_store_string, s1,"@pot_helmet"),
    (str_store_string, s2,"@pot_helmet.1"),
    (str_store_string, s3,"@upgrade_goggle"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),
    (cur_item_add_mesh, s3),]),]],
["pot_helmet_face_cover","Steel_Pot_Helmet_with_Goggles_and_Face_Cover", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_merchandise, 0,
  650, weight(2.5)|head_armor(26), imodbits_armor,
  [(ti_on_init_item,[
    (str_store_string, s1,"@pot_helmet"),
    (str_store_string, s2,"@pot_helmet.1"),
    (str_store_string, s3,"@upgrade_goggle"),
    (str_store_string, s4,"@upgrade_face_cover"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),
    (cur_item_add_mesh, s3),
    (cur_item_add_mesh, s4),]),]],

["metal_combat_helmet","Metal_Combat_Helmet", [("metal_combat_helmet", 0)], itp_type_head_armor|itp_merchandise, 0,
  700, weight(2)|head_armor(25), imodbits_armor, []],
["metal_combat_helmet_black","Metal_Combat_Helmet", [("metal_combat_helmet_black", 0)], itp_type_head_armor|itp_merchandise, 0,
  700, weight(2)|head_armor(25), imodbits_armor, []],
["metal_combat_helmet_medic","Metal_Combat_Helmet", [("metal_combat_helmet_medic", 0)], itp_type_head_armor|itp_merchandise, 0,
  700, weight(2)|head_armor(25), imodbits_armor, []],

["simple_helmet","Metal_Helmet", [("simple_helmet", 0)], itp_type_head_armor|itp_merchandise, 0,
  500, weight(2)|head_armor(20), imodbits_armor, []],
["simple_helmet_face_cover","Steel_Pot_Helmet_with_Face_Cover", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_merchandise, 0,
  650, weight(2)|head_armor(26), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@simple_helmet"),
    (cur_item_add_mesh, s1),

    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),

      (store_random_in_range,":rnd", 0, 4),
      (try_begin),
        (eq,":rnd",0),
        (str_store_string,s2,"@upgrade_face_cover"),
      (else_try),
        (eq,":rnd",1),
        (str_store_string,s2,"@upgrade_mask_1"),
      (else_try),
        (eq,":rnd",2),
        (str_store_string,s2,"@upgrade_mask_2"),
      (else_try),
        (str_store_string,s2,"@upgrade_mask_3"),
      (try_end),
      (cur_item_add_mesh,s2),
    (else_try),
      (str_store_string, s2,"@upgrade_face_cover"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],

["steel_helmet_1","Steel_Helmet", [("steel_helmet_1", 0),], itp_type_head_armor|itp_merchandise, 0,
  750, weight(3)|head_armor(30), imodbits_armor,[]],
["steel_helmet_1b","Steel_Helmet", [("steel_helmet_1b", 0),], itp_type_head_armor|itp_merchandise, 0,
  750, weight(3)|head_armor(30), imodbits_armor,[]],
["steel_helmet_1_face_cover","Steel_Helmet_with_Face_Cover", [("dummy_mesh", 0),], itp_type_head_armor|itp_merchandise, 0,
  775, weight(3)|head_armor(31), imodbits_armor,
  [(ti_on_init_item,[
      (str_store_string, s1,"@steel_helmet_1"),
      (cur_item_add_mesh, s1),
      (str_store_string, s2,"@upgrade_face_cover"),
      (cur_item_add_mesh, s2),]),]],
["steel_helmet_1b_face_cover","Steel_Helmet_with_Face_Cover", [("dummy_mesh", 0),], itp_type_head_armor|itp_merchandise, 0,
  775, weight(3)|head_armor(31), imodbits_armor,
  [(ti_on_init_item,[
      (str_store_string, s1,"@steel_helmet_1b"),
      (cur_item_add_mesh, s1),
      (str_store_string, s2,"@upgrade_face_cover"),
      (cur_item_add_mesh, s2),]),]],
["steel_helmet_1_gas","Steel_Helmet_with_Gas_Mask", [("dummy_mesh", 0),], itp_type_head_armor|itp_covers_head|itp_merchandise, 0,
  1125, weight(3.5)|head_armor(45), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),
    (str_store_string, s1,"@steel_helmet_1"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s3,"@upgrade_stormchaser"),
        (cur_item_add_mesh, s3),
      (try_end),
      (store_random_in_range,":rnd", 1, 2),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@gas_mask_ww"),
      (else_try),
        (str_store_string, s2,"@gas_mask_ww2"),
      (try_end),
      (cur_item_add_mesh, s2),
    (else_try),
      (str_store_string, s3,"@upgrade_stormchaser"),
      (str_store_string, s2,"@gas_mask_ww"),
      (cur_item_add_mesh, s3),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["steel_helmet_1b_gas","Steel_Helmet_with_Gas_Mask", [("dummy_mesh", 0),], itp_type_head_armor|itp_covers_head|itp_merchandise, 0,
  1125, weight(3.5)|head_armor(45), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),
    (str_store_string, s1,"@steel_helmet_1b"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s3,"@upgrade_stormchaser"),
        (cur_item_add_mesh, s3),
      (try_end),
      (store_random_in_range,":rnd", 1, 2),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@gas_mask_ww"),
      (else_try),
        (str_store_string, s2,"@gas_mask_ww2"),
      (try_end),
      (cur_item_add_mesh, s2),
    (else_try),
      (str_store_string, s3,"@upgrade_stormchaser"),
      (str_store_string, s2,"@gas_mask_ww"),
      (cur_item_add_mesh, s3),
      (cur_item_add_mesh, s2),
    (try_end),]),]],

["steel_helmet_2","Steel_Helmet", [("steel_helmet_2", 0),], itp_type_head_armor|itp_merchandise, 0,
  750, weight(3)|head_armor(30), imodbits_armor,[]],
["steel_helmet_3","Steel_Helmet", [("steel_helmet_3", 0),], itp_type_head_armor|itp_merchandise, 0,
  750, weight(3)|head_armor(30), imodbits_armor,[]],
["steel_helmet_2_face_cover","Steel_Helmet_with_Face_Cover", [("dummy_mesh", 0),], itp_type_head_armor|itp_merchandise, 0,
  775, weight(3)|head_armor(31), imodbits_armor,
  [(ti_on_init_item,[
      (str_store_string, s1,"@steel_helmet_2"),
      (cur_item_add_mesh, s1),
      (str_store_string, s2,"@upgrade_face_cover"),
      (cur_item_add_mesh, s2),]),]],
["steel_helmet_3_face_cover","Steel_Helmet_with_Face_Cover", [("dummy_mesh", 0),], itp_type_head_armor|itp_merchandise, 0,
  775, weight(3)|head_armor(31), imodbits_armor,
  [(ti_on_init_item,[
      (str_store_string, s1,"@steel_helmet_3"),
      (cur_item_add_mesh, s1),
      (str_store_string, s2,"@upgrade_face_cover"),
      (cur_item_add_mesh, s2),]),]],
["steel_helmet_2_gas","Steel_Helmet_with_Gas_Mask", [("dummy_mesh", 0),], itp_type_head_armor|itp_covers_head|itp_merchandise, 0,
  1125, weight(3.5)|head_armor(45), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),
    (str_store_string, s1,"@steel_helmet_2"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s3,"@upgrade_stormchaser"),
        (cur_item_add_mesh, s3),
      (try_end),
      (store_random_in_range,":rnd", 1, 2),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@gas_mask_ww"),
      (else_try),
        (str_store_string, s2,"@gas_mask_ww2"),
      (try_end),
      (cur_item_add_mesh, s2),
    (else_try),
      (str_store_string, s3,"@upgrade_stormchaser"),
      (str_store_string, s2,"@gas_mask_ww"),
      (cur_item_add_mesh, s3),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["steel_helmet_3_gas","Steel_Helmet_with_Gas_Mask", [("dummy_mesh", 0),], itp_type_head_armor|itp_covers_head|itp_merchandise, 0,
  1125, weight(3.5)|head_armor(45), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),
    (str_store_string, s1,"@steel_helmet_3"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s3,"@upgrade_stormchaser"),
        (cur_item_add_mesh, s3),
      (try_end),
      (store_random_in_range,":rnd", 1, 2),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@gas_mask_ww"),
      (else_try),
        (str_store_string, s2,"@gas_mask_ww2"),
      (try_end),
      (cur_item_add_mesh, s2),
    (else_try),
      (str_store_string, s3,"@upgrade_stormchaser"),
      (str_store_string, s2,"@gas_mask_ww"),
      (cur_item_add_mesh, s3),
      (cur_item_add_mesh, s2),
    (try_end),]),]],

["trench_helmet","Trench_Helmet", [("f_helmet", 0)], itp_type_head_armor|itp_merchandise, 0,
  950, weight(2.5)|head_armor(30), imodbits_armor, []],

["vintage_helm","Goggle_Helmet", [("vintage_helm", 0)], itp_type_head_armor|itp_merchandise, 0,
  625, weight(2)|head_armor(25), imodbits_armor, []],
["vintage_helm_scarf","Goggle_Helmet_with_Face_Cover", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_merchandise, 0,
  625, weight(2)|head_armor(26), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),
    (str_store_string, s2,"@vintage_helm"),
    (cur_item_add_mesh, s2),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 4),
      (try_begin),
        (eq,":rnd",0),
        (str_store_string,s1,"@upgrade_face_cover"),
      (else_try),
        (eq,":rnd",1),
        (str_store_string,s1,"@upgrade_mask_1"),
      (else_try),
        (eq,":rnd",2),
        (str_store_string,s1,"@upgrade_mask_2"),
      (else_try),
        (str_store_string,s1,"@upgrade_mask_3"),
      (try_end),
      (cur_item_add_mesh,s1),
    (else_try),
      (str_store_string, s1,"@upgrade_face_cover"),
      (cur_item_add_mesh, s1),
    (try_end),]),]],

["welder_mask","Welder_Mask", [("wielder_mask", 0)],itp_type_head_armor|itp_doesnt_cover_hair|itp_merchandise, 0,
  500, weight(1.5)|head_armor(20), imodbits_armor, []],
["welder_mask_ms","Makeshift_Welder_Mask", [("wielder_mask_ms", 0)],itp_type_head_armor|itp_doesnt_cover_hair|itp_merchandise, 0,
  250, weight(2.5)|head_armor(20), imodbits_armor, []],

["wooly_grey","Woolen Hat", [("dummy_mesh", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@wooly_grey"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),
    (store_random_in_range,":rnd", 0, 5),
    (try_begin),
      (eq,":rnd",1),
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),
    (else_try),
      (eq,":rnd",2),
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["wooly_red","Woolen Hat", [("dummy_mesh", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@wooly_red"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),
    (store_random_in_range,":rnd", 0, 5),
    (try_begin),
      (eq,":rnd",1),
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),
    (else_try),
      (eq,":rnd",2),
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["wooly_green","Woolen Hat", [("dummy_mesh", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@wooly_green"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),
    (store_random_in_range,":rnd", 0, 5),
    (try_begin),
      (eq,":rnd",1),
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),
    (else_try),
      (eq,":rnd",2),
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["wooly_black","Woolen Hat", [("dummy_mesh", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@wooly_black"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),
    (store_random_in_range,":rnd", 0, 5),
    (try_begin),
      (eq,":rnd",1),
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),
    (else_try),
      (eq,":rnd",2),
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["wooly_tan","Woolen Hat", [("dummy_mesh", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@wooly_tan"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),
    (store_random_in_range,":rnd", 0, 5),
    (try_begin),
      (eq,":rnd",1),
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),
    (else_try),
      (eq,":rnd",2),
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["wooly_blue","Woolen Hat", [("dummy_mesh", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  125, weight(0.25)|head_armor(5), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@wooly_blue"),
    (cur_item_add_mesh, s1),

    (ge,":agent",0),
    (lt,":troop",heroes_begin),
    (gt,":troop",0),
    (store_random_in_range,":rnd", 0, 5),
    (try_begin),
      (eq,":rnd",1),
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),
    (else_try),
      (eq,":rnd",2),
      (str_store_string, s2,"@upgrade_goggle"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["wooly_grey_scarf","Woolen Hat_with_Face_Scarf", [("dummy_mesh", 0)],itp_type_head_armor|itp_civilian|itp_covers_beard|itp_merchandise, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@wooly_grey"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (else_try),
        (eq,":rnd",2),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["wooly_red_scarf","Woolen Hat_with_Mask", [("dummy_mesh", 0)],itp_type_head_armor|itp_civilian|itp_covers_beard|itp_merchandise, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@wooly_red"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (else_try),
        (eq,":rnd",2),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["wooly_green_scarf","Woolen Hat_with_Mask", [("dummy_mesh", 0)],itp_type_head_armor|itp_civilian|itp_covers_beard|itp_merchandise, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@wooly_green"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (else_try),
        (eq,":rnd",2),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["wooly_black_scarf","Woolen Hat_with_Mask", [("dummy_mesh", 0)],itp_type_head_armor|itp_civilian|itp_covers_beard|itp_merchandise, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@wooly_black"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (else_try),
        (eq,":rnd",2),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["wooly_tan_scarf","Woolen Hat_with_Mask", [("dummy_mesh", 0)],itp_type_head_armor|itp_civilian|itp_covers_beard|itp_merchandise, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@wooly_tan"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (else_try),
        (eq,":rnd",2),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],
["wooly_blue_scarf","Woolen Hat_with_Mask", [("dummy_mesh", 0)],itp_type_head_armor|itp_civilian|itp_covers_beard|itp_merchandise, 0,
  150, weight(0.35)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@wooly_blue"),
    (cur_item_add_mesh, s1),
    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),
      (store_random_in_range,":rnd", 0, 5),
      (try_begin),
        (eq,":rnd",1),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (else_try),
        (eq,":rnd",2),
        (str_store_string, s2,"@upgrade_goggle"),
        (cur_item_add_mesh, s2),
      (try_end),
      (store_troop_faction, ":troop_faction", ":troop"),
      (try_begin),
        (this_or_next|eq, ":troop_faction", "fac_neutral"),
        (eq, ":troop_faction", "fac_commoners"),
        (str_store_string, s4,"@upgrade_covid_mask_cut"),
      (else_try),
        (store_random_in_range,":rnd", 0, 4),
        (try_begin),
          (eq,":rnd",0),
          (str_store_string,s4,"@upgrade_face_cover"),
        (else_try),
          (eq,":rnd",1),
          (str_store_string,s4,"@upgrade_mask_1"),
        (else_try),
          (eq,":rnd",2),
          (str_store_string,s4,"@upgrade_mask_2"),
        (else_try),
          (str_store_string,s4,"@upgrade_mask_3"),
        (try_end),
      (try_end),
      (cur_item_add_mesh,s4),
    (else_try),
      (str_store_string, s4,"@upgrade_mask_1"),
      (cur_item_add_mesh, s4),
    (try_end),]),]],

["zealot_helm_1","Madman Helmet", [("zealot_helm_1", 0)],
  itp_type_head_armor|itp_covers_hair_partially, 0,
  187, weight(2.5)|head_armor(15), imodbits_armor, []],

##################################################################################
## FACTIONS ##
##################################################################################
##Entenaii Empire
["entenaii_helmet","Entenaii_Infantry_Helmet", [("entenaii_helmet", 0)], itp_type_head_armor|itp_merchandise, 0,
  350, weight(2)|head_armor(27), imodbits_armor, []],
["entenaii_helmet_2","Entenaii_Infantry_Helmet", [("entenaii_helmet_2", 0)], itp_type_head_armor, 0,
  450, weight(2.5)|head_armor(31), imodbits_armor, []],
["entenaii_helmet_3","Entenaii_Infantry_Helmet", [("entenaii_helmet_3", 0)], itp_type_head_armor, 0,
  600, weight(3)|head_armor(37), imodbits_armor, []],
["entenaii_helmet_3_full","Entenaii_Infantry_Helmet", [("entenaii_helmet_3_full", 0)], itp_type_head_armor, 0,
  750, weight(3.5)|head_armor(43), imodbits_armor, []],
["entenaii_helmet_4","Entenaii_Cavalry_Helmet", [("entenaii_helmet_4", 0)], itp_type_head_armor, 0,
  1100, weight(3)|head_armor(51), imodbits_armor, []],
["entenaii_helmet_5","Entenaii_Guard_Helmet", [("entenaii_helmet_5", 0)], itp_type_head_armor, 0,
  1000, weight(5)|head_armor(49), imodbits_armor, []],
["entenaii_helmet_5_open","Entenaii_Guard_Helmet", [("entenaii_helmet_5_open", 0)], itp_type_head_armor, 0,
  925, weight(5)|head_armor(45), imodbits_armor, []],
["entenaii_helmet_lord","Entenaii_Lord_Helmet", [("entenaii_helmet_lord", 0)], itp_type_head_armor, 0,
  1200, weight(4.5)|head_armor(52), imodbits_armor, []],
["entenaii_helmet_lord_full","Entenaii_Lord_Helmet", [("entenaii_helmet_lord_full", 0)], itp_type_head_armor, 0,
  1350, weight(5)|head_armor(54), imodbits_armor, []],
["entenaii_fullhelm","Entenaii_Full_Helmet", [("entenaii_fullhelm", 0)], itp_type_head_armor, 0,
  1300, weight(5)|head_armor(53), imodbits_armor, []],

#
["entenaii_gasmask","Entenaii_Gasmask", [("entenaii_gasmask", 0)], itp_type_head_armor|itp_merchandise, 0,
  100, weight(2)|head_armor(10), imodbits_cloth, []],

["entenaii_helmet_gas","Entenaii_Infantry_Helmet_With_Gasmask", [("entenaii_helmet_gas", 0)], itp_type_head_armor|itp_merchandise, 0,
  360, weight(2)|head_armor(28), imodbits_armor, []],
["entenaii_helmet_2_gas","Entenaii_Infantry_Helmet_With_Gasmask", [("entenaii_helmet_2_gas", 0)], itp_type_head_armor, 0,
  460, weight(2.5)|head_armor(32), imodbits_armor, []],
["entenaii_helmet_3_gas","Entenaii_Infantry_Helmet_With_Gasmask", [("entenaii_helmet_3_gas", 0)], itp_type_head_armor, 0,
  610, weight(3)|head_armor(38), imodbits_armor, []],
["entenaii_helmet_lord_gas","Entenaii_Lord_Helmet_With_Gasmask", [("entenaii_helmet_lord_gas", 0)], itp_type_head_armor, 0,
  1210, weight(4.5)|head_armor(46), imodbits_armor, []],


#
["entenaii_beret","Entenaii_Specialist_Beret", [("beret_red", 0)], itp_type_head_armor|itp_doesnt_cover_hair, 0,
  550, weight(1)|head_armor(12), imodbits_armor, []],
#
["entenaii_helmet_emperor","Emperor_Helmet", [("entenaii_helmet_emperor", 0)], itp_type_head_armor|itp_attach_armature|itp_unique, 0,
  10000, weight(5)|head_armor(90), imodbits_armor, []],
#

##Entenaii Dominion
["dominion_recruit_helmet","Dominion_Recruit_Helmet", [("dominion_helmet_a", 0)], itp_type_head_armor|itp_merchandise, 0,
  325, weight(2)|head_armor(15), imodbits_armor, []],
["dominion_infantry_helmet","Dominion_Infantry_Helmet", [("dominion_helmet_b", 0)], itp_type_head_armor|itp_merchandise, 0,
  525, weight(2)|head_armor(20), imodbits_armor, []],
["dominion_sergeant_helmet","Dominion_Veteran_Helmet", [("dominion_helmet_c", 0)], itp_type_head_armor, 0,
  700, weight(2)|head_armor(25), imodbits_armor, []],
["dominion_raider_helmet","Dominion_Raider_Helmet", [("dominion_helmet_d", 0)], itp_type_head_armor, 0,
  740, weight(2)|head_armor(26), imodbits_armor, []],
["dominion_trench_helmet","Dominion_Trench_Helmet", [("dominion_trench_helmet_1", 0)], itp_type_head_armor, 0,
  800, weight(2)|head_armor(28), imodbits_armor, []],
#
["dominion_gasmask","Dominion_Gasmask", [("dominion_gasmask", 0)], itp_type_head_armor|itp_merchandise, 0,
  225, weight(1)|head_armor(10), imodbits_cloth, []],
["dominion_raider_helmet_gasmask","Dominion_Raider_Helmet_With_Gasmask", [("dominion_helmet_d_gas", 0)], itp_type_head_armor, 0,
  750, weight(2)|head_armor(27), imodbits_armor, []],
["dominion_trench_helmet_veiled","Dominion_Trench_Helmet_With_Veil", [("dominion_trench_helmet_1_veil", 0)], itp_type_head_armor, 0,
  900, weight(2.5)|head_armor(29), imodbits_armor, []],

["dominion_cavalry_helmet","Dominion_Rough-rider_Helmet", [("dominion_helmet_e", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(28), imodbits_armor, []],
["dominion_officer_helmet","Dominion_Officer_Helmet", [("dominion_helmet_f", 0)], itp_type_head_armor, 0,
  900, weight(2)|head_armor(30), imodbits_armor, []],
["dominion_officer_helmet_gasmask","Dominion_Officer_Helmet_With_Gasmask", [("dominion_helmet_f_gas", 0)], itp_type_head_armor, 0,
  910, weight(2)|head_armor(31), imodbits_armor, []],
#
["dominion_guard_helmet","Dominion_Guard_Helmet", [("dominion_helmet_f", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(28), imodbits_armor, []],
["dominion_castle_guard_helmet","Dominion_Castle_Guard_Helmet", [("dominion_helmet_g", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(29), imodbits_armor, []],
["dominion_hall_guard_helmet","Dominion_Viceregal_Guard_Helmet", [("dominion_helmet_g", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(30), imodbits_armor, []],
#
["dominion_fanatic_coif_a","Dominion_Fanatic_Coif", [("dominion_fanatic_coif_a", 0)], itp_type_head_armor|itp_merchandise, 0,
  225, weight(1)|head_armor(10), imodbits_cloth, []],
["dominion_fanatic_coif_b","Dominion_Fanatic_Coif", [("dominion_fanatic_coif_b", 0)], itp_type_head_armor|itp_merchandise, 0,
  225, weight(1)|head_armor(10), imodbits_cloth, []],
["dominion_fanatic_officer_coif","Dominion_Fanatic_Officer_Coif", [("dominion_fanatic_officer_coif", 0)], itp_type_head_armor|itp_merchandise, 0,
  400, weight(1)|head_armor(15), imodbits_cloth, []],
["dominion_fanatic_noble_coif_a","Dominion_Fanatic_Noble_Coif", [("dominion_fanatic_noble_coif_a", 0)], itp_type_head_armor, 0,
  1000, weight(1)|head_armor(20), imodbits_cloth, []],
["dominion_fanatic_noble_coif_c","Dominion_Fanatic_Noble_Coif", [("dominion_fanatic_noble_coif_c", 0)], itp_type_head_armor, 0,
  1000, weight(1)|head_armor(20), imodbits_cloth, []],
["dominion_fanatic_noble_mitre","Dominion_Fanatic_Noble_Mitre", [("dominion_fanatic_noble_mitre", 0)], itp_type_head_armor|itp_doesnt_cover_hair, 0,
  2000, weight(2)|head_armor(45), imodbits_cloth, []],
#
["beastling_head","Beastling_Head", [("beastling_1_head", 0)], itp_type_head_armor|itp_covers_head|itp_civilian|itp_unique, 0,
  0, weight(1)|head_armor(20), imodbits_none, []],
#
["dominion_governer_general_helmet","Governer_General_Helmet", [("dominion_fanatic_noble_mitre", 0)], itp_type_head_armor|itp_doesnt_cover_hair, 0,
  5000, weight(5)|head_armor(90), imodbits_cloth, []],
#

##Kingdom of Galvae
["galvae_mask_1","Galvae_Mask", [("galvae_mask_1", 0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian, 0,
  100, weight(2)|head_armor(8), imodbits_armor, []],
["galvae_mask_2","Galvae_Mask", [("galvae_mask_2", 0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian, 0,
  325, weight(2)|head_armor(12), imodbits_armor, []],
["galvae_mask_3","Galvae_Mask", [("galvae_mask_3", 0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian, 0,
  325, weight(2)|head_armor(15), imodbits_armor, []],
["galvae_mask_metal","Galvae_Metal_Mask", [("galvae_mask_metal", 0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian, 0,
  500, weight(2.5)|head_armor(20), imodbits_armor, []],
["galvae_mask_metal_2","Galvae_Metal_Mask", [("galvae_mask_metal_2", 0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian, 0,
  875, weight(2.5)|head_armor(25), imodbits_armor, []],
["galvae_battle_helmet","Galvae_Battle_Helmet", [("galvae_battle_helmet", 0)], itp_type_head_armor|itp_covers_beard|itp_civilian, 0,
  2500, weight(3)|head_armor(32), imodbits_armor, []],
["galvae_knight_helmet","Galvae_Knight_Helmet", [("galvae_knight_helmet", 0)], itp_type_head_armor|itp_covers_beard|itp_civilian, 0,
  3000, weight(3.5)|head_armor(40), imodbits_armor, []],
["galvae_mask_helmet","Galvae_Masked_Helmet", [("galvae_mask_helmet", 0)], itp_type_head_armor|itp_covers_beard|itp_civilian, 0,
  3500, weight(5)|head_armor(50), imodbits_armor, []],
["galvae_mask_helmet_royal","Galvae_Royal_Masked_Helmet", [("galvae_mask_helmet_royal", 0)], itp_type_head_armor|itp_covers_beard|itp_civilian, 0,
  8500, weight(5)|head_armor(65), imodbits_armor, []],

["galvae_taly_mask","Galvae_Taly_Mask", [("galvae_taly_mask", 0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian, 0,
  1500, weight(2.5)|head_armor(28), imodbits_armor, []],
["galve_veil_metal","Galve_Metal_Veil", [("galve_veil_metal", 0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian, 0,
  2200, weight(3.5)|head_armor(36), imodbits_armor, []],
["galvae_tanfen_mask","Galvae_Tanfen_Mask", [("galvae_falcon_hood", 0)], itp_type_head_armor|itp_civilian|itp_attach_armature, 0,
  7000, weight(1)|head_armor(58), imodbits_armor, []],

["galvae_masked_hood_1","Galvae_Masked_Hood_Black", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_attach_armature, 0,
  500, weight(3)|head_armor(18), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@hood_1"),
    (cur_item_add_mesh, s1),

    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),

      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",0),
        (str_store_string,s2,"@attach_galvae_mask_1"),
      (else_try),
        (eq,":rnd",1),
        (str_store_string,s2,"@attach_galvae_mask_2"),
      (try_end),
      (cur_item_add_mesh,s2),
    (else_try),
      (str_store_string, s2,"@attach_galvae_mask_1"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["galvae_masked_hood_2","Galvae_Masked_Hood_Grey", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_attach_armature, 0,
  500, weight(3)|head_armor(18), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@hood_2"),
    (cur_item_add_mesh, s1),

    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),

      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",0),
        (str_store_string,s2,"@attach_galvae_mask_1"),
      (else_try),
        (eq,":rnd",1),
        (str_store_string,s2,"@attach_galvae_mask_2"),
      (try_end),
      (cur_item_add_mesh,s2),
    (else_try),
      (str_store_string, s2,"@attach_galvae_mask_1"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["galvae_masked_hood_3","Galvae_Masked_Hood_Cream", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_attach_armature, 0,
  500, weight(3)|head_armor(18), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@hood_3"),
    (cur_item_add_mesh, s1),

    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),

      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",0),
        (str_store_string,s2,"@attach_galvae_mask_1"),
      (else_try),
        (eq,":rnd",1),
        (str_store_string,s2,"@attach_galvae_mask_2"),
      (try_end),
      (cur_item_add_mesh,s2),
    (else_try),
      (str_store_string, s2,"@attach_galvae_mask_1"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["galvae_masked_hood_4","Galvae_Masked_Hood_Brown", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_attach_armature, 0,
  500, weight(3)|head_armor(18), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@hood_4"),
    (cur_item_add_mesh, s1),

    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),

      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",0),
        (str_store_string,s2,"@attach_galvae_mask_1"),
      (else_try),
        (eq,":rnd",1),
        (str_store_string,s2,"@attach_galvae_mask_2"),
      (try_end),
      (cur_item_add_mesh,s2),
    (else_try),
      (str_store_string, s2,"@attach_galvae_mask_1"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["galvae_masked_hood_5","Galvae_Masked_Hood_Purple", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_attach_armature, 0,
  500, weight(3)|head_armor(18), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@hood_5"),
    (cur_item_add_mesh, s1),

    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),

      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",0),
        (str_store_string,s2,"@attach_galvae_mask_1"),
      (else_try),
        (eq,":rnd",1),
        (str_store_string,s2,"@attach_galvae_mask_2"),
      (try_end),
      (cur_item_add_mesh,s2),
    (else_try),
      (str_store_string, s2,"@attach_galvae_mask_1"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["galvae_masked_hood_6","Galvae_Masked_Hood_White", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_attach_armature, 0,
  500, weight(3)|head_armor(18), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@hood_6"),
    (cur_item_add_mesh, s1),

    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),

      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",0),
        (str_store_string,s2,"@attach_galvae_mask_1"),
      (else_try),
        (eq,":rnd",1),
        (str_store_string,s2,"@attach_galvae_mask_2"),
      (try_end),
      (cur_item_add_mesh,s2),
    (else_try),
      (str_store_string, s2,"@attach_galvae_mask_1"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],

["galvae_masked_metal_hood_1","Galvae_Metal_Masked_Hood_Black", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_attach_armature, 0,
  800, weight(4)|head_armor(26), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@hood_1"),
    (cur_item_add_mesh, s1),

    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),

      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",0),
        (str_store_string,s2,"@attach_galvae_mask_metal"),
      (else_try),
        (eq,":rnd",1),
        (str_store_string,s2,"@attach_galvae_mask_metal_2"),
      (try_end),
      (cur_item_add_mesh,s2),
    (else_try),
      (str_store_string, s2,"@attach_galvae_mask_metal"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["galvae_masked_metal_hood_2","Galvae_Metal_Masked_Hood_Grey", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_attach_armature, 0,
  800, weight(4)|head_armor(26), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@hood_2"),
    (cur_item_add_mesh, s1),

    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),

      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",0),
        (str_store_string,s2,"@attach_galvae_mask_metal"),
      (else_try),
        (eq,":rnd",1),
        (str_store_string,s2,"@attach_galvae_mask_metal_2"),
      (try_end),
      (cur_item_add_mesh,s2),
    (else_try),
      (str_store_string, s2,"@attach_galvae_mask_metal"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["galvae_masked_metal_hood_3","Galvae_Metal_Masked_Hood_Cream", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_attach_armature, 0,
  800, weight(4)|head_armor(26), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@hood_3"),
    (cur_item_add_mesh, s1),

    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),

      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",0),
        (str_store_string,s2,"@attach_galvae_mask_metal"),
      (else_try),
        (eq,":rnd",1),
        (str_store_string,s2,"@attach_galvae_mask_metal_2"),
      (try_end),
      (cur_item_add_mesh,s2),
    (else_try),
      (str_store_string, s2,"@attach_galvae_mask_metal"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["galvae_masked_metal_hood_4","Galvae_Metal_Masked_Hood_Brown", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_attach_armature, 0,
  800, weight(4)|head_armor(26), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@hood_4"),
    (cur_item_add_mesh, s1),

    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),

      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",0),
        (str_store_string,s2,"@attach_galvae_mask_metal"),
      (else_try),
        (eq,":rnd",1),
        (str_store_string,s2,"@attach_galvae_mask_metal_2"),
      (try_end),
      (cur_item_add_mesh,s2),
    (else_try),
      (str_store_string, s2,"@attach_galvae_mask_metal"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["galvae_masked_metal_hood_5","Galvae_Metal_Masked_Hood_Purple", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_attach_armature, 0,
  800, weight(4)|head_armor(26), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@hood_5"),
    (cur_item_add_mesh, s1),

    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),

      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",0),
        (str_store_string,s2,"@attach_galvae_mask_metal"),
      (else_try),
        (eq,":rnd",1),
        (str_store_string,s2,"@attach_galvae_mask_metal_2"),
      (try_end),
      (cur_item_add_mesh,s2),
    (else_try),
      (str_store_string, s2,"@attach_galvae_mask_metal"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
["galvae_masked_metal_hood_6","Galvae_Metal_Masked_Hood_White", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_beard|itp_attach_armature, 0,
  800, weight(4)|head_armor(26), imodbits_armor,
  [(ti_on_init_item,[
    (store_trigger_param_1,":agent"),
    (store_trigger_param_2,":troop"),

    (str_store_string, s1,"@hood_6"),
    (cur_item_add_mesh, s1),

    (try_begin),
      (ge,":agent",0),
      (lt,":troop",heroes_begin),
      (gt,":troop",0),

      (store_random_in_range,":rnd", 0, 2),
      (try_begin),
        (eq,":rnd",0),
        (str_store_string,s2,"@attach_galvae_mask_metal"),
      (else_try),
        (eq,":rnd",1),
        (str_store_string,s2,"@attach_galvae_mask_metal_2"),
      (try_end),
      (cur_item_add_mesh,s2),
    (else_try),
      (str_store_string, s2,"@attach_galvae_mask_metal"),
      (cur_item_add_mesh, s2),
    (try_end),]),]],
#
["galvae_royal_helmet","Royal_Helmet", [("galvae_king_helm", 0)], itp_type_head_armor|itp_covers_beard|itp_unique, 0,
  10000, weight(6)|head_armor(82), imodbits_armor, []],
##

##Molvat-Berchav Union
["union_coif","Union_Coif", [("union_coif", 0)], itp_type_head_armor|itp_merchandise, 0,
  255, weight(1)|head_armor(17), imodbits_cloth, []],
["union_helmet","Union_Infantry_Helmet", [("skull_cap_new", 0)], itp_type_head_armor|itp_merchandise, 0,
  475, weight(2)|head_armor(29), imodbits_armor, []],
["union_helmet_sergeant","Union_Sergeant_Helmet", [("union_sergeant_helmet", 0)], itp_type_head_armor, 0,
  595, weight(2)|head_armor(34), imodbits_armor, []],
["union_helmet_officer","Union_Officer_Helmet", [("chichak1", 0)], itp_type_head_armor, 0,
  785, weight(2)|head_armor(40), imodbits_armor, []],
["union_helmet_raider","Union_Raider_Helmet", [("union_raider_helmet", 0)], itp_type_head_armor|itp_attach_armature, 0,
  1200, weight(4)|head_armor(51), imodbits_armor, []],
["union_helmet_raider_2","Union_Raider_Helmet", [("union_raider_helmet_2", 0)], itp_type_head_armor|itp_attach_armature, 0,
  1250, weight(4)|head_armor(52), imodbits_armor, []],
["union_hood_sniper","Union_Snowstalker_Hood", [("union_snowstalker_coif", 0)], itp_type_head_armor|itp_merchandise, 0,
  400, weight(1)|head_armor(15), imodbits_cloth, []],
#
["union_young_culsar_helmet_1", "Union_Young_Culsar_Helmet", [("sturmhaube_1",0)],itp_type_head_armor|itp_merchandise ,0, 
  730 , weight(3.5)|abundance(10)|head_armor(28),imodbits_armor ],
["union_young_culsar_helmet_2", "Union_Young_Culsar_Helmet", [("sturmhaube_6",0)],itp_type_head_armor|itp_merchandise ,0, 
  730 , weight(3.5)|abundance(10)|head_armor(28),imodbits_armor ],
["union_culsar_helmet_1", "Union_Culsar_Helmet", [("sturmhaube_2",0)],itp_type_head_armor,0, 
  800 , weight(3.5)|abundance(10)|head_armor(34),imodbits_armor ],
["union_culsar_helmet_2", "Union_Culsar_Helmet", [("sturmhaube_3",0)],itp_type_head_armor,0, 
  800 , weight(3.5)|abundance(10)|head_armor(32),imodbits_armor ],
["union_culsar_helmet_3", "Union_Culsar_Helmet", [("sturmhaube_4",0)],itp_type_head_armor,0, 
  800 , weight(3.5)|abundance(10)|head_armor(32),imodbits_armor ],
["union_culsar_helmet_4", "Union_Culsar_Helmet", [("sturmhaube_7",0)],itp_type_head_armor,0, 
  800 , weight(3.5)|abundance(10)|head_armor(35),imodbits_armor ],
["union_veteran_culsar_helmet_1", "Union_Veteran_Culsar_Helmet", [("sturmhaube_5",0)],itp_type_head_armor,0, 
  980 , weight(3.5)|abundance(10)|head_armor(36),imodbits_armor ],
#
["union_diving_helmet", "Union_Marine_Diver_Helmet", [("diving_helmet",0)],itp_type_head_armor|itp_attach_armature,0, 
  4000 , weight(6.5)|abundance(10)|head_armor(45),imodbits_armor ],
#
["union_helmet_brotherhood", "Union_Brotherhood_Helmet", [("union_brotherhood_helmet",0)],itp_type_head_armor|itp_attach_armature,0, 
  1200 , weight(4)|abundance(10)|head_armor(42),imodbits_armor ],
#
["union_ravga_helmet","Union_Ravga_Head", [("ravga_head", 0)], itp_type_head_armor|itp_covers_head|itp_civilian|itp_attach_armature|itp_unique, 0,
  0, weight(1)|head_armor(40), imodbits_none, []],
["union_ravga_helmet_2","Union_Ravga_helmet", [("ravga_head", 0)], itp_type_head_armor|itp_covers_head|itp_civilian|itp_attach_armature|itp_unique, 0,
  0, weight(1)|head_armor(40), imodbits_none, []],
#
["union_tzar_helmet", "Tzar_Helmet", [("tzar_helmet",0)],itp_type_head_armor,0, 
  10000 , weight(5)|head_armor(84),imodbits_armor ],
##

##Vitzland Territories
["vitzland_recruit_helmet","Vitzland_Recruit_Helmet", [("vitzland_recruit_helmet", 0)], itp_type_head_armor|itp_merchandise, 0,
  325, weight(2)|head_armor(21), imodbits_armor, []],
["vitzland_helmet","Vitzland_Infantry_Helmet", [("vitzland_helmet", 0)], itp_type_head_armor|itp_merchandise, 0,
  525, weight(2)|head_armor(25), imodbits_armor, []],
["vitzland_helmet_2","Vitzland_Infantry_Helmet", [("vitzland_helmet_2", 0)], itp_type_head_armor|itp_merchandise, 0,
  550, weight(3)|head_armor(30), imodbits_armor, []],
["vitzland_salet_1","Vitzland_Salet", [("vitzland_salet_1", 0)], itp_type_head_armor, 0,
  725, weight(4)|head_armor(32), imodbits_armor, []],
["vitzland_salet_2","Vitzland_Raider_Helmet", [("vitzland_salet_2", 0)], itp_type_head_armor, 0,
  750, weight(4)|head_armor(37), imodbits_armor, []],
["vitzland_salet_3","Vitzland_Cavalry_Helmet", [("vitzland_salet_3", 0)], itp_type_head_armor, 0,
  800, weight(4)|head_armor(33), imodbits_armor, []],
["vitzland_salet_heavy","Vitzland_Heavy_Helmet", [("vitzland_salet_noble_open", 0)], itp_type_head_armor|itp_attach_armature, 0,
  950, weight(4)|head_armor(40), imodbits_armor, []],
["vitzland_salet_heavy_2","Vitzland_Heavy_Helmet", [("vitzland_salet_noble_closed", 0)], itp_type_head_armor|itp_attach_armature, 0,
  950, weight(4)|head_armor(40), imodbits_armor, []],
#
["vitzland_salet_guard","Vitzland_Guard_Helmet", [("vitzland_salet_guard", 0)], itp_type_head_armor|itp_attach_armature, 0,
  725, weight(4)|head_armor(35), imodbits_armor, []],
["vitzland_salet_guard_2","Vitzland_Guard_Helmet", [("vitzland_salet_guard_2", 0)], itp_type_head_armor|itp_attach_armature, 0,
  725, weight(4)|head_armor(39), imodbits_armor, []],
#
["nactman_head","Nactman_Head", [("nactman_head", 0)], itp_type_head_armor|itp_covers_head|itp_civilian|itp_unique, 0,
  0, weight(1)|head_armor(20), imodbits_none, []],
#
["vitzland_helmet_gasmask","Vitzland_Infantry_Helmet_With_Gasmask", [("vitzland_helmet_gasmask", 0)], itp_type_head_armor|itp_merchandise, 0,
  650, weight(4)|head_armor(35), imodbits_armor, []],
["vitzland_salet_1_gasmask","Vitzland_Salet_With_Gasmask", [("vitzland_salet_1_gasmask", 0)], itp_type_head_armor, 0,
  950, weight(6)|head_armor(42), imodbits_armor, []],
["vitzland_salet_3_gasmask","Vitzland_Salet_With_Gasmask", [("vitzland_salet_3_gasmask", 0)], itp_type_head_armor, 0,
  1450, weight(6.25)|head_armor(43), imodbits_armor, []],
#
["vitzland_salet_ubersto","Vitzland_Ubersto_Helmet", [("vitzland_salet_noble_open_plumed", 0)], itp_type_head_armor|itp_attach_armature, 0,
  1350, weight(4)|head_armor(44), imodbits_armor, []],
["vitzland_salet_ubersto_2","Vitzland_Ubersto_Helmet", [("vitzland_salet_noble_closed_plumed", 0)], itp_type_head_armor|itp_attach_armature, 0,
  1350, weight(4)|head_armor(44), imodbits_armor, []],
["vitzland_salet_nolte","Vitzland_Nolte_Helmet", [("vitzland_salet_nolte", 0)], itp_type_head_armor, 0,
  950, weight(4)|head_armor(30), imodbits_armor, []],
#
["vitzland_helmet_landansquet_1","Vitzland_Landansquet_Light_Helmet", [("vitzland_helmet_landansquet_1", 0)], itp_type_head_armor, 0,
  950, weight(4)|head_armor(35), imodbits_armor, []],
["vitzland_helmet_landansquet_2","Vitzland_Landansquet_Helmet", [("vitzland_helmet_landansquet_2", 0)], itp_type_head_armor, 0,
  1250, weight(4.5)|head_armor(38), imodbits_armor, []],
["vitzland_helmet_landansquet_3","Vitzland_Landansquet_Heavy_Helmet", [("vitzland_helmet_landansquet_3", 0)], itp_type_head_armor, 0,
  1850, weight(5)|head_armor(42), imodbits_armor, []],
#
["vitzland_kaiser_salet","Kaiser_Salet", [("vitzland_salet_kaiser", 0)], itp_type_head_armor, 0,
  15000, weight(6)|head_armor(85), imodbits_armor, []],
##

##Trezzo Republic ##
["republican_recruit_helmet","Republican_Recruit_Helmet", [("republican_helmet_1", 0)], itp_type_head_armor|itp_merchandise, 0,
  325, weight(2)|head_armor(30), imodbits_armor, []],
["republican_infantry_helmet","Republican_Syldati_Helmet", [("republican_helmet_2", 0)], itp_type_head_armor|itp_merchandise, 0,
  525, weight(2)|head_armor(31), imodbits_armor, []],
["republican_sergeant_helmet","Republican_Canorale_Helmet", [("republican_helmet_3", 0)], itp_type_head_armor, 0,
  700, weight(2)|head_armor(32), imodbits_armor, []],
["republican_raider_helmet","Republican_Servente_Helmet", [("republican_helmet_4", 0)], itp_type_head_armor, 0,
  720, weight(2)|head_armor(33), imodbits_armor, []],
["republican_cavalry_helmet","Republican_Cavalry_Helmet", [("republican_helmet_5", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(35), imodbits_armor, []],
["republican_officer_helmet","Republican_Senur_Helmet", [("republican_helmet_6", 0)], itp_type_head_armor, 0,
  900, weight(2)|head_armor(37), imodbits_armor, []],

["republican_guard_helmet","Republican_Vardina_Guarde_Helmet", [("republican_helmet_7", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(34), imodbits_armor, []],
["republican_guard_helmet_2","Republican_Vardina_Guarde_Helmet", [("republican_helmet_8", 0)], itp_type_head_armor, 0,
  980, weight(2)|head_armor(38), imodbits_armor, []],
["republican_castle_guard_helmet","Republican_Caratri_Guarde_Helmet", [("republican_helmet_9", 0)], itp_type_head_armor, 0,
  1200, weight(2)|head_armor(41), imodbits_armor, []],
["republican_hall_guard_helmet","Republican_Bellemeria_Guarde_Helmet", [("republican_helmet_10", 0)], itp_type_head_armor, 0,
  1500, weight(2)|head_armor(37), imodbits_armor, []],#
#
["republican_aux_helmet_1","Republican_Vencudi_Helmet", [("republican_vencudi_helmet_1", 0)], itp_attach_armature|itp_type_head_armor, 0,
  900, weight(2)|head_armor(35), imodbits_armor, []],
["republican_aux_helmet_2","Republican_Vencudi_Helmet", [("republican_vencudi_helmet_2", 0)], itp_attach_armature|itp_type_head_armor, 0,
  1000, weight(2)|head_armor(38), imodbits_armor, []],
["republican_aux_helmet_3","Republican_Vencudi_Helmet", [("republican_vencudi_helmet_3", 0)], itp_attach_armature|itp_type_head_armor, 0,
  1200, weight(2)|head_armor(40), imodbits_armor, []],
["republican_aux_helmet_4","Republican_Vencudi_Helmet", [("republican_vencudi_helmet_4", 0)], itp_attach_armature|itp_type_head_armor, 0,
  1500, weight(2)|head_armor(45), imodbits_armor, []],
#
["republican_noble_helmet", "Republican_Noble_Helmet", [("republican_noble_helmet_1",0)],itp_attach_armature|itp_type_head_armor ,0, 
  1000 , weight(3.5)|head_armor(45),imodbits_armor ],
["republican_noble_helmet_2", "Republican_Noble_Helmet", [("republican_noble_helmet_2",0)],itp_attach_armature|itp_type_head_armor,0, 
  2000 , weight(3.5)|head_armor(50),imodbits_armor ],
#
#
["republican_mastri_helmet","Republican_Mastri_Helmet", [("republican_mastri_helmet", 0)], itp_attach_armature|itp_type_head_armor, 0,
  15000, weight(4)|head_armor(75), imodbits_armor, []],
#
["republican_doge_helmet","Doge_Helmet", [("republican_doge_helmet", 0)], itp_attach_armature|itp_type_head_armor, 0,
  20000, weight(5)|head_armor(90), imodbits_armor, []],
##

##Itami Castedom ##
["itami_recruit_helmet","Itami_Recruit_Helmet", [("adventurer_foreign_kesoki_hat_1", 0)], itp_type_head_armor|itp_merchandise, 0,
  325, weight(2)|head_armor(15), imodbits_armor, []],
["itami_infantry_helmet","Itami_Infantry_Helmet", [("adventurer_foreign_kesoki_hat_1", 0)], itp_type_head_armor|itp_merchandise, 0,
  525, weight(2)|head_armor(20), imodbits_armor, []],
["itami_sergeant_helmet","Itami_Segeant_Helmet", [("adventurer_foreign_kesoki_hat_1", 0)], itp_type_head_armor, 0,
  700, weight(2)|head_armor(25), imodbits_armor, []],
["itami_raider_helmet","Itami_Raider_Helmet", [("adventurer_foreign_kesoki_hat_1", 0)], itp_type_head_armor, 0,
  740, weight(2)|head_armor(26), imodbits_armor, []],
["itami_cavalry_helmet","Itami_Cavalry_Helmet", [("adventurer_foreign_kesoki_hat_1", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(28), imodbits_armor, []],
["itami_officer_helmet","Itami_Officer_Helmet", [("adventurer_foreign_kesoki_hat_1", 0)], itp_type_head_armor, 0,
  900, weight(2)|head_armor(30), imodbits_armor, []],

["itami_guard_helmet","Itami_Guard_Helmet", [("adventurer_foreign_kesoki_hat_1", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(28), imodbits_armor, []],
["itami_castle_guard_helmet","Itami_Castle_Guard_Helmet", [("adventurer_foreign_kesoki_hat_1", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(29), imodbits_armor, []],
["itami_hall_guard_helmet","Itami_Hall_Guard_Helmet", [("adventurer_foreign_kesoki_hat_1", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(30), imodbits_armor, []],
#
["itami_noble_helmet", "Itami_Noble_Helmet", [("adventurer_foreign_kesoki_hat_1",0)],itp_type_head_armor ,0, 
  1000 , weight(3.5)|head_armor(45),imodbits_armor ],
#
["itami_amura_bloodblade_helmet", "Itami_Bloodblade_Helmet", [("itami_amura_bloodblade_helmet",0)],itp_type_head_armor,0, 
  2000,weight(3.5)|head_armor(48),imodbits_armor],
["itami_amura_bloodblade_helmet_2", "Itami_Bloodblade_Helmet", [("itami_amura_bloodblade_helmet_2",0)],itp_type_head_armor,0, 
  2100,weight(3.5)|head_armor(49),imodbits_armor],
["itami_amura_bloodblade_helmet_3", "Itami_Bloodblade_Helmet", [("itami_amura_bloodblade_helmet_3",0)],itp_type_head_armor,0, 
  2200,weight(3.5)|head_armor(50),imodbits_armor],
["itami_amura_bloodblade_helmet_4", "Itami_Bloodblade_Helmet", [("itami_amura_bloodblade_helmet_4",0)],itp_type_head_armor,0, 
  2300,weight(3.5)|head_armor(51),imodbits_armor],
["itami_amura_jetblade_helmet", "Itami_Jetblade_Helmet", [("itami_amura_jetblade_helmet",0)],itp_type_head_armor,0, 
  2500,weight(3.5)|head_armor(54),imodbits_armor],
["itami_amura_jetblade_helmet_2", "Itami_Jetblade_Helmet", [("itami_amura_jetblade_helmet_2",0)],itp_type_head_armor,0, 
  2600,weight(3.5)|head_armor(55),imodbits_armor],
["itami_amura_glassblade_helmet", "Itami_Glassblade_Helmet", [("itami_amura_glassblade_helmet",0)],itp_type_head_armor,0, 
  2900,weight(3.5)|head_armor(59),imodbits_armor],
["itami_amura_glassblade_helmet_2", "Itami_Glassblade_Helmet", [("itami_amura_glassblade_helmet_2",0)],itp_type_head_armor,0, 
  3000,weight(3.5)|head_armor(60),imodbits_armor],

#
["itami_kytra_helmet","Kytra_Helmet", [("adventurer_foreign_kesoki_hat_1", 0)], itp_type_head_armor, 0,
  20000, weight(5)|head_armor(90), imodbits_armor, []],
##

##Bashide Confederacy ##
["bashide_nerer_helmet","Bashide_Nerer_Helmet", [("bashide_nerer_helmet", 0)], itp_type_head_armor|itp_merchandise, 0,
  325, weight(2)|head_armor(15), imodbits_armor, []],
["bashide_onbar_helmet","Bashide_Onbar_Helmet", [("bashide_onbar_helmet", 0)], itp_type_head_armor|itp_merchandise, 0,
  525, weight(2)|head_armor(20), imodbits_armor, []],
["bashide_foruk_helmet","Bashide_Foruk_Helmet", [("bashide_foruk_helmet", 0)], itp_type_head_armor, 0,
  700, weight(2)|head_armor(25), imodbits_armor, []],
["bashide_foruk_helmet_2","Bashide_Foruk_Veteran_Helmet", [("bashide_foruk_helmet_2", 0)], itp_type_head_armor, 0,
  740, weight(2)|head_armor(26), imodbits_armor, []],
["bashide_anbati_helmet","Bashide_Anbati_Helmet", [("bashide_anbati_helmet", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(28), imodbits_armor, []],
["bashide_officer_helmet","Bashide_Senur_Helmet", [("bashide_officer_helmet", 0)], itp_type_head_armor, 0,
  900, weight(2)|head_armor(30), imodbits_armor, []],

["bashide_guard_helmet","Bashide_Vardina_Guarde_Helmet", [("bashide_guard_helmet", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(28), imodbits_armor, []],
["bashide_guard_helmet_2","Bashide_Vardina_Guarde_Helmet", [("bashide_guard_helmet_2", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(28), imodbits_armor, []],
["bashide_castle_guard_helmet","Bashide_Caratri_Guarde_Helmet", [("bashide_castle_guard_helm", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(29), imodbits_armor, []],
["bashide_hall_guard_helmet","Bashide_Bellemeria_Guarde_Helmet", [("bashide_hall_guard_helm", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(30), imodbits_armor, []],
#
["bashide_noble_helmet", "Bashide_Noble_Helmet", [("bashide_noble_helmet",0)],itp_type_head_armor ,0, 
  1000 , weight(3.5)|head_armor(45),imodbits_armor ],
["bashide_noble_helmet_2", "Bashide_Noble_Helmet", [("bashide_noble_helmet_2",0)],itp_type_head_armor,0, 
  2000 , weight(3.5)|head_armor(50),imodbits_armor ],
#
["bashide_gidon_headwrap_1", "Bashide_Gidon_Headwrap", [("bashide_gidon_headwrap_grey",0)],itp_type_head_armor ,0, 
  7000 , weight(1.5)|head_armor(45),imodbits_cloth],
["bashide_gidon_headwrap_2", "Bashide_Gidon_Headwrap", [("bashide_gidon_headwrap_black",0)],itp_type_head_armor ,0, 
  8000 , weight(1.5)|head_armor(49),imodbits_cloth],
["bashide_gidon_headwrap_3", "Bashide_Gidon_Headwrap", [("bashide_gidon_headwrap_black_2",0)],itp_type_head_armor ,0, 
  9600 , weight(2)|head_armor(52),imodbits_cloth],

#
["bashide_alran_helmet","Alran_Helmet", [("bashide_alran_helmet", 0)], itp_type_head_armor, 0,
  20000, weight(5)|head_armor(90), imodbits_armor, []],
##


## Renegades ##
["renegade_hat","Renegade_Hat", [("lakki", 0)], itp_type_head_armor|itp_merchandise, 0,
  100, weight(2)|head_armor(15), imodbits_cloth, []],
["renegade_infantry_helmet","Renegade_Infantry_Helmet", [("celtycka_lebka", 0)], itp_type_head_armor|itp_merchandise, 0,
  500, weight(2)|head_armor(29), imodbits_armor, []],
["renegade_sergeant_helmet","Renegade_Sergeant_Helmet", [("celtycka_iron", 0)], itp_type_head_armor, 0,
  700, weight(2)|head_armor(32), imodbits_armor, []],
["renegade_raider_helmet","Renegade_Raider_Helmet", [("frisian_helmet_mesh", 0)], itp_type_head_armor, 0,
  740, weight(2)|head_armor(33), imodbits_armor, []],
["renegade_cavalry_helmet","Renegade_Cavalry_Helmet", [("bowl_helmet", 0)], itp_type_head_armor, 0,
  780, weight(2)|head_armor(34), imodbits_armor, []],
["renegade_officer_helmet","Renegade_Officer_Helmet", [("conichelm", 0)], itp_type_head_armor, 0,
  900, weight(2)|head_armor(37), imodbits_armor, []],
#
["renegade_leader_helmet","Leader_Helmet", [("Rathos_bowl_helmet", 0)], itp_type_head_armor, 0,
  9000, weight(5)|head_armor(80), imodbits_armor, []],
##

##Theocracy of Throd ##
["throd_hood","Hood", [("throd_hood", 0)],
  itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  210, weight(1)|head_armor(10), imodbits_cloth,[]],
["throd_hood_2","Hood", [("throd_hood_2", 0)],
  itp_type_head_armor|itp_civilian, 0,
  400, weight(1.5)|head_armor(15), imodbits_cloth,[]],
["throd_hood_3","Hood", [("throd_hood_3", 0)],
  itp_type_head_armor|itp_civilian, 0,
  600, weight(1.5)|head_armor(20), imodbits_cloth,[]],
["throd_hood_theocracy","Theocracy_Hood", [("throd_hood_theocracy", 0)],
  itp_type_head_armor|itp_civilian, 0,
  1100, weight(3)|head_armor(40), imodbits_cloth,[]],
["throd_hood_god","Throd_Hood", [("throd_hood_god", 0)],
  itp_type_head_armor|itp_civilian, 0,
  3000, weight(5)|head_armor(65), imodbits_cloth,[]],

#
["throd_helmet","Throd_Helmet", [("throd_church_helmet", 0)], itp_type_head_armor, 0,
  1100, weight(5)|head_armor(35), imodbits_armor, []],
["throd_helmet_black","Black_Throd_Helmet", [("throd_church_helmet_black", 0)], itp_type_head_armor, 0,
  1400, weight(6)|head_armor(42), imodbits_armor, []],
##

##other

## Trench Knights ##
["trench_knight_helm","Trench_Knight_Helmet", [("trench_knight_helm", 0)], itp_type_head_armor|itp_merchandise, 0,
  1200, weight(5)|head_armor(40), imodbits_armor, []],
["trench_knight_helm_2","Trench_Knight_Helmet", [("trench_knight_helm_2", 0)], itp_type_head_armor|itp_merchandise, 0,
  1300, weight(5.5)|head_armor(41), imodbits_armor, []],
["trench_knight_helm_3","Trench_Knight_Helmet", [("trench_knight_helm_3", 0)], itp_type_head_armor|itp_merchandise, 0,
  1400, weight(5)|head_armor(42), imodbits_armor, []],
["trench_knight_helm_4","Trench_Knight_Helmet", [("trench_knight_helm_4", 0)], itp_type_head_armor|itp_merchandise, 0,
  1600, weight(5)|head_armor(43), imodbits_armor, []],
["trench_knight_helm_5","Trench_Knight_Helmet", [("trench_knight_helm_5", 0)], itp_type_head_armor|itp_merchandise, 0,
  1800, weight(5)|head_armor(44), imodbits_armor, []],
["trench_knight_helm_6","Trench_Knight_Helmet", [("trench_knight_helm_6", 0)], itp_type_head_armor|itp_attach_armature|itp_merchandise, 0,
  2000, weight(6)|head_armor(46), imodbits_armor, []],
["trench_knight_helm_6_c","Trench_Knight_Helmet", [("trench_knight_helm_6_closed", 0)], itp_type_head_armor|itp_attach_armature|itp_merchandise, 0,
  2000, weight(6)|head_armor(48), imodbits_armor, []],

#night_raiders
["night_raider_helm_1","Night_Raider_Helmet", [("night_raider_helm_1", 0)], itp_type_head_armor|itp_merchandise, 0,
  1200, weight(5)|head_armor(40), imodbits_armor, []],
["night_raider_helm_2","Night_Raider_Helmet", [("night_raider_helm_2", 0)], itp_type_head_armor|itp_merchandise, 0,
  1300, weight(5.5)|head_armor(41), imodbits_armor, []],
["night_raider_helm_3","Night_Raider_Helmet", [("night_raider_helm_3", 0)], itp_type_head_armor|itp_merchandise, 0,
  1400, weight(5.5)|head_armor(42), imodbits_armor, []],
["night_raider_helm_4","Night_Raider_Helmet", [("hell_helmet", 0)], itp_type_head_armor|itp_merchandise, 0,
  2600, weight(6.5)|head_armor(55), imodbits_armor, []],

["blackgod_knight_helmet","Night_Raider_Helmet", [("blackgod_knight_helmet", 0)], itp_type_head_armor|itp_merchandise, 0,
  1400, weight(5)|head_armor(42), imodbits_armor, []],

#shadow_operative
["shadow_operative_regular_helmet","Shadow_Operative_Helmet", [("myrmidon_helmet_4", 0)], itp_type_head_armor|itp_doesnt_cover_hair, 0,
  140, weight(3)|head_armor(15), imodbits_armor, []],
["shadow_operative_officer_cap","Shadow_Operative_Cap", [("shadow_operative_volk_cap", 0)], itp_type_head_armor|itp_doesnt_cover_hair, 0,
  670, weight(1)|head_armor(18), imodbits_cloth, []],
["shadow_operative_gunner_helmet","Shadow_Operative_Helmet", [("myrmidon_helmet_4", 0)], itp_type_head_armor|itp_doesnt_cover_hair, 0,
  880, weight(4)|head_armor(28), imodbits_armor, []],
["shadow_operative_saboteur_helmet","Shadow_Operative_Helmet", [("myrmidon_helmet_1", 0)], itp_type_head_armor|itp_doesnt_cover_hair, 0,
  1000, weight(5.5)|head_armor(30), imodbits_armor, []],
["shadow_operative_elite_cap","Shadow_Operative_Cap", [("shadow_operative_volk_cap", 0)], itp_type_head_armor|itp_doesnt_cover_hair, 0,
  860, weight(2)|head_armor(20), imodbits_cloth, []],
["shadow_operative_knight_helmet","Shadow_Operative_Helmet", [("myrmidon_helmet_2", 0)], itp_type_head_armor|itp_doesnt_cover_hair, 0,
  4500, weight(5.5)|head_armor(44), imodbits_armor, []],

#fallen_phalanx
["phalanx_fresh_helmet","Fallen_Phalanx_Helmet", [("phalanx_helmet_0", 0)], itp_type_head_armor|itp_attach_armature, 0,
  500, weight(3)|head_armor(32), imodbits_armor, []],
["phalanx_firstblood_helmet","Fallen_Phalanx_Helmet", [("phalanx_helmet_3", 0)], itp_type_head_armor|itp_attach_armature, 0,
  700, weight(3)|head_armor(35), imodbits_armor, []],
["phalanx_bloodied_helmet","Fallen_Phalanx_Helmet", [("phalanx_helmet_2", 0)], itp_type_head_armor|itp_attach_armature, 0,
  1100, weight(3.5)|head_armor(40), imodbits_armor, []],
["phalanx_scarred_helmet","Fallen_Phalanx_Helmet", [("phalanx_helmet_1", 0)], itp_type_head_armor|itp_attach_armature, 0,
  1500, weight(4)|head_armor(42), imodbits_armor, []],
["phalanx_chosen_helmet","Fallen_Phalanx_Helmet", [("phalanx_helmet_1_green", 0)], itp_type_head_armor|itp_attach_armature, 0,
  1900, weight(5)|head_armor(45), imodbits_armor, []],

["phalanx_flamer_helmet","Flmaer_Fallen_Phalanx_Helmet", [("phalanx_flamer_helmet", 0)], itp_type_head_armor|itp_attach_armature, 0,
  700, weight(3)|head_armor(35), imodbits_armor, []],

#adventurer_hats
["adventurer_black_hat", "Black_Adventurer_hat", [("adventurer_black_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_blue_hat", "Blue_Adventurer_hat", [("adventurer_blue_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_blue_red_hat", "Blue_Adventurer_hat", [("adventurer_blue_red_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_blue_yellow_hat", "Blue_Adventurer_hat", [("adventurer_blue_yellow_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_brown_hat", "Brown_Adventurer_hat", [("adventurer_brown_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_green_hat", "Green_Adventurer_hat", [("adventurer_green_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_grey_hat", "Grey_Adventurer_hat", [("adventurer_grey_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_grey_hat_2", "Grey_Adventurer_hat", [("adventurer_grey_hat_2",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_orange_hat", "Orange_Adventurer_hat", [("adventurer_orange_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_red_hat", "Red_Adventurer_hat", [("adventurer_red_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_red_yellow_hat", "Red_Adventurer_hat", [("adventurer_red_yellow_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_yellow_hat", "Yellow_Adventurer_hat", [("adventurer_yellow_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],

["adventurer_rough_black_hat", "Rough_Black_Adventurer_hat", [("adventurer_rough_black_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_rough_blue_hat", "Rough_Blue_Adventurer_hat", [("adventurer_rough_blue_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_rough_blue_red_hat", "Rough_Blue_Adventurer_hat", [("adventurer_rough_blue_red_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_rough_brown_hat", "Rough_Brown_Adventurer_hat", [("adventurer_rough_brown_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_rough_cream_hat", "Rough_Cream_Adventurer_hat", [("adventurer_rough_cream_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_rough_green_hat", "Rough_Green_Adventurer_hat", [("adventurer_rough_green_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],

["adventurer_bravado_grey_hat", "Bravado_Grey_Adventurer_hat", [("adventurer_bravado_grey_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_bravado_blue_hat", "Bravado_Blue_Adventurer_hat", [("adventurer_bravado_blue_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],

["adventurer_rich_black_hat", "Rich_Black_Adventurer_hat", [("adventurer_rich_black_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_rich_blue_hat", "Rich_Blue_Adventurer_hat", [("adventurer_rich_blue_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_rich_grey_hat", "Rich_Grey_Adventurer_hat", [("adventurer_rich_grey_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_rich_light_blue_hat", "Rich_Blue_Adventurer_hat", [("adventurer_rich_light_blue_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_rich_orange_hat", "Rich_Orange_Adventurer_hat", [("adventurer_rich_orange_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_rich_red_hat", "Rich_Red_Adventurer_hat", [("adventurer_rich_red_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_rich_white_hat", "Rich_White_Adventurer_hat", [("adventurer_rich_white_hat",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],

["adventurer_foreign_bashide_hat_1", "Bashide_Adventurer_hat", [("adventurer_foreign_bashide_hat_1",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_foreign_bashide_hat_2", "Bashide_Adventurer_hat", [("adventurer_foreign_bashide_hat_2",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_foreign_shonson_hat_1", "Shonson_Adventurer_hat", [("adventurer_foreign_shonson_hat_1",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_foreign_shonson_hat_2", "Shonson_Adventurer_hat", [("adventurer_foreign_shonson_hat_2",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_foreign_quvair_hat_1", "Quvair_Adventurer_hat", [("adventurer_foreign_quvair_hat_1",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_foreign_laloch_hat_1", "Laloch_Adventurer_hat", [("adventurer_foreign_laloch_hat_1",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_foreign_laloch_hat_2", "Laloch_Adventurer_hat", [("adventurer_foreign_laloch_hat_2",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_foreign_istak_hat_1", "Istak_Adventurer_hat", [("adventurer_foreign_istak_hat_1",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_foreign_istak_hat_2", "Istak_Adventurer_hat", [("adventurer_foreign_istak_hat_2",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_foreign_kesoki_hat_1", "Kesoki_Adventurer_hat", [("adventurer_foreign_kesoki_hat_1",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],
["adventurer_foreign_kesoki_hat_2", "Kesoki_Adventurer_hat", [("adventurer_foreign_kesoki_hat_2",0)],  itp_type_head_armor |itp_civilian|itp_merchandise|itp_attach_armature  ,0, 
  50 , weight(0.5)|abundance(80)|head_armor(5) ,imodbits_cloth ],

#candles
["candle_bandana_red","Red_Candle_Mask", [("red_candle_mask", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  180, weight(1)|head_armor(10), imodbits_cloth, []],
["candle_bandana_blue","Blue_Candle_Mask", [("blue_candle_mask", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  430, weight(1)|head_armor(14), imodbits_cloth, []],
["candle_bandana_black","Black_Candle_Mask", [("black_candle_mask", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  750, weight(1.5)|head_armor(18), imodbits_cloth, []],


#foreign
["yanizar_helmet_1","yanizar_Helmet", [("bork1", 0)], itp_type_head_armor|itp_merchandise, 0,
  250, weight(2)|head_armor(15), imodbits_armor, []],
["yanizar_helmet_2","yanizar_Helmet", [("bork2", 0)], itp_type_head_armor|itp_merchandise, 0,
  400, weight(2.5)|head_armor(20), imodbits_armor, []],

["winter_hat_1", "Winter_Hat", [("rus_cap_1",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0,
  60, weight(1)|abundance(70)|head_armor(16),imodbits_cloth],
["winter_hat_2", "Winter_Hat", [("rus_cap_2",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0,
  60, weight(1)|abundance(70)|head_armor(16),imodbits_cloth],
["winter_hat_b", "Winter_Hat", [("rus_cap_black",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0,
  80, weight(1)|abundance(70)|head_armor(18),imodbits_cloth],

["swamp_headwear_1","Bandit_Wrap", [("swamp_headwear_1", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  100, weight(0.5)|head_armor(5), imodbits_armor, []],
["swamp_headwear_2","Bandit_Wrap", [("swamp_headwear_2", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  100, weight(0.5)|head_armor(5), imodbits_armor, []],
["swamp_headwear_3","Bandit_Wrap", [("swamp_headwear_3", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  100, weight(0.5)|head_armor(5), imodbits_armor, []],

##civilian
["strawhat_1","Straw_Hat",[("strawhat_1",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0, 
  14 , weight(0.5)|abundance(100)|head_armor(7),imodbits_cloth ],
["strawhat_2","Straw_Hat",[("strawhat_2",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0, 
  14 , weight(0.5)|abundance(100)|head_armor(7),imodbits_cloth ],
["strawhat_3","Straw_Hat",[("strawhat_3",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0, 
  14 , weight(0.5)|abundance(100)|head_armor(7),imodbits_cloth ],
["strawhat_4","Straw_Hat",[("strawhat_4",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0, 
  14 , weight(0.5)|abundance(100)|head_armor(7),imodbits_cloth ],
["strawhat_5","Straw_Hat",[("strawhat_5",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0, 
  14 , weight(0.5)|abundance(100)|head_armor(7),imodbits_cloth ],
["strawhat_6","Straw_Hat",[("strawhat_6",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0, 
  14 , weight(0.5)|abundance(100)|head_armor(7),imodbits_cloth ],
["strawhat_7","Straw_Hat",[("strawhat_7",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0, 
  25 , weight(0.5)|abundance(100)|head_armor(8),imodbits_cloth ],

["peasant_cap_blue", "Peasant_Cap", [("woolen_cap_blu",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0,
  100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["peasant_cap_red", "Peasant_Cap", [("woolen_cap_red",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0,
  100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[], ],
["peasant_cap_green", "Peasant_Cap", [("woolen_cap_grn",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0,
  100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[], ],
["peasant_cap_black", "Peasant_Cap", [("woolen_cap_blk",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0,
  100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[], ],
["peasant_cap_white", "Peasant_Cap", [("woolen_cap_wht",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0,
  100, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth,[], ],

["admin_hat_blue", "Administrator_Hat", [("officerhatblue",0)],  itp_type_head_armor |itp_civilian|itp_merchandise  ,0, 
  130 , weight(0.5)|abundance(25)|head_armor(14),imodbits_cloth ],
["admin_hat_black", "Administrator_Hat", [("officerhatblack",0)],  itp_type_head_armor |itp_civilian|itp_merchandise  ,0, 
  130 , weight(0.5)|abundance(25)|head_armor(14),imodbits_cloth ],
["admin_hat_brown", "Administrator_Hat", [("officerhatbrown",0)],  itp_type_head_armor |itp_civilian|itp_merchandise  ,0, 
  130 , weight(0.5)|abundance(25)|head_armor(14),imodbits_cloth ],
 
["dominion_civ_hat_1", "Dominion_Civilian_Hat", [("dominion_civ_hat_1",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0,
  100, weight(1)|abundance(100)|head_armor(2),imodbits_cloth],
["cloth_hat_1", "Cloth_Hat", [("cloth_hat",0)],itp_type_head_armor|itp_civilian|itp_merchandise,0,
  100, weight(1)|abundance(100)|head_armor(2),imodbits_cloth],

#bandit
["bandit_helmet_1","Bandit_Helmet", [("bandit_helmet_1", 0)], itp_type_head_armor|itp_attach_armature|itp_merchandise, 0,
  500, weight(3.5)|head_armor(20), imodbits_armor, []],
["bandit_helmet_2","Bandit_Helmet", [("bandit_helmet_2", 0)], itp_type_head_armor|itp_attach_armature|itp_merchandise, 0,
  700, weight(3.5)|head_armor(22), imodbits_armor, []],
["bandit_helmet_2r","Bandit_Helmet", [("bandit_helmet_2r", 0)], itp_type_head_armor|itp_attach_armature|itp_merchandise, 0,
  750, weight(4)|head_armor(23), imodbits_armor, []],
["bandit_helmet_3","Bandit_Helmet", [("bandit_helmet_3", 0)], itp_type_head_armor|itp_attach_armature|itp_merchandise, 0,
  900, weight(4)|head_armor(26), imodbits_armor, []],
["bandit_helmet_3r","Bandit_Helmet", [("bandit_helmet_3r", 0)], itp_type_head_armor|itp_attach_armature|itp_merchandise, 0,
  950, weight(4.5)|head_armor(27), imodbits_armor, []],

["bandit_hood_blk","Hood", [("bandit_hood_blk", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,[]],
["bandit_hood_blk_scarf","Hood_with_Face_Scarf", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard|itp_merchandise, 0,
  150, weight(0.6)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@bandit_hood_blk"),
    (str_store_string, s2,"@upgrade_mask_1"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),]),]],

["bandit_hood_blu","Hood", [("bandit_hood_blu", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,[]],
["bandit_hood_blu_scarf","Hood_with_Face_Scarf", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard|itp_merchandise, 0,
  150, weight(0.6)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@bandit_hood_blu"),
    (str_store_string, s2,"@upgrade_mask_1"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),]),]],
  
["bandit_hood_grn","Hood", [("bandit_hood_grn", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,[]],
["bandit_hood_grn_scarf","Hood_with_Face_Scarf", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard|itp_merchandise, 0,
  150, weight(0.6)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@bandit_hood_grn"),
    (str_store_string, s2,"@upgrade_mask_1"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),]),]],
  
["bandit_hood_red","Hood", [("bandit_hood_red", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,[]],
["bandit_hood_red_scarf","Hood_with_Face_Scarf", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard|itp_merchandise, 0,
  150, weight(0.6)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@bandit_hood_red"),
    (str_store_string, s2,"@upgrade_mask_1"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),]),]],

["bandit_hood_wht","Hood", [("bandit_hood_wht", 0)], itp_type_head_armor|itp_civilian|itp_merchandise, 0,
  125, weight(0.5)|head_armor(5), imodbits_cloth,[]],
["bandit_hood_wht_scarf","Hood_with_Face_Scarf", [("dummy_mesh", 0)],
  itp_type_head_armor|itp_civilian|itp_covers_beard|itp_merchandise, 0,
  150, weight(0.6)|head_armor(6), imodbits_cloth,
  [(ti_on_init_item,[
    (str_store_string, s1,"@bandit_hood_wht"),
    (str_store_string, s2,"@upgrade_mask_1"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),]),]],

["bandit_fullhelm","Bandit_Heavy_Helmet", [("bandit_fullhelm", 0)], itp_type_head_armor|itp_merchandise, 0,
  1100, weight(3.5)|abundance(40)|head_armor(30), imodbits_armor, []],
["bandit_fullhelm2","Bandit_Heavy_Helmet", [("bandit_fullhelm2", 0)], itp_type_head_armor|itp_merchandise, 0,
  1100, weight(3.5)|abundance(40)|head_armor(30), imodbits_armor, []],

["bandit_knight_helm","Bandit_Knight_Helmet", [("bandit_knight_helm", 0)], itp_type_head_armor|itp_merchandise, 0,
  3800, weight(3.5)|abundance(40)|head_armor(40), imodbits_armor, []],
["bandit_knight_helm_rusty","Bandit_Rusty_Knight_Helmet", [("bandit_knight_helm_rusty", 0)], itp_type_head_armor|itp_merchandise, 0,
  1000, weight(3.5)|abundance(50)|head_armor(35), imodbits_armor, []],
["bandit_knight_helm_burnt","Bandit_Burnt_Knight_Helmet", [("bandit_knight_helm_burnt", 0)], itp_type_head_armor|itp_merchandise, 0,
  1200, weight(3.5)|abundance(45)|head_armor(38), imodbits_armor, []],

["bandit_knight_helm_black","Bandit_Knight_Black_Helmet", [("bandit_knight_helm_2", 0)], itp_type_head_armor|itp_merchandise, 0,
  4000, weight(3.5)|abundance(40)|head_armor(40), imodbits_armor, []],

["bandit_trench_helm","Bandit_Trench_Helmet", [("bandit_trench_helm", 0)], itp_type_head_armor|itp_merchandise, 0,
  5200, weight(5)|abundance(40)|head_armor(45), imodbits_armor, []],
["bandit_trench_helm_2","Bandit_Trench_Helmet", [("bandit_trench_helm_2", 0)], itp_type_head_armor|itp_merchandise, 0,
  5200, weight(5)|abundance(40)|head_armor(47), imodbits_armor, []],
["bandit_trench_helm_3","Bandit_Trench_Helmet", [("bandit_trench_helm_3", 0)], itp_type_head_armor|itp_merchandise, 0,
  5200, weight(5)|abundance(40)|head_armor(46), imodbits_armor, []],

["bandit_bulwark_helm","Bandit_Bulwark_Helmet", [("bandit_bulwark_helm", 0)], itp_type_head_armor|itp_merchandise, 0,
  5200, weight(5)|abundance(40)|head_armor(45), imodbits_armor, []],

#munition_bandits
["munition_bandit_helmet","Munition_Bandit_Helmet", [("munition_bandit_helmet", 0)], itp_type_head_armor, 0,
  5200, weight(5)|head_armor(40), imodbits_armor, []],
#horselords
#empty_ones
["empty_one_helmet","Empty_Ones_Helmet", [("empty_one_cap", 0)], itp_type_head_armor|itp_attach_armature, 0,
  2200, weight(3)|head_armor(30), imodbits_armor, []],


#
#veil
["veil_pink", "Pink Veil", [("veil_a",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_merchandise,0, 
  100 , weight(0.5)|abundance(100)|head_armor(5),imodbits_cloth ],
["veil_cream", "Cream Veil", [("veil_b",0)],  itp_type_head_armor | itp_civilian |itp_attach_armature|itp_merchandise,0, 
  100 , weight(0.5)|abundance(100)|head_armor(5),imodbits_cloth ],
["veil_blue", "Blue Veil", [("veil_d",0)],  itp_type_head_armor | itp_civilian |itp_attach_armature|itp_merchandise,0, 
  100 , weight(0.5)|abundance(100)|head_armor(5),imodbits_cloth ],
["veil_blue_2", "Blue Veil", [("veil_c",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_merchandise,0, 
  100 , weight(0.5)|abundance(100)|head_armor(5),imodbits_cloth ],
["veil_white", "White Veil", [("veil_e",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_merchandise,0, 
  100 , weight(0.5)|abundance(100)|head_armor(5),imodbits_cloth ],
["veil_green", "Green Veil", [("veil_f",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_merchandise,0, 
  100 , weight(0.5)|abundance(100)|head_armor(5),imodbits_cloth ],
["veil_grey", "Grey Veil", [("veil_g",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_merchandise,0, 
  100 , weight(0.5)|abundance(100)|head_armor(5),imodbits_cloth ],
["veil_grey_2", "Grey Veil", [("common_veil_a",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_merchandise,0, 
  100 , weight(0.5)|abundance(100)|head_armor(5),imodbits_cloth ],
["veil_cream_2", "Cream Veil", [("common_veil_b",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_merchandise,0, 
  100 , weight(0.5)|abundance(100)|head_armor(5),imodbits_cloth ],
["veil_brown", "Brown Veil", [("common_veil_d",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_merchandise,0, 
  100 , weight(0.5)|abundance(100)|head_armor(5),imodbits_cloth ],
["veil_orange", "Orange Veil", [("common_veil_c",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_merchandise,0, 
  100 , weight(0.5)|abundance(100)|head_armor(5),imodbits_cloth ],
["veil_striped", "Striped Veil", [("common_veil_e",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature|itp_merchandise,0, 
  100 , weight(0.5)|abundance(100)|head_armor(5),imodbits_cloth ],

#hooded cloak
["hooded_cloak_1", "Hooded_Cloak", [("cloak27",0)], itp_type_head_armor| itp_attach_armature| itp_fit_to_head|itp_merchandise,0, 
  193 , weight(2)|abundance(100)|head_armor(10)|body_armor(5)|leg_armor(3) ,imodbits_cloth ],
["hooded_cloak_2", "Hooded_Cloak", [("cloak28",0)], itp_type_head_armor| itp_attach_armature| itp_fit_to_head|itp_merchandise,0, 
  193 , weight(2)|abundance(100)|head_armor(10)|body_armor(5)|leg_armor(3) ,imodbits_cloth ],
["hooded_cloak_3", "Hooded_Cloak", [("cloak29",0)], itp_type_head_armor| itp_attach_armature| itp_fit_to_head|itp_merchandise,0, 
  193 , weight(2)|abundance(100)|head_armor(10)|body_armor(5)|leg_armor(3) ,imodbits_cloth ],
["hooded_cloak_4", "Hooded_Cloak", [("cloak30",0)], itp_type_head_armor| itp_attach_armature| itp_fit_to_head|itp_merchandise,0, 
  193 , weight(2)|abundance(100)|head_armor(10)|body_armor(5)|leg_armor(3) ,imodbits_cloth ],
["hooded_cloak_5", "Hooded_Cloak", [("cloak12",0)], itp_type_head_armor| itp_attach_armature| itp_fit_to_head|itp_merchandise,0, 
  193 , weight(2)|abundance(100)|head_armor(8)|body_armor(5)|leg_armor(3) ,imodbits_cloth ],

#totem
#
["bl_boar", "Boar Fur", [("BL_boar",0)], itp_type_head_armor| itp_attach_armature|itp_fit_to_head ,0,
  1580 , weight(3)|abundance(10)|head_armor(20)|body_armor(15)|leg_armor(0)|difficulty(4) ,imodbits_cloth],
["boar_helmet", "Boar Helmet", [("BL_boarhelmet",0)],  itp_type_head_armor|itp_civilian ,0,
  700 , weight(2)|abundance(30)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(3) ,imodbits_cloth],
#
["goat_cap", "Goat Cap", [("goat_cap",0)],  itp_type_head_armor|itp_civilian ,0,
  700 , weight(2)|abundance(30)|head_armor(18)|difficulty(3) ,imodbits_cloth],
["goat_hat", "Goat Hat", [("goat_bascinet",0)],  itp_type_head_armor|itp_civilian ,0,
  700 , weight(2)|abundance(30)|head_armor(22)|difficulty(3) ,imodbits_cloth],
#
["bear_helm", "Bear Helmet", [("bear_warior_helm",0)],  itp_type_head_armor|itp_civilian ,0,
  700 , weight(2)|abundance(30)|head_armor(28)|body_armor(2)|leg_armor(0)|difficulty(3) ,imodbits_cloth],
#
["wolf_helm", "Wolf Helmet", [("wolf_helm",0)],  itp_type_head_armor|itp_civilian ,0,
  700 , weight(2)|abundance(30)|head_armor(21)|difficulty(3) ,imodbits_cloth],
["wolf_helm_elder", "Elder Wolf Helmet", [("wolf_helm_elder",0)],  itp_type_head_armor|itp_civilian ,0,
  900 , weight(2)|abundance(20)|head_armor(26)|difficulty(3) ,imodbits_cloth],

#
["lobster", "Manhunter Helmet", [("lobster",0)],itp_type_head_armor ,0, 
  400 , weight(3.5)|abundance(10)|head_armor(30),imodbits_armor ],
["lobster2", "Manhunter Veteran Helmet", [("lobster2",0)],itp_type_head_armor ,0, 
  500 , weight(3.5)|abundance(10)|head_armor(33),imodbits_armor ],

["mp_helm", "Military_Police_Helmet", [("mp_helm",0)],itp_type_head_armor|itp_merchandise ,0, 
  400 , weight(3.5)|abundance(10)|head_armor(30),imodbits_armor ],
["mp_helm_1_raised", "Military_Police_Cage_Helmet", [("mp_helm_1_raised",0)],itp_type_head_armor ,0, 
  500 , weight(3.5)|abundance(10)|head_armor(33),imodbits_armor ],
["mp_helm_1", "Military_Police_Cage_Helmet", [("mp_helm_1",0)],itp_type_head_armor ,0, 
  500 , weight(3.5)|abundance(10)|head_armor(35),imodbits_armor ],

["cannibal_hood", "Cannibal_Hood", [("cannibal_hood_1",0)],itp_type_head_armor|itp_civilian|itp_attach_armature,0, 
  500,weight(1)|head_armor(22),imodbits_cloth],
["cannibal_hood_2", "Cannibal_Hood", [("cannibal_hood_2",0)],itp_type_head_armor|itp_civilian|itp_attach_armature,0, 
  550,weight(1)|head_armor(24),imodbits_cloth],
["cannibal_hood_3", "Cannibal_Hood", [("cannibal_hood_3",0)],itp_type_head_armor|itp_civilian|itp_attach_armature,0, 
  600,weight(1)|head_armor(26),imodbits_cloth],
["cannibal_hood_4", "Cannibal_Hood", [("cannibal_hood_4",0)],itp_type_head_armor|itp_civilian|itp_attach_armature,0, 
  650,weight(1.5)|head_armor(28),imodbits_cloth],
["cannibal_hood_5", "Cannibal_Hood", [("cannibal_hood_5",0)],itp_type_head_armor|itp_civilian|itp_attach_armature,0, 
  700,weight(1.5)|head_armor(30),imodbits_cloth],
["cannibal_hood_boss", "Cannibal_Hood", [("cannibal_hood_demon",0)],itp_type_head_armor|itp_civilian|itp_attach_armature,0, 
  950,weight(3)|head_armor(32),imodbits_cloth],
#
###############
#upgrades
["upgrade_glasses_dark","Dark Glasses", [("upgrade_glasses_dark", 0)],itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_merchandise, 0,
  125, weight(0.25)|head_armor(5), imodbits_none,[]],
["upgrade_glasses_dark_punk","Dark Glasses", [("upgrade_glasses_punk_dark", 0)],itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_merchandise, 0,
  125, weight(0.25)|head_armor(5), imodbits_none,[]],
["upgrade_bandage","Bandages", [("bandages", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_covers_beard|itp_merchandise, 0,
  25, weight(0.1)|head_armor(1), imodbits_cloth, []],
["upgrade_bandage_bloody","Bloody Bandages", [("bloody_bandages", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_covers_beard|itp_merchandise, 0,
  25, weight(0.1)|head_armor(1), imodbits_cloth, []],
["upgrade_church_tat","Cross_Face_Paint", [("upgrade_church_tat", 0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_unique, 0,
  1000, weight(0)|head_armor(1), imodbits_cloth, []],
["upgrade_church_tatb","Cross_Face_Paint", [("upgrade_church_tatb", 0)], itp_type_head_armor|itp_doesnt_cover_hair|itp_unique, 0,
  1000, weight(0)|head_armor(1), imodbits_cloth, []],
["upgrade_cigarette","Cigarette", [("upgrade_cigarette", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_merchandise, 0,
  25, weight(0)|head_armor(1), imodbits_none,[
      (ti_on_init_item, [
      (set_position_delta,0,25,0),
      (particle_system_add_new,"psys_gas_leak"),])]],
["upgrade_covid_mask","Mask", [("upgrade_covid_mask",0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_covers_beard, 0,
  25, weight(0.1)|head_armor(1)|body_armor(0),imodbits_cloth],
["upgrade_eyepatch_1","Eye_Patch", [("upgrade_eyepatch_1", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_merchandise, 0,
  25, weight(0.1)|head_armor(1), imodbits_none, []],
["upgrade_eyepatch_2","Glass_Eye_(w/Glass_Eye)", [("upgrade_eyepatch_2", 0)],itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_merchandise, 0,
  25, weight(0.1)|head_armor(1), imodbits_none, []],
["upgrade_face_scarf_1","Face_Scarf", [("upgrade_mask_1", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_covers_beard|itp_merchandise, 0,
  25, weight(0.1)|head_armor(1), imodbits_cloth, []],
["upgrade_face_scarf_2","Face_Scarf", [("upgrade_mask_2", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_covers_beard|itp_merchandise, 0,
  25, weight(0.1)|head_armor(1), imodbits_cloth, []],
["upgrade_face_scarf_3","Face_Scarf", [("upgrade_mask_3", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_covers_beard|itp_merchandise, 0,
  25, weight(0.1)|head_armor(1), imodbits_cloth, []],
["upgrade_face_cover","Face_Cover", [("upgrade_face_cover", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_covers_beard|itp_merchandise, 0,
  112, weight(0.25)|head_armor(5), imodbits_cloth,[]],
["upgrade_glasses","Glasses", [("cwr_glasses", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_merchandise, 0,
  75, weight(0.1)|head_armor(1), imodbits_none,[]],
["upgrade_glasses_punk","Glasses", [("upgrade_glasses_punk", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_merchandise, 0,
  75, weight(0.1)|head_armor(1), imodbits_none,[]],
["upgrade_goggle","Googles", [("upgrade_goggle", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_merchandise, 0,
  60, weight(0.25)|head_armor(5), imodbits_none, []],
["upgrade_sand_goggle","Googles", [("upgrade_sand_goggles", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_merchandise, 0,
  60, weight(0.25)|head_armor(5), imodbits_none, []],
["upgrade_headset_1","Feather", [("feather_1", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair, 0,
  125, weight(0.25)|head_armor(5), imodbits_none, []],
["upgrade_headset_2","Feather", [("feather_2", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair, 0,
  125, weight(0.25)|head_armor(5), imodbits_none, []],
["upgrade_iron_mask_1","Iron Mask", [("upgrade_iron_mask_1", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_covers_beard|itp_merchandise, 0,
  125, weight(2.5)|head_armor(10), imodbits_armor, []],
["upgrade_iron_mask_2","Iron Mask", [("upgrade_iron_mask_2", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_covers_beard|itp_merchandise, 0,
  125, weight(2.5)|head_armor(10), imodbits_armor, []],
["upgrade_iron_mask_3","Iron Mask", [("upgrade_iron_mask_3", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_covers_beard|itp_merchandise, 0,
  125, weight(2.5)|head_armor(10), imodbits_armor, []],
["upgrade_vision","Night Vision", [("upgrade_vision", 0)], itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair|itp_has_bayonet, 0,
  550, weight(0.5)|head_armor(1), imodbits_none, []],

##************************************************************************************************
## MELEE WEAPONS
##************************************************************************************************
##Unarmed##
# Brass knuckles
["brassknuckles","Brass_Knuckles", [("brassknuckles_R",0)], itp_type_hand_armor|itp_force_attach_right_hand|itp_force_show_left_hand|itp_force_show_right_hand|itp_merchandise, 0,
  50, weight(0.25)|body_armor(0),imodbits_mace],
["ironknuckles","Iron_Knuckles", [("ironknuckles_R",0)], itp_type_hand_armor|itp_force_attach_right_hand|itp_force_show_left_hand|itp_force_show_right_hand|itp_merchandise, 0,
  100, weight(0.25)|body_armor(0),imodbits_mace],

["studdedknuckles","Studded_Brass_Knuckles", [("studdedknuckles_R",0)], itp_type_hand_armor|itp_force_attach_right_hand|itp_force_show_left_hand|itp_force_show_right_hand|itp_merchandise, 0,
  150, weight(0.25)|body_armor(0),imodbits_mace],
["spikedknuckles","Spiked_Brass_Knuckles", [("spikedknuckles_R",0)], itp_type_hand_armor|itp_force_attach_right_hand|itp_force_show_left_hand|itp_force_show_right_hand|itp_merchandise, 0,
  150, weight(0.25)|body_armor(0),imodbits_mace],

["barbedknuckles","Barbed_Knuckles", [("handwraps_barbed_R",0)], itp_type_hand_armor|itp_force_attach_right_hand|itp_force_show_left_hand|itp_force_show_right_hand|itp_merchandise, 0,
  150, weight(0.25)|body_armor(0),imodbits_mace],

["axeknuckles","Bladed_Brass_Knuckles", [("axeknuckles_R",0)], itp_type_hand_armor|itp_force_attach_right_hand|itp_force_show_left_hand|itp_force_show_right_hand|itp_merchandise, 0,
  250, weight(0.25)|body_armor(0),imodbits_mace],
["clawknuckles","Brass_Claws", [("clawknuckles_R",0)], itp_type_hand_armor|itp_force_attach_right_hand|itp_force_show_left_hand|itp_force_show_right_hand|itp_merchandise, 0,
  500, weight(0.25)|body_armor(0),imodbits_mace],

#special
["renfieldgauntlet","Renfield_Gauntlet", [("renfield_gauntlet_R",0)], itp_type_hand_armor|itp_force_attach_right_hand|itp_force_show_left_hand|itp_force_show_right_hand, 0,
  50, weight(0.25)|body_armor(0),imodbits_mace],
  
# Power fist
["powerfist","Mechanical Club Gauntlet", [("powerfist_R",0)], itp_type_hand_armor|itp_force_attach_right_hand|itp_force_show_left_hand|itp_merchandise, 0,
  1500, weight(5)|abundance(10)|body_armor(0),imodbits_none,
  [(ti_on_init_item,[
  (store_trigger_param_1, ":agent"),
  (ge, ":agent", 1),
  (neq, ":agent", "$g_player"),
  (agent_ai_set_aggressiveness,":agent", 5000),
  (agent_get_wielded_item, ":wielded_0", ":agent", 0),
  (le, ":wielded_0", 0),
  (agent_get_wielded_item, ":wielded_1", ":agent", 1),
  (le, ":wielded_1", 0),
  (assign, ":continue", 1),
  (agent_get_troop_id,":troop", ":agent"),
  #(call_script, "script_equip_best_melee_weapon", ":agent", 1, 0, 0),
  (try_for_range, ":item_slot", ek_item_0, ek_head),
	  (eq, ":continue", 1),
	  (agent_get_item_slot, ":item", ":agent", ":item_slot"),
	  #(troop_get_inventory_slot, ":item", ":troop", ":item_slot"),
	  (gt, ":item", 0),
	  (item_get_type, ":weapon_type", ":item"),
	  #(try_begin),
		(eq, ":weapon_type", itp_type_shield),
		(agent_set_wielded_item, ":agent", ":item"),
		#(agent_equip_item, ":agent", ":item"),
		#(display_message, "@shield set 1"),
		(assign, ":continue", 0),
      #(try_end),
  (try_end),
  (eq, ":continue", 1),
  (agent_get_wielded_item, ":wielded_1", ":agent", 1),
  (le, ":wielded_1", 0),
  (try_for_range, ":item_slot", 10, 20),
	  (eq, ":continue", 1),
	  #(troop_get_, ":item", ":agent", ":item_slot"),
	  (troop_get_inventory_slot, ":item", ":troop", ":item_slot"),
	  (gt, ":item", 0),
	  (item_get_type, ":weapon_type", ":item"),
	  #(try_begin),
		(eq, ":weapon_type", itp_type_shield),
		#(agent_set_wielded_item, ":agent", ":item"),
		(agent_equip_item, ":agent", ":item"),
		#(display_message, "@shield set 2"),
		(assign, ":continue", 0),
      #(try_end),
  (try_end),
	]),
	]],
#####

## Weapons
# Clubs
["wooden_stick","Wooden_Stick",[("wooden_stick",0)],itp_type_one_handed_wpn|itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_merchandise,itc_scimitar|itcf_carry_mace_left_hip,
  5,weight(2.5)|spd_rtng(99)|weapon_length(63)|swing_damage(15,blunt),imodbits_polearm],
["wooden_stick_2","Wooden_Stick",[("wooden_stick_2",0)],itp_type_one_handed_wpn|itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_merchandise,itc_scimitar|itcf_carry_mace_left_hip,
  5,weight(2.5)|spd_rtng(99)|weapon_length(63)|swing_damage(15,blunt),imodbits_polearm],
["wooden_stick_3","Wooden_Stick",[("wooden_stick_3",0)],itp_type_one_handed_wpn|itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_merchandise,itc_scimitar|itcf_carry_mace_left_hip,
  5,weight(2.5)|spd_rtng(99)|weapon_length(63)|swing_damage(15,blunt),imodbits_polearm],
["wooden_stick_4","Wooden_Stick",[("wooden_stick_4",0)],itp_type_one_handed_wpn|itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_merchandise,itc_scimitar|itcf_carry_mace_left_hip,
  5,weight(2.5)|spd_rtng(99)|weapon_length(63)|swing_damage(15,blunt),imodbits_polearm],
["wooden_stick_5","Wooden_Stick",[("wooden_stick_5",0)],itp_type_one_handed_wpn|itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_merchandise,itc_scimitar|itcf_carry_mace_left_hip,
  5,weight(2.5)|spd_rtng(99)|weapon_length(63)|swing_damage(15,blunt),imodbits_polearm],
["wooden_stick_6","Wooden_Stick",[("wooden_stick_6",0)],itp_type_one_handed_wpn|itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_merchandise,itc_scimitar|itcf_carry_mace_left_hip,
  5,weight(2.5)|spd_rtng(99)|weapon_length(63)|swing_damage(15,blunt),imodbits_polearm],

["club","Club",[("club_swup",0),("club",imodbit_cracked|imodbit_bent),],itp_type_one_handed_wpn|itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack|itp_merchandise,itc_scimitar|itcf_carry_mace_left_hip,
  10,weight(2.5)|spd_rtng(98)|weapon_length(70)|swing_damage(20,blunt),imodbits_polearm],

["mace_1","Spiked_Trench_Club",[("mace_d",0)],itp_type_one_handed_wpn|itp_can_knock_down|itp_primary|itp_wooden_parry,itc_scimitar|itcf_carry_mace_left_hip,
  50,weight(2.5)|spd_rtng(98)|weapon_length(70)|swing_damage(20,pierce),imodbits_mace],
["mace_2","Spiked_Trench_Club",[("club_one",0)],itp_type_one_handed_wpn|itp_can_knock_down|itp_primary|itp_wooden_parry,itc_scimitar|itcf_carry_mace_left_hip,
  100,weight(2.5)|spd_rtng(98)|weapon_length(70)|swing_damage(23,pierce),imodbits_mace],

["long_spiked_club","Long_Spiked_Trench_Club",[("mace_long_c",0)],itp_type_two_handed_wpn|itp_can_knock_down|itp_primary|itp_wooden_parry,itc_staff|itcf_carry_axe_back,
  125,weight(3.5)|spd_rtng(95)|weapon_length(126)|swing_damage(20,pierce)|thrust_damage(20,blunt),imodbits_mace],

["big_club","Big_Club",[("cudgel_new",0)],itp_type_two_handed_wpn|itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack,itc_morningstar|itcf_carry_sword_back,
  50,weight(2.5)|spd_rtng(95)|weapon_length(71)|swing_damage(25,blunt),imodbits_polearm],

["big_spiked_club","Big_Spiked_Club",[("club1",0)],itp_type_two_handed_wpn|itp_wooden_parry|itp_primary|itp_can_knock_down,itc_greatsword|itcf_carry_sword_back,
  300,weight(3)|spd_rtng(95)|weapon_length(125)|swing_damage(30,pierce),imodbits_mace,[]],

["spiked_club","Spiked_Bastard_Club",[("spiked_club_swup",0)],itp_type_two_handed_wpn|itp_wooden_parry|itp_primary|itp_can_knock_down,itc_morningstar|itcf_carry_sword_back,
  150,weight(3)|spd_rtng(90)|weapon_length(74)|swing_damage(35,pierce),imodbits_mace,[]],

["baton_1","Baton",[("baton_1",0)],itp_type_one_handed_wpn|itp_primary|itp_can_knock_down,itc_scimitar,
  150,weight(3.5)|spd_rtng(95)|weapon_length(65)|swing_damage(25,blunt),imodbits_mace,[]],
["baton_2","Small Baton",[("baton_2", 0),],itp_type_one_handed_wpn|itp_primary|itp_can_knock_down,itc_scimitar,
  75,weight(2)|spd_rtng(97)|weapon_length(60)|swing_damage(22,blunt),imodbits_mace,[]],
["baton_3","Baton",[("baton_3", 0),],itp_type_two_handed_wpn|itp_primary|itp_can_knock_down,itc_morningstar|itcf_carry_sword_back,
  200,weight(4)|spd_rtng(91)|weapon_length(80)|swing_damage(28,blunt),imodbits_mace,[]],

# Common
["staff","Staff",[("wooden_staff_swup",0),("wooden_staff",imodbit_cracked|imodbit_bent),],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack|itp_merchandise,itc_staff|itcf_carry_sword_back,
  40,weight(1)|spd_rtng(100)|weapon_length(128)|swing_damage(15,blunt)|thrust_damage(20,blunt),imodbits_polearm],

["2by4","Two_by_Four_Board",[("twobyfour",0)],itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary,itcf_carry_sword_back|itc_nodachi,
  25,weight(2)|spd_rtng(90)|weapon_length(105)|swing_damage(20,blunt),imodbits_polearm,[],[]],
["2by4nails","Two_by_Four_Board_With_Nails",[("twobyfournails",0)],itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield,itcf_carry_sword_back|itc_nodachi,
  50,weight(2.5)|spd_rtng(85)|weapon_length(105)|swing_damage(20,pierce),imodbits_mace,[],[]],

["pitch_fork","Pitch_Fork",[("pitchfork",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_merchandise,itc_spear|itcf_carry_axe_back,
  25,weight(3)|spd_rtng(85)|weapon_length(137)|thrust_damage(25,pierce),imodbits_mace],

["crowbar","Crowbar",[("crowbar",0)],itp_type_two_handed_wpn|itp_wooden_parry|itp_primary|itp_can_knock_down,itc_morningstar|itcf_carry_mace_left_hip,
  100,weight(2)|spd_rtng(95)|weapon_length(67)|swing_damage(25,pierce),imodbits_mace,[]],

["wrench","Wrench",[("wrench",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_cleaver|itcf_carry_mace_left_hip,
  50,weight(0.5)|spd_rtng(105)|weapon_length(29)|swing_damage(20,blunt),imodbits_mace,[]],
["monkeywrench","Steel Pipe Wrench", [("monkeywrench", 0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_can_knock_down|itp_no_parry, itc_cleaver|itcf_carry_mace_left_hip,
  75, weight(3)|spd_rtng(85)|weapon_length(55)|swing_damage(25, blunt), imodbits_mace, []],

["screwdriver","Screwdriver",[("screwdriver",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itcf_thrust_onehanded,
  25,weight(0.25)|spd_rtng(110)|weapon_length(21)|thrust_damage(20,pierce),imodbits_mace],
["screwdriver2","Screwdriver",[("screwdriver2",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itcf_thrust_onehanded,
  25,weight(0.25)|spd_rtng(110)|weapon_length(21)|thrust_damage(20,pierce),imodbits_mace],

["shovel_short","Short_Shovel",[("shovel",0)],itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary,itcf_carry_axe_back|itc_bastardsword,
  150,weight(2.5)|difficulty(8)|spd_rtng(85)|weapon_length(74)|thrust_damage(20,cut)|swing_damage(25,blunt),imodbits_mace,[],[]],
["shovel","Shovel",[("rustyshovel",0)],itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary,itcf_carry_axe_back|itc_bastardsword,
  150,weight(2.5)|difficulty(8)|spd_rtng(80)|weapon_length(85)|thrust_damage(20,cut)|swing_damage(25,blunt),imodbits_mace,[],[]],

["hand_saw","Hand_Saw",[("hand_saw",0)],itp_type_one_handed_wpn|itp_no_parry|itp_wooden_parry|itp_primary|itp_secondary,itc_cleaver,
  50,weight(2)|spd_rtng(85)|weapon_length(69)|swing_damage(25,cut),imodbits_mace,[]],

# Pipes
["iron_pipe","Pipe",[("iron_pipe",0)],itp_type_one_handed_wpn|itp_primary|itp_can_knock_down,itc_scimitar|itcf_carry_mace_left_hip,
  10,weight(1.25)|spd_rtng(100)|weapon_length(53)|swing_damage(25,blunt),imodbits_mace,[],[]],

["lead_pipe","Lead_Pipe",[("lead_pipe",0)],itp_type_two_handed_wpn|itp_primary|itp_can_knock_down,itc_morningstar|itcf_carry_mace_left_hip,
  15,weight(2.5)|spd_rtng(98)|weapon_length(65)|swing_damage(25,blunt),imodbits_mace,[]],
["makeshift_pipe","Makeshift Pipe",[("makeshift_pipe",0)],itp_type_two_handed_wpn|itp_primary|itp_penalty_with_shield,itc_morningstar|itcf_carry_mace_left_hip,
  100,weight(5)|spd_rtng(85)|weapon_length(70)|swing_damage(35,cut),imodbits_mace,[]],

["iron_staff","Iron_Tube",[("iron_tube",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary,itc_staff|itcf_carry_sword_back,
  25,weight(3.5)|spd_rtng(95)|weapon_length(92)|swing_damage(25,blunt)|thrust_damage(25,blunt),imodbits_mace],

# Hammers
["hammer","Hammer",[("iron_hammer_new",0)],itp_type_one_handed_wpn|itp_can_knock_down|itp_primary|itp_secondary,itc_scimitar|itcf_carry_mace_left_hip,
  25,weight(1.5)|spd_rtng(95)|weapon_length(30)|swing_damage(25,blunt),imodbits_mace],
["hammer_big","Big Hammer",[("hammer_big",0)],itp_type_one_handed_wpn|itp_can_knock_down|itp_primary|itp_secondary,itc_scimitar|itcf_carry_mace_left_hip,
  75,weight(2.5)|spd_rtng(90)|weapon_length(53)|swing_damage(30,blunt),imodbits_mace],
["sledgehammer_small","Small_Sledgehammer",[("sledgehammer_small",0)],itp_crush_through|itp_type_one_handed_wpn|itp_can_knock_down|itp_primary|itp_wooden_parry|itp_unbalanced,itc_scimitar|itcf_carry_mace_left_hip,
  75,weight(5)|difficulty(12)|spd_rtng(80)|weapon_length(43)|swing_damage(30,blunt),imodbits_mace],
["sledgehammer","Sledgehammer",[("sledgehammer",0)],itp_crush_through|itp_type_two_handed_wpn|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_unbalanced,itc_nodachi|itcf_carry_spear,
  250,weight(7)|difficulty(12)|spd_rtng(80)|weapon_length(64)|swing_damage(40,blunt),imodbits_mace],

# Axes
["hatchet","Hatchet",[("hatchet_swup",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_scimitar|itcf_carry_axe_left_hip,
  25,weight(2)|spd_rtng(99)|weapon_length(43)|swing_damage(25,cut),imodbits_mace],
["hatchet_tactical","Tactical_Hatchet",[("hatchet_tactical",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield,itc_scimitar|itcf_carry_axe_left_hip,
  150,weight(2)|spd_rtng(95)|weapon_length(47)|swing_damage(35,cut),imodbits_mace],
["hand_axe","Axe",[("handaxe",0)],itp_type_two_handed_wpn|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield,itc_morningstar|itcf_carry_axe_left_hip,
  50,weight(2.5)|spd_rtng(95)|weapon_length(60)|swing_damage(30,cut),imodbits_mace,[]],
["one_handed_war_axe_a","Battle Axe",[("axe_war",0)],itp_type_two_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry,itc_morningstar|itcf_carry_axe_left_hip,
  100,weight(3.5)|difficulty(9)|spd_rtng(90)|weapon_length(55)|swing_damage(35,cut),imodbits_mace],

["battle_axe","Axe",[("axen",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry,itc_nodachi|itcf_carry_axe_back,
  240,weight(5)|difficulty(9)|spd_rtng(90)|weapon_length(77)|swing_damage(40,cut),imodbits_mace],
["war_axe","War_Axe",[("axe_big",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry,itc_nodachi|itcf_carry_axe_back,
  264,weight(5)|difficulty(10)|spd_rtng(88)|weapon_length(79)|swing_damage(45,cut),imodbits_mace],
["lumberjack_axe","Two_Handed_Axe",[("lumberjack_axe",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced,itc_nodachi|itcf_carry_axe_back,
  90,weight(4.5)|difficulty(9)|spd_rtng(90)|weapon_length(92)|swing_damage(35,cut),imodbits_mace],

["pickaxe","Pickaxe",[("pickaxe",0)],itp_type_two_handed_wpn|itp_primary|itp_wooden_parry|itp_bonus_against_shield,itc_morningstar|itcf_carry_mace_left_hip,
  50,weight(3)|spd_rtng(90)|weapon_length(52)|swing_damage(25,pierce),imodbits_mace],

# Spears
["shortened_spear","Shortened_Spear",[("spear_g_1-9m",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_wooden_parry|itp_merchandise,itc_spear|itcf_carry_spear,
  53,weight(2.0)|spd_rtng(102)|weapon_length(120)|swing_damage(20,blunt)|thrust_damage(25,pierce),imodbits_polearm],
["spear","Spear",[("spear",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_wooden_parry|itp_merchandise,itc_spear|itcf_carry_spear,
  85,weight(2.25)|spd_rtng(98)|weapon_length(120)|swing_damage(20,blunt)|thrust_damage(30,pierce),imodbits_polearm],

# Knifes
["practice_dagger","Practice_Dagger",[("practice_dagger",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack,itc_dagger,
  5,weight(0.5)|spd_rtng(110)|weapon_length(47)|swing_damage(10,blunt)|thrust_damage(15,blunt),imodbits_mace],
["simple_knife","Small Knife",[("simple_knife",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_merchandise,itc_dagger,
  12,weight(0.5)|spd_rtng(110)|weapon_length(19)|swing_damage(20,cut)|thrust_damage(25,pierce),imodbits_sword],
["knife","Knife",[("normal_knife",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_merchandise,itc_dagger,
  25,weight(0.5)|spd_rtng(110)|weapon_length(27)|swing_damage(20,cut)|thrust_damage(25,pierce),imodbits_sword],
["butchering_knife","Butchering_Knife",[("butchering_knife_new",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_merchandise,itc_dagger,
  50,weight(0.75)|spd_rtng(100)|weapon_length(36)|swing_damage(25,cut)|thrust_damage(25,pierce),imodbits_sword],
["bowie_knife","Bowie_Knife",[("tc_bowie",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_dagger,
  150,weight(0.75)|spd_rtng(105)|weapon_length(39)|swing_damage(25,cut)|thrust_damage(30,pierce),imodbits_sword_high],
["trench_knife","Trench_Knife",[("trench_knife",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_dagger,
  150,weight(0.75)|spd_rtng(110)|weapon_length(35)|swing_damage(25,blunt)|thrust_damage(25,pierce),imodbits_sword_high],
["cleaver","Cleaver",[("tc_cleaver",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry|itp_merchandise,itc_cleaver|itcf_carry_sword_left_hip,
  100,weight(1)|spd_rtng(99)|weapon_length(32)|swing_damage(30,cut),imodbits_sword_high],

# Kukri
["kukri","Kukri",[("kukri",0)],itp_type_one_handed_wpn|itp_primary,itc_longsword|itcf_carry_sword_left_hip,
  200,weight(1.5)|spd_rtng(99)|weapon_length(56)|thrust_damage(25,pierce)|swing_damage(30,cut),imodbits_sword,[]],
["kukri_rusty","Makeshift Kukri",[("kukri_rusty",0)],itp_type_one_handed_wpn|itp_primary,itc_longsword|itcf_carry_sword_left_hip,
  75,weight(1.5)|spd_rtng(99)|weapon_length(53)|thrust_damage(20,pierce)|swing_damage(25,cut),imodbits_sword,[]],
["kukri_old","Makeshift Kukri",[("kukri_old",0)],itp_type_one_handed_wpn|itp_primary,itc_longsword|itcf_carry_sword_left_hip,
  50,weight(1.5)|spd_rtng(99)|weapon_length(53)|thrust_damage(20,pierce)|swing_damage(20,cut),imodbits_sword,[]],

# Katana
["katana","Itami Officer Sword",[("shin_gunto",0),("shin_gunto_scab",ixmesh_carry)],itp_type_two_handed_wpn|itp_primary,itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn,
  1000,weight(1.5)|difficulty(8)|spd_rtng(99)|abundance(10)|weapon_length(98)|swing_damage(35,cut)|thrust_damage(30,pierce),imodbits_sword_high],

# Swords
["blade","Blade",[("blade",0)],itp_type_one_handed_wpn|itp_primary,itc_scimitar|itcf_carry_sword_left_hip,
  250,weight(3)|spd_rtng(95)|weapon_length(61)|swing_damage(30,cut)|thrust_damage(0,pierce),imodbits_sword],
["metal_blade","Metal_Blade",[("metal_blade",0)],itp_type_one_handed_wpn|itp_primary,itc_longsword|itcf_carry_sword_left_hip,
  150,weight(2.5)|spd_rtng(99)|weapon_length(52)|swing_damage(25,cut)|thrust_damage(30,pierce),imodbits_sword],

# Special
["shortened_military_scythe","Scythe",[("two_handed_battle_scythe_a",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary,itc_nodachi|itcf_carry_sword_back,
  264,weight(3.5)|difficulty(10)|spd_rtng(90)|weapon_length(112)|swing_damage(45,cut),imodbits_sword],
["staff_1","Staff",[("staff_1",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary,itc_staff|itcf_carry_sword_back,
  100,weight(2.5)|spd_rtng(95)|weapon_length(122)|swing_damage(25,blunt)|thrust_damage(25,blunt),imodbits_mace],

# others
["torch","Torch",[("club_swup",0)],itp_type_one_handed_wpn|itp_primary,itc_scimitar,
  10,weight(2.5)|spd_rtng(95)|weapon_length(70)|swing_damage(11,blunt),imodbits_none,
  [(ti_on_init_item,[(set_position_delta,0,60,0),(particle_system_add_new,"psys_torch_fire"),(particle_system_add_new,"psys_torch_smoke"),(set_current_color,150,130,70),(add_point_light,10,30),])]],
["flashlight","Lantern",[("flashlight",0)],itp_type_one_handed_wpn|itp_primary|itp_no_parry|itp_secondary,itc_cleaver,
  100,weight(1)|spd_rtng(99)|weapon_length(23)|swing_damage(20,blunt),imodbits_none],
["spyglass","Spyglass",[("newspy",0)],itp_type_one_handed_wpn|itp_primary|itp_no_parry|itp_secondary,itc_cleaver,
  100,weight(1)|spd_rtng(99)|weapon_length(23)|swing_damage(20,blunt),imodbits_none],
["steel_briefcase","Steel_Briefcase",[("steel_briefcase",0)],itp_type_one_handed_wpn|itp_primary,itc_scimitar,
  500,weight(2.5)|spd_rtng(85)|weapon_length(63)|swing_damage(15,blunt),imodbits_none,[]],
["leather_briefcase","Leather_Briefcase",[("leather_briefcase",0)],itp_type_one_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_primary,itc_scimitar,
  250,weight(2.5)|spd_rtng(90)|weapon_length(63)|swing_damage(10,blunt),imodbits_none,[]],

###############
##Barbed Wire###
###############
##Entenaii Empire
["ironclub", "Bar Mace", [("Faradon_IronClub",0)], itp_primary|itp_crush_through|itp_type_two_handed_wpn|itp_two_handed|itp_unbalanced|itp_can_knock_down, itc_nodachi, 
  1000, weight(5)|spd_rtng(77)|weapon_length(96)|swing_damage(44,blunt), imodbits_none], 

##Entenaii Dominion
["largeclub", "Warclub", [("Faradon_LargeClub",0)], itp_primary|itp_crush_through|itp_type_two_handed_wpn|itp_two_handed|itp_wooden_attack|itp_wooden_parry|itp_unbalanced|itp_can_knock_down, itc_nodachi, 
  900, weight(4)|spd_rtng(85)|weapon_length(92)|swing_damage(40,blunt), imodbits_none], 
["fanatic_staff","Fanatic_Staff",[("dominion_fanatic_noble_staff",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff,
  1400,weight(3)|spd_rtng(100)|weapon_length(128)|swing_damage(35,blunt)|thrust_damage(30,blunt),imodbits_polearm],

##Kingdom of Galvae
["ornate_seax", "Ornate Seax", [("ornate_seax",0),("ornate_seax_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 
  280,weight(0.5)|difficulty(0)|spd_rtng(92)|weapon_length(65)|swing_damage(14,cut)|thrust_damage(19,pierce),imodbits_sword,],
["shepherds_crook","Shepherd's Crook",[("shepherds_crook",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack|itp_merchandise,itc_staff|itcf_carry_sword_back,
  40,weight(1)|spd_rtng(100)|weapon_length(128)|swing_damage(15,blunt)|thrust_damage(20,blunt),imodbits_polearm],

["scottish_claymore", "Claymore", [("scottish_claymore",0)], itp_primary|itp_type_two_handed_wpn|itp_two_handed|itp_next_item_as_melee, itc_greatsword, 
  1000, weight(3)|abundance(15)|spd_rtng(88)|weapon_length(113)|swing_damage(41,cut)|thrust_damage(40,pierce), imodbits_sword_high], 
["scottish_claymore_alt_mode", "Claymore alt mode", [("scottish_claymore",0)], itp_primary|itp_type_polearm|itp_two_handed, itc_spear, 0, 
  weight(3)|spd_rtng(86)|weapon_length(113)|swing_damage(41,cut)|thrust_damage(40,pierce), imodbits_sword_high], 

["falx_1","Falx",[("falx_1",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary,itc_nodachi|itcf_carry_sword_back,
  1500,weight(3.5)|difficulty(10)|spd_rtng(90)|weapon_length(112)|swing_damage(40,cut),imodbits_sword],
["falx_2","Falx",[("falx_2",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary,itc_nodachi|itcf_carry_sword_back,
  1750,weight(3.5)|difficulty(10)|spd_rtng(92)|weapon_length(112)|swing_damage(44,cut),imodbits_sword],
["falx_3","Falx",[("falx_3",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary,itc_nodachi|itcf_carry_sword_back,
  2000,weight(3.5)|difficulty(10)|spd_rtng(96)|weapon_length(112)|swing_damage(48,cut),imodbits_sword],

["ossi_blade", "Os-si_Blade",[("ossi_blade",0),("ossi_blade_scab",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_unique, itc_scimitar|itcf_carry_sword_left_hip,
  8500,weight(0.4)|spd_rtng(102)|weapon_length(94)|swing_damage(42,cut),imodbits_sword_high ],
["ossi_blade_long","Os-si_Blade",[("ossi_blade_long",0),("ossi_blade_long_scab",ixmesh_carry)],itp_type_two_handed_wpn|itp_primary|itp_unique, itc_nodachi|itcf_carry_katana|itcf_show_holster_when_drawn,
  9000,weight(0.5)|difficulty(18)|spd_rtng(106)|abundance(10)|weapon_length(108)|swing_damage(45,cut)|thrust_damage(40,pierce),imodbits_sword_high],

##Molvat-Berchav Union
["ravensbeak", "Raven's Beak", [("ravensbeak",0)], itp_primary|itp_crush_through|itp_type_two_handed_wpn|itp_two_handed|itp_next_item_as_melee|itp_wooden_parry|itp_unbalanced|itp_can_knock_down, itc_nodachi|itcf_thrust_polearm, 
  850,weight(4)|abundance(18)|spd_rtng(90)|weapon_length(90)|swing_damage(40,blunt)|thrust_damage(36,pierce), imodbits_mace], 
["ravensbeak_alt_mode", "Raven's Beak alt mode", [("ravensbeak_alt",0)], itp_primary|itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry, itc_nodachi|itcf_thrust_polearm, 0, 
  weight(4)|spd_rtng(90)|weapon_length(90)|swing_damage(40,pierce)|thrust_damage(36,pierce), imodbits_none], 
["shashka", "Shashka", [("shashka",0)], itp_type_one_handed_wpn|itp_primary|itp_merchandise,itc_longsword|itcf_carry_sword_left_hip,
  300,weight(1.5)|spd_rtng(101)|weapon_length(100)|swing_damage(33,cut)|thrust_damage(22,pierce),imodbits_sword_high ],
["sovnya","Sovnya", [("sovnya",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
  450 , weight(4.5)|difficulty(0)|spd_rtng(88) | weapon_length(137)|swing_damage(34 , cut) | thrust_damage(22 ,  cut),imodbits_polearm ],
["sovnya_1","Brotherhood_Sovnya", [("sovnya_1",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
  650 , weight(4.5)|difficulty(0)|spd_rtng(92) | weapon_length(137)|swing_damage(38 , cut) | thrust_damage(22 ,  cut),imodbits_polearm ],

##Vitzland Territories
["flamberge", "Flamberge", [("flamberge",0)], itp_primary|itp_type_two_handed_wpn|itp_cant_use_on_horseback|itp_two_handed|itp_next_item_as_melee, itc_greatsword, 
  900, weight(4.5)|abundance(18)|spd_rtng(73)|weapon_length(139)|swing_damage(48,cut)|thrust_damage(36,pierce), imodbits_sword_high], 
["flamberge_alt_mode", "Flamberge alt mode", [("flamberge",0)], itp_primary|itp_crush_through|itp_type_polearm|itp_two_handed|itp_unbalanced, itc_spear, 0, 
  weight(4.5)|spd_rtng(73)|weapon_length(139)|swing_damage(48,cut)|thrust_damage(36,pierce), imodbits_sword_high], 
["blucher", "Blucher", [("blucher",0)], itp_type_one_handed_wpn|itp_primary|itp_merchandise,itc_scimitar|itcf_carry_sword_left_hip,
  320,weight(2.1)|spd_rtng(99)|weapon_length(120)|swing_damage(30,cut),imodbits_sword_high ],
["poleaxe", "Poleaxe", [("poleaxe1",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike, itc_parry_polearm|itcf_thrust_polearm|itcf_overswing_spear|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_carry_spear, 
  180 , weight(3.5)|difficulty(0)|spd_rtng(80) | weapon_length(150)|swing_damage(35 ,  pierce) | thrust_damage(35 ,  pierce),imodbits_polearm ], 

##Trezzo Republic
["cheap_rapier_1","Rapier", [("cheapsword1",0),("cheapsword1_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
  310 , weight(2.0)|difficulty(0)|spd_rtng(96) | weapon_length(90)|swing_damage(24 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["cheap_rapier_2","Rapier", [("cheapsword2",0),("cheapsword2_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
  325 , weight(2.0)|difficulty(0)|spd_rtng(97) | weapon_length(90)|swing_damage(25 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
["cheap_rapier_3","Rapier", [("cheapsword3",0),("cheapsword3_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
  340 , weight(2.0)|difficulty(0)|spd_rtng(98) | weapon_length(90)|swing_damage(26 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],
["cheap_rapier_4","Rapier", [("pappen1",0),("cheapsword3_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
  360 , weight(2.0)|difficulty(0)|spd_rtng(99) | weapon_length(90)|swing_damage(27 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],

["broadsword_1","Broad Sword", [("goodsword1",0),("goodsword1_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
  850 , weight(3.0)|difficulty(0)|spd_rtng(96) | weapon_length(100)|swing_damage(30 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
["broadsword_2","Broad Sword", [("goodsword2",0),("goodsword2_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
  875 , weight(3.0)|difficulty(0)|spd_rtng(97) | weapon_length(100)|swing_damage(31 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["noble_rapier","Rapier", [("goodrapier1",0),("goodrapier1_scab",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
  1000 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(95)|swing_damage(26 , cut) | thrust_damage(32 ,  pierce),imodbits_sword_high ],
["noble_rapier_1","Rapier", [("goodrapier2",0),("goodrapier2_scab",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
  1420 , weight(1.5)|difficulty(0)|spd_rtng(102) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(33 ,  pierce),imodbits_sword_high ],
["noble_rapier_2","Rapier", [("goodrapier3",0),("goodrapier3_scab",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
  1450 , weight(1.5)|difficulty(0)|spd_rtng(103) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(34 ,  pierce),imodbits_sword_high ],
["noble_rapier_3","Rapier", [("goodrapier4",0),("goodrapier4_scab",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
  1510 , weight(1.5)|difficulty(0)|spd_rtng(104) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(35 ,  pierce),imodbits_sword_high ],
#
["estoc", "Estoc", [("estoc",0)], itp_primary|itp_type_two_handed_wpn|itp_next_item_as_melee, itc_bastardsword|itcf_carry_sword_left_hip, 
  850, weight(3)|abundance(14)|spd_rtng(99)|weapon_length(114)|swing_damage(32,cut)|thrust_damage(46,pierce), imodbits_sword_high], 
["estoc_alt_mode", "Estoc alt mode", [("estoc",0)], itp_primary|itp_type_polearm, itc_spear|itcf_carry_sword_left_hip, 0, 
  weight(3)|spd_rtng(99)|weapon_length(114)|swing_damage(32,cut)|thrust_damage(46,pierce), imodbits_sword_high], 
#
["dueling_dagger_1","Ring and Quillion Dagger", [("antiquedagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_dagger|itcf_carry_dagger_front_left,
  125 , weight(0.5)|difficulty(0)|spd_rtng(110) | weapon_length(40)|swing_damage(21 , cut) | thrust_damage(19,pierce),imodbits_sword ],
["dueling_dagger_2","Ivory Hilt Dagger", [("ivoryhiltdagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_dagger|itcf_carry_dagger_front_left,
  125 , weight(0.5)|difficulty(0)|spd_rtng(110) | weapon_length(40)|swing_damage(21 , cut) | thrust_damage(19,pierce),imodbits_sword ],
#
["lord_rapier_1", "Cauncili Rapier", [("antique1",0)], itp_type_one_handed_wpn|itp_primary,itc_longsword|itcf_carry_sword_left_hip,
  394 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(10,cut) | thrust_damage(33,pierce),imodbits_sword_high ],
["lord_rapier_2", "Cauncili Rapier", [("ivoryhilt",0)], itp_type_one_handed_wpn|itp_primary,itc_longsword|itcf_carry_sword_left_hip,
  394 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(10,cut) | thrust_damage(33,pierce),imodbits_sword_high ],
#
["notte_rapier", "Blackened Rapier", [("blackenddueling",0)], itp_type_one_handed_wpn|itp_primary,itc_longsword|itcf_carry_sword_left_hip,
  1394 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(95)|swing_damage(30,cut) | thrust_damage(43,pierce),imodbits_sword_high ],
#
["doge_rapier", "Cup and Quillion Rapier", [("duelingsword",0)], itp_type_one_handed_wpn|itp_primary,itc_longsword|itcf_carry_sword_left_hip,
  2594 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(35,cut) | thrust_damage(48,pierce),imodbits_sword_high ],
#

##Itami Castedom
["boloknife", "Boloknife", [("boloknife",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 
  280,weight(1)|difficulty(0)|spd_rtng(93)|weapon_length(62)|swing_damage(18,cut)|thrust_damage(16,pierce),imodbits_sword,],

["toai", "Toai", [("toai",0),("toai_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
  105, weight(1.25)|difficulty(0)|spd_rtng(99)|weapon_length(85)|swing_damage(29,cut), imodbits_sword_high ],

["small_dadao", "Small_Dadao", [("small_dadao",0)], itp_type_one_handed_wpn|itp_primary|itp_merchandise,itc_longsword|itcf_carry_sword_left_hip,
  300,weight(1.5)|spd_rtng(101)|weapon_length(100)|swing_damage(33,cut)|thrust_damage(22,pierce),imodbits_sword_high ],

["dadao","Dadao",[("dadao",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary,itc_nodachi|itcf_carry_sword_back,
  264,weight(3.5)|difficulty(10)|spd_rtng(90)|weapon_length(112)|swing_damage(45,cut),imodbits_sword],

##Bashide Confederacy
["yaga", "Yaga", [("yaga",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  105, weight(1.25)|difficulty(0)|spd_rtng(99)|weapon_length(85)|swing_damage(29,cut), imodbits_sword_high ],

["tagan", "Tagan", [("tagan",0),("scab_tagan",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_merchandise, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
  105, weight(2.5)|difficulty(0)|spd_rtng(96)|weapon_length(73)|swing_damage(30,cut)|thrust_damage(0,pierce), imodbits_sword ],

##Renegade
["long_fighting_axe", "Long Fighting Axe", [("fighting_axe_new",0)], itp_primary|itp_type_two_handed_wpn|itp_two_handed, itc_nodachi|itcf_carry_mace_left_hip, 
  800, weight(5)|spd_rtng(91)|weapon_length(84)|swing_damage(44,pierce), imodbits_polearm], 
["lowlander_sword", "Lowlander Sword", [("lowlander_sword",0)], itp_primary|itp_type_two_handed_wpn|itp_two_handed|itp_next_item_as_melee, itc_greatsword, 
  780, weight(3.5)|abundance(16)|spd_rtng(82)|weapon_length(131)|swing_damage(42,cut)|thrust_damage(40,pierce), imodbits_sword_high], 
["lowlander_sword_alt_mode", "Lowlander Sword alt mode", [("lowlander_sword",0)], itp_primary|itp_type_polearm|itp_two_handed, itc_spear, 0, 
  weight(3.5)|spd_rtng(80)|weapon_length(131)|swing_damage(42,cut)|thrust_damage(40,pierce), imodbits_sword_high], 

##Throd
["throd_dagger_1","Ritual Dagger", [("uniquedagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_dagger|itcf_carry_dagger_front_left,
  1325 , weight(0.5)|difficulty(0)|spd_rtng(110) | weapon_length(55)|swing_damage(34 , cut) | thrust_damage(38,pierce),imodbits_sword ],
["miasma_pick","Miasma_Pick",[("crowbill",0)],itp_type_two_handed_wpn|itp_primary|itp_wooden_parry|itp_bonus_against_shield,itc_morningstar|itcf_carry_mace_left_hip,
  850,weight(6)|spd_rtng(99)|weapon_length(82)|swing_damage(38,pierce),imodbits_mace],


##other
["backsword", "Backsword", [("backsword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 
  300,weight(1)|difficulty(0)|spd_rtng(95)|weapon_length(57)|swing_damage(21,cut)|thrust_damage(12,pierce),imodbits_sword,],

["shovel_military","Military_Shovel",[("bsl110",0)],itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary,itcf_carry_axe_back|itc_bastardsword,
  150,weight(2.5)|difficulty(8)|spd_rtng(80)|weapon_length(66)|thrust_damage(20,cut)|swing_damage(25,blunt),imodbits_mace,[],[]],

["sharpened_stick","Sharpened_Stick",[("sharpened_stick",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_merchandise,itc_spear|itcf_carry_axe_back,
  25,weight(3)|spd_rtng(85)|weapon_length(105)|thrust_damage(20,pierce),imodbits_mace],
["bamboo_shortspear","Bamboo_Shortspear",[("bamboo_shortspear",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_merchandise,itc_spear|itcf_carry_axe_back,
  50,weight(2)|spd_rtng(90)|weapon_length(104)|thrust_damage(20,pierce),imodbits_mace],
["bamboo_spear","Bamboo_Spear",[("bamboo_spear",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_merchandise,itc_spear|itcf_carry_axe_back,
  120,weight(3.5)|spd_rtng(88)|weapon_length(171)|thrust_damage(20,pierce),imodbits_mace],
["bamboo_pike","Bamboo_Pike",[("bamboo_pike",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_merchandise,itc_spear|itcf_carry_axe_back,
  185,weight(4)|spd_rtng(85)|weapon_length(250)|thrust_damage(20,pierce),imodbits_mace],

["oar","Oar",[("oar",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_merchandise,itc_spear|itcf_carry_axe_back,
  105,weight(6)|spd_rtng(79)|weapon_length(280)|thrust_damage(18,blunt),imodbits_mace],

#gangs
#ashmaker
["ashmaker_war_club", "Ashmaker_War_Club", [("ashmaker_war_club",0)],itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  400, weight(2.5)|spd_rtng(88)|weapon_length(95)|swing_damage(28,pierce), imodbits_mace,
  [(ti_on_init_item,[(set_position_delta,0,60,0),(particle_system_add_new,"psys_torch_fire"),(particle_system_add_new,"psys_torch_smoke"),(set_current_color,150,130,70),(add_point_light,10,30),])]],
#
#munition_bandit
["grenade_club_1", "Grenade_Club", [("grenade_stick",0)],itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  100, weight(2)|spd_rtng(86)|weapon_length(53)|swing_damage(23,blunt), imodbits_none], 

#
["bastard_club_1", "Heavy Trench Club", [("mace_b",0)], itp_primary|itp_crush_through|itp_type_two_handed_wpn|itp_wooden_parry|itp_unbalanced|itp_can_knock_down|itp_merchandise, itc_morningstar|itcf_carry_mace_left_hip, 
  120, weight(1.1)|spd_rtng(94)|weapon_length(65)|swing_damage(33,blunt), imodbits_none],
["bastard_club_2", "Heavy Trench Club", [("bastard_mace_no1",0)], itp_primary|itp_crush_through|itp_type_two_handed_wpn|itp_wooden_parry|itp_unbalanced|itp_can_knock_down|itp_merchandise, itc_morningstar|itcf_carry_mace_left_hip, 
  250, weight(2.5)|spd_rtng(92)|weapon_length(92)|swing_damage(35,pierce), imodbits_none],

#trench clubs
["trench_club_1", "Trench Club", [("faradon_iberianmace",0)],itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  100, weight(2)|spd_rtng(86)|weapon_length(53)|swing_damage(20,blunt), imodbits_none], 
["trench_club_2", "Trench Club", [("cogwheelclub",0)],itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
  110, weight(2)|spd_rtng(87)|weapon_length(51)|swing_damage(21,blunt), imodbits_none],
["trench_club_3","Trench Club", [("club3",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  120 , weight(2.5)|spd_rtng(86) | weapon_length(70)|swing_damage(22 , blunt) ,imodbits_sword_high ],
["trench_club_4","Trench Club", [("kolben",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  130 , weight(2.0)|spd_rtng(92) | weapon_length(73)|swing_damage(23 , blunt),imodbits_sword_high ],
["trench_club_5","Trench Club", [("ball_mace_no1",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  140 , weight(2.0)|spd_rtng(88) | weapon_length(74)|swing_damage(24 , blunt),imodbits_sword_high ],
["trench_club_6","Trench Club", [("ball_mace_no2",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  150 , weight(2.0)|spd_rtng(90) | weapon_length(73)|swing_damage(25 , blunt),imodbits_sword_high ],
["trench_club_7","Trench Club", [("luc_studded_club",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  160 , weight(2.0)|spd_rtng(96) | weapon_length(69)|swing_damage(26 , blunt),imodbits_sword_high ],
["trench_club_8","Trench Club", [("mace_trails_no1",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  170 , weight(2.5)|spd_rtng(91) | weapon_length(70)|swing_damage(27 , blunt),imodbits_sword_high ],
["trench_club_9","Trench Club", [("romeyan_mace_1",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  180 , weight(2.0)|spd_rtng(92) | weapon_length(67)|swing_damage(28 , blunt),imodbits_sword_high ],
["trench_club_10","Trench Club", [("romeyan_mace_2",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  190 , weight(2.0)|spd_rtng(97) | weapon_length(67)|swing_damage(29 , blunt),imodbits_sword_high ],
["trench_club_11","Trench Club", [("serbian_knobbed_mace_a",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  200 , weight(2.0)|spd_rtng(98) | weapon_length(68)|swing_damage(30 , blunt),imodbits_sword_high ],
["trench_club_12","Trench Club", [("serbian_knobbed_mace_b",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  210 , weight(2.0)|spd_rtng(97) | weapon_length(68)|swing_damage(31 , blunt),imodbits_sword_high ],
["trench_club_13","Trench Club", [("serbian_knobbed_mace_c",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  220 , weight(2.0)|spd_rtng(92) | weapon_length(66)|swing_damage(32 , blunt),imodbits_sword_high ],
["trench_club_14","Trench Club", [("trenchclub",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  230 , weight(2.0)|spd_rtng(97) | weapon_length(41)|swing_damage(33 , blunt),imodbits_sword_high ],

["militia_hammer","Militia_Hammer", [("militia_hammer",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  100 , weight(4.5)|spd_rtng(89) | weapon_length(62)|swing_damage(22 , blunt),imodbits_sword_high ],

["long_trench_club_1","Trench Club", [("club1",0)], itp_type_two_handed_wpn|itp_primary, itc_morningstar|itcf_carry_sword_left_hip, 
  210 , weight(2.0)|difficulty(0)|spd_rtng(88) | weapon_length(126)|swing_damage(24 , blunt),imodbits_sword_high ],
["long_trench_club_2","Trench Club", [("club2",0)], itp_type_two_handed_wpn|itp_primary, itc_morningstar|itcf_carry_sword_left_hip, 
  200 , weight(3.0)|difficulty(0)|spd_rtng(89) | weapon_length(123)|swing_damage(22 , blunt),imodbits_sword_high ],

["bayonet_1","Bayonet",[("bayonet_1",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_dagger,
  150,weight(0.75)|spd_rtng(106)|weapon_length(40)|swing_damage(22,cut)|thrust_damage(33,pierce),imodbits_sword_high],
["bayonet_2","Bayonet",[("bayonet_2",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_dagger,
  110,weight(0.75)|spd_rtng(102)|weapon_length(32)|swing_damage(26,cut)|thrust_damage(26,pierce),imodbits_sword_high],
["bayonet_3","Bayonet",[("bayonet_3",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_dagger,
  80,weight(0.5)|spd_rtng(104)|weapon_length(28)|swing_damage(20,cut)|thrust_damage(22,pierce),imodbits_sword_high],
["bayonet_4","Bayonet",[("bayonet_4",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_dagger,
  120,weight(0.5)|spd_rtng(111)|weapon_length(57)|swing_damage(12,cut)|thrust_damage(35,pierce),imodbits_sword_high],
["bayonet_5","Bayonet",[("bayonet_5",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_dagger,
  130,weight(0.5)|spd_rtng(109)|weapon_length(31)|swing_damage(24,cut)|thrust_damage(30,pierce),imodbits_sword_high],
["bayonet_6","Bayonet",[("bayonet_6",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_dagger,
  130,weight(0.5)|spd_rtng(109)|weapon_length(31)|swing_damage(24,cut)|thrust_damage(30,pierce),imodbits_sword_high],
["bayonet_7","Bayonet",[("carcano_bayonet",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_dagger,
  130,weight(0.5)|spd_rtng(109)|weapon_length(31)|swing_damage(24,cut)|thrust_damage(30,pierce),imodbits_sword_high],

["trench_knife_1","Trench_Knife",[("trench_knife_1",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_dagger,
  165,weight(0.75)|spd_rtng(108)|weapon_length(32)|swing_damage(22,cut)|thrust_damage(26,pierce),imodbits_sword_high],

["carcanoknife","Fighting_Knife",[("carcanoknife",0),("carcanoknife_scab", ixmesh_carry)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_dagger|itcf_carry_dagger_front_right,
  165,weight(0.65)|spd_rtng(111)|weapon_length(22)|swing_damage(25,cut)|thrust_damage(29,pierce),imodbits_sword_high],
["fighting_knife_1","Fighting_Knife",[("nr40",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry,itc_dagger|itcf_carry_dagger_front_right,
  13,weight(0.5)|spd_rtng(112)|weapon_length(20)|swing_damage(25,cut)|thrust_damage(29,pierce),imodbits_sword_high],

["entrenching_tool","Entrenching_Tool",[("entrenching_tool",0)],itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_merchandise,itc_longsword|itcf_carry_axe_left_hip,
  110,weight(1)|spd_rtng(93)|weapon_length(58)|thrust_damage(20,cut)|swing_damage(25,cut),imodbits_polearm],
["entrenching_tool_2","Entrenching_Tool",[("mpl50",0)],itp_type_one_handed_wpn|itp_primary|itp_wooden_parry|itp_merchandise,itc_longsword|itcf_carry_axe_left_hip,
  100,weight(1)|spd_rtng(93)|weapon_length(41)|thrust_damage(20,cut)|swing_damage(25,cut),imodbits_polearm],

["saber1", "Sabre", [("saber",0),("saber_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_merchandise,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  280 , weight(1.5)|difficulty(0)|spd_rtng(102) | weapon_length(75)|swing_damage(30 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["light_cav_sword", "Light Cavalry Sword", [("1821_light_cavalry_sword",0),("saber_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_merchandise,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  500 , weight(1)|difficulty(0)|spd_rtng(105) | weapon_length(75)|swing_damage(32 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
["trooper_sword", "Trooper Sword", [("1864_trooper_sword",0),("saber_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_merchandise,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  150 , weight(2)|difficulty(0)|spd_rtng(99) | weapon_length(75)|swing_damage(28 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],
["persian_broadsword", "Sabre", [("persian_broadsword",0),("persian_sabre_a_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_merchandise,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  300 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(33 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
["turk_broadsword_a", "Sabre", [("turk_broadsword_a",0),("saber_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_merchandise,itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
  280 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(31 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
#
["wooden_sabre", "Wooden_Sabre", [("wooden_sabre",0)], itp_type_one_handed_wpn|itp_primary|itp_merchandise,itc_longsword|itcf_carry_sword_left_hip,
  220,weight(1.5)|abundance(20)|spd_rtng(96)|weapon_length(75)|swing_damage(27,blunt)|thrust_damage(23,blunt),imodbits_sword_high],


##
["austrian_hussar_sabre", "Sabre", [("austrian_hussar_sabre",0),("austrian_hussar_sabre_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 236, weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(95) | weapon_length(114)|swing_damage(33,cut)| thrust_damage(18,pierce),imodbits_sword_high ],
["british_infantry_sword", "Infantry_Sword", [("british_infantry_sword",0),("british_infantry_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 164, weight(1.25)|abundance(100)|difficulty(0)|spd_rtng(99) | weapon_length(84)|swing_damage(25,cut)| thrust_damage(25,pierce),imodbits_sword_high ],
["british_cavalry_sword", "Cavalry_Sword", [("british_cavalry_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 250, weight(2.00)|abundance(100)|difficulty(0)|spd_rtng(97) | weapon_length(101)|swing_damage(27,cut)| thrust_damage(24,pierce),imodbits_sword_high ],
["spanish_broadsword", "Broadsword", [("spanish_broadsword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 246, weight(2.00)|abundance(100)|difficulty(0)|spd_rtng(96) | weapon_length(109)|swing_damage(27,cut)| thrust_damage(27,pierce),imodbits_sword_high ],
["hungarian_sabre", "Cavalry_Sabre", [("hungarian_sabre",0),("hungarian_sabre_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 267, weight(2.00)|abundance(100)|difficulty(0)|spd_rtng(97) | weapon_length(106)|swing_damage(30,cut)| thrust_damage(23,pierce),imodbits_sword_high ],
["infantry_hanger", "Infantry_Hanger", [("infantry_hanger",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 110, weight(1.25)|abundance(100)|difficulty(0)|spd_rtng(102) | weapon_length(78)|swing_damage(26,cut)| thrust_damage(22,pierce),imodbits_sword_high ],
["officer_smallsword", "Officer's Small Sword", [("officer_smallsword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 315, weight(1.25)|abundance(100)|difficulty(0)|spd_rtng(104) | weapon_length(95)|swing_damage(18,cut)| thrust_damage(28,pierce),imodbits_sword_high ],
["polish_sabre", "Cavalry_Sabre", [("polish_sabre",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 212, weight(2.00)|abundance(100)|difficulty(0)|spd_rtng(96) | weapon_length(107)|swing_damage(31,cut)| thrust_damage(18,pierce),imodbits_sword_high ],
["german_dragoon_sword", "Dragoon_Sword", [("german_dragoon_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 223, weight(2.00)|abundance(100)|difficulty(0)|spd_rtng(96) | weapon_length(109)|swing_damage(26,cut)| thrust_damage(24,pierce),imodbits_sword_high ],
["french_grenadier_hanger", "Grenadier_Hanger", [("french_grenadier_hanger",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 200, weight(1.00)|abundance(100)|difficulty(0)|spd_rtng(101) | weapon_length(81)|swing_damage(28,cut)| thrust_damage(20,pierce),imodbits_sword_high ],
["infantry_sword", "Infantry_Sword", [("infantry_sword",0),("infantry_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 132, weight(1.75)|abundance(100)|difficulty(0)|spd_rtng(100) | weapon_length(90)|swing_damage(25,cut)| thrust_damage(23,pierce),imodbits_sword_high ],
["infantry_sword_2", "Infantry_Sword", [("infantry_sword_2",0),("infantry_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 132, weight(1.75)|abundance(100)|difficulty(0)|spd_rtng(100) | weapon_length(90)|swing_damage(25,cut)| thrust_damage(23,pierce),imodbits_sword_high ],

["spanish_cavalry_sword", "Cavalry_Sword", [("spanish_cavalry_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 245, weight(2.00)|abundance(100)|difficulty(0)|spd_rtng(96) | weapon_length(98)|swing_damage(29,cut)| thrust_damage(21,pierce),imodbits_sword_high ],
["dragoon_officer_sword", "Dragoon_Officer_Sword", [("spanish_dragoon_sword",0),("spanish_dragoon_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 284, weight(2.00)|abundance(100)|difficulty(0)|spd_rtng(98) | weapon_length(105)|swing_damage(29,cut)| thrust_damage(26,pierce),imodbits_sword_high ],
["scottish_broadsword", "Broadsword", [("scottish_broadsword",0),("scottish_broadsword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 278, weight(1.75)|abundance(100)|difficulty(0)|spd_rtng(98) | weapon_length(96)|swing_damage(28,cut)| thrust_damage(25,pierce),imodbits_sword_high ],
["spanish_cavalry_broadsword", "Cavalry_Broadsword", [("spanish_cavalry_broadsword",0),("spanish_cavalry_broadsword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 235, weight(1.75)|abundance(100)|difficulty(0)|spd_rtng(95) | weapon_length(107)|swing_damage(29,cut)| thrust_damage(24,pierce),imodbits_sword_high ],
["hungarian_grenadier_sword", "Grenadier_Sword", [("hungarian_grenadier_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 190, weight(1.50)|abundance(100)|difficulty(0)|spd_rtng(103) | weapon_length(73)|swing_damage(28,cut)| thrust_damage(23,pierce),imodbits_sword_high ],
["russian_shashka", "Shashka", [("russian_shashka",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 180, weight(1.75)|abundance(100)|difficulty(0)|spd_rtng(98) | weapon_length(93)|swing_damage(28,cut)| thrust_damage(25,pierce),imodbits_sword_high ],
["artillery_sword", "Artilleryman's_Sword", [("artillery_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 100, weight(1.50)|abundance(100)|difficulty(0)|spd_rtng(102) | weapon_length(60)|swing_damage(25,cut)| thrust_damage(25,pierce),imodbits_sword_high ],
["epee_du_soldat", "Epee_du_Soldat", [("epee_du_soldat",0),("epee_du_soldat_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 132, weight(1.50)|abundance(100)|difficulty(0)|spd_rtng(98) | weapon_length(95)|swing_damage(24,cut)| thrust_damage(27,pierce),imodbits_sword_high ],
["spanish_dragoon_sword", "Dragoon_Sword", [("spanish_dragoon_sword",0),("spanish_dragoon_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 284, weight(2.00)|abundance(100)|difficulty(0)|spd_rtng(96) | weapon_length(105)|swing_damage(29,cut)| thrust_damage(25,pierce),imodbits_sword_high ],
["old_schianova", "Schiavona", [("schianova",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 250, weight(1.50)|abundance(100)|difficulty(0)|spd_rtng(90) | weapon_length(95)|swing_damage(28,cut)| thrust_damage(23,pierce),imodbits_sword_high ],
##

["amura_sasu", "Amura_Sasu", [("amura_sasu",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_penalty_with_shield, itc_bastardsword|itcf_carry_sword_left_hip, 
  920, weight(1.5)|difficulty(9)|spd_rtng(99)|weapon_length(72)|swing_damage(32,cut)|thrust_damage(12,pierce), imodbits_sword_high],
["amura_sasu_long", "Amura_Long_Sasu", [("amura_sasu_long",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_penalty_with_shield, itc_bastardsword|itcf_carry_sword_left_hip, 
  1060, weight(1.5)|difficulty(10)|spd_rtng(95)|weapon_length(104)|swing_damage(35,cut)|thrust_damage(15,pierce), imodbits_sword_high],
["amura_sasu_great", "Amura_Great_Sasu", [("amura_sasu_great",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
  1920, weight(2.5)|difficulty(11)|spd_rtng(82)|weapon_length(142)|swing_damage(40,cut)|thrust_damage(18,pierce), imodbits_sword_high],


["lance_plain","Lance", [("lance_plain",0)], itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
  300 , weight(2.5)|difficulty(0)|spd_rtng(100) | weapon_length(210)|swing_damage(16 , blunt) | thrust_damage(35 ,  pierce),imodbits_polearm ],

["lance_entenaii","Entenaii_Lance", [("lance_entenaii",0)], itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
  340 , weight(2.5)|difficulty(0)|spd_rtng(100) | weapon_length(210)|swing_damage(16 , pierce) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["lance_dominion","Dominion_Lance", [("lance_dominion",0)], itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
  340 , weight(2.5)|difficulty(0)|spd_rtng(100) | weapon_length(210)|swing_damage(16 , pierce) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["lance_galvae","Galvae_Lance", [("lance_galvae",0)], itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
  340 , weight(2.5)|difficulty(0)|spd_rtng(100) | weapon_length(210)|swing_damage(16 , pierce) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["lance_union","Union_Lance", [("lance_union",0)], itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
  340 , weight(2.5)|difficulty(0)|spd_rtng(100) | weapon_length(210)|swing_damage(16 , pierce) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["lance_vitzland","Vitzland_Lance", [("lance_vitzland",0)], itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
  340 , weight(2.5)|difficulty(0)|spd_rtng(100) | weapon_length(210)|swing_damage(16 , pierce) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["lance_trezzo","Trezzo_Lance", [("lance_trezzo",0)], itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
  340 , weight(2.5)|difficulty(0)|spd_rtng(100) | weapon_length(210)|swing_damage(16 , pierce) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["lance_itami","Itami_Lance", [("lance_itami",0)], itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
  340 , weight(2.5)|difficulty(0)|spd_rtng(100) | weapon_length(210)|swing_damage(16 , pierce) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["lance_bashide","Bashide_Lance", [("lance_bashide",0)], itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
  340 , weight(2.5)|difficulty(0)|spd_rtng(100) | weapon_length(210)|swing_damage(16 , pierce) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["lance_renegade","Renegade_Lance", [("lance_renegade",0)], itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
  340 , weight(2.5)|difficulty(0)|spd_rtng(100) | weapon_length(210)|swing_damage(16 , pierce) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["lance_throd","Throd_Lance", [("lance_throd",0)], itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
  340 , weight(2.5)|difficulty(0)|spd_rtng(100) | weapon_length(210)|swing_damage(16 , pierce) | thrust_damage(35 ,  pierce),imodbits_polearm ],

["lunge_mine","Lunge_Mine",[("lunge_mine",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_wooden_attack|itp_penalty_with_shield|itp_merchandise,itcf_thrust_polearm|itcf_carry_sword_back,
  5040,weight(4)|spd_rtng(110)|weapon_length(200)|thrust_damage(15,blunt),imodbits_none, [ranged_weapon_triggers,
    (ti_on_weapon_attack , [
    
      (store_trigger_param_1,":agent"),
      (call_script,"script_create_explosion", pos1,":agent","itm_lunge_mine", 1000, 150, 250, 0),
    ]),]],


#axes
["battleaxe1","Pollaxe", [("battleaxe1",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  650 , weight(2.0)|difficulty(0)|spd_rtng(75) | weapon_length(75)|swing_damage(38 , cut) | thrust_damage(40 ,  pierce),imodbits_sword_high ],
["battleaxe2","Pollaxe", [("battleaxe2",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  650 , weight(2.0)|difficulty(0)|spd_rtng(85) | weapon_length(65)|swing_damage(38 , cut) | thrust_damage(40 ,  pierce),imodbits_sword_high ],
["axe1", "Axe", [("axe1",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
  250 , weight(1.65)|difficulty(9)|spd_rtng(75) | weapon_length(80)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
["axe2", "Axe", [("axe2",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
  250 , weight(1.65)|difficulty(9)|spd_rtng(75) | weapon_length(80)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],

["warhammer","Warhammer", [("warhammer",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
  930 , weight(2.0)|difficulty(0)|spd_rtng(75) | weapon_length(60)|swing_damage(41 , blunt) | thrust_damage(40 ,  pierce),imodbits_sword_high ], 

#polearms
["farmers_scythe","Farmer's Scythe", [("scythe",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry|itp_merchandise, itc_staff|itcf_carry_spear,
  100 , weight(4.5)|difficulty(0)|spd_rtng(78) | weapon_length(110)|swing_damage(22,cut),imodbits_polearm ],
["reaper_scythe","Reaper's Scythe", [("scythe",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry|itp_unique, itc_staff|itcf_carry_spear,
  10000 , weight(8.5)|difficulty(20)|spd_rtng(115) | weapon_length(110)|swing_damage(48,cut),imodbits_polearm ],

["pitch_fork_1","Pitch_Fork",[("pitchfork_1",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_merchandise,itc_spear|itcf_carry_axe_back,
  25,weight(3)|spd_rtng(85)|weapon_length(137)|thrust_damage(25,pierce),imodbits_mace],
["pitch_fork_2","Pitch_Fork",[("pitchfork_2",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_merchandise,itc_spear|itcf_carry_axe_back,
  25,weight(3)|spd_rtng(85)|weapon_length(137)|thrust_damage(25,pierce),imodbits_mace],

["pike1", "Pike", [("pike1",0),("pike1",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary|itp_offset_lance|itp_no_blur|itp_is_pike|itp_extra_penetration|itp_cant_use_on_horseback, itc_spear|itcf_carry_spear,
  280 , weight(12)|difficulty(0)|spd_rtng(68) | weapon_length(420)|swing_damage(24 ,  blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["pike2", "Pike", [("pike2",0),("pike2",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary|itp_offset_lance|itp_no_blur|itp_is_pike|itp_extra_penetration|itp_cant_use_on_horseback, itc_spear|itcf_carry_spear,
  350 , weight(12)|difficulty(0)|spd_rtng(70) | weapon_length(420)|swing_damage(25 ,  blunt) | thrust_damage(33 ,  pierce),imodbits_polearm ],

#giant
["giant_wooden_club","Giant_Wooden_Club", [("giant_wooden_club",0)], itp_type_two_handed_wpn|itp_primary, itc_morningstar|itcf_carry_sword_left_hip, 
  1200,weight(16.0)|difficulty(18)|spd_rtng(77)|weapon_length(125)|swing_damage(31,blunt),imodbits_mace],
["giant_hammer","Giant_Hammer", [("giant_hammer",0)], itp_type_two_handed_wpn|itp_primary, itc_morningstar|itcf_carry_sword_left_hip, 
  2000,weight(13.0)|difficulty(20)|spd_rtng(80)|weapon_length(125)|swing_damage(42,blunt),imodbits_mace],
["giant_mace","Giant_Mace", [("giant_mace",0)], itp_type_two_handed_wpn|itp_primary, itc_morningstar|itcf_carry_sword_left_hip, 
  1800,weight(10.0)|difficulty(18)|spd_rtng(85)|weapon_length(125)|swing_damage(35,blunt),imodbits_mace],
["giant_spiked_mace","Giant_Spiked_Mace", [("giant_mace_b",0)], itp_type_two_handed_wpn|itp_primary, itc_morningstar|itcf_carry_sword_left_hip, 
  1950,weight(11.0)|difficulty(19)|spd_rtng(85)|weapon_length(135)|swing_damage(30,pierce),imodbits_mace],

#cannibal
["cannibal_axe", "Primitive_Axe", [("cannibal_axe",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry|itp_merchandise, itc_scimitar|itcf_carry_axe_left_hip,
  70,weight(5.5)|spd_rtng(72)|weapon_length(58)|swing_damage(21,cut)|thrust_damage(0,pierce),imodbits_sword],
["cannibal_hatchet", "Primitive_Hatchet", [("cannibal_hatchet",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry|itp_merchandise, itc_scimitar|itcf_carry_axe_left_hip,
  50,weight(3.5)|spd_rtng(60)|weapon_length(43)|swing_damage(17,cut)|thrust_damage(0,pierce),imodbits_sword],
["cannibal_knife","Primitive_Knife",[("cannibal_knife",0)],itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_merchandise,itc_dagger,
  8,weight(1.5)|spd_rtng(100)|weapon_length(22)|swing_damage(10,cut)|thrust_damage(15,pierce),imodbits_sword],
["cannibal_spear","Primitive_Spear",[("cannibal_spear",0)],itp_type_two_handed_wpn|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_merchandise,itc_spear|itcf_carry_axe_back,
  30,weight(4.5)|spd_rtng(82)|weapon_length(132)|thrust_damage(22,pierce),imodbits_mace],
["butcher","Butcher",[("butcher",0),("butcher_scab",ixmesh_carry)],itp_type_two_handed_wpn|itp_merchandise|itp_primary,itc_morningstar|itcf_carry_sword_back,
  2000,weight(9.5)|difficulty(14)|spd_rtng(94)|weapon_length(93)|swing_damage(64,cut),imodbits_polearm],
["mackie_billhook","Billhook",[("mackie_billhook",0)],itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry,itc_cleaver,
  100,weight(0.5)|difficulty(0)|spd_rtng(200)|weapon_length(42)|swing_damage(30,cut),imodbits_sword],
["meatsplitter_1","Meat_Splitter",[("mackie_beefsplitter01",0)],itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry,itc_morningstar,
  1500,weight(0.5)|difficulty(0)|spd_rtng(87)|weapon_length(80)|swing_damage(55,cut),imodbits_polearm],
["meatsplitter_2","Meat_Splitter",[("mackie_beefsplitter02",0)],itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry,itc_morningstar,
  1600,weight(0.5)|difficulty(0)|spd_rtng(85)|weapon_length(83)|swing_damage(50,cut),imodbits_polearm],

################
###	old_broom marks the end of melee items, add new ones before this, not after - krag

["old_broom","Broom",[("old_broom",0)],itp_type_two_handed_wpn|itp_wooden_attack|itp_wooden_parry|itp_two_handed|itp_primary,itcf_carry_axe_back|itc_nodachi,
  70,weight(1.5)|spd_rtng(80)|weapon_length(144)|swing_damage(10,blunt),imodbits_none,[],[]],

###	old_broom marks the end of melee items, add new ones before this, not after - krag

##************************************************************************************************
## SHIELDS
##************************************************************************************************
["wooden_shield","Plank_Shield",[("wood_shield",0)],itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry,itcf_carry_board_shield,
100,weight(3.5)|hit_points(80)|body_armor(4)|spd_rtng(89)|shield_width(43)|shield_height(100),imodbits_shield],

["wooden_shield_2","Plank_Shield",[("plank_shield",0)],itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry,itcf_carry_board_shield,
100,weight(3.5)|hit_points(80)|body_armor(4)|spd_rtng(89)|shield_width(43)|shield_height(100),imodbits_shield],

["wood_shield","Wood_Round_Shield",[("spak_shield_wood2",0)],itp_type_shield|itp_wooden_parry,itcf_carry_round_shield,
200,weight(3.5)|hit_points(100)|body_armor(8)|spd_rtng(89)|shield_width(50),imodbits_shield],

["round_shield_leather","Round_Leather_Shield",[("wild_shield",0)],itp_type_shield|itp_wooden_parry,itcf_carry_round_shield,
300,weight(3.5)|hit_points(120)|body_armor(12)|spd_rtng(87)|shield_width(50),imodbits_shield],

["round_shield_flesh","Flesh_Shield",[("flesh_shield_a",0)],itp_type_shield|itp_wooden_parry,itcf_carry_round_shield,
300,weight(3.5)|hit_points(120)|body_armor(12)|spd_rtng(87)|shield_width(50),imodbits_shield],

["round_shield","Heavy_Round_Shield",[("wildling_shield",0)],itp_type_shield,itcf_carry_round_shield,
375,weight(4)|hit_points(150)|body_armor(15)|spd_rtng(84)|shield_width(50),imodbits_shield],

["riot_shield","Riot_Shield",[("riot_shield",0)],itp_type_shield|itp_cant_use_on_horseback,itcf_carry_board_shield,
200,weight(4)|hit_points(260)|body_armor(8)|spd_rtng(85)|shield_width(43)|shield_height(100),imodbits_shield],

["bal_shield_1","Trench_Shield",[("trench_tower_shield",0)],itp_type_shield|itp_cant_use_on_horseback,itcf_carry_board_shield,
350,weight(5)|hit_points(550)|body_armor(14)|spd_rtng(78)|shield_width(43)|shield_height(100),imodbits_shield],
["bal_shield_2","Trench_Shield",[("trench_tower_shield_2",0)],itp_type_shield|itp_cant_use_on_horseback,itcf_carry_board_shield,
350,weight(5)|hit_points(550)|body_armor(14)|spd_rtng(78)|shield_width(43)|shield_height(100),imodbits_shield],
["bal_shield_3","Trench_Shield",[("trench_tower_shield_3",0)],itp_type_shield|itp_cant_use_on_horseback,itcf_carry_board_shield,
350,weight(5)|hit_points(550)|body_armor(14)|spd_rtng(78)|shield_width(43)|shield_height(100),imodbits_shield],

["tc_shield_1","Pavise_Shield",[("wooden_pavise",0)],itp_type_shield|itp_cant_use_on_horseback,itcf_carry_board_shield,
150,weight(4.5)|hit_points(430)|body_armor(10)|spd_rtng(81)|shield_width(43)|shield_height(100),imodbits_shield],
["tc_shield_2","Shield",[("tc_shield_2",0)],itp_type_shield|itp_cant_use_on_horseback,itcf_carry_board_shield,
150,weight(4.5)|hit_points(430)|body_armor(10)|spd_rtng(81)|shield_width(43)|shield_height(100),imodbits_shield],
["tc_shield_5","Shield",[("tc_shield_5",0)],itp_type_shield|itp_cant_use_on_horseback,itcf_carry_board_shield,
150,weight(4.5)|hit_points(430)|body_armor(10)|spd_rtng(81)|shield_width(43)|shield_height(100),imodbits_shield],

################
##Barbed Wire###
################
##Entenaii Empire
##Entenaii Dominion
##Kingdom of Galvae
["galvae_shield_1", "Galvae_Sciath", [("cantabro_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  610 , weight(4.5)|hit_points(410)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(5),imodbits_shield],
["galvae_shield_2", "Galvae_Sciath", [("cantabro_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  588 , weight(4.5)|hit_points(420)|body_armor(10)|spd_rtng(54)|shield_width(70)|difficulty(5),imodbits_shield],
["galvae_shield_3", "Galvae_Sciath", [("cantabro_shield_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  604 , weight(5)|hit_points(415)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(5),imodbits_shield],
["galvae_shield_4", "Galvae_Sciath", [("cantabro_shield_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  590 , weight(4.5)|hit_points(408)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(5),imodbits_shield],
["galvae_shield_5", "Galvae_Sciath", [("cantabro_shield_5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  595 , weight(4.5)|hit_points(411)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(5),imodbits_shield],
["galvae_shield_6", "Galvae_Sciath", [("cantabro_shield_6",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  601 , weight(4.0)|hit_points(404)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(5),imodbits_shield],
["galvae_shield_7", "Galvae_Sciath", [("cantabro_shield_7",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  600 , weight(4.5)|hit_points(400)|body_armor(10)|spd_rtng(56)|shield_width(70)|difficulty(5),imodbits_shield],
["galvae_shield_8", "Galvae_Sciath", [("cantabro_shield_8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  618 , weight(4.5)|hit_points(410)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(5),imodbits_shield],
["galvae_shield_9", "Galvae_Sciath", [("cantabro_shield_9",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  602 , weight(4.5)|hit_points(412)|body_armor(10)|spd_rtng(55)|shield_width(70)|difficulty(5),imodbits_shield],
["galvae_shield_10", "Galvae_Lort_Sciath", [("cantabro_shield_10",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  1000 , weight(4.5)|hit_points(650)|body_armor(15)|spd_rtng(65)|shield_width(70)|difficulty(8),imodbits_shield],
##Molvat-Berchav Union
##Vitzland Territories
##Trezzo Republic
##Renegades
["rectangular_shield_1", "Rectangular Shield", [("vae_escudo_picto",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,[],],
["rectangular_shield_2", "Rectangular Shield", [("vae_escudo_picto2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,[],],
["rectangular_shield_3", "Rectangular Shield", [("vae_escudo_picto3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,[],],
["rectangular_shield_4", "Rectangular Shield", [("vae_escudo_picto4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,[],],
["rectangular_shield_5", "Rectangular Shield", [("vae_escudo_picto5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,[],],
["rectangular_shield_6", "Rectangular Shield", [("vae_escudo_picto6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,[],],
["rectangular_shield_7", "Rectangular Shield", [("vae_escudo_picto7",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,[],],
["rectangular_shield_8", "Rectangular Shield", [("vae_escudo_picto8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,[],],
["rectangular_shield_9", "Rectangular Shield", [("vae_escudo_picto9",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,[],],
["rectangular_shield_10", "Rectangular Shield", [("vae_escudo_picto10",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(60)|difficulty(1),imodbits_shield,[],],
##Throd
["throd_shield", "Throd_Shield", [("throd_shield",0)], itp_type_shield, itcf_carry_round_shield,  1000 , weight(6.5)|hit_points(950)|body_armor(22)|spd_rtng(55)|shield_width(70)|difficulty(8),imodbits_shield],
##Other
["blackgod_knight_shield", "Night_Raider_Shield", [("blackgod_knight_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  380 , weight(3)|hit_points(290)|body_armor(9)|spd_rtng(60)|shield_width(36)|shield_height(70)|difficulty(1),imodbits_shield,[],],

#
#
["testshield","Shield",[("testshield",0)],itp_type_shield|itp_cant_use_on_horseback,itcf_carry_board_shield,
750,weight(5.5)|hit_points(550)|body_armor(15)|spd_rtng(75)|shield_width(43)|shield_height(100),imodbits_shield],

##************************************************************************************************
## SPECIAL
##************************************************************************************************
# companions
["dog_companion_horse","Dog", [("doberman",0)],		itp_type_horse|itp_disable_agent_sounds, 0, 10,hit_points(350)|horse_speed(30)|horse_maneuver(90)|horse_scale(55), 0],
["dog_bite","Bite", [("dummy_mesh",0)], itp_type_polearm|itp_primary|itp_can_knock_down|itp_no_pick_up_from_ground,
itc_greatlance|itcf_carry_axe_left_hip, 1, weight(1)|spd_rtng(95)|weapon_length(65)|thrust_damage(25, pierce),0],
["bot_companion_horse","Bot", [("lilbot",0)],		itp_type_horse|itp_disable_agent_sounds, 0, 10,hit_points(350)|horse_speed(20)|horse_maneuver(50)|horse_scale(75), 0],

# walkers
["animal_cow","Cow", [("animal_cow",0)], itp_unique|itp_type_animal|itp_disable_agent_sounds, 0,
# ["animal_cow","Cow", [("animal_cow",0),("animal_cow2",imodbit_cracked),("animal_cow3",imodbit_rusty)], itp_unique|itp_type_animal|itp_disable_agent_sounds, 0,
0,hit_points(100)|body_armor(0)|horse_speed(5)|horse_maneuver(40)|horse_charge(35)|horse_scale(123),imodbits_horse_basic],
["animal_old_horse","Pack Horse", [("animal_old_horse_a",0)], itp_unique|itp_type_animal, 0,
0,hit_points(100)|body_armor(5)|horse_speed(30)|horse_maneuver(40)|horse_charge(5)|horse_scale(100),imodbits_horse_basic],
["animal_doberman","Doberman", [("doberman",0)], itp_unique|itp_type_animal|itp_disable_agent_sounds, 0,
0,hit_points(100)|body_armor(0)|horse_speed(20)|horse_maneuver(30)|horse_charge(5)|horse_scale(50),imodbits_horse_basic],
["animal_dog","Dog", [("dog_2",0)], itp_unique|itp_type_animal|itp_disable_agent_sounds, 0,
0,hit_points(100)|body_armor(0)|horse_speed(20)|horse_maneuver(30)|horse_charge(5)|horse_scale(50),imodbits_horse_basic],
["lilbot","lilbot", [("lilbot",0)], itp_type_animal|itp_disable_agent_sounds|itp_unique, 0,
0, abundance(0)|hit_points(180)|body_armor(2)|difficulty(11)|horse_speed(5)|horse_maneuver(42)|horse_charge(1)|horse_scale(100), imodbits_none ],
["lilbot_2","lilbot", [("lilbot_2",0)], itp_type_animal|itp_disable_agent_sounds|itp_unique, 0,
0, abundance(0)|hit_points(180)|body_armor(2)|difficulty(11)|horse_speed(5)|horse_maneuver(42)|horse_charge(1)|horse_scale(100), imodbits_none ],

#animals
["mutant_spider_big","Spider", [("spider",0)], itp_unique|itp_type_horse|itp_disable_agent_sounds, 0,
0,hit_points(1800)|body_armor(25)|difficulty(10)|horse_speed(10)|horse_scale(100)|horse_maneuver(75)|horse_charge(30),imodbits_horse_basic],
["mutant_spider","Spider", [("spider",0)], itp_unique|itp_type_horse|itp_disable_agent_sounds, 0,
0,hit_points(500)|body_armor(15)|difficulty(10)|horse_speed(15)|horse_scale(75)|horse_maneuver(75)|horse_charge(20),imodbits_horse_basic],
# ["mutant_spider_small","Spider", [("spider",0)], itp_unique|itp_type_horse|itp_disable_agent_sounds, 0,
# 0,hit_points(250)|body_armor(5)|difficulty(10)|horse_speed(35)|horse_scale(25)|horse_maneuver(75)|horse_charge(10),imodbits_horse_basic],
["spider_attack","spider_attack", [("dummy_mesh",0)], itp_unique|itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_slasher,
0,weight(1)|spd_rtng(65)|weapon_length(50)|swing_damage(30, blunt)|thrust_damage(60, pierce),imodbits_none,[
    (ti_on_weapon_attack, [
      (store_trigger_param_1,":agent"),
      (agent_play_sound,":agent","snd_spider_attack"),
    ]),]],

["infected_doberman","Infected Doberman", [("dobermanb",0)], itp_unique|itp_type_horse|itp_disable_agent_sounds, 0,
0,hit_points(100)|body_armor(0)|difficulty(10)|horse_speed(20)|horse_maneuver(50)|horse_charge(35)|horse_scale(50),imodbits_horse_basic],
["infected_doberman_2","Infected Doberman", [("dobermanc",0)], itp_unique|itp_type_horse|itp_disable_agent_sounds, 0,
0,hit_points(100)|body_armor(0)|difficulty(10)|horse_speed(20)|horse_maneuver(50)|horse_charge(35)|horse_scale(50),imodbits_horse_basic],
["infected_dog","Infected Dog", [("dog_2b",0)], itp_unique|itp_type_horse|itp_disable_agent_sounds, 0,
0,hit_points(100)|body_armor(0)|difficulty(10)|horse_speed(20)|horse_maneuver(50)|horse_charge(35)|horse_scale(50),imodbits_horse_basic],
["infected_dog_2","Infected Dog", [("dog_2c",0)], itp_unique|itp_type_horse|itp_disable_agent_sounds, 0,
0,hit_points(100)|body_armor(0)|difficulty(10)|horse_speed(20)|horse_maneuver(50)|horse_charge(35)|horse_scale(50),imodbits_horse_basic],
["rabid_doberman","Rabid Doberman", [("doberman",0)], itp_unique|itp_type_horse|itp_disable_agent_sounds, 0,
0,hit_points(100)|body_armor(0)|difficulty(10)|horse_speed(20)|horse_maneuver(50)|horse_charge(35)|horse_scale(50),imodbits_horse_basic],
["rabid_dog","Rabid Dog", [("dog_2",0)], itp_unique|itp_type_horse|itp_disable_agent_sounds, 0,
0,hit_points(100)|body_armor(0)|difficulty(10)|horse_speed(20)|horse_maneuver(50)|horse_charge(35)|horse_scale(50),imodbits_horse_basic],

#infected
# ["infected_1","Infected", [("zm_classic_01", 0)], itp_type_head_armor|itp_covers_head|itp_civilian|itp_unique|itp_attach_armature, 0,
# 0, weight(1)|head_armor(20), imodbits_none, []],
["infected_2","Infected", [("Zhead1", 0)], itp_type_head_armor|itp_covers_head|itp_civilian|itp_unique, 0,
0, weight(1)|head_armor(20), imodbits_none, []],
["infected_3","Infected", [("Zhead2", 0)], itp_type_head_armor|itp_covers_head|itp_civilian|itp_unique, 0,
0, weight(1)|head_armor(20), imodbits_none, []],
["infected_4","Infected", [("Zhead3", 0)], itp_type_head_armor|itp_covers_head|itp_civilian|itp_unique, 0,
0, weight(1)|head_armor(20), imodbits_none, []],
["infected_5","Infected", [("Zhead4", 0)], itp_type_head_armor|itp_covers_head|itp_civilian|itp_unique, 0,
0, weight(1)|head_armor(20), imodbits_none, []],
["infected_6","Infected", [("Zhead5", 0)], itp_type_head_armor|itp_covers_head|itp_civilian|itp_unique, 0,
0, weight(1)|head_armor(20), imodbits_none, []],
["infected_7","Infected", [("Zhead6", 0)], itp_type_head_armor|itp_covers_head|itp_civilian|itp_unique, 0,
0, weight(1)|head_armor(20), imodbits_none, []],
["infected_9","Infected", [("Zhead7", 0)], itp_type_head_armor|itp_covers_head|itp_civilian|itp_unique, 0,
0, weight(1)|head_armor(20), imodbits_none, []],

#brute
["brute_body1b","Brute_Body", [("brute_body1b", 0)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_civilian, 0,
0, weight(1)|head_armor(20)|body_armor(25)|leg_armor(20), imodbits_armor, []],
["brute_attack","brute_attack", [("dummy_mesh",0)], itp_unique|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield, itc_slasher,
0 , weight(1)|spd_rtng(65) | weapon_length(20)|swing_damage(60, blunt) | thrust_damage(50, blunt),imodbits_none ],

#zombie
["undead_1","Undead", [("undead_1", 0)], itp_type_body_armor|itp_covers_legs|itp_covers_head|itp_doesnt_cover_hair|itp_civilian|itp_unique, 0,
0, weight(1)|head_armor(20)|body_armor(25)|leg_armor(20), imodbits_armor, []],
["undead_2","Undead", [("undead_2", 0)], itp_type_body_armor|itp_covers_legs|itp_covers_head|itp_doesnt_cover_hair|itp_civilian|itp_unique, 0,
0, weight(1)|head_armor(20)|body_armor(25)|leg_armor(20), imodbits_armor, []],

["infected_attack","infected_attack", [("dummy_mesh", 0)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_no_pick_up_from_ground, itcf_carry_sword_left_hip|itc_slasher,
0, weight(1)|spd_rtng(50)|weapon_length(25)|thrust_damage(30, pierce)|swing_damage(20, cut), imodbits_sword, [
    (ti_on_weapon_attack, [
      (store_trigger_param_1,":agent"),
      (agent_set_animation,":agent","anim_release_thrust_zombie"),
    ]),]],

#ghoul
["ghoul_body","Ghoul_Body", [("ghoul_adjusted", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian|itp_unique, 0,
0, weight(1)|head_armor(10)|body_armor(8)|leg_armor(5), imodbits_armor, []],
["ghoul_body_2","Ghoul_Body", [("ghoul_zombie_2", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian|itp_unique, 0,
0, weight(1)|head_armor(10)|body_armor(13)|leg_armor(10), imodbits_armor, []],
["ghoul_body_3","Ghoul_Body", [("ghoul_zombie_aggressive", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian|itp_unique, 0,
0, weight(1)|head_armor(10)|body_armor(18)|leg_armor(15), imodbits_armor, []],
["ghoul_body_4","Ghoul_Body", [("ghoul_zombie_2_aggressive", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian|itp_unique, 0,
0, weight(1)|head_armor(10)|body_armor(18)|leg_armor(15), imodbits_armor, []],

["ghoul_1","Ghoul_Scavenger", [("ghoul_1", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian|itp_unique, 0,
0, weight(20)|head_armor(50)|body_armor(60)|leg_armor(40), imodbits_armor, []],

#beastling
["beastling_1","Feral Beastling", [("beastling_1_body", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique, 0,
0, weight(1)|head_armor(10)|body_armor(13)|leg_armor(10), imodbits_armor, []],

#cannibal
["cannibal_body","Cannibal", [("cannibal_body", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique, 0,
  0, weight(1)|head_armor(10)|body_armor(10)|leg_armor(10), imodbits_armor, []],
["cannibal_head","Cannibal_Head", [("dummy_mesh", 0)], itp_type_head_armor|itp_covers_head|itp_civilian|itp_unique, 0,
  0, weight(1)|head_armor(20), imodbits_none, 
  [(ti_on_init_item,[
    (str_store_string, s1,"@cannibal_head_1"),
    (str_store_string, s2,"@bloody_bandages"),
    (cur_item_add_mesh, s1),
    (cur_item_add_mesh, s2),]),]],

#cursed
["cursed_one","Cursed_One", [("heavy_armor_for_cursed_one", 0)], itp_type_body_armor|itp_covers_legs|itp_civilian|itp_unique, 0,
  0, weight(1)|head_armor(10)|body_armor(70)|leg_armor(50), imodbits_armor, []],
  
["cursed_one_head","Cursed_One_Head", [("cursed_one_head", 0)], itp_type_head_armor|itp_covers_head|itp_attach_armature|itp_civilian|itp_unique, 0,
  0, weight(1)|head_armor(40), imodbits_none, 
  [(ti_on_init_item,[(set_position_delta,0,10,0),(particle_system_add_new,"psys_torch_fire_black"),(particle_system_add_new,"psys_torch_smoke"),(set_current_color,0,0,0),])]],

#spitter
["spitter_body","Spitter_Body", [("real_spitter_body", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian|itp_unique, 0,
0, weight(1)|head_armor(20)|body_armor(25)|leg_armor(20), imodbits_armor, []],
["infected_spit","Infected_Spit", [("infected_spit_projectile", 0)], itp_type_thrown|itp_primary|itp_no_pick_up_from_ground|itp_unique, itcf_throw_stone,
# ["infected_spit","Infected_Spit", [("dummy_mesh", 0)], itp_type_musket|itp_primary|itp_no_pick_up_from_ground|itp_ignore_gravity|itp_ignore_friction|itp_unique, itcf_throw_stone,
0, weight(1)|accuracy(50)|spd_rtng(50)|shoot_speed(20)|max_ammo(50)|thrust_damage(20, blunt), imodbits_none, []],
["infected_ammo","Cartridges", [("dummy_mesh", 0),("infected_spit_projectile", ixmesh_flying_ammo)], itp_type_bullets|itp_no_pick_up_from_ground|itp_unique, 0,
# ["infected_ammo","Cartridges", [("dummy_mesh", 0),("infected_spit_projectile", ixmesh_flying_ammo)], itp_type_bullets|itp_no_pick_up_from_ground|itp_ignore_gravity|itp_ignore_friction|itp_unique, 0,
0, weight(1)|weapon_length(3)|max_ammo(50)|thrust_damage(1, blunt), imodbits_missile, []],

# #birkin
# ["birkin","birkin", [("birkin", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_unique, 0,
# 0, weight(1)|head_armor(20)|body_armor(25)|leg_armor(20), imodbits_armor, []],

#acid
["acid_mutant_1","Acid Mutant", [("acid_mutant_1", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_covers_head|itp_unique, 0,
0, weight(1)|head_armor(20)|body_armor(25)|leg_armor(20), imodbits_armor, []],

# #synth
# ["synth_mutant_1","Synth Mutant", [("synth_mutant_1", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_covers_head|itp_unique, 0,
# 0, weight(1)|head_armor(20)|body_armor(25)|leg_armor(20), imodbits_armor, []],

#nark
["nark_mutant_1","Nark Mutant", [("nark_mutant_1", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_covers_head|itp_unique, 0,
0, weight(1)|head_armor(20)|body_armor(25)|leg_armor(20), imodbits_armor, []],

#tick
["mutant_tick","Tick Mutant", [("mutant_tick", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_covers_head|itp_unique, 0,
0, weight(1)|head_armor(20)|body_armor(25)|leg_armor(20), imodbits_armor, []],

#tank
["mutant_tank","Mutant", [("mutant_tank", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_covers_head|itp_unique, 0,
0, weight(1)|head_armor(20)|body_armor(25)|leg_armor(20), imodbits_armor, []],

#tank
["mutant_wolfclaw","Wolfclaw", [("mutant_wolfclaw", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_covers_head|itp_unique, 0,
0, weight(1)|head_armor(20)|body_armor(25)|leg_armor(20), imodbits_none, []],
["mutant_wolfclaw_2","Wolfclaw", [("mutant_wolfclaw_2", 0)], itp_type_body_armor|itp_covers_legs|itp_doesnt_cover_hair|itp_covers_head|itp_unique, 0,
0, weight(1)|head_armor(30)|body_armor(35)|leg_armor(30), imodbits_none, []],

#rancor
["rancor_body_a","Rancor Body", [("swy_rancor",0)], itp_unique|itp_type_body_armor |itp_covers_head|itp_covers_legs |itp_civilian  ,0,
0 , weight(1)|head_armor(20)|body_armor(25)|leg_armor(20) ,imodbits_none ],
["rancor_body_c","Rancor Body", [("swy_rancor_mutant",0)], itp_unique|itp_type_body_armor |itp_covers_head|itp_covers_legs |itp_civilian  ,0,
0 , weight(1)|head_armor(20)|body_armor(25)|leg_armor(20) ,imodbits_none ],
["rancor_attack","rancor_attack", [("dummy_mesh",0)], itp_unique|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_no_parry, itc_slasher,
0 , weight(1)|spd_rtng(85) | weapon_length(25)|swing_damage(60, cut) | thrust_damage(45, pierce),imodbits_none ],

#special
["psycho_1","Psycho", [("psycho_1", 0)], itp_type_body_armor|itp_unique|itp_covers_head|itp_covers_legs|itp_civilian, 0,
0, weight(1)|head_armor(80)|body_armor(80)|leg_armor(80), imodbits_none, []],

#special items out of range
["guitar","Guitar",[("guitar",0),("guitar_carry", ixmesh_carry)],	itp_type_foot_armor|itp_attach_armature,0,0,weight(1)|body_armor(20),0],
["syringe_glove","Syringe", [("old_syringe_glove_R",0)], itp_type_hand_armor|itp_force_attach_right_hand|itp_force_show_left_hand|itp_force_show_right_hand, 0,
50, weight(0.1)|body_armor(2),0],

#dummy vehicles
["car","Automobile", [("dummy_mesh", 0),("dummy_mesh", ixmesh_inventory)], itp_type_horse|itp_disable_agent_sounds, 0,
0, weight(0)|body_armor(10)|difficulty(1)|hit_points(200)|horse_maneuver(25)|horse_speed(40)|weapon_length(85)|horse_charge(50), imodbits_horse_basic, []],
# ["heli","chopper", [("charger_plate_1", 0),("dummy_mesh", ixmesh_inventory)], itp_type_horse|itp_disable_agent_sounds, 0,
["heli","Aeromobile", [("dummy_mesh", 0),("zeppelin", ixmesh_inventory)], itp_type_horse|itp_disable_agent_sounds, 0,
0, weight(0)|body_armor(945)|difficulty(10)|hit_points(9500)|horse_scale(300)|horse_maneuver(45)|horse_speed(60)|weapon_length(0)|horse_charge(0), imodbits_horse_basic, []],	#make unhittable as added collision to shoot - krag
# 134, weight(0)|body_armor(14)|difficulty(1)|hit_points(100)|horse_maneuver(15)|horse_speed(40)|weapon_length(140)|horse_charge(9), imodbits_horse_basic, []],
["bus","Automobile_Big", [("dummy_mesh", 0),("dummy_mesh", ixmesh_inventory)], itp_type_horse|itp_disable_agent_sounds, 0,
0, weight(0)|body_armor(30)|difficulty(1)|hit_points(500)|horse_maneuver(25)|horse_speed(20)|weapon_length(100)|horse_charge(9), imodbits_horse_basic, []],

#dummy equipment
# ["shotgun_auto","shotgun_auto", [("dummy_mesh", 0)], itp_type_musket|itp_two_handed|itp_primary, itcf_shoot_musket|itcf_reload_musket,
# 0, weight(1)|accuracy(50)|spd_rtng(50)|shoot_speed(130)|max_ammo(1)|thrust_damage(75, pierce), imodbits_none, [], []],
# ["shotgun_missile","shotgun_missile", [("dummy_mesh", 0),("buckshot_missile", ixmesh_flying_ammo)], itp_type_bullets|itp_can_penetrate_shield|itp_default_ammo, 0,
# 0,weight(1)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(50),imodbits_missile, [bullet_impact]],
["invisi_gun","invisi_gun", [("dummy_mesh", 0)], itp_type_pistol|itp_primary|itp_two_handed, itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_revolver_right,
0, weight(1.5)|accuracy(65)|spd_rtng(60)|shoot_speed(160)|max_ammo(15)|thrust_damage(30, pierce), imodbits_none, []],
["invisi_attack","invisi_attack", [("dummy_mesh", 0)], itp_type_one_handed_wpn|itp_unique|itp_primary|itp_no_pick_up_from_ground, itc_slasher,
0, weight(1)|spd_rtng(50)|weapon_length(30)|swing_damage(10, cut), imodbits_sword, []],

["invisi_gloves","invisi_gloves", [("dummy_mesh", 0)], itp_type_hand_armor|itp_unique, 0,
0, weight(0), imodbits_none, []],
["invisi_head","invisi_head", [("dummy_mesh", 0)], itp_type_head_armor|itp_unique|itp_covers_head, 0,
0, weight(0), imodbits_none, []],
["invisi_body","invisi_body", [("dummy_mesh", 0)], itp_type_body_armor|itp_unique|itp_covers_legs|itp_doesnt_cover_hair|itp_civilian, 0,
0, weight(0), imodbits_none, []],
["invisi_boots","invisi_boots", [("dummy_mesh", 0)], itp_type_foot_armor|itp_attach_armature|itp_unique|itp_civilian, 0,
0, weight(0), imodbits_none, []],

["tank_sword","tank_sword", [("dummy_mesh",0)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
0 , weight(1.5)|spd_rtng(89) | weapon_length(89)|swing_damage(54 , cut) | thrust_damage(44 ,  pierce),imodbits_none ],

#mechs
["mech_walker_1_body","Tyrant-class Walker Mk1 Body", [("mech_walker_1",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian|itp_covers_head,0,
  100000, weight(100)|abundance(0)|head_armor(75)|body_armor(75)|leg_armor(75) ,imodbits_none ],
["mech_walker_2_body","Tyrant-class Walker Mk2 Body", [("mech_walker_2",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian|itp_covers_head,0,
 500000, weight(150)|abundance(0)|head_armor(100)|body_armor(100)|leg_armor(100) ,imodbits_none ],
["mech_walker_3_body","Tyrant-class Walker Mk3 Body", [("mech_walker_3",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian|itp_covers_head,0,
 500000, weight(150)|abundance(0)|head_armor(125)|body_armor(125)|leg_armor(125) ,imodbits_none ],
["mech_walker_4_body","Tyrant-class Walker Mk4 Body", [("mech_walker_4",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian|itp_covers_head,0,
 500000, weight(150)|abundance(0)|head_armor(150)|body_armor(150)|leg_armor(150) ,imodbits_none ],
["mech_walker_whiteling_body","Tyrant-class Walker Mk3-Whiteling Body", [("mech_whiteling",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian|itp_covers_head,0,
 500000, weight(150)|abundance(0)|head_armor(175)|body_armor(175)|leg_armor(175) ,imodbits_none ],

["mech_walker_imperial_body","Imperial_Escort_Walker_Body", [("mech_walker_imperial",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian|itp_covers_head,0,
 500000, weight(165)|head_armor(165)|body_armor(165)|leg_armor(165) ,imodbits_none ],

["b2series_attack","Tyrant-class Walker Attack", [("dummy_mesh",0)], itp_unique|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_crush_through|itp_unbalanced, itc_dagger,
  500, weight(1)|abundance(0)|spd_rtng(55) | weapon_length(280)|swing_damage(50, blunt) | thrust_damage(30, blunt),imodbits_none ],
["b2series_blaster","Blaster", [("dummy_mesh",0)], itp_unique|itp_type_pistol|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_revolver_right,
  500 , weight(2)|abundance(0)|spd_rtng(90) | shoot_speed(145) | thrust_damage(200,pierce)|max_ammo(24)|accuracy(88),imodbits_none,
  [(ti_on_weapon_attack, [(position_move_x, pos1,12),(position_move_y, pos1,15)])]],
  # [(ti_on_weapon_attack, [(play_sound,"snd_bigblaster19"),(position_move_x, pos1,12),(position_move_y, pos1,15)])]],

["mech_spider","Servo-spider", [("mech_spider",0)], itp_type_horse|itp_disable_agent_sounds, 0,
0,hit_points(1800)|body_armor(35)|difficulty(10)|horse_speed(5)|horse_scale(100)|horse_maneuver(50)|horse_charge(60),imodbits_horse_basic],

####################################################################################################################
["tankard","Tankard",[("dedal_kufelL",0)],	itp_type_hand_armor,0,0,weight(1),0],
["old_syringe","Syringe", [("old_syringe", 0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
100, weight(1)|spd_rtng(90)|weapon_length(10)|swing_damage(20, pierce), imodbits_none, ],
####################################################################################################################
##diplomacy begin
["dplmc_coat_of_plates_red_constable","Constable Coat of Plates", [("civil_duster_4",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
3828 , weight(25)|body_armor(52)|leg_armor(16) ,imodbits_armor, [], []],
##diplomacy end
####################################################################################################################
# ["pistol_fake","pistol_fake", [("dummy_mesh",0)], itp_type_pistol, 0, 250, 0, imodbits_gun, []],
# ["shotgun_fake","shotgun_fake", [("dummy_mesh",0)], itp_type_pistol, 0, 500, 0, imodbits_gun, []],
# ["rifle_fake","rifle_fake", [("dummy_mesh",0)], itp_type_pistol, 0, 500, 0, imodbits_gun, []],
# ["smg_fake","smg_fake", [("dummy_mesh",0)], itp_type_pistol, 0, 500, 0, imodbits_gun, []],
# ["a_rifle_fake","a_rifle_fake", [("dummy_mesh",0)], itp_type_pistol, 0, 1000, 0, imodbits_gun, []],
# ["sniper_fake","sniper_fake", [("dummy_mesh",0)], itp_type_pistol, 0, 1000, 0, imodbits_gun, []],
####################################################################################################################
# #]+[	#what's this for? doesn't appear to be needed now - krag
 ]#  < Needs to be always enabled  for the code to compile
##From NouH, adds the item's id as a local variable to the scope_add init_item triggers (can't be gained from paramaters for some reason)
def addScope():
    for item in items:
        if len(item) >= 9 and len(item[8]) > 0 and scope_add in item[8]: 
            itemId = "itm_" + item[0]
            for i, ti in enumerate(item[8]):
                if scope_add is ti:
                    tiBlock = list(scope_add[1])
                    tiBlock = [(assign, ":item", itemId)] + tiBlock
                    item[8][i] = (ti_on_init_item, tiBlock)
                    
addScope() 

##this version adds it to all init_item triggers, but probably takes slightly longer to compile
# def recursive_search(container, target):
    # for element in container:
        # if isinstance(element, (list, tuple)):
            # if recursive_search(element, target):
                # return True
        # elif element == target:
            # return True
    # return False

# def add_id_to_init_item():
    # for item in items:
        # if len(item) >= 9 and len(item[8]) > 0: 
            # itemId = "itm_" + item[0]
            # for i, ti in enumerate(item[8]):
                # if ti[0] == ti_on_init_item and recursive_search(ti[1], ":item"):
                    # item[8][i] = (ti_on_init_item, [(assign, ":item", itemId)] + ti[1])
                    
# add_id_to_init_item()
 
make_ai_firearms(items)
make_ai_firearms_2h(items)

##************************************************************************************************
## GUN ADDING GUIDE
##************************************************************************************************

# Warzone Acron automatically generates 2 additional versions of each gun for the ai to use. This is necessary for the toggling aim system the player uses. 
#(You can find it in process_items.py, but you shouldn't need to edit it)

# This means that adding new guns has additional steps to avoid item ID conflicts when compiling:

##	1. - Only add new guns between the existing "itm_pistol_1911" and "buffer_gun_1" items.  This is the section that gets duplicated for NPC versions.

##	2. - Only add 9 or less new guns at a time. Then compile twice. Then add the next set. Then compile twice, and so on.

#If you mess this up amd end up with messages about "itm_ai_gun_whatever" being missing you can maybe fix it by adding it manually to the bottom of your ID_items file, then compiling twice again.

#Additional:
#You should probably check the ranges set in module constants, such as rifle_begin rifle_end. Then place new guns within the appropriate section as some scripts will work differently for them.
#In module_warzone_scripts there is a script called "init_firearms" where you can set the gun's ammo type, animation, if it has a scope and son on. 
#You can also set the ironsight mesh here. Ironsight meshes are technically scene props you have to create. Look in module_scene_props for examples.# modmerger_start version=201 type=2
try:
    component_name = "items"
    var_set = { "items" : items }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
