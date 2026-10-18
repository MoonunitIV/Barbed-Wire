from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *

from module_constants import *

from compiler import *
####################################################################################################################
#  Each trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Delay interval: Time to wait before applying the consequences of the trigger
#    After its conditions have been evaluated as true.
# 3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
# 4) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#    Every time the trigger is checked, the conditions block will be executed.
#    If the conditions block returns true, the consequences block will be executed.
#    If the conditions block is empty, it is assumed that it always evaluates to true.
# 5) Consequences block (list). This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

# Some constants for use below
merchant_inventory_space = 30
num_merchandise_goods = 36



triggers = [
# Tutorial:
  (0.1, 0, ti_once, [
    (map_free,0)
    ], [
    # (set_global_cloud_amount, 0),
    # (set_global_haze_amount, 0),
    (dialog_box,"str_tutorial_map2")
    
    ]),
  
  (0.5, 0, ti_once, [(map_free,0)], [(dialog_box,"str_tutorial_map1")]),
  
  (1, 0, ti_once, [
  (map_free,0),
  (troop_get_slot, ":player_condition", "trp_player", slot_troop_condition),   
  (le,":player_condition",0),
  ], [(dialog_box,"str_tutorial_map3")]),




# Refresh Merchants
  (0.0, 0, 168.0, [],
  [
    (call_script, "script_refresh_center_inventories"),
                     ]),

# Refresh Armor sellers
  (0.0, 0, 168.0, [],
  [
    (call_script, "script_refresh_center_armories"),
                     ]),

# Refresh Weapon sellers
  (0.0, 0, 168.0, [],
  [
    (call_script, "script_refresh_center_weaponsmiths"),
                     ]),

# # Refresh Horse sellers
  # (0.0, 0, 168.0, [],
  # [
    # (call_script, "script_refresh_center_stables"),
                     # ]),


#############


  (5.7, 0, 0.0,
  [
    (store_num_parties_of_template, reg2, "pt_manhunters"),
    (lt, reg2, 4)
  ],
  [
    (set_spawn_radius, 1),
    # (store_add, ":p_town_22_plus_one", "p_town_22", 1), #SB : obvious random range
    (store_random_in_range, ":selected_town", towns_begin, towns_end),
    (spawn_around_party, ":selected_town", "pt_manhunters"),
  ]),



  (1.0, 0.0, 0.0, [
  (check_quest_active, "qst_track_down_bandits"),
  (neg|check_quest_failed, "qst_track_down_bandits"),
  (neg|check_quest_succeeded, "qst_track_down_bandits"),

  ],
   [
    (quest_get_slot, ":bandit_party", "qst_track_down_bandits", slot_quest_target_party),
	(try_begin),
		(party_is_active, ":bandit_party"),
		(store_faction_of_party, ":bandit_party_faction", ":bandit_party"),
		(neg|is_between, ":bandit_party_faction", kingdoms_begin, kingdoms_end), #ie, the party has not respawned as a non-bandit


		(assign, ":spot_range", 8),
		(try_begin),
			(is_currently_night),
			(assign, ":spot_range", 5),
		(try_end),

		(try_for_parties, ":party"),
			(gt, ":party", "p_spawn_points_end"),

			(store_faction_of_party, ":faction", ":party"),
			(is_between, ":faction", kingdoms_begin, kingdoms_end),


			(store_distance_to_party_from_party, ":distance", ":party", ":bandit_party"),
			(lt, ":distance", ":spot_range"),
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_party_name, s4, ":party"),
				(display_message, "@{!}DEBUG -- Wanted bandits spotted by {s4}"),
			(try_end),

			(call_script, "script_get_closest_center", ":bandit_party"),
			(assign, ":nearest_center", reg0),
#			(try_begin),
#				(get_party_ai_current_behavior, ":behavior", ":party"),
#				(eq, ":behavior", ai_bhvr_attack_party),
#				(call_script, "script_add_log_entry",  logent_party_chases_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(else_try),
#				(eq, ":behavior", ai_bhvr_avoid_party),
#				(call_script, "script_add_log_entry",  logent_party_runs_from_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(else_try),
			(call_script, "script_add_log_entry",  logent_party_spots_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(try_end),
		(try_end),
	(else_try), #Party not found
		(display_message, "str_bandits_eliminated_by_another"),
        (call_script, "script_abort_quest", "qst_track_down_bandits", 0),
	(try_end),
   ]),


##Tax Collectors
  (2.0, 0, 0, [(store_random_party_of_template, reg(2), "pt_prisoner_train_party"),
               (party_is_in_any_town,reg(2)),
               ],
              [(store_faction_of_party, ":faction_no", reg(2)),
               (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
               (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
               (party_set_ai_object,reg(2),reg0),
               (party_set_flags, reg(2), pf_default_behavior, 0),
            ]),

##Caravans
  (4.0, 0, 0.0,
   [
     (eq, "$caravan_escort_state", 1), #cancel caravan_escort_state if caravan leaves the destination
     (assign, ":continue", 0),
     (try_begin),
       (neg|party_is_active, "$caravan_escort_party_id"),
       (assign, ":continue", 1),
     (else_try),
       (get_party_ai_object, ":ai_object", "$caravan_escort_party_id"),
       (neq, ":ai_object", "$caravan_escort_destination_town"),
       (assign, ":continue", 1),
     (try_end),
     (eq, ":continue", 1),
     ],
   [
     (assign, "$caravan_escort_state", 0),
     ]),

##Kingdom Parties
  (1.0, 0, 0.0, [],
   [(try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),

      (try_begin),
        (store_random_in_range, ":random_no", 0, 100),
        (lt, ":random_no", 10),
        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_kingdom_caravan),
      (try_end),

    (try_end),
    ]),


#Companion quests
##### TODO: QUESTS COMMENT OUT BEGIN

###########################################################################
### Random Governer Quest triggers
###########################################################################

# Incriminate Loyal Advisor quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_incriminate_loyal_commander"),
       (neg|check_quest_concluded, "qst_incriminate_loyal_commander"),
       (quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_current_state, 2),
       (quest_get_slot, ":quest_target_center", "qst_incriminate_loyal_commander", slot_quest_target_center),
       (quest_get_slot, ":quest_target_party", "qst_incriminate_loyal_commander", slot_quest_target_party),
       (try_begin),
         (neg|party_is_active, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
         (call_script, "script_fail_quest", "qst_incriminate_loyal_commander"),
       (else_try),
         (party_is_in_town, ":quest_target_party", ":quest_target_center"),
         (remove_party, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
         (quest_get_slot, ":quest_object_troop", "qst_incriminate_loyal_commander", slot_quest_object_troop),
         (assign, ":num_available_factions", 0),
         (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
           (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
           (neq, ":faction_no", "fac_player_supporters_faction"),
           (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
           (val_add, ":num_available_factions", 1),
         (try_end),
         (try_begin),
           (gt, ":num_available_factions", 0),
           (store_random_in_range, ":random_faction", 0, ":num_available_factions"),
           (assign, ":target_faction", -1),
           (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
             (eq, ":target_faction", -1),
             (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
             (neq, ":faction_no", "fac_player_supporters_faction"),
             (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
             (val_sub, ":random_faction", 1),
             (lt, ":random_faction", 0),
             (assign, ":target_faction", ":faction_no"),
           (try_end),
         (try_end),
         (try_begin),
           (gt, ":target_faction", 0),
           (call_script, "script_change_troop_faction", ":quest_object_troop", ":target_faction"),
         (else_try),
           (call_script, "script_change_troop_faction", ":quest_object_troop", "fac_robber_knights"),
         (try_end),
         (call_script, "script_succeed_quest", "qst_incriminate_loyal_commander"),
       (try_end),
    ],
   []
   ),
# Runaway Peasants quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_bring_back_runaway_serfs"),
       (neg|check_quest_concluded, "qst_bring_back_runaway_serfs"),
       (quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
       (quest_get_slot, ":quest_target_center", "qst_bring_back_runaway_serfs", slot_quest_target_center),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_1"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_1"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_2"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_2"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_3"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_3"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
         (try_end),
       (try_end),
       (assign, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_returned"),
       (val_add, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_fleed"),
       (ge, ":sum_removed", 3),
       (try_begin),
         (ge, "$qst_bring_back_runaway_serfs_num_parties_returned", 3),
         (call_script, "script_succeed_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (eq, "$qst_bring_back_runaway_serfs_num_parties_returned", 0),
         (call_script, "script_fail_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (call_script, "script_conclude_quest", "qst_bring_back_runaway_serfs"),
       (try_end),
    ],
   []
   ),
# Follow Spy quest
  (0.5, 0.0, 0.0,
   [
       (check_quest_active, "qst_follow_spy"),
       (eq, "$qst_follow_spy_no_active_parties", 0),
       (quest_get_slot, ":quest_giver_center", "qst_follow_spy", slot_quest_giver_center),
       (quest_get_slot, ":quest_object_center", "qst_follow_spy", slot_quest_object_center),
       (assign, ":abort_meeting", 0),
       (try_begin),
         (this_or_next|ge, "$qst_follow_spy_run_away", 2),
         (this_or_next|neg|party_is_active, "$qst_follow_spy_spy_party"),
         (neg|party_is_active, "$qst_follow_spy_spy_partners_party"),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 0),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_party"),
         (try_begin),
           (assign, ":min_distance", 3),
           (try_begin),
             (is_currently_night),
             (assign, ":min_distance", 1),
           (try_end),
           (le, ":cur_distance", ":min_distance"),
           (store_distance_to_party_from_party, ":player_distance_to_quest_giver_center", "p_main_party", ":quest_giver_center"),
           (gt, ":player_distance_to_quest_giver_center", 1),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
             (assign, ":abort_meeting", 1),
             (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "$qst_follow_spy_spy_partners_party", "$qst_follow_spy_spy_party"),
           (le, ":cur_distance", 1),
           (party_attach_to_party, "$qst_follow_spy_spy_party", "$qst_follow_spy_spy_partners_party"),
           (assign, "$qst_follow_spy_meeting_state", 1),
           (assign, "$qst_follow_spy_meeting_counter", 0),
         (try_end),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 1),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_partners_party"),
         (try_begin),
           (le, ":cur_distance", 1),
           (party_detach, "$qst_follow_spy_spy_party"),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
             (assign, ":abort_meeting", 1),
             (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (val_add, "$qst_follow_spy_meeting_counter", 1),
           (gt, "$qst_follow_spy_meeting_counter", 4),
           (party_detach, "$qst_follow_spy_spy_party"),
           (assign, ":abort_meeting", 1),
           (assign, "$qst_follow_spy_meeting_state", 2),
         (try_end),
       (try_end),
       (try_begin),
         (eq, ":abort_meeting", 1),
         (party_set_ai_object, "$qst_follow_spy_spy_party", ":quest_giver_center"),

         (party_set_ai_object, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),

         (party_set_ai_behavior, "$qst_follow_spy_spy_party", ai_bhvr_travel_to_party),
         (party_set_ai_behavior, "$qst_follow_spy_spy_partners_party", ai_bhvr_travel_to_party),
         (party_set_flags, "$qst_follow_spy_spy_party", pf_default_behavior, 0),
         (party_set_flags, "$qst_follow_spy_spy_partners_party", pf_default_behavior, 0),
       (try_end),
       (assign, ":num_active", 0),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_party", ":quest_giver_center"),
         (remove_party, "$qst_follow_spy_spy_party"),
         (assign, "$qst_follow_spy_spy_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_partners_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
         (remove_party, "$qst_follow_spy_spy_partners_party"),
         (assign, "$qst_follow_spy_partner_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (eq, "$qst_follow_spy_partner_back_in_town",1),
         (eq, "$qst_follow_spy_spy_back_in_town",1),
         (call_script, "script_fail_quest", "qst_follow_spy"),
       (try_end),
       (try_begin),
         (eq, ":num_active", 0),
         (assign, "$qst_follow_spy_no_active_parties", 1),
         (party_count_prisoners_of_type, ":num_spies", "p_main_party", "trp_spy"),
         (party_count_prisoners_of_type, ":num_spy_partners", "p_main_party", "trp_spy_partner"),
         (gt, ":num_spies", 0),
         (gt, ":num_spy_partners", 0),
         (call_script, "script_succeed_quest", "qst_follow_spy"),
       (try_end),
    ],
   []
   ),


#########################################################################
# Random MERCHANT quest triggers
####################################
 # Apply interest to merchants guild debt  1% per week
  (24.0 * 7, 0.0, 0.0,
   [],
   [
       (val_mul,"$debt_to_merchants_guild",101),
       (val_div,"$debt_to_merchants_guild",100)
    ]
   ),
   #SB : deprecate these triggers, set party order directly
# Escort merchant caravan:
  (1, 0.0, ti_once, [
                   # (check_quest_active, "qst_escort_merchant_caravan"),
                   # (eq, "$escort_merchant_caravan_mode", 1)
                   ],
                  [
                   # (quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                   # (try_begin),
                     # (party_is_active, ":quest_target_party"),
                     # (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
                     # (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                   # (try_end),
                   ]),
  (1, 0.0, ti_once, [
                    # (check_quest_active, "qst_escort_merchant_caravan"),
                    # (eq, "$escort_merchant_caravan_mode", 0),
                    ],
                   [
                    # (quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                    # (try_begin),
                      # (party_is_active, ":quest_target_party"),
                      # (party_set_ai_behavior, ":quest_target_party", ai_bhvr_escort_party),
                      # (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                      # (party_set_ai_object, ":quest_target_party", "p_main_party"),
                    # (try_end),
                    ]),

  (0.3, 0, 1.1, [
                 (check_quest_active, "qst_escort_merchant_caravan"),
                 (quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                 (neg|party_is_active,":quest_target_party"),
                ],
                [
                 (call_script, "script_abort_quest", "qst_escort_merchant_caravan", 2),
                ]),

# Troublesome bandits
  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_failed, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (eq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(display_message, "str_bandits_eliminated_by_another"),
                   (call_script, "script_abort_quest", "qst_troublesome_bandits", 0),
                   ]),

  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_succeeded, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (neq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(call_script, "script_succeed_quest", "qst_troublesome_bandits"),]),

# Kidnapped girl:
   (1, 0, 0,
   [(check_quest_active, "qst_kidnapped_girl"),
    (quest_get_slot, ":quest_target_party", "qst_kidnapped_girl", slot_quest_target_party),
    (party_is_active, ":quest_target_party"),
    (party_is_in_any_town, ":quest_target_party"),
    (remove_party, ":quest_target_party"),
    ],
   []
   ),


# #Rebellion changes begin
# #move

  # (0, 0, 24 * 14,
   # [
        # (try_for_range, ":pretender", pretenders_begin, pretenders_end),
          # (troop_set_slot, ":pretender", slot_troop_cur_center, 0),
          # (neq, ":pretender", "$supported_pretender"),
          # (troop_get_slot, ":target_faction", ":pretender", slot_troop_original_faction),
          # (faction_slot_eq, ":target_faction", slot_faction_state, sfs_active),
          # (faction_slot_eq, ":target_faction", slot_faction_has_rebellion_chance, 1),
          # (neg|troop_slot_eq, ":pretender", slot_troop_occupation, slto_kingdom_hero),

          # (assign, ":break", 30),
          # (try_for_range, ":unused", 0, ":break"),
            # (troop_slot_eq, ":pretender", slot_troop_cur_center, 0),
            # (store_random_in_range, ":town", towns_begin, towns_end),
            # (party_get_slot, ":town_lord", ":town", slot_town_lord),
            # (ge, ":town_lord", "trp_player"), #not unassigned
            # (store_faction_of_party, ":town_faction", ":town"),
            # (store_relation, ":relation", ":town_faction", ":target_faction"),
            # (le, ":relation", 0), #fail if nothing qualifies

            # (troop_set_slot, ":pretender", slot_troop_cur_center, ":town"),
            # (try_begin), #SB : cheat mode
              # (eq, "$cheat_mode", 1),
              # (str_store_troop_name_link, 4, ":pretender"),
              # (str_store_party_name_link, 5, ":town"),
              # (display_message, "@{!}{s4} is in {s5}"),
            # (try_end),
            # (try_begin), #SB : actually give out base gold and some renown
              # (ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
              # (call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", 100, ":pretender"),
              # # do host relations
              # (assign, ":renown", 5),
              # (try_begin),
                # (neq, ":town_lord", "trp_player"),
                # (store_random_in_range, ":relation", -3, 4),
                # (call_script, "script_troop_change_relation_with_troop", ":pretender", ":town_lord", ":relation"),
              # (try_end),
              # #do other relations
              # (call_script, "script_get_heroes_attached_to_center", ":town", "p_temp_party"),
              # (party_get_num_companion_stacks, ":num_stacks", "p_temp_party"),
              # (try_for_range, ":stack_no", 0, ":num_stacks"),
                # (party_stack_get_troop_id, ":troop_no", "p_temp_party", ":stack_no"),
                # (neq, ":troop_no", ":pretender"),
                # (neq, ":troop_no", ":town_lord"), #double effect if actually at home?
                # (store_random_in_range, ":relation", -2, 3),
                # (call_script, "script_troop_change_relation_with_troop", ":pretender", ":troop_no", ":relation"),
                # (try_begin), #a bit of variation
                  # (ge, ":relation", 0),
                  # (val_add, ":renown", 1),
                # (else_try),
                  # (val_sub, ":renown", 1),
                # (try_end),
              # (try_end),
              # (call_script, "script_change_troop_renown", ":troop_no", ":renown"),
            # (try_end),
            # (assign, ":break", 0),
          # (try_end),

# #        (try_for_range, ":rebel_faction", rebel_factions_begin, rebel_factions_end),
# #            (faction_get_slot, ":rebellion_status", ":rebel_faction", slot_faction_state),
# #            (eq, ":rebellion_status", sfs_inactive_rebellion),
# #            (faction_get_slot, ":pretender", ":rebel_faction", slot_faction_leader),
# #            (faction_get_slot, ":target_faction", ":rebel_faction", slot_faction_rebellion_target),#

# #            (store_random_in_range, ":town", towns_begin, towns_end),
# #            (store_faction_of_party, ":town_faction", ":town"),
# #            (store_relation, ":relation", ":town_faction", ":target_faction"),
# #            (le, ":relation", 0), #fail if nothing qualifies

 # #           (faction_set_slot, ":rebel_faction", slot_faction_inactive_leader_location, ":town"),
        # (try_end),
       # ],
# []
# ),
# #Rebellion changes end

#NPC system changes begin
#Move unemployed NPCs around taverns
   (24 * 15 , 0, 0,
   [
    (call_script, "script_update_companion_candidates_in_taverns"),
    # (call_script, "script_new_npc_ai"),
    ],
   []
   ),

#Process morale and determine personality clashes
  (0, 0, 24,
   [],
[

#Count NPCs in party and get the "grievance divisor", which determines how fast grievances go away
#Set their relation to the player
        (assign, ":npcs_in_party", 0),
        (assign, ":grievance_divisor", 100),
        (try_for_range, ":npc1", companions_begin, companions_end),
            (main_party_has_troop, ":npc1"),
            (val_add, ":npcs_in_party", 1),
        (try_end),
        (val_sub, ":grievance_divisor", ":npcs_in_party"),
        (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
        (val_add, ":grievance_divisor", ":persuasion_level"),
        (assign, reg7, ":grievance_divisor"),

#        (display_message, "@{!}Process NPC changes. GD: {reg7}"),



##Activate personality clash from 24 hours ago
        (try_begin), #scheduled personality clashes require at least 24hrs together
             (gt, "$personality_clash_after_24_hrs", 0),
             (eq, "$disable_npc_complaints", 0),
             (try_begin),
                  (troop_get_slot, ":other_npc", "$personality_clash_after_24_hrs", slot_troop_personalityclash_object),
                  (main_party_has_troop, "$personality_clash_after_24_hrs"),
                  (main_party_has_troop, ":other_npc"),
                  (assign, "$npc_with_personality_clash", "$personality_clash_after_24_hrs"),
             (try_end),
             (assign, "$personality_clash_after_24_hrs", 0),
        (try_end),
#


        (try_for_range, ":npc", companions_begin, companions_end),
###Reset meeting variables
            (troop_set_slot, ":npc", slot_troop_turned_down_twice, 0),
            (try_begin),
                (troop_slot_eq, ":npc", slot_troop_met, 1),
                (troop_set_slot, ":npc", slot_troop_met_previously, 1),
            (try_end),

###Check for coming out of retirement
            (troop_get_slot, ":occupation", ":npc", slot_troop_occupation),
            (try_begin),
                (eq, ":occupation", slto_retirement),
                (troop_get_slot, ":renown_min", ":npc", slot_troop_return_renown),

                (str_store_troop_name, s31, ":npc"),
                (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
                (assign, reg4, ":player_renown"),
                (assign, reg5, ":renown_min"),
#                (display_message, "@{!}Test {s31}  for retirement return {reg4}, {reg5}."),

                (gt, ":player_renown", ":renown_min"),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, 0),
                (troop_set_slot, ":npc", slot_troop_morality_penalties, 0),
                (troop_set_slot, ":npc", slot_troop_occupation, 0),
            (try_end),


#Check for political issues
			(try_begin), #does npc's opponent pipe up?
				(troop_slot_ge, ":npc", slot_troop_days_on_mission, 5),
				(troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_kingsupport),

				(troop_get_slot, ":other_npc", ":npc", slot_troop_kingsupport_opponent),
				(troop_slot_eq, ":other_npc", slot_troop_kingsupport_objection_state, 0),

				(troop_set_slot, ":other_npc", slot_troop_kingsupport_objection_state, 1),

				(str_store_troop_name, s3, ":npc"),
				(str_store_troop_name, s4, ":other_npc"),

				(try_begin),
					(eq, "$cheat_mode", 1),
					(display_message, "str_s4_ready_to_voice_objection_to_s3s_mission_if_in_party"),
				(try_end),
			(try_end),

			#Check for quitting
            (try_begin),
                (main_party_has_troop, ":npc"),

                (call_script, "script_dplmc_npc_morale", ":npc", 0), #SB : just the number
                (assign, ":npc_morale", reg0),

                (try_begin),
					(lt, ":npc_morale", 20),
					
					# #They don't try to leave if everything is going fine (and you have a car)
					(troop_get_slot, reg6, "trp_player", slot_troop_condition_hunger),
					(troop_get_slot, reg1, "trp_player", slot_troop_condition_thirst),
					(troop_get_slot, reg2, "trp_player", slot_troop_condition_rest),
					(party_get_morale, reg9, "p_main_party"),
					(this_or_next|le, reg6, 50), 
					(this_or_next|le, reg1, 50),
					(this_or_next|le, reg2, 25),
					(this_or_next|le, reg9, 50),
					(this_or_next|le, "$car_condition", 25),
					(le, "$g_camp_quality", 50),
					
                    (store_random_in_range, ":random", 0, 100),
                    (val_add, ":npc_morale", ":random"),
                    (lt, ":npc_morale", 20),
                    (neq, "$disable_npc_complaints", 1), #SB : disable
                    (assign, "$npc_is_quitting", ":npc"),
                (try_end),

				#Reduce grievance over time (or augment, if party is overcrowded
                (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),

                (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),


				#Change personality grievance levels
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalityclash_object),
                    (main_party_has_troop, ":object"),
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash_state),
                (try_end),
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash2_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalityclash2_object),
                    (main_party_has_troop, ":object"),
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash2_state),
                (try_end),
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalitymatch_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalitymatch_object),
                    (main_party_has_troop, ":object"),
                    (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                    (val_mul, ":grievance", 9),
                    (val_div, ":grievance", 10),
                    (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),
                (try_end),



#Check for new personality clashes

				#Active personality clash 1 if at least 24 hours have passed
                (try_begin),
                    (eq, "$disable_npc_complaints", 0),
                    (eq, "$npc_with_personality_clash", 0),
                    (eq, "$npc_with_personality_clash_2", 0),
                    (eq, "$personality_clash_after_24_hrs", 0),
                    (troop_slot_eq, ":npc", slot_troop_personalityclash_state, 0),
                    (troop_get_slot, ":other_npc", ":npc", slot_troop_personalityclash_object),
                    (main_party_has_troop, ":other_npc"),
                    (assign, "$personality_clash_after_24_hrs", ":npc"),
                (try_end),

				#Personality clash 2 and personality match is triggered by battles
				(try_begin),
					(eq, "$npc_with_political_grievance", 0),

					(troop_slot_eq, ":npc", slot_troop_kingsupport_objection_state, 1),
					(assign, "$npc_with_political_grievance", ":npc"),
				(try_end),

			#main party does not have troop, and the troop is a companion
			(else_try),
				(neg|main_party_has_troop, ":npc"),
				(eq, ":occupation", slto_player_companion),

                (troop_get_slot, ":days_on_mission", ":npc", slot_troop_days_on_mission),

                (try_begin), #debug
                    (eq, "$cheat_mode", 1),
                    (str_store_troop_name, s10, ":npc"),
                    (assign, reg0, ":days_on_mission"),
                    (display_message, "@Checking rejoin of {s10} days on mission: {reg0}"),
                (try_end),

                (try_begin),
                    (gt, ":days_on_mission", 0),
                    (val_sub, ":days_on_mission", 1),
                    (troop_set_slot, ":npc", slot_troop_days_on_mission, ":days_on_mission"),
                ##diplomacy begin
                (else_try),
                  (this_or_next|troop_slot_eq, ":npc", slot_troop_current_mission, dplmc_npc_mission_spy_request), #spy mission
                  (troop_slot_eq, ":npc", slot_troop_current_mission, dplmc_npc_mission_rescue_prisoner), #SB : rescue mission
                  (troop_slot_ge, ":npc", dplmc_slot_troop_mission_diplomacy, 1), #caught

                  (try_begin), #use hired blade for spy
                    (troop_slot_eq, ":npc", slot_troop_current_mission, dplmc_npc_mission_spy_request),
                    (troop_set_slot, "trp_hired_blade", slot_troop_mission_object, ":npc"),
                    (assign, "$npc_to_rejoin_party", "trp_hired_blade"),
                  (else_try), #use town walker
                    (troop_slot_eq, ":npc", slot_troop_current_mission, dplmc_npc_mission_rescue_prisoner),
                    (troop_get_slot, ":town_no", ":npc", slot_troop_town_with_contacts),
                    (store_random_in_range, ":slot_no", slot_center_walker_0_troop, slot_center_walker_0_troop + num_town_walkers),
                    (party_get_slot, ":walker_no", ":town_no", ":slot_no"),
                    (troop_set_slot, ":walker_no", slot_troop_mission_object, ":npc"),
                    (assign, "$npc_to_rejoin_party", ":walker_no"),
                  (try_end),
                ##diplomacy end
				(else_try),
					(troop_slot_ge, ":npc", slot_troop_current_mission, 1),

					#If the hero can join
					(this_or_next|neg|troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_rejoin_when_possible),
					(hero_can_join, "p_main_party"), #SB : fix this stupid bug

					(assign, "$npc_to_rejoin_party", ":npc"),
				(try_end),
            (try_end),
        (try_end),
    ]),




##diplomacy begin
  # Appoint chamberlain
   (24 , 0, 24 * 12,
   [],
   [
    (assign, ":has_fief", 0),
    (try_for_range, ":center_no", centers_begin, centers_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
      (eq, ":lord_troop_id", "trp_player"),
      (assign, ":has_fief", 1),
    (try_end),
    (eq, ":has_fief", 1),

    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, "$g_player_chamberlain"),
      (display_message, "@{!}DEBUG : chamberlain: {reg0}"),
    (try_end),

    (assign, ":notification", 0),
    (try_begin),
      (eq, "$g_player_chamberlain", 0),
      (assign, ":notification", 1),
    (else_try),
      (neq, "$g_player_chamberlain", -1),
      (neq, "$g_player_chamberlain", "trp_dplmc_chamberlain"),
      (assign, ":notification", 1),
    (try_end),

    (try_begin),
      (eq, ":notification", 1),
      (call_script, "script_add_notification_menu", "mnu_dplmc_notification_appoint_chamberlain", 0, 0),
    (try_end),]
   ),

  # Appoint constable
   (24 , 0, 24 * 13,
   [],
   [
    (assign, ":has_fief", 0),
    (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
      (eq, ":lord_troop_id", "trp_player"),
      (assign, ":has_fief", 1),
    (try_end),
    (eq, ":has_fief", 1),

    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, "$g_player_constable"),
      (display_message, "@{!}DEBUG : constable: {reg0}"),
    (try_end),

    (assign, ":notification", 0),
    (try_begin),
      (eq, "$g_player_constable", 0),
      (assign, ":notification", 1),
    (else_try),
      (neq, "$g_player_constable", -1),
      (neq, "$g_player_constable", "trp_dplmc_constable"),
      (assign, ":notification", 1),
    (try_end),

    (try_begin),
      (eq, ":notification", 1),
      (call_script, "script_add_notification_menu", "mnu_dplmc_notification_appoint_constable", 0, 0),
    (try_end),
    ]
   ),

  # Appoint chancellor
   (24 , 0, 24 * 14,
   [],
   [
   (assign, ":has_fief", 0),
    (try_for_range, ":center_no", towns_begin, towns_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
      (eq, ":lord_troop_id", "trp_player"),
      (assign, ":has_fief", 1),
    (try_end),
    (eq, ":has_fief", 1),

    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, "$g_player_chancellor"),
      (display_message, "@{!}DEBUG : chancellor: {reg0}"),
    (try_end),

    (assign, ":notification", 0),
    (try_begin),
      (eq, "$g_player_chancellor", 0),
      (assign, ":notification", 1),
    (else_try),
      (neq, "$g_player_chancellor", -1),
      (neq, "$g_player_chancellor", "trp_dplmc_chancellor"),
      (assign, ":notification", 1),
    (try_end),

    (try_begin),
      (eq, ":notification", 1),
      (call_script, "script_add_notification_menu", "mnu_dplmc_notification_appoint_chancellor", 0, 0),
    (try_end),
    ]),

  #initialize autoloot feature if you have a chamberlain
  ##diplomacy start+
  #Disable this: autoloot gets initialized elsewhere.
  (24, 0, ti_once,
  [
	  ##NEW:
	  (eq, 0, 1),
	  ##OLD:
      #(store_skill_level, ":inv_skill", "skl_inventory_management", "trp_player"),
      #(gt, "$g_player_chamberlain", 0),
      #(ge, ":inv_skill", 3),
  ],
  [
	##NEW:
	#This doesn't ever get called, but if it did here's what should happen"
	(call_script, "script_dplmc_initialize_autoloot", 1),#argument "1" forces this to make changes
	##OLD:
    #(call_script, "script_dplmc_init_item_difficulties"),
    #(call_script, "script_dplmc_init_item_base_score"),
    #(assign, "$g_autoloot", 1),
  ]),

  (0.1, 0.5, 0, [(map_free,0),(eq,"$g_move_fast", 1)], [(assign,"$g_move_fast", 0)]),

##diplomacy end

#new
##########################################################################################  
#conditions      
  (24, 0, 0.0,
  [
    (eq,"$ondrugs",2),
  ],
  [
    (assign,"$ondrugs",0),
    (dialog_box, "str_drug_off", "str_event"),    
  ]),  
  
  (1, 0, 0.0,
  [
    (eq,"$ondrugs",1),
  ],
  [
    (assign,"$ondrugs",2),
  ]),   
  
  (48, 0, 0.0,
  [
    (this_or_next|eq,"$g_player_tigh_wound",2),
    (this_or_next|eq,"$g_player_calf_wound",2),
    (this_or_next|eq,"$g_player_foot_wound",2),
    (this_or_next|eq,"$g_player_spine_wound",2),
    (this_or_next|eq,"$g_player_thorax_wound",2),
    (this_or_next|eq,"$g_player_head_wound",2),
    (this_or_next|eq,"$g_player_shoulder_wound",2),
    (this_or_next|eq,"$g_player_arm_wound",2),
    (eq,"$g_player_hand_wound",2), 
  ],
  [
    (assign,"$g_player_tigh_wound",0),
    (assign,"$g_player_calf_wound",0),
    (assign,"$g_player_foot_wound",0),
    (assign,"$g_player_spine_wound",0),
    (assign,"$g_player_thorax_wound",0),
    (assign,"$g_player_head_wound",0),
    (assign,"$g_player_shoulder_wound",0),
    (assign,"$g_player_arm_wound",0),
    (assign,"$g_player_hand_wound",0),  
    (dialog_box, "str_wound_off", "str_event"),    
  ]),   

  (24, 0, 0.0,
  [
    (this_or_next|eq,"$g_player_tigh_wound",1),
    (this_or_next|eq,"$g_player_calf_wound",1),
    (this_or_next|eq,"$g_player_foot_wound",1),
    (this_or_next|eq,"$g_player_spine_wound",1),
    (this_or_next|eq,"$g_player_thorax_wound",1),
    (this_or_next|eq,"$g_player_head_wound",1),
    (this_or_next|eq,"$g_player_shoulder_wound",1),
    (this_or_next|eq,"$g_player_arm_wound",1),
    (eq,"$g_player_hand_wound",1), 

    (this_or_next|player_has_item, "itm_bandage"),
    (player_has_item, "itm_medkit"),
    
    (store_skill_level, ":wound_treatment", "skl_wound_treatment", "trp_player"),    
    (ge,":wound_treatment",1),
    
    (try_begin),
        (eq,":wound_treatment",1),
        (store_random_in_range,":chance",1,11),
    (else_try),
        (eq,":wound_treatment",2),
        (store_random_in_range,":chance",1,10),
    (else_try),
        (eq,":wound_treatment",3),
        (store_random_in_range,":chance",1,9),
    (else_try),
        (eq,":wound_treatment",4),
        (store_random_in_range,":chance",1,8),
    (else_try),
        (eq,":wound_treatment",5),
        (store_random_in_range,":chance",1,7),
    (else_try),
        (eq,":wound_treatment",6),
        (store_random_in_range,":chance",1,6),
    (else_try),
        (eq,":wound_treatment",7),
        (store_random_in_range,":chance",1,5),
    (else_try),
        (eq,":wound_treatment",8),
        (store_random_in_range,":chance",1,4),
    (else_try),
        (eq,":wound_treatment",9),
        (store_random_in_range,":chance",1,3),
    (else_try),
        (assign,":chance",1),    
    (try_end),
    (eq,":chance",1),    
  ],
  [
    (assign,"$g_player_tigh_wound",0),
    (assign,"$g_player_calf_wound",0),
    (assign,"$g_player_foot_wound",0),
    (assign,"$g_player_spine_wound",0),
    (assign,"$g_player_thorax_wound",0),
    (assign,"$g_player_head_wound",0),
    (assign,"$g_player_shoulder_wound",0),
    (assign,"$g_player_arm_wound",0),
    (assign,"$g_player_hand_wound",0), 

    (troop_get_inventory_capacity, ":capacity", "trp_player"),    
    (try_for_range, ":cur_slot", 0, ":capacity"),
      (troop_get_inventory_slot, ":cur_item", "trp_player", ":cur_slot"),
      (eq, ":cur_item", "itm_bandage"),
      (assign, ":capacity", 0),
      (troop_inventory_slot_get_item_amount, ":cur_amount", "trp_player", ":cur_slot"),
      (try_begin),           
        (le, ":cur_amount", 1),
        (troop_remove_item, "trp_player", ":cur_item"),    
      (else_try),                           
        (val_sub, ":cur_amount", 1),
        (troop_inventory_slot_set_item_amount, "trp_player", ":cur_slot", ":cur_amount"),
      (try_end),      
    (try_end),       
    (dialog_box, "str_wound_off", "str_event"),    
  ]),   
##########################################################################################  

  
      # (0.0, 0, 0, [            (key_clicked, key_tab), #Retreat
# ],
       # [
         # (question_box, "str_do_you_wish_to_leave_tutorial"),
        # ]),
      # (0.0, 0, 0, [],
       # [(store_trigger_param_1,":answer"),
        # (try_begin),
          # (eq,":answer",0),
          # (display_message,"@yes"),
          # (start_presentation, "prsnt_test_logo"),
        # (else_try),
                  # (eq,":answer",1),

          # (display_message,"@no"),
        # (try_end),
        
# # (change_screen_quit),
        # ]),

##########################################################################################  
(0.0, 0, 0, [(eq, "$g_ammo_unequip", 1),],
	[    
    (call_script, "script_cf_player_ammo_check",0),
	]),

 
]
# modmerger_start version=201 type=2
try:
    component_name = "triggers"
    var_set = { "triggers" : triggers }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
