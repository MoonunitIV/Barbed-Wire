from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from header_items import *
from header_skills import *
from module_constants import *

from ID_skyboxes import *
from ID_postfx_params import *

from compiler import *
####################################################################################################################
#   Each mission-template is a tuple that contains the following fields:
#  1) Mission-template id (string): used for referencing mission-templates in other files.
#     The prefix mt_ is automatically added before each mission-template id
#
#  2) Mission-template flags (int): See header_mission-templates.py for a list of available flags
#  3) Mission-type(int): Which mission types this mission template matches.
#     For mission-types to be used with the default party-meeting system,
#     this should be 'charge' or 'charge_with_ally' otherwise must be -1.
#
#  4) Mission description text (string).
#  5) List of spawn records (list): Each spawn record is a tuple that contains the following fields:
#    5.1) entry-no: Troops spawned from this spawn record will use this entry
#    5.2) spawn flags.
#    5.3) alter flags. which equipment will be overriden
#    5.4) ai flags.
#    5.5) Number of troops to spawn.
#    5.6) list of equipment to add to troops spawned from here (maximum 8).
#  6) List of triggers (list).
#     See module_triggers.py for infomation about triggers.
#
#  Please note that mission templates is work in progress and can be changed in the future versions.
#
####################################################################################################################

pilgrim_disguise = [itm_hood_1,itm_robe_1,itm_staff, itm_pistol_snubnosed_revolver, itm_pistol_ammo]
pilgrim_disguise2 = [itm_hood_1,itm_robe_1,itm_staff, itm_pistol_walther_ppk, itm_pistol_ammo]
pilgrim_disguise3 = [itm_hood_1,itm_robe_1,itm_staff, itm_pistol_walther_ppk_sil, itm_pistol_ammo]
af_castle_lord = af_override_horse | af_override_weapons| af_require_civilian

########################################################
## tocan orders
########################################################
#to prevent presentations from starting while old ones are still running
common_presentation_switcher = (
  .05, 0, 0, [
    (neq, "$switch_presentation_new", 0), #we can safely ignore prsnt_game_start
    (neg|is_presentation_active, "$switch_presentation_old"),
    ], [
    (start_presentation, "$switch_presentation_new"),
    (assign, "$switch_presentation_old", "$switch_presentation_new"), #this makes the heroic assumption that all presentations use this system
    (assign, "$switch_presentation_new", 0),
    ])
battle_panel_triggers = [ #4 triggers
  common_presentation_switcher,

  (ti_on_agent_spawn, 0, 0, [], [
      (store_trigger_param_1, ":agent_no"),
      (agent_set_slot, ":agent_no", slot_agent_map_overlay_id, 0),
  ]),

  (0, 0, 0, [
      (game_key_clicked, gk_view_orders),
      #(neg|main_hero_fallen),#too awkward if can't issue orders, troops end up hiding on cover and battle never ends
	  ],
    [
      (try_begin),
        (is_presentation_active, "prsnt_battle"),
        (presentation_set_duration, 0),

      (else_try),
        (presentation_set_duration, 0),
        (assign, "$switch_presentation_new", "prsnt_battle"),
      (try_end),
  ]),

  (0.1, 0, 0, [(is_presentation_active, "prsnt_battle")],
    [
      # (try_begin),
      # (gt, "$spawn_step", 0),
      # (val_sub, "$spawn_step", 1),
      # # (display_message, "@{!}INFO: I avoided the script in the first round!"),
      # # (overlay_set_alpha, 11, 0),#enable to test if the real cause of VC-2685 still exists
      # (else_try),
      (call_script, "script_update_order_panel_statistics_and_map"),
      # (try_end),
  ]),
]
extended_battle_menu = [  #15 triggers
  # Trigger file: extended_battle_menu_init
  (ti_before_mission_start ,0, ti_once, [], [
      (assign, "$gk_order", 0),	#tracks the first tier order given
      (assign, "$gk_order_hold_over_there", HOT_no_order),	#used to determine if F1 key is being held down
      (assign, "$native_opening_menu", 0),	#tracks whether the first tier battle menu would normally be showing
      (assign, "$g_presentation_active", 0),	#used here to track whether prsnt_battle is overridden when fake battle menu starts
      (assign, "$g_cover_order_radius", 5000),	#50m
  ]),

  common_presentation_switcher,

  # Trigger file: extended_battle_menu_division_selection
  (0,0,.1, [
      (this_or_next|game_key_clicked, gk_group0_hear),
      (this_or_next|game_key_clicked, gk_group1_hear),
      (this_or_next|game_key_clicked, gk_group2_hear),
      (this_or_next|game_key_clicked, gk_group3_hear),
      (this_or_next|game_key_clicked, gk_group4_hear),
      (this_or_next|game_key_clicked, gk_group5_hear),
      (this_or_next|game_key_clicked, gk_group6_hear),
      (this_or_next|game_key_clicked, gk_group7_hear),
      (this_or_next|game_key_clicked, gk_group8_hear),
      (this_or_next|game_key_clicked, gk_reverse_order_group),	#shows up as "unknown 6" on Native screen
      (this_or_next|game_key_clicked, gk_everyone_around_hear),
      (game_key_clicked, gk_everyone_hear),
      #(neg|main_hero_fallen),
      ],[
      (assign, "$gk_order", 0),
      (try_begin),
        (is_presentation_active, "prsnt_battle"),
        (assign, "$g_presentation_active", 1),
      (try_end),
      (presentation_set_duration, 0),
      (assign, "$switch_presentation_new", "prsnt_order_display"),
      (assign, "$native_opening_menu", 1),

      (assign, "$g_class_listening", grc_everyone),
      (try_begin),
        (game_key_clicked, gk_group0_hear),
        (assign, "$g_class_listening", grc_infantry),
      (else_try),
        (game_key_clicked, gk_group1_hear),
        (assign, "$g_class_listening", grc_archers),
      (else_try),
        (game_key_clicked, gk_group2_hear),
        (assign, "$g_class_listening", grc_cavalry),
      (else_try),
        (game_key_clicked, gk_group3_hear),
        (assign, "$g_class_listening", grc_4),
      (else_try),
        (game_key_clicked, gk_group4_hear),
        (assign, "$g_class_listening", grc_5),
      (else_try),
        (game_key_clicked, gk_group5_hear),
        (assign, "$g_class_listening", grc_6),
      (else_try),
        (game_key_clicked, gk_group6_hear),
        (assign, "$g_class_listening", grc_7),
      (else_try),
        (game_key_clicked, gk_group7_hear),
        (assign, "$g_class_listening", grc_special),
      (else_try),
        (game_key_clicked, gk_group8_hear),
        (assign, "$g_class_listening", grc_heroes),
      (else_try),
        (game_key_clicked, gk_everyone_hear),
        (assign, "$g_class_listening", grc_everyone),
      (try_end),
  ]),

  # Trigger file: extended_battle_menu_tab_out
  # (ti_tab_pressed, 0, 0, [
  # (is_presentation_active, "prsnt_order_display"),
  # ],[
  # (assign, "$gk_order", 0),
  # (assign, "$native_opening_menu", 0),
  # (presentation_set_duration, 0),
  # ]),

  # Trigger file: extended_battle_menu_esc_or_die_out
  (0, 0, 0, [
      #(this_or_next|main_hero_fallen),
      (key_is_down, key_escape),
      (is_presentation_active, "prsnt_order_display"),
      ],[
      (presentation_set_duration, 0),
      (assign, "$native_opening_menu", 0),
  ]),

  (0, 0, 0, [
     # (this_or_next|main_hero_fallen),
      (key_is_down, key_escape),
      (neq, "$gk_order", 0),
      ],[
      (assign, "$gk_order", 0),
  ]),

  # Trigger file: extended_battle_menu_hold_F1
  (.1, 0, 0, [
      (neq, "$when_f1_first_detected", 0),
      # (store_application_time, reg0),	#real time for when game time is slowed for real deployment
      (store_mission_timer_c_msec, reg0),
      (val_sub, reg0, "$when_f1_first_detected"),
      (ge, reg0, 250),	#check around .3 seconds later (Native trigger delay does not work right)
      (eq, "$gk_order", gk_order_1),	#next trigger set MOVE menu?
      ],[
      (assign, "$when_f1_first_detected", 0),

      (try_begin),
        (game_key_is_down, gk_order_1),	#BUT player is holding down key?
        (assign, "$gk_order_hold_over_there", HOT_F1_held),
        (assign, "$gk_order", 0),
        # # (store_and, reg0, "$g_first_time", first_time_hold_F1),
        # # (try_begin),
          # # (eq, reg0, 0),
          # # (val_or, "$g_first_time", first_time_hold_F1),
          # # (eq, "$g_is_quick_battle", 0),
          # # (dialog_box, "@Text", "@BLA"),
        # # (try_end),

      (else_try),
        (eq, "$gk_order_hold_over_there", HOT_F1_pressed),
        (assign, "$gk_order_hold_over_there", HOT_no_order),
        (assign, "$gk_order", 0),
      (try_end),
  ]),

  # Trigger file: extended_battle_menu_F1
  (0, 0, 0, [
      (game_key_clicked, gk_order_1),
      #(neg|main_hero_fallen)
      ], [
      # (store_application_time, "$when_f1_first_detected"),
      (store_mission_timer_c_msec, "$when_f1_first_detected"),
      # (get_player_agent_no, "$g_player"), #tocan
      (try_begin),
        #(eq, "$gk_order", 0),
        (neq, "$gk_order", gk_order_1),
        (neq, "$gk_order", gk_order_2),
        (neq, "$gk_order", gk_order_3),
        (assign, "$gk_order", gk_order_1),
        (assign, "$native_opening_menu", 0),
        (try_begin),
          (is_presentation_active, "prsnt_battle"),
          (assign, "$g_presentation_active", 1),
        (try_end),
        (presentation_set_duration, 0),	#clear main menu additions
        (assign, "$gk_order_hold_over_there", HOT_no_order),
      (else_try),
        (eq, "$gk_order", gk_order_1),	#HOLD
        (assign, "$gk_order_hold_over_there", HOT_F1_pressed),
      (else_try),
        (eq, "$gk_order", gk_order_2),	#ADVANCE
        (assign, "$gk_order", 0),
        (presentation_set_duration, 0),	#clear F2 menu additions
      (else_try),
        (eq, "$gk_order", gk_order_3),	#HOLD FIRE
        (assign, "$gk_order", 0),
      (try_end),
  ]),

  # Trigger file: extended_battle_menu_F2
  (0, 0, 0, [
      (game_key_clicked, gk_order_2),
      #(neg|main_hero_fallen)
      ], [
      (try_begin),
        #(eq, "$gk_order", 0),
        (neq, "$gk_order", gk_order_1),
        (neq, "$gk_order", gk_order_2),
        (neq, "$gk_order", gk_order_3),
        (assign, "$gk_order", gk_order_2),
        (assign, "$native_opening_menu", 0),
        (try_begin),
          (is_presentation_active, "prsnt_battle"),
          (assign, "$g_presentation_active", 1),
        (try_end),
        (presentation_set_duration, 0),
        (assign, "$switch_presentation_new", "prsnt_order_display"),
      (else_try),
        (eq, "$gk_order", gk_order_1),	#FOLLOW
        (assign, "$gk_order", 0),
      (else_try),
        (eq, "$gk_order", gk_order_2),	#FALL BACK
        (assign, "$gk_order", 0),
        (presentation_set_duration, 0),	#clear F2 menu additions
        # (call_script, "script_player_order_formations", mordr_fall_back),
      (else_try),
        (eq, "$gk_order", gk_order_3),	#FIRE AT WILL
        (assign, "$gk_order", 0),
      (try_end),
  ]),

  # Trigger file: extended_battle_menu_F3
  (0, 0, 0, [
      (game_key_clicked, gk_order_3),
      #(neg|main_hero_fallen)
      ], [
      (try_begin),
        #(eq, "$gk_order", 0),
        (neq, "$gk_order", gk_order_1),
        (neq, "$gk_order", gk_order_2),
        (neq, "$gk_order", gk_order_3),
        (assign, "$gk_order", gk_order_3),
        (assign, "$native_opening_menu", 0),
        (try_begin),
          (is_presentation_active, "prsnt_battle"),
          (assign, "$g_presentation_active", 1),
        (try_end),
        (presentation_set_duration, 0),	#clear main menu additions
      (else_try),
        (eq, "$gk_order", gk_order_1),	#CHARGE
        (assign, "$gk_order", 0),
      (else_try),
        (eq, "$gk_order", gk_order_2),	#SPREAD OUT
        (assign, "$gk_order", 0),
        (presentation_set_duration, 0),	#clear F2 menu additions
      (else_try),
        (eq, "$gk_order", gk_order_3),	#BLUNT WEAPONS
        (assign, "$gk_order", 0),
      (try_end),
  ]),

  # Trigger file: extended_battle_menu_hold_F4
  (.1, 1, 0, [
      #(neg|main_hero_fallen),

      (game_key_is_down, gk_order_4),	#BUT player is holding down key?
      ],[
      (game_key_is_down, gk_order_4),	#BUT player is holding down key?

      (assign, "$gk_order", 0),

      # (display_message, "@Cover", message_negative),
      # (set_fixed_point_multiplier, 1000),

      (mission_cam_get_position, pos1),
      (cast_ray, ":unused", pos3, pos1),
      # (position_set_z_to_ground_level, pos3),

      (agent_get_entry_no, ":entry", "$g_player"),
      (entry_point_get_position, pos65, ":entry"),
      (position_copy_origin,pos65,pos3),


      (scene_prop_get_num_instances, ":total", "spr_cover_marker"),
      (try_begin),
        (gt, ":total",0),
        (try_for_range,":cur_instance",0,":total"),
          (scene_prop_get_instance, ":instance_id", "spr_cover_marker", ":cur_instance"),
          (prop_instance_animate_to_position, ":instance_id", pos65, 1),
        (try_end),
      (else_try),
        (set_spawn_position, pos65),
        (spawn_scene_prop, "spr_cover_marker"),
      (try_end),

      (call_script, "script_cover_search_player", pos65, "$g_cover_order_radius"),
      (assign, reg1,"$g_cover_order_radius"),
      (val_div,reg1,100),
      (try_begin),
        (eq, "$g_class_listening", grc_everyone),
        (display_message,"@Everyone take cover within {reg1}m!",message_alert),
      (else_try),
        (str_store_class_name, s1, "$g_class_listening"),
        (display_message,"@{s1} take cover within {reg1}m!",message_alert),
      (try_end),

    ]),

  # Trigger file: extended_battle_menu_F4
  (0, 0, 0, [
      (game_key_clicked, gk_order_4),
      #(neg|main_hero_fallen)
      ], [
      (try_begin),
        (eq, "$gk_order", 0),	#Redisplay
        (eq, "$native_opening_menu", 1),
        (try_begin),
          (is_presentation_active, "prsnt_battle"),
          (assign, "$g_presentation_active", 1),
        (try_end),
        (presentation_set_duration, 0),
        (assign, "$switch_presentation_new", "prsnt_order_display"),
      (else_try),
        (eq, "$gk_order", gk_order_1),	#STAND GROUND
        (assign, "$gk_order", 0),
      (else_try),
        (eq, "$gk_order", gk_order_2),	#STAND CLOSER
        (assign, "$gk_order", 0),
        (presentation_set_duration, 0),	#clear F2 menu additions
      (else_try),
        (eq, "$gk_order", gk_order_3),	#ANY WEAPON
        (assign, "$gk_order", 0),
      (else_try),
        (eq, "$gk_order", gk_order_5),	#COMMAND RADIUS
        (assign, "$gk_order", 0),
        (assign, "$g_cover_order_radius", 1250),
      (else_try),
        (eq, "$gk_order", gk_order_6),	#Search Cover around Commander
        (assign, "$gk_order", 0),
        (agent_get_position,pos1,"$g_player"),
        (call_script, "script_cover_search_player", pos1, "$g_cover_order_radius"),
        (assign, reg1,"$g_cover_order_radius"),
        (val_div,reg1,100),
        (try_begin),
          (eq, "$g_class_listening", grc_everyone),
          (display_message,"@Everyone take cover within {reg1}m!",message_alert),
        (else_try),
          (str_store_class_name, s1, "$g_class_listening"),
          (display_message,"@{s1} take cover within {reg1}m!",message_alert),
        (try_end),
      (else_try),
        (eq, "$gk_order", key_f7),	#Leave cover
        (assign, "$gk_order", 0),
        (call_script, "script_cover_ai_end","$g_player_team"),
        (try_begin),
          (eq, "$g_class_listening", grc_everyone),
          (display_message,"@Everyone, leave cover!",message_alert),
        (else_try),
          (str_store_class_name, s1, "$g_class_listening"),
          (display_message,"@{s1}, leave cover!",message_alert),
        (try_end),
        (try_begin),
			(eq, "$g_autocover", 1),
			(display_message,"@AutoCover disabled as you told your forces to leave cover.",message_alert),
			(assign, "$g_autocover", 0),
        (try_end),
      (else_try),
        (eq, "$gk_order", key_f8),	#AutoCover on
        (assign, "$gk_order", 0),
        (display_message,"@AutoCover enabled! (set distance with F5)",message_alert),
		(assign, "$g_autocover", 1),
      (try_end),
  ]),

  # Trigger file: extended_battle_menu_F5
  (0, 0, 0, [
      (game_key_clicked, gk_order_5),
      #(neg|main_hero_fallen)
      ], [
      (try_begin),
        (eq, "$gk_order", 0),
        (try_begin),
          # (eq, "$FormAI_off", 0),
          (assign, "$gk_order", gk_order_5),
          (try_begin),
            (is_presentation_active, "prsnt_battle"),
            (assign, "$g_presentation_active", 1),
          (try_end),
          (presentation_set_duration, 0),
          (assign, "$switch_presentation_new", "prsnt_order_display"),

          # (store_and, reg0, "$g_first_time", first_time_formations),
          (store_and, reg0, "$g_first_time", first_time_mod_orders),
          (try_begin),
            (eq, reg0, 0),
            # (val_or, "$g_first_time", first_time_formations),
            (val_or, "$g_first_time", first_time_mod_orders),
            # (eq, "$g_is_quick_battle", 0),
            (dialog_box,"@With the Special Orders you have the possibility to let your troops search for cover. The options are short distance (25m) or longer (50m). Select Leave Cover to have the troops leave the covers and return to the normal position. Like all commands, only the troops currently listening will follow the commands.", "@Special Orders"),
          (try_end),

        (else_try),
          # (display_message, "@Formations turned OFF in options menu"),
          (eq, "$native_opening_menu", 1),
          (try_begin),
            (is_presentation_active, "prsnt_battle"),
            (assign, "$g_presentation_active", 1),
          (try_end),
          (presentation_set_duration, 0),
          (assign, "$switch_presentation_new", "prsnt_order_display"),
        (try_end),
      (else_try),
        (eq, "$gk_order", gk_order_1),	#RETREAT
        (assign, "$gk_order", 0),
        # (call_script, "script_player_order_formations", mordr_retreat),
      (else_try),
        (eq, "$gk_order", gk_order_2),	#MOUNT
        (assign, "$gk_order", 0),
        (presentation_set_duration, 0),	#clear F2 menu additions
      (else_try),
        (eq, "$gk_order", gk_order_5),	#COMMAND RADIUS
        (assign, "$gk_order", 0),
        (assign, "$g_cover_order_radius", 2500),
      (else_try),
        (eq, "$gk_order", gk_order_6),	#Search Cover around marker
        (assign, "$gk_order", 0),
        (scene_prop_get_num_instances, ":total", "spr_cover_marker"),
        (try_begin),
          (gt, ":total",0),
          (try_for_range,":cur_instance",0,":total"),
            (scene_prop_get_instance, ":instance_id", "spr_cover_marker", ":cur_instance"),
            (prop_instance_get_position, pos1, ":instance_id"),
          (try_end),
          (call_script, "script_cover_search_player", pos1, "$g_cover_order_radius"),

          (assign, reg1,"$g_cover_order_radius"),
          (val_div,reg1,100),
          (try_begin),
            (eq, "$g_class_listening", grc_everyone),
            (display_message,"@Everyone take cover within {reg1}m around Battlezone!",message_alert),
          (else_try),
            (str_store_class_name, s1, "$g_class_listening"),
            (display_message,"@{s1} take cover within {reg1}m around Battlezone!",message_alert),
          (try_end),
        (else_try),
          (display_message,"@No Cover Position Marker set!",message_alert),
        (try_end),
      (else_try),
        (eq, "$gk_order", key_f7),	#Leave Cover less than x m from commander
        (assign, "$gk_order", 0),
        (agent_get_position,pos1,"$g_player"),
        (try_for_agents,":agent_id"),
          (agent_slot_ge, ":agent_id", slot_agent_take_cover, 0),
          (agent_is_alive,":agent_id"),
          (agent_is_human,":agent_id"),
          (agent_get_team  ,":agent_team", ":agent_id"),
          (eq,":agent_team","$g_player_team"),
          (agent_get_class,":class", ":agent_id"),
          (this_or_next|eq,":class","$g_class_listening"), #class or all
          (eq,"$g_class_listening",grc_everyone),

          (agent_get_slot, ":instance_id", ":agent_id", slot_agent_prop_occupied),
          (prop_instance_get_position, pos2, ":instance_id"),
          (get_distance_between_positions, ":dist", pos1, pos2), #distance player agent, choosen prop
          (lt, ":dist", "$g_cover_order_radius"),

          (agent_clear_scripted_mode,":agent_id"),
          (agent_set_animation, ":agent_id", "anim_cover_crouch_to_stand"),
          # (agent_set_speed_modifier, ":agent_id", 100),
          (agent_get_slot, ":speed_mod", ":agent_id", slot_agent_speed_mod),
          (agent_set_speed_modifier, ":agent_id", ":speed_mod"),

          # (agent_get_slot, ":instance_id", ":agent_id", slot_agent_prop_occupied),
          (scene_prop_set_slot,":instance_id",scene_prop_cover_occupied,0),
          (agent_set_slot, ":agent_id", slot_agent_prop_occupied, -1),
          (agent_set_slot,":agent_id",slot_agent_take_cover,-1),
        (try_end),
        (assign, reg1,"$g_cover_order_radius"),
        (val_div,reg1,100),
        (try_begin),
          (eq, "$g_class_listening", grc_everyone),
          (display_message,"@Everyone, leave cover less {reg1}m from my position!",message_alert),
        (else_try),
          (str_store_class_name, s1, "$g_class_listening"),
          (display_message,"@{s1}, leave cover less {reg1}m from my position!",message_alert),
        (try_end),
      (else_try),
        (eq, "$gk_order", key_f8),	#AutoCover off
        (assign, "$gk_order", 0),
        (display_message,"@AutoCover disabled!",message_alert),
		(assign, "$g_autocover", 0),
      (try_end),
  ]),

  # Trigger file: extended_battle_menu_F6
  (0, 0, 0, [
      (game_key_clicked, gk_order_6),
      #(neg|main_hero_fallen)
      ], [
      (try_begin),
        (eq, "$gk_order", 0),
        (try_begin),
          (assign, "$gk_order", gk_order_6),
          (try_begin),
            (is_presentation_active, "prsnt_battle"),
            (assign, "$g_presentation_active", 1),
          (try_end),
          (presentation_set_duration, 0),
          (assign, "$switch_presentation_new", "prsnt_order_display"),

          # (store_and, reg0, "$g_first_time", first_time_formations),
          (store_and, reg0, "$g_first_time", first_time_mod_orders),
          (try_begin),
            (eq, reg0, 0),
            # (val_or, "$g_first_time", first_time_formations),
            (val_or, "$g_first_time", first_time_mod_orders),
            # (eq, "$g_is_quick_battle", 0),
            (dialog_box,"@With the Special Orders you have the possibility to let your troops search for cover. The options are short distance (25m) or longer (50m). Select Leave Cover to have the troops leave the covers and return to the normal position. Like all commands, only the troops currently listening will follow the commands.", "@Special Orders"),
          (try_end),

        (else_try),

          (eq, "$native_opening_menu", 1),
          (try_begin),
            (is_presentation_active, "prsnt_battle"),
            (assign, "$g_presentation_active", 1),
          (try_end),
          (presentation_set_duration, 0),
          (assign, "$switch_presentation_new", "prsnt_order_display"),
        (try_end),
      (else_try),
        (eq, "$gk_order", gk_order_2),	#DISMOUNT
        (assign, "$gk_order", 0),
        (presentation_set_duration, 0),	#clear F2 menu additions
      (else_try),
        (eq, "$gk_order", gk_order_5),	#COMMAND RADIUS
        (assign, "$gk_order", 0),
        (assign, "$g_cover_order_radius", 5000),
      (else_try),
        (eq, "$gk_order", gk_order_6),	#END
        (assign, "$gk_order", 0),
        (presentation_set_duration, 0),
      (else_try),
        (eq, "$gk_order", key_f7),	#Leave Cover more than x m from commander
        (assign, "$gk_order", 0),
        (agent_get_position,pos1,"$g_player"),
        (try_for_agents,":agent_id"),
          (agent_slot_ge, ":agent_id", slot_agent_take_cover, 0),
          (agent_is_alive,":agent_id"),
          (agent_is_human,":agent_id"),
          (agent_get_team  ,":agent_team", ":agent_id"),
          (eq,":agent_team","$g_player_team"),
          (agent_get_class,":class", ":agent_id"),
          (this_or_next|eq,":class","$g_class_listening"), #class or all
          (eq,"$g_class_listening",grc_everyone),

          (agent_get_slot, ":instance_id", ":agent_id", slot_agent_prop_occupied),
          (prop_instance_get_position, pos2, ":instance_id"),
          (get_distance_between_positions, ":dist", pos1, pos2), #distance player agent, choosen prop
          (gt, ":dist", "$g_cover_order_radius"),

          (agent_clear_scripted_mode,":agent_id"),
          (agent_set_animation, ":agent_id", "anim_cover_crouch_to_stand"),
          # (agent_set_speed_modifier, ":agent_id", 100),
          (agent_get_slot, ":speed_mod", ":agent_id", slot_agent_speed_mod),
          (agent_set_speed_modifier, ":agent_id", ":speed_mod"),

          # (agent_get_slot, ":instance_id", ":agent_id", slot_agent_prop_occupied),
          (scene_prop_set_slot,":instance_id",scene_prop_cover_occupied,0),
          (agent_set_slot, ":agent_id", slot_agent_prop_occupied, -1),
          (agent_set_slot,":agent_id",slot_agent_take_cover,-1),
        (try_end),
        (assign, reg1,"$g_cover_order_radius"),
        (val_div,reg1,100),
        (try_begin),
          (eq, "$g_class_listening", grc_everyone),
          (display_message,"@Everyone, leave cover more than {reg1}m from my position!",message_alert),
        (else_try),
          (str_store_class_name, s1, "$g_class_listening"),
          (display_message,"@{s1}, leave cover more than {reg1}m from my position!",message_alert),
        (try_end),
      (else_try),
        (eq, "$gk_order", key_f8),	#END
        (assign, "$gk_order", 0),
        (presentation_set_duration, 0),
      (try_end),
  ]),

  # Trigger file: extended_battle_menu_F7
  (0, 0, 0, [
      (key_clicked, key_f7),
     #(neg|main_hero_fallen)
      ], [
      (try_begin),
        (eq, "$gk_order", 0),
        (try_begin),
          # (eq, "$FormAI_off", 0),
          (assign, "$gk_order", key_f7),
          (try_begin),
            (is_presentation_active, "prsnt_battle"),
            (assign, "$g_presentation_active", 1),
          (try_end),
          (presentation_set_duration, 0),
          (assign, "$switch_presentation_new", "prsnt_order_display"),

          # (store_and, reg0, "$g_first_time", first_time_formations),
          (store_and, reg0, "$g_first_time", first_time_mod_orders),
          (try_begin),
            (eq, reg0, 0),
            # (val_or, "$g_first_time", first_time_formations),
            (val_or, "$g_first_time", first_time_mod_orders),
            # (eq, "$g_is_quick_battle", 0),
            (dialog_box,"@With the Special Orders you have the possibility to let your troops search for cover. The options are short distance (25m) or longer (50m). Select Leave Cover to have the troops leave the covers and return to the normal position. Like all commands, only the troops currently listening will follow the commands.", "@Special Orders"),
          (try_end),

        (else_try),
          # (display_message, "@Formations turned OFF in options menu"),
          (eq, "$native_opening_menu", 1),
          (try_begin),
            (is_presentation_active, "prsnt_battle"),
            (assign, "$g_presentation_active", 1),
          (try_end),
          (presentation_set_duration, 0),
          (assign, "$switch_presentation_new", "prsnt_order_display"),
        (try_end),
      (else_try),

        (eq, "$gk_order", gk_order_5),	#COMMAND RADIUS
        (assign, "$gk_order", 0),
        (assign, "$g_cover_order_radius", 10000),
      (else_try),
        (eq, "$gk_order", key_f7),	#Leave Cover less than x m from cover marker
        (assign, "$gk_order", 0),
        (scene_prop_get_num_instances, ":total", "spr_cover_marker"),
        (try_begin),
          (gt, ":total",0),
          (try_for_range,":cur_instance",0,":total"),
            (scene_prop_get_instance, ":instance_id", "spr_cover_marker", ":cur_instance"),
            (prop_instance_get_position, pos1, ":instance_id"),
          (try_end),

          (try_for_agents,":agent_id"),
            (agent_slot_ge, ":agent_id", slot_agent_take_cover, 0),
            (agent_is_alive,":agent_id"),
            (agent_is_human,":agent_id"),
            (agent_get_team  ,":agent_team", ":agent_id"),
            (eq,":agent_team","$g_player_team"),
            (agent_get_class,":class", ":agent_id"),
            (this_or_next|eq,":class","$g_class_listening"), #class or all
            (eq,"$g_class_listening",grc_everyone),

            (agent_get_slot, ":instance_id", ":agent_id", slot_agent_prop_occupied),
            (prop_instance_get_position, pos2, ":instance_id"),
            (get_distance_between_positions, ":dist", pos1, pos2), #distance player agent, choosen prop
            (lt, ":dist", "$g_cover_order_radius"),

            (agent_clear_scripted_mode,":agent_id"),
            (agent_set_animation, ":agent_id", "anim_cover_crouch_to_stand"),
            # (agent_set_speed_modifier, ":agent_id", 100),
            (agent_get_slot, ":speed_mod", ":agent_id", slot_agent_speed_mod),
            (agent_set_speed_modifier, ":agent_id", ":speed_mod"),

            # (agent_get_slot, ":instance_id", ":agent_id", slot_agent_prop_occupied),
            (scene_prop_set_slot,":instance_id",scene_prop_cover_occupied,0),
            (agent_set_slot, ":agent_id", slot_agent_prop_occupied, -1),
            (agent_set_slot,":agent_id",slot_agent_take_cover,-1),
          (try_end),
          (assign, reg1,"$g_cover_order_radius"),
          (val_div,reg1,100),
          (try_begin),
            (eq, "$g_class_listening", grc_everyone),
            (display_message,"@Everyone, leave cover {reg1}m  within Battlezone Marker!",message_alert),
          (else_try),
            (str_store_class_name, s1, "$g_class_listening"),
            (display_message,"@{s1}, leave cover {reg1}m within Battlezone Marker!",message_alert),
          (try_end),
        (else_try),
          (display_message,"@No Cover Position Marker set!", message_alert),
        (try_end),
      (try_end),
  ]),

  # Trigger file: extended_battle_menu_F8
  (0, 0, 0, [
      (key_clicked, key_f8),
      #(neg|main_hero_fallen)
      ], [

      (try_begin),
        (eq, "$gk_order", 0),
        (try_begin),
          # (eq, "$FormAI_off", 0),
          (assign, "$gk_order", key_f8),
          (try_begin),
            (is_presentation_active, "prsnt_battle"),
            (assign, "$g_presentation_active", 1),
          (try_end),
          (presentation_set_duration, 0),
          (assign, "$switch_presentation_new", "prsnt_order_display"),

          # (store_and, reg0, "$g_first_time", first_time_formations),
          (store_and, reg0, "$g_first_time", first_time_mod_orders),
          (try_begin),
            (eq, reg0, 0),
            # (val_or, "$g_first_time", first_time_formations),
            (val_or, "$g_first_time", first_time_mod_orders),
            # (eq, "$g_is_quick_battle", 0),
            (dialog_box,"@With the Special Orders you have the possibility to let your troops search for cover. The options are short distance (25m) or longer (50m). Select Leave Cover to have the troops leave the covers and return to the normal position. Like all commands, only the troops currently listening will follow the commands.", "@Special Orders"),
          (try_end),

        (else_try),
          # (display_message, "@Formations turned OFF in options menu"),
          (eq, "$native_opening_menu", 1),
          (try_begin),
            (is_presentation_active, "prsnt_battle"),
            (assign, "$g_presentation_active", 1),
          (try_end),
          (presentation_set_duration, 0),
          (assign, "$switch_presentation_new", "prsnt_order_display"),
        (try_end),
      (else_try),
        (eq, "$gk_order", gk_order_5),	#COMMAND RADIUS
        (assign, "$gk_order", 0),
        (assign, "$g_cover_order_radius", 20000),
      (else_try),
        (eq, "$gk_order", key_f7),	#Leave Cover more than x m from cover marker
        (assign, "$gk_order", 0),
        (scene_prop_get_num_instances, ":total", "spr_cover_marker"),
        (try_begin),
          (gt, ":total",0),
          (try_for_range,":cur_instance",0,":total"),
            (scene_prop_get_instance, ":instance_id", "spr_cover_marker", ":cur_instance"),
            (prop_instance_get_position, pos1, ":instance_id"),
          (try_end),

          (try_for_agents,":agent_id"),
            (agent_slot_ge, ":agent_id", slot_agent_take_cover, 0),
            (agent_is_alive,":agent_id"),
            (agent_is_human,":agent_id"),
            (agent_get_team  ,":agent_team", ":agent_id"),
            (eq,":agent_team","$g_player_team"),
            (agent_get_class,":class", ":agent_id"),
            (this_or_next|eq,":class","$g_class_listening"), #class or all
            (eq,"$g_class_listening",grc_everyone),

            (agent_get_slot, ":instance_id", ":agent_id", slot_agent_prop_occupied),
            (prop_instance_get_position, pos2, ":instance_id"),
            (get_distance_between_positions, ":dist", pos1, pos2), #distance player agent, choosen prop
            (gt, ":dist", "$g_cover_order_radius"),

            (agent_clear_scripted_mode,":agent_id"),
            (agent_set_animation, ":agent_id", "anim_cover_crouch_to_stand"),
            # (agent_set_speed_modifier, ":agent_id", 100),
            (agent_get_slot, ":speed_mod", ":agent_id", slot_agent_speed_mod),
            (agent_set_speed_modifier, ":agent_id", ":speed_mod"),

            # (agent_get_slot, ":instance_id", ":agent_id", slot_agent_prop_occupied),
            (scene_prop_set_slot,":instance_id",scene_prop_cover_occupied,0),
            (agent_set_slot, ":agent_id", slot_agent_prop_occupied, -1),
            (agent_set_slot,":agent_id",slot_agent_take_cover,-1),
          (try_end),
          (assign, reg1,"$g_cover_order_radius"),
          (val_div,reg1,100),
          (try_begin),
            (eq, "$g_class_listening", grc_everyone),
            (display_message,"@Everyone, leave cover more than {reg1}m from Battlezone Marker!",message_alert),
          (else_try),
            (str_store_class_name, s1, "$g_class_listening"),
            (display_message,"@{s1}, leave cover more than {reg1}m from Battlezone Marker!",message_alert),
          (try_end),
        (else_try),
          (display_message,"@No Cover Position Marker set!", message_alert),
        (try_end),
      (try_end),
  ]),

  # Trigger file: extended_battle_menu_F9
  (0, 0, 0, [
      (key_clicked, key_f9),
      #(neg|main_hero_fallen)
      ], [

      (try_begin),
        (eq, "$gk_order", 0),	#Redisplay
        (eq, "$native_opening_menu", 1),
        (try_begin),
          (is_presentation_active, "prsnt_battle"),
          (assign, "$g_presentation_active", 1),
        (try_end),
        (presentation_set_duration, 0),
        (assign, "$switch_presentation_new", "prsnt_order_display"),
      (else_try),
        (eq, "$gk_order", gk_order_5),	#END
        (assign, "$gk_order", 0),
        (presentation_set_duration, 0),
      (else_try),
        (eq, "$gk_order", key_f7),	#END
        (assign, "$gk_order", 0),
        (presentation_set_duration, 0),
      (try_end),
  ]),

  # Trigger file: extended_battle_menu_restore_prsnt_battle
  (0.7, 0, 0, [
      (eq, "$g_presentation_active", 1),
      (neg|is_presentation_active, "prsnt_order_display"),
      (eq, "$gk_order", 0),
      ],[
      (presentation_set_duration, 0),
      (assign, "$switch_presentation_new", "prsnt_battle"),
      (assign, "$g_presentation_active", 0),
  ]),
]#end extended battle menu

########################################################
## tocan common triggers
########################################################
tocan_common_triggers = [ #tocan: all missions
    (ti_before_mission_start, 0, 0, [], [	#1
        (stop_sound_channel, "$ambient_sound_channel"),
        (stop_all_sounds, 0),

        (call_script, "script_cf_mod_replace_objects"),
        (assign, "$g_player_heartbeat",0),
        (assign, "$g_animal_present", 0),
        (assign, "$g_new_animal", 0),
        (assign, "$g_spitter_active",0),
        (assign, "$guns_not_load_until", -1),
        (assign, "$guns_cant_fire_until", -1),
        (call_script, "script_init_firearms",0),
        (assign, "$cam_mode", 0),
        (assign, "$flashbang_thrown", 0),
        (assign, "$smokeg_thrown", 0),
        (assign, "$agent_on_fire", 0),

        (try_begin),
          (store_current_scene, ":cur_scene"),
          (this_or_next|is_between, ":cur_scene", rs_plain_begin,rs_scenes_end),
          (this_or_next|eq, ":cur_scene", "scn_battle_field_1b"),
          # (this_or_next|eq, ":cur_scene", "scn_test_city"),
          (eq, ":cur_scene", "scn_battle_field_2"),

          (assign,"$g_covers_active",1),
        (try_end),

		(assign, "$player_fallen_so_allies_seek_cover", 0),
		(assign, "$g_autocover_ai", 1),
        ]),

    # (ti_on_agent_blocked, 0, 0, [	#for testing number of pellets that can hit a single agent in 1 shot
	# #(neg|is_vanilla_warband),
	# ], [
        # # Trigger Param 1: receiver agent no
		# # Trigger Param 2: dealer agent no
		# # Trigger Param 3: item kind no
		# # Trigger Param 4: missile item kind no
		# # (store_trigger_param_1, ":receiver"),
      # # (store_trigger_param_2, ":dealer"),
      # # (store_trigger_param_3, ":item"),
      # #(store_trigger_param, ":missile", 4),
		# #(this_or_next|eq, ":missile", "itm_buckshot_ammo"),
       # # (eq, ":missile", "itm_buckshot_ammo_pw"),
		# (display_message, "@buckhot blocked"),
        # ]),

    (ti_after_mission_start, 0, ti_once, [], [	#2
        (set_fixed_point_multiplier, 100),

        (get_player_agent_no, "$g_player"),
        (try_begin),
            (lt, "$g_player", 0),
            (assign, "$g_player_team", -1),
        (else_try),
            (agent_get_group, "$g_player_team", "$g_player"),
        (try_end),

        (try_begin),
            # (eq,"$wounds_off",0), #optional
            (this_or_next|ge,"$g_player_tigh_wound",1),
            (this_or_next|ge,"$g_player_calf_wound",1),
            (this_or_next|ge,"$g_player_foot_wound",1),
            (this_or_next|ge,"$g_player_spine_wound",1),
            (this_or_next|ge,"$g_player_thorax_wound",1),
            (this_or_next|ge,"$g_player_head_wound",1),
            (this_or_next|ge,"$g_player_shoulder_wound",1),
            (this_or_next|ge,"$g_player_arm_wound",1),
            (ge,"$g_player_hand_wound",1),

            (call_script,"script_tocan_wounds","$g_player",0,2),
        (try_end),

        (agent_set_slot, "$g_player", slot_agent_last_roll, 0),

        # # (get_scene_boundaries, pos2, pos3),
        # # (position_get_x, "$t_map_right", pos3),
        # # (position_get_y, "$t_map_top", pos3),
        # # (position_get_x, "$t_map_left", pos2),
        # # (position_get_y, "$t_map_bottom", pos2),
        (get_scene_boundaries, pos10, pos11),
        # (position_get_x, "$g_scene_min_x", pos10),
        # (position_get_y, "$g_scene_min_y", pos10),
        (position_get_x, "$g_scene_max_x", pos11),
        # (position_get_y, "$g_scene_max_y", pos11),
        (val_add, "$g_scene_max_x", 2400),#2400 has been subtracted automatically
		#(assign, reg45, "$g_scene_max_x"),
		#(assign, ":pos_dist", "$g_scene_max_x"),
		#(position_get_x, reg46, pos10),
		#(display_message, "@g_scene_max_x: {reg45}, other: {reg46}"),
        # (val_add, "$g_scene_max_y", 2400),

        (store_current_scene, ":cur_scene"),
        (try_begin),
            # (this_or_next|eq,  ":cur_scene", "scn_battlehangar_scifi"),
            # (this_or_next|eq,  ":cur_scene", "scn_battlehangar_concrete"),
            (is_between, ":cur_scene", rs_plain_begin,rs_scenes_end),

            (store_div, ":pos_x", "$g_scene_max_x", 2),
            (store_div, ":pos_y", "$g_scene_max_x", 2),

            (init_position, pos22),
            (position_set_x, pos22, ":pos_x"),
            (position_set_y, pos22, ":pos_y"),

            (set_spawn_position, pos22),
            (spawn_scene_prop, "spr_tocan_scene_maker"),

            (rebuild_shadow_map),
        (try_end),

        # (store_normalized_team_count,":num_defenders",0),
        # (party_get_num_companions, ":count", "$g_encountered_party"),
        # (try_begin),
          # (le,":count",51),
          # (entry_point_get_position,pos1, 4),
          # (position_move_y,pos1,100000),
          # (entry_point_set_position,4,pos1),
        # (try_end),

        (mission_cam_set_screen_color, 0xFF008000), #roughly the colour of the menu bg
        (mission_cam_animate_to_screen_color, 0x00008000, 1500),
        ]),

    (ti_on_agent_spawn, 0, 0, [], [	#3
        (store_trigger_param_1, ":agent_id"),

        (agent_set_slot, ":agent_id", slot_agent_take_cover, -1),
        (agent_set_slot, ":agent_id", slot_agent_prop_occupied, -1),
        (agent_set_slot, ":agent_id", slot_agent_rides_x,-1),
        (agent_set_slot, ":agent_id", slot_agent_horse_prop,-1),
        # (agent_set_slot, ":agent_id", slot_agent_rides_animal,-1),
        (agent_set_slot, ":agent_id", slot_agent_is_animal,-1),

        (get_player_agent_no, "$g_player"),

        (agent_get_troop_id, ":troop_id", ":agent_id"),
        (neq, ":troop_id", "trp_dog_companion"),
        (neq, ":troop_id", "trp_bot_companion"),

        (try_begin),
          (agent_is_human, ":agent_id"),

          (try_begin),
            (eq,":troop_id","trp_spitter"),
            (assign,"$g_spitter_active",1),
          (else_try),
            (troop_slot_eq, ":troop_id", slot_troop_is_animal, 1),

            # (this_or_next|eq,":troop_id","trp_mech_spider"),
            # (this_or_next|eq,":troop_id","trp_mutant_spider"),
            # (this_or_next|eq,":troop_id","trp_mutant_spider_big"),
            # (this_or_next|eq,":troop_id","trp_infected_doberman"),
            # (this_or_next|eq,":troop_id","trp_infected_dog"),
            # (this_or_next|eq,":troop_id","trp_rabid_doberman"),
            # (eq,":troop_id","trp_rabid_dog"),

            (assign,"$g_animal_present",1),
            (assign, "$g_new_animal", 1),
          (try_end),
          (neg|troop_slot_eq, ":troop_id", slot_troop_is_animal, 1),

          (store_proficiency_level, ":firing_skill", ":troop_id", wpt_firearm),
          (agent_set_slot, ":agent_id", slot_agent_firearm_skill,":firing_skill"),

          (agent_get_accuracy_modifier, ":accuracy_modifier", ":agent_id"),
          (agent_get_damage_modifier, ":damage_modifier", ":agent_id"),
          (agent_get_speed_modifier, ":speed_modifier", ":agent_id"),
          (agent_get_reload_speed_modifier, ":reload_speed_modifier", ":agent_id"),
          # (assign,":ranged_damage_modifier",100),
          # (assign,":aggro_modifier",100),

          # (assign,":battle_effectivness",0),
          # (assign,":ranged_effectivness",0),
          # (assign,":hp_bonus",0),

          # (store_troop_faction, ":faction", ":troop_id"),

          # (store_skill_level, ":skl_leadership",  "skl_leadership", ":troop_id"),
          # (val_add, ":battle_effectivness", ":skl_leadership"),
          # (store_skill_level, ":skl_spotting",  "skl_spotting", ":troop_id"),
          # (val_add, ":ranged_effectivness", ":skl_spotting"),
          # (store_skill_level, ":skl_tactics",  "skl_tactics", ":troop_id"),
          # (val_add, ":battle_effectivness", ":skl_tactics"),
          # (store_skill_level, ":skl_power_strike",  "skl_power_strike", ":troop_id"),
          # (val_add, ":health", ":skl_power_strike"),
          # (store_skill_level, ":skl_ironflesh",  "skl_ironflesh", ":troop_id"),
          # (val_add, ":health", ":skl_ironflesh"),
          # (store_skill_level, ":skl_tracking",  "skl_tracking", ":troop_id"),
          # (val_add, ":health", ":skl_tracking"),
          # (store_skill_level, ":skl_trainer",  "skl_trainer", ":troop_id"),
          # (val_add, ":battle_effectivness", ":skl_trainer"),
          # (store_skill_level, ":skl_horse_archery",  "skl_horse_archery", ":troop_id"),
          # (val_add, ":ranged_effectivness", ":skl_horse_archery"),

          # (try_begin),
              # (eq, ":faction", "fac_infected"),
              # (val_mul, ":health", 5), #double hp
          # (else_try),
              # (eq, ":faction", "fac_mutants"),
              # (val_mul, ":health", 4), #double hp
          # (else_try),
              # (val_mul, ":health", 2), #double hp
          # (try_end),

          (try_begin), #no player
            (agent_is_non_player, ":agent_id"),

            (agent_ai_set_can_crouch, ":agent_id", 0),  #no crouch

            # (val_add, ":aggro_modifier", ":battle_effectivness"),
            # (agent_ai_set_aggressiveness, ":agent_id", ":aggro_modifier"),

            (try_begin), #night penalty
                # (store_time_of_day, ":day_time"),
                # (neg|is_between, ":day_time", 5, 21),
				(this_or_next|eq,"$g_rad_zone",1),
				(this_or_next|eq,"$g_sandstorm",1),
                (is_currently_night),
                (val_div, ":accuracy_modifier", 4),
                (val_mul, ":accuracy_modifier", 3),
            (try_end),
            (try_begin),
              (party_get_current_terrain, ":terrain", "p_main_party"),
              (this_or_next|eq, ":terrain", rt_steppe_forest),
              (eq, ":terrain", rt_forest),
              (val_div, ":accuracy_modifier", 10),
              (val_mul, ":accuracy_modifier", 9),
            (try_end),

            (assign,":has_shield",0),
            (try_for_range, ":item_slot", ek_item_0, ek_horse),
              (neq,":has_shield",1),
              (agent_get_item_slot, ":item_no", ":agent_id", ":item_slot"),
              (gt, ":item_no", -1),

              (item_get_type, ":item_type", ":item_no"),
              (eq, ":item_type", itp_type_shield),

              (assign,":has_shield",1),
            (try_end),

            (try_for_range, ":item_slot", ek_item_0, ek_horse),
              (agent_get_item_slot, ":item_no", ":agent_id", ":item_slot"),
              (gt, ":item_no", -1),

              (item_get_type, ":item_type", ":item_no"),
			  (this_or_next|is_between, ":item_no", grenades_begin, grenades_end),
              (this_or_next|eq, ":item_type", itp_type_bow),
              #(this_or_next|eq, ":item_type", itp_type_crossbow),
              (this_or_next|eq, ":item_type", itp_type_pistol),
              (eq, ":item_type", itp_type_musket),

              (agent_set_slot, ":agent_id", slot_agent_has_ranged, 1),

              (try_begin),
                # # (troop_is_hero,":troop_id"),
                (assign,":new_item",":item_no"),
                (is_between, ":new_item", firearms_begin,firearms_end),

                (agent_unequip_item, ":agent_id", ":new_item", ":item_slot"),

                (try_begin), #if no shield and a pistol use 2hander gun animation
                    (neq,":has_shield",1),
                    (eq,":item_type",itp_type_pistol),
                    (val_sub, ":new_item", firearms_begin),
                    (val_add, ":new_item", ai_ranged_weapons_begin_2h),
                (else_try),
                    (val_sub, ":new_item", firearms_begin),
                    (val_add, ":new_item", ai_ranged_weapons_begin),

                    # (try_begin),
                        # (gt, ":item_no", "itm_rifle_arisaka_b"),	#offset for arisaka bayonet - krag
                        # (val_sub, ":new_item",1),
                    # (try_end),
                (try_end),

            #   # (str_store_item_name, s33, ":item_no"),
            #   # (str_store_item_name, s34, ":new_item"),
            #   # (display_message, "@old:{s33},  new: {s34}"),	#check conversion
			 # (str_store_item_id, s33, ":item_no"),	#wse
             # (str_store_item_id, s34, ":new_item"),	#wse
              #(display_message, "@old:{s33},  new: {s34}"),	#check conversion
                (agent_equip_item, ":agent_id", ":new_item", ":item_slot"),
				(try_begin),
					(neg|agent_is_alarmed,":agent_id"),
					(agent_set_wielded_item, ":agent_id", -1),	#guards were unholstering in towns for no reason - krag
				(try_end),
              (try_end),
            (try_end),

            # (try_begin),
                  # (neq,":has_shield",1),
                  # (eq,":item_type",itp_type_pistol),
				  # (str_store_item_id, s33, ":item_no"),
				  # (assign,":new_item",":item_no"),
                  # (val_sub, ":new_item", pistol_begin),
                  # (val_add, ":new_item", ai_ranged_weapons_begin_2h),
                  # (agent_unequip_item, ":agent_id", ":item_no", ":item_slot"),
                  # (agent_equip_item, ":agent_id", ":new_item", ":item_slot"),

					# (str_store_item_id, s34, ":new_item"),
					# (display_message, "@old:{s33},  new: {s34}"),	#check conversion
                # (try_end),
          (else_try), #player condition/stamina
            (neg|agent_is_non_player, ":agent_id"),

            (agent_set_slot, "$g_player", slot_agent_player_stamina, 100),

            # (store_attribute_level, ":player_agility", "trp_player", ca_agility),
            # (val_mul,":player_agility",100),
            (store_skill_level, ":player_athletics", skl_athletics, "trp_player"),
            (val_mul,":player_athletics",10),

            # (store_add,":total",":player_agility",":player_athletics"),
            (assign, ":weight", 0),
            (try_for_range, ":item_slot", ek_item_0, ek_horse),
                (agent_get_item_slot, ":item_no", "$g_player", ":item_slot"),
                (gt, ":item_no", -1),
                (item_get_weight, ":item_weight", ":item_no"),
                (val_add,":weight",":item_weight"),
            (try_end),

            # (try_begin),
                # # (ge,":weight",1),
                # (assign,reg20,":weight"),
                # # (val_div,":total",":weight"),
                # (display_message,"@{reg20} weight"),
            # # (else_try),
                # # (assign,":weight",1),
            # (try_end),

            (assign, ":stamina_rate", 100),
            (try_begin),
                (ge,":weight",10000),
                (val_mul, ":stamina_rate", 2),
            (try_end),
            (val_sub,":stamina_rate", ":player_athletics"),
            (val_max,":stamina_rate", 10),

            # # (assign,reg17,":player_agility"),
            # (assign,reg18,":player_athletics"),
            (assign,reg19,":stamina_rate"),
            # # (display_message,"@{reg17} agi"),
            # (display_message,"@{reg18} ath"),
            # (display_message,"@{reg19} rate"),

            (assign,"$g_player_stamina_rate",reg19),

            (troop_get_slot, ":condition", "trp_player", slot_troop_condition),
            (troop_get_slot, ":bonus", "trp_player", slot_troop_food_bonus),

            (try_begin),
              (ge,":condition",75),
              (gt,":bonus",0),
              (val_div,":bonus",2),
              (val_clamp,":bonus",1,6),
              (val_add,":damage_modifier",":bonus"),
              (val_add,":accuracy_modifier",":bonus"),
              (assign,reg0,":bonus"),
              (display_message, "@Food Bonus: {reg0}", message_positive),
            (else_try),
              (le,":condition",10),
              (val_sub,":damage_modifier",10),
              (val_sub,":accuracy_modifier",10),
            (else_try),
              (le,":condition",20),
              (val_sub,":damage_modifier",5),
              (val_sub,":accuracy_modifier",5),
            (else_try),
              (le,":condition",30),
              (val_sub,":damage_modifier",3),
              (val_sub,":accuracy_modifier",3),
            (else_try),
              (le,":condition",40),
              (val_sub,":damage_modifier",1),
              (val_sub,":accuracy_modifier",1),
            (try_end),
            (assign, "$g_player_speed_mod", ":speed_modifier"),
            (assign, "$g_player_speed_mod_running", ":speed_modifier"),
            (val_add,"$g_player_speed_mod_running",50),
          (try_end),

          (agent_set_accuracy_modifier, ":agent_id", ":accuracy_modifier"),
          (agent_set_slot, ":agent_id", slot_agent_accuracy_mod,":accuracy_modifier"),

          (agent_set_damage_modifier, ":agent_id", ":damage_modifier"),

          (agent_set_speed_modifier, ":agent_id", ":speed_modifier"),
          (agent_set_slot, ":agent_id", slot_agent_speed_mod,":speed_modifier"),

          (agent_set_reload_speed_modifier, ":agent_id", ":reload_speed_modifier"),
          # (agent_set_ranged_damage_modifier, ":agent_id", ":ranged_damage_modifier"),

  #special behavior
          (try_begin),
              (eq, ":troop_id", "trp_undead_1"),
              (agent_set_speed_limit, ":agent_id", 5),
              (agent_set_walk_forward_animation, ":agent_id", "anim_zombie_walk"),
              (store_random_in_range, ":chance", 1, 3),
              (try_begin),
                (eq, ":chance", 1),
                (agent_play_sound, ":agent_id", "snd_infected_standard_1"),
              (else_try),
                (eq, ":chance", 2),
                (agent_play_sound, ":agent_id", "snd_infected_standard_2"),
              (try_end),
          (try_end),

          (try_begin),
              (eq, ":troop_id", "trp_f6_tier_6"),
			  (agent_equip_item, ":agent_id", "itm_grenade_molotov"),
            (else_try),
              (eq, ":troop_id", "trp_mercenary_grenadier"),
			  (agent_equip_item, ":agent_id", "itm_grenade"),
          (try_end),


        # (else_try),
          # (neg|agent_is_human, ":agent_id"),
        (try_end),


        ]),

    (ti_on_agent_hit, 0, 0, [], [	#4
      # Trigger Param 1: damage inflicted agent_id
      # Trigger Param 2: damage dealer agent_id
      # Trigger Param 3: inflicted damage
      # Trigger Param 4: hit bone
      # Trigger Param 5: missile item kind no
      # Register 0: damage dealer item_id
      # Position Register 0: position of the blow
      #                      rotation gives the direction of the blow
      # Trigger result: if returned result is greater than or equal to zero, inflicted damage is set to the value specified by the module.

      (set_fixed_point_multiplier, 100),
      (store_trigger_param_1, ":inflicted"),
      (store_trigger_param_2, ":dealer"),
      (store_trigger_param_3, ":damage"),
      (store_trigger_param, ":hitbone", 4),
      (store_trigger_param, ":ammo", 5),

      (agent_is_alive, ":inflicted"),
      (agent_is_human, ":inflicted"),
      (agent_is_human, ":dealer"),

	  (assign, ":attacker_weapon", reg0),
	  
	  # (assign, reg53, ":damage"),
	  # (str_store_agent_name, s53, ":inflicted"),
	  # (str_clear, s54),
	  # (set_show_messages, 0),
	  # (str_store_item_name, s54, ":attacker_weapon"),
	  # (str_store_item_name, s55, ":ammo"),
	  # (set_show_messages, 1),
	  # (display_message,"@{s53}'s damage: {reg53}, using: {s54}, ammo: {s55}.", message_alert),

	  (store_mission_timer_a, ":time"),
	  (try_begin),
		(is_between, ":attacker_weapon", sniper_ai_begin, sniper_ai_end),
		(val_add, ":time", 120),
	   (else_try),
		(gt, ":attacker_weapon", 0),
		(item_get_missile_speed, ":missile_speed", ":attacker_weapon"),
		(this_or_next|is_between, ":attacker_weapon", shotgun_ai_begin, shotgun_ai_end),	#ineffective at long range
		#(this_or_next|is_between, ":attacker_weapon", shotgun_begin, shotgun_end),
		(lt, ":missile_speed", 159),	#standard gun speed is 160
		(val_add, ":time", 15),
	   (else_try),
		(val_add, ":time", 60),	#was 120, but too slow after a lucky/early hit? eg against cav
	  (try_end),
	  (agent_set_slot, ":dealer", slot_agent_last_time_hit_enemy, ":time"),	#for leaving cover if not hit for a while


      (assign, ":attack_was_ranged", 0),
	  (try_begin),
        (this_or_next|eq, ":ammo", "itm_buckshot_ammo"), #vary buckshot damage by distance as many-pellet hits are blocked by the engine - krag
        (eq, ":ammo", "itm_buckshot_ammo_pw"),
		(agent_get_position, pos18, ":inflicted"),
		(agent_get_position, pos19, ":dealer"),
		(get_distance_between_positions, ":shot_distance", pos18, pos19),
		(try_begin),
			(gt, ":shot_distance", 4000),
			(val_div, ":damage", 2),
		  (else_try),
			(gt, ":shot_distance", 3000),
			(val_div, ":damage", 3),
			(val_mul, ":damage", 2),
		  (else_try),
			(lt, ":shot_distance", 100),
			(val_mul, ":damage", 6),
		  (else_try),
			(lt, ":shot_distance", 300),
			(val_mul, ":damage", 5),
		  (else_try),
			(lt, ":shot_distance", 500),
			(val_mul, ":damage", 4),
		  (else_try),
			(lt, ":shot_distance", 1000),
			(val_mul, ":damage", 3),
		  (else_try),
			(lt, ":shot_distance", 1500),
			(val_mul, ":damage", 2),
		(try_end),
	  (try_end),
      # (try_begin),
        # (eq, ":dealer", "$g_player"),
        # # (eq, ":inflicted", "$g_player"),
        # (call_script, "script_rnd", 0,64),
        # (eq,reg0,1),
        # (assign,":found",0),
        # (try_for_range, reg1, ek_item_0, ek_head),
          # (neq,":found",1),
          # (troop_get_inventory_slot, ":item_no", "trp_player", reg1),
          # (ge, ":item_no",0),
          # (eq, ":attacker_weapon",":item_no"),
          # (troop_get_inventory_slot_modifier, ":slot_item_imod", "trp_player", reg1),
          # (call_script, "script_get_next_lower_imod_for_item", ":item_no", ":slot_item_imod"),
          # (assign, ":new_imod", reg0),
          # (neq, ":slot_item_imod", ":new_imod"),
          # (troop_set_inventory_slot_modifier, "trp_player", reg1, ":new_imod"),
          # (str_store_item_name, s1, ":item_no"),
          # (display_message,"@Your {s1} shows signs of wear and tear!",message_alert),
          # (assign,":found",1),
        # (try_end),
      # (else_try),
        # (eq, ":inflicted", "$g_player"),
        # (call_script, "script_rnd", 0,64),
        # (eq,reg0,1),
        # (assign, reg1, ek_head),
        # (assign, reg2, ek_body),
        # (assign, reg3, ek_foot),
        # (assign, reg4, ek_gloves),
        # # (assign, reg5, ek_horse),
        # (shuffle_range, 1, 5),
        # (troop_get_inventory_slot, ":item_no", "trp_player", reg1),
        # (ge, ":item_no",0),
        # (troop_get_inventory_slot_modifier, ":slot_item_imod", "trp_player", reg1),
        # (call_script, "script_get_next_lower_imod_for_item", ":item_no", ":slot_item_imod"),
        # (assign, ":new_imod", reg0),
        # (neq, ":slot_item_imod", ":new_imod"),
        # (troop_set_inventory_slot_modifier, "trp_player", reg1, ":new_imod"),
        # (str_store_item_name, s1, ":item_no"),
        # (display_message,"@Your {s1} shows signs of wear and tear!",message_alert),
      # (try_end),

      (try_begin),
        (gt, ":attacker_weapon", 0),
        (item_get_type, ":item_type", ":attacker_weapon"),
        (this_or_next|eq, ":item_type", itp_type_bow),
        #(this_or_next|eq, ":item_type", itp_type_crossbow),
        (this_or_next|eq, ":item_type", itp_type_thrown),
        (this_or_next|eq, ":item_type", itp_type_pistol),
        (this_or_next|eq, ":item_type", itp_type_arrows),
        (this_or_next|eq, ":item_type", itp_type_bolts),
        (this_or_next|eq, ":item_type", itp_type_bullets),
        (eq, ":item_type", itp_type_musket),
        (assign, ":attack_was_ranged", 1),
      (try_end),
      
      (assign, ":animation", -1),
      (assign, ":ek_gloves", -1),

      (agent_get_troop_id, ":agent_troop_id", ":dealer"),
      (agent_get_troop_id, ":agent_troop_id_victim", ":inflicted"),
      (agent_get_horse, ":inflicted_mount",":inflicted"),
      (troop_get_type, ":inflicted_race", ":agent_troop_id_victim"),

      ##player only
      (try_begin),
        (this_or_next|eq,":inflicted","$g_player"),
        (eq,":dealer","$g_player"),
      ##player luck
        (assign,":lucky",0),
        (store_skill_level, ":player_luck", skl_luck, "trp_player"),
        (store_random_in_range,":chance",1,101),
        (ge,":player_luck",":chance"),
        (try_begin),
            (neg|agent_is_non_player, ":inflicted"),
            (assign,":lucky",1),
        (else_try),
            (assign,":xdamage",":damage"),
            (val_mul, ":xdamage", 200),
            (val_div, ":xdamage", 100),
            (val_add, ":damage", ":xdamage"),
        (try_end),
        (display_message,"str_luck",message_positive),
      (try_end),
      (neq,":lucky",1),

      ##damage without weapon
      (try_begin),
		#(eq, 1, 2), #testing
		(le, ":attacker_weapon", 0),
		
		(neq, ":inflicted", ":dealer"),
		
		(agent_get_wielded_item,":dealer_weapon",":dealer",0),
		(le, ":dealer_weapon", 0),	#stop grenades and other things causing unarmed damage - krag
		#(str_store_agent_name, s53, ":inflicted"),
		#(display_message, "@unarmed {s53}", message_positive),

        (store_attribute_level, ":ca_strength", ":agent_troop_id", ca_strength),
        (store_skill_level, ":skl_power_strike", "skl_power_strike", ":agent_troop_id"),
        (val_mul,":skl_power_strike",2),
        (store_skill_level, ":skl_shield", "skl_shield", ":agent_troop_id"),
        (store_skill_level, ":skl_ironflesh", "skl_ironflesh", ":agent_troop_id"),
        (store_add,":xdamage",":ca_strength",":skl_power_strike"),
        (val_add, ":xdamage", ":skl_shield"),
        (val_add, ":xdamage", ":skl_ironflesh"),
        (val_div, ":xdamage", 2),
        (val_add, ":damage", ":xdamage"),
        # (try_end),

        (troop_get_inventory_slot, ":ek_gloves", ":agent_troop_id", ek_gloves),
        (gt, ":ek_gloves", 0),

        (try_begin),
          (this_or_next|eq, ":ek_gloves", "itm_renfieldgauntlet"),
          (eq, ":ek_gloves", "itm_brassknuckles"),
          (val_add, ":damage", 15),
          (store_random_in_range,":chance",0,3),
          (try_begin),
              (eq,":chance",1),
              (assign,":fallback",1),
          (try_end),
        # (else_try),
          # (eq, ":ek_gloves", "itm_powerfist"),
          # (val_add, ":damage", 30),
          # (agent_play_sound, ":dealer", "snd_powerfist"),
          # (store_random_in_range,":chance",0,2),
          # (try_begin),
              # (eq,":chance",1),
              # (assign,":fallback",1),
          # (try_end),
        (try_end),
	   (else_try),
		(eq, ":inflicted", ":dealer"), #fall damage
		(troop_get_inventory_slot, ":foot_slot", ":agent_troop_id_victim", ek_foot),
		(eq, ":foot_slot", "itm_upgrade_exo"), #exoskeleton
		(val_div, ":damage", 2),
      (try_end),

      ##damage weapon craftable
      (try_begin),
        (gt, ":attacker_weapon", 0),
        (item_slot_ge, ":attacker_weapon", slot_item_crafting, 1),
		(this_or_next|eq, ":agent_troop_id", "trp_player"),	#don't add crafting bonus to enemies with same weapon - krag
		(is_between, ":agent_troop_id", companions_begin, companions_end),

        (assign, ":xdamage", 0),

        (store_skill_level, ":skl_crafting", skl_crafting, ":agent_troop_id"),
        (val_mul,":skl_crafting",5),
        (val_add,":skl_crafting",100),
        (assign,":xdamage",":damage"),
        (val_mul, ":xdamage", ":skl_crafting"),
        (val_div, ":xdamage", 100),
        (val_add, ":damage", ":xdamage"),

      (try_end),

      ##damage critical hit
      (try_begin),
        (try_begin),
          (gt, ":attacker_weapon", 0),
          (eq, ":attack_was_ranged", 1),

          (try_begin),
                  # (eq,"$g_player",":dealer"),
                  # (store_skill_level, ":skl_horse_archery", "skl_horse_archery", "trp_player"),
                # (else_try),
                    # (agent_get_troop_id, ":agent_troop_id", ":dealer"),
            (store_skill_level, ":skl_horse_archery", "skl_horse_archery", ":agent_troop_id"),
                # (try_end),
            (store_random_in_range,":chance",1,101),
            (ge,":skl_horse_archery",":chance"),

            (assign,":xdamage",":damage"),
            (val_mul, ":xdamage", 150),
            (val_div, ":xdamage", 100),
            (val_add, ":damage", ":xdamage"),
          (try_end),

          (try_begin), #bow
            (eq, ":item_type", itp_type_bow),
                # (try_begin),
                    # (eq,"$g_player",":dealer"),
                    # (store_skill_level, ":skl_power_draw", "skl_power_draw", "trp_player"),
                # (else_try),
                    # (agent_get_troop_id, ":agent_troop_id", ":dealer"),
            (store_skill_level, ":skl_power_draw", "skl_power_draw", ":agent_troop_id"),
                # (try_end),
            (store_random_in_range,":chance",1,101),
            (ge,":skl_power_draw",":chance"),

            (assign,":xdamage",":damage"),
            (val_mul, ":xdamage", 150),
            (val_div, ":xdamage", 100),
            (val_add, ":damage", ":xdamage"),
          (else_try), #thrown
            (eq, ":item_type", itp_type_thrown),

            (store_skill_level, ":skl_power_throw", "skl_power_throw", ":agent_troop_id"),

            (store_random_in_range,":chance",1,101),
            (ge,":skl_power_throw",":chance"),

            (assign,":xdamage",":damage"),
            (val_mul, ":xdamage", 150),
            (val_div, ":xdamage", 100),
            (val_add, ":damage", ":xdamage"),
        (try_end),
      (else_try), #warrior
        (gt, ":attacker_weapon", 0),

        (eq, ":attack_was_ranged", 0),

        (store_skill_level, ":skl_shield", "skl_shield", ":agent_troop_id"),
        (store_random_in_range,":chance",1,101),
        (ge,":skl_shield",":chance"),

        (assign,":xdamage",":damage"),
        (val_mul, ":xdamage", 150),
        (val_div, ":xdamage", 100),
        (val_add, ":damage", ":xdamage"),
      (try_end),

      ##damage from behind critical
      (try_begin),
        (this_or_next|eq, ":attack_was_ranged", 0), #only melee
        (eq, ":attacker_weapon", -1),
		(agent_get_wielded_item,":dealer_weapon",":dealer",0),
		(neg|is_between, ":dealer_weapon", grenades_begin, grenades_end),
        (agent_get_position, pos1, ":inflicted"),
        (agent_get_position, pos2, ":dealer"),
        (position_is_behind_position, pos2, pos1),
        (assign, ":xdamage", ":damage"),
        (val_div, ":xdamage", 2),
        (val_add, ":damage", ":xdamage"),
        (assign, reg1, ":xdamage"),
        (try_begin), #new animation
            (gt, ":damage", 50),
            # (agent_get_horse, ":inflicted_mount",":inflicted"),
            (le, ":inflicted_mount", -1),
            (store_random_in_range,":chance",0,5),
            (try_begin),
                (eq,":chance",1),
                (assign,":animation","anim_rider_fall_roll"),
            (else_try),
                (eq,":chance",2),
                (assign,":animation","anim_strike_fly_front_rise"),
            (try_end),
        (try_end),
        (try_begin),
            (neg|agent_is_non_player, ":dealer"),
            (display_message, "@Delivered extra damage from behind!", message_positive),
            # (display_message, "@Delivered {reg1} extra damage from behind!", 0x3AD54F),
        (else_try),
            (neg|agent_is_non_player, ":inflicted"),
            (display_message, "@Received extra damage from behind!", message_positive),
            # (display_message, "@Received {reg1} extra damage from behind!", 0xFF0000),
        (try_end),
      (try_end),

      ##aggromode
      # (try_begin), #aggro #this gives some variety in the ai behavior, also increased combat difficulty/dynamic.
          # # (eq,"$aggro_mode_off",0), #optional
          # (lt, ":damage", wound_damage), #not too much damage
          # (neg|agent_slot_eq, ":inflicted", slot_agent_is_bleeding, 1),  #not bleeding
          # # (neg|agent_slot_eq, ":inflicted", slot_agent_tigh_wound, 1), #not wounded
          # (store_random_in_range,":aggro",100,251),
          # (agent_ai_set_aggressiveness,":inflicted",":aggro"),
      # (try_end),

      ##bleeding
      (try_begin), #bleeding
        # (eq,"$bleeding_off",0),
        (ge, ":damage", bleed_damage),
        (neg|agent_slot_eq, ":inflicted", slot_agent_is_bleeding, 1),
        (store_random_in_range,":chance",0,10),
        (try_begin),
          (eq,":chance",1),
          (agent_set_slot, ":inflicted", slot_agent_is_bleeding, 1),
          (try_begin),
            (eq, ":inflicted", "$g_player"),
            (display_message, "@You are bleeding profusely!", message_negative),
          (try_end),
        (try_end),
      (try_end),

      ##wound
      (try_begin), #wound
          # (eq,"$wounds_off",0),
          (ge, ":damage", wound_damage),
          (store_random_in_range,":wunde",0,25),
          (try_begin),
            (eq,":wunde",1),
            (assign,":verwundet",1),
            (neg|agent_slot_eq, ":inflicted", slot_agent_is_bleeding, 1),
            (store_random_in_range,":chance",0,2),
            (try_begin),
              (eq,":chance",1),
              (agent_set_slot, ":inflicted", slot_agent_is_bleeding, 1),
              (try_begin),
                  (eq, ":inflicted", "$g_player"),
                  (display_message, "@You are bleeding profusely!", message_negative),
              (try_end),
            (try_end),
          (try_end),
      (try_end),

      ##damage sys / decap
      (try_begin),
          # (eq,"$hitsys_off",0),
          (try_begin), #0 = normal body
              # (eq, ":hitbone", 0),
              # (assign, ":bdamage", ":damage"),
              # (assign, ":damage", ":bdamage"),
              # (assign, reg1, ":bdamage"),
              # (try_begin),
                  # (eq,"$display_damage",1),
                  # (try_begin),
                      # (eq, ":dealer", "$g_player"),
                      # (display_message, "@Delivered {reg1} damage to the body!", 0x3AD54F),
                  # (else_try),
                      # (eq, ":inflicted", "$g_player"),
                      # (display_message, "@Received {reg1} damage to the body!", 0xFF0000),
                  # (try_end),
              # (try_end),
          (else_try),   #oberschenkel
              (this_or_next|eq, ":hitbone", 1),
              (eq, ":hitbone", 4),
              (try_begin),
                (eq, ":attack_was_ranged", 1),
                (assign, ":bdamage", ":damage"),
                (val_mul, ":bdamage", 95),
                (val_div, ":bdamage", 100),
                (assign, ":damage", ":bdamage"),
                # (assign, reg1, ":bdamage"),
              (try_end),

              (try_begin),
                  (eq,":verwundet",1),
                  (neg|agent_slot_eq, ":inflicted", slot_agent_tigh_wound, 1),
                  (call_script,"script_tocan_wounds",":inflicted",slot_agent_tigh_wound,1),
                  # (agent_set_slot, ":inflicted", slot_agent_is_bleeding, 1),
                  (try_begin),
                      (eq, ":inflicted", "$g_player"),
                      (assign,"$g_player_tigh_wound",1),
                      # (assign,"$player_has_wound",1),
                      (display_message, "@You received a wound to the tigh!", message_negative),
                  (try_end),
              (try_end),
              # (try_begin),
                  # (eq,"$display_damage",1),
                  # (try_begin),
                      # (eq, ":dealer", "$g_player"),
                      # (display_message, "@Delivered {reg1} damage to the thigh!", 0x3AD54F),
                  # (else_try),
                      # (eq, ":inflicted", "$g_player"),
                      # (display_message, "@Received {reg1} damage to the thigh!", 0xFF0000),
                  # (try_end),
              # (try_end),
          (else_try),
              (this_or_next|eq, ":hitbone", 2),
              (eq, ":hitbone", 5),
              (try_begin),
                (eq, ":attack_was_ranged", 1),

                (assign, ":bdamage", ":damage"),
                (val_mul, ":bdamage", 85),
                (val_div, ":bdamage", 100),
                (assign, ":damage", ":bdamage"),
                # (assign, reg1, ":bdamage"),
              (try_end),
              (try_begin),
                  (eq,":verwundet",1),
                  (neg|agent_slot_eq, ":inflicted", slot_agent_calf_wound, 1),
                  (call_script,"script_tocan_wounds",":inflicted",slot_agent_calf_wound,1),
                  # (agent_set_slot, ":inflicted", slot_agent_is_bleeding, 1),
                  (try_begin),
                      (neg|agent_is_non_player, ":inflicted"),
                      (assign,"$g_player_calf_wound",1),
                      # (assign,"$player_has_wound",1),
                      (display_message, "@You received a wound to the calf!", message_negative),
                  (try_end),
              (try_end),
              # (try_begin),
                  # (eq,"$display_damage",1),
                  # (try_begin),
                      # (eq, ":dealer", "$g_player"),
                      # (display_message, "@Delivered {reg1} damage to the calf!", 0x3AD54F),
                  # (else_try),
                      # (eq, ":inflicted", "$g_player"),
                      # (display_message, "@Received {reg1} damage to the calf!", 0xFF0000),
                  # (try_end),
              # (try_end),
          (else_try),
              (this_or_next|eq, ":hitbone", 3),
              (eq, ":hitbone", 6),
              (try_begin),
                (eq, ":attack_was_ranged", 1),

                (assign, ":bdamage", ":damage"),
                (val_mul, ":bdamage", 75),
                (val_div, ":bdamage", 100),
                (assign, ":damage", ":bdamage"),
                # (assign, reg1, ":bdamage"),
              (try_end),
              (try_begin),
                  (eq,":verwundet",1),
                  (neg|agent_slot_eq, ":inflicted", slot_agent_foot_wound, 1),
                  (call_script,"script_tocan_wounds",":inflicted",slot_agent_foot_wound,1),
                  # (agent_set_slot, ":inflicted", slot_agent_is_bleeding, 1),
                  (try_begin),
                      (eq, ":inflicted", "$g_player"),
                      (assign,"$g_player_foot_wound",1),
                      # (assign,"$player_has_wound",1),
                      (display_message, "@You received a wound to the foot!", message_negative),
                  (try_end),
              (try_end),
              # (try_begin),
                  # (eq,"$display_damage",1),
                  # (try_begin),
                      # (eq, ":dealer", "$g_player"),
                      # (display_message, "@Delivered {reg1} damage to the foot!", 0x3AD54F),
                  # (else_try),
                      # (eq, ":inflicted", "$g_player"),
                      # (display_message, "@Received {reg1} damage to the foot!", 0xFF0000),
                  # (try_end),
              # (try_end),
          (else_try),
              (eq, ":hitbone", 7),
              (try_begin),
                (eq, ":attack_was_ranged", 1),

                (assign, ":bdamage", ":damage"),
                (val_mul, ":bdamage", 125),
                (val_div, ":bdamage", 100),
                (assign, ":damage", ":bdamage"),
                # (assign, reg1, ":bdamage"),
              (try_end),
              (try_begin),
                  (eq,":verwundet",1),
                  (neg|agent_slot_eq, ":inflicted", slot_agent_spine_wound, 1),
                  (call_script,"script_tocan_wounds",":inflicted",slot_agent_spine_wound,1),
                  # (agent_set_slot, ":inflicted", slot_agent_is_bleeding, 1),
                  (try_begin),
                      (eq, ":inflicted", "$g_player"),
                      (assign,"$g_player_spine_wound",1),
                      # (assign,"$player_has_wound",1),
                      (display_message, "@You received a wound to the spine!", message_negative),
                  (try_end),
              (try_end),
              # (try_begin),
                  # (eq,"$display_damage",1),
                  # (try_begin),
                      # (eq, ":dealer", "$g_player"),
                      # (display_message, "@Delivered {reg1} damage to the spine!", 0x3AD54F),
                  # (else_try),
                      # (eq, ":inflicted", "$g_player"),
                      # (display_message, "@Received {reg1} damage to the spine!", 0xFF0000),
                  # (try_end),
              # (try_end),
          (else_try),
              (eq, ":hitbone", 8),
              (try_begin),
                (eq, ":attack_was_ranged", 1),

                (assign, ":bdamage", ":damage"),
                (val_mul, ":bdamage", 110),
                (val_div, ":bdamage", 100),
                (assign, ":damage", ":bdamage"),
                # (assign, reg1, ":bdamage"),
              (try_end),
              (try_begin),
                  (eq,":verwundet",1),
                  (neg|agent_slot_eq, ":inflicted", slot_agent_thorax_wound, 1),
                  (call_script,"script_tocan_wounds",":inflicted",slot_agent_thorax_wound,1),
                  # (agent_set_slot, ":inflicted", slot_agent_is_bleeding, 1),
                  (try_begin),
                      (eq, ":inflicted", "$g_player"),
                      (assign,"$g_player_thorax_wound",1),
                      # (assign,"$player_has_wound",1),
                      (display_message, "@You received a wound to the torax!", message_negative),
                  (try_end),
              (try_end),
              # (try_begin),
                  # (eq,"$display_damage",1),
                  # (try_begin),
                      # (eq, ":dealer", "$g_player"),
                      # (display_message, "@Delivered {reg1} damage to the thorax!", 0x3AD54F),
                  # (else_try),
                      # (eq, ":inflicted", "$g_player"),
                      # (display_message, "@Received {reg1} damage to the thorax!", 0xFF0000),
                  # (try_end),
              # (try_end),
          (else_try),
              (eq, ":hitbone", 9),
              (try_begin),
                  (eq, ":attack_was_ranged", 0),

                  # (assign, ":bdamage", ":damage"),
                  # (val_mul, ":bdamage", 150),
                  # (val_div, ":bdamage", 100),
                  # (assign, ":damage", ":bdamage"),
                  # (assign, reg1, ":bdamage"),
                  (try_begin), #new animation
                      (gt, ":damage", bleed_damage),
                      (store_random_in_range,":chance",0,5),
                      (try_begin),
                          (eq, ":chance", 1),
                          # (agent_get_horse, ":inflicted_mount",":inflicted"),
                          (le, ":inflicted_mount", -1),
                          (assign,":animation","anim_kicked_down"),
                      (try_end),
                  (try_end),
              (else_try),
                  # (is_between, ":attacker_weapon", ranged_weapons_begin, ranged_weapons_end),

                  (assign, ":bdamage", ":damage"),
                  (val_mul, ":bdamage", 200),
                  (val_div, ":bdamage", 100),
                  (assign, ":damage", ":bdamage"),
                  (assign, reg1, ":bdamage"),
              (try_end),
              (try_begin),
                  (eq,":verwundet",1),
                  (neg|agent_slot_eq, ":inflicted", slot_agent_head_wound, 1),
                  (call_script,"script_tocan_wounds",":inflicted",slot_agent_head_wound,1),
                  # (agent_set_slot, ":inflicted", slot_agent_is_bleeding, 1),
                  (try_begin),
                      (eq, ":inflicted", "$g_player"),
                      (assign,"$g_player_head_wound",1),
                      # (assign,"$player_has_wound",1),
                      (display_message, "@You received a wound to the head!", message_negative),
                  (try_end),
              (try_end),
              # (try_begin),
                  # (eq,"$display_damage",1),
                  # (try_begin),
                      # (eq, ":dealer", "$g_player"),
                      # (display_message, "@Delivered {reg1} damage to the head!", 0x3AD54F),
                  # (else_try),
                      # (eq, ":inflicted", "$g_player"),
                      # (display_message, "@Received {reg1} damage to the head!", 0xFF0000),
                  # (try_end),
              # (try_end),
              (try_begin),
                  # (eq,"$decap_off",0),
                  # (try_begin),
                      (neq, ":inflicted", "$g_player"),
                      (neg | troop_is_hero,":agent_troop_id_victim"),

                      # (store_faction_of_troop, ":faction", ":agent_troop_id_victim"),
                      # (neq,":faction","fac_infected"),
                      # (neq,":faction","fac_mutants"),

                      (eq, ":inflicted_race", tf_man),
                      # (this_or_next|eq, ":inflicted_race", tf_man),
                      # (this_or_next|eq, ":inflicted_race", tf_man_big),
                      # (eq, ":inflicted_race", tf_man_small),

                      (store_agent_hit_points, ":inflicted_hp", ":inflicted", 1),
                      (store_sub, ":inflicted_new_hp", ":inflicted_hp", ":damage"),
                      (le, ":inflicted_new_hp", 0),

                      (gt, ":attacker_weapon", 0),

                      (item_get_swing_damage, ":swing_damage", ":attacker_weapon"),
                      (item_get_thrust_damage, ":thrust_damage", ":attacker_weapon"),
                      (try_begin),
                        (ge, ":swing_damage", ":thrust_damage"),
                        (item_get_swing_damage_type, ":item_dmg_type", ":attacker_weapon"),
                      (else_try),
                        (lt, ":swing_damage", ":thrust_damage"),
                        (item_get_thrust_damage_type, ":item_dmg_type", ":attacker_weapon"),
                      (try_end),
                      (eq,":item_dmg_type",0),

                      (assign, ":base_chance", 5),
                      (try_begin),
                          (agent_get_horse, ":horse", ":dealer"),
                          (try_begin), # Mounted bot
                              (agent_is_non_player, ":dealer"),
                              (try_begin),
                                  (neq, ":horse", -1),
                                  (val_add, ":base_chance", 10),
                              (try_end),
                          (else_try), #Player bonus
                              (eq,":dealer","$g_player"),
                              (store_attribute_level, ":skill", "$g_player", ca_strength),
                              (val_add, ":base_chance", ":skill"),
                              (try_begin),
                                  (neq, ":horse", -1),
                                  (val_add, ":base_chance", 30),
                              (try_end),
                          (try_end),
                          (try_begin), # Helmet
                              (agent_get_item_slot, ":head_gear", ":inflicted", ek_head),
                              (ge, ":head_gear", 1),
                              (item_get_head_armor, ":armor", ":head_gear"),
                              (gt, ":armor", 20),
                              (val_sub, ":base_chance", 5),
                          (try_end),
                          (val_max, ":base_chance", 30),
                      (try_end),
                      (store_random_in_range, ":rand", 1, 101),

                      (ge, ":base_chance", ":rand"),

                      (try_begin),
                        (agent_get_item_slot, ":head_gear", ":inflicted", ek_head),
                        (ge, ":head_gear", 1),
                        (assign, ":spawn_for_timer", 60),

                        # helmet on the ground
                        (copy_position, pos2, pos0),
                        (position_move_x, pos2, 20, 0),
                        (position_move_z, pos2, -30, 0),
                        (store_random_in_range, ":rot_x", 10, 40),
                        (store_random_in_range, ":rot_z", 15, 75),
                        (position_rotate_x, pos2, ":rot_x", 1),
                        (position_rotate_z, pos2, ":rot_z", 1),
                        (position_set_z_to_ground_level, pos2),
                        (position_move_y, pos2, -5, 1),
                        (set_spawn_position, pos2),
                        (spawn_item, ":head_gear", 0, ":spawn_for_timer"),

                        (agent_unequip_item, ":inflicted", ":head_gear"),
                      (try_end),

                      # equip invisible head on agent
                      (agent_equip_item, ":inflicted", "itm_invisi_head"),

                      # blood
                      # (copy_position, pos2, pos0),
                      (set_spawn_position, pos0),
                      # # (particle_system_burst, "psys_game_blood", pos2, 5), #tocan test
                      # (particle_system_burst, "psys_game_blood_2", pos2, 5),
                      # (particle_system_burst, "psys_game_blood_2", pos2, 15),
                      # (particle_system_burst, "psys_explosion_blood", pos2, 5),
                      (particle_system_burst, "psys_game_blood", pos0, 125),
                      (particle_system_burst, "psys_game_blood_2", pos0, 135),
                      (particle_system_burst, "psys_explosion_blood", pos0, 125),
                      # fake head
                      (spawn_scene_prop, "spr_physics_head"),
                      (assign, ":head_id", reg0),

                      (prop_instance_enable_physics, ":head_id", 1),

                      # makes sure the agent dies
                      (agent_set_hit_points,":inflicted", 0, 1),
                  (try_end),
              (try_end),
          (else_try),
              (this_or_next|eq, ":hitbone", 10),
              (eq, ":hitbone", 15),
              (try_begin),
                (eq, ":attack_was_ranged", 1),

                (assign, ":bdamage", ":damage"),
                (val_mul, ":bdamage", 90),
                (val_div, ":bdamage", 100),
                (assign, ":damage", ":bdamage"),
                # (assign, reg1, ":bdamage"),
              (try_end),
              (try_begin),
                  (eq,":verwundet",1),
                  (neg|agent_slot_eq, ":inflicted", slot_agent_shoulder_wound, 1),
                  (call_script,"script_tocan_wounds",":inflicted",slot_agent_shoulder_wound,1),
                  # (agent_set_slot, ":inflicted", slot_agent_is_bleeding, 1),
                  (try_begin),
                      (agent_get_wielded_item,":defender_weapon",":inflicted",0),
                      (gt,":defender_weapon",0),
                      (store_random_in_range,":damn",0,5),
                      (eq,":damn",1),
                      (agent_unequip_item, ":inflicted", ":defender_weapon"),
                      (spawn_item, ":defender_weapon", 0, 1000),
                  (try_end),
                  (try_begin),
                      (eq, ":inflicted", "$g_player"),
                      (assign,"$g_player_shoulder_wound",1),
                      # (assign,"$player_has_wound",1),
                      (display_message, "@You received a wound to the shoulder!", message_negative),
                  (try_end),
              (try_end),
              # (try_begin),
                  # (eq,"$display_damage",1),
                  # (try_begin),
                      # (eq, ":dealer", "$g_player"),
                      # (display_message, "@Delivered {reg1} damage to the shoulder!", 0x3AD54F),
                  # (else_try),
                      # (eq, ":inflicted", "$g_player"),
                      # (display_message, "@Received {reg1} damage to the shoulder!", 0xFF0000),
                  # (try_end),
              # (try_end),
          (else_try),
              (this_or_next|is_between, ":hitbone", 11, 13),
              (is_between, ":hitbone", 16, 18),
              (try_begin),
                (eq, ":attack_was_ranged", 1),

                (assign, ":bdamage", ":damage"),
                (val_mul, ":bdamage", 80),
                (val_div, ":bdamage", 100),
                (assign, ":damage", ":bdamage"),
                # (assign, reg1, ":bdamage"),
              (try_end),
              (try_begin),
                  (eq,":verwundet",1),
                  (neg|agent_slot_eq, ":inflicted", slot_agent_arm_wound, 1),
                  (call_script,"script_tocan_wounds",":inflicted",slot_agent_arm_wound,1),
                  # (agent_set_slot, ":inflicted", slot_agent_is_bleeding, 1),
                  (try_begin),
                      (agent_get_wielded_item,":defender_weapon",":inflicted",0),
                      (gt,":defender_weapon",0),
                      (store_random_in_range,":damn",0,3),
                      (eq,":damn",1),
                      # (item_get_type, ":item_type", ":defender_weapon"),
                      # (neq, ":item_type", itp_type_one_handed_wpn),
                      (agent_unequip_item, ":inflicted", ":defender_weapon"),
                      (spawn_item, ":defender_weapon", 0, 1000),
                  (try_end),
                  (try_begin),
                      (eq, ":inflicted", "$g_player"),
                      (assign,"$g_player_arm_wound",1),
                      # (assign,"$player_has_wound",1),
                      (display_message, "@You received a wound to the arm!", message_negative),
                  (try_end),
              (try_end),
              # (try_begin),
                  # (eq,"$display_damage",1),
                  # (try_begin),
                      # (eq, ":dealer", "$g_player"),
                      # (display_message, "@Delivered {reg1} damage to the arm!", 0x3AD54F),
                  # (else_try),
                      # (eq, ":inflicted", "$g_player"),
                      # (display_message, "@Received {reg1} damage to the arm!", 0xFF0000),
                  # (try_end),
              # (try_end),
          (else_try),
              (this_or_next|eq, ":hitbone", 13),
              (eq, ":hitbone", 18),
              (try_begin),
                (eq, ":attack_was_ranged", 1),

                (assign, ":bdamage", ":damage"),
                (val_mul, ":bdamage", 70),
                (val_div, ":bdamage", 100),
                (assign, ":damage", ":bdamage"),
                # (assign, reg1, ":bdamage"),
              (try_end),
              (try_begin),
                  (eq,":verwundet",1),
                  (neg|agent_slot_eq, ":inflicted", slot_agent_hand_wound, 1),
                  (call_script,"script_tocan_wounds",":inflicted",slot_agent_hand_wound,1),
                  # (agent_set_slot, ":inflicted", slot_agent_is_bleeding, 1),
                  (try_begin),
                      (agent_get_wielded_item,":defender_weapon",":inflicted",0),
                      (gt,":defender_weapon",0),
                      # (item_get_type, ":item_type", ":defender_weapon"),
                      # (neq, ":item_type", itp_type_one_handed_wpn),
                      (agent_unequip_item, ":inflicted", ":defender_weapon"),
                      (spawn_item, ":defender_weapon", 0, 1000),
                  (try_end),
                  (try_begin),
                      (eq, ":inflicted", "$g_player"),
                      (assign,"$g_player_hand_wound",1),
                      # (assign,"$player_has_wound",1),
                      (display_message, "@You received a wound to the hand!", message_negative),
                  (try_end),
              (try_end),
              # (try_begin),
                  # (eq,"$display_damage",1),
                  # (try_begin),
                      # (eq, ":dealer", "$g_player"),
                      # (display_message, "@Delivered {reg1} damage to the hand!", 0x3AD54F),
                  # (else_try),
                      # (eq, ":inflicted", "$g_player"),
                      # (display_message, "@Received {reg1} damage to the hand!", 0xFF0000),
                  # (try_end),
              # (try_end),
          (try_end),
      (try_end),

      ##special behavior
      (try_begin),
        (eq, ":agent_troop_id_victim", "trp_fanatic"),
        (store_agent_hit_points, ":inflicted_hp", ":inflicted"),
        (le, ":inflicted_hp", 15),
        # (agent_set_slot, ":inflicted", slot_agent_runs_amok, 1),
        (agent_equip_item, ":inflicted", "itm_dynamite"),
        (agent_set_wielded_item, ":inflicted", "itm_dynamite"),
      (try_end),

      ##player cam
      (try_begin),
        (eq,":inflicted","$g_player"),
        (gt, "$g_fate_cam_shake_frames", 0),
        (assign,":xdamage",":damage"),
        (val_div,":xdamage",10),
        (val_min,":xdamage",10),
        (val_add, "$g_fate_cam_shake_frames", ":xdamage"),
      (try_end),

      ##animation
      #special attacks
      (try_begin),
        # (gt,":damage",0),
        # (eq,":animation",-1),
        (this_or_next|eq,":attacker_weapon","itm_brute_attack"),
        (eq,":ek_gloves","itm_powerfist"),
        (try_begin),
          (eq, ":ek_gloves", "itm_powerfist"),
          (val_add, ":damage", 30),
          (agent_play_sound, ":dealer", "snd_powerfist"),
        (try_end),

        # (assign, ":bdamage", ":damage"),
        # (val_mul, ":bdamage", 200),
        # (val_div, ":bdamage", 100),
        # (assign, ":damage", ":bdamage"),
        # # # (call_script,"script_tocan_fall",pos1,":dealer"),
        # (agent_get_horse, ":inflicted_mount",":inflicted"),
        (le, ":inflicted_mount", -1),
        (store_random_in_range,":chance",0,5),
        (try_begin),
            (eq,":chance",1),
            (assign, ":animation", "anim_pushed_back_15"),
        (else_try),
            (eq,":chance",2),
            (assign, ":animation", "anim_strike_fly_back_med_rise"),
        (else_try),
            (eq,":chance",3),
            (assign, ":animation", "anim_strike_fly_back_far_rise"),
        (try_end),
      (try_end),
      #fallback big damage
      (try_begin),
          (ge,":damage",big_damage),
          (eq,":animation",-1),
          # (agent_get_horse, ":inflicted_mount",":inflicted"),
          (le, ":inflicted_mount", -1),
          (store_random_in_range,":chance",0,3),
          (try_begin),
              (eq,":chance",1),
              (assign,":fallback",1),
          (try_end),
      (try_end),
      #animation  set
      (try_begin),
          (neq,":animation",-1),
          # (agent_get_troop_id, ":agent_troop_id_victim", ":inflicted"),
          (store_faction_of_troop, ":faction", ":agent_troop_id_victim"),
          (neq, ":faction", "fac_infected"),
          (neq, ":faction", "fac_mutants"),
          # (neq, ":troop", "trp_brute_zombie"),
          (try_begin),
              (eq,":fallback",1),
              (store_random_in_range,":chance",1,4),
              (try_begin),
                  (eq,":chance",1),
                  (agent_set_animation, ":inflicted", "anim_strike_fall_back_rise"),
                  (agent_set_animation, ":inflicted", "anim_strike_fall_back_rise_upper"),
              (else_try),
                  (eq,":chance",2),
                  (agent_set_animation, ":inflicted", "anim_strike_fly_back_near_rise"),
              (else_try),
                  (eq,":chance",3),
                  (agent_set_animation, ":inflicted", "anim_fall_far_back2"),
              (try_end),
          (else_try),
              (agent_set_animation, ":inflicted", ":animation"),
          (try_end),
      (try_end),

      (try_begin),
        (this_or_next|eq, ":inflicted_race", tf_skeleton),
        (eq, ":inflicted_race", tf_undead),
        (try_begin),
          (eq, ":attack_was_ranged", 1), #25%
          (val_div, ":damage", 4),
        (else_try),
          (val_div, ":damage", 2), #50%
        (try_end),
        (particle_system_burst, "psys_game_blood_black_2", pos0, 15),
      (else_try),
        (this_or_next|eq, ":inflicted_race", tf_mutant),
        (this_or_next|eq, ":inflicted_race", tf_mutant_big),
        (this_or_next|eq, ":inflicted_race", tf_ghoul),
        (this_or_next|eq, ":inflicted_race", tf_infected),
        (eq, ":inflicted_race", tf_rancor),
        (try_begin),
          (eq, ":attack_was_ranged", 1), #50%
          (val_div, ":damage", 2),
        (else_try),              #50%
          (val_div, ":damage", 2),
        (try_end),
        (particle_system_burst, "psys_game_blood_green_2", pos0, 15),
      (else_try),
        (eq, ":inflicted_race", tf_droid),
        (try_begin),
          (eq, ":attack_was_ranged", 1), #666%
          (val_div, ":damage", 3),
        (else_try),              #50%
          (val_div, ":damage", 2),
        (try_end),
        (particle_system_burst, "psys_hit_robo", pos0, 15),
      (else_try),
        (eq, ":attack_was_ranged", 1),
        (val_mul, ":damage", 75),
        (val_div, ":damage", 100),
      (try_end),

      (try_begin),
        (agent_slot_eq, ":inflicted", slot_agent_smokecover, 1),
        (val_div, ":damage",2),
      (try_end),

      (try_begin),
        (ge, ":damage",5),

        (troop_get_inventory_slot, ":ek_gloves_defender", ":agent_troop_id_victim", ek_gloves),
        (this_or_next|eq, ":ek_gloves_defender", "itm_brassknuckles"),
        (this_or_next|eq, ":ek_gloves_defender", "itm_renfieldgauntlet"),
        (eq, ":ek_gloves_defender", "itm_powerfist"),

        (agent_get_animation, ":cur_animation", ":inflicted", 1),
        (is_between,":cur_animation","anim_defend_fist","anim_defend_shield_forward"),
        (val_div, ":damage", 5),
      (else_try),
        (lt, ":damage",5),

        (neq, "$g_player", ":inflicted"),
        (agent_is_alive, ":inflicted"),
        (store_random_in_range, ":rnd", 0, 20),
        (eq, ":rnd", 1),
        (eq, ":inflicted_race", 0),

        (play_sound_at_position, "snd_usa_cry", pos0),
      (else_try),
        (ge, ":damage",25),

        (neq, "$g_player", ":inflicted"),
        (agent_is_alive, ":inflicted"),
        (store_random_in_range, ":rnd", 0, 20),
        (eq, ":rnd", 1),
        (eq, ":inflicted_race", 0),

        (play_sound_at_position, "snd_warcry", pos0),
      (try_end),

      #trigger
      (set_trigger_result, ":damage"),
        ],),

    (ti_on_item_wielded, 0, 0, [(neg|main_hero_fallen),], [	#5
      (set_fixed_point_multiplier, 100),
      (store_trigger_param_1, ":agent"),
      (store_trigger_param_2, ":item"),

      (gt, ":agent", 0),
      (gt, ":item", 0),
      (neg|agent_is_non_player, ":agent"),

      (agent_is_alive, ":agent"),

      # (agent_get_troop_id, ":troop", ":agent"),

      (item_get_type, ":type", ":item"),

      # (store_sub, ":previous_item", ":item", 1),

      # Fate combat reload, needs tweaks to keep empty weapons empty
      # TODO: Set up seperate agent slots for item slots 1 - 4 to track individual clips
      #		This will prevent clips from being overwritten between weapons.

      (try_begin),
        (this_or_next|eq, ":type", itp_type_musket),
        (eq, ":type", itp_type_pistol),

        (try_begin),
          # (eq, "$g_ammo_unequip", 1),
          (call_script, "script_cf_player_ammo_check",1),
        (try_end),

        (assign, ":ammo", 0),

        (agent_get_item_slot, ":slot1", ":agent", 0),
        (try_begin),
          (gt, ":slot1", 0),
          (item_get_type, ":slot1_type", ":slot1"),
        (try_end),

        (agent_get_item_slot, ":slot2", ":agent", 1),
        (try_begin),
          (gt, ":slot2", 0),
          (item_get_type, ":slot2_type", ":slot2"),
        (try_end),

        (agent_get_item_slot, ":slot3", ":agent", 2),
        (try_begin),
          (gt, ":slot3", 0),
          (item_get_type, ":slot3_type", ":slot3"),
        (try_end),

        (agent_get_item_slot, ":slot4", ":agent", 3),
        (try_begin),
          (gt, ":slot4", 0),
          (item_get_type, ":slot4_type", ":slot4"),
        (try_end),

        (try_begin),
          (gt, ":slot1", 0),
          (eq, ":slot1_type", itp_type_bullets),
          (assign, ":ammo", ":slot1"),
        (else_try),
          (gt, ":slot2", 0),
          (eq, ":slot2_type", itp_type_bullets),
          (assign, ":ammo", ":slot2"),
        (else_try),
          (gt, ":slot3", 0),
          (eq, ":slot3_type", itp_type_bullets),
          (assign, ":ammo", ":slot3"),
        (else_try),
          (gt, ":slot4", 0),
          (eq, ":slot4_type", itp_type_bullets),
          (assign, ":ammo", ":slot4"),
        (try_end),

        (try_begin),
          (eq, ":ammo", 0),
          (assign, ":ammo", "itm_pistol_ammo"),
        (try_end),


        (item_get_max_ammo, ":clip_size", ":item"),
        (agent_get_ammo, ":total_ammo", ":agent", 1),
        (item_get_slot, ":first_clip", ":item", slot_item_first_clip),

        (agent_get_slot, ":current_clip", ":agent", slot_agent_ammo_in_clip),
        (val_add, ":total_ammo", ":current_clip"),

        (try_begin),
          (eq, ":first_clip", 1),
          (agent_set_slot, ":agent", slot_agent_ammo_in_clip, ":clip_size"),
          (item_set_slot, ":item", slot_item_first_clip, 0),
        (else_try),
          (eq, ":total_ammo", 0),
          (assign, ":clip_size", 0),
          #(display_message, "@You're out of ammunition!"),
          (agent_set_slot, ":agent", slot_agent_ammo_in_clip, ":clip_size"),
        (else_try),
          (ge, ":total_ammo", ":clip_size"),
          (val_sub, ":total_ammo", ":clip_size"),
          (agent_set_ammo, ":agent", ":ammo", ":total_ammo"),
          (agent_set_slot, ":agent", slot_agent_ammo_in_clip, ":clip_size"),
        (else_try),
          (assign, ":clip_size", ":total_ammo"),
          (agent_set_ammo, ":agent", ":ammo", 0),
          (agent_set_slot, ":agent", slot_agent_ammo_in_clip, ":clip_size"),
        (try_end),

        (agent_set_kick_allowed, ":agent", 0), # Disable Kicks for Firearms, allowing 'E' to reload.
      (else_try),
        (agent_set_kick_allowed, ":agent", 1),
      (try_end),

      # (try_begin),
        # (eq, ":item", "itm_vulcan"),
        # (agent_set_stand_animation, ":agent", "anim_idle_minigun"),
        # (agent_set_speed_modifier, ":agent", 25),
        # (agent_set_animation, ":agent", "anim_idle_minigun", 1),
        # (display_message, "@Equipped Minigun! Carnage Awaits!", 0xFF736252),
      # (else_try),
        # (agent_set_stand_animation, ":agent", -1),
        # (agent_set_speed_modifier, ":agent", 100),
      # (try_end),
        ],),

    (ti_on_item_unwielded, 0, 0, [(neg|main_hero_fallen),], [	#6
      (store_trigger_param_1, ":player"),
      (store_trigger_param_2, ":item"),
      #(store_trigger_param_3, ":slot"),

      (gt, ":player", 0),
      (gt, ":item", 0),

      (neg|agent_is_non_player, ":player"),

      (agent_is_alive, "$g_player"),

      (item_get_type, ":type", ":item"),
      (this_or_next|eq, ":type", itp_type_pistol),
      (eq, ":type", itp_type_musket),

      (agent_get_slot, ":speed_modifier", "$g_player", slot_agent_speed_mod),
      (agent_set_speed_modifier, "$g_player", ":speed_modifier"),

      (try_begin),
        (agent_slot_eq, "$g_player", slot_agent_gun_ironsight_on, 1),

        (item_get_slot, ":ironsight", ":item", slot_item_has_ironsight),

        (agent_set_slot, "$g_player", slot_agent_gun_ironsight_on, 0),
        (agent_set_visibility, "$g_player", 1),
        (mission_cam_set_mode, 0),

        (ge, ":ironsight", 0), #for script errors
        (scene_prop_get_num_instances, ":total", ":ironsight"),
        (try_begin),
          (gt, ":total",0),
          (try_for_range,":cur_instance",0,":total"),
            (scene_prop_get_instance, ":instance_id", ":ironsight", ":cur_instance"),
            (prop_instance_get_position, pos1, ":instance_id"),
            (position_move_z, pos1, -10000),
            (prop_instance_set_position, ":instance_id", pos1),
            # (prop_instance_animate_to_position, ":instance_id", pos1, 1),
            # (scene_prop_fade_in, ":instance_id", 1),
          (try_end),
        (try_end),
      (try_end),
      (try_begin),
        (agent_slot_eq, "$g_player", slot_agent_gun_scope_on, 1),

        (agent_set_slot, "$g_player", slot_agent_gun_scope_on, 0),
        (agent_set_visibility, "$g_player", 1),
        (mission_cam_set_mode, 0),
      (try_end),

      (agent_slot_eq, "$g_player", slot_agent_gun_aim_on, 1),
      (agent_set_slot, "$g_player", slot_agent_gun_aim_on, 0),
      (agent_set_slot, "$g_player", slot_agent_gun_automatic_on, 0),

      ]),

    (ti_on_item_dropped, 0, 0, [(neg|main_hero_fallen),], [	#7
      (store_trigger_param_1, ":agent"),
      (store_trigger_param_2, ":item"),
      # (store_trigger_param_3, ":item_instance"),

      (agent_is_alive, "$g_player"),

      (gt, ":agent", 0),
      (gt, ":item", 0),

      # (try_begin),
        # (item_get_type, ":type", ":item"),
        # (eq, ":type", itp_type_bullets),
        # (prop_instance_get_position, pos1, ":item_instance"),
        # (set_spawn_position,pos1),
        # (spawn_scene_prop, "spr_ammobag"),
      # (try_end),
#
      (neg|agent_is_non_player, ":agent"),

      # (agent_is_alive, "$g_player"),

      (item_get_type, ":type", ":item"),
      (this_or_next|eq, ":type", itp_type_pistol),
      (eq, ":type", itp_type_musket),

      (agent_get_slot, ":speed_modifier", "$g_player", slot_agent_speed_mod),
      (agent_set_speed_modifier, "$g_player", ":speed_modifier"),

      (try_begin),
        (agent_slot_eq, "$g_player", slot_agent_gun_ironsight_on, 1),

        (item_get_slot, ":ironsight", ":item", slot_item_has_ironsight),

        (agent_set_slot, "$g_player", slot_agent_gun_ironsight_on, 0),
        (agent_set_visibility, "$g_player", 1),
        (mission_cam_set_mode, 0),

		(ge, ":ironsight", 0), #for script errors
        (scene_prop_get_num_instances, ":total", ":ironsight"),
        (try_begin),
          (gt, ":total",0),
          (try_for_range,":cur_instance",0,":total"),
            (scene_prop_get_instance, ":instance_id", ":ironsight", ":cur_instance"),
            (prop_instance_get_position, pos1, ":instance_id"),
            (position_move_z, pos1, -10000),
            (prop_instance_set_position, ":instance_id", pos1),
            # (prop_instance_animate_to_position, ":instance_id", pos1, 1),
            # (scene_prop_fade_in, ":instance_id", 1),
          (try_end),
        (try_end),
      (try_end),
      (try_begin),
        (agent_slot_eq, "$g_player", slot_agent_gun_scope_on, 1),

        (agent_set_slot, "$g_player", slot_agent_gun_scope_on, 0),
        (agent_set_visibility, "$g_player", 1),
        (mission_cam_set_mode, 0),
      (try_end),

      (agent_slot_eq, "$g_player", slot_agent_gun_aim_on, 1),
      (agent_set_slot, "$g_player", slot_agent_gun_aim_on, 0),
      (agent_set_slot, "$g_player", slot_agent_gun_automatic_on, 0),
      ]),

 	(ti_on_item_picked_up, 0, 0,	#attempt ai weapon conversion - krag	#8
       [(neg|main_hero_fallen),],
       [
        (store_trigger_param_1, ":agent_id"),
        (store_trigger_param_2, ":weapon"),
        (store_trigger_param_3, ":prop"),

        # (get_player_agent_no, ":player_agent"),
        (eq, ":agent_id", "$g_player"),
        #(str_store_item_id, s33, ":weapon"),
        #(display_message, "@OLD:{s33}"),


        (try_begin),
          (is_between, ":weapon", ai_ranged_weapons_begin, ai_ranged_weapons_end_2h),

          (try_for_range, ":item_slot", ek_item_0, ek_horse),
            (agent_get_item_slot, ":item_no", ":agent_id", ":item_slot"),
            #(gt, ":item_no", -1),
            (eq, ":item_no", ":weapon"),
            (assign,":item_slot_for_swap",":item_slot"),
          (try_end),

          (assign,":new_item",":weapon"),
          (agent_get_item_cur_ammo, ":new_ammo", ":agent_id", ":item_slot_for_swap"),



          (agent_unequip_item, ":agent_id", ":weapon", ":item_slot_for_swap"),
          (try_begin),
            (is_between, ":weapon", ai_ranged_weapons_begin_2h, ai_ranged_weapons_end_2h),

            (val_sub, ":new_item", ai_ranged_weapons_begin_2h),
            (val_add, ":new_item", firearms_begin),
           (else_try),
            (val_sub, ":new_item", ai_ranged_weapons_begin),
            (val_add, ":new_item", firearms_begin),
			(try_begin),
				(this_or_next|eq, ":new_item", "itm_rifle_arisaka_b_alt"),	#convert melee version to ranged for bayonet guns - krag
				(this_or_next|eq, ":new_item", "itm_rifle_m1_garand_bayonet"),
				(eq, ":new_item", "itm_rifle_m1_garand_alt_bayonet"),
				(val_sub, ":new_item",1),
				#(item_get_max_ammo, ":new_ammo",":new_item"),
				(prop_instance_get_position, pos14, ":prop"),
				(set_spawn_position, pos14),
				(spawn_item, "itm_rifle_ammo", 0, 1000),
            (try_end),
          (try_end),



            #   # (str_store_item_name, s33, ":item_no"),
            #   # (str_store_item_name, s34, ":new_item"),
            #   # (display_message, "@old:{s33},  new: {s34}"),	#check conversion

				  # (try_begin),
					# (neg|is_vanilla_warband),
					# (is_edit_mode_enabled),
					# (str_store_item_id, s33, ":weapon"),
					# (str_store_item_id, s34, ":new_item"),
					# (assign, reg35, ":new_ammo"),
					# (display_message, "@OLD:{s33}, NEW:{s34}, AMMO:{reg35}"),	#check conversion
				  # (try_end),
          (agent_equip_item, ":agent_id", ":new_item", ":item_slot_for_swap"),
          (agent_set_ammo, ":agent_id", ":new_item", ":new_ammo"),
          (agent_set_wielded_item, ":agent_id", ":new_item"),
		  (call_script, "script_set_current_player_weapon", ":item_slot_for_swap", ":new_item"),

		 (else_try),  # krag robbery - attempt to steal weapon if has slot free

			(try_for_range, ":item_slot", ek_item_0, ek_horse),
				(agent_get_item_slot, ":item_no", ":agent_id", ":item_slot"),
				#(gt, ":item_no", -1),
				(eq, ":item_no", ":weapon"),
				(assign,":item_slot_for_swap",":item_slot"),
            (try_end),
			(assign,":new_item",":weapon"),
			(call_script, "script_set_current_player_weapon", ":item_slot_for_swap", ":new_item"),
        (try_end),
       ]),

    # (ti_on_item_picked_up, 0, 0, [(neg|main_hero_fallen),], [
      # (set_fixed_point_multiplier, 1000),
      # (store_trigger_param_1, ":agent"),
      # (store_trigger_param_2, ":item"),
      # (store_trigger_param_3, ":item_instance"),

      # (gt, ":agent", 0),
      # (gt, ":item", 0),

      # (neg|agent_is_non_player, ":agent"),

      # (agent_is_alive, ":agent"),

      # (item_get_type, ":type", ":item"),

      # (eq, ":type", itp_type_bullets),

      # (prop_instance_get_position, pos1, ":item_instance"),
      # (display_message,"@check instance"),
      # (try_for_prop_instances, ":instance", "spr_ammobag"),
        # (prop_instance_get_position, pos2, ":instance"),
        # (get_distance_between_positions,":doit",pos1,pos2),
        # (le,":doit",300),
        # (scene_prop_set_visibility, ":instance", 0),
      # (try_end),
       # ]),

    (ti_on_agent_killed_or_wounded, 0, 0, [],[	#9
        (store_trigger_param_1, ":agent_id"),
        #(store_trigger_param_2, ":attacker_agent_id"),

        (try_begin),
          (eq,":agent_id","$g_player"),
          (stop_sound_channel, "$heartbeat"),
        (else_try),
          (eq, "$g_animal_present", 1),
          (try_begin),
            (agent_slot_ge, ":agent_id", slot_agent_rides_x, 0),
            # (agent_slot_ge, ":agent_id", slot_agent_rides_animal, 0),

            (agent_get_troop_id, ":agent_troop_id", ":agent_id"),
            (troop_slot_eq, ":agent_troop_id", slot_troop_is_animal, 1),

            (try_begin),
              (this_or_next|eq,":agent_troop_id","trp_mutant_spider"),
              (eq,":agent_troop_id","trp_mutant_spider"),

              (play_sound,"snd_spider_death"),
            (try_end),

            (agent_get_slot, ":horse_agent_id", ":agent_id", slot_agent_rides_x),
            # (agent_get_slot, ":horse_agent_id", ":agent_id", slot_agent_rides_animal),
            # (agent_is_alive,":horse_agent_id"),


            (agent_deliver_damage_to_agent, ":horse_agent_id", ":horse_agent_id", 10000),

            # (display_message,"@Animal kills Animal"),
          (else_try),
            (agent_slot_ge, ":agent_id", slot_agent_is_animal, 0),
            (agent_get_slot, ":rider_agent_id", ":agent_id", slot_agent_is_animal),
            # (agent_is_alive,":rider_agent_id"),
            (agent_deliver_damage_to_agent, ":rider_agent_id", ":rider_agent_id", 10000),

            # (display_message,"@Animal Rider kills  Animal Rider"),
          (try_end),
		(else_try),
		    (eq, "$g_car_is_present", 2),
		  
		    (agent_get_troop_id, ":troop_id", ":agent_id"),
            (eq, ":troop_id", "trp_chopper_pilot"),
			(store_trigger_param_2, ":attacker_agent_id"),
			
			(agent_get_slot, ":instance_no", ":agent_id", slot_agent_horse_prop),
			(call_script, "script_helicopter_crash", ":instance_no", ":attacker_agent_id"),
			#(display_message, "@script_helicopter_crash pilot killed"),
        (try_end),
        ]),

    (ti_on_agent_killed_or_wounded, 0, 0, [
      (store_trigger_param_1, ":dead_agent_no"),
      (eq, ":dead_agent_no", "$g_player"),
      (agent_slot_ge, "$g_player", slot_agent_gun_ironsight_on, 1),
      (agent_get_wielded_item, ":equipped", "$g_player", 0),
      (item_get_slot, ":ironsight", ":equipped", slot_item_has_ironsight),
      (gt, ":ironsight",0),
      (scene_prop_get_num_instances, ":total", ":ironsight"),
      (gt, ":total",0),
      (try_for_range,":cur_instance",0,":total"),
        (scene_prop_get_instance, ":instance_id", ":ironsight", ":cur_instance"),
        (prop_instance_get_position, pos1, ":instance_id"),
        (position_move_z, pos1, -10000),
        (prop_instance_set_position, ":instance_id", pos1),
        # (prop_instance_animate_to_position, ":instance_id", pos1, 1),
        # (scene_prop_fade_in, ":instance_id", 1),
      (try_end),
    ],[]),

    #PLAYERmain tocan: this one is getting crazy	#10
    (0, 0, 0,
      [
        (neg|conversation_screen_is_active),
        (neg|main_hero_fallen),
      ],
      [
        (set_fixed_point_multiplier, 1000),

        (store_mission_timer_a_msec, ":time"),

        (set_fixed_point_multiplier, 100),

        (gt, "$g_player", 0), #player is active
        (agent_is_alive, "$g_player"),

        (agent_get_wielded_item, ":equipped", "$g_player", 0),
        (agent_get_wielded_item, ":shield_equipped", "$g_player", 1),
        (agent_get_animation, ":cur_animation", "$g_player", 1),
        # (agent_get_crouch_mode, ":crouching", "$g_player"),

        #stimpak //first
		(try_begin), #force crouch when using stimpak and crouching, dunno why this is necessary... - krag
			(agent_slot_eq, "$g_player", slot_agent_crouching, 1),
			(agent_slot_ge, "$g_player", slot_agent_using_stimpak, 1),
			(agent_set_speed_modifier, "$g_player", 40),
			(try_begin),
				(game_key_is_down, gk_move_forward),
				(neg|game_key_is_down, gk_move_backward),
				(neg|game_key_is_down, gk_move_left),
				(neg|game_key_is_down, gk_move_right),
				  (agent_set_animation, "$g_player", "anim_walk_forward_crouch", 0),
			  (else_try),
				(game_key_is_down, gk_move_forward),
				(game_key_is_down, gk_move_left),
				(neg|game_key_is_down, gk_move_backward),
				(neg|game_key_is_down, gk_move_right),
				  (agent_set_animation, "$g_player", "anim_rifle_walk_left_crouch_45", 0),
			  (else_try),
				(game_key_is_down, gk_move_left),
				(neg|game_key_is_down, gk_move_backward),
				(neg|game_key_is_down, gk_move_forward),
				(neg|game_key_is_down, gk_move_right),
				  (agent_set_animation, "$g_player", "anim_walk_left_crouch_90", 0),
			  (else_try),
				(game_key_is_down, gk_move_forward),
				(game_key_is_down, gk_move_right),
				(neg|game_key_is_down, gk_move_backward),
				(neg|game_key_is_down, gk_move_left),
				  (agent_set_animation, "$g_player", "anim_walk_right_crouch_45", 0),
			  (else_try),
				(game_key_is_down, gk_move_right),
				(neg|game_key_is_down, gk_move_backward),
				(neg|game_key_is_down, gk_move_left),
				(neg|game_key_is_down, gk_move_forward),
				  (agent_set_animation, "$g_player", "anim_walk_right_crouch_90", 0),
			  (else_try),
				(game_key_is_down, gk_move_backward),
				(neg|game_key_is_down, gk_move_right),
				(neg|game_key_is_down, gk_move_left),
				(neg|game_key_is_down, gk_move_forward),
				  (agent_set_animation, "$g_player", "anim_walk_backward_crouch", 0),
			  (else_try),
				(game_key_is_down, gk_move_backward),
				(game_key_is_down, gk_move_right),
				(neg|game_key_is_down, gk_move_left),
				(neg|game_key_is_down, gk_move_forward),
				  (agent_set_animation, "$g_player", "anim_walk_backward_crouch", 0),#reuse as not really obvious - krag
			  (else_try),
				(game_key_is_down, gk_move_backward),
				(game_key_is_down, gk_move_left),
				(neg|game_key_is_down, gk_move_right),
				(neg|game_key_is_down, gk_move_forward),
				  (agent_set_animation, "$g_player", "anim_walk_backward_crouch", 0),
			  (else_try),
				(agent_set_animation, "$g_player", "anim_player_crouch", 0),
			(try_end),
		(try_end),
        (try_begin),
          (agent_slot_eq, "$g_player", slot_agent_using_stimpak, 2),
          (agent_set_slot, "$g_player", slot_agent_using_stimpak, 3),
        (try_end),
        (try_begin),
          (key_clicked, "$key_quickfix"),
		  (store_agent_hit_points, ":health", "$g_player",0),
          (this_or_next|key_is_down, key_left_control),	#make cheaters use it
          (this_or_next|key_is_down, key_right_control),
          (lt,":health",100),
          (agent_get_horse, ":horse", "$g_player"),
          (eq, ":horse", -1),
          (neg|agent_slot_ge, "$g_player", slot_agent_using_stimpak, 1),
		  (neg|agent_slot_ge, "$g_player", slot_agent_gun_scope_on, 1), #can cause problems if activated with ironsights etc - krag
          (neg|agent_slot_ge, "$g_player", slot_agent_gun_aim_on, 1),
          (neq, ":cur_animation", "anim_syringe"),
          (neq, ":cur_animation", "anim_syringe2"),
          (neq, ":cur_animation", "anim_syringe3"),
          (neq, ":cur_animation", "anim_syringe4"),
          (neq, ":cur_animation", "anim_syringe5"),
          (neq, ":equipped", "itm_old_syringe"),
          (player_has_item, "itm_medkit"),
          (troop_get_inventory_capacity, ":inv_size", "trp_player"),
          (try_for_range, ":item_slot", 0, ":inv_size"),
            (troop_get_inventory_slot, ":item_no", "trp_player", ":item_slot"),
            (ge, ":item_no", 0),
            (eq, ":item_no", "itm_medkit"),
            (troop_inventory_slot_get_item_amount, ":cur_amount", "trp_player", ":item_slot"),
            (try_begin),
              (le, ":cur_amount", 1),
              (troop_remove_item, "trp_player", ":item_no"),
            (else_try),
              (val_sub, ":cur_amount", 1),
              (troop_inventory_slot_set_item_amount, "trp_player", ":item_slot", ":cur_amount"),
            (try_end),
            (display_message, "@You use a medi-kit", message_alert),
            (assign,":inv_size", -1),
          (try_end),

          (agent_set_slot, "$g_player", slot_agent_using_stimpak, 1),
          (agent_set_slot, "$g_player", slot_agent_gun_aim_on, 0),
          (agent_set_slot, "$g_player", slot_agent_gun_automatic_on, 0),
          (agent_set_slot, "$g_player", slot_agent_gun_ironsight_on, 0),
          (agent_set_slot, "$g_player", slot_agent_gun_scope_on, 0),
          (agent_get_slot, ":speed_modifier", "$g_player", slot_agent_speed_mod),
          (agent_set_speed_modifier, "$g_player", ":speed_modifier"),
        (try_end),
        (try_begin),
          (agent_slot_eq, "$g_player", slot_agent_using_stimpak, 1),

          # # (troop_clear_inventory, "trp_temp_troop"),
          # (try_for_range, ":item_slot", ek_item_0, ek_head),
          #   (troop_set_inventory_slot, "trp_temp_troop", ":item_slot", -1),
          # (try_end),

          # (assign, ":empty_slot", -1),
          # (try_for_range, ":item_slot", ek_item_0, ek_head),
          #   (agent_get_item_slot, ":item_no", "$g_player", ":item_slot"),
          #   (lt, ":item_no", 0),#find empty slot
          #   (assign, ":empty_slot", ":item_slot"),

          #   # (gt, ":item_no", 0),
          #   # (troop_get_inventory_slot_modifier, ":slot_item_imod", "trp_player", ":item_slot"),
          #   # (troop_set_inventory_slot, "trp_temp_troop", ":item_slot", ":item_no"),
          #   # (troop_set_inventory_slot_modifier, "trp_temp_troop", ":item_slot", ":slot_item_imod"),
          #   # (agent_unequip_item, "$g_player", ":item_no", ":item_slot"),
          # (try_end),
          # (try_begin),
          #   (gt, ":empty_slot", -1),#only use empty slot, otherwise no item added
          #   (agent_equip_item, "$g_player", "itm_old_syringe", ":empty_slot"),
          #   (agent_set_wielded_item, "$g_player", "itm_old_syringe"),
          # (try_end),
		  (agent_equip_item, "$g_player", "itm_syringe_glove", ek_gloves),
		  (try_begin),
				(agent_slot_eq, "$g_player", slot_agent_crouching, 1),
				(agent_set_animation, "$g_player", "anim_syringe", 1),
				(agent_set_slot, "$g_player", slot_agent_crouching, 1),
				(agent_set_speed_modifier, "$g_player", 40),
				# (agent_set_crouch_mode, "$g_player", 1),
				(agent_set_animation, "$g_player", "anim_player_crouch", 0),
			  (else_try),
				(agent_set_animation, "$g_player", "anim_syringe", 1),
		  (try_end),
          (agent_set_slot, "$g_player", slot_agent_using_stimpak, 2),
        (try_end),
        (try_begin),
          (eq, ":cur_animation", "anim_syringe4"),
          # (display_message,"@anim_syringe4"),
          (assign, ":one_second_check", "$g_one_hundredth_second_timer"),
          (val_mod, ":one_second_check", 100),
          (try_begin),
            (eq, ":one_second_check", 0),  ## true once every second

            (store_agent_hit_points, ":health", "$g_player",0),
            (neq,":health",100),
            (store_agent_hit_points, ":health", "$g_player",1),
            (val_add,":health",6),	#was 3, but too low
            # (val_min,":health",100),
            (agent_set_hit_points, "$g_player", ":health", 1),

          (try_end),
        (try_end),
        (neq, ":cur_animation", "anim_syringe"),
        (neq, ":cur_animation", "anim_syringe2"),
        (neq, ":cur_animation", "anim_syringe3"),
        (neq, ":cur_animation", "anim_syringe4"),
        (neq, ":cur_animation", "anim_syringe5"),
        (neg|agent_slot_eq, "$g_player", slot_agent_using_stimpak, 2),
        (try_begin),
          (agent_slot_eq, "$g_player", slot_agent_using_stimpak, 3),
          # (eq,":equipped","itm_old_syringe"),

          # (try_for_range, ":item_slot", ek_item_0, ek_head),
          #   (agent_get_item_slot, ":item_no", "$g_player", ":item_slot"),
          #   (gt, ":item_no", 0),
          #   (eq,":item_no","itm_old_syringe"),
          #   (agent_unequip_item, "$g_player", ":item_no", ":item_slot"),
          # (try_end),

          # (try_for_range, ":item_slot", ek_item_0, ek_head),
          #   (troop_get_inventory_slot, ":item_no", "trp_temp_troop", ":item_slot"),
          #   (gt, ":item_no", 0),
          #   (troop_get_inventory_slot_modifier, ":slot_item_imod", "trp_temp_troop", ":item_slot"),
          #   (agent_equip_item,"$g_player", ":item_no", ":item_slot", ":slot_item_imod"),
          # (try_end),
          # # (troop_clear_inventory, "trp_temp_troop"),
          # (try_for_range, ":item_slot", ek_item_0, ek_head),
          #   (troop_set_inventory_slot, "trp_temp_troop", ":item_slot", -1),
          # (try_end),

        # #bonus
		  (agent_unequip_item, "$g_player", "itm_syringe_glove", ek_gloves),
          (troop_get_inventory_slot, ":item_no", "trp_player", ek_gloves),
		  (try_begin),
            (gt, ":item_no", 0),
			(le, "$sneaked_into_town", disguise_none),
            (troop_get_inventory_slot_modifier, ":slot_item_imod", "trp_player", ek_gloves),
            (agent_equip_item,"$g_player", ":item_no", ek_gloves, ":slot_item_imod"),
          (try_end),
          (agent_set_slot, "$g_player", slot_agent_using_stimpak, 0),
        (try_end),

        #crouching
        (try_begin),
          (key_clicked, "$key_crouch"),
          (try_begin),
            (agent_slot_eq, "$g_player", slot_agent_crouching, 1),
            (agent_set_slot, "$g_player", slot_agent_crouching, 0),
            (agent_get_slot, ":speed_modifier", "$g_player", slot_agent_speed_mod),
            (agent_set_speed_modifier, "$g_player", ":speed_modifier"),
            # (agent_set_crouch_mode, "$g_player", 0),
            (agent_set_animation, "$g_player", "anim_walk_forward"),
          (else_try),
            (agent_get_horse, ":horse", "$g_player"),
            (le, ":horse", 0),
            (agent_set_slot, "$g_player", slot_agent_crouching, 1),
            (agent_set_speed_modifier, "$g_player", 40),
            # (agent_set_crouch_mode, "$g_player", 1),
            (agent_set_animation, "$g_player", "anim_player_crouch", 0),
          (try_end),
        (try_end),

        (try_begin),
          (agent_slot_eq, "$g_player", slot_agent_crouching, 1),
          (this_or_next|game_key_clicked, gk_action), #mounting horse, etc.
          (game_key_clicked, gk_jump),
          #(this_or_next|game_key_clicked, gk_jump),
         # (game_key_clicked, gk_kick),

          (agent_set_slot, "$g_player", slot_agent_crouching, 0),
          (agent_get_slot, ":speed_modifier", "$g_player", slot_agent_speed_mod),
          (agent_set_speed_modifier, "$g_player", ":speed_modifier"),
          # (agent_set_crouch_mode, "$g_player", 0),
          (agent_set_animation, "$g_player", "anim_walk_forward"),
        (else_try),
          (agent_slot_eq, "$g_player", slot_agent_crouching, 1),
          (agent_get_horse, ":horse", "$g_player"),
          (le, ":horse", 0),

          (agent_set_speed_modifier, "$g_player", 40),

          (try_begin),
            (game_key_is_down, gk_move_forward),
            (neg|game_key_is_down, gk_move_backward),
            (neg|game_key_is_down, gk_move_left),
            (neg|game_key_is_down, gk_move_right),

            # (agent_set_crouch_mode, "$g_player", 0),
            (try_begin),
              (gt, ":equipped", 0),
              (item_get_type, ":type", ":equipped"),
              (eq, ":type", itp_type_musket),
              (agent_set_animation, "$g_player", "anim_rifle_walk_crouch", 0),
            (else_try),
              (agent_set_animation, "$g_player", "anim_walk_forward_crouch", 0),
            (try_end),
          (else_try),
            (game_key_is_down, gk_move_forward),
            (game_key_is_down, gk_move_left),
            (neg|game_key_is_down, gk_move_backward),
            (neg|game_key_is_down, gk_move_right),

            # (agent_set_crouch_mode, "$g_player", 0),
            (try_begin),
              (gt, ":equipped", 0),
              (item_get_type, ":type", ":equipped"),
              (eq, ":type", itp_type_musket),
              (agent_set_animation, "$g_player", "anim_rifle_walk_left_crouch_45", 0),
            (else_try),
              (agent_set_animation, "$g_player", "anim_walk_left_crouch_45", 0),
            (try_end),
          (else_try),
            (game_key_is_down, gk_move_left),
            (neg|game_key_is_down, gk_move_backward),
            (neg|game_key_is_down, gk_move_forward),
            (neg|game_key_is_down, gk_move_right),

            # (agent_set_crouch_mode, "$g_player", 0),
            (try_begin),
              (gt, ":equipped", 0),
              (item_get_type, ":type", ":equipped"),
              (eq, ":type", itp_type_musket),
              (agent_set_animation, "$g_player", "anim_rifle_walk_left_crouch_90", 0),
            (else_try),
              (agent_set_animation, "$g_player", "anim_walk_left_crouch_90", 0),
            (try_end),
          (else_try),
            (game_key_is_down, gk_move_forward),
            (game_key_is_down, gk_move_right),
            (neg|game_key_is_down, gk_move_backward),
            (neg|game_key_is_down, gk_move_left),

            # (agent_set_crouch_mode, "$g_player", 0),
            (try_begin),
              (gt, ":equipped", 0),
              (item_get_type, ":type", ":equipped"),
              (eq, ":type", itp_type_musket),
              (agent_set_animation, "$g_player", "anim_rifle_walk_right_crouch_45", 0),
            (else_try),
              (agent_set_animation, "$g_player", "anim_walk_right_crouch_45", 0),
            (try_end),
          (else_try),
            (game_key_is_down, gk_move_right),
            (neg|game_key_is_down, gk_move_backward),
            (neg|game_key_is_down, gk_move_left),
            (neg|game_key_is_down, gk_move_forward),

            # (agent_set_crouch_mode, "$g_player", 0),
            (try_begin),
              (gt, ":equipped", 0),
              (item_get_type, ":type", ":equipped"),
              (eq, ":type", itp_type_musket),
              (agent_set_animation, "$g_player", "anim_rifle_walk_right_crouch_90", 0),
            (else_try),
              (agent_set_animation, "$g_player", "anim_walk_right_crouch_90", 0),
            (try_end),
          (else_try),
            (game_key_is_down, gk_move_backward),
            (neg|game_key_is_down, gk_move_right),
            (neg|game_key_is_down, gk_move_left),
            (neg|game_key_is_down, gk_move_forward),

            (try_begin),
              (gt, ":equipped", 0),
              (item_get_type, ":type", ":equipped"),
              (eq, ":type", itp_type_musket),
              (agent_set_animation, "$g_player", "anim_rifle_walk_backward_crouch", 0),
            (else_try),
              (agent_set_animation, "$g_player", "anim_walk_backward_crouch", 0),
            (try_end),
          (else_try),
            (game_key_is_down, gk_move_backward),
            (game_key_is_down, gk_move_right),
            (neg|game_key_is_down, gk_move_left),
            (neg|game_key_is_down, gk_move_forward),

            (try_begin),
              (gt, ":equipped", 0),
              (item_get_type, ":type", ":equipped"),
              (eq, ":type", itp_type_musket),
              (agent_set_animation, "$g_player", "anim_rifle_walk_backward_crouch", 0),
            (else_try),
              (agent_set_animation, "$g_player", "anim_walk_backward_crouch", 0),
            (try_end),
          (else_try),
            (game_key_is_down, gk_move_backward),
            (game_key_is_down, gk_move_left),
            (neg|game_key_is_down, gk_move_right),
            (neg|game_key_is_down, gk_move_forward),

            # (agent_set_crouch_mode, "$g_player", 0),
            (try_begin),
              (gt, ":equipped", 0),
              (item_get_type, ":type", ":equipped"),
              (eq, ":type", itp_type_musket),
              (agent_set_animation, "$g_player", "anim_rifle_walk_backward_crouch", 0),
            (else_try),
              (agent_set_animation, "$g_player", "anim_walk_backward_crouch", 0),
            (try_end),
          (else_try),
            # (neq, ":cur_animation_low", "anim_player_crouch"),
            # (agent_set_crouch_mode, "$g_player", 1),
            (agent_set_animation, "$g_player", "anim_player_crouch", 0),
          (try_end),
        (try_end),

        #flashblinded
        (try_begin),
          (agent_slot_eq, "$g_player", slot_agent_flashblinded, 1),
          (agent_get_position, pos0, "$g_player"),
          # (position_move_y, pos0, 80, 0),
          (agent_get_horse, ":horse", "$g_player"),
          (agent_get_animation, ":cur_animation_low", "$g_player", 0),

          (try_begin),
            (eq, ":horse", -1),
            (this_or_next|eq, ":cur_animation_low", "anim_stand_to_crouch"),
            (this_or_next|is_between, ":cur_animation_low", "anim_crouch_unarmed", "anim_reload_musket_full"),
            (this_or_next|is_between, ":cur_animation_low", "anim_walk_right_crouch_45", "anim_syringe"),
            (eq, ":cur_animation_low", "anim_walk_forward_crouch"),
            (position_move_z, pos0, 160, 1),
         (else_try),
             (gt, ":horse", 0),
             (position_move_z, pos0, 290, 1),
          (else_try),
            (position_move_z, pos0, 180, 1), #from 140
          (try_end),
          (particle_system_burst, "psys_explosion_flash", pos0, 1),
        (try_end),

        #dodge
        (try_begin),
          (key_clicked, "$key_dodge"),
          (neg|agent_slot_eq, "$g_player", slot_agent_gun_aim_on, 1),
          (agent_get_animation, ":cur_animation_low", "$g_player", 0),
          (neg|is_between, ":cur_animation_low", "anim_jump", "anim_stand_unarmed"), #cant roll when jumping
          (neg|agent_slot_eq, "$g_player", slot_agent_crouching, 1),
          # (agent_get_crouch_mode, ":crouching", "$g_player"),
          # (neq, ":crouching", 1), #not crouching
          (agent_get_horse, ":horse", "$g_player"),
          (eq, ":horse", -1),
          (try_begin),
            (agent_slot_ge, "$g_player", slot_agent_last_roll, 1),
            (display_message, "@You can't dodge again yet, improve your athletics skill.", message_alert),
          (try_end),
          (agent_slot_eq, "$g_player", slot_agent_last_roll, 0),

          (store_skill_level, ":athletics", skl_athletics),
          (store_sub, ":cooldown", 7, ":athletics"),
          (val_max, ":cooldown", 0),

          (try_begin),
            (game_key_is_down, gk_move_forward),
            (neg|game_key_is_down, gk_move_left),
            (neg|game_key_is_down, gk_move_right),
            (key_clicked, "$key_dodge"),
            (agent_set_animation, "$g_player", "anim_dodge_forward"), #dodge forward
            (agent_set_slot, "$g_player", slot_agent_last_roll, ":cooldown"),
          (else_try),
            (game_key_is_down, gk_move_forward),
            (game_key_is_down, gk_move_left),
            (key_clicked, "$key_dodge"),
            (agent_set_animation, "$g_player", "anim_dodge_left_forward"), #dodge left forward
            (agent_set_slot, "$g_player", slot_agent_last_roll, ":cooldown"),
          (else_try),
            (game_key_is_down, gk_move_forward),
            (game_key_is_down, gk_move_right),
            (key_clicked, "$key_dodge"),
            (agent_set_animation, "$g_player", "anim_dodge_right_forward"), #dodge right forward
            (agent_set_slot, "$g_player", slot_agent_last_roll, ":cooldown"),
          (else_try),
            (game_key_is_down, gk_move_left),
            (key_clicked, "$key_dodge"),
            (agent_set_animation, "$g_player", "anim_dodge_left"),  #dodge left
            (agent_set_slot, "$g_player", slot_agent_last_roll, ":cooldown"),
          (else_try),
            (game_key_is_down, gk_move_right),
            (key_clicked, "$key_dodge"),
            (agent_set_animation, "$g_player", "anim_dodge_right"),  #dodge left
            (agent_set_slot, "$g_player", slot_agent_last_roll, ":cooldown"),
          # (else_try),
            # (key_clicked, "$key_dodge"),
            # (agent_set_animation, "$g_player", "anim_dodge_forward"),
            # (agent_set_slot, "$g_player", slot_agent_last_roll, ":cooldown"),
          (try_end),
        (try_end),

        #zoom/ironsight/scope
        (try_begin),
          (game_key_is_down, gk_zoom),
          (try_begin), #scope on
            (game_key_clicked, gk_zoom),
            (agent_slot_eq, "$g_player", slot_agent_gun_scope_on, 0),
            (agent_slot_eq, "$g_player", slot_agent_gun_aim_on, 1),
			(gt, ":equipped", 0),
            (item_slot_ge, ":equipped", slot_item_has_scope, 0),

            (item_get_slot, ":reload_anim", ":equipped", slot_item_reload_animation),
            (neq, ":cur_animation", ":reload_anim"),

            (agent_set_slot, "$g_player", slot_agent_gun_scope_on, 1),

            (agent_get_slot, ":speed_modifier", "$g_player", slot_agent_speed_mod),
            (val_div,":speed_modifier",3),
            (agent_set_speed_modifier, "$g_player", ":speed_modifier"),
          (else_try), #scope off
            (game_key_clicked, gk_zoom),

            (agent_slot_eq, "$g_player", slot_agent_gun_scope_on, 1),
            (agent_set_slot, "$g_player", slot_agent_gun_scope_on, 2),
          (else_try), #ironsigh on
            (game_key_clicked, gk_zoom),
            (agent_slot_eq, "$g_player", slot_agent_gun_ironsight_on, 0),
            (agent_slot_eq, "$g_player", slot_agent_gun_aim_on, 1),
			(gt, ":equipped", 0),
            (item_slot_ge, ":equipped", slot_item_has_ironsight, 0),

            (item_get_slot, ":reload_anim", ":equipped", slot_item_reload_animation),
            (neq, ":cur_animation", ":reload_anim"),

            (agent_set_slot, "$g_player", slot_agent_gun_ironsight_on, 1),

            # (agent_get_slot, ":speed_modifier", "$g_player", slot_agent_speed_mod),
            # (val_div,":speed_modifier",3),
            # (agent_set_speed_modifier, "$g_player", ":speed_modifier"),
          (else_try), #ironsigh off
            (game_key_clicked, gk_zoom),

            (agent_slot_eq, "$g_player", slot_agent_gun_ironsight_on, 1),
            (agent_set_slot, "$g_player", slot_agent_gun_ironsight_on, 2),
          (else_try), #zoom
            (ge,":equipped",0),
            (neg|item_slot_ge, ":equipped", slot_item_has_ironsight, 1),
            (neg|item_slot_ge, ":equipped", slot_item_has_scope, 1),
            (eq, "$cam_mode", 0),

            (set_zoom_amount, 100),
            (assign, "$cam_mode", 2),
          (else_try),
            (lt,":equipped",0),
            (eq, "$cam_mode", 0),

            (set_zoom_amount, 100),
            (assign, "$cam_mode", 2),
          (try_end),
        (try_end),
        (try_begin),
          (eq, "$cam_mode", 2),
          (neg|game_key_is_down, gk_zoom),
          # # (eq, "$cam_mode", 2),
          (set_zoom_amount, 0),
          # (agent_set_visibility, "$g_player", 1),
          (assign, "$cam_mode", 0),
        (try_end),
        (try_begin), #use cam key to disable ironsight/scope
          (game_key_is_down, gk_cam_toggle),
          (this_or_next|agent_slot_eq, "$g_player", slot_agent_gun_ironsight_on, 1),
          (agent_slot_eq, "$g_player", slot_agent_gun_scope_on, 1),

          (agent_set_slot, "$g_player", slot_agent_gun_ironsight_on, 2),
          (agent_set_slot, "$g_player", slot_agent_gun_scope_on, 2),
        (try_end),
        #zoom end
        #scope
        (try_begin),
          (agent_slot_eq, "$g_player", slot_agent_gun_scope_on, 1),
          (agent_slot_eq, "$g_player", slot_agent_gun_aim_on, 1),
		  (gt, ":equipped", 0),
          (item_slot_ge, ":equipped", slot_item_has_scope, 0),

          (item_get_slot, ":reload_anim", ":equipped", slot_item_reload_animation),
          (neq, ":cur_animation", ":reload_anim"),

          (agent_set_visibility, "$g_player", 0),

          (agent_get_look_position, pos33, "$g_player"),
          (agent_get_bone_position, pos1, "$g_player", hb_hand_r, 1),
          (position_copy_rotation, pos1, pos33),
          (position_move_z, pos1, 10),
          # (item_get_slot, ":ironsight", ":equipped", slot_item_has_ironsight),

          (mission_cam_set_mode, 1),

          (mission_cam_set_position, pos1),

          (mission_cam_set_aperture, 1),
        (else_try),
          (agent_slot_eq, "$g_player", slot_agent_gun_scope_on, 2),

          (agent_set_slot, "$g_player", slot_agent_gun_scope_on, 0),
          (agent_set_visibility, "$g_player", 1),
          (mission_cam_set_mode, 0),
        (try_end),
        #ironsight
        (try_begin),
          (agent_slot_eq, "$g_player", slot_agent_gun_ironsight_on, 1),

          (agent_slot_eq, "$g_player", slot_agent_gun_aim_on, 1),
		  (gt, ":equipped", 0),
          (item_slot_ge, ":equipped", slot_item_has_ironsight, 0),

          (item_get_slot, ":reload_anim", ":equipped", slot_item_reload_animation),
          (neq, ":cur_animation", ":reload_anim"),

          (agent_set_visibility, "$g_player", 0),

          (agent_get_look_position, pos33, "$g_player"),
          (agent_get_bone_position, pos1, "$g_player", hb_hand_r, 1),
          (position_copy_rotation, pos1, pos33),
          (position_move_z, pos1, 10),
          (item_get_slot, ":ironsight", ":equipped", slot_item_has_ironsight),

		  (ge, ":ironsight", 0), #for script errors
          (scene_prop_get_num_instances, ":total", ":ironsight"),
          (try_begin),
            (gt, ":total",0),
            (try_for_range,":cur_instance",0,":total"),
              (scene_prop_get_instance, ":instance_id", ":ironsight", ":cur_instance"),
              (prop_instance_set_position, ":instance_id", pos1),
              # (prop_instance_animate_to_position, ":instance_id", pos1, 1),
              # (scene_prop_fade_in, ":instance_id", 1),
            (try_end),
          (else_try),
            (set_spawn_position, pos1),
            (spawn_scene_prop, ":ironsight"),
          (try_end),

          (mission_cam_set_mode, 1),

          (mission_cam_set_position, pos1),

          (mission_cam_set_aperture, 45),
        (else_try),
          (agent_slot_eq, "$g_player", slot_agent_gun_ironsight_on, 2),

		  (gt, ":equipped", 0),
          (item_slot_ge, ":equipped", slot_item_has_ironsight, 0),
          (item_get_slot, ":ironsight", ":equipped", slot_item_has_ironsight),

          (ge, ":ironsight", 0), #for script errors
		  (scene_prop_get_num_instances, ":total", ":ironsight"),
          (try_begin),
            (gt, ":total",0),
            (try_for_range,":cur_instance",0,":total"),
              (scene_prop_get_instance, ":instance_id", ":ironsight", ":cur_instance"),
              (prop_instance_get_position, pos1, ":instance_id"),
              (position_move_z, pos1, -10000),
              (prop_instance_set_position, ":instance_id", pos1),
              # (prop_instance_animate_to_position, ":instance_id", pos1, 1),
              # (scene_prop_fade_in, ":instance_id", 1),
            (try_end),
          (try_end),

          (agent_set_slot, "$g_player", slot_agent_gun_ironsight_on, 0),
          (agent_set_visibility, "$g_player", 1),
          (mission_cam_set_mode, 0),
        (try_end),

        #camera shake
        (try_begin),
          (neg|key_clicked, key_tilde),
          (neg|key_is_down, key_tilde),
          (gt, "$g_fate_cam_shake_frames", 0),

          (try_begin),
            (agent_get_horse, ":horse", "$g_player"), #tocan todo: fix on horse
            (eq, ":horse", -1),

            (call_script, "script_camera_shake"),
          (try_end),

          (val_sub, "$g_fate_cam_shake_frames", 1),

          (eq, "$g_fate_cam_shake_frames", 0),
          (init_position, pos_game_cam_store),

          (neg|agent_slot_eq, "$g_player", slot_agent_gun_ironsight_on, 1),
          (neg|agent_slot_eq, "$g_player", slot_agent_gun_scope_on, 1),

          (mission_cam_set_mode, 0, 0, 0),
        (try_end),

        #firearms
        (gt, ":equipped", 0),
        (item_get_type, ":type", ":equipped"),

        (try_begin),
          (is_between, ":equipped", firearms_begin, firearms_end),
          # (neq, ":equipped", "itm_rpg"),
          (this_or_next|eq, ":type", itp_type_pistol),
          (eq, ":type", itp_type_musket),

          (try_begin),
            (eq, "$g_ammo_unequip", 1),
            (call_script, "script_cf_player_ammo_check",1),
          (try_end),

          (item_get_slot, ":reload_anim", ":equipped", slot_item_reload_animation),
          (try_begin),
            (eq, ":cur_animation", ":reload_anim"),
            (agent_slot_ge, "$g_player", slot_agent_gun_ironsight_on, 1),

            (item_get_slot, ":ironsight", ":equipped", slot_item_has_ironsight),

            (ge, ":ironsight", 0), #for script errors
			(scene_prop_get_num_instances, ":total", ":ironsight"),
            (gt, ":total",0),
            # # (try_for_range,":cur_instance",0,":total"),
              (scene_prop_get_instance, ":instance_id", ":ironsight", 0),
              (prop_instance_get_position, pos1, ":instance_id"),
              (position_move_z, pos1, -10000),
              (prop_instance_set_position, ":instance_id", pos1),

              # (mission_cam_get_aperture, ":cam_aperture"),
              # (val_add,":cam_aperture",1),
              # (val_min,":cam_aperture",75),
              # (mission_cam_set_aperture, ":cam_aperture"),
              # # (prop_instance_animate_to_position, ":instance_id", pos1, 1),
              # # (scene_prop_fade_in, ":instance_id", 1),
              # # (agent_get_position, pos1, "$g_player"),
              # # (position_move_z, pos1, -30),
              # # (position_rotate_x, pos1, -90),
              # # (prop_instance_animate_to_position, ":instance_id", pos1, 50),
            # # (try_end),

            (agent_set_visibility, "$g_player", 1),
            (mission_cam_set_mode, 0),
          (else_try),
            (eq, ":cur_animation", ":reload_anim"),
            (agent_slot_ge, "$g_player", slot_agent_gun_scope_on, 1),

            (agent_set_visibility, "$g_player", 1),
            (mission_cam_set_mode, 0),
          (try_end),
          (neq, ":cur_animation", ":reload_anim"),

          (assign, ":reloading", 0),
          (agent_get_slot, ":clip_size", "$g_player", slot_agent_ammo_in_clip),
          (item_get_max_ammo, ":max_ammo", ":equipped"),

          (assign, ":ammo", -1),
          (assign, ":total_ammo", 0),
          (try_for_range, ":slot", 0, 4),
            (eq, ":ammo", -1),
            (agent_get_item_slot, ":s_item", "$g_player", ":slot"),
            (gt, ":s_item", 0),
            (item_get_type, ":item_type", ":s_item"),
            (eq, ":item_type", itp_type_bullets),
            (agent_get_ammo_for_slot, ":ammo_count", "$g_player", ":slot"),
            (gt, ":ammo_count", 0),
            (assign, ":ammo", ":s_item"),
          (try_end),
          (try_for_range, ":slot", 0, 4),	# This is to allow multiple slots of the same ammo type
            (agent_get_item_slot, ":s_item", "$g_player", ":slot"),
            (eq, ":s_item", ":ammo"),
            (agent_get_ammo_for_slot, ":ammo_count", "$g_player", ":slot"),
            (val_add, ":total_ammo", ":ammo_count"),
          (try_end),
          (try_begin),
            (eq, ":ammo", -1),
            (assign, ":ammo", "itm_pistol_ammo"),
          (try_end),

          (try_begin),
            (game_key_clicked, gk_kick),
            (try_begin),
              (neq, ":max_ammo", ":clip_size"),
              (neq, ":total_ammo", 0),

              (store_sub, ":sub_remaining", ":max_ammo", ":clip_size"),
              (val_max, ":sub_remaining", 0),
              (try_begin),
                (ge, ":total_ammo", ":max_ammo"),

                (val_sub, ":total_ammo", ":sub_remaining"),
                (agent_set_ammo, "$g_player", ":ammo", ":total_ammo"),
              (else_try),
                (assign, ":max_ammo", ":total_ammo"),
                (agent_set_ammo, "$g_player", ":ammo", 0),
              (try_end),
              (gt, ":max_ammo", 0),
              (assign, ":reloading", 1),

              # (try_begin),
                # (this_or_next|eq, ":equipped", "itm_webley"),
                # (this_or_next|eq, ":equipped", "itm_contender"),
                # (eq, ":equipped", "itm_sawedoff"),

                # (assign, ":shells", ":max_ammo"),

                # (val_sub, ":shells", ":sub_remaining"),
                # (val_add, ":shell", 1),

                # (try_for_range, reg0, 0, ":shells"),
                  # (particle_system_burst, ":shell", pos30, 1),
                # (try_end),
              # (try_end),

              (item_get_slot, ":reload_anim", ":equipped", slot_item_reload_animation),
              (assign, ":cur_animation", ":reload_anim"),
            (else_try),
              (eq, ":max_ammo", ":clip_size"),
              (display_message, "@Your weapon is topped off!", message_alert),
            (else_try),
              (eq, ":total_ammo", 0),
              (display_message, "@You're out of ammunition!", message_alert),
              (play_sound, "snd_firedry", sf_vol_15),
              (agent_set_kick_allowed, "$g_player", 1),
            (try_end),
          (try_end),

          (try_begin), #no ammo
            (eq, ":clip_size", 0),
            (try_begin),
              (eq, ":total_ammo", 0),
              (assign, ":max_ammo", 0),
              (this_or_next|key_clicked, key_left_mouse_button),
              (key_clicked, key_right_mouse_button),
              (play_sound, "snd_firedry"),
              (display_message, "@You're out of ammunition!", message_alert),
              (agent_set_slot, "$g_player", slot_agent_gun_aim_on, 0),
              (agent_set_slot, "$g_player", slot_agent_gun_automatic_on, 0),
              (try_begin),
                (agent_slot_eq, "$g_player", slot_agent_gun_ironsight_on, 1),
                (agent_set_slot, "$g_player", slot_agent_gun_ironsight_on, 2),
              (try_end),
              (try_begin),
                (agent_slot_eq, "$g_player", slot_agent_gun_scope_on, 1),
                (agent_set_slot, "$g_player", slot_agent_gun_scope_on, 2),
              (try_end),

              (agent_get_slot, ":speed_modifier", "$g_player", slot_agent_speed_mod),
              (agent_set_speed_modifier, "$g_player", ":speed_modifier"),
              # (item_get_slot, ":aim_anim", ":equipped", slot_item_ready_animation),
              # (item_get_slot, ":aim_loop_anim", ":equipped", slot_item_aim_loop_animation),
              # (item_get_slot, ":fire_anim", ":equipped", slot_item_fire_animation),
              (try_begin),
                (this_or_next|eq, ":cur_animation", "anim_pistol_ready"),
                (this_or_next|eq, ":cur_animation", "anim_pistol_ready_shield"),
                (this_or_next|eq, ":cur_animation", "anim_pistol_ready_2h"),
                (this_or_next|eq, ":cur_animation", "anim_pistol_fire"),
                (this_or_next|eq, ":cur_animation", "anim_pistol_fire_shield"),
                (this_or_next|eq, ":cur_animation", "anim_pistol_fire_2h"),
                (this_or_next|eq, ":cur_animation", "anim_pistol_fire_contd_shield"),
                (this_or_next|eq, ":cur_animation", "anim_pistol_fire_contd_2h"),
                (this_or_next|eq, ":cur_animation", "anim_pistol_aim"),
                (this_or_next|eq, ":cur_animation", "anim_pistol_aim_shield"),
                (this_or_next|eq, ":cur_animation", "anim_pistol_aim_2h"),
                (this_or_next|eq, ":cur_animation", "anim_rifle_ready"),
                (this_or_next|eq, ":cur_animation", "anim_rifle_ready_grip"),
                (this_or_next|eq, ":cur_animation", "anim_rifle_fire"),
                (this_or_next|eq, ":cur_animation", "anim_rifle_fire_grip"),
                (this_or_next|eq, ":cur_animation", "anim_rifle_aim_grip"),
                (this_or_next|eq, ":cur_animation", "anim_rifle_bolt_ready"),
                (this_or_next|eq, ":cur_animation", "anim_rifle_bolt_fire"),
                (this_or_next|eq, ":cur_animation", "anim_rifle_bolt_fire_contd"),
                (this_or_next|eq, ":cur_animation", "anim_rifle_bolt_aim"),
                #Mongol additions VVV
                (this_or_next|eq, ":cur_animation", "anim_shotgun_aim"),
                (this_or_next|eq, ":cur_animation", "anim_shotgun_fire"),
                (this_or_next|eq, ":cur_animation", "anim_shotgun_fire_contd"),
                (this_or_next|eq, ":cur_animation", "anim_rifle_higher_ready"),
                (this_or_next|eq, ":cur_animation", "anim_rifle_higher_fire"),
                #(this_or_next|eq, ":cur_animation", "anim_rifle_higher_fire_contd"),
                (this_or_next|eq, ":cur_animation", "anim_rifle_higher_aim"),
                (this_or_next|eq, ":cur_animation", "anim_rifle_semi_ready"),
                (this_or_next|eq, ":cur_animation", "anim_rifle_semi_fire"),
                #(this_or_next|eq, ":cur_animation", "anim_rifle_semi_fire_contd"),
                (this_or_next|eq, ":cur_animation", "anim_rifle_semi_aim"),
                (this_or_next|eq, ":cur_animation", "anim_type99_ready"),
                (this_or_next|eq, ":cur_animation", "anim_type99_fire"),
                (this_or_next|eq, ":cur_animation", "anim_type99_fire_contd"),
                (this_or_next|eq, ":cur_animation", "anim_type99_aim"),
                (this_or_next|eq, ":cur_animation", "anim_pistol_fire_2h_auto"),
                (this_or_next|eq, ":cur_animation", "anim_pistol_fire_2h_contd_auto"),
                (eq, ":cur_animation", "anim_rifle_aim"),
                (try_begin),
                  (neq,":shield_equipped",-1),
                  (eq,":type",itp_type_pistol),
                  (assign, ":end_anim", "anim_pistol_unready_shield"),
                (else_try),
                  (item_get_slot, ":end_anim", ":equipped", slot_item_end_animation),
                (try_end),
                # (item_get_slot, ":end_anim", ":equipped", slot_item_end_animation),
                (agent_set_animation, "$g_player", ":end_anim", 1),
              (try_end),
            (else_try),
              (ge, ":total_ammo", ":max_ammo"),
              (val_sub, ":total_ammo", ":max_ammo"),
              (agent_set_ammo, "$g_player", ":ammo", ":total_ammo"),
            (else_try),
              (assign, ":max_ammo", ":total_ammo"),
              (agent_set_ammo, "$g_player", ":ammo", 0),
            (try_end),
            (gt, ":max_ammo", 0),
            (assign, ":reloading", 1),

            (item_get_slot, ":reload_anim", ":equipped", slot_item_reload_animation),
            (assign, ":cur_animation", ":reload_anim"),
          (else_try), #shooting sys
            # (neq, ":cur_animation", ":reload_anim"),
            (gt, ":clip_size", 0),

            (try_begin),
              (game_key_clicked, gk_defend),
              (neg|game_key_is_down, gk_attack),
              (eq,":shield_equipped",-1),
              (try_begin),
                (agent_slot_eq, "$g_player", slot_agent_gun_aim_on, 0),
                (agent_set_slot, "$g_player", slot_agent_gun_aim_on, 1),

                (try_begin),
                  (eq,":type",itp_type_pistol),
                  (neq,":shield_equipped",-1),
                  (assign, ":aim_anim", "anim_pistol_ready_shield"),
                  # (item_get_slot, ":aim_anim", ":equipped", slot_item_ready_animation_alt),
                (else_try),
                  (item_get_slot, ":aim_anim", ":equipped", slot_item_ready_animation),
                (try_end),
                # (item_get_slot, ":aim_anim", ":equipped", slot_item_ready_animation),

                (agent_get_slot, ":speed_modifier", "$g_player", slot_agent_speed_mod),
                (try_begin),
                  (eq, ":type", itp_type_pistol),
                  (is_between, ":equipped", pistol_begin, smg_end),
                  (val_mul,":speed_modifier",75),
                  (val_div,":speed_modifier",100),
                (else_try),
                  (is_between, ":equipped", smg_begin, smg_end),
                  (val_mul,":speed_modifier",65),
                  (val_div,":speed_modifier",100),
                (else_try),
                   (is_between, ":equipped", mg_begin, mg_end),
                  (val_mul,":speed_modifier",30),
                  (val_div,":speed_modifier",100),
                (else_try),
                  (val_div,":speed_modifier",2),
                (try_end),
                # (val_mul,":speed_modifier",75),
                # (val_div,":speed_modifier",100),
                (agent_set_speed_modifier, "$g_player", ":speed_modifier"),

                (agent_set_animation, "$g_player", ":aim_anim", 1),
              (else_try),
                (agent_set_slot, "$g_player", slot_agent_gun_aim_on, 0),
                (agent_set_slot, "$g_player", slot_agent_gun_automatic_on, 0),
                (try_begin),
                  (agent_slot_eq, "$g_player", slot_agent_gun_ironsight_on, 1),
                  (agent_set_slot, "$g_player", slot_agent_gun_ironsight_on, 2),
                (try_end),
                (try_begin),
                  (agent_slot_eq, "$g_player", slot_agent_gun_scope_on, 1),
                  (agent_set_slot, "$g_player", slot_agent_gun_scope_on, 2),
                (try_end),

                (try_begin),
                  (neq,":shield_equipped",-1),
                  (eq,":type",itp_type_pistol),
                  (assign, ":end_anim", "anim_pistol_unready_shield"),
                  # (item_get_slot, ":end_anim", ":equipped", slot_item_end_animation_alt),
                (else_try),
                  (item_get_slot, ":end_anim", ":equipped", slot_item_end_animation),
                (try_end),
                # (item_get_slot, ":end_anim", ":equipped", slot_item_end_animation),
                (agent_set_animation, "$g_player", ":end_anim", 1),

                (agent_get_slot, ":speed_modifier", "$g_player", slot_agent_speed_mod),
                (agent_set_speed_modifier, "$g_player", ":speed_modifier"),

                (try_begin),
                  (this_or_next|eq, ":equipped", "itm_flamethrower_union"),
                  (eq, ":equipped", "itm_flamethrower"),
                  (play_sound, "snd_flamer_idle"),
                (else_try),
                  (this_or_next|eq, ":equipped", "itm_pistol_plasma"),
                  (eq, ":equipped", "itm_rifle_plasma"),
                  (play_sound, "snd_rifleplasma_idle"),
                (try_end),
              (try_end),
            (try_end),

            (try_begin),
              (game_key_clicked, gk_attack),
              (agent_slot_eq, "$g_player", slot_agent_gun_aim_on, 1),
              (try_begin),
                (ge, ":time", "$guns_not_load_until"),
                (item_get_hit_points, ":frequency", ":equipped"),
                # (val_clamp,":frequency",500,1001),
                (store_add, "$guns_not_load_until", ":time", ":frequency"),
                # (store_add, "$guns_not_load_until", ":time", 1000), #1000 #frequency#
                (assign, "$guns_cant_fire_until", ":time"),
              (else_try),
                (assign, "$guns_cant_fire_until", -1),
              (try_end),
            (try_end),

            (try_begin),
              (game_key_is_down, gk_attack),
              (try_begin),
                (agent_slot_eq, "$g_player", slot_agent_gun_aim_on, 1),
                (agent_slot_eq, "$g_player", slot_agent_gun_automatic_on, 0),
                (neq, "$guns_cant_fire_until", -1),
                (ge, ":time", "$guns_cant_fire_until"),

                # (item_get_food_quality, ":num_missiles", ":equipped"),
                # (item_get_max_ammo, ":consumption", ":equipped"),
                # (val_mul, ":consumption", ":num_missiles"),
                # (ge, ":ammo", ":consumption"),

                (agent_set_slot, "$g_player", slot_agent_gun_automatic_on, 1),
              (try_end),
            (else_try),
              (agent_slot_eq, "$g_player", slot_agent_gun_automatic_on, 1),
              (agent_set_slot, "$g_player", slot_agent_gun_automatic_on, 0),
            (try_end),

            (try_begin),  #pistol + shield
              (game_key_clicked, gk_attack),
              (neg|game_key_is_down, gk_defend),
              (neq,":shield_equipped",-1),
              (agent_slot_eq, "$g_player", slot_agent_gun_aim_on, 0),
              (agent_set_slot, "$g_player", slot_agent_gun_aim_on, 1),
              (assign, ":aim_anim", "anim_pistol_ready_shield"),
              # (item_get_slot, ":aim_anim", ":equipped", slot_item_ready_animation),

              (agent_get_slot, ":speed_modifier", "$g_player", slot_agent_speed_mod),
              (val_mul,":speed_modifier",75),
              (val_div,":speed_modifier",100),
              (agent_set_speed_modifier, "$g_player", ":speed_modifier"),

              (agent_set_animation, "$g_player", ":aim_anim", 1),
            (try_end),

            (try_begin),  #pistol + shield
              (game_key_clicked, gk_defend),
              (neg|game_key_is_down, gk_attack),
              (neq,":shield_equipped",-1),
              (agent_set_slot, "$g_player", slot_agent_gun_aim_on, 0),
              (agent_set_slot, "$g_player", slot_agent_gun_automatic_on, 0),
              (try_begin),
                (agent_slot_eq, "$g_player", slot_agent_gun_ironsight_on, 1),
                (agent_set_slot, "$g_player", slot_agent_gun_ironsight_on, 2),
              (try_end),
              (try_begin),
                (agent_slot_eq, "$g_player", slot_agent_gun_scope_on, 1),
                (agent_set_slot, "$g_player", slot_agent_gun_scope_on, 2),
              (try_end),

              (assign, ":end_anim", "anim_pistol_unready_shield"),
              # (item_get_slot, ":end_anim", ":equipped", slot_item_end_animation),
              (agent_set_animation, "$g_player", ":end_anim", 1),

              (agent_get_slot, ":speed_modifier", "$g_player", slot_agent_speed_mod),
              (agent_set_speed_modifier, "$g_player", ":speed_modifier"),

              (try_begin),
                (this_or_next|eq, ":equipped", "itm_flamethrower_union"),
                (eq, ":equipped", "itm_flamethrower"),
                (play_sound, "snd_flamer_idle"),
              (try_end),
            (try_end),

#############################
            #Autofire
            (try_begin),
              (agent_slot_eq, "$g_player", slot_agent_gun_aim_on, 1),

			  (try_begin),
				(neg|is_camera_in_first_person),
				(agent_get_horse, ":mount","$g_player"),
				(le, ":mount", -1),

				(agent_get_position, pos0, "$g_player"),
			    (position_get_distance_to_ground_level, ":ground_dist", pos0),
				(agent_get_look_position, pos33, "$g_player"),
				(position_copy_rotation, pos0, pos33),
				(agent_get_animation, ":cur_leg_animation", "$g_player", 0),

				(try_begin),
				    #(gt, ":ground_dist", 0),
					(le, ":ground_dist", 20), #falling anim starts at 630 accroding to dalion.
					(neq, ":cur_leg_animation", "anim_jump"),
					(neq, ":cur_leg_animation", "anim_jump_loop"),
					(agent_set_position, "$g_player", pos0),
				  (else_try),
					(agent_set_no_dynamics, "$g_player", 1),
					(try_begin),
						(gt, ":ground_dist", 20),
						(neq, ":cur_leg_animation", "anim_jump"),
						(neq, ":cur_leg_animation", "anim_jump_loop"),
						(position_move_z, pos0, -2, 1),	#stop walking in the air - krag
					  (else_try),
						(lt, ":ground_dist", 0),
						(position_set_z_to_ground_level, pos0),
					(try_end),
					(agent_set_position, "$g_player", pos0),
					(agent_set_no_dynamics, "$g_player", 0),
				(try_end),
			  (try_end),

			  # (item_get_slot, ":aim_anim", ":equipped", slot_item_ready_animation),
			  (try_begin), #pistol+shield
				(neq,":shield_equipped",-1),
				(eq,":type",itp_type_pistol),
				(assign, ":aim_loop_anim", "anim_pistol_aim_shield"),
				(assign, ":fire_anim", "anim_pistol_fire_shield"),
				# (item_get_slot, ":aim_loop_anim", ":equipped", slot_item_aim_loop_animation_alt),
				# (item_get_slot, ":fire_anim", ":equipped", slot_item_fire_animation_alt),
			  (else_try),
				(item_get_slot, ":aim_loop_anim", ":equipped", slot_item_aim_loop_animation),
				(item_get_slot, ":fire_anim", ":equipped", slot_item_fire_animation),
			  (try_end),

              (neq, ":cur_animation", "anim_pistol_ready"),
              (neq, ":cur_animation", "anim_pistol_ready_shield"),
              (neq, ":cur_animation", "anim_pistol_ready_2h"),
              (neq, ":cur_animation", "anim_pistol_fire"),
              (neq, ":cur_animation", "anim_pistol_fire_shield"),
              (neq, ":cur_animation", "anim_pistol_fire_2h"),
              (neq, ":cur_animation", "anim_pistol_fire_contd_shield"),
              (neq, ":cur_animation", "anim_pistol_fire_contd_2h"),
              (neq, ":cur_animation", "anim_pistol_aim"),
              (neq, ":cur_animation", "anim_pistol_aim_shield"),
              (neq, ":cur_animation", "anim_pistol_aim_2h"),


              (neq, ":cur_animation", "anim_rifle_ready"),
              (neq, ":cur_animation", "anim_rifle_ready_grip"),
              (neq, ":cur_animation", "anim_rifle_fire"),
              (neq, ":cur_animation", "anim_rifle_fire_grip"),
              (neq, ":cur_animation", "anim_rifle_aim"),
              (neq, ":cur_animation", "anim_rifle_aim_grip"),
              (neq, ":cur_animation", "anim_rifle_bolt_ready"),
              (neq, ":cur_animation", "anim_rifle_bolt_fire"),
              (neq, ":cur_animation", "anim_rifle_bolt_fire_contd"),
              (neq, ":cur_animation", "anim_rifle_bolt_aim"),


                # - Mongol edits VVV
              (neq, ":cur_animation",  "anim_shotgun_aim"),
              (neq, ":cur_animation",  "anim_shotgun_fire"),
              (neq, ":cur_animation",  "anim_shotgun_fire_contd"),
              (neq, ":cur_animation", "anim_rifle_higher_ready"),
              (neq, ":cur_animation", "anim_rifle_higher_fire"),
              #(neq, ":cur_animation", "anim_rifle_higher_fire_contd"),
              (neq, ":cur_animation", "anim_rifle_higher_aim"),
              (neq, ":cur_animation", "anim_rifle_semi_ready"),
              (neq, ":cur_animation", "anim_rifle_semi_fire"),
              #(neq, ":cur_animation", "anim_rifle_semi_fire_contd"),
              (neq, ":cur_animation", "anim_rifle_semi_aim"),
              (neq, ":cur_animation", "anim_type99_ready"),
              (neq, ":cur_animation", "anim_type99_fire"),
              (neq, ":cur_animation", "anim_type99_fire_contd"),
              (neq, ":cur_animation", "anim_type99_aim"),
              (neq, ":cur_animation", "anim_pistol_fire_2h_auto"),
              (neq, ":cur_animation", "anim_pistol_fire_2h_contd_auto"),
              #  (eq, ":cur_animation", "anim_rifle_aim"),

              # (neq, ":cur_animation", ":aim_anim"),
              # (neq, ":cur_animation", ":aim_loop_anim"),
              # (neq, ":cur_animation", ":fire_anim"),
              (agent_set_animation, "$g_player", ":aim_loop_anim", 1),
            (try_end),

            (try_begin),
              (agent_slot_eq, "$g_player", slot_agent_gun_automatic_on, 1),
              # (item_get_food_quality, ":num_missiles", ":equipped"),
              # (item_get_max_ammo, ":consumption", ":equipped"),
              # (val_mul, ":consumption", ":num_missiles"),
              (try_begin),
                # (ge, ":ammo", ":consumption"),
                (agent_get_slot, ":last_time", "$g_player", slot_agent_last_time_shot),
                (item_get_hit_points, ":frequency", ":equipped"),
				(try_begin),
					(gt, ":equipped", 0),
					(item_slot_eq, ":equipped", slot_item_has_autofire, 1),
					(agent_slot_ge, "$g_player", slot_agent_gun_scope_on, 1),
					(val_mul, ":frequency", 5),	#make slower if using scope and autofire, to simulate switching to semi auto - krag
				(try_end),
                (store_add, ":next_time", ":last_time", ":frequency"),
                (try_begin),
                  (ge, ":time", ":next_time"),
                  (agent_set_slot, "$g_player", slot_agent_last_time_shot, ":time"),

                  (try_begin),
					(gt, ":equipped", 0),
					(this_or_next|agent_slot_ge, "$g_player", slot_agent_gun_scope_on, 1),#stop autofire when using full scope - krag
                    (item_slot_eq, ":equipped", slot_item_has_autofire, -1),
                    (agent_set_slot, "$g_player", slot_agent_gun_automatic_on, 0),
                    (assign, "$guns_cant_fire_until", -1),
                  (try_end),

                  (agent_get_slot, ":effective_shots", "$g_player", slot_agent_effective_shots),
                  (val_add, ":effective_shots", 1),


                  (agent_set_slot, "$g_player", slot_agent_effective_shots, ":effective_shots"),

                  # (val_sub, ":ammo", 1),
                  # (val_sub, ":ammo", ":consumption"),
                  # (agent_set_ammo,"$g_player", ":ammo_type", ":ammo"),

                  (try_begin),
                    (neg|agent_slot_ge, "$g_player", slot_agent_gun_scope_on, 1),
                    (neg|agent_slot_ge, "$g_player", slot_agent_gun_ironsight_on, 1),

                    (agent_get_bone_position, pos0, "$g_player", hb_item_r, 1),
                    (copy_position, pos30, pos0),
                    (copy_position, pos31, pos0),
                    (agent_get_look_position, pos33, "$g_player"),
                    (position_copy_rotation, pos0, pos33),

                    (item_get_weapon_length, ":length", ":equipped"),
                    (position_move_y, pos0, ":length"),
                    (position_move_z, pos0, 10),
                  (else_try),
                    (mission_cam_get_position, pos0),

                    (position_move_z, pos0, -2), #was 10
                  (try_end),

                  # # (agent_get_bone_position, pos0, "$g_player", hb_item_r, 1),
                  # # (copy_position, pos30, pos0),
                  # # # (agent_get_bone_position, pos30, "$g_player", hb_hand_r, 1),
                  # # (agent_get_look_position, pos33, "$g_player"),
                  # # (position_copy_rotation, pos0, pos33),
                  # # # (position_copy_rotation, pos30, pos33),

                  # # (try_begin),
                    # # (neg|agent_slot_ge, "$g_player", slot_agent_gun_scope_on, 1),
                    # # (neg|agent_slot_ge, "$g_player", slot_agent_gun_ironsight_on, 1),
                    # # (item_get_weapon_length, ":length", ":equipped"),
                    # # (position_move_y, pos0, ":length"),
                    # # (position_move_z, pos0, 10),
                    # # # (position_move_z, pos0, 25),
                  # # (else_try),
                    # # (position_move_y, pos0, 10),
                    # # (position_move_z, pos0, 10),
                  # # (try_end),

                  (assign, ":shell", -1),
                  (try_begin),
                    (eq, ":type", itp_type_pistol),
                    (is_between, ":equipped", pistol_begin, smg_end),

                    (assign, ":shell", "psys_shell_pistol"),
                    (position_move_x, pos30, 5),
                    (position_move_y, pos30, 10),
                  (else_try),
                    (is_between, ":equipped", smg_begin, smg_end),

                    (assign, ":shell", "psys_shell_pistol"),
                    (position_move_x, pos30, -10),
                    (position_move_y, pos30, 20),
                  (else_try),
                    (this_or_next|is_between, ":equipped", sniper_begin, sniper_end),
                    (this_or_next|is_between, ":equipped", rifle_begin, rifle_end),
                    (this_or_next|is_between, ":equipped", lmg_begin, lmg_end),
                    (is_between, ":equipped", a_rifle_begin, a_rifle_end),

                    (assign, ":shell", "psys_shell_rifle"),
                    (position_move_x, pos30, -10),
                    (position_move_y, pos30, 20),
                  (else_try),
                    (is_between, ":equipped", shotgun_begin, shotgun_end),

                    (assign, ":shell", "psys_shell_shotgun"),
                    (position_move_x, pos30, -10),
                    (position_move_y, pos30, 20),
                  (else_try),
                    (is_between, ":equipped", mg_begin, mg_end),

                    (assign, ":shell", "psys_shell_rifle"),
                    (position_move_x, pos30, -10),
                    (position_move_y, pos30, 20),
                  (try_end),
                  (item_get_slot, ":particle", ":equipped", slot_item_particle),
                  (item_get_slot, ":particle_strength", ":equipped", slot_item_particle_strength),
                  (item_get_food_quality, ":pew", ":equipped"),

                  (try_begin),
                    (this_or_next|eq, ":ammo", "itm_flameammo_burst"),
                    (this_or_next|eq, ":ammo", "itm_flameshot_ammo"),
                    (this_or_next|eq, ":ammo", "itm_flameshot_ammo_pw"),
                    (this_or_next|eq, ":ammo", "itm_buckshot_ammo"),
                    (eq, ":ammo", "itm_buckshot_ammo_pw"),
                    (assign, ":missile_speed", 16000),#was 5k, too slow - krag #was 10k, but changed to same as actual shot
                    (assign, ":num_missiles", 9),
                  (else_try),
                    (eq, ":ammo", "itm_flameammo"),
                    (assign, ":missile_speed", 1500),
                    (assign, ":num_missiles", 4),
                  (else_try),
                    (item_get_thrust_damage, ":missile_speed", ":equipped"),
                    (val_mul, ":missile_speed", 500),
                    (val_max, ":missile_speed", 10000),
                    (val_min, ":missile_speed", 20000),
					(try_begin),
						(agent_slot_ge, "$g_player", slot_agent_gun_scope_on, 1), #increase speed when using scopes to avoid player frustration - krag
						(gt, ":equipped", 0),
						(item_slot_ge, ":equipped", slot_item_has_scope, 1),
						(item_get_accuracy, ":accuracy", ":equipped"),
						(val_mul, ":accuracy", 500),
						(val_add, ":missile_speed", ":accuracy"),
					(try_end),
					#(assign, reg9,  ":missile_speed"),
					#(display_message, "@missile_speed {reg9}"),
                    (assign, ":num_missiles", 1),
                  (try_end),

                  (call_script, "script_gun_calculate_dispersion", "$g_player", ":equipped"),
                  (assign, ":dispersion", reg0),
                  #(assign, ":dispersion", 0),#testing with no dispersion
                   #(display_message, "@Dispersion final: {reg0}"),
                   #(display_message, "@Dispersion: base:{reg10}, shots:{reg11}, recoil:{reg21}, {reg12}, skill:{reg13}, speed:{reg14}, scope:{reg15}"),
                   #(display_message, "@ANIM:{reg0}"),#final

                  (try_begin),
                    (neq, ":cur_animation", ":fire_anim"),
                    (agent_set_animation, "$g_player", ":fire_anim", 1),
                  (try_end),

                  (try_for_range, ":unused", 0, ":num_missiles"),
                    (copy_position, pos1, pos0),
                    (call_script, "script_rnd", 0, 36000),
                    (position_rotate_y_floating, pos1, reg0),
                    (call_script, "script_rnd", 0, ":dispersion"),
					#(display_message, "@rnd {reg0}"),	#test
                    (position_rotate_x_floating, pos1, reg0),
                    (add_missile, "$g_player", pos1, ":missile_speed", ":equipped", 0, ":ammo", 0),
					(try_begin),
						(agent_slot_ge, "$g_player", slot_agent_gun_scope_on, 1),
						#(item_has_property, ":equipped", itp_has_bayonet),	#if an automatic using a scope for semi auto then multiply affective shots to stop semi auto spam with no recoil
						(gt, ":equipped", 0),
						(item_slot_eq, ":equipped", slot_item_has_autofire, 1),
						(agent_get_slot, ":effective_shots", "$g_player", slot_agent_effective_shots),
						(val_add, ":effective_shots", 6),
						(agent_set_slot, "$g_player", slot_agent_effective_shots, ":effective_shots"),
					(try_end),
					# (try_begin),
						# #robbery/rescue alert when shooting # not working
						# #(display_message, "@robbery/rescue alert when shooting"),
						# (this_or_next|eq,"$robbery_in_progress",1),
						# (this_or_next|eq, "$talk_context", tc_prison_break),
						# (this_or_next|party_slot_eq, "$current_town", slot_center_has_attacker,3),#make it work during bandit attack
						# (eq, "$talk_context", tc_escape),
						# #(display_message, "@robbery/rescue alert when shooting 2"),
						# (try_begin),
							# (cast_ray, ":unused", pos22, pos1), #doesn't seem to return the correct position?
						# (try_end),
						# (set_spawn_position, pos22),
						# (spawn_scene_prop, "spr_lightbulb"),
						# (display_message, "@robbery/rescue alert when shooting 3"),
						# (call_script, "script_hit_alerts_guards_panicks_civilians", "$g_player", ":ammo"),#needs target in pos12
					# (try_end),
                  (try_end),

                  (play_sound_at_position, ":pew", pos0, sf_vol_4),

                  (try_begin),
                    (gt, ":particle", 0),
                    #(neg|agent_slot_ge, "$g_player", slot_agent_gun_scope_on, 1),
                    (try_begin),
                      (agent_slot_ge, "$g_player", slot_agent_gun_scope_on, 1),
					  (position_move_y, pos0, 90),
					  (position_move_z, pos0, -4, 0),
					  #(position_move_x, pos0, 1, 0),
					   #(particle_system_burst, "psys_food_steam", pos0, 5),
                    (else_try),
					  (agent_slot_ge, "$g_player", slot_agent_gun_ironsight_on, 1),
                      (item_get_weapon_length, ":length", ":equipped"),
                      (position_move_y, pos0, ":length"),
                      #(position_move_z, pos0, -8), #was 10
					  (try_begin),
                        (eq, ":type", itp_type_pistol),
                        (position_move_y, pos0, 30),
                        (position_move_z, pos0, 7),
					   (else_try),
						(position_move_z, pos0, -8),
                      (try_end),
                    (else_try),
                      (try_begin),
                        (eq, ":type", itp_type_pistol),
                        (position_move_z, pos0, 15),
                        # (position_move_z, pos0, 25),
                      (else_try),
                        (position_move_z, pos0, 5),
                        # (position_move_z, pos0, 15),
                        (position_move_x, pos0, -5),
                      (try_end),
                    (try_end),
                    (particle_system_burst, ":particle", pos0, ":particle_strength"),
					(try_begin),
                        (neq, ":ammo", "itm_plasma_ammo"),
                        (neq, ":ammo", "itm_flameammo"),
                        (particle_system_burst, "psys_food_steam", pos0, 1),
                    (try_end),
                  (try_end),
                  (try_begin),
                    (neg|agent_slot_ge, "$g_player", slot_agent_gun_scope_on, 1),
                    (neg|agent_slot_ge, "$g_player", slot_agent_gun_ironsight_on, 1),
                    (gt, ":shell", 0),
                    (particle_system_burst, ":shell", pos30, 1),
                  (try_end),

                  (try_begin),
                    (this_or_next|eq, ":equipped", "itm_flamethrower_vitzland_pistol"),
                    (this_or_next|eq, ":equipped", "itm_flamethrower_vitzland"),
                    (this_or_next|eq, ":equipped", "itm_flamethrower_union"),
                    (eq, ":equipped", "itm_flamethrower"),
                    # (assign, ":one_msecond_check", "$g_one_hundredth_second_timer"),
                    # (val_mod, ":one_msecond_check", 10),
                    # (try_begin),
                      # (eq, ":one_msecond_check", 0),
                      (call_script, "script_flamer_fire", pos0, "$g_player"),
                    # (try_end),
                  (try_end),

                  (val_sub, ":clip_size", 1),

                  # (item_get_hit_points, reg1, ":equipped"),
                  # (item_get_accuracy, ":accuracy", ":equipped"),
                  # (store_sub,reg2,100,":accuracy"),
                  # (assign,reg3,":missile_speed"),
                  # (display_message, "@Accuracy {reg2}^^Shoot Frequency {reg1}^^Shoot Speed {reg3}"),
                (try_end),
              (else_try),
                (agent_set_slot, "$g_player", slot_agent_gun_automatic_on, 0),
              (try_end),
            (else_try),#spread cool down
              (agent_get_slot, ":last_time", "$g_player", slot_agent_last_time_shot_recover),
              (item_get_hit_points, ":frequency", ":equipped"),
			  # (try_begin),
					# (item_slot_eq, ":equipped", slot_item_has_autofire, 1),
					# (agent_slot_ge, "$g_player", slot_agent_gun_scope_on, 1),
					# (val_div, ":frequency", 10),	#simulate switching to semi auto - krag
			  # (try_end),
              (val_div, ":frequency", 2),
              (store_add, ":next_time", ":last_time", ":frequency"),
              (ge, ":time", ":next_time"),
              (agent_set_slot, "$g_player", slot_agent_last_time_shot_recover, ":time"),
              (agent_get_slot, ":effective_shots", "$g_player", slot_agent_effective_shots),
              (gt, ":effective_shots", 0),
              (val_sub, ":effective_shots", 1),
              (agent_set_slot, "$g_player", slot_agent_effective_shots, ":effective_shots"),
            (try_end),
          (try_end),

          (try_begin),
            (eq, ":reloading", 1),
            (assign, ":clip_size", ":max_ammo"),
            (item_get_slot, ":reload_anim", ":equipped", slot_item_reload_animation),
            (item_get_slot, ":reload_sound", ":equipped", slot_item_reload_sound),
            (agent_set_animation, "$g_player", ":reload_anim", 1),

            #ironsight remove gun
            (try_begin),
              (agent_slot_ge, "$g_player", slot_agent_gun_ironsight_on, 1),

              (item_get_slot, ":ironsight", ":equipped", slot_item_has_ironsight),
			  (try_begin),
				  (gt, ":ironsight",0),
				  (scene_prop_get_num_instances, ":total", ":ironsight"),
				  (try_begin),
					(gt, ":total",0),
					(try_for_range,":cur_instance",0,":total"),
					  (scene_prop_get_instance, ":instance_id", ":ironsight", ":cur_instance"),
					  (prop_instance_get_position, pos1, ":instance_id"),
					  (position_move_z, pos1, -10000),
					  (prop_instance_set_position, ":instance_id", pos1),
					  # (prop_instance_animate_to_position, ":instance_id", pos1, 1),
					  # (scene_prop_fade_in, ":instance_id", 1),
					(try_end),
				  (try_end),
              (try_end),
            (try_end),

            #reload sounds
            (try_begin),
              (neq,":reload_sound",-1),
              (play_sound, ":reload_sound"),
            (try_end),

           (try_begin),
               (eq, ":equipped", "itm_rifle_m1_garand"),

               # (position_move_y, pos0, 30),
               # (position_move_z, pos0, 7),

               (particle_system_burst, "psys_enbloc_clip", pos31, 1),
           (try_end),

          (try_end),

          (agent_set_slot, "$g_player", slot_agent_ammo_in_clip, ":clip_size"),
        # (else_try),#binoculars
          # (eq, ":equipped", itm_binoculars),
          # (game_key_clicked, gk_defend),
        (try_end),
          ]),

    #animals
    (ti_on_agent_dismount, 0, 0, [
          (eq, "$g_animal_present", 1),
      ], [
          (store_trigger_param_1, ":agent_id"),
          (agent_slot_ge, ":agent_id", slot_agent_rides_x, 0),
          # (agent_slot_ge, ":agent_id", slot_agent_rides_animal, 0),
          (agent_get_troop_id, ":agent_troop_id", ":agent_id"),
          (troop_slot_eq, ":agent_troop_id", slot_troop_is_animal, 1),

          (store_trigger_param_2, ":horse_agent_id"),

          (agent_is_alive,":agent_id"),
          (agent_deliver_damage_to_agent, ":agent_id", ":agent_id", 10000),
          (agent_is_alive,":horse_agent_id"),
          (agent_deliver_damage_to_agent, ":horse_agent_id", ":horse_agent_id", 10000),

      ]),

    (0, 0, 0,
      [
        (eq, "$g_animal_present", 1),
        (eq, "$g_new_animal", 1),
      ],
      [
        (call_script, "script_init_animals"),
      ]),

    #bleed/flash
    (5, 0.0, 0.0,
      [(neg|conversation_screen_is_active),],[

        (call_script,"script_tocan_bleeding"),

        (try_begin),
          (eq, "$flashbang_thrown", 1),
          (assign,":found",0),
          (try_for_agents, ":agent_id"),
            (agent_is_alive, ":agent_id"),
            (agent_slot_eq, ":agent_id", slot_agent_flashblinded, 1),
            (assign,":found",1),
			(store_random_in_range, ":rand_smoke", 0, 4),
			(eq, ":rand_smoke", 3),
            (agent_get_slot, ":accuracy_mod", ":agent_id", slot_agent_accuracy_mod),
            (agent_set_accuracy_modifier, ":agent_id", ":accuracy_mod"),
            (agent_set_slot, ":agent_id", slot_agent_flashblinded, 0),
          (try_end),
          (neq,":found",1),
          (assign, "$flashbang_thrown", 0),
        (try_end),

        (try_begin),
          (eq, "$smokeg_thrown", 1),
          (assign,":found",0),
          (try_for_agents, ":agent_id"),
            (agent_slot_eq, ":agent_id", slot_agent_smokecover, 1),
            (agent_is_alive, ":agent_id"),
            (assign,":found",1),
			(store_random_in_range, ":rand_smoke", 0, 4),
			(eq, ":rand_smoke", 3),
            (agent_set_slot, ":agent_id", slot_agent_smokecover, 0),
          (try_end),
          (neq,":found",1),
          (assign, "$smokeg_thrown", 0),
        (try_end),

        (try_begin),
          (eq, "$agent_on_fire", 1),
          (assign,":found",0),
          (try_for_agents, ":agent_id"),
            (agent_is_alive, ":agent_id"),
            (agent_slot_eq, ":agent_id", slot_agent_on_fire, 1),
            (assign,":found",1),
            (agent_set_slot, ":agent_id", slot_agent_on_fire, 0),
          (try_end),
          (neq,":found",1),
          (assign, "$agent_on_fire", 0),
        (try_end),
      ]),

    (0.1, 0, 0,
          [
          (eq, "$agent_on_fire", 1),
          ],
          [
          (try_for_agents, ":agent_id"),
            (agent_is_alive, ":agent_id"),
            (agent_slot_eq, ":agent_id", slot_agent_on_fire, 1),
            (try_for_range, ":bone", 0, 18),
              (agent_get_bone_position, pos1, ":agent_id", ":bone", 1),
              (particle_system_burst, "psys_fireplace_fire_small", pos13, 3),
              (particle_system_burst, "psys_mortar_fire_smoke", pos13, 1),
            (try_end),
          (try_end),
          ]),


    #stamina/running
    (0.1, 0, 0,
          [
            (neg|conversation_screen_is_active),
            (neg|main_hero_fallen),
            (neq,"$g_player",-1),
            # (neg|agent_slot_eq, "$g_player", slot_agent_gun_aim_on, 1),
            # (neg|agent_slot_eq, "$g_player", slot_agent_crouching, 1),
            # (agent_get_crouch_mode, ":crouching", "$g_player"),
            # (neq, ":crouching", 1), #not crouching
          ],
          [
            (agent_get_slot, reg10, "$g_player", slot_agent_player_stamina),
            (try_begin),
                (key_is_down, "$key_run"),
				(neg|agent_slot_eq, "$g_player", slot_agent_gun_aim_on, 1),#moved here so can regen when crouching/aiming
				(neg|agent_slot_eq, "$g_player", slot_agent_crouching, 1),

                (this_or_next|game_key_is_down, gk_move_forward),
                (this_or_next|game_key_is_down, gk_move_backward),
                (this_or_next|game_key_is_down, gk_move_left),
                (game_key_is_down, gk_move_right),

                (agent_get_horse, ":horse", "$g_player"),
                (le, ":horse", 0),

                (try_begin),
                    (ge,reg10,1),

                    (val_mul,reg10,100),

                    (val_sub,reg10,"$g_player_stamina_rate"),
                    # (val_sub,reg10,60),

                    (val_div,reg10,100),

                    (agent_set_slot, "$g_player", slot_agent_player_stamina, reg10),

                    (agent_set_speed_modifier, "$g_player", "$g_player_speed_mod_running"),
                (else_try),
                    (agent_set_speed_modifier, "$g_player", "$g_player_speed_mod"),
                (try_end),
            (else_try),
                (neg|key_is_down, "$key_run"),

                (agent_set_speed_modifier, "$g_player", "$g_player_speed_mod"),

                (lt,reg10,100),

                (val_add,reg10,1),
                # (val_div,reg10,100),

                (agent_set_slot, "$g_player", slot_agent_player_stamina, reg10),
            (try_end),
            # (display_message,"@{reg10}"),
          ]),

    #dodge
    (0, 0, 0.01, [(neg|conversation_screen_is_active),],
      [
        (get_player_agent_no, "$g_player"),
        (agent_is_alive, "$g_player"),
        # (agent_get_wielded_item, ":wielded", "$g_player", 0),

        (assign, ":one_second_check", "$g_one_hundredth_second_timer"),
        (val_mod, ":one_second_check", 100),
        (try_begin),
          (eq, ":one_second_check", 0),  ## true once every second
          (agent_get_slot, ":roll_cooldown", "$g_player", slot_agent_last_roll),
          # reduce the duration
          (try_begin),
            (gt, ":roll_cooldown", 0),
            (val_sub, ":roll_cooldown", 1),
            (agent_set_slot, "$g_player", slot_agent_last_roll, ":roll_cooldown"),
          (else_try),
            (agent_set_slot, "$g_player", slot_agent_last_roll, 0),
            # (try_begin),
              # (ge, ":wielded", 0),
              # (neg|is_presentation_active, "prsnt_battle"),
              # (neg|is_presentation_active, "prsnt_swc_zoom_view"),
              # (start_presentation, "prsnt_show_weapon_stats"),
            # (try_end),
          (try_end),
        (try_end),

      ]),

    #timer
    (0, 0, 0.01, [],
        [
            (val_add, "$g_one_hundredth_second_timer", 1),
            ]),

    #ui
    (0.5, 0, 0,
        [
        (neg|conversation_screen_is_active),

        (neg|is_presentation_active, "prsnt_player_ui"),
        (neg|is_presentation_active, "prsnt_battle"),
        (neg|is_presentation_active, "prsnt_order_display"),
        # (neg|main_hero_fallen),

        ],
        [
        (start_presentation, "prsnt_player_ui"),
        ]),

    (0, 0, 0, [
        (this_or_next|key_clicked, key_page_up),
        (key_clicked, key_page_down),
      ],[
        (try_begin),
          # (key_clicked, key_page_up),
          (key_is_down, key_page_up),
          # (key_clicked, key_r),
          # (key_is_down, key_r),
          (call_script, "script_musicplayer",0),

        (else_try),
          # (key_clicked, key_page_down),
          (key_is_down, key_page_down),
          # (key_clicked, key_t),
          # (key_is_down, key_t),

          (call_script, "script_musicplayer",1),
        (try_end),
      ]),

    # #test	#disabled for now - krag
    # (ti_before_mission_start, 0, 0, [], [
      # (assign,"$fx_test",0),
        # ]),
    # (0, 0, 0, [
          # (key_clicked, key_k),
      # ], [
          # (set_postfx, "$fx_test"),
          # (assign,reg0,"$fx_test"),
          # (display_message,"@{reg0}"),
          # (try_begin),
              # (val_add,"$fx_test",1),
              # (gt,"$fx_test",20),
              # (assign,"$fx_test",0),
          # (try_end),
        # ]),

    # # (0, 2, 0, [
          # # (key_clicked, key_k),
                # # # (get_startup_sun_light, pos1), #tocan test
                # # # (position_get_x, "$sun_r", pos1),	# r
                # # # (position_get_y, "$sun_g", pos1), # g
                # # # (position_get_z, "$sun_b", pos1),	# b
                # # # (get_startup_ambient_light, pos1),
                # # # (position_get_x, "$amb_r", pos1),	# r
                # # # (position_get_y, "$amb_g", pos1), # g
                # # # (position_get_z, "$amb_b", pos1),	# b
            # # # (set_startup_sun_light, 100000, 100000, 100000), #tocan test
            # # # (set_startup_ambient_light, 100000, 100000, 100000),
            # # (set_fog_distance, 1, 0x00ffffff),
    # # ], [
            # # (set_fog_distance, "$g_fog_dist", 0x00ffffff),
            # # # (set_startup_sun_light, "$sun_r", "$sun_g", "$sun_b"),
            # # # (set_startup_ambient_light, "$amb_r", "$amb_g", "$amb_b"),
          # # # (set_postfx, "$fx_test"),
          # # # (assign,reg0,"$fx_test"),
          # # # (display_message,"@{reg0}"),
          # # # (try_begin),
              # # # (val_add,"$fx_test",1),
              # # # (gt,"$fx_test",13),
              # # # (assign,"$fx_test",0),
          # # # (try_end),
        # # ]),
    # # (ti_on_item_picked_up, 0, ti_once,
       # # [
        # # # (store_trigger_param_1, ":agent_id"),
        # # # # (store_trigger_param_2, ":weapon"),
        # # # (eq,"$g_player"),
       # # ],
       # # [
        # # (store_free_inventory_capacity, ":count", "trp_player"),
        # # # (try_begin),
          # # # (lt,":count",1),
          # # # (display_message,"@You don't have any room in your inventory to carry any fish.",message_negative),
        # # # (try_end),
        # # (ge,":count",1),
        # # (store_trigger_param_2, ":item"),
        # # (assign,":found",0),
        # # (assign,"$g_pickedup",0),
        # # (troop_get_inventory_capacity, ":inv_size", "trp_player"),
        # # (try_for_range, ":item_slot", 0, ":inv_size"),
          # # (neq,":found",1),
          # # (troop_get_inventory_slot, ":item_no", "trp_player", ":item_slot"),
          # # (ge, ":item_no", 0),
          # # (eq, ":item_no", ":item"),
          # # (assign,":found",1),
        # # (try_end),
        # # (neq,":found",1),
        # # (str_store_item_name, s1, ":item"),
        # # (assign,"$g_pickedup",1),
        # # (question_box,"@You just picked up a {s1}. Do you want to keep it in your inventory?"),
       # # ]),
    # # (0, 0, 0, [
      # # (eq,"$g_pickedup",1),
    # # ],
     # # [
      # # (store_trigger_param_1,":answer"),
      # # (try_begin),
        # # (eq,":answer",0),
        # # (agent_get_wielded_item,":item","$g_player",0),
        # # (str_store_item_name, s1, ":item"),
        # # (troop_add_item, "trp_player", ":item"),
        # # (display_message,"@{s1} added to your inventory.",message_alert),
      # # (try_end),
      # # (assign,"$g_pickedup",0),
      # # ]),
    ]

common_position = (0, 0, 0,
      [
            (eq,"$position_mod",1),
            (assign,":continue",0),
            (try_begin),
                (eq,"$position_party", "$current_town"),
                (assign,":continue",1),
            (else_try),
                (assign,"$position_mod",0),
            (try_end),
            (eq,":continue",1),
      ],
      [
            (get_player_agent_no, "$g_player"),
            # (agent_get_horse, ":player_horse","$g_player"),
            (troop_get_inventory_slot, ":has_item", "trp_player", ek_horse),
            (try_begin),
                (ge, ":has_item", 0),
                # (agent_set_position, ":player_horse", "$position_mod_value"),
            (else_try),
                (agent_set_position, "$g_player", "$position_mod_value"),
            (try_end),

            (assign,"$position_mod",0),

      ])

common_agent_label = (0, 0, 0,
    [
        (neg|conversation_screen_is_active),

        (neg|is_presentation_active, "prsnt_display_agent_labels"),
        (neg|is_presentation_active, "prsnt_deposit_withdraw_money"),
    ],
    [
        (start_presentation, "prsnt_display_agent_labels"),
    ])

common_info_message = (5, 0, ti_once, [],
    [
      (is_between,"$current_town",centers_begin,centers_end),
      (call_script, "script_info_message")
    ])

common_torch_at_night = (0, 1, ti_once,
    [
    (is_currently_night),
    ],
    [
      (try_for_agents, ":agent_id"),
	    (neg|agent_slot_ge, ":agent_id", slot_agent_static_npc, 1),
        (agent_is_alive, ":agent_id"),
		(agent_is_non_player, ":agent_id"),
        (agent_is_human, ":agent_id"),
		(agent_get_troop_id, ":troop_no", ":agent_id"),
		(neq, ":troop_no", "trp_dog_companion"),
		(neq, ":troop_no", "trp_bot_companion"),
		(neq, ":troop_no", "trp_wanted_sign"),
		(neg|is_between, ":troop_no", companions_begin, companions_end),
		(neg|is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
        (store_random_in_range,":chance",0,5),
        (try_begin),
            (eq,":chance",1),
            (agent_equip_item, ":agent_id", "itm_torch"),
            (agent_set_wielded_item, ":agent_id", "itm_torch"),
        (else_try),
            (eq,":chance",2),
            (agent_equip_item, ":agent_id", "itm_flashlight"),
            (agent_set_wielded_item, ":agent_id", "itm_flashlight"),
        (try_end),
      (try_end),
    ])

tocan_ambience = [   #tocan: all outdoor missions	#8 triggers
    #weather init
    (ti_before_mission_start, 0, 0, [	#1

      # (assign,"$thunder",-1),
      (assign, "$lightning_cycle", -1),
      (assign, "$g_fog_dist",1600),
      (assign, "$g_fog_color",0xFF8CA2AD),

      (store_time_of_day, ":day_time"),
      # (store_current_scene, ":scene"),
      (party_get_current_terrain, ":terrain", "p_main_party"),

      #rain/thunder
      (try_begin),
        (eq,"$g_rain",1),
        (store_random_in_range,":rain_strenght",100,301),
        (set_rain, 1, ":rain_strenght"),
        # (try_begin),
          # (gt,"$g_cloud",85),
          # (store_random_in_range,":chance",0,3),
          # (eq,":chance",1),
          # (assign,"$thunder",1),
        # (try_end),
      (else_try),
        (set_rain,0),
      (try_end),

      #sandstorm
      (try_begin),
        (eq,"$g_sandstorm",1),
        (lt,"$g_fog",50),
        (store_random_in_range, ":sandstorm_fog", 50, 101),
        (set_global_haze_amount, ":sandstorm_fog"),
      (try_end),

      #skybox
      (assign,":skybox",sb_skybox_clearday),
      (try_begin),
        (is_currently_night),

        (assign, "$g_fog_color",0xFF05070C),
        #(store_random_in_range, ":skybox", sb_skybox_night_1, sb_skybox_night_2),
         (assign,":skybox",sb_skybox_night_1),
        (try_begin),
          (gt, "$g_cloud", 50),
          #(store_random_in_range, ":skybox", sb_skybox_night_2, sb_skybox_sunset_1_new_1),
           (assign,":skybox",sb_skybox_night_2),
        (try_end),
      (else_try),
        (neg|is_currently_night),

        (try_begin),
          (neq,"$g_rad_zone",1),
          (neq,"$g_sandstorm",1),
          (try_begin),
            (is_between, ":day_time", 6, 20),
            (try_begin),
              (le, "$g_cloud", 15),
              (assign, "$g_fog_color",0xFF8CA2AD),
              (store_random_in_range, ":skybox", sb_skybox_clearday, sb_skybox_cloud_1),
            (else_try),
              (le, "$g_cloud", 50),
              (assign, "$g_fog_color",0xFF8CA2AD),
              (store_random_in_range, ":skybox", sb_skybox_cloud_1, sb_skybox_cloud_2),
            (else_try),
              (le, "$g_cloud", 85),
              (assign, "$g_fog_color",0xFF607090),
              (assign,":skybox",sb_skybox_cloud_2),
            (else_try),
              (assign, "$g_fog_color",0xFF607090),
              (store_random_in_range, ":skybox", sb_skybox_cloud_2_overcast, sb_skybox_night_1),
            (try_end),
          (else_try),
            (try_begin),
              # (le, "$g_cloud", 15),
              # (assign, "$g_fog_color",0xFF897262),
              # (assign,":skybox",sb_skybox_new_sunset_1),
            # (else_try),
              (le, "$g_cloud", 50),
              (assign, "$g_fog_color",0xFF897262),
              (store_random_in_range, ":skybox", sb_skybox_sunset_1_new_1, sb_skybox_sunset_2),
            (else_try),
              (assign, "$g_fog_color",0xFF897262),
              (store_random_in_range, ":skybox", sb_skybox_sunset_2, sb_skybox_tox),
            (try_end),
          (try_end),
        (else_try),
          (eq,"$g_sandstorm",1),
          (store_random_in_range, "$g_fog_dist", 50, 251),
          (assign, "$g_fog_color",0xFFCABC92),
          (assign, ":skybox", sb_skybox_orange_2),
        (else_try),
          (eq,"$g_rad_zone",1),
          (store_random_in_range, "$g_fog_dist", 50, 251),
          (assign, "$g_fog_color",0xFF314B37),
          (assign, ":skybox", sb_skybox_tox),
        (try_end),
      (try_end),

      (set_fog_distance, "$g_fog_dist", "$g_fog_color"),
      (set_skybox, ":skybox", ":skybox"),
###
      (set_fixed_point_multiplier, 1),
      (try_begin),
        (neq, ":terrain", rt_plain),
        (neq, ":terrain", rt_forest),
        (neq, ":terrain", rt_steppe_forest),
        (neq, ":terrain", rt_steppe),

        (set_shader_param_float, "@vEnvironment", shader_set_2),
      # (else_try),
        # (store_mod, ":even",  ":scene", 3),
        # (eq,":even",0),
        # (set_shader_param_float, "@vEnvironment", shader_set_3),
      (else_try),
        (set_shader_param_float, "@vEnvironment", shader_set_1),
      (try_end),
      # (store_random_in_range,":rnd",shader_set_1,shader_set_3+1),
        # (set_shader_param_float, "@vEnvironment", ":rnd"),
      (set_fixed_point_multiplier, 100),

        ],[]),

    #weather/light/postfx	#2
    (0, 0, ti_once, [
        (set_fixed_point_multiplier, 100),

        (try_begin),
          (call_script, "script_cf_warzone_ambience",1),
        (try_end),

        # #thunder
        # (try_begin),
            # (eq, "$thunder", 1),
            # # (store_time_of_day, ":day_time"),
            # # (neg|is_between, ":day_time", 4, 20),
            # (assign, "$lightning_cycle", 0),
            # (try_begin),
                # (eq, "$lightning_cycle", 0),
                # (get_startup_sun_light, pos1),
                # (position_get_x, "$sun_r", pos1),	# r
                # (position_get_y, "$sun_g", pos1), # g
                # (position_get_z, "$sun_b", pos1),	# b
                # (get_startup_ambient_light, pos1),
                # (position_get_x, "$amb_r", pos1),	# r
                # (position_get_y, "$amb_g", pos1), # g
                # (position_get_z, "$amb_b", pos1),	# b
            # (try_end),
        # (try_end),

        #drugs
        (try_begin),
            (this_or_next|eq,"$ondrugs",1),
            (eq,"$ondrugs",2),
            # (store_random_in_range, ":postfx", 10, 13),
            (set_postfx, pfx_drugs),
		  (else_try),
			  (is_currently_night),
			  (store_current_scene, ":scene"),
			  (neg|is_between,":scene", "scn_town_1_castle", "scn_town_1_alley"),
			  (get_player_agent_no, ":player_agent"),
			  (agent_get_item_slot, ":head_gear", ":player_agent", ek_head),
			  (this_or_next|eq, ":head_gear", "itm_upgrade_vision"),
			  (this_or_next|eq, ":head_gear", "itm_gas_mask_ww_e"),
			  (this_or_next|eq, ":head_gear", "itm_helmet_gas_olive"),
			  (this_or_next|eq, ":head_gear", "itm_helmet_gas"),
			 # (this_or_next|eq, ":head_gear", "itm_"),
			  (is_between, ":head_gear", "itm_ach_full", "itm_army_cap_1"),

			  (set_postfx, pfx_nightvision),
        (try_end),],[]),

    (2, 0, 0, [(store_mission_timer_a,":cur_time"),	#3
      (ge,":cur_time",5),],[
      (call_script, "script_cf_warzone_ambience", 0),]),

    #thunder	#4
    (3, 0.2, 6, 			#lightning 1
        [
            (eq, "$g_thunder", 1),
            (eq,"$lightning_cycle",0),
            (store_random_in_range,":chance",1,5),
            (eq,":chance",1),
            (play_sound,"snd_ambient_thunder_close"),
            (set_startup_sun_light, 1000, 1000, 1000),
            (set_startup_ambient_light, 1000, 1000, 1000),
        ],
        [
            (set_startup_sun_light, 0, 0, 0),
            (set_startup_ambient_light, 0, 0, 0),

            (assign, "$lightning_cycle",1),
        ]),
    (0.4,0.1, 6,			#lightning 2	#5
        [
            (eq, "$g_thunder", 1),
            (eq,"$lightning_cycle",1),

            (set_startup_sun_light, 220, 220, 220),
            (set_startup_ambient_light, 220, 220, 220),
        ],
        [
            (set_startup_sun_light, 1, 1, 1),
            (set_startup_ambient_light, 1, 1, 1),
            (assign,"$lightning_cycle",2),
        ]),
    (0.5,0.1, 6,			#lightning 3	#5
        [
            (eq, "$g_thunder", 1),
            (eq,"$lightning_cycle",2),
            (set_startup_sun_light, 150, 150, 150),
            (set_startup_ambient_light, 150, 150, 150),
        ],
        [
            (set_startup_sun_light, "$sun_r", "$sun_g", "$sun_b"),
            (set_startup_ambient_light, "$amb_r", "$amb_g", "$amb_b"),
            (assign,"$lightning_cycle", 0),
        ]),
    (2.5, 0, 0, #new thunder	#7
        [
            (eq, "$g_thunder", 1),
            (store_random_in_range,":chance",1,3),
            (eq,":chance",1),
        ],
        [
            (set_fixed_point_multiplier, 1),
            # (get_player_agent_no, "$g_player"),
            (agent_get_position, pos53, "$g_player"),
            (store_random_in_range, ":z_rot", 0, 360),
            (position_rotate_z, pos53, ":z_rot"),
            # (position_move_z, pos1, 30000),
            (position_set_z_to_ground_level, pos53),
            (position_move_z,pos53,1),
            (position_move_y, pos53, 100000),
            # (particle_system_burst, "psys_lightning_1", pos1, 1),
            (copy_position, pos54, pos53),
            (position_move_z, pos54, 50000),
            (particle_system_burst_no_sync, "psys_upper_lightning", pos54, 1),
            (store_random_in_range, ":particle", "psys_lightning_1", "psys_upper_lightning"),
            (particle_system_burst_no_sync, ":particle", pos53, 1),
            (set_fixed_point_multiplier, 100),
        ]),

    #sandstorm	#8
    (0, 0, 0,
      [
        (eq, "$g_sandstorm",1),
        (gt, "$g_player",-1),
      ],
      [
        # (get_player_agent_no, "$g_player"),
        (agent_get_position, pos0, "$g_player"),
        (position_set_z_to_ground_level, pos0),
        #(position_move_z, pos3, 350),
        (position_get_z, ":z", pos0),
        (val_add, ":z", 400),
        (position_set_z, pos0, ":z"),
        (particle_system_burst, "psys_desert_storm", pos0,2),
        (set_fixed_point_multiplier, 100),
      ]),

    ]

tocan_walkers =	[
    (0, 0, ti_once, [
        (neg|is_currently_night),
      ],
      [
        (call_script, "script_cf_spawn_npcs"),
      ]),


    (1, 6, 0, [
        (neg|is_currently_night),
        (neg|party_slot_ge, "$current_town", slot_center_has_attacker,3),
        # (neg|gt, "$g_main_attacker_agent", 0),
      ],
      [
        (try_for_agents, ":agent_id"),
          (agent_is_alive, ":agent_id"),
          (agent_slot_eq, ":agent_id", slot_agent_walker_occupation, 1),
          (store_random_in_range, ":rand", 0, 2),
          (eq, ":rand", 0),
          (store_random_in_range, ":rand", 32, 40),
          (entry_point_get_position, pos1, ":rand"),
          (agent_set_scripted_destination, ":agent_id", pos1, 0),
        (try_end),
      ]),

      # # (3, 0, 0, [(neg|is_currently_night),],
        # # [
          # # (store_random_in_range, ":rand", 0, 5),
          # # (eq, ":rand", 0),
          # # (assign, ":sound_played", 0),
          # # (try_for_agents, ":agent_id"),
            # # (eq, ":sound_played", 0),
            # # (neg|agent_is_human, ":agent_id"),
            # # (agent_is_alive, ":agent_id"),
            # # (agent_get_item_id, ":item", ":agent_id"),
            # # (eq, ":item", "itm_animal_pig"),
            # # (store_random_in_range, ":rand", 0, 3),
            # # (eq, ":rand", 0),
            # # (agent_play_sound, ":agent_id", "snd_pig"),
            # # (assign, ":sound_played", 1),
          # # (try_end),
      # # ]),
    ]

tocan_flashlight = [
    (ti_after_mission_start, 0, ti_once,
      [
        (assign,"$flashlight_active",0),
      ],
      [
      ]),
    (ti_on_item_wielded, 0, 0,
      [
        (store_trigger_param_1, ":agent_id"),
        (store_trigger_param_2, ":weapon"),
        (get_player_agent_no, "$g_player"),
        (eq,":agent_id", "$g_player"),
        (eq,":weapon", "itm_flashlight"),
        (agent_get_position, pos3, ":agent_id"),
        (position_move_y, pos3, 300),
        (position_move_z, pos3, 300),
        (set_spawn_position, pos3),
        (spawn_scene_prop, "spr_movelight"),
        (assign, "$move_light", reg0),
        (assign,"$flashlight_active",1),
      ],
      [
      ]),
    (ti_on_item_unwielded, 0, 0,
      [
        (eq,"$flashlight_active",1),
        (store_trigger_param_1, ":agent_id"),
        (store_trigger_param_2, ":weapon"),
        (get_player_agent_no, "$g_player"),
        (eq,":agent_id", "$g_player"),
        (eq,":weapon", "itm_flashlight"),
        (assign,"$flashlight_active",0),
      ],
      [
      ]),
    (0.1, 0, 0,
      [
        (eq,"$flashlight_active",1),
		(prop_instance_is_valid, "$move_light"),
        (get_player_agent_no, "$g_player"),
        (agent_get_position, pos4, "$g_player"),
        (position_move_y, pos4, 300),
        (position_move_z, pos4, 250),
        (prop_instance_set_position, "$move_light",pos4),
      ],
      [


      ]),
  ]

x_companion =	[		# 7 trigger
  (0, 0, ti_once,
    [
        # (ge, "$g_special_companion", 1),
		(le, "$sneaked_into_town", disguise_none),
        (get_player_agent_no, "$g_player"),
        (agent_is_active, "$g_player"),
    ],
    [
        (ge, "$g_special_companion", 1),
        # (eq, "$g_special_companion", 1),
        (call_script, "script_cf_additional_npc_conditions"),
        (set_fixed_point_multiplier, 100),
        # (get_player_agent_no, "$g_player"),
        (agent_get_position, pos1, "$g_player"),
        (position_move_x, pos1, 150),
        (set_spawn_position, pos1),
        (try_begin),
            (eq, "$g_special_companion", 1),
            (spawn_agent, "trp_dog_companion"),
            # (assign, "$g_player_x_agent_no", reg0),
        (else_try),
            (spawn_agent, "trp_bot_companion"),
            # (assign, "$g_player_x_agent_no", reg0),
        (try_end),
        # (spawn_agent, "trp_dog_companion"),
        (assign, "$g_player_x_agent_no", reg0),
        (agent_add_relation_with_agent, "$g_player", "$g_player_x_agent_no", 1),#was 0. why enemy?
        (assign, "$x_npc_order", 0),
        (agent_set_hit_points, "$g_player_x_agent_no", 100, 0),

        (agent_get_team, "$g_player_team", "$g_player"),
        (agent_set_team, "$g_player_x_agent_no", "$g_player_team"),
        (agent_set_division, "$g_player_x_agent_no", grc_special),
        (try_begin),
            (eq, "$g_special_companion", 1),
            # (spawn_agent, "trp_dog_companion"),
            (str_store_troop_name, s1, "trp_dog_companion"),
        (else_try),
            # (spawn_agent, "trp_bot_companion"),
            (str_store_troop_name, s1, "trp_bot_companion"),
        (try_end),
        # (str_store_troop_name, s1, "trp_dog_companion"),
        (class_set_name, grc_special, s1),
        ]),

  (1, 0, 0,
    # CIVIL DOG ORDERS
    [
        (ge, "$g_special_companion", 1),
		(le, "$sneaked_into_town", disguise_none),
        (ge, "$x_npc_order", 0),
        (agent_is_active, "$g_player_x_agent_no"),
        (agent_is_alive, "$g_player_x_agent_no"),
        #(neg|agent_is_human, "$g_player_x_agent_no"),
        (store_random_in_range, ":rand", 0, 3),
        (this_or_next|eq, "$x_npc_order", 1),
        (eq, ":rand", 0),
    ],
    [
        (set_fixed_point_multiplier, 100),
        # (get_player_agent_no, "$g_player"),
        (agent_get_position, pos1, "$g_player"),
        (try_begin),
            (eq, "$x_npc_order", 0),
            (store_random_in_range, ":rand", -500, 500),
            (position_move_x, pos1, ":rand"),
            (store_random_in_range, ":rand", 200, 700),
            (position_move_y, pos1, ":rand"),
        (else_try),
            (position_move_y, pos1, 150),
        (try_end),
        (agent_set_scripted_destination, "$g_player_x_agent_no", pos1),
    ]),

  (ti_on_agent_killed_or_wounded, 0, ti_once,
    #KILL/WOUND DOG
    [
        (ge, "$g_special_companion", 1),
		(le, "$sneaked_into_town", disguise_none),
        (store_trigger_param_1, ":dead_agent_no"),
        (eq, ":dead_agent_no", "$g_player_x_agent_no"),
    ],
    [
        # # (store_random_in_range, ":rand", 1, 11),
        # # (try_begin),
        # # (eq, 1, 0),#VC-3394
        # # (eq, ":rand", 10),
        # # (agent_set_slot, "$g_player_x_agent_no", slot_agent_vc_wounded, -1),
        # # #(display_message, "@{!}TEST: Dog should be shown as dead!"),
        # # (assign, "$dog_companion", 0),
        # # (str_store_string, s7, "@Dog"),
        # # (troop_set_name, "trp_dog_companion", s7),
        # # (else_try),
        # (agent_set_slot, "$g_player_x_agent_no", slot_agent_vc_wounded, 1),
        # # (try_end),
        (agent_get_horse, ":horse", "$g_player_x_agent_no"),
        (gt, ":horse", 0),
        (agent_deliver_damage_to_agent, ":horse", ":horse", 1000),
    ]),

  (ti_on_order_issued, 0, 0,
    #AVOID DISMOUNT COMMAND
    [
        (ge, "$g_special_companion", 1),
		(le, "$sneaked_into_town", disguise_none),
        (store_trigger_param, ":order_no", 1),
        (eq, ":order_no", mordr_dismount),
    ],
    [
        (try_begin),
            (agent_is_active, "$g_player_x_agent_no"),
            (agent_is_alive, "$g_player_x_agent_no"),
            # (get_player_agent_no, "$g_player"),
            (agent_get_team, "$g_player_team", "$g_player"),
            (set_show_messages, 0),
            (team_give_order, "$g_player_team", grc_special, mordr_mount),
            (set_show_messages, 1),
        (try_end),
    ]),

  #KILL DOG ON DISMOUNT 1
  (ti_on_agent_dismount, 0, 0, [
        (ge, "$g_special_companion", 1),
		(le, "$sneaked_into_town", disguise_none),
        (store_trigger_param_1, ":agent_id"),
        (eq, ":agent_id", "$g_player_x_agent_no"),
    ], [
        (assign, "$x_npc_order", -2),
        (store_trigger_param_2, "$alpha_animal"),
    ]),

  #KILL DOG ON DISMOUNT 2
  (0.5, 0.5, 0, [
        (ge, "$g_special_companion", 1),
		(le, "$sneaked_into_town", disguise_none),
        (eq, "$x_npc_order", -2),
    ], [
        (assign, "$x_npc_order", -1),
        (try_begin),
            (agent_is_active, "$g_player_x_agent_no"),
            (agent_is_alive, "$g_player_x_agent_no"),
			(set_show_messages, 0),
            (agent_deliver_damage_to_agent, "$g_player_x_agent_no", "$g_player_x_agent_no", 1000),
			(set_show_messages, 1),
        (try_end),
        (try_begin),
            (agent_is_active, "$alpha_animal"),
            (agent_is_alive, "$alpha_animal"),
			(set_show_messages, 0),
            (agent_deliver_damage_to_agent, "$alpha_animal", "$alpha_animal", 1000),
			(set_show_messages, 1),
        (try_end),
  ]),

  (1, 0, 0, [
        (ge, "$g_special_companion", 1),
		(le, "$sneaked_into_town", disguise_none),
    ],
    # FIX ENGINE DIVISION PROBLEM
    [
        (try_begin),
            (agent_is_active, "$g_player_x_agent_no"),
            (agent_is_alive, "$g_player_x_agent_no"),
            (agent_get_division ,":division", "$g_player_x_agent_no"),
            (neq ,":division", grc_special),
            #(display_message, "@Resetting Dog division."),
            # (get_player_agent_no, "$g_player"),
            (agent_get_team, "$g_player_team", "$g_player"),
            (agent_set_division, "$g_player_x_agent_no", grc_special),
            (team_get_movement_order, ":order", "$g_player_team", grc_special),
            (set_show_messages, 0),
            (team_give_order, "$g_player_team", grc_special, ":order"),
            (set_show_messages, 1),
        (try_end),
        ]),
  ]

tocan_battle_triggers = [ #tocan: battle missions
    # (ti_after_mission_start, 0, 0, [
        # ],[]),

    (0.5, 0, 0, [],
      [
        (ge, "$g_player", 0),
        (agent_get_troop_id, ":current_player_troop_id", "$g_player"),
        (try_for_agents, ":agent"),
          (agent_is_alive, ":agent"),
          (agent_is_human, ":agent"),

          # DETECTING WEAPON BREAK CAUSE
          (assign, ":state", 0),
          (try_begin),
            (agent_is_in_parried_animation, ":agent"),
            (assign, ":state", 1),
          (else_try),
            (call_script, "script_cf_agent_is_in_parrying_animation", ":agent"),
            (assign, ":state", 2),
          (end_try),
          (ge, ":state", 1),
          (agent_get_wielded_item, ":wielded_item", ":agent", 0),
          (neq, ":wielded_item", -1),

          # GETTING BASIC CHANCE
          (try_begin),
            # player (imod)
            (eq, ":agent", "$g_player"),
            (assign, ":wielded_item_slot", -1),
            (try_for_range, ":item_slot", 0, 4),
              (troop_get_inventory_slot, ":slot_item", ":current_player_troop_id", ":item_slot"),
              (eq, ":slot_item", ":wielded_item"),
              (assign, ":wielded_item_slot", ":item_slot"),
            (try_end),
            (neq, ":wielded_item_slot", -1),
            (troop_get_inventory_slot_modifier, ":slot_item_imod", ":current_player_troop_id", ":wielded_item_slot"),
            (item_get_type, ":item_type", ":wielded_item"),
            (call_script, "script_get_item_modifier_effects", ":item_type", ":slot_item_imod"),
            (assign, ":basic_chance", reg5),			# 40(cracked) up to 180(tempered)
            (val_div, ":basic_chance", -10),			# -4(cracked) up to -18(tempered)
            (val_add, ":basic_chance", 22),			# 18(cracked) up to   4(tempered)
            (val_max, ":basic_chance", 1),			# so "cracked" should be 1,8% and "tempered" 0,4%
          (else_try),
            # all others
            (assign, ":basic_chance", 10),			# as if AI would have imod heavy in general
          (end_try),

          #TEST
          # (assign, reg5, ":basic_chance"),
          # (display_message, "@{!}TEST: Weapon break: basic_chance: {reg5}"),

          # MODIFING CHANCE
          (try_begin),
            (eq, ":state", 1),
            (assign, ":chance", ":basic_chance"),	# ~1%
          (else_try),
            (store_mul, ":chance", ":basic_chance", 2),	# ~2%
          (end_try),
          (item_get_type, ":item_type", ":wielded_item"),
          (item_get_weapon_length, ":weapon_length", ":wielded_item"),
          (try_begin),
            (eq, ":item_type", itp_type_polearm),
            #Adjustment for weapon length JUJU
            (val_mul, ":chance", ":weapon_length"),	# *1,5 # was *1,7
            (val_div, ":chance", 100),
          (else_try),
            (is_between, ":wielded_item", "itm_hatchet", "itm_staff"),#axes
            (val_div, ":weapon_length", 2),
            (val_add, ":weapon_length", 100),
            (val_mul, ":chance", ":weapon_length"),
            #(val_mul, ":chance", 140),	# *1,4 # was *1,5
            (val_div, ":chance", 100),
          (end_try),

          (try_begin),
            (eq, ":agent", "$g_player"),
            (party_get_skill_level, ":skill", "p_main_party", skl_engineer),
            (party_get_skill_level, ":skill2", "p_main_party", skl_crafting),
            (val_add, ":skill", ":skill2",),
          (else_try),
            (agent_get_troop_id, ":troop_id", ":agent"),
            (store_character_level, ":level", ":troop_id"),
            (this_or_next|ge, ":level", 25),
            (troop_is_hero,  ":troop_id"),
            (assign, ":skill", 7),
          (else_try),
            (assign, ":skill", 3),
          (end_try),
          (val_mul, ":skill", 7),  #7% for each skill point
          (store_sub, ":skill_modifier", 100, ":skill"),  #so skill_modifier is 0-100
          (val_mul, ":chance", ":skill_modifier"),
          (val_div, ":chance", 100),

          # DECISION
          (store_random_in_range, ":rand", 1, 1001),
          # (assign, reg4, ":rand"),(assign, reg5, ":chance"),
          # (display_message, "@{!}TEST: Weapon break: rand: {reg4}, chance: {reg5}"),
          (le, ":rand", ":chance"),

          (try_begin),
            # DEGRADE
            (eq, ":agent", "$g_player"),
            (neg|game_in_multiplayer_mode),
            (call_script, "script_get_next_lower_imod_for_item", ":wielded_item", ":slot_item_imod"),
            (neq, ":slot_item_imod", reg0),	#weapon will break if this fails
            (troop_set_inventory_slot_modifier, ":current_player_troop_id", ":wielded_item_slot", reg0),
            (play_sound, "snd_dummy_hit"),
            (display_message, "@Your weapon was damaged!",message_alert),
          (else_try),
            # BREAK
            (agent_unequip_item, ":agent", ":wielded_item", ":wielded_item_slot"),
            (agent_get_bone_position, pos1, ":agent", hb_item_r, 1),
            (particle_system_burst, "psys_dummy_smoke", pos1, 3),
            (particle_system_burst, "psys_dummy_straw", pos1, 10),

            # ANIMATION
            (try_begin),
              (agent_get_horse, ":horse", ":agent"),
              (neq, ":horse", -1),
              (agent_set_animation, ":agent", "anim_strike_chest_front_stop"),
            (end_try),

            # SOUND AND MESSAGE
            (try_begin),
              (eq, ":agent", "$g_player"),
              (play_sound, "snd_dummy_hit"),
              (display_message, "@Your weapon broke!", message_negative),
            (end_try),

            #EQUIP NEW WEAPON
            (try_begin),
              (neq, ":agent", "$g_player"),
              (agent_get_group, ":team", ":agent"),
              (agent_get_division, ":division", ":agent"),
              (try_begin),
                (eq,":division",-1),
                (assign,reg0,aordr_fire_at_will),
              (else_try),
                (team_get_hold_fire_order, reg0, ":team", ":division"),
              (try_end),
              (call_script, "script_equip_best_melee_weapon", ":agent", 0, 0, reg0),
            (end_try),
            (assign, ":agent_weapons", 0),
            (try_for_range, ":item_slot", 0, 4),
              (agent_get_item_slot,  ":item", ":agent", ":item_slot"),
              (gt, ":item", -1),
              (item_get_type, ":item_type", ":item"),
              (this_or_next|eq, ":item_type", itp_type_one_handed_wpn),
              (this_or_next|eq, ":item_type", itp_type_two_handed_wpn),
              (			 	eq, ":item_type", itp_type_polearm),
              (val_add, ":agent_weapons", 1),
            (try_end),

            # COURAGE
            (try_begin),
              (neq, ":agent", "$g_player"),
              (neg|game_in_multiplayer_mode),
              (eq, ":agent_weapons", 0),
              (agent_get_slot, ":agent_courage_score", ":agent",  slot_agent_courage_score),
              (val_sub, ":agent_courage_score", 1000),
              (val_max, ":agent_courage_score", 0),
              (agent_set_slot, ":agent", slot_agent_courage_score, ":agent_courage_score"),
            (end_try),
          (end_try),
        (end_try),
      ]),


    #passable allies
    (0, 0, 0, [
            (neg|main_hero_fallen),
            (key_is_down, "$key_letmepass"),
        ],[
            (get_player_agent_no, "$g_player"),
            (agent_get_position, pos1, "$g_player"),
            (agent_get_team, ":p_team", "$g_player"),
            (try_for_agents, ":agent_id"),
                (agent_is_alive, ":agent_id"),
                (agent_is_human, ":agent_id"),
                (agent_is_non_player, ":agent_id"),
                (agent_get_team, ":a_team", ":agent_id"),
                (neg|teams_are_enemies, ":a_team", ":p_team"),
                (agent_get_position, pos2, ":agent_id"),
                (get_distance_between_positions, ":dist", pos2, pos1),
                (call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":p_team", 1),
                (assign, ":min_dist_e", reg1), # Find distance of nearest 3 enemies
                (try_begin),
                    (gt, ":min_dist_e", 200), # Are the enemies within 2 meters?
                    (le, ":dist", 100),
                    (position_move_y, pos1, 1),
                    (agent_set_position, "$g_player", pos1),
                (try_end),
            (try_end),
        ]),

    #permadeath
    (1, 4, ti_once, [
            (eq, "$g_permadeath", 1),(main_hero_fallen)],
        [
            (store_random_in_range, ":permanent_death", 1, 101), #
            (try_begin),
                (gt, ":permanent_death", 90),
                (jump_to_menu,"mnu_player_permanent_death"),
            (try_end),
            (try_begin),
                (call_script, "script_cf_dplmc_battle_continuation"),
            (else_try),
                (assign, "$pin_player_fallen", 1),
                (str_store_string, s5, "str_retreat"),
                (call_script, "script_simulate_retreat", 10, 20),
                (assign, "$g_battle_result", -1),
                (set_mission_result,-1),
                (call_script, "script_count_mission_casualties_from_agents"),
                (finish_mission,0),
           (try_end),
			  ]),

    #spitters
    (0.25, 0, 0,
       [
            # (store_faction_of_party, ":faction", "$g_encountered_party"),
            # (eq, ":faction", "fac_infected"),
            # (party_get_template_id, ":template", "$g_encountered_party"),
            # (eq, ":template", "pt_spitters"),
            # (display_message, "@Firing spitters", message_negative),
            (eq,"$g_spitter_active",1),

       ], [
            (set_fixed_point_multiplier, 100),

            # (get_player_agent_no,"$g_player"),
            (try_for_agents, ":spitter"),
              (agent_is_non_player, ":spitter"),
              (agent_is_alive, ":spitter"),
              (agent_is_human, ":spitter"),
              (agent_is_active, ":spitter"),
              (agent_get_troop_id, ":troop_no", ":spitter"),
              (eq,":troop_no","trp_spitter"),

              (agent_get_team, ":team", ":spitter"),
              (assign, ":maximum_distance", 500),

              (agent_ai_get_look_target,":target",":spitter"),
              (gt,":target",0),
              (agent_is_alive, ":target"),
              (agent_is_human, ":target"),
              (agent_is_active, ":target"),
              (agent_get_team, ":target_team", ":target"),
              (neq, ":target_team", ":team"),

                # #(agent_get_position, pos1, ":spitter"),
                # (agent_get_look_position, pos3, ":spitter"),    # Try from here
                # # (position_set_z, pos1, 180),
                # #(position_move_z, pos1, 180),
                 # (agent_get_bone_position, pos1, ":spitter", 9, 1), # Forgot to ask for the location in global space! ah nice!
                 # (position_move_y,0
                 # (position_copy_rotation, pos1, pos3),  # To Here

                (agent_get_look_position, pos1, ":spitter"),
                (position_move_z, pos1, 175),
                (position_move_y, pos1, 1, 0),
                # (position_rotate_y, pos1, 90),
                (agent_get_position, pos2, ":target"),
                # (neg|position_is_behind_position, pos2, pos1), #Suspect can't be behind kicker.
                (get_distance_between_positions, ":distance", pos1, pos2),
                (le, ":distance", ":maximum_distance"),

                (store_random_in_range,":chance",0,5),
                (eq,":chance",1),
                # (agent_set_slot, ":spitter", slot_agent_infected_spit, 1),

                # (agent_set_attack_action, ":spitter", -1, 0), #cancel
                # (agent_set_defend_action, ":spitter", 0, 1), #cancel

                # (agent_set_animation, ":spitter", "anim_headbutt"),
                (agent_set_animation, ":spitter", "anim_shoot_spit"),
                (add_missile, ":spitter", pos1, 500, "itm_infected_spit", 0, "itm_infected_spit", 0),

                (position_move_x, pos1, 0),
                (position_move_y, pos1, 25),
                (particle_system_burst, "psys_game_blood_green_2", pos1, 500),
            (try_end),])

    ]

tocan_cover =	[
    (ti_before_mission_start, 0, 0, [], #init before mission
      [
      (assign, "$scene_has_cover", 0),
      (assign, "$cover_ai_timer", 0),
      ]),

    (ti_after_mission_start, 0, 0, [],[
        # (assign, "$g_one_hundredth_second_timer", 0),
        (scene_prop_get_num_instances, ":total", "spr_cover"),
        (try_begin),
          (gt, ":total",0),
          (assign, "$scene_has_cover", 1),
          (assign, "$g_class_listening", grc_everyone),
          (try_for_range,":cur_instance",0,":total"),
            (scene_prop_get_instance, ":instance_id", "spr_cover", ":cur_instance"),
            (scene_prop_set_slot,":instance_id",scene_prop_cover_occupied,0),
          (try_end),

          (scene_prop_get_num_instances, ":total", "spr_cover_enemy"),
          (try_begin),
            (gt, ":total",0),
            (try_for_range,":cur_instance",0,":total"),
              (scene_prop_get_instance, ":instance_id", "spr_cover_enemy", ":cur_instance"),
              (scene_prop_set_slot,":instance_id",scene_prop_cover_occupied,0),
            (try_end),
          (try_end),
        (try_end),

		# (try_for_prop_instances, ":instance_id", "spr_cover"), #alternate for setting cover prop slots, change size for visual cue - krag
			# (scene_prop_set_slot,":instance_id",scene_prop_cover_occupied,0),(prop_instance_set_scale, ":instance_id", 200, 200, 100),
			# #(prop_instance_set_scale, ":instance_id", 50, 50, 200),
		# (try_end),
		# (try_for_prop_instances, ":instance_id", "spr_cover_enemy"),
			# (scene_prop_set_slot,":instance_id",scene_prop_cover_occupied,0),(prop_instance_set_scale, ":instance_id", 200, 200, 100),
			# #(prop_instance_set_scale, ":instance_id", 50, 50, 200),
		# (try_end),
        ]),

    (1,0, 0, #check
      [
        (eq, "$scene_has_cover", 1),
        # (neq, "$g_battle_result", 1),
      ],
      [
        (call_script,"script_cover_ai_position"),
      ]),

    (1,0, 0, #check
      [
        (eq, "$scene_has_cover", 1),
        # (neq, "$g_battle_result", 1),
      ],
      [
        (call_script,"script_cover_ai_check"),
      ]),

    (ti_on_agent_killed_or_wounded, 0, 0, [(eq, "$scene_has_cover", 1),], #free cover slut
       [
        (store_trigger_param_1, ":dead_agent_no"),

        (try_begin),
          (ge, ":dead_agent_no", 0),

          (agent_is_human, ":dead_agent_no"),
          (agent_is_active, ":dead_agent_no"),
          (agent_slot_ge, ":dead_agent_no", slot_agent_take_cover, 0),

          (agent_get_slot, ":instance_id", ":dead_agent_no", slot_agent_prop_occupied),
          (scene_prop_set_slot,":instance_id",scene_prop_cover_occupied,0),
        (try_end),]),

    (5, 0, ti_once,
      [
        (eq, "$scene_has_cover", 1),
      ],
      [
        # (call_script,"script_cover_battle_start","$g_player_team", 1000),	#search for close cover first - krag

        # (call_script,"script_cover_battle_start","$g_player_team", 3500),	#search for mid cover second - krag

        # (call_script,"script_cover_battle_start","$g_player_team", 7000),
        # (display_message, "@Troops searching for cover positions..."),
      ]),

    ]

tocan_vehicles =	[
    (ti_before_mission_start, 0, 0,
    [],
    [
      (assign, "$g_car_is_present", 0),

      (assign, "$g_vehicle_car_1", 0),
      (assign, "$g_vehicle_car_2", 0),
      (assign, "$g_vehicle_car_3", 0),
      (assign, "$g_vehicle_car_m1", 0),
      (assign, "$g_vehicle_car_m2", 0),
      (assign, "$g_vehicle_car_m3", 0),
      (assign, "$g_vehicle_car_raider", 0),
      (assign, "$g_vehicle_chopper_1", 0),
      (assign, "$g_vehicle_chopper_2", 0),

      # (assign, "$car_dest", 0),
    ]),

    (ti_on_agent_spawn, 0, 0,
    [],
    [
      (store_trigger_param_1, ":agent_id"),
      (agent_is_human, ":agent_id"),
      (agent_get_troop_id, ":troopd_id", ":agent_id"),
      (try_begin),
        (this_or_next|eq, ":troopd_id", "trp_car_mechanic"),
        (this_or_next|eq, ":troopd_id", "trp_f1_car_mechanic"),
        (this_or_next|eq, ":troopd_id", "trp_f2_car_mechanic"),
        (this_or_next|eq, ":troopd_id", "trp_chopper_mechanic"),
        (this_or_next|eq, ":troopd_id", "trp_f1_chopper_mechanic"),
        # (this_or_next|eq, ":troopd_id", "trp_f2_chopper_mechanic"),
        (eq, ":troopd_id", "trp_bus_mechanic"),
        (assign, "$g_car_is_present", 1),
      (try_end),
    ]),

    (2, 3, ti_once,
      [(eq, "$g_car_is_present", 1),],
      [(call_script, "script_cf_deploy_cart"),
      (assign, "$g_car_is_present", 2),
      ]),

    (0.03, 0, 0,
      [(eq, "$g_car_is_present", 2),],[(call_script, "script_cart_scan"),]),

    (0, 0, 0.0,
    [
      (eq, "$g_car_is_present", 2),
    ],
    [
      (try_for_agents, ":agent_id"),
        (agent_is_human, ":agent_id"),
        (agent_is_alive, ":agent_id"),

        (agent_slot_ge, ":agent_id", slot_agent_rides_x, 0),

        (this_or_next|agent_has_item_equipped, ":agent_id", "itm_bus"),
        (this_or_next|agent_has_item_equipped, ":agent_id", "itm_car"),
        (agent_has_item_equipped, ":agent_id", "itm_heli"),

        (agent_get_horse, ":horse", ":agent_id"),

        (try_begin), #car active, agent on it
          (gt, ":horse", 0),
          # (agent_slot_ge, ":horse", slot_agent_horse_prop, 0),

          (try_begin),
            (agent_has_item_equipped, ":agent_id", "itm_car"),

            (agent_set_animation, ":agent_id", "anim_driving", 0),	#set to lower only - krag
			#(agent_get_wielded_item, ":wielded", ":agent_id", 0),
            #(try_begin),
				#(call_script, "script_cf_agent_wield_weapons", ":agent_id"),
				#(agent_set_wielded_item, ":agent_id", "itm_ai_lmg_pkm"),
				(agent_set_wielded_item, ":agent_id", "itm_ai_mg_auto_cannon"),
			#(try_end),
          (else_try),
            (agent_has_item_equipped, ":agent_id", "itm_bus"),
            (agent_set_animation, ":agent_id", "anim_driving3", 0),
          (try_end),

          (try_begin),
            (this_or_next|agent_has_item_equipped, ":agent_id", "itm_car"),
            (agent_has_item_equipped, ":agent_id", "itm_bus"),
            (agent_get_speed, pos1, ":horse"),
            (position_get_y, ":speed", pos1),
            (gt, ":speed", 10),

            (try_for_agents, ":inflicted"),
              (agent_is_alive, ":inflicted"),
              (agent_is_human, ":inflicted"),
              (neq, ":inflicted", ":agent_id"),
              (neg|agent_is_ally, ":inflicted"),
              (agent_get_position, pos2, ":inflicted"),
              (agent_get_position, pos3, ":horse"),
              (get_distance_between_positions, ":dist", pos3, pos2),
              (try_begin),
                (lt, ":dist", 120),
                (val_div,":speed",300),#was 200, but was instakill basically
                (val_max,":speed",1),
                (assign,reg14,":speed"),
                (agent_deliver_damage_to_agent, ":agent_id", ":inflicted", ":speed", "itm_sledgehammer"),
                # (agent_deliver_damage_to_agent, ":agent_id", ":inflicted", 50),
                                    # (display_message, "@car makes {reg14} damage"),
              (try_end),
            (try_end),
          (else_try),
            (agent_has_item_equipped, ":agent_id", "itm_heli"),
            (agent_get_ammo, ":ammo", ":agent_id", 0),
			(try_begin),
				(le,":ammo",0),
				(agent_set_slot, ":agent_id",  slot_agent_is_running_away, 1),
				 (agent_start_running_away, ":agent_id"),
			  (else_try),
				#(neg|agent_has_item_equipped, ":agent_id", "itm_grenade"),
				(agent_set_wielded_item, ":agent_id", "itm_ai_mg_auto_cannon"),
				#(agent_set_wielded_item, ":agent_id", "itm_grenade"),
			(try_end),

			(agent_ai_get_cached_enemy, ":cached_agent_id", ":agent_id", 0),
			(try_begin),
				(gt, ":cached_agent_id", 0),
				(agent_is_active, ":cached_agent_id"),
				 (agent_is_non_player, ":cached_agent_id"),
				 (agent_get_ammo, ":cached_ammo", ":cached_agent_id", 0),
				(try_begin),
					(le,":cached_ammo",0),
					(agent_get_troop_id, ":troop_id", ":cached_agent_id"),
					(neg|is_between,":troop_id",infested_mut_begin,infested_end),
					(agent_set_slot, ":cached_agent_id",  slot_agent_is_running_away, 1),
					(agent_set_slot, ":cached_agent_id", slot_agent_courage_score, 0),
					(agent_start_running_away, ":cached_agent_id"),
				(try_end),
			(try_end),
			(agent_ai_get_cached_enemy, ":cached_agent_id2", ":agent_id", 1),
			(try_begin),
				(gt, ":cached_agent_id2", 0),
				(agent_is_active, ":cached_agent_id2"),
				 (agent_is_non_player, ":cached_agent_id2"),
				 (agent_get_ammo, ":cached_ammo2", ":cached_agent_id2", 0),
				(try_begin),
					(le,":cached_ammo2",0),
					(agent_get_troop_id, ":troop_id", ":cached_agent_id"),
					(neg|is_between,":troop_id",infested_mut_begin,infested_end),
					(agent_set_slot, ":cached_agent_id2",  slot_agent_is_running_away, 1),
					 (agent_set_slot, ":cached_agent_id2", slot_agent_courage_score, 0),
					(agent_start_running_away, ":cached_agent_id2"),
				(try_end),
			(try_end),
          (try_end),
        (else_try),
          (lt, ":horse", 0),
          # (agent_slot_ge, ":horse", slot_agent_horse_prop, 0),

          # (agent_get_slot, ":prop", ":horse", slot_agent_horse_prop),
          # (scene_prop_set_slot, ":prop", scene_prop_attached_horse, -1),

          # (agent_set_slot, ":agent_id", slot_agent_horse_prop, -1),

          (agent_set_slot, ":agent_id", slot_agent_rides_x, -1),

          (assign,":continue",1),
          (try_begin),
            (agent_get_troop_id, ":troop_id", ":agent_id"),
            (eq, ":troop_id", "trp_chopper_pilot"),
            (assign,":continue",0),
			
			(agent_get_slot, ":instance_no", ":agent_id", slot_agent_horse_prop),
			(call_script, "script_helicopter_crash", ":instance_no", -1), #second paramater is attacker, but unknow here - krag
			#(display_message, "@script_helicopter_crash dismount"),
            (agent_deliver_damage_to_agent, ":agent_id", ":agent_id", 10000),

          (try_end),

                # (display_message, "@car no longer active"),
          (eq,":continue",1),

          (assign, ":weapon_slot", ek_head),
          (try_for_range, ":slot_no", 0, ":weapon_slot"),
            (agent_get_item_slot, ":item_no", ":agent_id", ":slot_no"),
            (gt, ":item_no", -1),
            (item_get_type, ":itp", ":item_no"),
            (this_or_next|is_between, ":itp", itp_type_bow, itp_type_thrown),
            (this_or_next|eq, ":itp", itp_type_pistol),
            (eq, ":itp", itp_type_musket),
            (assign, ":weapon_slot", 0),
          (try_end),
          (try_begin),
            (eq, ":weapon_slot", 0),
            (agent_set_division, ":agent_id", grc_archers),
          (else_try),
            (agent_set_division, ":agent_id", grc_infantry),
          (try_end),
        (try_end),
      (try_end),
    ]),


    ]

bodyguard_triggers = [
 (ti_after_mission_start, 0, ti_once, [(eq, "$bodyguard_off", 0),(neq, "$g_mt_mode", tcm_disguised),(le, "$sneaked_into_town", disguise_none),], #condition for not sneaking in; to exclude prison-breaks, etc change to (eq, "$g_mt_mode", tcm_default")
   [
    #Get number of bodyguards
    (store_skill_level, ":leadership", skl_leadership, "trp_player"),
    (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
    (val_div, ":leadership", 4),
    (val_div, ":renown", 500),
    (store_add, ":max_guards", ":renown", ":leadership"),
    (val_min, ":max_guards", 2),

    (ge, ":max_guards", 1),

    #Get player info
    (get_player_agent_no, "$g_player"),
    (agent_get_team, ":playerteam", "$g_player"),
    (agent_get_horse, ":use_horse", "$g_player"), #If the player spawns with a horse, the bodyguard will too.

    (assign, ":bodyguard_count", 0),
    (party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
    (try_for_range, ":i", 0, ":num_of_stacks"),
        (party_stack_get_troop_id, ":troop_id", "p_main_party", ":i"),
        (neq, ":troop_id", "trp_player"),
        (troop_is_hero, ":troop_id"),
        (neg|troop_is_wounded, ":troop_id"),
        (val_add, ":bodyguard_count", 1),

        (try_begin), #For prison-breaks
            (this_or_next|eq, "$talk_context", tc_escape),
            (eq, "$talk_context", tc_prison_break),
            (troop_set_slot, ":troop_id", slot_troop_will_join_prison_break, 1),
        (try_end),

        (assign, ":entry_point", 0),
        (assign, ":mission_tpl", 0),
        (try_begin),
            (party_slot_eq, "$current_town", slot_party_type, spt_village),
            (assign, ":entry_point", 11), #Village Elder's Entry
            (assign, ":mission_tpl", "mt_village_center"),
        (else_try),
            (this_or_next|eq, "$talk_context", tc_prison_break),
            (this_or_next|eq, "$talk_context", tc_escape),
            (eq, "$talk_context", tc_town_talk),
            (assign, ":entry_point", 24), #Prison Guard's Entry
            #(assign, ":entry_point", 0),#didn't work
            (try_begin),
                (party_slot_eq, "$current_town", slot_party_type, spt_castle),
                (assign, ":mission_tpl", "mt_castle_visit"),
            (else_try),
                (assign, ":mission_tpl", "mt_town_center"),
            (try_end),
        (else_try),
            (eq, "$talk_context", tc_tavern_talk),
            (assign, ":entry_point", 17), #First NPC Tavern Entry
        (try_end),
        (try_begin),
            (neq, "$talk_context", tc_tavern_talk),
            (gt, ":use_horse", 0),
            (mission_tpl_entry_set_override_flags, ":mission_tpl", ":entry_point", 0),
        (try_end),

        (store_current_scene, ":cur_scene"),
        (modify_visitors_at_site, ":cur_scene"),
        (add_visitors_to_current_scene, ":entry_point", ":troop_id", 1),

        (eq, ":bodyguard_count", ":max_guards"),
        (assign, ":num_of_stacks", 0), #Break Loop
    (try_end), #Stack Loop
    (gt, ":bodyguard_count", 0), #If bodyguards spawned...
    (set_show_messages, 0),
    (team_give_order, ":playerteam", 8, mordr_follow), #Division 8 to avoid potential conflicts
    (set_show_messages, 1),
   ]),

 (ti_on_agent_spawn, 0, 0, [(le, "$sneaked_into_town", disguise_none),],
   [
    (store_trigger_param_1, ":agent_id"),
    (agent_get_troop_id, ":troop", ":agent_id"),
    (neq, ":troop", "trp_player"),
    (neq, ":troop", "trp_dog_companion"),
    (neq, ":troop", "trp_bot_companion"),
    (troop_is_hero, ":troop"),
    (main_party_has_troop, ":troop"),

    (get_player_agent_no, "$g_player"),
    (agent_get_team, ":playerteam", "$g_player"),
    (agent_get_position,pos1,"$g_player"),

    (agent_set_team, ":agent_id", ":playerteam"),
    (agent_set_division, ":agent_id", 8),
    (agent_add_relation_with_agent, ":agent_id", "$g_player", 1),
    (agent_set_is_alarmed, ":agent_id", 1),
    (store_random_in_range, ":shift", 1, 3),
    (val_mul, ":shift", 100),
    (position_move_y, pos1, ":shift"),
    (store_random_in_range, ":shift", 1, 3),
    (store_random_in_range, ":shift_2", 0, 2),
    (val_mul, ":shift_2", -1),
    (try_begin),
        (neq, ":shift_2", 0),
        (val_mul, ":shift", ":shift_2"),
    (try_end),
    (position_move_x, pos1, ":shift"),
    (agent_set_position, ":agent_id", pos1),
	(agent_set_slot, ":agent_id", slot_agent_is_bodyguard, 1),
   ]),

 (ti_on_agent_killed_or_wounded, 0, 0, [(le, "$sneaked_into_town", disguise_none),],
    [
     (store_trigger_param_1, ":dead_agent"),

     (agent_get_troop_id, ":troop", ":dead_agent"),
     (neq, ":troop", "trp_player"),
     (troop_is_hero, ":troop"),
     (main_party_has_troop, ":troop"),
     (party_wound_members, "p_main_party", ":troop", 1),
    ]),
 ]

tocan_center_attack = [
    (ti_before_mission_start, 0, 0,
      [
        (neg|is_currently_night),
        (party_slot_ge, "$current_town", slot_center_has_attacker,1),
        (neg|troop_slot_eq, "trp_hired_assassin", slot_troop_cur_center, "$current_town"),
        (neg|troop_slot_eq, "trp_belligerent_drunk", slot_troop_cur_center, "$current_town"),
        (neg|troop_slot_eq, "trp_fight_promoter", slot_troop_cur_center, "$current_town"),

      ],
      [
        (party_set_slot, "$current_town", slot_center_has_attacker, 2),
        (assign, "$g_one_second_timer", 0),   #here until later
        ]),
    (0, 0, 1, [
        (party_slot_eq, "$current_town", slot_center_has_attacker,2),
        ],
        [
            (val_add, "$g_one_second_timer", 1),
        ]),
    (1, 0, ti_once,    [
        (party_slot_eq, "$current_town", slot_center_has_attacker,2),
        (store_random_in_range,":begin",30,180),
        (gt,"$g_one_second_timer",":begin"),
		(eq,"$has_prison_key",0),	#krag robbery added these 3 lines to stop interferance/bugs during robbery/breakout
		(eq,"$has_castle_key",0),
		(eq,"$robbery_in_progress",0),
		(neg|quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"), #seems to cause bugs when fugitive is here
        ],
        [
        (call_script,"script_cf_center_attack"),
        ]),

    (3, 0, 0,
        [
            # (eq,"$town_battle",2),
            (party_slot_eq, "$current_town", slot_center_has_attacker,3),
            (neg|main_hero_fallen,0),
            (store_mission_timer_a, ":time"),
            (ge, ":time", 10),
            (all_enemies_defeated),
        ],
        [
            # (assign,"$town_battle",0),
            # (finish_party_battle_mode),
            (party_set_slot, "$current_town", slot_center_has_attacker, -1),
            (display_message,"@No more enemies.",message_alert),
            # (get_player_agent_no, "$g_player"),
            (agent_get_kill_count, ":killcount", "$g_player"),
            (agent_get_kill_count, ":woundcount", "$g_player", 1),
            (store_add, reg1, ":killcount", ":woundcount"),
            (try_begin),
                (ge,reg1,1),
                (call_script, "script_change_player_relation_with_center", "$current_town", reg1),#was 1
            (try_end),
            (finish_party_battle_mode),
            (try_for_agents, ":agent_id"),
                (agent_is_non_player, ":agent_id"),
                (agent_is_alive, ":agent_id"),
                (agent_is_human, ":agent_id"),
                (agent_is_non_player, ":agent_id"),
                (agent_set_team, ":agent_id", 7),

                (agent_clear_scripted_mode, ":agent_id"),
                (agent_set_slot, ":agent_id", slot_agent_is_running_away, 0),
                (agent_set_speed_limit, ":agent_id", 5),
                (agent_force_rethink, ":agent_id"),
            (try_end),
            (call_script, "script_tick_town_walkers"),
            (mission_enable_talk),
             # (finish_mission,0)
    ]),

	(0, 0, 0,    [		#krag add for testing
		(is_edit_mode_enabled),
		(key_clicked, key_enter),
        ],
        [
        (party_set_slot, "$current_town", slot_center_has_attacker, 2),
		(call_script,"script_cf_center_attack"),
        ]),
    ]

particle_preview = (0, 0, 0,
    [
      (ge, "$cheat_mode", 1),
      (key_clicked, key_enter), # replace with any button you want
      (neg|is_presentation_active, "prsnt_particle_preview"), # every presentation call spawns a new plate, so we have to check if it is spawned already
    ],
    [
      (start_presentation, "prsnt_particle_preview"),])

common_auto_fire_new = (0.1, 0, 0,
  [
  #(eq,1,2)
  ],
  [
    (try_for_agents, ":shooter_agent"),
      (agent_is_alive, ":shooter_agent"),
      (agent_is_non_player, ":shooter_agent"),

      (agent_get_wielded_item, ":cur_weapon", ":shooter_agent", 0),
      (try_begin),
        (gt, ":cur_weapon", -1),
        # (is_between, ":cur_weapon", ai_ranged_weapons_begin, ai_ranged_weapons_end),
        (item_slot_eq, ":cur_weapon", slot_item_has_autofire, 1),

		#krag switched to only check when shooting so they don't do it when lining up shots
        (agent_get_animation, ":shooter_stance", ":shooter_agent", 1),
        # (this_or_next|eq, ":shooter_stance", "anim_ready_bow"),
        # (this_or_next|eq, ":shooter_stance", "anim_ready_crossbow"),
        # (this_or_next|eq, ":shooter_stance", "anim_ready_javelin"),
        (this_or_next|eq, ":shooter_stance", "anim_release_musket"),
        (this_or_next|eq, ":shooter_stance", "anim_release_musket_higher_piority"),
        #(this_or_next|eq, ":shooter_stance", "anim_release_pistol"),
        (eq, ":shooter_stance", "anim_release_pistol"),
        #(this_or_next|eq, ":shooter_stance", "anim_ready_pistol"),
        #(eq, ":shooter_stance", "anim_ready_musket"),

        # (agent_is_non_player, ":shooter_agent"),
        (agent_get_combat_state, ":cur_state", ":shooter_agent"),
        (this_or_next|eq, ":cur_state", 1), #krag added this as they otherwise only fire twice, so I assume the other states only last a very short time
        (this_or_next|eq, ":cur_state", 3),
        (eq, ":cur_state", 4), #tocan test

        (assign, ":ammo_item", 0),
        (try_for_range, ":cur_slot", 0, 4),
          (agent_get_item_slot, ":cur_item", ":shooter_agent", ":cur_slot"),
          (try_begin),
            (eq, ":cur_item", ":cur_weapon"),
            (assign, ":weapon_slot", ":cur_slot"),
          (else_try),
            (is_between, ":cur_item", firearm_ammo_begin, firearm_ammo_end),
            (assign, ":ammo_item", ":cur_item"),
          (try_end),
        (try_end),
        (gt, ":ammo_item", 0),

        (agent_get_ammo_for_slot, ":ammo", ":shooter_agent", ":weapon_slot"),
        (gt, ":ammo", 0),


		#krag disabled this as it seemed to interfere with stuff
        # (try_begin),
          # (item_has_capability, ":cur_weapon", itcf_shoot_pistol),
		  # (eq, ":shooter_stance", "anim_ready_pistol"),
          # (agent_set_animation, ":shooter_agent", "anim_release_pistol", 1),
        # (else_try),
          # (eq, ":shooter_stance", "anim_ready_musket"),
		  # (agent_set_animation, ":shooter_agent", "anim_release_musket", 1),
        # (try_end),

		#krag addition
		(assign, ":continue", 0),
		(try_begin),
			#(this_or_next|is_between, ":cur_weapon", lmg_begin, mg_end), #heavy weapons always auto
			#(this_or_next|is_between, ":cur_weapon", lmg_ai_begin_2h, mg_ai_end_2h), #heavy weapons always auto
			(is_between, ":cur_weapon", lmg_ai_begin, mg_ai_end), #heavy weapons always auto
			(assign, ":continue", 1),	#this section isn't working? they don't auto at long range
			#(display_message, "@lmg"),
		  (else_try),
			#(eq, ":continue", 0),
			(agent_ai_get_look_target, ":target_agent", ":shooter_agent"),
			(gt, ":target_agent", 0),
			(agent_get_position, pos41, ":shooter_agent"),
			(agent_get_position, pos42, ":target_agent"),
			(get_distance_between_positions_in_meters, ":distance", pos41, pos42),
			(item_get_accuracy, ":cur_weapon_accuracy", ":cur_weapon"),
			(lt, ":distance", ":cur_weapon_accuracy"),
			(assign, ":continue", 1),
		(try_end),
		(eq, ":continue", 1),

		(val_sub, ":ammo", 1),#moved this here
        (agent_set_ammo, ":shooter_agent", ":cur_weapon", ":ammo"),

        (call_script, "script_ai_autofire", ":shooter_agent", ":cur_weapon", ":ammo_item"),
		(agent_set_animation, ":shooter_agent", "anim_release_musket_higher_piority", 1),
      (else_try),
        (agent_get_slot, ":effective_shots", ":shooter_agent", slot_agent_effective_shots),
        (gt, ":effective_shots", 0),
        (val_sub, ":effective_shots", 1),
        (agent_set_slot, ":shooter_agent", slot_agent_effective_shots, ":effective_shots"),
      (try_end),
    (try_end),
   ])

tocan_autofire = [
  common_auto_fire_new,
  ]

#######################################################################################################################################

##diplomacy begin

dplmc_random_mixed_gender = (ti_on_agent_spawn, 0, 0, [
],
  [
  (store_trigger_param_1, ":agent_no"),
  (agent_is_human, ":agent_no"),
  (agent_get_troop_id, ":troop_no", ":agent_no"),
  (neg|troop_is_hero, ":troop_no"),
  (is_between, ":troop_no", soldiers_begin, soldiers_end),
  (neg|is_between, ":troop_no", "trp_follower_woman", mercenary_troops_end),
  (neq, ":troop_no","trp_jackal_raider"),
  (neq, ":troop_no","trp_jackal_predator"),
  (neq, ":troop_no","trp_jackal_marauder"),
  (neq, ":troop_no","trp_jackal_chieftain"),
  (neq, ":troop_no","trp_sea_raider"),
  (neq, ":troop_no","trp_f3_terror"),
  (neq, ":troop_no","trp_peasant_woman"),
  (neq, ":troop_no","trp_traveler_w"),

  #get individual faction chances
  (store_faction_of_troop, ":faction_no", ":troop_no"),
  (neq, ":faction_no", "fac_infected"),
  (neq, ":faction_no", "fac_mutants"),
  (try_begin),
    (agent_get_party_id, ":party_no", ":agent_no"),
    (party_is_active, ":party_no"),
    (store_faction_of_party, ":party_faction", ":party_no"),
    (eq, ":party_faction", "$players_kingdom"),
    (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":party_faction"),
    (ge, reg0, DPLMC_FACTION_STANDING_LEADER),
    (assign, ":faction_no", "fac_player_supporters_faction"),
  (try_end),
  (faction_get_slot, ":ratio", ":faction_no", slot_faction_gender_ratio),
  (store_random_in_range, ":gender", -100, ":ratio"),
  (try_begin),
    (le, ":gender", 0),
    (troop_set_type, ":troop_no", tf_man),
  (else_try),
    (troop_set_type, ":troop_no", tf_woman),
  (try_end),
  ])


#alternate mouse camera
##BEAN BEGIN - Deathcam
common_move_deathcam = (
    0, 0, 0,
    [
        (main_hero_fallen),
        (eq, "$g_dplmc_battle_continuation", 0),

        (eq, "$g_dplmc_cam_activated", camera_mouse),
        (this_or_next|game_key_is_down, gk_move_forward),
        (this_or_next|game_key_is_down, gk_move_backward),
        (this_or_next|game_key_is_down, gk_move_left),
        (this_or_next|game_key_is_down, gk_move_right),
        (this_or_next|key_is_down, "$g_cam_tilt_left"),
        (this_or_next|key_is_down, "$g_cam_tilt_right"),
        (this_or_next|key_is_down, "$g_camera_adjust_sub"),
        (this_or_next|key_is_down, "$g_camera_adjust_add"),
        (this_or_next|key_clicked, key_home),
        (game_key_is_down, gk_zoom),
    ],
    [
        (set_fixed_point_multiplier, 10000),
        (mission_cam_get_position, pos47),

        # (try_begin),
        # (key_clicked, key_home),
            # (position_set_x, pos47, "$deathcam_death_pos_x"),
            # (position_set_y, pos47, "$deathcam_death_pos_y"),
            # (position_set_z, pos47, "$deathcam_death_pos_z"),
        # (try_end),

        (assign, ":move_x", 0),
        (assign, ":move_y", 0),
        (assign, ":move_z", 0),

        (try_begin),
          (game_key_is_down, gk_move_forward),
          (val_add, ":move_y", 10),
        (else_try),
          (game_key_is_down, gk_move_backward),
          (val_add, ":move_y", -10),
        (try_end),

        (try_begin),
          (game_key_is_down, gk_move_right),
          (val_add, ":move_x", 10),
        (else_try),
          (game_key_is_down, gk_move_left),
          (val_add, ":move_x", -10),
        (try_end),

        (try_begin),
          (key_is_down, "$g_camera_adjust_add"),
          (val_add, ":move_z", 10),
        (else_try),
          (key_is_down, "$g_camera_adjust_sub"),
          (val_add, ":move_z", -10),
        (try_end),

        (try_begin),
          (game_key_is_down, gk_zoom),
          (val_mul, ":move_x", 4),
          (val_mul, ":move_y", 4),
          (val_mul, ":move_z", 2),
        (try_end),

        (position_move_x, pos47, ":move_x"),
        (position_move_y, pos47, ":move_y"),
        (position_move_z, pos47, ":move_z"),

        (mission_cam_set_position, pos47),

        (try_begin),
          (key_is_down, "$g_cam_tilt_left"),
          (ge, "$deathcam_sensitivity_x", 4), #Negative check.
          (ge, "$deathcam_sensitivity_y", 3),
          (val_sub, "$deathcam_sensitivity_x", 4),
          (val_sub, "$deathcam_sensitivity_y", 3),
          (store_mod, reg6, "$deathcam_sensitivity_x", 100), #25% increments
          (store_mod, reg7, "$deathcam_sensitivity_y", 75),
          (try_begin),
            (eq, reg6, 0),
            (eq, reg7, 0),
            (assign, reg8, "$deathcam_sensitivity_x"),
            (assign, reg9, "$deathcam_sensitivity_y"),
            (display_message, "@Sensitivity - 25% ({reg8}, {reg9})"),
          (try_end),
        (else_try),
          (key_is_down, "$g_cam_tilt_right"),
          (val_add, "$deathcam_sensitivity_x", 4),
          (val_add, "$deathcam_sensitivity_y", 3),
          (store_mod, reg6, "$deathcam_sensitivity_x", 100), #25% increments
          (store_mod, reg7, "$deathcam_sensitivity_y", 75),
          (try_begin),
            (eq, reg6, 0),
            (eq, reg7, 0),
            (assign, reg8, "$deathcam_sensitivity_x"),
            (assign, reg9, "$deathcam_sensitivity_y"),
            (display_message, "@Sensitivity + 25% ({reg8}, {reg9})"),
          (try_end),
      (try_end),
   ]
)

common_rotate_deathcam = (
    0, 0, 0,
    [
        (main_hero_fallen),
        (eq, "$g_dplmc_battle_continuation", 0),
        (eq, "$g_dplmc_cam_activated", camera_mouse),
    ],
    [
        (set_fixed_point_multiplier, 10000), #Extra Precision

        (try_begin),
            (this_or_next|is_presentation_active, "prsnt_battle"), #Opened (mouse must move)
            (this_or_next|key_clicked, key_escape), #Menu
            (this_or_next|key_clicked, key_q), #Notes, etc
            (key_clicked, key_tab), #Retreat
            (eq, "$deathcam_prsnt_was_active", 0),
            (assign, "$deathcam_prsnt_was_active", 1),
            (assign, "$deathcam_mouse_last_notmoved_x", "$deathcam_mouse_notmoved_x"),
            (assign, "$deathcam_mouse_last_notmoved_y", "$deathcam_mouse_notmoved_y"),
        (try_end),

        (assign, ":continue", 0),

        (try_begin),
            (neg|is_presentation_active, "prsnt_battle"),
            (mouse_get_position, pos1), #Get and set mouse position
            (position_get_x, reg1, pos1),
            (position_get_y, reg2, pos1),

            (mission_cam_get_position, pos47),

            (try_begin),
            (neq, "$deathcam_prsnt_was_active", 1),
                (try_begin), #Check not moved
                (eq, reg1, "$deathcam_mouse_last_x"),
                (eq, reg2, "$deathcam_mouse_last_y"),
                (this_or_next|neq, reg1, "$deathcam_mouse_notmoved_x"),
                (neq, reg2, "$deathcam_mouse_notmoved_y"),
                    (val_add, "$deathcam_mouse_notmoved_counter", 1),
                    (try_begin), #Notmoved for n cycles
                    (ge, "$deathcam_mouse_notmoved_counter", 15),
                        (assign, "$deathcam_mouse_notmoved_counter", 0),
                        (assign, "$deathcam_mouse_notmoved_x", reg1),
                        (assign, "$deathcam_mouse_notmoved_y", reg2),
                    (try_end),
                (else_try), #Has moved
                    (assign, ":continue", 1),
                    (assign, "$deathcam_mouse_notmoved_counter", 0),
                (try_end),
                (assign, "$deathcam_mouse_last_x", reg1), #Next cycle, this pos = last pos
                (assign, "$deathcam_mouse_last_y", reg2),
            (else_try), #prsnt was active
                (try_begin),
                (neq, reg1, "$deathcam_mouse_last_x"), #Is moving
                (neq, reg2, "$deathcam_mouse_last_y"),
                    (store_sub, ":delta_x2", reg1, "$deathcam_mouse_last_notmoved_x"), #Store pos difference
                    (store_sub, ":delta_y2", reg2, "$deathcam_mouse_last_notmoved_y"),
                (is_between, ":delta_x2", -10, 11), #when engine recenters mouse, there is a small gap
                (is_between, ":delta_y2", -10, 11), #usually 5 pixels, but did 10 to be safe.
                    (assign, "$deathcam_prsnt_was_active", 0),
                    (assign, "$deathcam_mouse_notmoved_x", "$deathcam_mouse_last_notmoved_x"),
                    (assign, "$deathcam_mouse_notmoved_y", "$deathcam_mouse_last_notmoved_y"),
                (else_try),
                    (assign, "$deathcam_mouse_notmoved_x", reg1),
                    (assign, "$deathcam_mouse_notmoved_y", reg2),
                (try_end),
                    (assign, "$deathcam_mouse_last_x", reg1), #Next cycle, this pos = last pos
                    (assign, "$deathcam_mouse_last_y", reg2),
            (try_end),
        (try_end),

        (assign, ":delta_x", 0),
        (assign, ":delta_y", 0),
        (assign, ":rotating_horizontal", 0),
        (assign, ":rotating_vertical", 0),

        (try_begin),
          (key_is_down, "$g_camera_rot_left"),
          (try_begin),
            (ge, "$deathcam_keyboard_rotation_x", 0),
            (assign, "$deathcam_keyboard_rotation_x", -20),
          (try_end),
          (val_add, "$deathcam_keyboard_rotation_x", -1),
          (assign, ":continue", 2),
          (assign, ":rotating_horizontal", -1),
        (else_try),
          (key_is_down, "$g_camera_rot_right"),
          (try_begin),
            (le, "$deathcam_keyboard_rotation_x", 0),
            (assign, "$deathcam_keyboard_rotation_x", 20),
          (try_end),
          (val_add, "$deathcam_keyboard_rotation_x", 1),
          (assign, ":continue", 2),
          (assign, ":rotating_horizontal", 1),
        (else_try),
          (assign, "$deathcam_keyboard_rotation_x", 0),
          (assign, ":rotating_horizontal", 0),
        (try_end),

        (try_begin),
          (key_is_down, "$g_camera_rot_up"),
          (try_begin),
            (le, "$deathcam_keyboard_rotation_y", 0),
            (assign, "$deathcam_keyboard_rotation_y", 15),
          (try_end),
          (val_add, "$deathcam_keyboard_rotation_y", 1),
          (assign, ":continue", 2),
          (assign, ":rotating_vertical", 1),
        (else_try),
          (key_is_down, "$g_camera_rot_down"),
          (try_begin),
            (ge, "$deathcam_keyboard_rotation_y", 0),
            (assign, "$deathcam_keyboard_rotation_y", -15),
          (try_end),
          (val_add, "$deathcam_keyboard_rotation_y", -1),
          (assign, ":continue", 2),
          (assign, ":rotating_vertical", -1),
        (else_try),
          (assign, "$deathcam_keyboard_rotation_y", 0),
          (assign, ":rotating_vertical", 0),
        (try_end),

        (try_begin),
          (eq, ":continue", 1),
          (store_sub, ":delta_x", reg1, "$deathcam_mouse_notmoved_x"), #Store pos difference
          (store_sub, ":delta_y", reg2, "$deathcam_mouse_notmoved_y"),
        (else_try),
          (eq, ":continue", 2),
          (try_begin),
            (neq, ":rotating_horizontal", 0),
            (val_clamp, "$deathcam_keyboard_rotation_x", -80, 80),
            (assign, ":delta_x", "$deathcam_keyboard_rotation_x"),
          (try_end),

          (try_begin),
            (neq, ":rotating_vertical", 0),
            (val_clamp, "$deathcam_keyboard_rotation_y", -45, 45),
            (assign, ":delta_y", "$deathcam_keyboard_rotation_y"),
          (try_end),
        (try_end),

        (try_begin),
          (ge, ":continue", 1),
          (val_mul, ":delta_x", "$deathcam_sensitivity_x"),
          (val_mul, ":delta_y", "$deathcam_sensitivity_y"),
          # (val_mul, ":delta_y", "$deathcam_flip_y_multiplier"),

          (val_clamp, ":delta_x", -80000, 80001), #8
          (val_clamp, ":delta_y", -60000, 60001), #6

          (store_mul, ":neg_rotx", "$deathcam_total_rotx", -1),
          (position_rotate_x_floating, pos47, ":neg_rotx"), #Reset x axis to initial state

          (position_rotate_y, pos47, 90), #Barrel roll by 90 degrees to inverse x/z axis
          (position_rotate_x_floating, pos47, ":delta_x"), #Rotate simulated z axis, Horizontal
          (position_rotate_y, pos47, -90), #Reverse

          (position_rotate_x_floating, pos47, "$deathcam_total_rotx"), #Reverse

          (position_rotate_x_floating, pos47, ":delta_y"), #Vertical
          (val_add, "$deathcam_total_rotx", ":delta_y"), #Fix yaw
          (mission_cam_set_position, pos47),
        (try_end),
    ]
)
##BEAN END - Deathcam
#alternate follower camera
custom_commander_camera = (
  0, 0, 0, [
    (main_hero_fallen),
    (eq, "$g_dplmc_battle_continuation", 0),
    (eq, "$g_dplmc_cam_activated", camera_follow),
  ],
  [
    (stop_sound_channel, "$heartbeat"),
    (try_begin),
      (main_hero_fallen),
      (gt, "$dmod_current_agent", -1), #should be -1, but variable gets bugged
      # (agent_is_active, "$dmod_current_agent"),
      (assign, ":player_agent", "$dmod_current_agent"),
      (assign, ":duration", 500),
    (else_try),
      # (get_player_agent_no, ":player_agent"),
      (assign, ":player_agent", "$g_player"),
      (assign, ":duration", 0),#instant
    (try_end),

    #compared to other deathcams these values are kept between missions
    (ge, ":player_agent", 0),
    (assign, ":continue", 0),
    (try_begin),
      (key_is_down, "$g_camera_adjust_add"),
      (val_add, "$g_camera_z", 5),
      (assign, ":continue", 1),
      (try_begin),
        (key_is_down, key_left_control),
        (val_add, "$g_camera_rotate_y", 5),
      (try_end),
    (else_try),
      (key_is_down, "$g_camera_adjust_sub"),
      (val_sub, "$g_camera_z", 5),
      (assign, ":continue", 1),
      (try_begin),
        (key_is_down, key_left_control),
        (val_sub, "$g_camera_rotate_y", 5),
      (try_end),
    (else_try),
      (key_is_down, "$g_camera_rot_up"),
      (val_add, "$g_camera_y", 5),
      (assign, ":continue", 1),
      (try_begin),
        (key_is_down, key_left_control),
        (val_add, "$g_camera_rotate_x", 5),
      (try_end),
    (else_try),
      (key_is_down, "$g_camera_rot_down"),
      (val_sub, "$g_camera_y", 5),
      (assign, ":continue", 1),
      (try_begin),
        (key_is_down, key_left_control),
        (val_sub, "$g_camera_rotate_x", 5),
      (try_end),
    (try_end),

    (try_begin),
      (key_is_down, key_left_control),
      (try_begin),
        (key_is_down, "$g_camera_rot_left"),
        (val_sub, "$g_camera_rotate_y", 5),
      (else_try),
        (key_is_down, "$g_camera_rot_right"),
        (val_add, "$g_camera_rotate_y", 5),
      (try_end),
    (try_end),
    (try_begin), #any key pressed, immediate update
      (eq, ":continue", 1),
      #no headless mode
      (set_camera_in_first_person, 0),
      (assign, ":duration", 0),
      (mission_cam_set_mode, 1),
    (try_end),

    (agent_get_look_position, pos47, ":player_agent"),
    #moving around x when following is pointless
    (position_move_z, pos47, "$g_camera_z"),
    (position_move_y, pos47, "$g_camera_y"),

    (position_rotate_z, pos47, "$g_camera_rotate_z"),
    #rot x is the only one that makes sense, other rotations tilt too much
    (position_rotate_x, pos47, "$g_camera_rotate_x"),
    (position_rotate_y, pos47, "$g_camera_rotate_y"),
    (agent_get_horse, ":horse_agent", ":player_agent"),
    (try_begin),
      (ge, ":horse_agent", 0),
      (position_move_z, pos47, 90),
      (val_div, ":duration", 2),#mounted agents need to refresh faster
    (try_end),

    #prevent clipping underground
    (position_get_distance_to_ground_level, ":height", pos47),
    (try_begin), #centimeters?
      (le, ":height", 0),
      (position_set_z_to_ground_level, pos47),
      (position_move_z, pos47, 15), #keep around knee height?
    (try_end),

    (try_begin), #if we don't cancel during first person, head disappears
      (call_script, "script_cf_cancel_camera_keys"),
      (neg|main_hero_fallen),
    (else_try),
      (gt, ":duration", 0), #if 0, won't animate at all
      # (eq, "$dmod_move_camera", 1),
      (mission_cam_animate_to_position, pos47, ":duration", 0),
    (else_try), #this allows moving with the troop every frame
      (mission_cam_set_position, pos47),
    (try_end),
  ])

deathcam_cycle_forwards = (0, 0.5, 1,[
        (this_or_next|key_clicked, key_mouse_scroll_up),
        (key_clicked, "$g_cam_tilt_left"),
        (main_hero_fallen),
        (eq, "$g_dplmc_battle_continuation", 0),
        (eq, "$g_dplmc_cam_activated", camera_follow),
        ],
        [(call_script, "script_dmod_cycle_forwards"),])

deathcam_cycle_backwards = (0, 0.5, 1,[
(this_or_next|key_clicked, key_mouse_scroll_down),
(key_clicked, "$g_cam_tilt_right"),
(main_hero_fallen),
(eq, "$g_dplmc_battle_continuation", 0),
(eq, "$g_dplmc_cam_activated", camera_follow),
        ],
        [(call_script, "script_dmod_cycle_backwards"),])

#default keyboard camera
dplmc_death_camera = (
  0, 0, 0,
  [
   (main_hero_fallen),
   (eq, "$g_dplmc_battle_continuation", 0),
   (eq, "$g_dplmc_cam_activated", camera_keyboard),

  ],
  [
    #(agent_get_look_position, pos47, "$g_player"),

    # (get_player_agent_no, "$g_player"),
    # (agent_get_team, ":player_team", "$g_player"),

    (stop_sound_channel, "$heartbeat"),

    (mission_cam_get_position, pos47),

    (assign, ":camera_rotate_x", 0),
    (assign, ":camera_rotate_y", 0),
    (assign, ":camera_rotate_z", 0),
    (assign, ":camera_x", 0),
    (assign, ":camera_y", 0),
    (assign, ":camera_z", 0),

    (try_begin),
      (game_key_is_down, gk_move_left),
      (val_sub, ":camera_x", 10),
    (else_try),
      (game_key_is_down, gk_move_right),
      (val_add, ":camera_x", 10),
    (try_end),
    (position_move_x, pos47, ":camera_x"),

    (try_begin),
      (game_key_is_down, gk_move_forward),
      (val_add, ":camera_y", 10),
    (else_try),
      (game_key_is_down, gk_move_backward),
      (val_sub, ":camera_y", 10),
    (try_end),
    (position_move_y, pos47, ":camera_y"),

    (try_begin),
      (key_is_down, "$g_camera_adjust_add"),
      (val_add, ":camera_z", 10),
    (else_try),
      (key_is_down, "$g_camera_adjust_sub"),
      (val_sub, ":camera_z", 10),
    (try_end),
    (position_move_z, pos47, ":camera_z"),

    (try_begin),
      (key_is_down, "$g_camera_rot_left"),
      (val_add, ":camera_rotate_z", 1),
    (else_try),
      (key_is_down, "$g_camera_rot_right"),
      (val_sub, ":camera_rotate_z", 1),
    (try_end),
    (position_rotate_z, pos47, ":camera_rotate_z"),

    (try_begin),
      (key_is_down, "$g_cam_tilt_left"),
      (val_add, ":camera_rotate_y", 1),
    (else_try),
      (key_is_down, "$g_cam_tilt_right"),
      (val_sub, ":camera_rotate_y", 1),
    (try_end),
    (position_rotate_y, pos47, ":camera_rotate_y"),

    (try_begin),
      (key_is_down, "$g_camera_rot_up"),
      (val_add, ":camera_rotate_x", 1),
    (else_try),
      (key_is_down, "$g_camera_rot_down"),
      (val_sub, ":camera_rotate_x", 1),
    (try_end),
    (position_rotate_x, pos47, ":camera_rotate_x"),

    (try_begin),
      (call_script, "script_cf_cancel_camera_keys"),
    (else_try),
      (mission_cam_set_mode, 1),
      (mission_cam_set_position, pos47),
    (try_end),
  ])

autocover = (	#also player_fallen_so_allies_seek_cover - krag
	0.1, 0, 0, [
	(ge, "$g_covers_active", 1),
	(this_or_next|ge, "$g_autocover", 1),
	(ge, "$player_fallen_so_allies_seek_cover", 1),
	(neq,"$g_battle_won",1),#stop firing after won
	],
	[
	(set_fixed_point_multiplier, 1), #needed?
	(assign, ":radius",  3500), #was 15000
	#(assign, ":radius",  5000), #50m, then 100 then 200
	(try_begin),
		#(main_hero_fallen),
		#(ge, "$player_fallen_so_allies_seek_cover", 1),
		#(store_div, reg11,  ":radius", 100),
		#(display_message, "@Your troops seek cover after you fall (if possible)."),
	  #(else_try),
		(ge, "$g_autocover", 1),
		(assign, ":radius", "$g_cover_order_radius"),
		(val_div, ":radius", 4),
		#(store_div, reg11,  ":radius", 100),
		#(display_message, "@Autocover: Your troops seek cover {reg11}m from your position."),
	(try_end),
	#(assign, ":radius",  5000), #50m, then 100 then 200

	#(get_player_agent_no, "$g_player"),
	##(agent_get_position, pos65, "$g_player"), #changed to agent themselves
	#(call_script, "script_cover_search_player", pos26, ":radius"),
	#(copy_position, pos65, ":order_pos"),

	(scene_prop_get_num_instances, ":total", "spr_cover"),
	(scene_prop_get_num_instances, ":total2", "spr_cover_enemy"),

	#(assign, ":stop", 0),
	(assign, ":unchecked_agents", 0),
	(assign, reg11, 0),
	(assign, reg12, 0),
	(assign, reg13, 0),
	#(store_random_in_range, ":rand", 0, 3),
    (try_for_agents, ":agent_id"),
      (eq, reg11, 0),
	  (gt,":agent_id", 0),
	  (agent_is_alive,":agent_id"),
	  (agent_get_team  ,":agent_team", ":agent_id"),
      (eq,":agent_team","$g_player_team"),
	  (try_begin),
		#(agent_slot_eq, ":agent_id", slot_agent_cover_cycle,0),#check only one agent
		(neg|agent_slot_ge, ":agent_id", slot_agent_cover_cycle,1), #0
		(agent_set_slot, ":agent_id", slot_agent_cover_cycle, 1),
		(val_add, ":unchecked_agents", 1),
	    (assign, reg11, 1),
	    (assign, reg12, 1),
	  #(else_try),
		#(agent_slot_eq, ":agent_id", slot_agent_cover_cycle,1),
		#(agent_slot_ge, ":agent_id", slot_agent_take_cover,0),
		#(agent_set_slot, ":agent_id", slot_agent_cover_cycle, 0),
	  (try_end),
	  (eq, reg12, 1),


	  #(eq, ":stop", 0),
	  (agent_slot_eq, ":agent_id", slot_agent_has_ranged,1),
      (agent_slot_eq, ":agent_id", slot_agent_take_cover,-1),
      (neg|agent_slot_ge, ":agent_id", slot_agent_horse_prop,0),
      (agent_is_active, ":agent_id"),
      #(agent_is_alive,":agent_id"),
      (agent_is_human,":agent_id"),
      (agent_is_non_player, ":agent_id"),

      # (agent_get_team  ,":agent_team", ":agent_id"),
      # (eq,":agent_team","$g_player_team"), #same team as player

      (agent_get_class,":class", ":agent_id"),
      (this_or_next|eq,":class","$g_class_listening"), #class or all
      (eq,"$g_class_listening",grc_everyone),

      (agent_get_horse, ":horse", ":agent_id"),
      (eq, ":horse", -1), #should not be mounted
      (agent_get_wielded_item, ":wielded_item", ":agent_id", 0),
      (gt, ":wielded_item", -1),
      # (is_between, ":wielded_item", ranged_weapons_begin, ranged_weapons_end),  #only ranged for now
      (item_get_type, ":item_type", ":wielded_item"),

	  #(str_store_agent_name, s23, ":agent_id"),
	  #(str_store_item_name, s24, ":wielded_item"),
	  #(display_message, "@{s23} wielding {s24}", message_negative),

      (this_or_next|is_between, ":wielded_item", grenades_begin, grenades_end),#why no work?! - krag
      (this_or_next|eq, ":item_type", itp_type_bow),
      #(this_or_next|eq, ":item_type", itp_type_crossbow),
      (this_or_next|eq, ":item_type", itp_type_pistol),
      (eq, ":item_type", itp_type_musket),

	  #(assign, reg11, 0),
	  (agent_get_position,pos65,":agent_id"),
	  (call_script, "script_cover_search_player_single_agent", ":radius", ":agent_id", ":total", ":total2"),
	  (try_begin),
		(eq, reg13, 0),
		(store_random_in_range, ":rand", 0, 3),
		(le, ":rand", 1),
		(val_mul, ":radius", 2),
		#(display_message, "@doubling radius"),
		(call_script, "script_cover_search_player_single_agent", ":radius", ":agent_id", ":total", ":total2"),
		(try_begin),
			(eq, reg13, 0),
			(le, ":rand", 2),
			(val_mul, ":radius", 2),
			#(display_message, "@quadrupling radius"),
			(call_script, "script_cover_search_player_single_agent", ":radius", ":agent_id", ":total", ":total2"),
		  (try_end),
	  (try_end),
	(try_end),

	(try_begin),
		(eq, ":unchecked_agents", 0),
		#(display_message, "@unchecked agents  = 0"),
		(try_for_agents, ":agent_id"),
			(agent_is_alive,":agent_id"),
			(agent_get_team  ,":agent_team", ":agent_id"),
			(eq,":agent_team","$g_player_team"),
			(agent_set_slot, ":agent_id", slot_agent_cover_cycle, 0),
		(try_end),
	(try_end),
])

autocover_ai = (	#also player_fallen_so_allies_seek_cover - krag
	0.1, 0, 0, [
	(ge, "$g_covers_active", 1),
	(ge, "$g_autocover_ai", 1),
	],
	[
	(set_fixed_point_multiplier, 1), #needed?
	(assign, ":radius",  1250), #50m at max
	#(display_message, "@autocover_ai"),

	#(scene_prop_get_num_instances, ":total", "spr_cover"),
	#(scene_prop_get_num_instances, ":total2", "spr_cover_enemy"),

	(scene_prop_get_num_instances, ":total_spr_cover", "spr_cover"),
	#(assign, reg24, ":total_spr_cover"),
	(scene_prop_get_num_instances, ":total_spr_cover_enemy", "spr_cover_enemy"),
	#(assign, reg25, ":total_spr_cover_enemy"),
	#(display_message, "@cover: {reg24},  cover_enemy: {reg25}"),



	#(assign, ":stop", 0),
	(assign, ":unchecked_agents", 0),
	(assign, reg11, 0),
	(assign, reg12, 0),
	(assign, reg13, 0),
	#(store_random_in_range, ":rand", 0, 3),
    (try_for_agents, ":agent_id"),
      (eq, reg11, 0),
	  (agent_is_alive,":agent_id"),
	  (agent_get_team  ,":agent_team", ":agent_id"),
      (neq,":agent_team","$g_player_team"),
	  (try_begin),
		#(agent_slot_eq, ":agent_id", slot_agent_cover_cycle,0),#check only one agent
		(neg|agent_slot_ge, ":agent_id", slot_agent_cover_cycle_ai,1), #0
		(agent_set_slot, ":agent_id", slot_agent_cover_cycle_ai, 1),
		(val_add, ":unchecked_agents", 1),
	    (assign, reg11, 1),
	    (assign, reg12, 1),
	  #(else_try),
		#(agent_slot_eq, ":agent_id", slot_agent_cover_cycle,1),
		#(agent_slot_ge, ":agent_id", slot_agent_take_cover,0),
		#(agent_set_slot, ":agent_id", slot_agent_cover_cycle, 0),
	  (try_end),
	  (eq, reg12, 1),


	  #(eq, ":stop", 0),
	  (agent_slot_eq, ":agent_id", slot_agent_has_ranged,1),
      (agent_slot_eq, ":agent_id", slot_agent_take_cover,-1),
      (neg|agent_slot_ge, ":agent_id", slot_agent_horse_prop,0),
      (agent_is_active, ":agent_id"),
      #(agent_is_alive,":agent_id"),
      (agent_is_human,":agent_id"),
      (agent_is_non_player, ":agent_id"),

      # (agent_get_team  ,":agent_team", ":agent_id"),
      # (eq,":agent_team","$g_player_team"), #same team as player

      #(agent_get_class,":class", ":agent_id"),
      #(this_or_next|eq,":class","$g_class_listening"), #class or all
     # (eq,"$g_class_listening",grc_everyone),

      (agent_get_horse, ":horse", ":agent_id"),
      (eq, ":horse", -1), #should not be mounted
      (agent_get_wielded_item, ":wielded_item", ":agent_id", 0),
      (gt, ":wielded_item", -1),
      # (is_between, ":wielded_item", ranged_weapons_begin, ranged_weapons_end),  #only ranged for now
      (item_get_type, ":item_type", ":wielded_item"),
	  (this_or_next|is_between, ":wielded_item", grenades_begin, grenades_end),
      (this_or_next|eq, ":item_type", itp_type_bow),
      #(this_or_next|eq, ":item_type", itp_type_crossbow),
      (this_or_next|eq, ":item_type", itp_type_pistol),
      (eq, ":item_type", itp_type_musket),
	  
	  (agent_get_troop_id, ":troop_id", ":agent_id"),
	  (neg|is_between, ":troop_id", infested_mut_begin, infested_end),

	  (try_begin),
        (neg|teams_are_enemies,":agent_team","$g_player_team"), #same team as player

        (assign,":cover_prop","spr_cover"),
        (assign,":cover_prop_enemy","spr_cover_enemy"),

        (assign,":total",":total_spr_cover"),
        (assign,":total2",":total_spr_cover_enemy"),
       (else_try),
        (assign,":cover_prop","spr_cover_enemy"),
        (assign,":cover_prop_enemy","spr_cover"),

		(assign,":total",":total_spr_cover_enemy"),
        (assign,":total2",":total_spr_cover"),
      (try_end),

	  #(assign, reg11, 0),
	  (agent_get_position,pos65,":agent_id"),
	  (call_script, "script_cover_battle_start_single_agent", ":agent_team", ":radius", ":agent_id", ":total", ":total2", ":cover_prop", ":cover_prop_enemy"),
	  (try_begin),
		(eq, reg13, 0),
		(store_random_in_range, ":rand", 0, 3),
		(le, ":rand", 1),
		(val_mul, ":radius", 2),
		#(display_message, "@doubling radius"),
		(call_script, "script_cover_battle_start_single_agent", ":agent_team", ":radius", ":agent_id", ":total", ":total2", ":cover_prop", ":cover_prop_enemy"),
		(try_begin),
			(eq, reg13, 0),
			(le, ":rand", 2),
			(val_mul, ":radius", 3),
			#(display_message, "@quadrupling radius"),
			(call_script, "script_cover_battle_start_single_agent", ":agent_team", ":radius", ":agent_id", ":total", ":total2", ":cover_prop", ":cover_prop_enemy"),
		  (try_end),
	  (try_end),
	(try_end),

	(try_begin),
		(eq, ":unchecked_agents", 0),
		#(display_message, "@unchecked_agents  = 0"),
		(try_for_agents, ":agent_id"),
			(agent_is_alive,":agent_id"),
			(agent_get_team  ,":agent_team", ":agent_id"),
			(neq,":agent_team","$g_player_team"),
			(agent_set_slot, ":agent_id", slot_agent_cover_cycle_ai, 0),
		(try_end),
	(try_end),
])

#<<<<<<< HEAD
#some cover seekers (slot_agent_take_cover=0) seem to get stuck near their destination and so never leave "cover", this should - free them. - krag
free_stuck_cover_seekers = (
	5, 0, 0, [
	  ],
       [
       # (display_message, "@agent check"),
	(store_mission_timer_a, ":time"),
	(gt, ":time", 30),
	(try_for_agents, ":agent_id"),
		#(agent_get_slot, ":take_cover", ":agent_id", slot_agent_take_cover),
		 #(eq, ":take_cover", 0),	#seeking cover
		 (agent_slot_eq, ":agent_id", slot_agent_take_cover, 0),
		 
		 (agent_get_animation, ":run", ":agent_id", 0),
       ## (neg|is_between, ":run", "anim_run_forward", "anim_stand_to_crouch"), #standing still
        (is_between, ":run", "anim_stand", "anim_turn_right"), #standing still? might exclude agents who are trapped against others
		 
	   (agent_is_active, ":agent_id"),
        (agent_is_alive, ":agent_id"),
        (agent_is_human, ":agent_id"),
        (agent_is_non_player, ":agent_id"),
		
		(agent_get_attack_action, ":action", ":agent_id"),
		(le, ":action", 0),	#not fighting anyway
		
		(agent_get_ammo, ":ammo", ":agent_id", 0),
		 
		 (agent_get_slot, ":last_hit", ":agent_id", slot_agent_last_time_hit_enemy),	#for leaving cover if not hit for a while - krag
		 (store_sub, ":time_diff", ":time", ":last_hit"),
		 
		  (this_or_next|le, ":ammo", 0),
		  (gt, ":time_diff", 30),
	 
		(agent_get_speed, pos2, ":agent_id"),
        (position_get_y, ":speedy", pos2),
        (position_get_x, ":speedx", pos2),
        (le, ":speedy", 0),	#isn't moving for whatever reason
        (le, ":speedx", 0),
		 
		(agent_get_speed_modifier, reg23, ":agent_id"),
		(gt, reg23, 0),#make sure isn't frozen for some reason
	     
		(agent_get_team, ":agent_team", ":agent_id"),
		(assign, ":continue", 1),
		(try_begin),
			(is_between, "$g_encountered_party", towns_begin, towns_end),
			(this_or_next|eq, ":agent_team", "$defender_team"),
			(eq, ":agent_team", "$defender_team_2"),
			(lt, ":time_diff", 60),
			(assign, ":continue", 0),
		(try_end),
		(eq, ":continue", 1), 
		 
		
		#(agent_get_wielded_item, ":wielded_item", ":agent_id", 0),
		 #(gt, ":wielded_item", 0), might be unarmed
		 # (item_get_type, ":item_type", ":wielded_item"),
		 # (this_or_next|eq, ":item_type", itp_type_one_handed_wpn),
		 # (this_or_next|eq, ":item_type", itp_type_two_handed_wpn),
		 # (eq, ":item_type", itp_type_polearm),
		
	    # (str_store_agent_name, s23, ":agent_id"),
		# (str_store_item_name, s24, ":wielded_item"),
		# (assign, reg25, ":take_cover"),
		# (assign, reg27, ":time_diff"),
		# (assign, reg24, ":action"),
		# (assign, reg26, ":ammo"),
		# #(spawn_scene_prop, "spr_cover_marker"),
		# #(assign, ":marker_prop", reg0),
		# #(agent_set_attached_scene_prop,":agent_id", ":marker_prop"),
		# (display_message, "@{s23} with {s24} has {reg23} speed, action is {reg24}, cover is {reg25}, ammo is {reg26}, time diff is {reg27}.", message_positive),  
		
		(agent_get_slot, ":instance_id", ":agent_id", slot_agent_prop_occupied), #use this for movement
		(try_begin),
			(gt, ":instance_id", -1), 
			(agent_set_slot, ":agent_id", slot_agent_last_cover_used, ":instance_id"),
			(scene_prop_set_slot,":instance_id",scene_prop_cover_occupied,0),
		(try_end),
		
		(agent_set_slot, ":agent_id", slot_agent_prop_occupied, -1),
		(agent_set_slot,":agent_id",slot_agent_take_cover,-1),
		
		(agent_clear_scripted_mode,":agent_id"),
		(agent_force_rethink, ":agent_id"),
		(agent_set_no_dynamics, ":agent_id",0),
    (try_end),
       ])
	
  
#=======

#>>>>>>> 73caf4feef816e1e3cd1718fbe5c34f6e47c4e03

##SB : new camera triggers
dplmc_battle_mode_triggers = [
    dplmc_random_mixed_gender,
    # dplmc_horse_speed,
    common_move_deathcam, common_rotate_deathcam,
    custom_commander_camera, deathcam_cycle_forwards, deathcam_cycle_backwards,
    dplmc_death_camera,
	autocover, #krag piggyback this
	autocover_ai,
  ]
##diplomacy end

common_battle_mission_start = (
  ti_before_mission_start, 0, 0, [],
  [
    (team_set_relation, 0, 2, 1),
    (team_set_relation, 1, 3, 1),
    (call_script, "script_change_banners_and_chest"),
    ])

common_battle_tab_press = (
  ti_tab_pressed, 0, 0, [(neg|is_presentation_active, "prsnt_order_display"),],
  [
    (try_begin),
       (eq, 1, 2),#disable for release
	   (key_is_down, key_left_control),
	   (is_edit_mode_enabled),
	   #(change_screen_quit),#crashes if called directly
	   (finish_mission, 0),
	   (jump_to_menu, "mnu_quit_to_main_menu"),#quick quit during testing. - krag
   (else_try),
      (eq, "$g_battle_won", 1),
      (call_script, "script_count_mission_casualties_from_agents"),
      (finish_mission,0),
    ##diplomacy begin
   (else_try),
      (eq, "$g_dplmc_battle_continuation", 0),
      ##diplomacy start+ Import Caba`drin's battle continuation fix
      (this_or_next|main_hero_fallen),   #CABA EDIT/FIX FOR DEATH CAM
      ##diplomacy end+
      (eq, "$pin_player_fallen", 1),
      (question_box,"str_do_you_want_to_retreat"),
##      (call_script, "script_simulate_retreat", 5, 20),
##      (str_store_string, s5, "str_retreat"),
##      (call_script, "script_count_mission_casualties_from_agents"),
##      (set_mission_result, -1),
##      (finish_mission,0),
    ##diplomacy end
    (else_try),
      (call_script, "script_cf_check_enemies_nearby"),
      (question_box,"str_do_you_want_to_retreat"),
    (else_try),
      (display_message,"str_can_not_retreat",message_alert),
    (try_end),
    ])

common_battle_init_banner = (
  ti_on_agent_spawn, 0, 0, [],
  [
    (store_trigger_param_1, ":agent_no"),
    (agent_get_troop_id, ":troop_no", ":agent_no"),
    (call_script, "script_troop_agent_set_banner", "tableau_game_troop_label_banner", ":agent_no", ":troop_no"),
  ])


common_arena_fight_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (question_box,"str_give_up_fight"),
    ])

common_custom_battle_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (try_begin),
      (neq, "$g_battle_result", 0),
      (call_script, "script_custom_battle_end"),
      (finish_mission),
    (else_try),
      (question_box,"str_give_up_fight"),
    (try_end),
    ])

custom_battle_check_victory_condition = (
  1, 60, ti_once,
  [
    (store_mission_timer_a,reg(1)),
    (ge,reg(1),10),
    (all_enemies_defeated, 2),
    ##diplomacy begin
    (this_or_next|eq, "$g_dplmc_battle_continuation", 0),
    (neg|main_hero_fallen, 0),
    ##diplomacy end
    (set_mission_result,1),
    (display_message,"str_msg_battle_won",message_positive),
    (assign, "$g_battle_won",1),
    (assign, "$g_battle_result", 1),
    ],
  [
    (call_script, "script_custom_battle_end"),
    (finish_mission, 1),
    ])

custom_battle_check_defeat_condition = (
  1, 4,
##diplomacy begin
0,
##diplomacy end
  [
    (main_hero_fallen),
    ##diplomacy begin
    (try_begin),
      (call_script, "script_cf_dplmc_battle_continuation"),
    (else_try),
      ##diplomacy end
      (assign,"$g_battle_result",-1),
      ##diplomacy begin
    (try_end),
    ##diplomacy end
    ],
  [
    (call_script, "script_custom_battle_end"),
    (finish_mission),
    ])

common_battle_victory_display = (
  10, 0, 0, [],
  [
    (eq,"$g_battle_won",1),
    (display_message,"str_msg_battle_won",message_positive),
    ])

common_siege_question_answered = (
  ti_question_answered, 0, 0, [],
   [
     (store_trigger_param_1,":answer"),
     (eq,":answer",0),
     (assign, "$pin_player_fallen", 0),
     # (get_player_agent_no, "$g_player"),
     (agent_get_team, ":agent_team", "$g_player"),
     (try_begin),
       (neq, "$attacker_team", ":agent_team"),
       (neq, "$attacker_team_2", ":agent_team"),
       (str_store_string, s5, "str_siege_continues"),
       (call_script, "script_simulate_retreat", 8, 15, 0),
     (else_try),
       (str_store_string, s5, "str_retreat"),
       (call_script, "script_simulate_retreat", 5, 20, 0),
     (try_end),
     (call_script, "script_count_mission_casualties_from_agents"),
     (finish_mission,0),
     ])

common_siege_init = (
  0, 0, ti_once, [],
  [
    (assign,"$g_battle_won",0),
    (assign,"$defender_reinforcement_stage",0),
    (assign,"$attacker_reinforcement_stage",0),
    # (call_script, "script_music_set_situation_with_culture", mtf_sit_siege),
    (call_script, "script_init_death_cam"), #SB : initialize this here

   ## HOLD ON START
   (get_player_agent_no, "$g_player"),
   (agent_get_team, ":player_team", "$g_player"),
   (set_show_messages, 0),
   (team_give_order, ":player_team", grc_everyone, mordr_hold),
   (set_show_messages, 1),
   ## END HOLD ON START
    ])

# common_music_situation_update = (
  # 30, 0, 0, [],
  # [
    # (call_script, "script_combat_music_set_situation_with_culture"),
    # ])

common_siege_ai_trigger_init = (
  0, 0, ti_once,
  [
    (assign, "$defender_team", 0),
    (assign, "$attacker_team", 1),
    (assign, "$defender_team_2", 2),
    (assign, "$attacker_team_2", 3),
    ], [])

common_siege_ai_trigger_init_after_2_secs = (
  0, 2, ti_once, [],
  [
    (try_for_agents, ":agent_no"),
      (agent_set_slot, ":agent_no", slot_agent_is_not_reinforcement, 1),
    (try_end),
    ])

common_siege_defender_reinforcement_check = (
  3, 0, 5, [],
  [(lt, "$defender_reinforcement_stage", 7),
   (store_mission_timer_a,":mission_time"),
   (ge,":mission_time",10),
   (store_normalized_team_count,":num_defenders",0),
   (lt,":num_defenders",8),
   (add_reinforcements_to_entry,4, 7),
   (val_add,"$defender_reinforcement_stage",1),
   (agent_get_team, ":player_team", "$g_player"),
   (try_begin),
     (gt, ":mission_time", 600), #5 minutes, don't let small armies charge	;extended as charging too early - krag
     # (get_player_agent_no, "$g_player"),
     #(agent_get_team, ":player_team", "$g_player"),
     (neq, ":player_team", "$defender_team"), #player should be the attacker
     (neq, ":player_team", "$defender_team_2"), #player should be the attacker
     (ge, "$defender_reinforcement_stage", 2),
	 (display_message, "@Defenders charging out!"),
     (set_show_messages, 0),
     (team_give_order, "$defender_team", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
     (team_give_order, "$defender_team_2", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
     (team_give_order, "$defender_team", grc_cavalry, mordr_charge), #AI desperate charge:cavalry!!!
     (team_give_order, "$defender_team_2", grc_cavalry, mordr_charge), #AI desperate charge:cavalry!!!
     (set_show_messages, 1),
     (ge, "$defender_reinforcement_stage", 4),
     (set_show_messages, 0),
     (team_give_order, "$defender_team", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
     (team_give_order, "$defender_team_2", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
     (set_show_messages, 1),
   (try_end),
   (try_begin),
		(main_hero_fallen),
		(this_or_next| eq, ":player_team", "$defender_team"),
		(eq, ":player_team", "$defender_team_2"),
		#(assign, "$player_fallen_so_allies_seek_cover", 1),
		(assign, "$g_autocover", 1),
		# (get_player_agent_no, "$g_player"),
		# (agent_get_position, pos26, "$g_player"),
		# (call_script, "script_cover_search_player", pos26, 10000),	#player troops search for cover on death
		# (display_message, "@Your troops seek cover after you fall (if possible)."),
	(try_end),
   ])

common_siege_defender_reinforcement_archer_reposition = (
  2, 0, 0,
  [
    (gt, "$defender_reinforcement_stage", 0),
    ],
  [
    (call_script, "script_siege_move_archers_to_archer_positions"),
    ])

common_siege_attacker_reinforcement_check = (
  1, 0, 5,
  [
    (lt,"$attacker_reinforcement_stage",5),
    (store_mission_timer_a,":mission_time"),
    (ge,":mission_time",10),
    (store_normalized_team_count,":num_attackers",1),
    (lt,":num_attackers",6)
    ],
  [
    (add_reinforcements_to_entry, 1, 8),
    (val_add,"$attacker_reinforcement_stage", 1),
    ])

common_siege_attacker_do_not_stall = (
#  ti_once, 6, 0, [],
  20, 0, 0, [],
  [ #Make sure attackers do not stall on the ladders...
    (try_for_agents, ":agent_no"),
      (agent_is_human, ":agent_no"),
      (agent_is_alive, ":agent_no"),
      (agent_get_team, ":agent_team", ":agent_no"),
	  (agent_get_troop_id, ":troop_id", ":agent_no"),
	  (this_or_next|is_between, ":troop_id", infested_mut_begin, infested_end), #make sure monsters are agressive even if defending
      (this_or_next|eq, ":agent_team", "$attacker_team"),
      (eq, ":agent_team", "$attacker_team_2"),

	  (assign, ":continue", 1),
	  (try_for_range, ":slot", 0, 4),
			(eq, ":continue", 1),
			(agent_get_item_slot, ":item", ":agent_no", ":slot"),
			(ge, ":item", 1),
			(this_or_next|is_between, ":item", sniper_ai_begin, sniper_ai_end),
			(this_or_next|is_between, ":item", lmg_ai_begin, mg_ai_end),
			(item_slot_ge, ":item", slot_item_has_scope, 1),
			(assign, ":continue", 0),
			(agent_ai_set_aggressiveness, ":agent_no", 1),
	  (try_end),
	  (this_or_next|is_between, ":troop_id", infested_mut_begin, infested_end), #make sure monsters are agressive
	  (eq, ":continue", 1),

      (agent_ai_set_always_attack_in_melee, ":agent_no", 1),

	  (agent_get_class, ":class", ":agent_no"),
	  (try_begin),
		(neq, ":class", grc_infantry),
		(agent_ai_set_aggressiveness, ":agent_no", 1),
	   (else_try),
	     (agent_ai_set_aggressiveness, ":agent_no", 250),
	  (try_end),
    (try_end),
    ])

common_siege_attacker_do_not_stall_spawn = (
  ti_on_agent_spawn, 0, 0, [],
  [ #Make sure attackers do not stall on the ladders...
  (store_trigger_param_1, ":agent_no"),
      (agent_is_human, ":agent_no"),
     # (agent_is_alive, ":agent_no"),
      (agent_get_team, ":agent_team", ":agent_no"),
	  (agent_get_troop_id, ":troop_id", ":agent_no"),
	  (this_or_next|is_between, ":troop_id", infested_mut_begin, infested_end), #make sure monsters are agressive even if defending
      (this_or_next|eq, ":agent_team", "$attacker_team"),
      (eq, ":agent_team", "$attacker_team_2"),

	  (assign, ":continue", 1),
	  (try_for_range, ":slot", 0, 4),
			(eq, ":continue", 1),
			(agent_get_item_slot, ":item", ":agent_no", ":slot"),
			(ge, ":item", 1),
			(this_or_next|is_between, ":item", sniper_ai_begin, sniper_ai_end),
			(this_or_next|is_between, ":item", lmg_ai_begin, mg_ai_end),
			(item_slot_ge, ":item", slot_item_has_scope, 1),
			(assign, ":continue", 0),
			(agent_ai_set_aggressiveness, ":agent_no", 1),
	  (try_end),
	  (this_or_next|is_between, ":troop_id", infested_mut_begin, infested_end), #make sure monsters are agressive
	  (eq, ":continue", 1),

     (agent_ai_set_always_attack_in_melee, ":agent_no", 1),
	 (agent_get_class, ":class", ":agent_no"),
	  (try_begin),
		(neq, ":class", grc_infantry),
		(agent_ai_set_aggressiveness, ":agent_no", 1),
	   (else_try),
	     (agent_ai_set_aggressiveness, ":agent_no", 250),
	  (try_end),
    ])


common_battle_check_friendly_kills = (
  2, 0, 0, [],
  [
    (call_script, "script_check_friendly_kills"),
    ])

common_battle_check_victory_condition = (
  1, 60, ti_once,
  [
    (store_mission_timer_a,reg(1)),
    (ge,reg(1),10),
    (all_enemies_defeated, 5),
    ##diplomacy begin
    (this_or_next|eq, "$g_dplmc_battle_continuation", 0),
    (neg|main_hero_fallen),
    ##diplomacy end

    (try_for_agents,":agent_id"),
        (agent_is_alive,":agent_id"),
        (agent_is_human,":agent_id"),
        (agent_slot_ge, ":agent_id", slot_agent_take_cover, 0),
        (agent_clear_scripted_mode,":agent_id"),
        (agent_set_slot, ":agent_id", slot_agent_take_cover, -1),
    (try_end),

    (set_mission_result,1),
    (display_message,"str_msg_battle_won",message_positive),
    (assign,"$g_battle_won",1),
    (assign, "$g_battle_result", 1),
    (call_script, "script_play_victorious_sound"),
    ],
  [
    (call_script, "script_count_mission_casualties_from_agents"),
    (finish_mission, 1),

    ])

common_battle_victory_display = (
  10, 0, 0, [(eq,"$g_battle_won",1),], #SB : moved conditions
  [
    (display_message,"str_msg_battle_won",message_positive),
    ])

common_siege_refill_ammo = (
  300, 0, 0, [],
  # 120, 0, 0, [],
  [#refill ammo of defenders every two minutes.
    # (get_player_agent_no, "$g_player"),
    (try_for_agents,":cur_agent"),
      # (neq, ":cur_agent", "$g_player"),
      (agent_is_alive, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
      (agent_get_team, ":agent_team", ":cur_agent"),
      (this_or_next|eq, ":agent_team", "$defender_team"),
      (eq, ":agent_team", "$defender_team_2"),
      (agent_refill_ammo, ":cur_agent"),
      (try_begin),
        (eq, ":cur_agent","$g_player"),
        (display_message,"@Defender ammunition replenished.", message_positive),
      (try_end),
    (try_end),
    ])

common_siege_check_defeat_condition = (
  1, 4,
##diplomacy begin
0,
##diplomacy end
  [
    (main_hero_fallen)
    ],
  [
    ##diplomacy begin
      (try_begin),
        (call_script, "script_cf_dplmc_battle_continuation"),
      (else_try),
        ##diplomacy end
        (assign, "$pin_player_fallen", 1),
        # (get_player_agent_no, "$g_player"),
        (agent_get_team, ":agent_team", "$g_player"),
        (try_begin),
          (neq, "$attacker_team", ":agent_team"),
          (neq, "$attacker_team_2", ":agent_team"),
          (str_store_string, s5, "str_siege_continues"),
          (call_script, "script_simulate_retreat", 8, 15, 0),
        (else_try),
          (str_store_string, s5, "str_retreat"),
          (call_script, "script_simulate_retreat", 5, 20, 0),
        (try_end),
        (assign, "$g_battle_result", -1),
        (set_mission_result,-1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),
        ##diplomacy begin
      (try_end),
    ##diplomacy end
    ])

common_battle_inventory = (
  ti_inventory_key_pressed, 0, 0, [],
  [
    (try_begin),
        (eq, "$g_special_companion", 2),

        (agent_is_active, "$g_player_x_agent_no"),
        (agent_is_alive, "$g_player_x_agent_no"),

        (agent_get_position, pos1, "$g_player"),
        (agent_get_position, pos2, "$g_player_x_agent_no"),
        (get_distance_between_positions, ":dist", pos1, pos2),
        (lt,":dist",300),
        (set_trigger_result, 1),
    (else_try),
        (eq, "$g_special_companion", 2),

        (display_message,"str_use_baggage_or_bot_for_inventory"),
    (else_try),
        (display_message,"str_use_baggage_for_inventory"),
    (try_end),

    ])

common_inventory_not_available = (
  ti_inventory_key_pressed, 0, 0,
  [
    (display_message, "str_cant_use_inventory_now",message_alert),
    ], [])

#for testing
teleport_to_entry_point = (
	0, 0, 0, [
	(is_edit_mode_enabled),
	(eq,"$cheat_mode",1),
	(key_is_down, key_t),
	],
	[
	(get_player_agent_no, ":player"),

	(try_begin),
		(key_clicked, key_0),
		(entry_point_get_position, pos19, 0),
	  (else_try),
		(key_clicked, key_1),
		(entry_point_get_position, pos19, 1),
	  (else_try),
		(key_clicked, key_2),
		(entry_point_get_position, pos19, 2),
	  (else_try),
		(key_clicked, key_3),
		(entry_point_get_position, pos19, 3),
	  (else_try),
		(key_clicked, key_4),
		(entry_point_get_position, pos19, 4),
	  (else_try),
		(key_clicked, key_5),
		(entry_point_get_position, pos19, 5),
	  (else_try),
		(key_clicked, key_6),
		(entry_point_get_position, pos19, 6),
	  (else_try),
		(key_clicked, key_7),
		(entry_point_get_position, pos19, 7),
	  (else_try),
		(key_clicked, key_8),
		(entry_point_get_position, pos19, 8),
	  (else_try),
		(key_clicked, key_9),
		(entry_point_get_position, pos19, 9),
	  (else_try),
		(key_clicked, key_right_control),
		#(get_camera_position, pos19),
		(mission_cam_get_position, pos19),
	(try_end),

		(position_get_x, ":pos19_x", pos19),
		(neq, ":pos19_x", 0),
		(position_rotate_z, pos19, 180),
		(agent_get_horse, ":player_horse", ":player"),
		(try_begin),
			(eq, ":player_horse", -1),
			(agent_set_position, ":player", pos19),
		  (else_try),
		    (agent_set_position, ":player_horse", pos19),
		(try_end),
		(init_position, pos19),

])


tournament_triggers = [
  (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest"),
                                       (assign, "$g_arena_training_num_agents_spawned", 0)]),
  (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena",message_alert)], []),
  (ti_tab_pressed, 0, 0, [],
   [(try_begin),
      (eq, "$g_mt_mode", abm_visit),
      # (show_object_details_overlay, 1),
      (set_trigger_result, 1),
    (else_try),
      (question_box,"str_give_up_fight"),
    (try_end),
    ]),
  (ti_question_answered, 0, 0, [],
   [(store_trigger_param_1,":answer"),
    (eq,":answer",0),
    (try_begin),
      (eq, "$g_mt_mode", abm_tournament),
      (call_script, "script_end_tournament_fight", 0),
    (else_try),
      (this_or_next|eq, "$g_mt_mode", abm_brawl),
      (eq, "$g_mt_mode", abm_training),
      # (get_player_agent_no, "$g_player"),
      (agent_get_kill_count, "$g_arena_training_kills", "$g_player", 1),#use this for conversation
      #SB : deduct health here
      (call_script, "script_agent_apply_training_health", "$g_player"),
    (try_end),
    (finish_mission,0),
    ]),

  (1, 0, ti_once, [], [
      (eq, "$g_mt_mode", abm_visit),
      # (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
      (store_current_scene, reg(1)),
      (scene_set_slot, reg(1), slot_scene_visited, 1),
      (mission_enable_talk),
      # (get_player_agent_no, "$g_player"),
      (assign, ":team_set", 0),
      (try_for_agents, ":agent_no"),
        (neq, ":agent_no", "$g_player"),
        (agent_get_troop_id, ":troop_id", ":agent_no"),
        (is_between, ":troop_id", regular_troops_begin, regular_troops_end),
        (eq, ":team_set", 0),
        (agent_set_team, ":agent_no", 1),
        (assign, ":team_set", 1),
      (try_end),
    ]),

#even though $disable_npc_complaints should really only apply for companions
 (ti_on_agent_killed_or_wounded, 0, 0, [
        # (ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
      (eq, "$g_mt_mode", abm_tournament),
      (eq, "$disable_npc_complaints", 0),
    ],
    [
      (store_trigger_param_1, ":dead_agent_no"),
      (store_trigger_param_2, ":killer_agent_no"),

      (agent_get_troop_id, ":killer_troop", ":killer_agent_no"),
      (troop_is_hero, ":killer_troop"),

      (agent_is_human, ":dead_agent_no"),
      (agent_get_troop_id, ":wounded_troop", ":dead_agent_no"),
      (troop_is_hero, ":wounded_troop"),
      (is_between, ":wounded_troop", heroes_begin, heroes_end), #exclude common tournament fighters (and the player from being a sore loser)
      (try_begin), #calculate relation loss
        (troop_get_slot, ":lrep", ":wounded_troop", slot_lord_reputation_type),
        (this_or_next|eq, ":lrep", lrep_quarrelsome),
        (troop_slot_eq, ":killer_troop", slot_lord_reputation_type, lrep_quarrelsome),
        (assign, ":relation_loss", -2),
      (else_try),
        (neq, ":lrep", lrep_martial), #martial lords don't mind losing fights
        (neq, ":lrep", lrep_goodnatured), #goodnature ones don't care
        (neq, ":lrep", lrep_none), #don't reduce warlord/pretender relations
        (this_or_next|eq, ":lrep", lrep_roguish), #only the "bad" companion lrep
        (neg|is_between, ":wounded_troop", companions_begin, companions_end),
        (assign, ":relation_loss", -1),
      (else_try),
        (assign, ":relation_loss", 0),
      (try_end),

      # (agent_get_position, pos1, ":killer_agent_no"),
      # (agent_get_position, pos2, ":dead_agent_no"),
      # (get_distance_between_positions, ":dist", pos1, pos2),
      # (lt, ":dist", 200),
      # (try_begin), #backstabbed
        # (position_is_behind_position, pos1, pos2),
        # (call_script, "script_troop_change_relation_with_troop", "$g_player_troop", ":wounded_troop", -1),
        # # (eq, "$g_player_troop", "trp_player"),
        # # (call_script, "script_change_player_honor", -1),
      # (try_end),
      (try_begin), #friendly fire, it happens
        (eq, ":killer_troop", "trp_player"),
        (agent_is_ally, ":dead_agent_no"),
        (call_script, "script_change_player_relation_with_troop", ":wounded_troop", -3),
      (else_try),
        (call_script, "script_troop_change_relation_with_troop", ":killer_troop", ":wounded_troop", ":relation_loss"),
      (try_end),
      (call_script, "script_change_troop_renown", ":killer_troop", 1), #Static amount
    ]),

  (0, 0, ti_once, [(eq, "$g_mt_mode", abm_tournament),],
   [
     (play_sound, "snd_arena_ambiance", sf_looping),
     # (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
     ]),

  (1, 4, ti_once, [(eq, "$g_mt_mode", abm_tournament),
                   (this_or_next|main_hero_fallen),
                   (num_active_teams_le, 1)],
   [
       (try_begin),
         (neg|main_hero_fallen),
         (call_script, "script_end_tournament_fight", 1),
         (call_script, "script_play_victorious_sound"),
         (finish_mission),
       (else_try),
         (call_script, "script_end_tournament_fight", 0),
         (finish_mission),
       (try_end),
       ]),

  (ti_battle_window_opened, 0, 0, [], [
  (this_or_next|eq, "$g_mt_mode", abm_brawl),
  (eq, "$g_mt_mode", abm_training),
  (start_presentation, "prsnt_arena_training")]),

  (0, 0, ti_once, [], [(eq, "$g_mt_mode", abm_training),
                       (assign, "$g_arena_training_max_opponents", 40),
                       (assign, "$g_arena_training_num_agents_spawned", 0),
                       (assign, "$g_arena_training_kills", 0),
                       (assign, "$g_arena_training_won", 0),
                       # (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
                       ]),
  (0, 0, ti_once, [], [(eq, "$g_mt_mode", abm_brawl),
                       (assign, "$g_arena_training_max_opponents", 10), #tocan 40
                       (assign, "$g_arena_training_num_agents_spawned", 0),
                       (assign, "$g_arena_training_kills", 0),
                       (assign, "$g_arena_training_won", 0),
                       # (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
                       (set_fixed_point_multiplier, 100),
                       (try_for_agents, ":agent_id"), #tocan to make visitor animations desync
                           (agent_get_entry_no, ":entry", ":agent_id"),
                           (gt, ":entry", 39),
                           # (val_add,"$spectators",1),
                           (store_random_in_range,":desync",0,100),
                           (agent_set_animation_progress, ":agent_id", ":desync"), # Desync their standing animation!
                       (try_end),
                       ]),

  (1, 4, ti_once, [
                   (this_or_next|eq, "$g_mt_mode", abm_brawl),
                   (eq, "$g_mt_mode", abm_training),
                   (store_mission_timer_a, ":cur_time"),
                   (gt, ":cur_time", 3),
                   (assign, ":win_cond", 0),
                   (try_begin),
                     (ge, "$g_arena_training_num_agents_spawned", "$g_arena_training_max_opponents"),#spawn at most 40 agents
                     (num_active_teams_le, 1),
                     (assign, ":win_cond", 1),
                   (try_end),
                   (this_or_next|eq, ":win_cond", 1),
                   (main_hero_fallen)],
   [
       # (get_player_agent_no, "$g_player"),
       (agent_get_kill_count, "$g_arena_training_kills", "$g_player", 1),#use this for conversation
       (assign, "$g_arena_training_won", 0),
       (try_begin),
         (neg|main_hero_fallen),
         (assign, "$g_arena_training_won", 1),#use this for conversation
       (try_end),
       (assign, "$g_mt_mode", abm_visit),
       (set_jump_mission, "mt_arena_melee_fight"),
       (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
       (modify_visitors_at_site, ":arena_scene"),
       (reset_visitors),
       (set_visitor, 35, "trp_arena_training_fighter_8"),
       (set_visitor, 36, "trp_hired_blade"),
       (set_jump_entry, 50),
       (jump_to_scene, ":arena_scene"),

       #SB : deduct health here
       (call_script, "script_agent_apply_training_health", "$g_player"),
       ]),


  (0.2, 0, 0,
   [
       (eq, "$g_mt_mode", abm_training),
       (assign, ":num_active_fighters", 0),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_is_alive, ":agent_no"),
         (agent_get_team, ":team_no", ":agent_no"),
         (is_between, ":team_no", 0 ,7),
         (val_add, ":num_active_fighters", 1),
       (try_end),
       (lt, ":num_active_fighters", 7),
       (neg|main_hero_fallen),
       (store_mission_timer_a, ":cur_time"),
       (this_or_next|ge, ":cur_time", "$g_arena_training_next_spawn_time"),
       (this_or_next|lt, "$g_arena_training_num_agents_spawned", 6),
       (num_active_teams_le, 1),
       (lt, "$g_arena_training_num_agents_spawned", "$g_arena_training_max_opponents"),
      ],
    [
       (assign, ":added_troop", "$g_arena_training_num_agents_spawned"),
       (store_div,  ":added_troop", "$g_arena_training_num_agents_spawned", 6),
       (assign, ":added_troop_sequence", "$g_arena_training_num_agents_spawned"),
       (val_mod, ":added_troop_sequence", 6),
       (val_add, ":added_troop", ":added_troop_sequence"),
       (val_min, ":added_troop", 9),
       (val_add, ":added_troop", "trp_arena_training_fighter_1"),
       (assign, ":end_cond", 10000),
       (get_player_agent_no, "$g_player"),
       (agent_get_position, pos5, "$g_player"),
       (try_for_range, ":unused", 0, ":end_cond"),
         (store_random_in_range, ":random_entry_point", 32, 40),
         #SB : now we use this to prevent duplicate
         (neq, ":random_entry_point", "$g_player_entry_point"), # make sure we don't overwrite player
         (entry_point_get_position, pos1, ":random_entry_point"),
         (get_distance_between_positions, ":dist", pos5, pos1),
         (gt, ":dist", 1200), #must be at least 12 meters away from the player
         (assign, ":end_cond", 0),
       (try_end),
       (add_visitors_to_current_scene, ":random_entry_point", ":added_troop", 1),
       #SB : set this as last spawnpoint
       (assign, "$g_player_entry_point", ":random_entry_point"),
       (store_add, ":new_spawned_count", "$g_arena_training_num_agents_spawned", 1),
       (store_mission_timer_a, ":cur_time"),
       (store_add, "$g_arena_training_next_spawn_time", ":cur_time", 14),
       (store_div, ":time_reduction", ":new_spawned_count", 3),
       (val_sub, "$g_arena_training_next_spawn_time", ":time_reduction"),
       ]),
  (0.2, 0, 0,
   [
       (eq, "$g_mt_mode", abm_brawl),
       (assign, ":num_active_fighters", 0),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_is_alive, ":agent_no"),
         (agent_get_team, ":team_no", ":agent_no"),
         (is_between, ":team_no", 0 ,7),
         (val_add, ":num_active_fighters", 1),
       (try_end),
       (lt, ":num_active_fighters", 2), #tocan 7
       (neg|main_hero_fallen),
       (store_mission_timer_a, ":cur_time"),
       (this_or_next|ge, ":cur_time", "$g_arena_training_next_spawn_time"),
       (this_or_next|lt, "$g_arena_training_num_agents_spawned", 6),
       (num_active_teams_le, 1),
       (lt, "$g_arena_training_num_agents_spawned", "$g_arena_training_max_opponents"),
      ],
    [
       # (assign, ":added_troop", "$g_arena_training_num_agents_spawned"),
       # (store_div,  ":added_troop", "$g_arena_training_num_agents_spawned", 6),
       # (assign, ":added_troop_sequence", "$g_arena_training_num_agents_spawned"),
       # (val_mod, ":added_troop_sequence", 6),
       # (val_add, ":added_troop", ":added_troop_sequence"),
       # (val_min, ":added_troop", 9),
       # (val_add, ":added_troop", "trp_arena_training_fighter_1"),
       (store_random_in_range,":added_troop",soldiers_begin,soldiers_end),
       (assign, ":end_cond", 10000),
       (get_player_agent_no, "$g_player"),
       (agent_get_position, pos5, "$g_player"),
       (try_for_range, ":unused", 0, ":end_cond"),
         (store_random_in_range, ":random_entry_point", 32, 35), #tocan
         #SB : now we use this to prevent duplicate
         (neq, ":random_entry_point", "$g_player_entry_point"), # make sure we don't overwrite player
         (entry_point_get_position, pos1, ":random_entry_point"),
         (get_distance_between_positions, ":dist", pos5, pos1),
         (gt, ":dist", 5), #must be at least 12 meters away from the player
         (assign, ":end_cond", 0),
       (try_end),
       (add_visitors_to_current_scene, ":random_entry_point", ":added_troop", 1),
       #SB : set this as last spawnpoint
       (assign, "$g_player_entry_point", ":random_entry_point"),
       (store_add, ":new_spawned_count", "$g_arena_training_num_agents_spawned", 1),
       (store_mission_timer_a, ":cur_time"),
       (store_add, "$g_arena_training_next_spawn_time", ":cur_time", 14),
       (store_div, ":time_reduction", ":new_spawned_count", 3),
       (val_sub, "$g_arena_training_next_spawn_time", ":time_reduction"),
       ]),
  #SB : change interval
  (3, 0, 0,
   [
       (this_or_next|eq, "$g_mt_mode", abm_brawl),
       (eq, "$g_mt_mode", abm_training),
       ],
    [
       (assign, ":max_teams", 6),
       (val_max, ":max_teams", 1),
       # (get_player_agent_no, "$g_player"),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_is_alive, ":agent_no"),
         (agent_slot_eq, ":agent_no", slot_agent_arena_team_set, 0),
         (agent_get_team, ":team_no", ":agent_no"),
         (is_between, ":team_no", 0 ,7),
         (try_begin),
           (eq, ":agent_no", "$g_player"),
           (agent_set_team, ":agent_no", 6), #player is always team 6.
         (else_try),
           (store_random_in_range, ":selected_team", 0, ":max_teams"),
          # find strongest team
           (try_for_range, ":t", 0, 6),
             (troop_set_slot, "trp_temp_array_a", ":t", 0),
           (try_end),
           (try_for_agents, ":other_agent_no"),
             (agent_is_human, ":other_agent_no"),
             (agent_is_alive, ":other_agent_no"),
             (neq, ":agent_no", "$g_player"),
             (agent_slot_eq, ":other_agent_no", slot_agent_arena_team_set, 1),
             (agent_get_team, ":other_agent_team", ":other_agent_no"),
             (troop_get_slot, ":count", "trp_temp_array_a", ":other_agent_team"),
             (val_add, ":count", 1),
             (troop_set_slot, "trp_temp_array_a", ":other_agent_team", ":count"),
           (try_end),
           (assign, ":strongest_team", 0),
           (troop_get_slot, ":strongest_team_count", "trp_temp_array_a", 0),
           (try_for_range, ":t", 1, 6),
             (troop_slot_ge, "trp_temp_array_a", ":t", ":strongest_team_count"),
             (troop_get_slot, ":strongest_team_count", "trp_temp_array_a", ":t"),
             (assign, ":strongest_team", ":t"),
           (try_end),
           (store_random_in_range, ":rand", 5, 100),
           (try_begin),
             (lt, ":rand", "$g_arena_training_num_agents_spawned"),
             (assign, ":selected_team", ":strongest_team"),
           (try_end),
           (agent_set_team, ":agent_no", ":selected_team"),
         (try_end),
         (agent_set_slot, ":agent_no", slot_agent_arena_team_set, 1),
         (try_begin),
           (neq, ":agent_no", "$g_player"),
           (val_add, "$g_arena_training_num_agents_spawned", 1),
         (try_end),
       (try_end),
       ]),
  ] #SB : include horse cull + unarmed_agent_damage?

mission_templates = [
  (
    "town_default",0,-1,
    "Default town visit",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (8,mtef_scene_source,af_override_horse,0,1,[]),
     (9,mtef_scene_source,af_override_horse,0,1,[]),
     (10,mtef_scene_source,af_override_horse,0,1,[]),
     (11,mtef_scene_source,af_override_horse,0,1,[]),
     (12,mtef_scene_source,af_override_horse,0,1,[]),
     (13,mtef_scene_source,0,0,1,[]),
     (14,mtef_scene_source,0,0,1,[]),
     (15,mtef_scene_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),
     (17,mtef_visitor_source,af_override_horse,0,1,[]),
     (18,mtef_visitor_source,af_override_horse,0,1,[]),
     (19,mtef_visitor_source,af_override_horse,0,1,[]),
     (20,mtef_visitor_source,af_override_horse,0,1,[]),
     (21,mtef_visitor_source,af_override_horse,0,1,[]),
     (22,mtef_visitor_source,af_override_horse,0,1,[]),
     (23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),
     (25,mtef_visitor_source,af_override_horse,0,1,[]),
     (26,mtef_visitor_source,af_override_horse,0,1,[]),
     (27,mtef_visitor_source,af_override_horse,0,1,[]),
     (28,mtef_visitor_source,af_override_horse,0,1,[]),
     (29,mtef_visitor_source,af_override_horse,0,1,[]),
     (30,mtef_visitor_source,af_override_horse,0,1,[]),
     (31,mtef_visitor_source,af_override_horse,0,1,[]),
     ], tocan_common_triggers+bodyguard_triggers+
     [
      common_agent_label,

      (1, 0, ti_once, [],
      [
        (store_current_scene, ":cur_scene"),
        (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
        # (try_begin),
          # (eq, "$sneaked_into_town", 1),
          # (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
        # (else_try),
          # (eq, "$talk_context", tc_tavern_talk),
          # (call_script, "script_music_set_situation_with_culture", mtf_sit_tavern),
        # (else_try),
          # (call_script, "script_music_set_situation_with_culture", mtf_sit_town),
        # (try_end),
      ]),
	  
	#loud robbery/raid unalarmed guards occasionally walk towards the player position - krag
    (2, 0, 0,
      [
	  (eq, "$loud_robbery_in_progress", 1),
	  ],
	  [
			(get_player_agent_no, "$g_player"),
			#(display_message, "@loud robbery in progress town_default 2",message_alert),
			(agent_get_position, pos12, "$g_player"),
			#(call_script, "script_hit_alerts_guards_panicks_civilians", "$g_player", "itm_large_caliber_ammo_pw"),
			(try_for_agents, ":turning_agent"),
				(agent_get_troop_id, ":troop", ":turning_agent"),
				(is_between, ":troop", soldiers_begin, soldiers_end),
				
				(agent_slot_eq, ":turning_agent", slot_agent_is_running_away, 0),
				(agent_is_human, ":turning_agent"),
				(agent_is_alive, ":turning_agent"),
				(agent_is_active, ":turning_agent"),
				(try_begin),
					(agent_is_alarmed, ":turning_agent"),
					(agent_clear_scripted_mode, ":turning_agent"),
					#(agent_force_rethink, ":turning_agent"),
				  (else_try),
					#(neg|agent_is_alarmed, ":turning_agent"),
					(store_random_in_range, ":rand", 0, 10),
					(eq, ":rand", 9),
					(agent_set_no_dynamics, ":turning_agent", 0),
					#(agent_set_speed_limit, ":turning_agent", 99),
					(agent_set_slot, ":turning_agent", slot_agent_static_npc, 0),
					(agent_set_slot, ":turning_agent", slot_agent_walker_occupation, 0),
					(agent_set_animation_progress, ":turning_agent", 99),
					(agent_set_scripted_destination, ":turning_agent", pos12, 1, 0),
					#(agent_set_is_alarmed, ":turning_agent", 1),
				(try_end),
			(try_end),
	  ]),

      (ti_before_mission_start, 0, 0, [],
      [
        (call_script, "script_change_banners_and_chest"),
        (call_script, "script_initialize_tavern_variables"),
      ]),

      #SB : minstrels equip instruments
      (ti_on_agent_spawn, 0, 0,
        [
          (eq, "$talk_context", tc_tavern_talk),
          (store_trigger_param_1, ":agent_no"),
          (agent_get_troop_id, ":troop_no", ":agent_no"),
          (is_between, ":troop_no", tavern_minstrels_begin, tavern_minstrels_end),
          (this_or_next|troop_slot_eq, ":troop_no", slot_troop_cur_center, "$current_town"),
          (party_slot_eq, "$current_town", slot_center_tavern_minstrel, ":troop_no"),
        ],
        #this only works for the "true" minstrel, last condition prohibits the one added from alternative_town in module_game_menus
        [
          (store_trigger_param_1, ":agent_no"),
          (agent_get_troop_id, ":troop_no", ":agent_no"),
          (assign, ":item_no", -1),

          (store_item_kind_count, ":item_count", "itm_guitar", ":troop_no"),
          # (try_begin),
            (this_or_next|gt, ":item_count", 0),
            (troop_has_item_equipped, ":troop_no", "itm_guitar"),
            (assign, ":item_no", "itm_guitar"),
          # (else_try),
            # (store_item_kind_count, ":item_count", "itm_lute", ":troop_no"),
            # (this_or_next|gt, ":item_count", 0),
            # (troop_has_item_equipped, ":troop_no", "itm_lute"),
            # (assign, ":item_no", "itm_lute"),
          # (try_end),
          (neq, ":item_no", -1),
          (agent_equip_item, ":agent_no", ":item_no"), #equip instrument
          (agent_set_wielded_item, ":agent_no", -1), #doff it
        ]),

      (ti_inventory_key_pressed, 0, 0,
      [ #SB : disable inventory while attacked in taverns
        (eq,"$has_prison_key",0),	#krag robbery added these 3 lines
		(eq,"$has_castle_key",0),
		(eq,"$robbery_in_progress",0),
		(try_begin),
          (this_or_next|eq, "$g_main_attacker_agent", 0),
          (neq, "$talk_context", tc_tavern_talk),
          # (show_object_details_overlay, 1),
          (set_trigger_result, 1),
        (else_try),
          (display_message, "@Dispatch your opponents first!",message_alert),
        (try_end),
      ], []),

      #tavern - belligerent drunk leaving/fading out
      (1, 0, 0,
      [
        (gt, "$g_belligerent_drunk_leaving", 0),
        (entry_point_get_position, pos0, 0),
        (agent_get_position, pos1, "$g_belligerent_drunk_leaving"),
        (get_distance_between_positions, ":dist", pos0, pos1),
        (le, ":dist", 150),
      ],
      [
        (agent_fade_out, "$g_belligerent_drunk_leaving"),
        (assign, "$g_belligerent_drunk_leaving", 0),
      ]),

      (ti_tab_pressed, 0, 0,
      [
        (try_begin),
          (eq,"$has_prison_key",0),	#krag robbery added these 3 lines
		  (eq,"$has_castle_key",0),
		  (eq,"$robbery_in_progress",0),
		  (neq, "$talk_context", tc_prison_break),#krag robbery added, normally not an issue in taver/shop/etc
		  (eq, "$g_main_attacker_agent", 0),
          (set_trigger_result, 1),
        (else_try),
          (display_message, "str_cannot_leave_now",message_alert), #SB : message
        (try_end),
      ], []),

	   #krag robbery failure, added this trigger
      (1, 0, ti_once,
      [
	    (neg|conversation_screen_is_active),
		(this_or_next|eq,"$has_prison_key",1),
		(this_or_next|eq,"$has_castle_key",1),
		(this_or_next|eq,"$robbery_in_progress",1),
        (this_or_next|eq, "$talk_context", tc_escape),
		(eq, "$talk_context", tc_prison_break),
		(main_hero_fallen),
      ],
      [
    (assign, "$capturer_party", "$g_encountered_party"), # set variable properly
	  (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
	  (finish_mission,0)
	  ]),

	#krag robbery jailbreak new panick system
	(ti_on_agent_hit, 0, 0, [
	(le, "$g_start_promoted_fight", 0),
	],
   [
      (store_trigger_param_1, ":target"),
      (store_trigger_param_2, ":dealer"),
      #(store_trigger_param_3, ":damage"),
      #(store_trigger_param, ":hitbone", 4),
	  (store_trigger_param, ":ammo_type", 5),
	  # reg0            = weapon item_id
	  # pos0            = position of the hit area, rotation fields contain the direction of the blow
	  (neq, ":target", ":dealer"),
	  (agent_is_human,":target"),
	(agent_get_position, pos12, ":target"),
	(call_script, "script_hit_alerts_guards_panicks_civilians", ":dealer", ":ammo_type"),#needs target in pos12
   ]),

	  (0.2, 0, 0,	# krag robbery clear panicking agents
    [
      (this_or_next|eq,"$has_prison_key",1),
		(this_or_next|eq,"$has_castle_key",1),
		(this_or_next|eq,"$robbery_in_progress",1),
	  (this_or_next|eq, "$talk_context", tc_prison_break),
        (eq, "$talk_context", tc_escape),
    ],
    [
     (call_script, "script_clear_panicking_agents_near_passages", 150),
	 (entry_point_get_position, pos17, 0),#Keep this section is it's likely the passage will be blocked by the player
	  (try_for_agents, ":escaping_agent", pos17, 150),
		(agent_is_active,":escaping_agent"),
		(agent_is_alive,":escaping_agent"),
		(agent_is_human,":escaping_agent"),
		(agent_slot_eq, ":escaping_agent", slot_agent_is_running_away, 1),
		(agent_fade_out, ":escaping_agent"),
		#(display_message, "@agent faded"),
	  (try_end),
    ]),

	(0, 0, ti_once, [	#krag robbery added to make shopkeeps hostile during raid
	  (this_or_next|eq,"$has_prison_key",1),
		(this_or_next|eq,"$has_castle_key",1),
		(this_or_next|eq,"$robbery_in_progress",1),
        (eq, "$talk_context", tc_escape),
		  ],
      [
		(call_script, "script_make_town_guards_and_hero_troops_turn_hostile"),
		(get_player_agent_no, ":player"),
		(call_script, "script_cf_agent_wield_weapons", ":player"),
		#(assign, "$talk_context", tc_prison_break),
      ]),

	  (ti_on_agent_spawn, 0, 0,	#krag robbery clear wounded agents (couldn't find a way to block spawning)
        [
          # (this_or_next|eq,"$has_prison_key",1),
		# (this_or_next|eq,"$has_castle_key",1),
		# (this_or_next|eq,"$robbery_in_progress",1),
	  # (this_or_next|eq, "$talk_context", tc_prison_break),
        # (eq, "$talk_context", tc_escape),
        ],
        [
          (store_trigger_param_1, ":agent_no"),
          (agent_get_troop_id, ":troop_no", ":agent_no"),
          (gt, ":troop_no", 0),#avoid player
			(store_troop_health, ":troop_health", ":troop_no"),
			(eq, ":troop_health", 0),
			(agent_set_visibility, ":agent_no", 0),
			(agent_fade_out, ":agent_no"),
        ]),



	  #tavern brawl triggers - drunk
      (2, 0, 0,
      [
	    (neg|conversation_screen_is_active),

		(eq, "$talk_context", tc_tavern_talk),
		(eq,"$has_prison_key",0),	#krag robbery added these 3 lines
		(eq,"$has_castle_key",0),
		(eq,"$robbery_in_progress",0),

		(neg|troop_slot_eq, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),
		(troop_slot_eq, "trp_belligerent_drunk", slot_troop_cur_center, "$g_encountered_party"),
		(eq, "$drunks_dont_pick_fights", 0),
	  ],
	  [
	    (try_begin),
	      (eq, "$g_start_belligerent_drunk_fight", 0),
	      (assign, "$g_start_belligerent_drunk_fight", 1),

	      (try_for_agents, ":cur_agent"),
	        (agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
	        (eq, ":cur_agent_troop", "trp_belligerent_drunk"),
	        (assign, "$g_belligerent_drunk", ":cur_agent"),
	      (try_end),
	    (else_try),
	      (eq, "$g_start_belligerent_drunk_fight", 1),

	      (agent_is_active, "$g_belligerent_drunk"),
	      (agent_is_alive, "$g_belligerent_drunk"),
	      # (get_player_agent_no, "$g_player"),
	      (agent_get_position, pos0, "$g_player"),
	      (agent_get_position, pos1, "$g_belligerent_drunk"),
	      (get_distance_between_positions, ":dist", pos0, pos1),
	      (position_get_z, ":pos0_z", pos0),
	      (position_get_z, ":pos1_z", pos1),
	      (store_sub, ":z_difference", ":pos1_z", ":pos0_z"),
	      (try_begin),
	        (le, ":z_difference", 0),
	        (val_mul, ":z_difference", -1),
	      (try_end),
	      (store_mul, ":z_difference_mul_3", ":z_difference", 3),
	      (val_add, ":dist", ":z_difference_mul_3"),
	      (store_random_in_range, ":random_value", 0, 200),
	      (store_add, ":400_plus_random_200", 400, ":random_value"),
	      (le, ":dist", ":400_plus_random_200"),

 		  (call_script, "script_activate_tavern_attackers"),
  		  (start_mission_conversation, "trp_belligerent_drunk"),
  		  (assign, "$g_start_belligerent_drunk_fight", 2),
	    (try_end),
	  ]),

	  #tavern brawl triggers - assassin
      (2, 0, 0, [
	    (neg|conversation_screen_is_active),
		(eq, "$talk_context", tc_tavern_talk),
		(troop_slot_eq, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),
		(eq,"$has_prison_key",0),	#krag robbery added these 3 lines
		(eq,"$has_castle_key",0),
		(eq,"$robbery_in_progress",0),
	  ],
	  [
	    (try_begin),
	      (eq, "$g_start_hired_assassin_fight", 0),
	      (assign, "$g_start_hired_assassin_fight", 1),

	      (try_for_agents, ":cur_agent"),
	        (agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
	        (eq, ":cur_agent_troop", "trp_hired_assassin"),
	        (assign, "$g_hired_assassin", ":cur_agent"),
	      (try_end),
	    (else_try),
	      (eq, "$g_start_hired_assassin_fight", 1),

	      (agent_is_active, "$g_hired_assassin"),
	      (agent_is_alive, "$g_hired_assassin"),
	      # (get_player_agent_no, "$g_player"),
	      (agent_get_position, pos0, "$g_player"),
	      (agent_get_position, pos1, "$g_hired_assassin"),
	      (get_distance_between_positions, ":dist", pos0, pos1),
	      (position_get_z, ":pos0_z", pos0),
	      (position_get_z, ":pos1_z", pos1),
	      (store_sub, ":z_difference", ":pos1_z", ":pos0_z"),
	      (try_begin),
	        (le, ":z_difference", 0),
	        (val_mul, ":z_difference", -1),
	      (try_end),
	      (store_mul, ":z_difference_mul_3", ":z_difference", 3),
	      (val_add, ":dist", ":z_difference_mul_3"),
	      (store_random_in_range, ":random_value", 0, 200),
	      (store_add, ":400_plus_random_200", 400, ":random_value"),
	      (le, ":dist", ":400_plus_random_200"),

		  (call_script, "script_activate_tavern_attackers"),
		  (assign, "$g_start_hired_assassin_fight", 2),
		(try_end),
	  ]),

	  #Aftermath talks
      (3, 0, ti_once,
      [
	    (neg|conversation_screen_is_active),
		(eq, "$talk_context", tc_tavern_talk),
		(gt, "$g_main_attacker_agent", 0),

		(this_or_next|neg|agent_is_alive, "$g_main_attacker_agent"),
		(agent_is_wounded, "$g_main_attacker_agent"),
      ],
      [
        (mission_enable_talk),

		(try_for_agents, ":agent_id"),
		  (agent_is_alive, ":agent_id"),
		  (agent_get_position, pos4, ":agent_id"),
		  (agent_set_scripted_destination, ":agent_id", pos4),
		(try_end),

		#(party_get_slot, ":tavernkeeper", "$g_encountered_party", slot_town_tavernkeeper),
		#(start_mission_conversation, ":tavernkeeper"),

		##the above doesn't seem to fire, or does but gives wrong dialog, so setting the stuff here - krag
		(assign, "$g_main_attacker_agent", 0),
		(troop_add_gold, "trp_player", 50),
		(try_begin),
			(gt, "$g_attacker_drawn_weapon", 0),
			(assign, reg8, "$g_attacker_drawn_weapon"),
			(call_script, "script_convert_ai_gun_for_player", "$g_attacker_drawn_weapon"),#output reg8
			(assign, "$g_attacker_drawn_weapon", reg8),
			(store_free_inventory_capacity, ":inv_space"),
			(ge, ":inv_space", 1),
			(troop_add_item, "trp_player", "$g_attacker_drawn_weapon", 0),
		(try_end),
		(try_begin),
			(troop_slot_eq, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),
			(troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, -1),
			(display_message,"@It seems he was an assassin sent to kill you!"),
		(try_end),
	  ]),


	  #Aftermath talks
      (3, 0, ti_once,
      [
	    (neg|conversation_screen_is_active),
		(eq, "$talk_context", tc_tavern_talk),
		(gt, "$g_main_attacker_agent", 0),
		(main_hero_fallen),
      ],
      [
	  (jump_to_menu, "mnu_lost_tavern_duel"),
	  (finish_mission,0)

	  ]),

		## removed as players will often have no melee, plus have set drunk/assassin to use a gun - krag
	  # #No shooting in the tavern
      # (1, 0, 0,
      # [
	    # (neg|conversation_screen_is_active),
		# (eq, "$talk_context", tc_tavern_talk),
		# (gt, "$g_main_attacker_agent", 0),

		# # (get_player_agent_no, "$g_player"),
		# (agent_is_alive, "$g_player"),
		# ## SB : move diplomacy standing check back up here in conditions
		# (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$g_encountered_party_faction"),
		# (lt, reg0, DPLMC_FACTION_STANDING_MEMBER),
		# (agent_get_wielded_item, ":wielded_item", "$g_player", 0),
		# (gt, ":wielded_item", 0),
		# (item_get_type, ":type", ":wielded_item"),
		# (this_or_next|is_between, ":type", itp_type_bow, itp_type_goods),
		# (is_between, ":type", itp_type_pistol, itp_type_bullets),
		# # (is_between, ":wielded_item", "itm_darts", "itm_torch"),
		# # (neq, ":wielded_item", "itm_javelin_melee"),
		# # (neq, ":wielded_item", "itm_throwing_spear_melee"),
		# # (neq, ":wielded_item", "itm_jarid_melee"),
		# # (neq, ":wielded_item", "itm_light_throwing_axes_melee"),
		# # (neq, ":wielded_item", "itm_throwing_axes_melee"),
		# # (neq, ":wielded_item", "itm_heavy_throwing_axes_melee"),
        # #SB : also add these conditions

		# ##Stop this from continually firing if you have no melee weapons
	  # (assign, ":continue", 0),
      # (try_for_range, ":i_slot", 0, 4),
        # (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
        # (gt, ":item_id", 0),
        # (neq, ":item_id", ":wielded_item"),
        # (item_get_type, ":itp", ":item_id"),
        # (is_between, ":itp", itp_type_one_handed_wpn, itp_type_arrows),
        # (assign, ":continue", 1),
      # (try_end),
		# (eq, ":continue", 1),

      # ],
      # [
		# (party_get_slot, ":tavernkeeper", "$g_encountered_party", slot_town_tavernkeeper),
		# # ##diplomacy start+
		# # #Turn of this !@#$%ing obnoxious and totally illogical restriction provided:
		# # (try_begin),
			# # #1) there is an actual fight
			# # (gt, "$g_main_attacker_agent", 0),
			# # (agent_is_alive, "$g_main_attacker_agent"),
			# # (neg|agent_is_wounded, "$g_main_attacker_agent"),
			# # #2) the player is the lord of this town, a mercenary captain in the faction's employ, or ruler of this faction
			# # (store_faction_of_party , ":center_faction", "$g_encountered_party"),
			# # (this_or_next|eq, ":center_faction", "$players_kingdom"),
				# # (eq, ":center_faction", "fac_player_supporters_faction"),
		# # (else_try),
		# # #Else, original behavior:
			# (start_mission_conversation, ":tavernkeeper"),
		# # (try_end),
		# ##diplomacy stop+
	  # ]),

      #SB : drunks are totally effective fighters
      (3, 0, 0,
      [
       (eq, "$talk_context", tc_tavern_talk),
       (ge, "$g_start_belligerent_drunk_fight", 1),
       (gt, "$g_main_attacker_agent", 0),
       (agent_is_alive, "$g_main_attacker_agent"),
       # (eq, "$g_belligerent_drunk_leaving", 0), #don't stumble while leaving
       (store_random_in_range, ":random_no", 0, 3),
       (eq, ":random_no", 0),
       ],
      [
      # (store_random_in_range, ":anim", "anim_strike_chest_front_stop", "anim_cheer"),
      (store_random_in_range, ":anim", "anim_strike3_head_left", "anim_fall_face_hold"),
      (agent_set_animation, "$g_main_attacker_agent", ":anim"),
      (store_random_in_range, ":progress", 0, 100),
      (agent_set_animation_progress, "$g_main_attacker_agent", ":progress"),
      ]),
      #Check for weapon in hand of attacker, also, everyone gets out of the way
      (1, 0, 0,
      [
        (gt, "$g_main_attacker_agent", 0),
      ],
      [
        (agent_get_wielded_item, ":wielded_item", "$g_main_attacker_agent", 0),
        (val_max, "$g_attacker_drawn_weapon", ":wielded_item"),

        (call_script, "script_neutral_behavior_in_fight"),
      ]),

	(ti_on_agent_killed_or_wounded, 0, 0, [], #consequences for killing mercs and shopkeepers
   [
     (store_trigger_param_1, ":dead_agent_no"),
     (store_trigger_param_2, ":killer_agent_no"),
     #(store_trigger_param_3, ":is_wounded"),

	  (agent_is_human,":dead_agent_no"),
     (agent_get_troop_id, ":dead_agent_troop_no", ":dead_agent_no"),
     #(agent_get_troop_id, ":killer_agent_troop_no", ":killer_agent_no"),
	 (agent_get_team, ":killer_team",  ":killer_agent_no"),	#krag for below
	 (get_player_agent_no, ":player_agent"),
	 (agent_get_team, ":player_team",  ":player_agent"),
	 #(agent_get_wielded_item, ":killer_weapon",  ":killer_agent_no", 0),

     (try_begin),
		(party_get_slot, ":merc_type", "$current_town", slot_center_mercenary_troop_type),
		(eq, ":dead_agent_troop_no", ":merc_type"),
		(party_set_slot, "$current_town", slot_center_mercenary_troop_type, -1),
		(party_set_slot, "$current_town", slot_center_mercenary_troop_amount, -1),
	  (else_try),
	    (eq, ":player_team",  ":killer_team"),
		(is_between, ":dead_agent_troop_no", armor_merchants_begin, goods_merchants_end),
		(call_script, "script_change_player_relation_with_center", "$current_town", -1),
		(store_faction_of_party, ":town_faction", "$current_town"),
		(call_script, "script_change_player_relation_with_faction", ":town_faction", -1),
     (try_end),
   ]),

    ],
  ), # ^ town_default, used only in taverns and shops?

# This template is used in party encounters and such.
#
  (
    "conversation_encounter",0,-1,
    "Conversation_encounter",
    [( 0,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 1,mtef_visitor_source,af_override_fullhelm,0,1,[]),
     ( 2,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 3,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 4,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 5,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 6,mtef_visitor_source,af_override_fullhelm,0,1,[]),
     ( 7,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 8,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 9,mtef_visitor_source,af_override_fullhelm,0,1,[]),(10,mtef_visitor_source,af_override_fullhelm,0,1,[]),(11,mtef_visitor_source,af_override_fullhelm,0,1,[]),
    #prisoners now...
     (12,mtef_visitor_source,af_override_fullhelm,0,1,[]),(13,mtef_visitor_source,af_override_fullhelm,0,1,[]),(14,mtef_visitor_source,af_override_fullhelm,0,1,[]),(15,mtef_visitor_source,af_override_fullhelm,0,1,[]),(16,mtef_visitor_source,af_override_fullhelm,0,1,[]),
    #Other party
     (17,mtef_visitor_source,af_override_fullhelm,0,1,[]),(18,mtef_visitor_source,af_override_fullhelm,0,1,[]),(19,mtef_visitor_source,af_override_fullhelm,0,1,[]),(20,mtef_visitor_source,af_override_fullhelm,0,1,[]),(21,mtef_visitor_source,af_override_fullhelm,0,1,[]),
     (22,mtef_visitor_source,af_override_fullhelm,0,1,[]),(23,mtef_visitor_source,af_override_fullhelm,0,1,[]),(24,mtef_visitor_source,af_override_fullhelm,0,1,[]),(25,mtef_visitor_source,af_override_fullhelm,0,1,[]),(26,mtef_visitor_source,af_override_fullhelm,0,1,[]),
     (27,mtef_visitor_source,af_override_fullhelm,0,1,[]),(28,mtef_visitor_source,af_override_fullhelm,0,1,[]),(29,mtef_visitor_source,af_override_fullhelm,0,1,[]),(30,mtef_visitor_source,af_override_fullhelm,0,1,[]),(31,mtef_visitor_source,af_override_fullhelm,0,1,[]),
     ],
    [
      # (ti_before_mission_start, 0, ti_once, [],
      # [
      # (assign,":entry",0),
      # (try_for_range,":unused",":entry",32),
        # (mission_tpl_entry_set_override_flags, "mt_visit_town_castle",":entry", 0),
        # (mission_tpl_entry_clear_override_items, "mt_visit_town_castle", ":entry"),
      # (try_end),
      # ]),
    ],
    #SB : replace banner in town scenes? script_change_banners_and_chest

  ),

#----------------------------------------------------------------
#mission templates before this point are hardwired into the game.
#-----------------------------------------------------------------

("town_center",0,-1,
    "Default town visit",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (8,mtef_visitor_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),
	 (10,mtef_visitor_source,af_override_horse,0,1,[]),
	 (11,mtef_visitor_source,af_override_horse,0,1,[]),
	 (12,mtef_visitor_source,af_override_horse,0,1,[]),
	 (13,mtef_visitor_source,0,0,1,[]),
	 (14,mtef_scene_source,0,0,1,[]),
	 (15,mtef_scene_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),
	 (17,mtef_visitor_source,af_override_horse,0,1,[]),
	 (18,mtef_visitor_source,af_override_horse,0,1,[]),
	 (19,mtef_visitor_source,af_override_horse,0,1,[]),
	 (20,mtef_visitor_source,af_override_horse,0,1,[]),
	 (21,mtef_visitor_source,af_override_horse,0,1,[]),
	 (22,mtef_visitor_source,af_override_horse,0,1,[]),
	 (23,mtef_visitor_source,af_override_horse,0,1,[]), #guard
     (24,mtef_visitor_source,af_override_horse,0,1,[]), #guard
	 (25,mtef_visitor_source,af_override_horse,0,1,[]), #guard
	 (26,mtef_visitor_source,af_override_horse,0,1,[]), #guard
	 (27,mtef_visitor_source,af_override_horse,0,1,[]), #guard
	 (28,mtef_visitor_source,af_override_horse,0,1,[]), #guard
	 (29,mtef_visitor_source,af_override_horse,0,1,[]),
	 (30,mtef_visitor_source,af_override_horse,0,1,[]),
	 (31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),
	 (33,mtef_visitor_source,af_override_horse,0,1,[]),
	 (34,mtef_visitor_source,af_override_horse,0,1,[]),
	 (35,mtef_visitor_source,af_override_horse,0,1,[]),
	 (36,mtef_visitor_source,af_override_horse,0,1,[]), #town walker point
	 (37,mtef_visitor_source,af_override_horse,0,1,[]), #town walker point
	 (38,mtef_visitor_source,af_override_horse,0,1,[]),
	 (39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]), #in towns, can be used for guard reinforcements
	 (41,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]), #in towns, can be used for guard reinforcements
	 (42,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]), #in towns, can be used for guard reinforcements
	 (43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]), #in towns, can be used for guard reinforcements
     (44,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (45,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (46,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (47,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     ], tocan_ambience+tocan_common_triggers+tocan_autofire+tocan_flashlight+x_companion+tocan_walkers+bodyguard_triggers+tocan_center_attack+ #common_first_time+
    [

    # common_position,
    common_agent_label,
    common_torch_at_night,
    common_info_message,

    (ti_after_mission_start, 0, ti_once, [], [
        (scene_prop_get_num_instances, ":total", "spr_windmill_fan_turning"),
        (try_begin),
            (ge, ":total", 1),

            (try_for_range,":cur_instance",0,":total"),
                (scene_prop_get_instance, ":instance_id", "spr_windmill_fan_turning", ":cur_instance"),
                (ge, ":instance_id", 0),
                (assign,"$windmill",1),
            (try_end),
        (else_try),
                (assign,"$windmill",0),
        (try_end),

        ]),

    (1, 0, 0, [(eq,"$windmill",1),], [
        (scene_prop_get_num_instances, ":total", "spr_windmill_fan_turning"),
        (try_for_range,":cur_instance",0,":total"),
            (scene_prop_get_instance, ":instance_id", "spr_windmill_fan_turning", ":cur_instance"),
            (ge, ":instance_id", 0),
            (call_script, "script_cf_turn_windmill_fans", ":cur_instance"),
        (try_end),
        ]),


      (ti_before_mission_start, 0, 0, [],
      [
        (call_script, "script_change_banners_and_chest"),
        (call_script, "script_initialize_tavern_variables"),
      ]),

      #tavern - belligerent drunk leaving/fading out
      (1, 0, 0,
      [
        (gt, "$g_belligerent_drunk_leaving", 0),
        (entry_point_get_position, pos0, 0),
        (agent_get_position, pos1, "$g_belligerent_drunk_leaving"),
        (get_distance_between_positions, ":dist", pos0, pos1),
        (le, ":dist", 150),
      ],
      [
        (agent_fade_out, "$g_belligerent_drunk_leaving"),
        (assign, "$g_belligerent_drunk_leaving", 0),
      ]),

	  #tavern brawl triggers - drunk
      (2, 0, 0,
      [
	    (neg|conversation_screen_is_active),

		# (eq, "$talk_context", tc_tavern_talk),

		(neg|troop_slot_eq, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),
		(troop_slot_eq, "trp_belligerent_drunk", slot_troop_cur_center, "$g_encountered_party"),
		(eq, "$drunks_dont_pick_fights", 0),
	  ],
	  [
	    (try_begin),
	      (eq, "$g_start_belligerent_drunk_fight", 0),
	      (assign, "$g_start_belligerent_drunk_fight", 1),

	      (try_for_agents, ":cur_agent"),
	        (agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
	        (eq, ":cur_agent_troop", "trp_belligerent_drunk"),
	        (assign, "$g_belligerent_drunk", ":cur_agent"),
	      (try_end),
	    (else_try),
	      (eq, "$g_start_belligerent_drunk_fight", 1),

	      (agent_is_active, "$g_belligerent_drunk"),
	      (agent_is_alive, "$g_belligerent_drunk"),
	      # (get_player_agent_no, "$g_player"),
	      (agent_get_position, pos0, "$g_player"),
	      (agent_get_position, pos1, "$g_belligerent_drunk"),
	      (get_distance_between_positions, ":dist", pos0, pos1),
	      (position_get_z, ":pos0_z", pos0),
	      (position_get_z, ":pos1_z", pos1),
	      (store_sub, ":z_difference", ":pos1_z", ":pos0_z"),
	      (try_begin),
	        (le, ":z_difference", 0),
	        (val_mul, ":z_difference", -1),
	      (try_end),
	      (store_mul, ":z_difference_mul_3", ":z_difference", 3),
	      (val_add, ":dist", ":z_difference_mul_3"),
	      (store_random_in_range, ":random_value", 0, 200),
	      (store_add, ":400_plus_random_200", 400, ":random_value"),
	      (le, ":dist", ":400_plus_random_200"),

 		  (call_script, "script_activate_tavern_attackers"),
  		  (start_mission_conversation, "trp_belligerent_drunk"),
  		  (assign, "$g_start_belligerent_drunk_fight", 2),
	    (try_end),
	  ]),

	  #tavern brawl triggers - assassin
      (2, 0, 0, [
	    (neg|conversation_screen_is_active),
		# (eq, "$talk_context", tc_tavern_talk),
		(troop_slot_eq, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),
	  ],
	  [
	    (try_begin),
	      (eq, "$g_start_hired_assassin_fight", 0),
	      (assign, "$g_start_hired_assassin_fight", 1),

	      (try_for_agents, ":cur_agent"),
	        (agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
	        (eq, ":cur_agent_troop", "trp_hired_assassin"),
	        (assign, "$g_hired_assassin", ":cur_agent"),
	      (try_end),
	    (else_try),
	      (eq, "$g_start_hired_assassin_fight", 1),

	      (agent_is_active, "$g_hired_assassin"),
	      (agent_is_alive, "$g_hired_assassin"),
	      # (get_player_agent_no, "$g_player"),
	      (agent_get_position, pos0, "$g_player"),
	      (agent_get_position, pos1, "$g_hired_assassin"),
	      (get_distance_between_positions, ":dist", pos0, pos1),
	      (position_get_z, ":pos0_z", pos0),
	      (position_get_z, ":pos1_z", pos1),
	      (store_sub, ":z_difference", ":pos1_z", ":pos0_z"),
	      (try_begin),
	        (le, ":z_difference", 0),
	        (val_mul, ":z_difference", -1),
	      (try_end),
	      (store_mul, ":z_difference_mul_3", ":z_difference", 3),
	      (val_add, ":dist", ":z_difference_mul_3"),
	      (store_random_in_range, ":random_value", 0, 200),
	      (store_add, ":400_plus_random_200", 400, ":random_value"),
	      (le, ":dist", ":400_plus_random_200"),

		  (call_script, "script_activate_tavern_attackers"),
		  (assign, "$g_start_hired_assassin_fight", 2),
		(try_end),
	  ]),

	  #No weapons in brawl
      (0.5, 0, 0,
      [
	    (neg|conversation_screen_is_active),
		(eq, "$g_start_promoted_fight", 2),
		#(eq, "$g_start_belligerent_drunk_fight", 2),
		(gt, "$g_main_attacker_agent", 0),

		(get_player_agent_no, "$g_player"),
		(agent_is_alive, "$g_player"),

		(agent_get_wielded_item, ":wielded_item", "$g_player", 0),
		(gt, ":wielded_item", 0),
        # (this_or_next|game_key_is_down, gk_move_forward),
        # (game_key_clicked, gk_move_forward),
        (agent_unequip_item,"$g_player", ":wielded_item"),

        (display_message,"@No weapons!",message_alert),

      ],
      [
	  ]),

	  # #Aftermath talks
      # (3, 0, ti_once,
      # [
	    # (neg|conversation_screen_is_active),
		# # (eq, "$talk_context", tc_tavern_talk),
		# (gt, "$g_main_attacker_agent", 0),

		# (this_or_next|neg|agent_is_alive, "$g_main_attacker_agent"),
		# (agent_is_wounded, "$g_main_attacker_agent"),
      # ],
      # [
        # (mission_enable_talk),

		# (try_for_agents, ":agent_id"),
		  # (agent_is_alive, ":agent_id"),
		  # (agent_get_position, pos4, ":agent_id"),
		  # (agent_set_scripted_destination, ":agent_id", pos4),
		# (try_end),

		# (party_get_slot, ":tavernkeeper", "$g_encountered_party", slot_town_tavernkeeper),
		# (start_mission_conversation, ":tavernkeeper"),
	  # ]),

	  # #Aftermath talks (exterior)
      (3, 0, ti_once,
      [
	    (neg|conversation_screen_is_active),
		#(eq, "$talk_context", tc_tavern_talk),
		(neq, "$talk_context", tc_escape),
        (neq, "$talk_context", tc_prison_break),
		(neq, "$has_prison_key", 1),
		(neq, "$has_castle_key", 1),
		(neq,"$robbery_in_progress",1),
		(gt, "$g_main_attacker_agent", 0),

		(this_or_next|neg|agent_is_alive, "$g_main_attacker_agent"),
		(agent_is_wounded, "$g_main_attacker_agent"),
      ],
      [
        (mission_enable_talk),

		# (try_for_agents, ":agent_id"),
		  # (agent_is_alive, ":agent_id"),
		  # (agent_get_position, pos4, ":agent_id"),
		  # (agent_set_scripted_destination, ":agent_id", pos4),
		# (try_end),

		# (party_get_slot, ":tavernkeeper", "$g_encountered_party", slot_town_tavernkeeper),
		# (start_mission_conversation, ":tavernkeeper"),

        (agent_get_troop_id, ":type", "$g_main_attacker_agent"),
        (try_begin),
            (eq, ":type", "trp_hired_assassin"),
           # (try_begin), #random "good" imod
                #(store_random_in_range, ":imod", imod_old, imod_exquisite),
                #(gt, "$g_attacker_drawn_weapon", 0),
               # (troop_add_item, "trp_player", "$g_attacker_drawn_weapon", ":imod"), # doesn't seem to be working - krag
			    (store_free_inventory_capacity, ":inv_space"),
			    (ge, ":inv_space", 1),
                (troop_add_item, "trp_player", "itm_pistol_walther_ppk_sil"),
            #(try_end),
        (else_try),
            (eq, ":type", "trp_brawler"),
            (assign,":pay_count",0),
            (try_for_agents, ":agent_id"),
                (agent_is_active,":agent_id"),
                (agent_get_troop_id, ":troop_id", ":agent_id"),

                (neq, ":troop_id", "trp_farmer"), #farmers are "neutral"
                (neq, ":troop_id", "trp_musician"),
                (neq, ":troop_id", "trp_dancer_girl"),
                (neq, ":troop_id", "trp_mechanic"),
                (neg|is_between, ":troop_id", soldiers_begin, soldiers_end), #but lie within this range
                (neg|is_between, ":troop_id", armor_merchants_begin, village_elders_end), #but lie within this range

                (agent_get_position, pos4, ":agent_id"),
                (agent_get_position, pos6, "$g_player"),

                (get_distance_between_positions, ":agent_distance_to_target", pos6, pos4),
                (lt, ":agent_distance_to_target", 2000),
                (val_add,":pay_count",1),
			(try_end),
			(get_player_agent_no,   ":player_agent"),
			(agent_get_team, ":player_team",  ":player_agent"),
			(try_for_agents, ":agent_id"),
				(agent_get_troop_id, ":troop_id", ":agent_id"),
				(this_or_next|is_between, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
				(is_between, ":troop_id", companions_begin, companions_end), #set neutral bodyguards back to player team - krag
				(main_party_has_troop, ":troop_id"),
				(agent_set_team, ":agent_id", ":player_team"),
			(try_end),
            (display_message,"@You won the brawl!", message_positive),
        (else_try),
            (lt, "$g_attacker_drawn_weapon", "itm_tutorial_spear"),
            (try_begin),
                (try_for_range, ":item_slot", ek_item_0, ek_head),
                    (agent_get_item_slot, ":item_no", "$g_main_attacker_agent", ":item_slot"),
                    (gt, ":item_no", 0),
					(store_free_inventory_capacity, ":inv_space"),
					(ge, ":inv_space", 1),
                    (troop_add_item, "trp_player", ":item_no", 0), # SB: add attacker sword
                (try_end),
            (try_end),
            #SB : this is useless, change with town instead
            (try_begin),
                (agent_is_wounded, "$g_main_attacker_agent"),
                (call_script, "script_change_player_relation_with_center", "$current_town", 1), #useless, increase with town instead
            (try_end),
        (else_try),
			(store_free_inventory_capacity, ":inv_space"),
			(ge, ":inv_space", 1),
            (troop_add_item, "trp_player", "$g_attacker_drawn_weapon", 0), # SB: add attacker sword
            (try_begin),
                (agent_is_wounded, "$g_main_attacker_agent"),
                (call_script, "script_change_player_relation_with_center", "$current_town", 1), #useless, increase with town instead
            (try_end),
        (try_end),

        (try_begin),
            (eq, ":type", "trp_brawler"),
            (assign,":xmoney",25),
            (val_mul, ":xmoney", ":pay_count"),
            (val_div, ":xmoney", 2),
            (store_skill_level, ":luck", skl_luck, "trp_player"),
            (val_add,":luck",100),
            (val_mul, ":xmoney", ":luck"),
            (val_div, ":xmoney", 100),

        (else_try),
            (store_skill_level, ":luck", skl_luck, "trp_player"),
            # (assign,":money",50),
            (assign,":xmoney",50),
            (val_add,":luck",100),

            (val_mul, ":xmoney", ":luck"),
            (val_div, ":xmoney", 100),
            # (val_add, ":money", ":xmoney"),
        (try_end),

        (troop_add_gold, "trp_player", ":xmoney"),
        # (troop_add_gold, "trp_player", 50),
        (assign, "$g_main_attacker_agent", 0),
        (troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, -1),
        (troop_set_slot, "trp_fight_promoter", slot_troop_cur_center, -1),
	  ]),

	  #Aftermath talks
      (3, 0, ti_once,
      [
	    (neg|conversation_screen_is_active),
		# (eq, "$talk_context", tc_tavern_talk),
		(gt, "$g_main_attacker_agent", 0),
		(main_hero_fallen),
      ],
      [
	  (jump_to_menu, "mnu_lost_tavern_duel"),
	  (finish_mission,0)

	  ]),


	  # #No shooting in the tavern
      # (1, 0, 0,
      # [
	    # (neg|conversation_screen_is_active),
		# (eq, "$talk_context", tc_tavern_talk),
		# (gt, "$g_main_attacker_agent", 0),

		# (get_player_agent_no, "$g_player"),
		# (agent_is_alive, "$g_player"),
		# ## SB : move diplomacy standing check back up here in conditions
		# (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$g_encountered_party_faction"),
		# (lt, reg0, DPLMC_FACTION_STANDING_MEMBER),
		# (agent_get_wielded_item, ":wielded_item", "$g_player", 0),
		# (gt, ":wielded_item", 0),
		# (item_get_type, ":type", ":wielded_item"),
		# (this_or_next|is_between, ":type", itp_type_bow, itp_type_goods),
		# (is_between, ":type", itp_type_pistol, itp_type_bullets),
		# # (is_between, ":wielded_item", "itm_darts", "itm_torch"),
		# # (neq, ":wielded_item", "itm_javelin_melee"),
		# # (neq, ":wielded_item", "itm_throwing_spear_melee"),
		# # (neq, ":wielded_item", "itm_jarid_melee"),
		# # (neq, ":wielded_item", "itm_light_throwing_axes_melee"),
		# # (neq, ":wielded_item", "itm_throwing_axes_melee"),
		# # (neq, ":wielded_item", "itm_heavy_throwing_axes_melee"),
        # #SB : also add these conditions

      # ],
      # [
		# (party_get_slot, ":tavernkeeper", "$g_encountered_party", slot_town_tavernkeeper),
		# # ##diplomacy start+
		# # #Turn of this !@#$%ing obnoxious and totally illogical restriction provided:
		# # (try_begin),
			# # #1) there is an actual fight
			# # (gt, "$g_main_attacker_agent", 0),
			# # (agent_is_alive, "$g_main_attacker_agent"),
			# # (neg|agent_is_wounded, "$g_main_attacker_agent"),
			# # #2) the player is the lord of this town, a mercenary captain in the faction's employ, or ruler of this faction
			# # (store_faction_of_party , ":center_faction", "$g_encountered_party"),
			# # (this_or_next|eq, ":center_faction", "$players_kingdom"),
				# # (eq, ":center_faction", "fac_player_supporters_faction"),
		# # (else_try),
		# # #Else, original behavior:
			# (start_mission_conversation, ":tavernkeeper"),
		# # (try_end),
		# ##diplomacy stop+
	  # ]),

      #SB : drunks are totally effective fighters
      (3, 0, 0,
      [
       # (eq, "$talk_context", tc_tavern_talk),
       (ge, "$g_start_belligerent_drunk_fight", 1),
       (gt, "$g_main_attacker_agent", 0),
       (agent_is_alive, "$g_main_attacker_agent"),
       # (eq, "$g_belligerent_drunk_leaving", 0), #don't stumble while leaving
       (store_random_in_range, ":random_no", 0, 3),
       (eq, ":random_no", 0),
       ],
      [
      # (store_random_in_range, ":anim", "anim_strike_chest_front_stop", "anim_cheer"),
      (store_random_in_range, ":anim", "anim_strike3_head_left", "anim_fall_face_hold"),
      (agent_set_animation, "$g_main_attacker_agent", ":anim"),
      (store_random_in_range, ":progress", 0, 100),
      (agent_set_animation_progress, "$g_main_attacker_agent", ":progress"),
      ]),

      #Check for weapon in hand of attacker, also, everyone gets out of the way
      (1, 0, 0,
      [
        (gt, "$g_main_attacker_agent", 0),
      ],
      [
        (try_begin),
            (agent_get_troop_id, ":type", "$g_main_attacker_agent"),
            (eq, ":type", "trp_brawler"),
            (call_script, "script_neutral_behavior_in_brawl"),
        # (else_try),      # #krag robbery disabled in favour of shooting/hitting system
            # (agent_get_wielded_item, ":wielded_item", "$g_main_attacker_agent", 0),
            # (val_max, "$g_attacker_drawn_weapon", ":wielded_item"),

            # (call_script, "script_neutral_behavior_in_fight"),
        (try_end),

      ]),

      (ti_on_agent_spawn, 0, 0, [],
      [
        (store_trigger_param_1, ":agent_no"),

        (try_begin),
          (this_or_next|eq, "$has_prison_key", 1),	#krag robbery added this line
		  (this_or_next|eq, "$talk_context", tc_escape),
          (eq, "$talk_context", tc_prison_break),
          (agent_get_troop_id, ":troop_no", ":agent_no"),
		  (try_begin),	#krag robbery added this section to force player weild
				(eq, ":troop_no", 0),
				(get_player_agent_no, ":player"),
				(call_script, "script_cf_agent_wield_weapons", ":player"),
		  (try_end),
          (troop_slot_eq, ":troop_no", slot_troop_will_join_prison_break, 1),
		  (neg|main_party_has_troop, ":troop_no"),#krag robbery block bodyguards, handled elsewhere
          #(agent_set_team, ":agent_no", 0),
          (agent_ai_set_aggressiveness, ":agent_no", 5),
          #(troop_set_slot, ":troop_no", slot_troop_will_join_prison_break, 0),#krag robbery disabled, reset in ti_on_switch_to_map

			(get_player_agent_no, "$g_player"),
			(agent_get_team, ":playerteam", "$g_player"),
			(agent_get_position, pos1, "$g_player"),

			(agent_set_team, ":agent_no", ":playerteam"),
			(agent_set_division, ":agent_no", 8),
			(agent_add_relation_with_agent, ":agent_no", "$g_player", 1), 	#maybe clears the sticking-to-player bug? something here does
			(agent_set_is_alarmed, ":agent_no", 1),

			(store_random_in_range, ":shift", 1, 3),	#krag robbery copied this section from bodyguard triggers to move them near player when exiting fort etc
			(val_mul, ":shift", 50), 	#less than 100 causes sticking-to-player bug
			(position_move_y, pos1, ":shift"),
			(store_random_in_range, ":shift", 1, 3),
			(store_random_in_range, ":shift_2", 0, 2),
			(val_mul, ":shift_2", -1),
			(try_begin),
				(neq, ":shift_2", 0),
				(val_mul, ":shift", ":shift_2"),
			(try_end),
			(position_move_x, pos1, ":shift"),
			(position_set_z_to_ground_level, pos1),
			(agent_set_position, ":agent_no", pos1),

          (try_begin),
            (troop_slot_eq, ":troop_no", slot_troop_mission_participation, mp_prison_break_stand_back),
            (agent_get_position, pos1, ":agent_no"),
            (agent_set_scripted_destination, ":agent_no", pos1),
          (try_end),
        (else_try),
          (call_script, "script_init_town_agent", ":agent_no"),
        (try_end),
      ]),

      (1, 0, ti_once,
      [],
      [
        (try_begin),
          (eq, "$g_mt_mode", tcm_default),
          (store_current_scene, ":cur_scene"),
          (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
        (try_end),
        (call_script, "script_init_town_walker_agents"),
        # (try_begin),
          # (eq, "$sneaked_into_town", 1),
          # (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
        # (else_try),
          # (call_script, "script_music_set_situation_with_culture", mtf_sit_town),
        # (try_end),
      ]),

      (ti_inventory_key_pressed, 0, 0,
      [
        (try_begin),
          (eq,"$has_prison_key",0),	#krag robbery added these 3 lines to stop refilling ammo during robbery
		  (eq,"$has_castle_key",0),
		  (eq,"$robbery_in_progress",0),

		  (eq, "$g_main_attacker_agent", 0),
          (eq, "$g_mt_mode", tcm_default),
          # (show_object_details_overlay, 1),
          (set_trigger_result,1),
        (else_try),
          (eq, "$g_mt_mode", tcm_disguised),
          (display_message,"str_cant_use_inventory_disguised",message_alert),
        (else_try),
          (display_message, "str_cant_use_inventory_now",message_alert),
        (try_end),
      ],
      []),

      (ti_tab_pressed, 0, 0,
      [
        (try_begin),
          (this_or_next|eq, "$talk_context", tc_escape),
          (this_or_next|eq, "$talk_context", tc_prison_break),
          (gt, "$g_main_attacker_agent", 0),
          (display_message, "str_cannot_leave_now",message_alert),
        (else_try),
          (this_or_next|eq, "$g_mt_mode", tcm_default),
          (eq, "$g_mt_mode", tcm_disguised),
          (mission_enable_talk),
#          (get_player_agent_no, "$g_player"),
#          (agent_get_horse, ":player_horse","$g_player"),
#          (try_begin),
#            (le, ":player_horse", 0),
#            (agent_get_position,pos10,"$g_player"),
#          # (else_try),
#            # (agent_get_position,pos10,":player_horse"),
#            (assign,"$position_mod_value",pos10),
#            (assign,"$position_mod",1),
#            (assign,"$position_party", "$current_town"),
#          (try_end),
          (set_trigger_result,1),
        (else_try),
          (display_message, "str_cannot_leave_now",message_alert),
        (try_end),
      ],
      []),

      (ti_on_leave_area, 0, 0,
      [
        (try_begin),
          (eq, "$g_defending_against_siege", 0),
          (assign,"$g_leave_town",1),
        (try_end),
      ],
      [
        (try_begin),
          (this_or_next|eq, "$talk_context", tc_prison_break),
		  (this_or_next|eq,"$has_prison_key",1),
		  (this_or_next|eq,"$has_castle_key",1),
		  (this_or_next|eq,"$robbery_in_progress",1),
		  (eq, "$talk_context", tc_escape),
          (call_script, "script_deduct_casualties_from_garrison"),
          #(jump_to_menu,"mnu_sneak_into_town_caught_dispersed_guards"),#why this? strange - krag
          (jump_to_menu,"mnu_sneak_into_town_caught_ran_away"),
        (try_end),

        (mission_enable_talk),
      ]),

     # # (0, 0, ti_once,
     # # [],
     # # [
       # # (party_slot_eq, "$current_town", slot_party_type, spt_town),
       # # # (call_script, "script_town_init_doors", 0),
       # # (try_begin),
         # # (eq, "$town_nighttime", 0),
         # # (play_sound, "snd_town_ambiance", sf_looping),
       # # (try_end),
     # # ]),

	(3, 0, 0,[(call_script, "script_tick_town_walkers")],[]),

	#JAILBREAK TRIGGERS
	#Civilians get out of the way
  (1, 0, 0,
    [
      (this_or_next|eq, "$talk_context", tc_prison_break),
        (eq, "$talk_context", tc_escape),
    ],
    [
      #(agent_get_team, ":prisoner_agent", 0),
      #(call_script, "script_neutral_behavior_in_fight"),	#krag robbery disabled in favour of below system
      (mission_disable_talk),
    ]),

	#krag robbery jailbreak new panick system
	(ti_on_agent_hit, 0, 0, [
	(le, "$g_start_promoted_fight", 0),
	],
   [
      (store_trigger_param_1, ":target"),
      (store_trigger_param_2, ":dealer"),
      #(store_trigger_param_3, ":damage"),
      #(store_trigger_param, ":hitbone", 4),
	  (store_trigger_param, ":ammo_type", 5),
	  # reg0            = weapon item_id
	  # pos0            = position of the hit area, rotation fields contain the direction of the blow
	  (neq, ":target", ":dealer"),
	   (agent_is_human,":target"),
	(agent_get_position, pos12, ":target"),
	(call_script, "script_hit_alerts_guards_panicks_civilians", ":dealer", ":ammo_type"),#needs target in pos12
   ]),

   (0.2, 0, 0,	# krag robbery clear panicking agents
    [
      (this_or_next|eq,"$has_prison_key",1),	#krag robbery added these
		(this_or_next|eq,"$has_castle_key",1),
		(this_or_next|eq,"$robbery_in_progress",1),
	  (this_or_next|eq, "$talk_context", tc_prison_break),
	  (this_or_next|party_slot_eq, "$current_town", slot_center_has_attacker,3),#make it work during bandit attack
        (eq, "$talk_context", tc_escape),
    ],
    [
     (call_script, "script_clear_panicking_agents_near_passages", 250),
    ]),

	(2.1, 0, ti_once,	#krag robbery failure results in capture
      [
	    (neg|conversation_screen_is_active),
		(this_or_next|eq,"$has_prison_key",1),
		(this_or_next|eq,"$has_castle_key",1),
		(this_or_next|eq,"$robbery_in_progress",1),
        (this_or_next|eq, "$talk_context", tc_escape),
		(eq, "$talk_context", tc_prison_break),
		(main_hero_fallen),
      ],
      [
    (assign, "$capturer_party", "$g_encountered_party"), # set variable properly
	  (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
	  (finish_mission,0)
	  ]),

	#The game begins with the town alerted
    (1, 0, ti_once,
      [
        #If I set this to 1, 0, ti_once, then the prisoner spawns twice
		(this_or_next|eq,"$has_prison_key",1),	#krag robbery added these 3 lines
		(this_or_next|eq,"$has_castle_key",1),
		(this_or_next|eq,"$robbery_in_progress",1),
        (eq, "$talk_context", tc_escape),
	  ],
	  [
	    (assign, reg6, "$g_player"),
		(call_script, "script_activate_town_guard"),
		(mission_disable_talk),

		(agent_get_position, pos4, "$g_player"),

		(try_for_range, ":prisoner", active_npcs_begin, kingdom_ladies_end),
		  (troop_slot_ge, ":prisoner", slot_troop_mission_participation, mp_prison_break_fight),
			(store_troop_health, ":prisoner_health", ":prisoner"),	#krag robbery added these to stop KO'd lords respawning
			(neq, ":prisoner_health", 0),
		  (str_store_troop_name, s4, ":prisoner"),
		  (display_message, "str_s4_joins_prison_break",message_positive),

          (store_current_scene, ":cur_scene"),
          (modify_visitors_at_site, ":cur_scene"),

          (add_visitors_to_current_scene, 24, ":prisoner", 1, 0, 0),
          (troop_set_slot, ":prisoner", slot_troop_will_join_prison_break, 1),
		  (assign, "$talk_context", tc_escape),	#krag robbery add this line to allow succesful rscue even with scene switching shenanigans
        (try_end),
	  ]),

	#loud robbery/raid unalarmed guards occasionally walk towards the player position - krag
    (2, 0, 0,
      [
	  (eq, "$loud_robbery_in_progress", 1),
	  ],
	  [
			(get_player_agent_no, "$g_player"),
			#(display_message, "@loud robbery in progress town_center 2",message_alert),
			(agent_get_position, pos12, "$g_player"),
			#(call_script, "script_hit_alerts_guards_panicks_civilians", "$g_player", "itm_large_caliber_ammo_pw"),
			(try_for_agents, ":turning_agent"),
				(agent_get_troop_id, ":troop", ":turning_agent"),
				(is_between, ":troop", soldiers_begin, soldiers_end),
				
				(agent_slot_eq, ":turning_agent", slot_agent_is_running_away, 0),
				(agent_is_human, ":turning_agent"),
				(agent_is_alive, ":turning_agent"),
				(agent_is_active, ":turning_agent"),
				(try_begin),
					(agent_is_alarmed, ":turning_agent"),
					(agent_clear_scripted_mode, ":turning_agent"),
					#(agent_force_rethink, ":turning_agent"),
				  (else_try),
					#(neg|agent_is_alarmed, ":turning_agent"),
					(store_random_in_range, ":rand", 0, 10),
					(eq, ":rand", 9),
					(agent_set_no_dynamics, ":turning_agent", 0),
					#(agent_set_speed_limit, ":turning_agent", 99),
					(agent_set_slot, ":turning_agent", slot_agent_static_npc, 0),
					(agent_set_slot, ":turning_agent", slot_agent_walker_occupation, 0),
					(agent_set_animation_progress, ":turning_agent", 99),
					(agent_set_scripted_destination, ":turning_agent", pos12, 1, 0),
					#(agent_set_is_alarmed, ":turning_agent", 1),
				(try_end),
			(try_end),
	  ]),

   (3, 0, 0,
   [
     (main_hero_fallen, 0),
   ],
   [
     (try_begin),
       (this_or_next|eq, "$talk_context", tc_prison_break),
       (eq, "$talk_context", tc_escape),

       (call_script, "script_deduct_casualties_from_garrison"),
	   (jump_to_menu,"mnu_captivity_start_castle_defeat"),

	   (assign, ":end_cond", kingdom_ladies_end),
       (try_for_range, ":prisoner", active_npcs_begin, ":end_cond"),
  	     (troop_set_slot, ":prisoner", slot_troop_mission_participation, 0), #new
  	   (try_end),

	   (mission_enable_talk),
	   (finish_mission, 0),
	 (else_try),
	   (set_trigger_result,1),
	 (try_end),
   ]),

   (3, 0, 0,
   [
	 (eq, "$talk_context", tc_escape),
	 (neg|main_hero_fallen,0),
     (store_mission_timer_a, ":time"),
     (ge, ":time", 10),

     (all_enemies_defeated), #1 is default enemy team for in-town battles
   ],
   [
     (call_script, "script_deduct_casualties_from_garrison"),
	 (try_for_agents, ":agent_id"),
	 (agent_get_troop_id, ":troop", ":agent_id"),
       (troop_slot_ge, ":troop", slot_troop_mission_participation, mp_prison_break_fight),
       (try_begin),
         (agent_is_alive, ":agent_id"),
         (troop_set_slot, ":troop", slot_troop_mission_participation, mp_prison_break_escaped),
       (else_try),
         (troop_set_slot, ":troop", slot_troop_mission_participation, mp_prison_break_caught),
       (try_end),
     (try_end),
     (jump_to_menu,"mnu_sneak_into_town_caught_ran_away"),

     (mission_enable_talk),
     (finish_mission,0)
   ]),

   (ti_on_agent_killed_or_wounded, 0, 0, [],
   [
     (store_trigger_param_1, ":dead_agent_no"),
     (store_trigger_param_2, ":killer_agent_no"),
     #(store_trigger_param_3, ":is_wounded"),

	  (agent_is_human,":dead_agent_no"),
     (agent_get_troop_id, ":dead_agent_troop_no", ":dead_agent_no"),
     #(agent_get_troop_id, ":killer_agent_troop_no", ":killer_agent_no"),
	 (agent_get_team, ":killer_team",  ":killer_agent_no"),	#krag for below
	 (get_player_agent_no, ":player_agent"),
	 (agent_get_team, ":player_team",  ":player_agent"),
	 #(agent_get_wielded_item, ":killer_weapon",  ":killer_agent_no", 0),

     (try_begin),
       (le,"$has_prison_key",0),
	   # (this_or_next|eq, ":dead_agent_troop_no", "trp_swadian_prison_guard"),
       (this_or_next|eq, ":dead_agent_troop_no", "trp_f1_guard"),
       # (this_or_next|eq, ":dead_agent_troop_no", "trp_vaegir_prison_guard"),
       (this_or_next|eq, ":dead_agent_troop_no", "trp_f2_guard"),
       (this_or_next|eq, ":dead_agent_troop_no", "trp_f3_guard"),
       (this_or_next|eq, ":dead_agent_troop_no", "trp_f4_guard"),
       (this_or_next|eq, ":dead_agent_troop_no", "trp_f5_guard"),
       (eq, ":dead_agent_troop_no", "trp_f6_guard"),

       #(eq, ":killer_agent_troop_no", "trp_player"),	#krag robbery replaced with team as bodyguard can be the one to do it
	    (eq, ":player_team",  ":killer_team"),

       #SB : proper string
       (display_message, "@You got keys to the dungeon.", message_positive),
	   (assign,"$has_prison_key",1), 	#krag robbery allows to enter prison after starting robbery
	 (else_try),						#krag robbery allows to enter fort
		(le,"$has_castle_key",0),
		(eq, ":player_team",  ":killer_team"),
		(faction_slot_eq, "$g_encountered_party_faction", slot_faction_castle_guard_troop, ":dead_agent_troop_no"),
		(display_message, "@You got keys to the hall.", message_positive),
	    (assign,"$has_castle_key",1),
	 (else_try),						#krag robbery allows to enter shop
		(le,"$has_shop_key",0),
		(eq, ":player_team",  ":killer_team"),
		(this_or_next|is_between, ":dead_agent_troop_no", goods_merchants_begin, goods_merchants_end),
		(is_between, ":dead_agent_troop_no", mayors_begin, mayors_end),
		(call_script, "script_change_player_relation_with_center", "$current_town", -1),
		(store_faction_of_party, ":town_faction", "$current_town"),
		(call_script, "script_change_player_relation_with_faction", ":town_faction", -1),
		(is_currently_night),
		(display_message, "@You got the key to the shopfront.", message_positive),
	    (assign,"$has_shop_key",1),
	    (assign,"$robbery_in_progress",1),
     (else_try), #SB : do this here instead of post-combat
       (troop_is_hero, ":dead_agent_troop_no"),
       (troop_slot_ge, ":dead_agent_troop_no", slot_troop_mission_participation, mp_prison_break_fight),
       (troop_set_slot, ":dead_agent_troop_no", slot_troop_mission_participation, mp_prison_break_caught),
	 (else_try),
		(party_get_slot, ":merc_type", "$current_town", slot_center_mercenary_troop_type),
		(eq, ":dead_agent_troop_no", ":merc_type"),
		(party_set_slot, "$current_town", slot_center_mercenary_troop_type, -1),
		(party_set_slot, "$current_town", slot_center_mercenary_troop_amount, -1),
	  (else_try),
	    (eq, ":player_team",  ":killer_team"),
		(is_between, ":dead_agent_troop_no", armor_merchants_begin, goods_merchants_end),
		(call_script, "script_change_player_relation_with_center", "$current_town", -1),
		(store_faction_of_party, ":town_faction", "$current_town"),
		(call_script, "script_change_player_relation_with_faction", ":town_faction", -1),
     (try_end),
   ]),
  ]),

("village_center",0,-1,
    "village center",
    [(0,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (1,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),

     (8,mtef_visitor_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_visitor_source,0,0,1,[]),(14,mtef_visitor_source,0,0,1,[]),(15,mtef_visitor_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source,af_override_horse,0,1,[]),(41,mtef_visitor_source,af_override_horse,0,1,[]),(42,mtef_visitor_source,af_override_horse,0,1,[]),(43,mtef_visitor_source,af_override_horse,0,1,[]),(44,mtef_visitor_source,af_override_horse,0,1,[]),(45,mtef_visitor_source,af_override_horse,0,1,[]),(46,mtef_visitor_source,af_override_horse,0,1,[]),(47,mtef_visitor_source,af_override_horse,0,1,[]),
     # ], tocan_ambience+tocan_common_triggers+tocan_walkers+bodyguard_triggers+tocan_center_attack+#common_first_time+#+tocan_flashlight+
     ], tocan_ambience+tocan_common_triggers+tocan_autofire+tocan_flashlight+x_companion+tocan_walkers+bodyguard_triggers+tocan_center_attack+

    [
############################
      common_position,
      common_agent_label,
      common_torch_at_night,
      particle_preview,
      common_info_message,

    (ti_after_mission_start, 0, ti_once, [], [
        (scene_prop_get_num_instances, ":total", "spr_windmill_fan_turning"),
        (try_begin),
            (ge, ":total", 1),

            (try_for_range,":cur_instance",0,":total"),
                (scene_prop_get_instance, ":instance_id", "spr_windmill_fan_turning", ":cur_instance"),
                (ge, ":instance_id", 0),
                (assign,"$windmill",1),
            (try_end),
        (else_try),
                (assign,"$windmill",0),
        (try_end),

        ]),

    (1, 0, 0, [(eq,"$windmill",1),], [
        (scene_prop_get_num_instances, ":total", "spr_windmill_fan_turning"),
        (try_for_range,":cur_instance",0,":total"),
            (scene_prop_get_instance, ":instance_id", "spr_windmill_fan_turning", ":cur_instance"),
            (ge, ":instance_id", 0),
            (call_script, "script_cf_turn_windmill_fans", ":cur_instance"),
        (try_end),
        ]),

    # # (0, 0, 0,
    # # [
      # # (key_clicked, key_m),
    # # ],
    # # [
        # # # (set_fixed_point_multiplier, 100),
        # # # (try_begin),
            # # (get_player_agent_no,"$g_player"),
            # # (agent_get_position, pos1, "$g_player"),
            # # (call_script,"script_debug_pos",pos1),
				# # # (position_get_x, reg1, pos1),
				# # # (position_get_y, reg2, pos1),
				# # # (position_get_z, reg3, pos1),
                # # # (display_message, "@X: {reg1}"),
                # # # (display_message, "@Y: {reg2}"),
                # # # (display_message, "@Z: {reg3}"),
        # # # (try_end),
    # # ]),


    (1, 0, ti_once, [], [
          (store_current_scene, ":cur_scene"),
          (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
          (call_script, "script_init_town_walker_agents"),
          # (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
        ]),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
      (ti_inventory_key_pressed, 0, 0, [
      #SB : same conditions, no weapon switching mid-fight
        (try_begin),
          (check_quest_active, "qst_hunt_down_fugitive"),
          (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
          (neg|check_quest_failed, "qst_hunt_down_fugitive"),
          (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_current_state, 1),
          (display_message, "str_cant_use_inventory_now",message_alert),
        (else_try),
          (check_quest_active, "qst_wanted_fugitive"),
          (neg|check_quest_succeeded, "qst_wanted_fugitive"),
          (neg|check_quest_failed, "qst_wanted_fugitive"),
          (quest_slot_eq, "qst_wanted_fugitive", slot_quest_current_state, 1),
          (display_message, "str_cant_use_inventory_now",message_alert),
        (else_try),
          # (show_object_details_overlay, 1),
          (set_trigger_result,1),
        (try_end),], []),
      (ti_tab_pressed, 0, 0, [(try_begin),
                                (check_quest_active, "qst_hunt_down_fugitive"),
                                (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
                                (neg|check_quest_failed, "qst_hunt_down_fugitive"),
                                (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
                                (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_current_state, 1),
                                (try_begin),
                                  (call_script, "script_cf_troop_agent_is_alive", "trp_fugitive"),
                                  (call_script, "script_fail_quest", "qst_hunt_down_fugitive"),
                                (else_try),
                                  (call_script, "script_succeed_quest", "qst_hunt_down_fugitive"),
                                (try_end),
                              (else_try),
                                (check_quest_active, "qst_wanted_fugitive"),
                                (neg|check_quest_succeeded, "qst_wanted_fugitive"),
                                (neg|check_quest_failed, "qst_wanted_fugitive"),
                                # (quest_slot_eq, "qst_wanted_fugitive", slot_quest_target_center, "$current_town"),
                                (quest_slot_eq, "qst_wanted_fugitive", slot_quest_current_state, 1),
                                (call_script, "script_get_correct_fugitive_troop_to_reg0"),
                                (assign, ":var3", reg0),
                                (try_begin),
                                  (call_script, "script_cf_troop_agent_is_alive", ":var3"),
                                  (call_script, "script_fail_quest", "qst_wanted_fugitive"),
                                (else_try),
                                  (call_script, "script_succeed_quest", "qst_wanted_fugitive"),
                                (try_end),
                              (try_end),
                              (get_player_agent_no, "$g_player"),
                              (agent_get_horse, ":player_horse","$g_player"),
                              (try_begin),
                                (le, ":player_horse", 0),
                                (agent_get_position,pos10,"$g_player"),
                              # (else_try),
                                # (agent_get_position,pos10,":player_horse"),
                                (assign,"$position_mod_value",pos10),
                                (assign,"$position_mod",1),
                                (assign,"$position_party", "$current_town"),
                              (try_end),

                              (set_trigger_result,1)], []),
      (ti_on_leave_area, 0, 0, [
          (try_begin),
            (assign,"$g_leave_town",1),
          (try_end),
          ], []),
      (3, 0, 0, [(call_script, "script_tick_town_walkers")], []),
      # (2, 0, 0, [(call_script, "script_cf_warzone_ambience", 0),], []),


      (1, 0, ti_once, [
        (check_quest_active, "qst_wanted_fugitive"),
        (neg|check_quest_succeeded, "qst_wanted_fugitive"),
        (neg|check_quest_failed, "qst_wanted_fugitive"),

        (quest_slot_eq, "qst_wanted_fugitive", slot_quest_target_center, "$current_town"),
        (quest_slot_eq, "qst_wanted_fugitive", slot_quest_current_state, 0),
                       ],
       [
        (call_script, "script_get_correct_fugitive_troop_to_reg0"),
        (assign, ":var3", reg0),
        (try_begin),
          (eq, ":var3",  "trp_fugitive_wanted_1"),
          (store_random_in_range,":rnd",0,10),
          (eq, ":rnd",  1),
          (quest_set_slot, "qst_wanted_fugitive", slot_quest_current_state, 1),
          (call_script, "script_activate_tavern_attackers"),
        (else_try),
          (eq, ":var3",  "trp_fugitive_wanted_2"),
          (store_random_in_range,":rnd",0,5),
          (eq, ":rnd",  1),
          (quest_set_slot, "qst_wanted_fugitive", slot_quest_current_state, 1),
          (call_script, "script_activate_tavern_attackers"),
        (else_try),
          (eq, ":var3",  "trp_fugitive_wanted_3"),
          (store_random_in_range,":rnd",0,3),
          (eq, ":rnd",  1),
          (quest_set_slot, "qst_wanted_fugitive", slot_quest_current_state, 1),
          (call_script, "script_activate_tavern_attackers"),
        (try_end),

        ]),
      (1, 0, ti_once, [

                       (check_quest_active, "qst_wanted_fugitive"),
                       (neg|check_quest_succeeded, "qst_wanted_fugitive"),
                       (neg|check_quest_failed, "qst_wanted_fugitive"),

                       # (quest_slot_eq, "qst_wanted_fugitive", slot_quest_target_center, "$current_town"),
                       (quest_slot_eq, "qst_wanted_fugitive", slot_quest_current_state, 1),
                       (assign, ":not_alive", 0),
                       (call_script, "script_get_correct_fugitive_troop_to_reg0"),
                       (assign, ":var3", reg0),
                       (try_begin),
                         (call_script, "script_cf_troop_agent_is_alive", ":var3"),
                       (else_try),
                         (assign, ":not_alive", 1),
                       (try_end),
                       (this_or_next|main_hero_fallen),
                       (eq, ":not_alive", 1),
                       ],
       [(try_begin),
          (main_hero_fallen),
          (call_script, "script_fail_quest", "qst_wanted_fugitive"),
          (finish_mission, 4),
        (else_try),
          # (call_script, "script_change_player_relation_with_center", "$current_town", -2),
          (call_script, "script_succeed_quest", "qst_wanted_fugitive"),
        (try_end),
        ]),

      #SB : replace with agent triggers
      # (1, 0, ti_once, [(check_quest_active, "qst_hunt_down_fugitive"),
                       # (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
                       # (neg|check_quest_failed, "qst_hunt_down_fugitive"),
                       # (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_current_state, 1),
                       # (assign, ":not_alive", 0),
                       # (try_begin),
                         # (call_script, "script_cf_troop_agent_is_alive", "trp_fugitive"),
                       # (else_try),
                         # (assign, ":not_alive", 1),
                       # (try_end),
                       # (this_or_next|main_hero_fallen),
                       # (eq, ":not_alive", 1),
                       # ],
       # [(try_begin),
          # (main_hero_fallen),
          # (jump_to_menu, "mnu_village_hunt_down_fugitive_defeated"),
          # (call_script, "script_fail_quest", "qst_hunt_down_fugitive"),
          # (finish_mission, 4),
        # (else_try),
          # (call_script, "script_change_player_relation_with_center", "$current_town", -2),
          # (call_script, "script_succeed_quest", "qst_hunt_down_fugitive"),
        # (try_end),
        # ]),


   (ti_on_agent_killed_or_wounded, 0, 0, [(check_quest_active, "qst_hunt_down_fugitive"), #not ti_once
                       (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
                       (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),],
   [
    (store_trigger_param_1, ":dead_agent_no"),
    # (store_trigger_param_2, ":killer_agent"),
    (agent_is_human, ":dead_agent_no"),
    (store_trigger_param_3, ":is_wounded"),
    # (get_player_agent_no, "$g_player"),
    (agent_get_troop_id, ":corpse", ":dead_agent_no"),
    (try_begin),
      (this_or_next|eq, ":dead_agent_no", "$g_player"),
      (main_hero_fallen),#should be same

      (jump_to_menu, "mnu_village_hunt_down_fugitive_defeated"),
      # (call_script, "script_fail_quest", "qst_hunt_down_fugitive"), #do this from menu so we can reuse it
      (finish_mission, 4),
    (else_try),
      (eq, ":corpse", "trp_fugitive"),
      (party_remove_members, "$current_town", "trp_fugitive", 1),
      # (eq, ":killer_agent", "$g_player"), #bodyguards, villagers also applicable
      (try_begin),
        (eq, ":is_wounded", 0),#killed rather than wounded
        (call_script, "script_change_player_relation_with_center", "$current_town", -2),
      (else_try),
        # (display_message, "@You leave the fugitive to villager's justice.", message_positive),
        (party_force_add_prisoners, "p_main_party", "trp_fugitive", 1),
        (quest_set_slot, "qst_hunt_down_fugitive", slot_quest_current_state, 2), #enter phase 2 of bringing him back
      (try_end),
      (agent_get_wielded_item, ":item", ":dead_agent_no", 0),
      (try_begin),
        (gt, ":item", 0),
        (store_random_in_range, ":imod", imod_plain, imod_fine),
		(store_free_inventory_capacity, ":inv_space"),
		(ge, ":inv_space", 1),
        (troop_add_item, "trp_player", ":item", ":imod"),
        (agent_unequip_item, ":dead_agent_no", ":item"),
      (try_end),
      (call_script, "script_succeed_quest", "qst_hunt_down_fugitive"),
      (call_script, "script_deactivate_tavern_attackers"),
    (else_try), #villagers?
      (call_script, "script_change_player_relation_with_center", "$current_town", -1),
    (try_end),
   ]),
    ],
  ),

("bandits_at_night",0,-1,
    "Default town visit",
    [(0,mtef_scene_source|mtef_team_0, af_override_horse, aif_start_alarmed, 1, pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_visitor_source|mtef_team_0, af_override_horse, aif_start_alarmed, 1, []),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),

     (8,mtef_scene_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_scene_source,0,0,1,[]),(14,mtef_scene_source,0,0,1,[]),(15,mtef_scene_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(28,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(41,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(42,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(45,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(46,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(47,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     ], x_companion+tocan_ambience+tocan_common_triggers+tocan_battle_triggers+tocan_autofire+tocan_flashlight+bodyguard_triggers+
    [
      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (neq, ":troop_no", "trp_player"),
         (neq, ":troop_no", "trp_dog_companion"),
         (neq, ":troop_no", "trp_bot_companion"),
		 (neg|is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
		 (neg|is_between,":troop_no", companions_begin, companions_end),
         (agent_set_team, ":agent_no", 1),
		 (agent_get_position, pos1, ":agent_no"),
		 (get_player_agent_no, ":player"),
		 (try_begin),
			 (gt, ":player", -1),
			 (agent_get_position, pos2, ":player"),
			 (get_distance_between_positions_in_meters, ":dist", pos1, pos2),
			 (lt, ":dist", 25),
			 (call_script, "script_equip_best_melee_weapon",":agent_no", 0, 0, aordr_hold_your_fire),	#stop player getting blasted immediately
			 #(display_message, "@calling script_equip_best_melee_weapon"),
		 (try_end),
         ]),

      (ti_before_mission_start, 0, 0, [], [
	  (call_script, "script_change_banners_and_chest"),
	  (replace_scene_props, "spr_safe_merchant_closed", "spr_safe_merchant_open"),
	  (replace_scene_props, "spr_safe_vendors_closed", "spr_safe_vendors_open"),
	  (replace_scene_props, "spr_safe_lord_closed", "spr_safe_lord_open"),
	  ]),

      (4, 0, ti_once, [],
        [
          (try_begin),
              (ge, "$g_special_companion", 1),
              (assign, "$x_npc_order", -1),
              # (get_player_agent_no, "$g_player"),
              (agent_clear_scripted_mode, "$g_player_x_agent_no"),
              # (agent_get_team, ":player_team", "$g_player"),
              #(agent_add_relation_with_agent, "$g_player", "$g_player_x_agent_no", 1),
              (set_show_messages, 0),
              (team_give_order, "$g_player_team", grc_special, mordr_follow),
              (set_show_messages, 1),
          (try_end),
      ]),

      common_inventory_not_available,

      (ti_tab_pressed, 0, 0,
       [
         (display_message, "str_cannot_leave_now",message_alert),
         ], []),
      (ti_on_leave_area, 0, 0,
       [
         (try_begin),
           (eq, "$g_defending_against_siege", 0),
           (assign,"$g_leave_town",1),
         (try_end),
         ], []),

      (0, 0, ti_once, [],
       [
         # (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
         (set_party_battle_mode),
         # (party_slot_eq, "$current_town", slot_party_type, spt_town),
         # (call_script, "script_town_init_doors", 0),
        ]),


      (2, 0, ti_once, [],	#make player bodyguards actually attack as rather useless in follow mode - krag
       [
		(get_player_agent_no, "$g_player"),
		(agent_get_team, ":playerteam", "$g_player"),
		(set_show_messages, 0),
		(team_give_order, ":playerteam", 8, mordr_charge),
		(team_give_order, ":playerteam", 8, mordr_use_any_weapon),
		(set_show_messages, 1),
        ]),


      (1, 4, ti_once,
       [
         (store_mission_timer_a,":cur_time"),
         (ge, ":cur_time", 5),
         (this_or_next|main_hero_fallen),
         (num_active_teams_le,1)
         ],
       [
         (try_begin),
           (main_hero_fallen),
           (jump_to_menu, "mnu_town_bandits_failed"),
         (else_try),
           (jump_to_menu, "mnu_town_bandits_succeeded"),
         (try_end),
         (finish_mission),
         ]),
      ],
    ),


("village_training", mtf_arena_fight, -1,
    "village_training",
    [(2,mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm_staff]), #tocan todo
     (4,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_staff]),
     ], tocan_ambience+tocan_common_triggers+
    [
      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_train_peasants_against_bandits_training_succeeded", 0),
         (call_script, "script_change_banners_and_chest"),
         ]),

		 (ti_on_agent_spawn, 0, 0, [],
      [
        (store_trigger_param_1, ":agent_no"),
        (agent_get_troop_id, ":troop_no", ":agent_no"),
        (gt, ":troop_no", 0),
        (neq, ":troop_no", "trp_trainee_peasant"),
		(agent_fade_out, ":agent_no"),

      ]),

      common_arena_fight_tab_press,

      (ti_question_answered, 0, 0, [],
       [
         (store_trigger_param_1,":answer"),
         (eq,":answer",0),
         (finish_mission),
         ]),

      common_inventory_not_available,

      (1, 4, ti_once,
       [
         (this_or_next|main_hero_fallen),
         (num_active_teams_le, 1)
         ],
       [
         (try_begin),
           (neg|main_hero_fallen),
           (assign, "$g_train_peasants_against_bandits_training_succeeded", 1),
         (try_end),
         (finish_mission),
         ]),
      ],
    ),

("visit_town_castle",0,-1,
    "You enter the halls of the lord.",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons|af_override_head,0,1,pilgrim_disguise), #disguise added for robbery
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]), #for doors
     (5,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (8,mtef_visitor_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),
     (10,mtef_scene_source,af_override_horse,0,1,[]),
     (11,mtef_scene_source,af_override_horse,0,1,[]),
     (12,mtef_visitor_source,af_override_horse,0,1,[]),
     (13,mtef_visitor_source,0,0,1,[]),
     (14,mtef_visitor_source,0,0,1,[]),
     (15,mtef_visitor_source,0,0,1,[]),
     (16,mtef_visitor_source,af_castle_lord,0,1,[]),
     (17,mtef_visitor_source,af_castle_lord,0,1,[]),
     (18,mtef_visitor_source,af_castle_lord,0,1,[]),
     (19,mtef_visitor_source,af_castle_lord,0,1,[]),
     (20,mtef_visitor_source,af_castle_lord,0,1,[]),
     (21,mtef_visitor_source,af_castle_lord,0,1,[]),
     (22,mtef_visitor_source,af_castle_lord,0,1,[]),
     (23,mtef_visitor_source,af_castle_lord,0,1,[]),
     (24,mtef_visitor_source,af_castle_lord,0,1,[]),
     (25,mtef_visitor_source,af_castle_lord,0,1,[]),
     (26,mtef_visitor_source,af_castle_lord,0,1,[]),
     (27,mtef_visitor_source,af_castle_lord,0,1,[]),
     (28,mtef_visitor_source,af_castle_lord,0,1,[]),
     (29,mtef_visitor_source,af_castle_lord,0,1,[]),
     (30,mtef_visitor_source,af_castle_lord,0,1,[]),
     (31,mtef_visitor_source,af_castle_lord,0,1,[]),
     # (16,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons|af_override_head,0,1,[]), #SB : replacement
     ], tocan_common_triggers+bodyguard_triggers+
    [

      common_agent_label,

      (ti_on_agent_spawn, 0, 0, [],
      [
        (store_trigger_param_1, ":agent_no"),
        (call_script, "script_init_town_agent", ":agent_no"),
      ]),

      (ti_before_mission_start, 0, 0, [],
      [
        (call_script, "script_change_banners_and_chest"),
      ]),

      (ti_inventory_key_pressed, 0, 0,
      [
        # (show_object_details_overlay, 1),
		(eq,"$has_prison_key",0),	#krag robbery added these 3 lines to stop refilling ammo during robbery
		  (eq,"$has_castle_key",0),
		  (eq,"$robbery_in_progress",0),
        (set_trigger_result,1)
      ], []),

	  #adjust for prison break
      (ti_tab_pressed, 0, 0,
	  [
	    (eq,"$has_prison_key",0),	#krag robbery added these 3 lines to stop escaping during robbery
		  (eq,"$has_castle_key",0),
		  (eq,"$robbery_in_progress",0),
	    (set_trigger_result,1)
	  ], []),

      (ti_on_leave_area, 0, 0,
      [
 	    (eq, "$talk_context", tc_prison_break),
 	  ],
	  [
	    (display_message, "str_leaving_area_during_prison_break",message_alert),
	    (set_jump_mission, "mt_sneak_caught_fight"),
	  ]),

      (ti_after_mission_start, 0, ti_once, [], [
        (assign, ":no_fade", 0),
        (try_begin), #SB : reposition player agent if ruling at court
          (eq, "$g_player_court", "$current_town"),
          (eq, "$talk_context", tc_court_talk),
          (this_or_next|party_slot_eq, "$current_town", slot_party_temp_slot_1, "p_temp_party"),
          (party_slot_eq, "$current_town", slot_party_temp_slot_1, "p_temp_party_2"),
          (get_player_agent_no, ":agent_no"),
          (entry_point_get_position, pos1, 16),
          (agent_is_active, ":agent_no"),
          (agent_set_position, ":agent_no", pos1),
          # (entry_point_get_position, pos2, 0),
          # (agent_set_look_target_position, pos2, ":agent_no"),
          # (agent_set_position, ":agent_no", pos1),
        (else_try),
          (eq, "$talk_context", tc_court_talk),
          # (this_or_next|party_slot_eq, "$current_town", slot_town_lord, stl_unassigned),
          (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
          (troop_get_slot, ":employee", dplmc_employees_end, dplmc_slot_troop_affiliated),
          (neq, ":employee", 0),
          (assign, "$g_talk_agent", -1),
          (assign, "$g_main_attacker_agent", -1),
          (troop_is_hero, ":employee"),
          (call_script, "script_dplmc_get_court_guard_troop", "$current_town"),
          (assign, ":guard_troop", reg0),
          (try_for_agents, ":agent_no"),
            # (eq, "$g_talk_agent", -1),
            (agent_is_active, ":agent_no"),
            (agent_is_human, ":agent_no"),
            (agent_get_troop_id, ":troop_no", ":agent_no"),
            (try_begin),
              (eq, ":troop_no", ":employee"),
              (assign, "$g_talk_agent", ":agent_no"),
            (else_try), #guard troop
              (eq, ":troop_no", ":guard_troop"),
              (assign, "$g_main_attacker_agent", ":agent_no"),
            (try_end),
          (try_end),
          (neq, "$g_talk_agent", -1),
          (try_begin),
            (neq, "$g_main_attacker_agent", -1),
            (agent_get_position, pos1, "$g_main_attacker_agent"),
            (agent_set_visibility, "$g_main_attacker_agent", 0),
            (agent_fade_out, "$g_main_attacker_agent"),
            (agent_set_position, "$g_talk_agent", pos1),
          (try_end),
          # (get_player_agent_no, "$g_player"),
          # (agent_get_position, pos1, "$g_player"),
          # (agent_set_scripted_destination, "$g_talk_agent", pos1),
          # (try_begin),
            # (set_fixed_point_multiplier, 1000),
            # (scene_prop_get_instance, ":player_chest", "spr_player_chest", 0),
            # (ge, ":player_chest", 0),
            # (prop_instance_get_position, pos1, ":player_chest"),
            # (position_move_z, pos1, 500),
            # (position_rotate_y, pos1, 180),
            # (agent_set_position, "$g_player", pos1),
            # (agent_set_look_target_agent, "$g_player", "$g_talk_agent"),
          # (try_end),
          (start_mission_conversation, ":employee"),
          (assign, ":no_fade", 1),
          # (entry_point_get_position, pos2, 0),
          # (agent_set_look_target_position, pos2, ":agent_no"),
          # (agent_set_position, ":agent_no", pos1),
        (try_end),

        (try_begin),
          (eq, ":no_fade", 0),
          (try_begin),
            (eq, "$talk_context", tc_court_talk),
            (try_begin),
              (store_faction_of_party, ":center_faction", "$current_town"),
              (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
              (faction_slot_eq, ":center_faction", slot_faction_ai_object, "$current_town"),
              # (call_script, "script_music_set_situation_with_culture", mtf_sit_feast),
              # #(call_script, "script_music_set_situation_with_culture", mtf_sit_lords_hall),
            (try_end),
            (mission_cam_set_screen_color, 0xFF736252), #roughly the colour of the menu bg
            (mission_cam_animate_to_screen_color, 0x00736252, 1500),
          (else_try),
            (eq, ":no_fade", 0),
            (mission_cam_set_screen_color, 0xFF010203), #roughly dungeon moss/lichen colours
            (mission_cam_animate_to_screen_color, 0x00000000, 3000),
            # (call_script, "script_music_set_situation_with_culture", 0), #prison
          (try_end),
        (try_end),
        ]),

    #SB : chest presentation
      ## CC
      (1, 0, 5, [(key_is_down, key_right_mouse_button),
        (scene_prop_get_instance, ":player_chest", "spr_player_chest", 0),
        (ge, ":player_chest", 0),
        (prop_instance_get_position, pos1, ":player_chest"),
        # (get_player_agent_no, "$g_player"),
        (agent_is_active, "$g_player"),
        (agent_get_position, pos2, "$g_player"),
        (get_distance_between_positions, ":dist", pos1, pos2),
        (lt, ":dist", 250),],
        [

        (tutorial_message, -1),
        (call_script, "script_get_chest_troop", "$current_town"),
        (assign, "$g_pool_troop", reg0),
        (start_presentation, "prsnt_deposit_withdraw_money"),
      ]),

      (2, 1.5, 5, [(scene_prop_get_instance, ":player_chest", "spr_player_chest", 0),
        (ge, ":player_chest", 0),
        (prop_instance_get_position, pos1, ":player_chest"),
        # (get_player_agent_no, "$g_player"),
        (agent_get_position, pos2, "$g_player"),
        (get_distance_between_positions, ":dist", pos1, pos2),
        (lt, ":dist", 300),
        # (position_has_line_of_sight_to_position, pos2, pos1),
        (neg|position_is_behind_position, pos1, pos2),
        (neg|is_presentation_active, "prsnt_deposit_withdraw_money"),
        (neg|conversation_screen_is_active),
        ],
        [
        (tutorial_message_set_size, 17, 17),
        (tutorial_message_set_position, 500, 500),
        (tutorial_message_set_center_justify, 1),
        (tutorial_message_set_background, 1),
        (tutorial_message, "str_chest_info"),
      ]),

      (2, 0, 5, [(scene_prop_get_instance, ":player_chest", "spr_player_chest", 0),
        (ge, ":player_chest", 0),
        # (try_begin),
          # (neq, "$g_talk_agent", -1),
          # (get_player_agent_no, "$g_player"),
          # (agent_get_position, pos1, "$g_player"),
          # (agent_set_scripted_destination, "$g_talk_agent", pos1),
        # (try_end),
        (this_or_next|conversation_screen_is_active),
        (is_presentation_active, "prsnt_deposit_withdraw_money"),
        #TODO disable opening chest (it crashes)
        ],
        [
        # (tutorial_message_set_size, 17, 17),
        # (tutorial_message_set_position, 500, 500),
        # (tutorial_message_set_center_justify, 1),
        # (tutorial_message_set_background, 1),
        (tutorial_message, -1),
        (clear_omitted_keys),
        # (omit_key_once, key_f), #probably prevents accidental chest opens
      ]),

	  (0, 0, ti_once, [
	  (store_current_scene, ":current_scene"),
	  (neg|is_between, ":current_scene", "scn_town_1_prison", "scn_town_1_alley"),
	  ],		#krag robbery added to equip player and make ladies leave
      [
			(this_or_next|eq,"$has_prison_key",1),
			(this_or_next|eq,"$has_castle_key",1),
			(eq,"$robbery_in_progress",1),
			(get_player_agent_no, ":player"),

			(try_for_agents, ":agent"),
				(agent_get_troop_id, ":troop_id", ":agent"),
				(this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_id"),
				(this_or_next|eq, ":player" , ":agent"),
				(is_between, ":troop_id", companions_begin, companions_end),
				(agent_set_is_alarmed, ":agent", 1),
				(agent_set_team,":agent", "$g_player_team"),

				(troop_get_inventory_slot, ":item4", ":troop_id", 3),
				(try_begin),
					(gt, ":item4", 0),
					(agent_equip_item, ":agent", ":item4", 3),
					(agent_set_wielded_item, ":agent", ":item4"),
				(try_end),
				(troop_get_inventory_slot, ":item3", ":troop_id", 2),
				(try_begin),
					(gt, ":item3", 0),
					(agent_equip_item, ":agent", ":item3", 2),
					(agent_set_wielded_item, ":agent", ":item3"),
				(try_end),
				(troop_get_inventory_slot, ":item2", ":troop_id", 1),
				(try_begin),
					(gt, ":item2", 0),
					(agent_equip_item, ":agent", ":item2", 1),
					(agent_set_wielded_item, ":agent", ":item2"),
				(try_end),
				(troop_get_inventory_slot, ":item1", ":troop_id", 0),
				(try_begin),
					(gt, ":item1", 0),
					(agent_equip_item, ":agent", ":item1", 0),
					(agent_set_wielded_item, ":agent", ":item1"),
				(try_end),

				(troop_get_inventory_slot, ":item5", ":troop_id", 4), #helmet
				(try_begin),
					(gt, ":item5", 0),
					(agent_equip_item, ":agent", ":item5", 4),
				(try_end),
			(try_end),
      ]),

	  (1, 0, ti_once, [
	  (store_current_scene, ":current_scene"),
	  (neg|is_between, ":current_scene", "scn_town_1_prison", "scn_town_1_alley"),
	  ],		#krag robbery added to equip player and make ladies leave
      [
			(this_or_next|eq,"$has_prison_key",1),
			(this_or_next|eq,"$has_castle_key",1),
			(eq,"$robbery_in_progress",1),

			(get_player_agent_no, "$g_player"),
		    (agent_get_team, "$g_player_team", "$g_player"),
		    (set_show_messages, 0),
		    (team_give_order, "$g_player_team", grc_everyone, mordr_charge), #doesn't work if done at mission start for some reason
			(set_show_messages, 1),
      ]),

	   (2, 0, ti_once, [
	   (store_current_scene, ":scene"),
	  (neg|is_between, ":scene", "scn_town_1_prison", "scn_town_1_alley"),
	   ],		#krag robbery added to initiate violence during fort raid
      [
			(this_or_next|eq,"$has_prison_key",1),
			(this_or_next|eq,"$has_castle_key",1),
			(eq,"$robbery_in_progress",1),

			(try_for_agents, ":agent_no"),
				(agent_get_troop_id, ":troop_id", ":agent_no"),
					(try_begin),
						(is_between, ":troop_id", kings_begin, lords_end),
						(call_script, "script_change_player_relation_with_troop", ":troop_id", -5),
					  (else_try),
					    (is_between, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
						(call_script, "script_change_player_relation_with_troop", ":troop_id", -5),
						(troop_set_slot, ":troop_id", slot_troop_cur_center, -1),
					  (else_try),
						(is_between, ":troop_id", soldiers_begin, soldiers_end),	#hall guards are on player team by default for some reason
						(agent_set_team,":agent_no", 1),
					(try_end),
			(try_end),

			(call_script, "script_make_town_guards_and_hero_troops_turn_hostile"),
			(get_player_agent_no, ":player"),
			(agent_get_position, pos12, ":player"),
		    (call_script, "script_hit_alerts_guards_panicks_civilians", ":player", "itm_pistol_ammo"),
			(mission_disable_talk),
      ]),

	   #krag robbery failure, added this trigger
      (3, 0, ti_once,
      [
	    (neg|conversation_screen_is_active),
		(this_or_next|eq,"$has_prison_key",1),
		(this_or_next|eq,"$has_castle_key",1),
		(this_or_next|eq,"$robbery_in_progress",1),
        (this_or_next|eq, "$talk_context", tc_escape),
		(eq, "$talk_context", tc_prison_break),
		(main_hero_fallen),
      ],
      [
      (assign, "$capturer_party", "$g_encountered_party"), # set variable properly
	  (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
	  (finish_mission,0)
	  ]),

	  (0.5, 0, 0,	# krag robbery clear panicking agents
    [
      (this_or_next|eq,"$has_prison_key",1),
		(this_or_next|eq,"$has_castle_key",1),
		(this_or_next|eq,"$robbery_in_progress",1),
	  (this_or_next|eq, "$talk_context", tc_prison_break),
        (eq, "$talk_context", tc_escape),
    ],
    [
     (call_script, "script_clear_panicking_agents_near_passages", 150),
	 (entry_point_get_position, pos17, 0),#Keep this section is it's likely the passage will be blocked by the player
	  (try_for_agents, ":escaping_agent", pos17, 150),
		(agent_is_active,":escaping_agent"),
		(agent_is_alive,":escaping_agent"),
		(agent_slot_eq, ":escaping_agent", slot_agent_is_running_away, 1),
		(agent_fade_out, ":escaping_agent"),
		#(display_message, "@agent faded"),
	  (try_end),
    ]),
    ],
  ),


("back_alley_kill_local_merchant",mtf_battle_mode,-1,
    "You enter the back alley",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
    # ], tocan_ambience+tocan_common_triggers+tocan_battle_triggers+
     ], tocan_ambience+tocan_common_triggers+tocan_battle_triggers+tocan_autofire+tocan_flashlight+

    [
      common_inventory_not_available,
      (ti_tab_pressed, 0, 0, [(display_message,"str_cannot_leave_now",message_alert)], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      # (0, 0, ti_once, [],
       # [
         # (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
         # ]),

      (0, 0, ti_once, [
          (store_mission_timer_a,":cur_time"),
          (ge,":cur_time",1),
          (assign, ":merchant_hp", 0),
          (assign, ":player_hp", 0),
          (assign, ":merchant_hp", 0),
          (assign, ":merchant_agent", -1),
          (assign, ":player_agent", -1),
          (try_for_agents, ":agent_no"),
            (agent_get_troop_id, ":troop_id", ":agent_no"),
            (try_begin),
              (eq, ":troop_id", "trp_local_merchant"),
              (store_agent_hit_points, ":merchant_hp", ":agent_no"),
              (assign, ":merchant_agent", ":agent_no"),
            (else_try),
              (eq, ":troop_id", "trp_player"),
              (store_agent_hit_points, ":player_hp",":agent_no"),
              (assign, ":player_agent", ":agent_no"),
            (try_end),
          (try_end),
          (ge, ":player_agent", 0),
          (ge, ":merchant_agent", 0),
          (agent_is_alive, ":player_agent"),
          (agent_is_alive, ":merchant_agent"),
          (is_between, ":merchant_hp", 1, 30),
          (gt, ":player_hp", 50),
          (start_mission_conversation, "trp_local_merchant"),
          ], []),

      (1, 4, ti_once, [(assign, ":not_alive", 0),
                       (try_begin),
                         (call_script, "script_cf_troop_agent_is_alive", "trp_local_merchant"),
                       (else_try),
                         (assign, ":not_alive", 1),
                       (try_end),
                       (this_or_next|main_hero_fallen),
                       (eq, ":not_alive", 1)],
       [
           (try_begin),
             (main_hero_fallen),
             (call_script, "script_fail_quest", "qst_kill_local_merchant"),
           (else_try),
             (call_script, "script_change_player_relation_with_center", "$current_town", -4),
             (call_script, "script_succeed_quest", "qst_kill_local_merchant"),
           (try_end),
           (finish_mission),
           ]),
    ],
  ),

("back_alley_revolt",mtf_battle_mode,charge,
    "You lead your men to battle.",
    [(0,mtef_team_0|mtef_use_exact_number,af_override_horse|af_override_weapons|af_override_head,aif_start_alarmed,4,[itm_staff]),
     (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # ], tocan_ambience+tocan_common_triggers+tocan_battle_triggers+
     ], tocan_ambience+tocan_common_triggers+tocan_battle_triggers+tocan_autofire+tocan_flashlight+

    [
      common_inventory_not_available,

      common_battle_init_banner,

      (ti_tab_pressed, 0, 0, [],
       [(question_box,"str_do_you_want_to_retreat"),
        ]),
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (jump_to_menu, "mnu_collect_taxes_failed"),
        (finish_mission),]),

      (ti_tab_pressed, 0, 0, [(display_message,"str_cannot_leave_now",message_alert)], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      # (0, 0, ti_once, [],
       # [
         # (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
         # ]),

      (1, 4, ti_once, [(this_or_next|main_hero_fallen),(num_active_teams_le,1)],
       [
           (try_begin),
             (main_hero_fallen),
             (jump_to_menu, "mnu_collect_taxes_failed"),
           (else_try),
             (jump_to_menu, "mnu_collect_taxes_rebels_killed"),
           (try_end),
           (finish_mission),
           ]),
    ],
  ),

("lead_charge",mtf_battle_mode,charge,#mtf_synch_inventory, removed to have medikit disappearing, I dont know what it is good for
    "You lead your men to battle.",
    [
     (1,mtef_defenders|mtef_team_0,0,aif_start_alarmed,12,[]),
     (0,mtef_defenders|mtef_team_0,0,aif_start_alarmed,0,[]),
     (4,mtef_attackers|mtef_team_1,0,aif_start_alarmed,12,[]),
     (4,mtef_attackers|mtef_team_1,0,aif_start_alarmed,0,[]),
     ],
     # tocan_ambience+tocan_common_triggers+tocan_scene_maker+tocan_cover+tocan_battle_triggers+
     x_companion+tocan_ambience+tocan_common_triggers+tocan_battle_triggers+tocan_cover+tocan_autofire+tocan_flashlight+tocan_vehicles+

    [

	(ti_after_mission_start, 0, ti_once, [], [
		(assign, "$default_disguise_torso", 0),#use for now to keep save compatibility
		(assign, ":total_props", 0),
		# (try_for_prop_instances, ":instance"),

			# (prop_instance_get_scene_prop_kind,":prop_id", ":instance"),
			# (neq, ":prop_id", "spr_tocan_scene_maker"),
			# (neq, ":prop_id", "spr_player_chest"),
			# (val_add, ":total_props", 1),
		# (try_end),
		(scene_prop_get_num_instances, ":total_props", "spr_cover_enemy"),

		(assign, "$default_disguise_torso", ":total_props"),
		(assign, reg2, ":total_props"),
		#display_message, "@total_props : {reg2}"),

		(get_player_agent_no, "$g_player"),

        ]),

      (ti_on_agent_spawn, 1, 0, [], #ghoul/bandit random placement
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_id", ":agent_no"),
         #(neq, ":troop_id", "trp_player"),#for testing, should be more interesting if player is also random - krag
		 (assign, ":stop", 0),
		 (agent_get_team, ":agent_team", ":agent_no"),
		 (try_begin),
			(this_or_next|agent_is_ally, ":agent_no"),
			(eq, ":agent_team", "$g_player_team"),
			(eq, "$g_autocover", 0),
			(assign, ":stop", 1),
		 (try_end),
		 
	 (try_begin),
		 (eq, ":stop", 0),

		 (try_begin),
			(get_player_agent_no, "$g_player"),
			(gt, "$g_player", -1),
			(agent_get_position, pos21, "$g_player"),
		  (else_try),
			(init_position, pos21),
			(position_move_z, pos21, -6000),
		 (try_end),
		 (try_begin),
			 #(this_or_next|eq, ":troop_id", "trp_looter"),	#disable as can get into other parties then behaves weird
			 #(this_or_next|eq, ":troop_id", "trp_cannibal"),
             (this_or_next|eq, ":troop_id", "trp_the_suits"),
			 (this_or_next|eq, ":troop_id", "trp_infected_1"),
			 (this_or_next|eq, ":troop_id", "trp_infected_2"),
			 (this_or_next|eq, ":troop_id", "trp_infected_3"),
             (this_or_next|eq, ":troop_id", "trp_infected_4"),
             (this_or_next|eq, ":troop_id", "trp_infected_5"),
             (this_or_next|eq, ":troop_id", "trp_infected_6"),
			 (this_or_next|eq, ":troop_id", "trp_ghoul_scavenger"),
			 (eq, ":troop_id", "trp_ghoul"),
			 #(assign, ":stop", 0),
			 (assign, "$g_autocover_ai", 0),	#stop them taking cover
		 (try_end),
		 (try_begin),
			 # #(this_or_next|eq, ":troop_id", "trp_looter"),	#disable as can get into other parties then behaves weird
			 # #(this_or_next|eq, ":troop_id", "trp_cannibal"),
			 # (this_or_next|eq, ":troop_id", "trp_infected_1"),
			 # (this_or_next|eq, ":troop_id", "trp_infected_2"),
			 # (this_or_next|eq, ":troop_id", "trp_infected_3"),
			 # (this_or_next|eq, ":troop_id", "trp_ghoul_scavenger"),
			 # (eq, ":troop_id", "trp_ghoul"),
			 # #(assign, ":stop", 0),
			 # (assign, "$g_autocover_ai", 0),	#stop them taking cover
			 # (try_begin),


				# # (assign, "$default_disguise_torso", 0),#use for now to keep save compatibility
				# # (assign, ":total_props", 0),
				# #(assign, ":stop", 0),
				# #(get_player_agent_no, "$g_player"),
				# #(gt, "$g_player", -1),
				# #(agent_get_position, pos21, "$g_player"),
				# #(display_message, "@Ghoul trying to find prop"),
				# (try_for_prop_instances, ":instance"),# "spr_cover_enemy"),
					# (eq, ":stop", 0),
					# #(prop_instance_get_scene_prop_kind,":prop_id", ":instance"),
					# #(neq, ":prop_id", "spr_tocan_scene_maker"),
					# #(neq, ":prop_id", "spr_player_chest"),
					# #(val_add, ":total_props", 1),
					# (store_random_in_range, ":chance", 0, 20),
					# (eq, ":chance", 0),
					# (prop_instance_get_position, pos20, ":instance"),


					# (get_distance_between_positions_in_meters, ":dist", pos20, pos21),
					# (gt, ":dist", 60),
					# (position_move_x, pos20, 250),
					# (position_set_z_to_ground_level, pos20),
					# (agent_set_position, ":agent_no", pos20),
					# #(display_message, "@Ghoul flanking!"),
					# (assign, ":stop", 1),
				# (try_end),
				# (eq, ":stop", 1),
				# #(display_message, "@Ghoul found prop!"),
			  # (else_try),
				# (eq, ":stop", 0),
				# (agent_get_position, pos22, ":agent_no"),
				# (store_random_in_range, ":spread", -15000, 15000),
				# (position_move_x, pos22, ":spread"),
				# # (val_div, ":spread", 2),
				# # (try_begin),
					# # (lt, ":spread", 0),
					# # (val_mul, ":spread", -1),
				# # (try_end),
				# # (position_move_y, pos22, ":spread"),
				# (position_set_z_to_ground_level, pos22),
				# (position_get_distance_to_ground_level, ":height", pos22),
				# (ge,":height", 0),

				# (get_distance_between_positions_in_meters, ":dist", pos22, pos21),	#check not close to player, mostly for reinforcements
				# (gt, ":dist", 60),
				# (agent_set_position, ":agent_no", pos22),

				# #(assign, reg3, ":spread"),
				# #(display_message, "@Ghoul spread : {reg3}"),
			 # (try_end),
			# (else_try),
				#(this_or_next|is_between, ":troop_id", mercenary_troops_begin, mercenary_troops_end),	#spread bandit types too
				#(is_between, ":troop_id", bandits_begin, infested_end),
				#(neq, ":troop_id", "trp_player"),
				#(neg|is_between, ":troop_id", kings_begin, kingdom_ladies_end),	#put in the middle? or better to vary?
				#(neg|is_between, ":troop_id", companions_begin, companions_end),
				
				 # (assign, reg45, "$g_scene_max_x"),
				 # (assign, ":pos_dist", "$g_scene_max_x"),
				 # (display_message, "@g_scene_max_x {reg45}"),
				# # #(store_div, ":pos_x", "$g_scene_max_x", 2),
				 # (store_mul, ":neg_dist", "$g_scene_max_x", -1),
				# # (init_position, <position>),
				
				(agent_get_position, pos22, ":agent_no"),
				#(store_random_in_range, ":spread", -40000, 40000),
				(store_random_in_range, ":spread", 0, 40000),
				(store_random_in_range, ":mul", 1, 3),
				(try_begin),
					(eq,":mul", 1),
					(val_mul, ":spread", -1),
				(try_end),
				#(assign, reg45, ":spread"),
				#(display_message, "@spread1: {reg45}"),
				(position_move_x, pos22, ":spread", 0),
				(position_set_z_to_ground_level, pos22),
				(position_get_distance_to_ground_level, ":height", pos22),
				(try_begin),
					(lt,":height", 0),
					(agent_get_position, pos22, ":agent_no"),
					#(store_random_in_range, ":spread", -30000, 30000),
					(store_random_in_range, ":spread", 0, 30000),
					(try_begin),
						(eq,":mul", 1),
						(val_mul, ":spread", -1),
					(try_end),
					(position_move_x, pos22, ":spread"),
					(position_set_z_to_ground_level, pos22),
					(position_get_distance_to_ground_level, ":height", pos22),
					(try_begin),
						(lt,":height", 0),
						(agent_get_position, pos22, ":agent_no"),
						#(store_random_in_range, ":spread", -20000, 20000),
						(store_random_in_range, ":spread", 0, 20000),
						(try_begin),
							(eq,":mul", 1),
							(val_mul, ":spread", -1),
						(try_end),
						(position_move_x, pos22, ":spread"),
						(position_set_z_to_ground_level, pos22),
						(position_get_distance_to_ground_level, ":height", pos22),
						(try_begin),
							(lt,":height", 0),
							(agent_get_position, pos22, ":agent_no"),
							#(store_random_in_range, ":spread", -15000, 15000),
							(store_random_in_range, ":spread", 0, 15000),
							(try_begin),
								(eq,":mul", 1),
								(val_mul, ":spread", -1),
							(try_end),
							(position_move_x, pos22, ":spread"),
							(position_set_z_to_ground_level, pos22),
							(position_get_distance_to_ground_level, ":height", pos22),
							(try_begin),
								(lt,":height", 0),
								(agent_get_position, pos22, ":agent_no"),
								#(store_random_in_range, ":spread", -10000, 10000),
								(store_random_in_range, ":spread", 0, 10000),
								(try_begin),
									(eq,":mul", 1),
									(val_mul, ":spread", -1),
								(try_end),
								(position_move_x, pos22, ":spread"),
								(position_set_z_to_ground_level, pos22),
								(position_get_distance_to_ground_level, ":height", pos22),
							(try_end),
						(try_end),
					(try_end),
				(try_end),
				
				#(assign, reg45, ":spread"),
				#(display_message, "@spread2: {reg45}"),
				(ge,":height", 0),
				
				(get_distance_between_positions_in_meters, ":dist", pos22, pos21),	#check not close to player, mostly for reinforcements
				(this_or_next|eq, ":agent_team", "$g_player_team"),
				(this_or_next|agent_is_ally, ":agent_no"),
				(gt, ":dist", 60),
				(agent_set_position, ":agent_no", pos22),
		 (try_end),
	 (try_end),
		 
	 (try_begin),
		(eq, "$freelancer_state", 1),	#move closer if forced into one-sided battles while enlisted
		(ge, "$g_battle_advantage", 10),
		
		(agent_get_position, pos22, ":agent_no"),
		(position_move_y, pos22, 5000, 0),
		(position_set_z_to_ground_level, pos22),
		(position_get_distance_to_ground_level, ":height", pos22),
		
		(ge,":height", 0),
		(agent_set_position, ":agent_no", pos22),
	 (try_end),
         ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (neq,":agent_no","$g_player_x_agent_no"),
         # (neq,":agent_no","$g_fake_agent"),

         (agent_get_troop_id, ":troop_id", ":agent_no"),
         (neg|troop_slot_eq, ":troop_id", slot_troop_is_animal, 1),
         (neq, ":troop_id", "trp_dog_companion"),
         (neq, ":troop_id", "trp_bot_companion"),
         (neq, ":troop_id", "trp_car_gunner"),
         (neq, ":troop_id", "trp_chopper_pilot"),
         (neq, ":troop_id", "trp_bus_gunner"),

         (call_script, "script_agent_reassign_team", ":agent_no"),

         (assign, ":initial_courage_score", 5000),

         (store_character_level, ":troop_level", ":troop_id"),
         (val_mul, ":troop_level", 35),
         (val_add, ":initial_courage_score", ":troop_level"), #average : 20 * 35 = 700

         (store_random_in_range, ":randomized_addition_courage", 0, 3000), #average : 1500
         (val_add, ":initial_courage_score", ":randomized_addition_courage"),

         (agent_get_party_id, ":agent_party", ":agent_no"),
         (party_get_morale, ":cur_morale", ":agent_party"),

         (store_sub, ":morale_effect_on_courage", ":cur_morale", 70),
         (val_mul, ":morale_effect_on_courage", 30), #this can effect morale with -2100..900
         (val_add, ":initial_courage_score", ":morale_effect_on_courage"),

         #average = 5000 + 700 + 1500 = 7200; min : 5700, max : 8700
         #morale effect = min : -2100(party morale is 0), average : 0(party morale is 70), max : 900(party morale is 100)
         #min starting : 3600, max starting  : 9600, average starting : 7200
         (agent_set_slot, ":agent_no", slot_agent_courage_score, ":initial_courage_score"),
         ]),

      common_battle_init_banner,

      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        (store_trigger_param_3, ":is_wounded"),

        (try_begin),
          (ge, ":dead_agent_no", 0),
          (neg|agent_is_ally, ":dead_agent_no"),
          (agent_is_human, ":dead_agent_no"),
          (agent_get_troop_id, ":dead_agent_troop_id", ":dead_agent_no"),
##          (str_store_troop_name, s6, ":dead_agent_troop_id"),
##          (assign, reg0, ":dead_agent_no"),
##          (assign, reg1, ":killer_agent_no"),
##          (assign, reg2, ":is_wounded"),
##          (agent_get_team, reg3, ":dead_agent_no"),
          #(display_message, "@{!}dead agent no : {reg0} ; killer agent no : {reg1} ; is_wounded : {reg2} ; dead agent team : {reg3} ; {s6} is added"),
          (party_add_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), #addition_to_p_total_enemy_casualties
          (eq, ":is_wounded", 1),
          (party_wound_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1),
        (try_end),

        (call_script, "script_apply_death_effect_on_courage_scores", ":dead_agent_no", ":killer_agent_no"),
       ]),

      common_battle_tab_press,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (try_begin),
          (store_mission_timer_a, ":elapsed_time"),
          (gt, ":elapsed_time", 20),
          (str_store_string, s5, "str_retreat"),
          (call_script, "script_simulate_retreat", 10, 20, 1),
        (try_end),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (ti_before_mission_start, 0, 0, [],
       [
         (team_set_relation, 0, 2, 1),
         (team_set_relation, 1, 3, 1),
         (call_script, "script_place_player_banner_near_inventory_bms"),

         (party_clear, "p_routed_enemies"),

         (assign, "$g_latest_order_1", 1),
         (assign, "$g_latest_order_2", 1),
         (assign, "$g_latest_order_3", 1),
         (assign, "$g_latest_order_4", 1),
         ]),


      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           (assign,"$defender_reinforcement_stage",0),
                           (assign,"$attacker_reinforcement_stage",0),
                           (call_script, "script_place_player_banner_near_inventory"),
                           # (call_script, "script_combat_music_set_situation_with_culture"),
                           (assign, "$g_defender_reinforcement_limit", 2),
                           ##diplomacy begin
                           (call_script, "script_init_death_cam"),
                           # (assign, "$g_dplmc_charge_when_dead", 0),
                           ##diplomacy end
                           ## HOLD ON START
                           (get_player_agent_no, "$g_player"),
                           (agent_get_team, "$g_player_team", "$g_player"),
                           (set_show_messages, 0),
						   (try_begin),
								(eq, "$g_autocover", 1),
								(team_give_order, "$g_player_team", grc_everyone, mordr_stand_ground),	#switch to this now spread across map on spawn
							  (else_try),
								(team_give_order, "$g_player_team", grc_everyone, mordr_hold),
								(team_give_order, "$g_player_team", grc_everyone, mordr_spread_out),
								#(team_give_order, "$g_player_team", grc_everyone, mordr_spread_out),
						   (try_end),
                           #

                           # (team_give_order, "$g_player_team", grc_everyone, mordr_spread_out),

                           # (team_give_order, "$g_player_team", grc_everyone, mordr_advance),
                           # (team_give_order, "$g_player_team", grc_everyone, mordr_advance),
                           # (team_give_order, "$g_player_team", grc_cavalry, mordr_fall_back),
                           # (team_give_order, "$g_player_team", grc_cavalry, mordr_fall_back),
                           (set_show_messages, 1),
                           ## END HOLD ON START
                           ]),

      (4, 0, ti_once, [],
        [
          (try_begin),
              (ge, "$g_special_companion", 1),
              (assign, "$x_npc_order", -1),
              # (get_player_agent_no, "$g_player"),
              (agent_clear_scripted_mode, "$g_player_x_agent_no"),
              # (agent_get_team, ":player_team", "$g_player"),
              #(agent_add_relation_with_agent, "$g_player", "$g_player_x_agent_no", 1),
              (set_show_messages, 0),
              (team_give_order, "$g_player_team", grc_special, mordr_follow),
              (set_show_messages, 1),
          (try_end),
      ]),

      # common_music_situation_update,
      common_battle_check_friendly_kills,

      (1, 0, 5, [

      #new (25.11.09) starts (sdsd = TODO : make a similar code to also helping ally encounters)
      #count all total (not dead) enemy soldiers (in battle area + not currently placed in battle area)
      (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
      (assign, ":total_enemy_soldiers", reg0),

      #decrease number of agents already in battle area to find all number of reinforcement enemies
      (assign, ":enemy_soldiers_in_battle_area", 0),
      (try_for_agents,":cur_agent"),
        (agent_is_human, ":cur_agent"),
        (agent_get_party_id, ":agent_party", ":cur_agent"),
        (try_begin),
          (neq, ":agent_party", "p_main_party"),
          (neg|agent_is_ally, ":cur_agent"),
          (val_add, ":enemy_soldiers_in_battle_area", 1),
        (try_end),
      (try_end),
      (store_sub, ":total_enemy_reinforcements", ":total_enemy_soldiers", ":enemy_soldiers_in_battle_area"),

      (try_begin),
        (lt, ":total_enemy_reinforcements", 15),
        (ge, "$defender_reinforcement_stage", 2),
        (eq, "$defender_reinforcement_limit_increased", 0),
        (val_add, "$g_defender_reinforcement_limit", 1),
        (assign, "$defender_reinforcement_limit_increased", 1),
      (try_end),
      #new (25.11.09) ends






      (lt,"$defender_reinforcement_stage","$g_defender_reinforcement_limit"),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_defenders", 0),
                 (lt,":num_defenders",6)],
           [(add_reinforcements_to_entry,0,7),(assign, "$defender_reinforcement_limit_increased", 0),(val_add,"$defender_reinforcement_stage",1)]),

      (1, 0, 5, [(lt,"$attacker_reinforcement_stage",2),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_attackers", 1),
                 (lt,":num_attackers",6)],
           [(add_reinforcements_to_entry,3,7),(val_add,"$attacker_reinforcement_stage",1)]),

      common_battle_check_victory_condition,
      common_battle_victory_display,

      (1, 4,
      ##diplomacy begin
      0,
      ##diplomacy end
      [(main_hero_fallen)],
          [
              ##diplomacy begin
              (try_begin),
                (call_script, "script_cf_dplmc_battle_continuation"),
              (else_try),
                ##diplomacy end
                (assign, "$pin_player_fallen", 1),
                (str_store_string, s5, "str_retreat"),
                (call_script, "script_simulate_retreat", 10, 20, 1),
                (assign, "$g_battle_result", -1),
                (set_mission_result,-1),
                (call_script, "script_count_mission_casualties_from_agents"),
                (finish_mission,0),
                ##diplomacy begin
              (try_end),
              ##diplomacy end
            ]),

      common_battle_inventory,


      #AI Triggers
      (0, 0, ti_once, [
          (store_mission_timer_a,":mission_time"),(ge,":mission_time",2),
          ],
       [(call_script, "script_select_battle_tactic"),
        (call_script, "script_battle_tactic_init"),
        #(call_script, "script_battle_calculate_initial_powers"), #deciding run away method changed and that line is erased
        ]),

      (3, 0, 0, [
          (call_script, "script_apply_effect_of_other_people_on_courage_scores"),
              ], []), #calculating and applying effect of people on others courage scores

      (3, 0, 0, [
          (store_mission_timer_a,":mission_time"),
          (try_for_agents, ":agent_no"),
            (agent_is_human, ":agent_no"),
            (agent_is_alive, ":agent_no"),
            # (store_mission_timer_a,":mission_time"),
            (ge,":mission_time",3),
            (agent_get_team, ":agent_team", ":agent_no"),
            (neq, ":agent_team", 5), #tocan test

            (agent_get_troop_id, ":troop_id", ":agent_no"),
            (neq, ":troop_id", "trp_dog_companion"),
            (neq, ":troop_id", "trp_bot_companion"),
            (neq, ":troop_id", "trp_car_gunner"),
            (neq, ":troop_id", "trp_chopper_pilot"),
            # (neq, ":troop_id", "trp_havoc_pilot"),
            (neq, ":troop_id", "trp_bus_gunner"),
            (troop_get_type,":troop_type",":troop_id"),
            (le, ":troop_type", 1),

            (call_script, "script_decide_run_away_or_not", ":agent_no", ":mission_time"),
          (try_end),
              ], []), #controlling courage score and if needed deciding to run away for each agent

      (5, 0, 0, [
          (store_mission_timer_a,":mission_time"),

          (ge,":mission_time",3),

          (call_script, "script_battle_tactic_apply"),
          ], []), #applying battle tactic

      # common_battle_order_panel,
      # common_battle_order_panel_tick,

    ]
    ##diplomacy begin
   + dplmc_battle_mode_triggers #+ dplmc_horse_cull  #SB : horse cull
   + battle_panel_triggers + extended_battle_menu,
    ##diplomacy end
  ),



  (
    "village_attack_bandits",mtf_battle_mode,charge,#mtf_synch_inventory, removed to have medikit disappearing, I dont know what it is good for
    "You lead your men to battle.",
    [
     (3,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     (1,mtef_team_0|mtef_use_exact_number,0,aif_start_alarmed, 7,[]),
     (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
     # ], tocan_ambience+tocan_common_triggers+tocan_battle_triggers+
     ], x_companion+tocan_ambience+tocan_common_triggers+tocan_battle_triggers+tocan_autofire+tocan_flashlight+
    [
      common_battle_tab_press,
      common_battle_init_banner,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 10, 20, 1),
        (assign, "$g_battle_result", -1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (0, 0, ti_once, [], [(assign, "$g_battle_won", 0),
                           (assign, "$defender_reinforcement_stage", 0),
                           (assign, "$attacker_reinforcement_stage", 0),
                           (try_begin),
                             (eq, "$g_mt_mode", vba_after_training),
                             (add_reinforcements_to_entry, 1, 6),
                           (else_try),
                             (add_reinforcements_to_entry, 1, 29),
                           (try_end),
                           #SB : deathcam
                           (call_script, "script_init_death_cam"),
                           # (call_script, "script_combat_music_set_situation_with_culture"),
                           ## HOLD ON START
                           (get_player_agent_no, "$g_player"),
                           (agent_get_team, ":player_team", "$g_player"),
                           (set_show_messages, 0),
                           (team_give_order, ":player_team", grc_everyone, mordr_hold),
                           (set_show_messages, 1),
                           ## END HOLD ON START
                           ]),

      (4, 0, ti_once, [],
        [
          (try_begin),
              (ge, "$g_special_companion", 1),
              (assign, "$x_npc_order", -1),
              # (get_player_agent_no, "$g_player"),
              (agent_clear_scripted_mode, "$g_player_x_agent_no"),
              # (agent_get_team, ":player_team", "$g_player"),
              #(agent_add_relation_with_agent, "$g_player", "$g_player_x_agent_no", 1),
              (set_show_messages, 0),
              (team_give_order, "$g_player_team", grc_special, mordr_follow),
              (set_show_messages, 1),
          (try_end),
      ]),

      # common_music_situation_update,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,

      (1, 4,
      ##diplomacy begin
      0,
      ##diplomacy end
      [(main_hero_fallen)],
          [
              ##diplomacy begin
              (try_begin),
                (call_script, "script_cf_dplmc_battle_continuation"),
              (else_try),
                ##diplomacy end
                (assign, "$pin_player_fallen", 1),
                (str_store_string, s5, "str_retreat"),
                (call_script, "script_simulate_retreat", 10, 20, 1),
                (assign, "$g_battle_result", -1),
                (set_mission_result, -1),
                (call_script, "script_count_mission_casualties_from_agents"),
                (finish_mission, 0),
                ##diplomacy begin
              (try_end),
              ##diplomacy end
              ]),

      common_battle_inventory,
      # common_battle_order_panel,
      # common_battle_order_panel_tick,

    ]
    ##diplomacy begin
    + dplmc_battle_mode_triggers #+ dplmc_horse_cull  #SB : horse cull
    ##diplomacy end
    + battle_panel_triggers,

  ),



  (
    "village_raid",mtf_battle_mode,charge,#mtf_synch_inventory, removed to have medikit disappearing, I dont know what it is good for
    "You lead your men to battle.",
    [
     (3,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,12,[]),
     (3,mtef_defenders|mtef_team_0,0,aif_start_alarmed,0,[]),
     (1,mtef_attackers|mtef_team_1,0,aif_start_alarmed,12,[]),
     (1,mtef_attackers|mtef_team_1,0,aif_start_alarmed,0,[]),
     # ], tocan_ambience+tocan_common_triggers+tocan_battle_triggers+
     ], x_companion+tocan_ambience+tocan_common_triggers+tocan_battle_triggers+tocan_autofire+tocan_flashlight+
    [
      common_battle_tab_press,
      common_battle_init_banner,
	  
	(ti_on_agent_spawn, 1, 0, [	#villager random placement - krag
		(is_between, "$g_encountered_party", villages_begin,villages_end), #only for villagers, not interupting lords
	], 
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_id", ":agent_no"),
		 (this_or_next|eq, ":troop_id", "trp_farmer"),	#only these 2 are used for now
		 (eq, ":troop_id", "trp_peasant_woman"),
		 (assign, ":stop", 0),
		 (agent_get_team, ":agent_team", ":agent_no"),
		 (try_begin),
			(this_or_next|agent_is_ally, ":agent_no"),
			(eq, ":agent_team", "$g_player_team"),
			(assign, ":stop", 1),
		 (try_end),
		 (eq, ":stop", 0),
		 
		 (store_random_in_range, ":rand", 0, 3),
		 (le, ":rand", 1),	#keep a decent chunk in main group

		 (try_begin),
				#(agent_get_position, pos22, ":agent_no"),
				(store_random_in_range, ":spread", 32, 40),
				(entry_point_get_position, pos22, ":spread"),
				(store_random_in_range, ":rotation", 0, 360),
				(position_rotate_z, pos22, ":rotation"),
				(store_random_in_range, ":move", 5, 50), # make not all spawn in same exact pos
				(position_move_y, pos22, ":move"),
				(position_set_z_to_ground_level, pos22),
				(position_get_distance_to_ground_level, ":height", pos22),
				(position_get_distance_to_terrain, ":terrain_height", pos22),
				(eq, ":terrain_height", ":height"),	#make sure don't spawn in/on props
				
				#(assign, reg45, ":spread"),
				#(display_message, "@spread: {reg45}"),
				(ge,":height", 0),#not over edge of map somehow
				
				 (try_begin),
					(get_player_agent_no, "$g_player"),
					(gt, "$g_player", -1),
					(agent_get_position, pos21, "$g_player"),
				  (else_try),
					#(init_position, pos21),
					#(position_move_z, pos21, -6000),
					(entry_point_get_position, pos21, 1),
				 (try_end),
				 
				(get_distance_between_positions_in_meters, ":dist", pos22, pos21),	#check not close to player, mostly for reinforcements
				#(this_or_next|eq, ":agent_team", "$g_player_team"),
				#(this_or_next|agent_is_ally, ":agent_no"),
				(gt, ":dist", 30),
				(agent_set_position, ":agent_no", pos22),
				#(assign, reg45, ":spread"),
				#(display_message, "@spread: {reg45}"),
		 (try_end),
         ]),


      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 10, 20, 1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (4, 0, ti_once, [],
        [
          (try_begin),
              (ge, "$g_special_companion", 1),
              (assign, "$x_npc_order", -1),
              # (get_player_agent_no, "$g_player"),
              (agent_clear_scripted_mode, "$g_player_x_agent_no"),
              # (agent_get_team, ":player_team", "$g_player"),
              #(agent_add_relation_with_agent, "$g_player", "$g_player_x_agent_no", 1),
              (set_show_messages, 0),
              (team_give_order, "$g_player_team", grc_special, mordr_follow),
              (set_show_messages, 1),
          (try_end),
      ]),

      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           (assign,"$defender_reinforcement_stage",0),
                           (assign,"$attacker_reinforcement_stage",0),
                           #SB : deathcam
                           (call_script, "script_init_death_cam"),
                           # (call_script, "script_combat_music_set_situation_with_culture"),
                           ## HOLD ON START
                           (get_player_agent_no, "$g_player"),
                           (agent_get_team, ":player_team", "$g_player"),
                           (set_show_messages, 0),
                           (team_give_order, ":player_team", grc_everyone, mordr_hold),
                           #(set_show_messages, 1),
                           ## END HOLD ON START
						   
						   (neq, ":player_team", 0),
						   (entry_point_get_position, pos1, 3),
						   (team_give_order, 0, grc_archers, mordr_hold),	#enemy ranged don't be suicidal
						   (team_give_order, 0, grc_archers, mordr_spread_out),
						   (team_give_order, 0, grc_archers, mordr_spread_out),
						   
						   (set_show_messages, 1),
                           ]),

      (45, 0, ti_once, [], [
                           (get_player_agent_no, "$g_player"),
                           (agent_get_team, ":player_team", "$g_player"),
                           #(set_show_messages, 0),
						   
						   (neq, ":player_team", 0),
						   (team_give_order, 0, grc_archers, mordr_stand_ground),	#enemy ranged stand ground
						   
						   #(set_show_messages, 1),
						   #(display_message, "@mordr_stand_ground"),
                           ]),

      (120, 0, ti_once, [], [
                           (get_player_agent_no, "$g_player"),
                           (agent_get_team, ":player_team", "$g_player"),
                           #(set_show_messages, 0),
						   
						   (neq, ":player_team", 0),
						   (team_give_order, 0, grc_archers, mordr_charge),	#enemy ranged charge as probably out of ammo
						   
						   #(set_show_messages, 1),
						   #(display_message, "@mordr_charge"),
                           ]),

      # common_music_situation_update,
      common_battle_check_friendly_kills,

      (1, 0, 5, [(lt,"$defender_reinforcement_stage",2),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_defenders", 0),
                 (lt,":num_defenders",6)],
           [(add_reinforcements_to_entry,0,6),(val_add,"$defender_reinforcement_stage",1)]),
      (1, 0, 5, [(lt,"$attacker_reinforcement_stage",2),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_attackers", 1),
                 (lt,":num_attackers",6)],
           [(add_reinforcements_to_entry,3,6),(val_add,"$attacker_reinforcement_stage",1)]),

      #SB : battle continuation
      (1, 60, ti_once,
       [
         (store_mission_timer_a,reg(1)),
         (ge,reg(1),10),
         (all_enemies_defeated, 5),
         ##diplomacy begin
         (this_or_next|eq, "$g_dplmc_battle_continuation", 0),
         (neg|main_hero_fallen),
         ##diplomacy end
         (set_mission_result,1),
         (display_message,"str_msg_battle_won",message_positive),
         (assign,"$g_battle_won",1),
         (assign, "$g_battle_result", 1),
         (try_begin),
           (eq, "$g_village_raid_evil", 0),
           (call_script, "script_play_victorious_sound"),
         (else_try),
           (play_track, "track_victorious_evil", 1),
         (try_end),
         ],
       [
         (call_script, "script_count_mission_casualties_from_agents"),
         (finish_mission, 1),
         ]),

      common_battle_victory_display,

      (1, 4,
      ##diplomacy begin
      0,
      ##diplomacy end
      [(main_hero_fallen)],
          [
              ##diplomacy begin
              (try_begin),
                (call_script, "script_cf_dplmc_battle_continuation"),
              (else_try),
                ##diplomacy end
                (assign, "$pin_player_fallen", 1),
                (str_store_string, s5, "str_retreat"),
                (call_script, "script_simulate_retreat", 10, 20, 1),
                (assign, "$g_battle_result", -1),
                (set_mission_result,-1),
                (call_script, "script_count_mission_casualties_from_agents"),
                (finish_mission,0),
                ##diplomacy begin
              (try_end),
              ##diplomacy end
          ]),

   #SB : handle nervous man as fugitive quest
   (ti_on_agent_killed_or_wounded, 0, 0, [(check_quest_active, "qst_hunt_down_fugitive"), #not ti_once
                       (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
                       (neg|check_quest_failed, "qst_hunt_down_fugitive"),
                       (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
                       (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_current_state, 1),],
   [
    (store_trigger_param_1, ":dead_agent_no"),
    # (store_trigger_param_2, ":killer_agent"),
    (agent_is_human, ":dead_agent_no"),
    (store_trigger_param_3, ":is_wounded"),
    # (get_player_agent_no, "$g_player"),
    (agent_get_troop_id, ":corpse", ":dead_agent_no"),
    (try_begin),
      (eq, ":corpse", "trp_fugitive"),
      # (party_remove_members, "$current_town", "trp_fugitive", 1),
      # (eq, ":killer_agent", "$g_player"), #bodyguards, villagers also applicable
      (try_begin),
        (eq, ":is_wounded", 1),#wounded, add as prisoner since normally we don't access casualties in this mission template
        # (display_message, "@You leave the fugitive to villager's justice.", message_positive),
        (party_force_add_prisoners, "p_main_party", "trp_fugitive", 1),
        (quest_set_slot, "qst_hunt_down_fugitive", slot_quest_current_state, 2), #enter phase 2 of bringing him back
      (try_end),
      (call_script, "script_succeed_quest", "qst_hunt_down_fugitive"),
      # (call_script, "script_deactivate_tavern_attackers"),
    # (else_try), #villagers?
      # (call_script, "script_change_player_relation_with_center", "$current_town", -1),
    (try_end),
    ]),

      common_battle_inventory,
      # common_battle_order_panel,
      # common_battle_order_panel_tick,


    ]
    ##diplomacy begin
    + dplmc_battle_mode_triggers #+ dplmc_horse_cull  #SB : horse cull
    ##diplomacy end
    + battle_panel_triggers,
  ),


("besiege_inner_battle_castle",mtf_battle_mode,-1,
    "You attack the walls of the fort...",
    [
     (0, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (6, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (7, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (16, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (17, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (18, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (19, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (20, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # ], tocan_ambience+tocan_common_triggers+tocan_battle_triggers+
     ], tocan_ambience+tocan_common_triggers+tocan_battle_triggers+tocan_autofire+tocan_flashlight+
    [
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      common_battle_tab_press,
      common_battle_init_banner,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 5, 20, 0),
        (assign, "$g_battle_result", -1),
        (set_mission_result,-1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),
        ]),

      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           ##diplomacy begin
                           (call_script, "script_init_death_cam"),
                           # (assign, "$g_dplmc_charge_when_dead", 1),
                           ##diplomacy end
                           # (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
                            ## HOLD ON START
                           (get_player_agent_no, "$g_player"),
                           (agent_get_team, ":player_team", "$g_player"),
                           (set_show_messages, 0),
                           (team_give_order, ":player_team", grc_everyone, mordr_hold),
                           (set_show_messages, 1),
                           ## END HOLD ON START
                           ]),

      #AI Tiggers
      (0, 0, ti_once, [
          (assign, "$defender_team", 0),
          (assign, "$attacker_team", 1),
          (assign, "$defender_team_2", 2),
          (assign, "$attacker_team_2", 3),
          ], []),

      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,

      (1, 4,
      ##diplomacy begin
      0,
      ##diplomacy end
      [(main_hero_fallen)],
          [
            ##diplomacy begin
            (try_begin),
              (call_script, "script_cf_dplmc_battle_continuation"),
            (else_try),
              (assign, "$pin_player_fallen", 1),
              (str_store_string, s5, "str_retreat"),
              (call_script, "script_simulate_retreat", 5, 20, 0),
              (assign, "$g_battle_result", -1),
              (set_mission_result,-1),
              (call_script, "script_count_mission_casualties_from_agents"),
              (finish_mission,0),
            (try_end),
            ##diplomacy end
              ]),

      # common_battle_order_panel,
      # common_battle_order_panel_tick,
      common_battle_inventory,
    ]
    ##diplomacy begin
    + dplmc_battle_mode_triggers
    ##diplomacy end
    + battle_panel_triggers,
  ),

("besiege_inner_battle_town_center",mtf_battle_mode,-1,
    "You attack the walls of the fort...",
    [
     (0, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,4,[]),
     (2, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (23, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (24, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (25, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (26, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (27, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (28, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     ], tocan_ambience+tocan_common_triggers+tocan_battle_triggers+tocan_autofire+tocan_flashlight+
     # ], tocan_ambience+tocan_common_triggers+tocan_battle_triggers+
    [
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      common_battle_tab_press,
      common_battle_init_banner,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 5, 20, 0),
        (assign, "$g_battle_result", -1),
        (set_mission_result,-1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),
        ]),

      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           ##diplomacy begin
                           (call_script, "script_init_death_cam"),
                           # (assign, "$g_dplmc_charge_when_dead", 1),
                           ##diplomacy end
                           # (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
                           ## HOLD ON START
                           (get_player_agent_no, "$g_player"),
                           (agent_get_team, ":player_team", "$g_player"),
                           (set_show_messages, 0),
                           (team_give_order, ":player_team", grc_everyone, mordr_hold),
                           (set_show_messages, 1),
                           ## END HOLD ON START
                           ]),

      #AI Tiggers
      (0, 0, ti_once, [
          (assign, "$defender_team", 0),
          (assign, "$attacker_team", 1),
          (assign, "$defender_team_2", 2),
          (assign, "$attacker_team_2", 3),
          ], []),

      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,

      (1, 4,
      ##diplomacy begin
      0,
      ##diplomacy end
      [(main_hero_fallen)],
          [
          ##diplomacy begin
          (try_begin),
            (call_script, "script_cf_dplmc_battle_continuation"),
          (else_try),
            ##diplomacy end
            (assign, "$pin_player_fallen", 1),
            (str_store_string, s5, "str_retreat"),
            (call_script, "script_simulate_retreat", 5, 20, 0),
            (assign, "$g_battle_result", -1),
            (set_mission_result,-1),
            (call_script, "script_count_mission_casualties_from_agents"),
            (finish_mission,0),
          ##diplomacy begin
          (try_end),
          ##diplomacy end

              ]),

      # common_battle_order_panel,
      # common_battle_order_panel_tick,
      common_battle_inventory,
    ]
    + dplmc_battle_mode_triggers + battle_panel_triggers,
  ),

  (
    "castle_visit",0,-1,
    "Castle visit",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons|af_override_head,0,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise), 
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise), #for doors
     (5,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (6,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (7,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (8,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(9,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(10,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(11,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (12,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(13,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(14,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(15,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (16,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(17,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(18,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(19,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (20,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(21,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(22,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(23,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (24,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(25,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(26,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(27,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (28,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(29,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(30,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(31,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (32,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(33,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(34,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(35,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (36,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(37,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(38,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(39,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     # Party members
     (40,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (41,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (42,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (43,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (44,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (45,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (46,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     ],
    [    
      (ti_on_agent_spawn, 0, 0, [],
      [
        (store_trigger_param_1, ":agent_no"),
        (call_script, "script_init_town_agent", ":agent_no"),
        (get_player_agent_no, ":player_agent"),
        (try_begin),
          (neq, ":player_agent", ":agent_no"),
          (agent_set_team, ":agent_no", 7),
        (try_end),
        
        (try_begin),
          (this_or_next|eq, "$talk_context", tc_escape),
          (eq, "$talk_context", tc_prison_break),
          (agent_get_troop_id, ":troop_no", ":agent_no"),
          (troop_get_slot, ":will_join_prison_break", ":troop_no", slot_troop_will_join_prison_break),
          (eq, ":will_join_prison_break", 1),
          (agent_set_team, ":agent_no", 0),
          (agent_ai_set_aggressiveness, ":agent_no", 5),
          (troop_set_slot, ":troop_no", slot_troop_will_join_prison_break, 0),

          (try_begin),
            (troop_slot_eq, ":troop_no", slot_troop_mission_participation, mp_prison_break_stand_back),
            (agent_get_position, pos1, ":agent_no"),                        
            (agent_set_scripted_destination, ":agent_no", pos1),
          (try_end),
        (try_end),
      ]),
      
      (ti_on_agent_killed_or_wounded, 0, 0, [],
      [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        #(store_trigger_param_3, ":is_wounded"),
        
        (agent_get_troop_id, ":dead_agent_troop_no", ":dead_agent_no"),
        (agent_get_troop_id, ":killer_agent_troop_no", ":killer_agent_no"),
                
        (try_begin), 
          (this_or_next|eq, ":dead_agent_troop_no", "trp_f1_guard"),
          (this_or_next|eq, ":dead_agent_troop_no", "trp_f2_guard"),
          (this_or_next|eq, ":dead_agent_troop_no", "trp_f3_guard"),
          (this_or_next|eq, ":dead_agent_troop_no", "trp_f4_guard"),
          (this_or_next|eq, ":dead_agent_troop_no", "trp_f5_guard"),
          (this_or_next|eq, ":dead_agent_troop_no", "trp_irregular_guard"),
          (eq, ":dead_agent_troop_no", "trp_f6_guard"),
          
          (eq, ":killer_agent_troop_no", "trp_player"),
          
          (display_message, "@You got keys of dungeon."),
        (try_end),
      ]),     

      #JAILBREAK TRIGGERS 
      #Civilians get out of the way
      (1, 0, 0,
      [
        (this_or_next|eq, "$talk_context", tc_prison_break),
        (eq, "$talk_context", tc_escape),
      ],
      [
        #(agent_get_team, ":prisoner_agent", 0),
        (call_script, "script_neutral_behavior_in_fight"),
        (mission_disable_talk),
      ]),
      
      #The game begins with the town alerted
      (1, 0, ti_once,
      [
        #If I set this to 1, 0, ti_once, then the prisoner spawns twice
        (eq, "$talk_context", tc_escape),
      ],
      [
        (get_player_agent_no, ":player_agent"),
        (assign, reg6, ":player_agent"),
        (call_script, "script_activate_town_guard"),		
        
        (get_player_agent_no, ":player_agent"),
        (agent_get_position, pos4, ":player_agent"),
        
        (try_for_range, ":prisoner", active_npcs_begin, kingdom_ladies_end),
          (troop_slot_ge, ":prisoner", slot_troop_mission_participation, 1),
          
          (str_store_troop_name, s4, ":prisoner"),
          (display_message, "str_s4_joins_prison_break"),
          
          (store_current_scene, ":cur_scene"), #this might be a better option?
          (modify_visitors_at_site, ":cur_scene"),
          #<entry_no>,<troop_id>,<number_of_troops>, <team_no>, <group_no>), 
          #team no and group no are used in multiplayer mode only. default team in entry is used in single player mode
          (store_current_scene, ":cur_scene"),
          (modify_visitors_at_site, ":cur_scene"),
          (assign, ":nearest_entry_no", 24),
          (add_visitors_to_current_scene, ":nearest_entry_no", ":prisoner", 1, 0, 0),
          (troop_set_slot, ":prisoner", slot_troop_will_join_prison_break, 1),          
        (try_end),
	  ]),

      (ti_tab_pressed, 0, 0,
      [
        (try_begin),
          (this_or_next|eq, "$talk_context", tc_escape),
          (eq, "$talk_context", tc_prison_break),
          (display_message, "str_cannot_leave_now"),
        (else_try),
          (this_or_next|eq, "$g_mt_mode", tcm_default),
          (eq, "$g_mt_mode", tcm_disguised),
          (set_trigger_result, 1),
          (mission_enable_talk),
        (else_try),
          (display_message, "str_cannot_leave_now"),
        (try_end),
      ], 
      []),
            
      (ti_before_mission_start, 0, 0, [], 
      [
        (call_script, "script_change_banners_and_chest"),
        #(call_script, "script_remove_siege_objects"),
      ]),
      
      (3, 0, 0, 
      [     
        (main_hero_fallen, 0),
      ],	  
      [
        (try_begin),
          (this_or_next|eq, "$talk_context", tc_prison_break),
          (eq, "$talk_context", tc_escape),
       
          (call_script, "script_deduct_casualties_from_garrison"),
	      (jump_to_menu,"mnu_captivity_start_castle_defeat"), 
	 
	      (assign, ":end_cond", kingdom_ladies_end),
          (try_for_range, ":prisoner", active_npcs_begin, ":end_cond"),
  	        (troop_set_slot, ":prisoner", slot_troop_mission_participation, 0), #new	  
  	      (try_end),  
	 
	      (mission_enable_talk),
	      (finish_mission, 0),
	    (else_try),  
	      (mission_enable_talk),
	      (finish_mission, 0),
	      (set_trigger_result, 1),
        (try_end),	 	 
      ]),
      
      (3, 0, 0, 
      [
        (eq, "$talk_context", tc_escape),
        (neg|main_hero_fallen,0),
        (store_mission_timer_a, ":time"),
        (ge, ":time", 10),      
        (all_enemies_defeated), #1 is default enemy team for in-town battles
      ],
      [
        (call_script, "script_deduct_casualties_from_garrison"),
        (try_for_agents, ":agent"),
          (agent_get_troop_id, ":troop", ":agent"),
          (troop_slot_ge, ":troop", slot_troop_mission_participation, mp_prison_break_fight),
          (try_begin),
            (agent_is_alive, ":agent"),
            (troop_set_slot, ":troop", slot_troop_mission_participation, mp_prison_break_escaped),
          (else_try),
            (troop_set_slot, ":troop", slot_troop_mission_participation, mp_prison_break_caught),
          (try_end),
        (try_end),
        (jump_to_menu, "mnu_sneak_into_town_caught_ran_away"),
        (mission_enable_talk),
        (finish_mission, 0),
      ]),
    ],
  ),

  (
    "sneak_caught_fight",mtf_battle_mode,-1,
    "You must fight your way out!",
    [
     (0,mtef_scene_source|mtef_team_0,af_override_all,aif_start_alarmed,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,af_override_all,aif_start_alarmed,1,pilgrim_disguise),
     (2,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (4,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (5,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (6,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (7,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (8,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (9,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (10,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (11,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (12,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (13,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (14,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (15,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (16,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (17,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (18,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (19,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (20,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (21,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (22,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (23,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (24,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (25,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (26,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (27,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (28,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (29,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (30,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (31,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (32,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (33,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (34,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (35,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (36,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (37,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (38,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (39,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (40,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (41,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (42,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (45,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (46,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (47,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (48,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (49,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (50,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (51,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (52,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (53,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (54,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (55,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (56,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (57,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (58,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (59,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (60,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (61,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (62,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (63,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (64,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),

     # (0,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,pilgrim_disguise),
     # (25,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (26,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (27,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (28,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (29,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (30,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (31,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (32,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     ], tocan_ambience+tocan_common_triggers+
    [
      (ti_before_mission_start, 0, 0, [],
      [
        (call_script, "script_change_banners_and_chest"),
      ]),

      (ti_after_mission_start, 0, 0, [],
       [
        (assign, ":num_guards", 5),

        (try_begin),
          (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
          (store_current_hours, ":cur_time"),
          (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),
          (is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"), #SB : fix is_between that was always false
          (assign, ":num_guards", 2),
        (else_try),
          (this_or_next|eq, "$talk_context", tc_escape),
          (eq, "$talk_context", tc_prison_break),

          (assign, ":num_guards", 4),
        (try_end),

        (try_begin),
          (this_or_next|eq, "$talk_context", tc_escape),
          (eq, "$talk_context", tc_prison_break),
          (entry_point_get_position, pos0, 7),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (entry_point_get_position, pos0, 0),
        (else_try),
          (entry_point_get_position, pos0, 1),
        (try_end),

        (assign, ":last_nearest_entry_distance", -1),
        (assign, ":last_nearest_entry_point", -1),
        (try_for_range, ":guard_no", 0, ":num_guards"),
          (assign, ":smallest_dist", 100000),
          (try_for_range, ":guard_entry_point", 2, 64),
            (neq, ":last_nearest_entry_point", ":guard_entry_point"),
            (entry_point_get_position, pos1, ":guard_entry_point"),
            (get_distance_between_positions, ":dist", pos0, pos1),
            (lt, ":dist", ":smallest_dist"),
            (gt, ":dist", ":last_nearest_entry_distance"),
            (assign, ":smallest_dist", ":dist"),
            (assign, ":nearest_entry_point", ":guard_entry_point"),
          (try_end),

          (store_faction_of_party, ":town_faction","$current_town"),
          (try_begin),
            (this_or_next|eq, ":guard_no", 0),
            (eq, ":guard_no", 2),
            (faction_get_slot, ":troop_of_guard", ":town_faction", slot_faction_tier_2_troop),
          # (else_try),
            # (faction_get_slot, ":troop_of_guard", ":town_faction", slot_faction_tier_2_troop),
          (try_end),

          (assign, ":last_nearest_entry_point", ":nearest_entry_point"),
          (assign, ":last_nearest_entry_distance", ":smallest_dist"),

          (add_visitors_to_current_scene, ":nearest_entry_point", ":troop_of_guard", 1, 0),
        (try_end),
      ]),

      (ti_tab_pressed, 0, 0, [],
       [(question_box,"str_do_you_wish_to_surrender")]),

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),(eq,":answer",0),(jump_to_menu,"mnu_captivity_start_castle_defeat"),(finish_mission,0),]),

      (1, 0, ti_once, [],
       [
         (play_sound,"snd_sneak_town_halt"),
         # (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
         ]),

      (0, 3, 0,
       [
          (main_hero_fallen,0),
        ],
       [
         (jump_to_menu,"mnu_captivity_start_castle_defeat"),
         (finish_mission,0),
       ]),

      (1, 0, 0, [],
       [
	    # (get_player_agent_no, "$g_player"),
	    (agent_get_position, pos0, "$g_player"),

        (try_for_agents, ":agent_no"),
          (neq, ":agent_no", "$g_player"),
          (agent_is_alive, ":agent_no"),
          (agent_get_team, ":agent_team", ":agent_no"),
          (eq, ":agent_team", 1),

          (agent_get_position, pos1, ":agent_no"),

          (get_distance_between_positions, ":dist", pos0, pos1),

          (try_begin),
            (le, ":dist", 800),
            (agent_clear_scripted_mode, ":agent_no"),
          (else_try),
            (agent_set_scripted_destination, ":agent_no", pos0, 0),
          (try_end),
        (try_end),
       ]),

	   (5, 1, ti_once,
	   [
	     #(num_active_teams_le,1),
		 (all_enemies_defeated),
	     (neg|main_hero_fallen),

         (store_mission_timer_a,":cur_time"),
         (ge, ":cur_time", 5),
	   ],
       [
         (assign,"$auto_menu",-1),
         (jump_to_menu,"mnu_sneak_into_town_caught_dispersed_guards"),
         (finish_mission,1),
       ]),

	   (ti_on_leave_area, 0, ti_once, [],
       [(assign,"$auto_menu",-1),(jump_to_menu,"mnu_sneak_into_town_caught_ran_away"),(finish_mission,0)]),

      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena",message_alert)], []),

    ],
  ),

   (
    "ai_training",0,-1,
    "You start training.",
    [
#     (0,0,af_override_horse,aif_start_alarmed,1,[]),
     (0,0,0,aif_start_alarmed,30,[]),
#     (1,mtef_no_leader,0,0|aif_start_alarmed,5,[]),
#     (0,mtef_no_leader,0,0|aif_start_alarmed,0,[]),
#     (3,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,6,[]),
#     (4,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,0,[]),
     ], tocan_ambience+tocan_common_triggers+
    [
#      (ti_before_mission_start, 0, 0, [], [(set_rain, 1,100), (set_fog_distance, 10)]),
      (ti_tab_pressed, 0, 0, [],
       [(finish_mission,0)]),

	   #teleport_to_entry_point, #for testing

      # common_battle_order_panel,
      # common_battle_order_panel_tick,

	  (1, 0, ti_once, [	#display total number of props
	  (set_passage_menu, "mnu_town"),	#also stop activating random cheat menu entires if use a door
	  (is_edit_mode_enabled)
	  ],
       [
	   (assign, ":prop_total", 0),
	   (try_for_prop_instances, ":props"),
			(val_add, ":prop_total", 1),
			(assign, reg1, ":props"),#for compiler
	   (try_end),
	   (assign, reg1, ":prop_total"),
	   #(display_message, "str_reg1"),#why no work?!
	   (display_message, "@prop_total: {reg1}"),
		
	   ]),

##      (0, 0, ti_once,
##       [
##         (key_clicked, key_numpad_7),
##        (mission_cam_set_mode,1),
##        (get_player_agent_no, "$g_player"),
##        (mission_cam_set_target_agent, "$g_player", 1),
##        (mission_cam_set_animation, "anim_test_cam"),], []),
    ]+ battle_panel_triggers,
  ),
   (
    "kragg_parade",0,-1,
    "You start training.",
    [
     #(0,0,0,aif_start_alarmed,1,[]),
     (0,0,af_override_horse,0,30,[]),
#     (1,mtef_no_leader,0,0|aif_start_alarmed,5,[]),
#     (0,mtef_no_leader,0,0|aif_start_alarmed,0,[]),
#     (3,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,6,[]),
#     (4,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,0,[]),
     ], tocan_ambience+tocan_common_triggers+
    [
#      (ti_before_mission_start, 0, 0, [], [(set_rain, 1,100), (set_fog_distance, 10)]),
      (ti_tab_pressed, 0, 0, [],
       [(finish_mission,0)]),


	    (ti_before_mission_start, 0, 0,
      [
	  (assign, "$g_no_of_parade_troops_in_row", 0),
	  (assign, "$g_no_of_parade_rows", 0),
	  (mission_disable_talk),
	   ], []),

	   (ti_on_agent_spawn, 0, 0,
      [
      (store_trigger_param_1, ":agent"),
	  (get_player_agent_no, ":player_agent"),

	  (try_begin),
		(neg|agent_is_non_player,":agent"),
		(init_position, pos4),
		(init_position, pos5),
		(agent_get_position, pos3, ":player_agent"),
		(copy_position, pos4, pos3),
		(copy_position, pos5, pos3),

		(position_move_y, pos3, 600),
		(position_move_x, pos3, 1500),
		(position_rotate_z, pos3, 180),
		(agent_set_position, ":player_agent", pos3),
		(mission_cam_set_target_agent, ":player_agent", 1),
		(agent_set_look_target_position, ":player_agent", pos3),
		(troop_get_inventory_slot, ":horse", "trp_player", ek_horse),
		(gt,":horse", -1),
		(position_move_x, pos3, 150),
		(set_spawn_position, pos3),
		(spawn_horse, ":horse"),
	   (else_try),
		(agent_is_human, ":agent"),
		(agent_is_non_player,":agent"),
		(store_mul,":x_distance", 100, "$g_no_of_parade_troops_in_row"),
		(store_mul,":y_distance", -100, "$g_no_of_parade_rows"),
		(position_move_x, pos4, ":x_distance"),
		(position_move_y, pos4, ":y_distance"),
		(position_set_z_to_ground_level, pos4),
		(agent_set_position, ":agent", pos4),

		(agent_set_animation, ":agent", "anim_at_ease_to_attention"),
		(agent_set_stand_animation, ":agent", "anim_attention"),

	    (val_add, "$g_no_of_parade_troops_in_row", 1),
		(try_begin),
			(gt, "$g_no_of_parade_troops_in_row", 30),
			(assign, "$g_no_of_parade_troops_in_row", 0),
			(val_add, "$g_no_of_parade_rows", 1),
		(try_end),
		(copy_position, pos4, pos5),
		
		(agent_ai_set_interact_with_player,":agent",0),
	  (try_end),

	   ], []),

	    (ti_on_agent_hit, 0, 0,
      [
      (store_trigger_param_1, ":shot_agent"),
	  (store_trigger_param_2, ":attacker"),
	  (neg|agent_is_non_player,":attacker"),
	  #(eq, ":attacker", "trp_player"),
	  (agent_is_non_player,":shot_agent"),
	  (agent_set_is_alarmed, ":shot_agent", 1),
	  (agent_set_team,":shot_agent", 1),
	   ], [

	  (store_trigger_param_1, ":shot_agent"),
	  (store_trigger_param_2, ":attacker"),
	  (neq, ":shot_agent", ":attacker"),
	  (store_trigger_param_3, ":damage"),


	  (neq, ":damage", 0),

	  (agent_is_non_player,":shot_agent"),
	  (neg|agent_is_non_player,":attacker"),
	  (agent_is_human, ":shot_agent"),
	  #(agent_get_wielded_item, ":damaging_item_id", ":attacker", 0),

	  #(assign, reg21, ":damage"),
	  #(display_message, "@Delivered {reg21} damage.", message_neutral),#sows twice for some reason?
      # (set_show_messages, 0),
	  # (agent_deliver_damage_to_agent, ":shot_agent", ":shot_agent", ":damage", ":damaging_item_id"), #causes crashes in wse2
      # (set_show_messages, 1),

		  (try_for_agents, ":agent"),
			(neq, ":agent", ":shot_agent"),
			(neq, ":agent", ":attacker"),
			(neg|agent_is_alarmed, ":agent"),
			(agent_is_non_player,":agent"),
			(agent_is_human, ":agent"),
			(agent_is_alive, ":agent"),
			(agent_set_stand_animation, ":agent", "anim_stand"),
			(agent_set_is_alarmed, ":agent", 1),
			#(agent_clear_relations_with_agents, ":agent"),
			(agent_ai_set_aggressiveness,":agent", 200),
			#(agent_is_ally, ":agent"),

			(agent_force_rethink, ":agent"),

			(store_random_in_range, ":flee_chance", 0, 5),
			(try_begin),
				(eq, ":flee_chance", 2),
				(agent_start_running_away, ":agent"),
				(agent_set_team,":agent", 1),
			   (else_try),
				(ge, ":flee_chance", 3),
				(get_player_agent_no, "$g_player"),
                (agent_get_team, ":player_team", "$g_player"),
				(agent_set_team,":agent", ":player_team"),
				#(agent_clear_relations_with_agents, ":agent"),
				#(agent_force_rethink, ":agent"),
			  (else_try),
				(agent_set_team,":agent", 1),#enemy?
			(try_end),
		  (try_end),

		  (set_trigger_result, 0),

	   ]),

      # common_battle_order_panel,
      # common_battle_order_panel_tick,

##      (0, 0, ti_once,
##       [
##         (key_clicked, key_numpad_7),
##        (mission_cam_set_mode,1),
##        (get_player_agent_no, "$g_player"),
##        (mission_cam_set_target_agent, "$g_player", 1),
##        (mission_cam_set_animation, "anim_test_cam"),], []),
    ]+ battle_panel_triggers,
  ),


  (
    "arena_melee_fight",mtf_arena_fight,-1,
    "You enter a melee fight in the arena.",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_mechanic_red]),
      (1,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_mechanic_red]),
      (2,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_mechanic_red]),
      (3,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_mechanic_red]),
      (4,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_mechanic_red]),
      (5,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_mechanic_red]),
      (6,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_mechanic_red]),
      (7,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_mechanic_red]),

      (8,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_mechanic_blue]),
      (9,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_mechanic_blue]),
      (10,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_mechanic_blue]),
      (11,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_mechanic_blue]),
      (12,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_mechanic_blue]),
      (13,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_mechanic_blue]),
      (14,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_mechanic_blue]),
      (15,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_mechanic_blue]),

      (16,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_mechanic_green]),
      (17,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_mechanic_green]),
      (18,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_mechanic_green]),
      (19,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_mechanic_green]),
      (20,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_mechanic_green]),
      (21,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_mechanic_green]),
      (22,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_mechanic_green]),
      (23,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_mechanic_green]),

      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_mechanic_brown]),
      (25,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_mechanic_brown]),
      (26,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_mechanic_brown]),
      (27,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_mechanic_brown]),
      (28,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_mechanic_brown]),
      (29,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_mechanic_brown]),
      (30,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_mechanic_brown]),
      (31,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_mechanic_brown]),
#32
      (32,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[arena_brawl_costume]),
      (33,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[arena_brawl_costume]),
      (34,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[arena_brawl_costume]),
      (35,mtef_visitor_source|mtef_team_4,af_override_all,aif_start_alarmed,1,[arena_brawl_costume]),
      (36,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[arena_brawl_costume]),
      (37,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[arena_brawl_costume]),
      (38,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[arena_brawl_costume]),
      (39,mtef_visitor_source|mtef_team_4,af_override_all,aif_start_alarmed,1,[arena_brawl_costume]),
#40-49 not used yet

      (50, mtef_scene_source,af_override_horse|af_override_weapons|af_override_head,0,1,[]),
      (51, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[]),
      (52, mtef_scene_source,af_override_horse,0,1,[]),
#not used yet:
      (53, mtef_scene_source,af_override_horse,0,1,[]),(54, mtef_scene_source,af_override_horse,0,1,[]),(55, mtef_scene_source,af_override_horse,0,1,[]),
#used for tournament master scene

      # (56, mtef_visitor_source|mtef_team_0, af_override_all, aif_start_alarmed, 1, [itm_practice_sword, itm_practice_shield, itm_padded_cloth, itm_segmented_helmet]),
      # (57, mtef_visitor_source|mtef_team_0, af_override_all, aif_start_alarmed, 1, [itm_practice_sword, itm_practice_shield, itm_padded_cloth, itm_segmented_helmet]),
      (56, mtef_visitor_source|mtef_team_0, af_override_all, aif_start_alarmed, 1, [itm_practice_dagger, itm_round_shield]),
      (57, mtef_visitor_source|mtef_team_0, af_override_all, aif_start_alarmed, 1, [itm_practice_dagger, itm_round_shield]),
    ],
    tocan_ambience+tocan_common_triggers+tournament_triggers
  ),

  (
    "arena_challenge_fight",mtf_arena_fight|mtf_commit_casualties,-1,
    "You enter a melee fight in the arena.",
    [
      (56, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 1, []),
      (58, mtef_visitor_source|mtef_team_2, 0, aif_start_alarmed, 1, []),
    ],
    [
      # common_inventory_not_available,
      # (ti_tab_pressed, 0, 0, [(display_message, "str_cannot_leave_now")], []),
      # (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      # (0, 0, ti_once, [],
       # [
         # (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
         # ]),


	# #NOTE -- THIS IS A VESTIGIAL SCRIPT. FOR LORD DUELS, USE THE NEXT SCRIPT DOWN
      # (1, 4, ti_once, [
	  # (this_or_next|main_hero_fallen),
		# (num_active_teams_le,1)],
       # [
           # (try_begin),
             # (main_hero_fallen),
			 # (check_quest_active, "qst_duel_for_lady"),
			 # (quest_slot_eq, "qst_duel_for_lady", slot_quest_target_troop, "$g_duel_troop"),
             # (call_script, "script_fail_quest", "qst_duel_for_lady"),
           # (else_try),
			 # (check_quest_active, "qst_duel_for_lady"),
			 # (quest_slot_eq, "qst_duel_for_lady", slot_quest_target_troop, "$g_duel_troop"),
             # (call_script, "script_succeed_quest", "qst_duel_for_lady"),
		   # (else_try),
             # (main_hero_fallen),
			 # (check_quest_active, "qst_duel_courtship_rival"),
			 # (quest_slot_eq, "qst_duel_courtship_rival", slot_quest_target_troop, "$g_duel_troop"),
             # (call_script, "script_fail_quest", "qst_duel_courtship_rival"),
           # (else_try),
			 # (check_quest_active, "qst_duel_courtship_rival"),
			 # (quest_slot_eq, "qst_duel_courtship_rival", slot_quest_target_troop, "$g_duel_troop"),
             # (call_script, "script_succeed_quest", "qst_duel_courtship_rival"),
		   # (else_try),
             # (main_hero_fallen),
			 # (check_quest_active, "qst_duel_avenge_insult"),
			 # (quest_slot_eq, "qst_duel_avenge_insult", slot_quest_target_troop, "$g_duel_troop"),
             # (call_script, "script_fail_quest", "qst_duel_avenge_insult"),
           # (else_try),
			 # (check_quest_active, "qst_duel_avenge_insult"),
			 # (quest_slot_eq, "qst_duel_avenge_insult", slot_quest_target_troop, "$g_duel_troop"),
             # (call_script, "script_succeed_quest", "qst_duel_avenge_insult"),
		   # (else_try),
             # (main_hero_fallen),
			 # (check_quest_active, "qst_denounce_lord"),
			 # (quest_slot_eq, "qst_denounce_lord", slot_quest_target_troop, "$g_duel_troop"),
             # (call_script, "script_fail_quest", "qst_denounce_lord"),
           # (else_try),
			 # (check_quest_active, "qst_denounce_lord"),
			 # (quest_slot_eq, "qst_denounce_lord", slot_quest_target_troop, "$g_duel_troop"),
             # (call_script, "script_succeed_quest", "qst_denounce_lord"),
		   # (else_try),
			 # (quest_get_slot, ":target_troop", "qst_denounce_lord", slot_quest_target_troop),
		     # (str_store_troop_name, s4, ":target_troop"),
		   # (try_end),
           # (finish_mission),
           # ]),
    ],
  ),

  (
    "duel_with_lord",mtf_arena_fight|mtf_commit_casualties,-1,
    "You enter a melee fight in the arena.",
    [
      # (0, mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_sword_medieval_a,itm_arena_tunic_blue]),
      # (16, mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_sword_medieval_a,itm_arena_tunic_blue]),
      # #SB : use these for fort courtyard duels
      # (23, mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_arena_sword,itm_heraldic_mail_with_tunic]),
      # (24, mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_arena_sword,itm_heraldic_mail_with_tunic_b]), #tocan test
      (0, mtef_visitor_source|mtef_team_0,af_override_head|af_override_horse,aif_start_alarmed,1,[]),
      (16, mtef_visitor_source|mtef_team_1,af_override_head|af_override_horse,aif_start_alarmed,1,[]),
      #SB : use these for fort courtyard duels
      (23, mtef_visitor_source|mtef_team_0,af_override_head|af_override_horse,aif_start_alarmed,1,[]),
      (24, mtef_visitor_source|mtef_team_1,af_override_head|af_override_horse,aif_start_alarmed,1,[]),

    ], tocan_ambience+tocan_common_triggers+
    [
      common_inventory_not_available,
      (ti_tab_pressed, 0, 0, [(display_message, "str_cannot_leave_now",message_alert)], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest"),
        #SB : remove siege objects if we fight in forts
        # (call_script, "script_remove_siege_objects"),
      ]),
      #SB : auto-lose duel if player leaves for some reason
      (ti_on_leave_area, 0, ti_once,
      [],
      [
          (try_for_range, ":quest", "qst_deliver_message_to_prisoner_lord", lady_quests_end),
            (try_begin),
              (eq, ":quest", "qst_deliver_message_to_prisoner_lord"),
              (assign, ":quest", "qst_denounce_lord"),
            (try_end),
            (check_quest_active, ":quest"),
            (quest_slot_eq, ":quest", slot_quest_target_troop, "$g_duel_troop"),
            (call_script, "script_fail_quest", ":quest"),
            (finish_mission),
          (try_end),
      ]),
      # (0, 0, ti_once, [],
       # [
         # (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
         # ]),


      (1, 4, ti_once, [
	  (this_or_next|main_hero_fallen),
		(num_active_teams_le,1)],
       [

          (try_begin),
            (main_hero_fallen),
            (assign, ":state", "script_fail_quest"),
          (else_try),
            (assign, ":state", "script_succeed_quest"),
          (try_end),
          #start at 1 before the duel quests
          (try_for_range, ":quest", "qst_deliver_message_to_prisoner_lord", lady_quests_end),
            (try_begin),
              (eq, ":quest", "qst_deliver_message_to_prisoner_lord"),
              (assign, ":quest", "qst_denounce_lord"),
            (try_end),
            (check_quest_active, ":quest"),
            (quest_slot_eq, ":quest", slot_quest_target_troop, "$g_duel_troop"),
            (call_script, ":state", ":quest"),
          (try_end),
          #SB : replace with loop
          (finish_mission),
           ]),
    ],
  ),


  (
    "wedding",0,-1,
    "Wedding",
    [
        (0,mtef_visitor_source,af_override_everything,0,1,[itm_formal]),
        (1,mtef_visitor_source,af_override_everything,0,1,[itm_bride_dress, itm_bride_crown]),
        (2,mtef_visitor_source,af_castle_lord,0,1,[]),
        (3,mtef_visitor_source,af_castle_lord,0,1,[]),
        # (3,mtef_visitor_source,af_override_everything,0,1,[itm_coat_1]),
        (4,mtef_visitor_source,af_castle_lord,0,1,[]),
        (5,mtef_visitor_source,af_castle_lord,0,1,[]),
        (6,mtef_visitor_source,af_castle_lord,0,1,[]),
        (7,mtef_visitor_source,af_castle_lord,0,1,[]),
        (8,mtef_visitor_source,af_castle_lord,0,1,[]),
        (9,mtef_visitor_source,af_castle_lord,0,1,[]),
        (10,mtef_visitor_source,af_castle_lord,0,1,[]),
        (11,mtef_visitor_source,af_castle_lord,0,1,[]),
        (12,mtef_visitor_source,af_castle_lord,0,1,[]),
        (13,mtef_visitor_source,af_castle_lord,0,1,[]),
        (14,mtef_visitor_source,af_castle_lord,0,1,[]),
        (15,mtef_visitor_source,af_castle_lord,0,1,[]),
        (16,mtef_visitor_source,af_castle_lord,0,1,[]),
        (17,mtef_visitor_source,af_castle_lord,0,1,[]),
        (18,mtef_visitor_source,af_castle_lord,0,1,[]),
        (19,mtef_visitor_source,af_castle_lord,0,1,[]),
        (20,mtef_visitor_source,af_castle_lord,0,1,[]),
        (21,mtef_visitor_source,af_castle_lord,0,1,[]),
        (22,mtef_visitor_source,af_castle_lord,0,1,[]),
        (23,mtef_visitor_source,af_castle_lord,0,1,[]),
        (24,mtef_visitor_source,af_castle_lord,0,1,[]),
        (25,mtef_visitor_source,af_castle_lord,0,1,[]),
        (26,mtef_visitor_source,af_castle_lord,0,1,[]),
        (27,mtef_visitor_source,af_castle_lord,0,1,[]),
        (28,mtef_visitor_source,af_castle_lord,0,1,[]),
        (29,mtef_visitor_source,af_castle_lord,0,1,[]),
        (30,mtef_visitor_source,af_castle_lord,0,1,[]),
        (31,mtef_visitor_source,af_castle_lord,0,1,[]),
     ],
    [
      (ti_tab_pressed, 0, 0, [],
       [
         (show_object_details_overlay, 1),
         (finish_mission,0),
        ]),
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (show_object_details_overlay, 1),
        (finish_mission,0),
        ]),

      (ti_after_mission_start, 0, 0, [],
       [
        (assign, "$g_wedding_state", 0),
        (play_track, "track_wedding", 2),
        (show_object_details_overlay, 0),
         ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (troop_get_type, ":gender", ":troop_no"),
         (set_fixed_point_multiplier, 100),
         (try_begin),
           (eq, ":troop_no", "$g_wedding_bishop_troop"),
         (else_try),
           (eq, ":troop_no", "$g_wedding_bride_troop"),
           (agent_set_no_dynamics, ":agent_no", 1),
           (init_position, pos1),
           (position_set_z, pos1, -1000),
           (agent_set_position, ":agent_no", pos1),
         (else_try),
           (eq, ":troop_no", "$g_wedding_brides_dad_troop"),
           (agent_set_no_dynamics, ":agent_no", 1),
           (init_position, pos1),
           (position_set_z, pos1, -1000),
           (agent_set_position, ":agent_no", pos1),
         (else_try),
           (eq, ":troop_no", "$g_wedding_groom_troop"),
           (agent_set_no_dynamics, ":agent_no", 1),
           (init_position, pos1),
           (position_move_x, pos1, 175),
           (position_move_z, pos1, 10),
           (position_rotate_z, pos1, 180),
           (agent_set_position, ":agent_no", pos1),
           (agent_set_animation, ":agent_no", "anim_wedding_groom_wait"),
         (else_try),
           (try_begin),
             (eq, ":gender", 0), #male
             (store_random_in_range, ":random_no", 0, 3),
             (try_begin),
               (eq, ":random_no", 0),
               (agent_set_slot, ":agent_no", slot_agent_cur_animation, "anim_wedding_guest_notr"),
               (agent_set_animation, ":agent_no", "anim_wedding_guest_notr"),
             (else_try),
               (agent_set_slot, ":agent_no", slot_agent_cur_animation, "anim_wedding_guest"),
               (agent_set_animation, ":agent_no", "anim_wedding_guest"),
             (try_end),
           (else_try), #female
             (agent_set_slot, ":agent_no", slot_agent_cur_animation, "anim_wedding_guest_woman"),
             (agent_set_animation, ":agent_no", "anim_wedding_guest_woman"),
           (try_end),
           (store_random_in_range, ":progress", 0, 100),
           (agent_set_animation_progress, ":agent_no", ":progress"),
         (try_end),
         ]),

      (0, 0, 0,
       [
         (store_mission_timer_a, ":cur_time"),
         (set_fixed_point_multiplier, 100),
         (try_for_agents, ":agent_no"),
           (agent_get_troop_id, ":troop_no", ":agent_no"),
           (try_begin),
             (eq, ":troop_no", "$g_wedding_groom_troop"),
           (else_try),
             (eq, ":troop_no", "$g_wedding_bride_troop"),
           (else_try),
             (eq, ":troop_no", "$g_wedding_brides_dad_troop"),
           (else_try),
             (eq, ":troop_no", "$g_wedding_bishop_troop"),
           (else_try),
             (agent_get_slot, ":cur_animation", ":agent_no", slot_agent_cur_animation),
             (agent_set_animation, ":agent_no", ":cur_animation"),
           (try_end),
         (try_end),
         (try_begin),
           (eq, "$g_wedding_state", 0),
           #SB : head camera, store cur values and force 3rd person
           (try_begin),
             (is_camera_in_first_person),
             (assign, "$g_dplmc_cam_activated", 1),
           (else_try),
             (assign, "$g_dplmc_cam_activated", 0),
           (try_end),
           (set_camera_in_first_person, 0),
           (mission_cam_set_mode, 1, 0, 0),
           (init_position, pos1),
           (position_rotate_z, pos1, 180),
           (position_rotate_x, pos1, 5),
           (position_set_x, pos1, -500),
           (position_set_y, pos1, 1000),
           (position_set_z, pos1, 600),
           (mission_cam_set_position, pos1),
           (init_position, pos1),
           (position_rotate_z, pos1, 180),
           (position_rotate_x, pos1, -15),
           (position_set_x, pos1, -500),
           (position_set_y, pos1, 1000),
           (position_set_z, pos1, 600),
           (mission_cam_animate_to_position, pos1, 4000, 0),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 1),
           (ge, ":cur_time", 4),
           (init_position, pos1),
           (position_rotate_z, pos1, 90),
           (position_rotate_x, pos1, -10),
           (position_set_x, pos1, -580),
           (position_set_y, pos1, 700),
           (position_set_z, pos1, 200),
           (mission_cam_set_position, pos1),
           (init_position, pos1),
           (position_rotate_z, pos1, 150),
           (position_rotate_x, pos1, -10),
           (position_set_x, pos1, -580),
           (position_set_y, pos1, 100),
           (position_set_z, pos1, 200),
           (mission_cam_animate_to_position, pos1, 6000, 1),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 2),
           (ge, ":cur_time", 9),
           (mission_cam_animate_to_screen_color, 0xFF000000, 1000),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 3),
           (ge, ":cur_time", 10),
           (init_position, pos1),
           (position_move_x, pos1, 175),
           (position_move_z, pos1, 10),
           (position_rotate_z, pos1, 180),
           (try_for_agents, ":agent_no"),
             (agent_get_troop_id, ":agent_troop", ":agent_no"),
             (try_begin),
               (eq, ":agent_troop", "$g_wedding_bride_troop"),
               (agent_set_position, ":agent_no", pos1),
               (agent_set_animation, ":agent_no", "anim_wedding_bride_stairs"),
             (else_try),
               (eq, ":agent_troop", "$g_wedding_brides_dad_troop"),
               (agent_set_position, ":agent_no", pos1),
               (agent_set_animation, ":agent_no", "anim_wedding_dad_stairs"),
             (try_end),
           (try_end),
           (init_position, pos1),
           (position_rotate_z, pos1, -90),
           (position_set_x, pos1, 300),
           (position_set_y, pos1, 950),
           (position_set_z, pos1, 420),
           (mission_cam_set_position, pos1),
           (position_set_x, pos1, 175),
           (position_set_y, pos1, 950),
           (position_set_z, pos1, 320),
           (mission_cam_animate_to_position, pos1, 4000, 0),
           (mission_cam_animate_to_screen_color, 0x00000000, 500),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 4),
           (ge, ":cur_time", 14),
           (init_position, pos1),
           (position_rotate_z, pos1, -60),
           (position_rotate_x, pos1, 10),
           (position_set_x, pos1, -400),
           (position_set_y, pos1, 200),
           (position_set_z, pos1, 115),
           (mission_cam_set_position, pos1),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 5),
           (ge, ":cur_time", 20),
           (init_position, pos1),
           (position_move_x, pos1, 175),
           (position_move_z, pos1, 10),
           (position_rotate_z, pos1, 180),
           (try_for_agents, ":agent_no"),
             (agent_get_troop_id, ":agent_troop", ":agent_no"),
             (try_begin),
               (eq, ":agent_troop", "$g_wedding_bride_troop"),
               (agent_set_position, ":agent_no", pos1),
               (agent_set_animation, ":agent_no", "anim_wedding_bride_walk"),
             (else_try),
               (eq, ":agent_troop", "$g_wedding_brides_dad_troop"),
               (agent_set_position, ":agent_no", pos1),
               (agent_set_animation, ":agent_no", "anim_wedding_dad_walk"),
             (try_end),
           (try_end),
           (init_position, pos1),
           (position_rotate_z, pos1, -140),
           (position_rotate_x, pos1, -15),
           (position_set_x, pos1, -625),
           (position_set_y, pos1, -530),
           (position_set_z, pos1, 180),
           (mission_cam_set_position, pos1),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 6),
           (ge, ":cur_time", 22),
           (init_position, pos1),
           (position_rotate_z, pos1, 45),
           (position_rotate_x, pos1, -10),
           (position_set_x, pos1, -260),
           (position_set_y, pos1, 120),
           (position_set_z, pos1, 275),
           (mission_cam_set_position, pos1),
           (position_rotate_z, pos1, 10),
           (mission_cam_animate_to_position, pos1, 2000, 0),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 7),
           (ge, ":cur_time", 24),
           (init_position, pos1),
           (position_move_x, pos1, 175),
           (position_move_z, pos1, 10),
           (position_rotate_z, pos1, 180),
           (try_for_agents, ":agent_no"),
             (agent_get_troop_id, ":agent_troop", ":agent_no"),
             (try_begin),
               (eq, ":agent_troop", "$g_wedding_bride_troop"),
               (agent_set_position, ":agent_no", pos1),
               (agent_set_animation, ":agent_no", "anim_wedding_bride_last"),
             (else_try),
               (eq, ":agent_troop", "$g_wedding_brides_dad_troop"),
               (agent_set_position, ":agent_no", pos1),
               (agent_set_animation, ":agent_no", "anim_wedding_dad_last"),
             (else_try),
               (eq, ":agent_troop", "$g_wedding_groom_troop"),
               (agent_set_position, ":agent_no", pos1),
               (agent_set_animation, ":agent_no", "anim_wedding_groom_last"),
             (try_end),
           (try_end),
           (init_position, pos1),
           (position_rotate_z, pos1, -45),
           (position_rotate_x, pos1, -10),
           (position_set_x, pos1, -900),
           (position_set_y, pos1, -850),
           (position_set_z, pos1, 230),
           (mission_cam_set_position, pos1),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 8),
           (ge, ":cur_time", 31),
           (init_position, pos1),
           (position_set_x, pos1, -550),
           (position_set_y, pos1, -625),
           (position_set_z, pos1, 1500),
           (particle_system_burst, "psys_wedding_rose", pos1, 750),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 9),
           (ge, ":cur_time", 33),
           (init_position, pos1),
           (position_rotate_z, pos1, 180),
           (position_set_x, pos1, -536),
           (position_set_y, pos1, -415),
           (position_set_z, pos1, 135),
           (mission_cam_set_position, pos1),
           (position_rotate_z, pos1, -8),
           (position_set_z, pos1, 350),
           (position_rotate_x, pos1, 35),
           (mission_cam_animate_to_position_and_aperture, pos1, 10, 9000, 1),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 10),
           (ge, ":cur_time", 41),
           (mission_cam_set_screen_color, 0x00FFFFFF),
           (mission_cam_animate_to_screen_color, 0xFFFFFFFF, 3000),
           (val_add, "$g_wedding_state", 1),
         (else_try),
           (eq, "$g_wedding_state", 11),
           (ge, ":cur_time", 48),
           #SB : reset camera
           (set_camera_in_first_person, "$g_dplmc_cam_activated"),
           (show_object_details_overlay, 1),
           (finish_mission,0),
         (try_end),
         ], []),
    ],
  ),

("meeting_merchant",0,-1,
    "Meeting with the merchant",
    [
      (0,mtef_team_0,af_override_horse,0,1,[]),
      (1,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (2,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (3,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (4,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (5,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (6,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (7,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (8,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (9,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
    ],
    [
      (ti_on_agent_spawn, 0, 0, [],
      [
        (store_trigger_param_1, ":agent_no"),

        (try_begin),
          (agent_get_troop_id, ":troop_no", ":agent_no"),
          (is_between, ":troop_no", startup_merchants_begin, startup_merchants_end),
          (agent_set_team, ":agent_no", 7),
          (team_set_relation, 0, 7, 0),
        (try_end),
      ]),

      (1, 0, ti_once, [],
      [
        (assign, "$dialog_with_merchant_ended", 0),
        (store_current_scene, ":cur_scene"),
        (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
        # (try_begin),
          # (gt, "$sneaked_into_town", disguise_none),
          # (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
        # (else_try),
          # (eq, "$talk_context", tc_tavern_talk),
          # (call_script, "script_music_set_situation_with_culture", mtf_sit_tavern),
        # (else_try),
          # (call_script, "script_music_set_situation_with_culture", mtf_sit_town),
        # (try_end),
      ]),

      (1, 0, 0,
      [
        (assign, ":continue", 0),
        (try_begin),
          (ge, "$dialog_with_merchant_ended", 6),
          (assign, ":continue", 1),
        (else_try),
          (ge, "$dialog_with_merchant_ended", 1),
          (neg|conversation_screen_is_active),

          (try_begin),
            (eq, "$dialog_with_merchant_ended", 1),
            (check_quest_active, "qst_collect_men"),
            (tutorial_box, "str_start_up_first_quest", "@Tutorial"),
          (try_end),

          (val_add, "$dialog_with_merchant_ended", 1),
          (assign, ":continue", 0),
        (try_end),

        (try_begin),
          (conversation_screen_is_active),
          (tutorial_message, -1),
          (assign, ":continue", 0),
        (try_end),

        (eq, ":continue", 1),
      ],
      [
        (tutorial_message_set_size, 17, 17),
        (tutorial_message_set_position, 500, 650),
        (tutorial_message_set_center_justify, 0),
        (tutorial_message_set_background, 1),
        (tutorial_message, "str_press_tab_to_exit_from_town"),
      ]),

      (ti_inventory_key_pressed, 0, 0,
      [
        # (show_object_details_overlay, 1),
        (set_trigger_result, 1),
      ], []),

      (ti_tab_pressed, 0, 0,
      [
        (try_begin),
          (gt, "$dialog_with_merchant_ended", 0),

          (assign, ":max_dist", 0),
          (party_get_position, pos1, "$current_town"),
          (try_for_range, ":unused", 0, 10),
            (map_get_random_position_around_position, pos0, pos1, 2),
            (get_distance_between_positions, ":dist", pos0, pos1),
            (ge, ":dist", ":max_dist"),
            (assign, ":max_dist", ":dist"),
            (copy_position, pos2, pos0),
          (try_end),

          (party_set_position, "p_main_party", pos2),

          (finish_mission),

          (assign, "$current_startup_quest_phase", 2),

          (tutorial_message, -1),

          (tutorial_message_set_background, 0),

          (change_screen_map),

          (try_begin),
            (check_quest_finished, "qst_save_town_from_bandits"),
            (assign, "$g_do_one_more_meeting_with_merchant", 1),
          (else_try),
            #will do this at first spawning in the map
            (set_spawn_radius, 50),
            (try_for_range, ":unused", 0, 20),
              (spawn_around_party, "p_main_party", "pt_looters"),
            (try_end),
          (try_end),

          (set_trigger_result, 1),
        (else_try),
          (display_message, "str_cannot_leave_now",message_alert),
        (try_end),
      ], []),
    ]),

("town_attack",mtf_battle_mode,-1,#mtf_synch_inventory, removed to have medikit disappearing, I dont know what it is good for
    "You attack the walls of the town...",
    [
     (1,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (1,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     # (2,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,14,[]),
     # (2,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,6,[]),
     # (2,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (14,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,6,[]),	#defender spawn, was 2 - krag
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),	#defender reinforcements, was 2
     (32,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (33,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (34,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (35,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (36,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (37,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (38,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (39,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),

     # (1,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     # (1,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     # # (10,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # # (11,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # # (12,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # (2,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # # (23,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # # (24,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # # (25,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # # (26,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # # (27,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # # (28,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # # (3,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # (32,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,2,[]),
     # (33,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,2,[]),
     # (34,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,2,[]),
     # (35,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,2,[]),
     # (36,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,2,[]),
     # (37,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # (38,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # (39,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # # (4,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # # (5,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # # (6,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # # (7,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     # # (9,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),

     # (40,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     # (41,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     # (42,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     # (43,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     # (44,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     # (45,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     # (46,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     ], tocan_ambience+tocan_common_triggers+tocan_battle_triggers+tocan_cover+tocan_autofire+tocan_flashlight+
    [
      common_battle_mission_start,
      common_battle_tab_press,
      common_battle_init_banner,
      common_siege_question_answered,
      common_siege_init,
      # common_music_situation_update,
      common_siege_ai_trigger_init,
      common_siege_ai_trigger_init_after_2_secs,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,
      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_inventory_not_available,

      common_siege_attacker_do_not_stall,
	  common_siege_attacker_do_not_stall_spawn,
	  
	  free_stuck_cover_seekers,

    (ti_before_mission_start, 0, 0, [ #init before mission

      (try_begin),
        (neq, "$g_player_team", "$attacker_team"), #player should be the defender
        (neq, "$g_player_team", "$attacker_team_2"), #player should be the defender

        (assign, "$g_last_cover_radius", 1000),
       (else_try),
        (assign, "$g_last_cover_radius", 2000),
      (try_end),

      (replace_scene_props, "spr_prop_npc_armored_guard", "spr_empty"),
      (replace_scene_props, "spr_prop_npc_dancing_woman", "spr_empty"),
      (replace_scene_props, "spr_prop_npc_sitting_on_stool", "spr_empty"),
      (replace_scene_props, "spr_prop_npc_sitting_drinking", "spr_empty"),
      (replace_scene_props, "spr_prop_npc_sitting_on_floor", "spr_empty"),
      (replace_scene_props, "spr_prop_npc_sleeping", "spr_empty"),
      (replace_scene_props, "spr_prop_npc_man_guitar", "spr_empty"),
      (replace_scene_props, "spr_prop_npc_man_pressups", "spr_empty"),
      (replace_scene_props, "spr_prop_npc_hanging", "spr_empty"),
      (replace_scene_props, "spr_prop_npc_priest", "spr_empty"),
      (replace_scene_props, "spr_prop_npc_mechanic", "spr_empty"),
      (replace_scene_props, "spr_prop_npc_hobo", "spr_empty"),
      (replace_scene_props, "spr_prop_npc_doctor", "spr_empty"),

      (store_current_scene, ":cur_scene"),
      (try_begin),
        (this_or_next|eq, ":cur_scene", "scn_town_1_center"),
        (this_or_next|eq, ":cur_scene", "scn_town_2_center"),  
        (this_or_next|eq, ":cur_scene", "scn_town_3_center"),
        (this_or_next|eq, ":cur_scene", "scn_town_4_center"),  
        (this_or_next|eq, ":cur_scene", "scn_town_5_center"),  
        (this_or_next|eq, ":cur_scene", "scn_town_6_center"),	
        (this_or_next|eq, ":cur_scene", "scn_town_7_center"),
        (this_or_next|eq, ":cur_scene", "scn_town_8_center"),
        (this_or_next|eq, ":cur_scene", "scn_town_new3"),		
        (this_or_next|eq, ":cur_scene", "scn_town_10_center"), 
        (this_or_next|eq, ":cur_scene", "scn_town_11_center"), 
        (this_or_next|eq, ":cur_scene", "scn_town_15_center"), 
        (this_or_next|eq, ":cur_scene", "scn_town_16_center"), 
        (this_or_next|eq, ":cur_scene", "scn_town_17_center"),
        (this_or_next|eq, ":cur_scene", "scn_town_19_center"),
        (this_or_next|eq, ":cur_scene", "scn_town_20_center"), 
        (this_or_next|eq, ":cur_scene", "scn_town_21_center"),
        (this_or_next|eq, ":cur_scene", "scn_town_22_center"), 
        (eq, ":cur_scene", "scn_town_12_center"),

        (assign,"$g_covers_active",2),
      (else_try),
        (assign,"$g_covers_active",1),
      (try_end),

      ],
        []),

    (5, 0, ti_once,
          [
           (try_begin), 
			(eq, "$scene_has_cover", 1),
            (set_show_messages, 0),
            (team_give_order, "$defender_team", grc_everyone, mordr_stand_ground),
            (team_give_order, "$defender_team_2", grc_everyone, mordr_stand_ground),

            # (call_script,"script_cover_battle_start","$defender_team",1000),	#search for close cover first - krag
            # (call_script,"script_cover_battle_start","$defender_team_2",1000),
            # (call_script,"script_cover_battle_start","$attacker_team",1000),
            # (call_script,"script_cover_battle_start","$attacker_team_2",1000),

            # (call_script,"script_cover_battle_start","$defender_team",2500),	#search for mid cover second
            # (call_script,"script_cover_battle_start","$defender_team_2",2500),
            # (call_script,"script_cover_battle_start","$attacker_team",2500),
            # (call_script,"script_cover_battle_start","$attacker_team_2",2500),

            (call_script,"script_cover_battle_start","$defender_team",15000),
            (call_script,"script_cover_battle_start","$defender_team_2",15000),
            (call_script,"script_cover_battle_start","$attacker_team",5000),
            (call_script,"script_cover_battle_start","$attacker_team_2",5000),
            (display_message, "@Cover positions found, troops entering cover..."),
            (set_show_messages, 1),
		   (try_end),	

           (try_begin), 
			(this_or_next|eq, "$g_encountered_party_faction", "fac_infected"),
			(eq, "$g_encountered_party_faction", "fac_mutants"),
            #(set_show_messages, 0),
            (team_give_order, "$defender_team", grc_everyone, mordr_charge),
            (team_give_order, "$defender_team_2", grc_everyone, mordr_charge),
            #(set_show_messages, 1),
           # (display_message, "@The monstrous defenders swarm out!", message_negative),
		   (try_end),	

          ], []),

    (0, 1, ti_once,
    [
      ],
      [
	  (neq, "$g_encountered_party_faction", "fac_infected"),
	  (neq, "$g_encountered_party_faction", "fac_mutants"),
	  #(display_message, "@The defenders stand their ground", message_positive),
      (set_show_messages, 0),

      (team_give_order, "$defender_team", grc_everyone, mordr_stand_ground),
      (team_give_order, "$defender_team_2", grc_everyone, mordr_stand_ground),

      (set_show_messages, 1),
      ]),

    (1, 0, 5, #attacker
      [
        ],
      [
        (lt,"$attacker_reinforcement_stage",5),
        (store_mission_timer_a,":mission_time"),
        (ge,":mission_time",10),

        (store_normalized_team_count,":num_attackers",1),
        (lt,":num_attackers",6),
        (add_reinforcements_to_entry, 1, 8),
        (val_add,"$attacker_reinforcement_stage", 1),

		(try_begin),
          # (agent_get_team, ":player_team", "$g_player"),
          (neq, "$g_player_team", "$attacker_team"), #player should be the defender
          (neq, "$g_player_team", "$attacker_team_2"), #player should be the defender

          (try_begin),
            (gt, "$g_last_cover_radius", 5000),

            (assign, "$g_last_cover_radius", 1000),
          (else_try),
            (val_add, "$g_last_cover_radius", 1000),
          (try_end),

		  #(assign, reg27, "$attacker_team"),
		#(assign, reg28, "$attacker_team_2"),
		#(display_message, "@attacker_team: {reg27},  attacker_team_2: {reg28}"),

           (call_script,"script_cover_battle_start","$attacker_team", "$g_last_cover_radius"),
           (call_script,"script_cover_battle_start","$attacker_team_2", "$g_last_cover_radius"),
        (try_end),

        ]),


      (3, 0, 5, [],
        [(lt, "$defender_reinforcement_stage", 7),
         (store_mission_timer_a,":mission_time"),
         (ge,":mission_time",10),



         (store_normalized_team_count,":num_defenders",0),
         (lt,":num_defenders",8),
         (add_reinforcements_to_entry,3, 7),
         # (add_reinforcements_to_entry,4, 7),

		 (try_begin),
            # (agent_get_team, ":player_team", "$g_player"),
            (neq, "$g_player_team", "$defender_team"), #player should be the attacker
            (neq, "$g_player_team", "$defender_team_2"), #player should be the attacker

              (try_begin),
                (gt, "$g_last_cover_radius", 10000),

                (assign, "$g_last_cover_radius", 2000),
              (else_try),
                (val_add, "$g_last_cover_radius", 2000),
              (try_end),

				#(assign, reg27, "$defender_team"),
				#(assign, reg28, "$defender_team_2"),
				#(display_message, "@defender_team: {reg27},  defender_team_2: {reg28}"),

             (call_script,"script_cover_battle_start","$defender_team", "$g_last_cover_radius"),
             (call_script,"script_cover_battle_start","$defender_team_2", "$g_last_cover_radius"),
          (try_end),

         (val_add,"$defender_reinforcement_stage",1),
		 (agent_get_team, ":player_team", "$g_player"),
         (try_begin),
           (gt, ":mission_time", 600), #5 minutes, don't let small armies charge	;extended as charging too early - krag
           # (get_player_agent_no, "$g_player"),

           (neq, ":player_team", "$defender_team"), #player should be the attacker
           (neq, ":player_team", "$defender_team_2"), #player should be the attacker
           (ge, "$defender_reinforcement_stage", 5),	#was 2
		   (display_message, "@Defenders charging out."),
           (set_show_messages, 0),
           (team_give_order, "$defender_team", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
           (team_give_order, "$defender_team_2", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
           (team_give_order, "$defender_team", grc_cavalry, mordr_charge), #AI desperate charge:cavalry!!!
           (team_give_order, "$defender_team_2", grc_cavalry, mordr_charge), #AI desperate charge:cavalry!!!
           (set_show_messages, 1),
           (ge, "$defender_reinforcement_stage", 7), #was 4
           (set_show_messages, 0),
           (team_give_order, "$defender_team", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
           (team_give_order, "$defender_team_2", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!

		    (call_script,"script_cover_ai_end","$defender_team"),	#make thema ctually leave cover
		    (call_script,"script_cover_ai_end","$defender_team_2"),
			(assign, "$g_autocover_ai", 0),	#stop them getting back in
           (set_show_messages, 1),
         (try_end),

		 (try_begin),
			(main_hero_fallen),
			(this_or_next| eq, ":player_team", "$defender_team"),
			(eq, ":player_team", "$defender_team_2"),
			#(assign, "$player_fallen_so_allies_seek_cover", 1),
			(assign, "$g_autocover", 1),
			# (get_player_agent_no, "$g_player"),
			# (agent_get_position, pos26, "$g_player"),
			# (call_script, "script_cover_search_player", pos26, 10000),	#player troops search for cover on death
			# (display_message, "@Your troops seek cover after you fall (if possible)."),
		(try_end),
         ]),


      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        (store_trigger_param_3, ":is_wounded"),

        (try_begin),
          (ge, ":dead_agent_no", 0),
          (neg|agent_is_ally, ":dead_agent_no"),
          (agent_is_human, ":dead_agent_no"),
          (agent_get_troop_id, ":dead_agent_troop_id", ":dead_agent_no"),
          (str_store_troop_name, s6, ":dead_agent_troop_id"),
          (assign, reg0, ":dead_agent_no"),
          (assign, reg1, ":killer_agent_no"),
          (assign, reg2, ":is_wounded"),
          (agent_get_team, reg3, ":dead_agent_no"),
          #(display_message, "@{!}dead agent no : {reg0} ; killer agent no : {reg1} ; is_wounded : {reg2} ; dead agent team : {reg3} ; {s6} is added"),
          (party_add_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), #addition_to_p_total_enemy_casualties
          (eq, ":is_wounded", 1),
          (party_wound_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1),
        (try_end),
       ]),
	   
      (ti_on_agent_spawn, 0, 0, [(neq, "$g_autocover_ai", 0),], #ghoul/infected stop ai autocover
       [
		(store_trigger_param_1, ":agent_no"),
		(agent_get_troop_id, ":troop_id", ":agent_no"),
        (this_or_next|eq, ":troop_id", "trp_the_suits"),
		(this_or_next|eq, ":troop_id", "trp_infected_1"),
		(this_or_next|eq, ":troop_id", "trp_infected_2"),
		(this_or_next|eq, ":troop_id", "trp_infected_3"),
        (this_or_next|eq, ":troop_id", "trp_infected_4"),
        (this_or_next|eq, ":troop_id", "trp_infected_5"),
        (this_or_next|eq, ":troop_id", "trp_infected_6"),
		(this_or_next|eq, ":troop_id", "trp_ghoul_scavenger"),
		(eq, ":troop_id", "trp_ghoul"),
		(assign, "$g_autocover_ai", 0),	#stop them taking cover
         ]),
	   

    ]
    + dplmc_battle_mode_triggers + battle_panel_triggers + extended_battle_menu,

  ),

("camp_attack_bandits",mtf_battle_mode,charge,#mtf_synch_inventory, removed to have medikit disappearing, I dont know what it is good for
    "You lead your men to battle.",
    [
     (3,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     (1,mtef_team_0|mtef_use_exact_number,0,aif_start_alarmed, 7,[]),
     (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
     ], x_companion+tocan_ambience+tocan_common_triggers+tocan_battle_triggers+tocan_autofire+tocan_cover+tocan_flashlight+
     # ], tocan_ambience+tocan_common_triggers+tocan_scene_maker+tocan_cover+tocan_battle_triggers+
    [
      common_battle_tab_press,
      common_battle_init_banner,

      (0, 0, ti_once, [],
       [
        (entry_point_get_position,pos1, 11), #village master
        (try_for_prop_instances, ":instance"),
            (prop_instance_get_position, pos2, ":instance"),
            (get_distance_between_positions,":doit",pos1,pos2),
            (le,":doit",2500),
            # (prop_instance_get_scene_prop_kind, ":prop",":instance"),
            # (is_between,":prop","spr_invalid_object","spr_scene_props_end"),
            (store_random_in_range,":particle",0,10),

            (try_begin),
                (eq,":particle",1),
                (position_set_z_to_ground_level, pos2),

                (set_spawn_position, pos2),
                # (display_message,"@spr_battle_field_smoke"),
                (spawn_scene_prop, "spr_battle_field_smoke"),
            (else_try),
                (eq,":particle",2),
                (position_set_z_to_ground_level, pos2),

                (set_spawn_position, pos2),
                # (display_message,"@spr_Village_fire_big"),
                (spawn_scene_prop, "spr_Village_fire_big"),
            (else_try),
                (eq,":particle",3),
                (position_set_z_to_ground_level, pos2),

                (set_spawn_position, pos2),
                # (display_message,"@spr_fire"),
                (spawn_scene_prop, "spr_fire"),
            (try_end),
        (try_end),
         ]),

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 10, 20, 1),
        (assign, "$g_battle_result", -1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (4, 0, ti_once, [],
        [
          (try_begin),
              (ge, "$g_special_companion", 1),
              (assign, "$x_npc_order", -1),
              # (get_player_agent_no, "$g_player"),
              (agent_clear_scripted_mode, "$g_player_x_agent_no"),
              # (agent_get_team, ":player_team", "$g_player"),
              #(agent_add_relation_with_agent, "$g_player", "$g_player_x_agent_no", 1),
              (set_show_messages, 0),
              (team_give_order, "$g_player_team", grc_special, mordr_follow),
              (set_show_messages, 1),
          (try_end),
      ]),

      (0, 0, ti_once, [], [(assign, "$g_battle_won", 0),
                           (assign, "$defender_reinforcement_stage", 0),
                           (assign, "$attacker_reinforcement_stage", 0),
                           (add_reinforcements_to_entry, 1, 29),
                           #SB : deathcam
                           (call_script, "script_init_death_cam"),
                           # (call_script, "script_combat_music_set_situation_with_culture"),
                            ## HOLD ON START
                           (get_player_agent_no, "$g_player"),
                           (agent_get_team, ":player_team", "$g_player"),
                           (set_show_messages, 0),
                           (team_give_order, ":player_team", grc_everyone, mordr_hold),
                           (set_show_messages, 1),
                           ## END HOLD ON START
                           ]),

      # common_music_situation_update,
      common_battle_check_friendly_kills,
      # common_battle_check_victory_condition,
  (1, 60, ti_once,
  [
    (store_mission_timer_a,reg(1)),
    (ge,reg(1),10),
    (all_enemies_defeated, 5),
    ##diplomacy begin
    (this_or_next|eq, "$g_dplmc_battle_continuation", 0),
    (neg|main_hero_fallen),
    ##diplomacy end
    (set_mission_result,1),
    (display_message,"str_msg_battle_won",message_positive),
    (assign,"$g_battle_won",1),
    (assign, "$g_battle_result", 1),
    (call_script, "script_play_victorious_sound"),
    ],
  [
    (call_script, "script_count_mission_casualties_from_agents"),
    # (finish_mission, 1),
    ]),
      # common_battle_victory_display,
  (10, 0, 0, [],
  [
    (eq,"$g_battle_won",1),
    (display_message,"@Battle won! Press tab key to leave... Don't forget to scavenge the place.",message_positive),
    ]),

      (1, 4,
      ##diplomacy begin
      0,
      ##diplomacy end
      [(main_hero_fallen)],
          [
              ##diplomacy begin
              (try_begin),
                (call_script, "script_cf_dplmc_battle_continuation"),
              (else_try),
              ##diplomacy end
              (assign, "$pin_player_fallen", 1),
              (str_store_string, s5, "str_retreat"),
              (call_script, "script_simulate_retreat", 10, 20, 1),
              (assign, "$g_battle_result", -1),
              (set_mission_result, -1),
              (call_script, "script_count_mission_casualties_from_agents"),
              (finish_mission, 0),
              ##diplomacy begin
              (try_end),
              ##diplomacy end
              ]),

      common_battle_inventory,
      # common_battle_order_panel,

      # common_gore,
    ]
    ##diplomacy begin
    + dplmc_battle_mode_triggers #+ dplmc_horse_cull #+ mod_battle_triggers #SB : horse cull
    ##diplomacy end
	# + utility_triggers + extended_battle_menu + common_division_data + division_order_processing + real_deployment + formations_triggers + mod_ai_triggers + AI_triggers
    + battle_panel_triggers,
  ),

("intro_1", mtf_battle_mode,charge,
    "Alley fight",
    [
        (0,mtef_team_0|mtef_scene_source,af_override_horse|af_override_weapons,0,1,[]),
    ], tocan_common_triggers+ #+tocan_autofire+tocan_flashlight+
    [
    common_inventory_not_available,

    (ti_tab_pressed, 0, 0,
        [
        # (try_begin),
          # # (eq, "$g_main_attacker_agent", 0),
          # (set_trigger_result, 1),
        # (else_try),
          (display_message, "str_cannot_leave_now",message_alert),
        # (try_end),

        # (jump_to_menu, "mnu_start_phase_2"),

        ], []),
    #set light
    (0, 0, ti_once, [],
        [
        # light
        (set_fixed_point_multiplier, 100),
        #thunder
        (assign, "$lightning_cycle", 0),
        (set_fixed_point_multiplier, 100),
        (get_startup_sun_light, pos20),
        (position_get_x, "$sun_r", pos20),	# r
        (position_get_y, "$sun_g", pos20), # g
        (position_get_z, "$sun_b", pos20),	# b
        (get_startup_ambient_light, pos21),
        (position_get_x, "$amb_r", pos21),	# r
        (position_get_y, "$amb_g", pos21), # g
        (position_get_z, "$amb_b", pos21),	# b
        ]),
#thunder
    (3, 0.2, 6, 			#lightning 1
        [
          (eq,"$lightning_cycle",0),
          # (store_random_in_range,":chance",1,5),
          (store_random_in_range,":chance",1,3),
          (eq,":chance",1),
          (play_sound,"snd_ambient_thunder_close"),
          (set_startup_sun_light, 1000, 1000, 1000),
          (set_startup_ambient_light, 1000, 1000, 1000),
        ],
        [
          (set_startup_sun_light, 0, 0, 0),
          (set_startup_ambient_light, 0, 0, 0),

          (assign, "$lightning_cycle",1),
      ]),
    (0.4,0.1, 6,			#lightning 2
        [
          (eq,"$lightning_cycle",1),

          (set_startup_sun_light, 220, 220, 220),
          (set_startup_ambient_light, 220, 220, 220),
        ],
        [
          (set_startup_sun_light, 1, 1, 1),
          (set_startup_ambient_light, 1, 1, 1),
          (assign,"$lightning_cycle",2),
      ]),
    (0.5,0.1, 6,			#lightning 3
        [
          (eq,"$lightning_cycle",2),
          (set_startup_sun_light, 150, 150, 150),
          (set_startup_ambient_light, 150, 150, 150),
        ],
        [
          (set_startup_sun_light, "$sun_r", "$sun_g", "$sun_b"),
          (set_startup_ambient_light, "$amb_r", "$amb_g", "$amb_b"),
          (assign,"$lightning_cycle", 0),
      ]),
    (2.5, 0, 0, #tocan: new thunder
        [
          # (eq, "$g_thunder", 1),
          (store_random_in_range,":chance",1,3),
          (eq,":chance",1),
        ],
        [
        (set_fixed_point_multiplier, 1),
        # (get_player_agent_no, "$g_player"),
        (agent_get_position, pos53, "$g_player"),
        (store_random_in_range, ":z_rot", 0, 360),
        (position_rotate_z, pos53, ":z_rot"),
        (position_set_z_to_ground_level, pos53),
        (position_move_z,pos53,1),
        (position_move_y, pos53, 100000),
        (copy_position, pos54, pos53),
        (position_move_z, pos54, 50000),
        (particle_system_burst_no_sync, "psys_upper_lightning", pos54, 1),
        (store_random_in_range, ":particle", "psys_lightning_1", "psys_upper_lightning"),
        (particle_system_burst_no_sync, ":particle", pos53, 1),
        (set_fixed_point_multiplier, 100),
      ]),
#init
    (ti_before_mission_start, 0, 0, [],
            [
            (assign,"$intro_state",0),
            (assign, "$cam_overview", 1),
            (assign, "$next_cam_agent", -1),
            (assign, "$next_cam_agent_2", -1),
            (assign, "$next_cam_agent_3", -1),
            (assign,"$starting_prop",-1),
            (assign, "$sas_loaded", 0),
            (assign, "$g_thunder", 1),

            (set_skybox, sb_skybox_night_2, sb_skybox_night_2),
            (set_rain, 1, 100),
            (scene_set_day_time, 0),
            (set_cheer_at_no_enemy, 0),
            (set_fog_distance, 250, 0x000000),

            (set_fixed_point_multiplier, 1),
            (set_shader_param_float, "@vEnvironment", shader_set_2),

            (set_fixed_point_multiplier, 100),

            ]),
    (ti_after_mission_start, 0, 0, [],
            [
            (mission_disable_talk),
            (music_set_situation, mtf_sit_main_title),
            (play_track, "track_rainy_night_in_tallinn", 2),

            ]),
#cam
    (0, 0, 0,[
            (this_or_next|eq, "$cam_overview", 1),
            (this_or_next|eq, "$cam_overview", 2),
            (eq, "$cam_overview", 3),
        ],
        [
            (store_mission_timer_a, ":cur_time"),
            (set_fixed_point_multiplier, 100),
            (get_player_agent_no, "$g_player"),

            (try_begin),
                (eq, "$cam_overview", 1),
                (mission_cam_set_mode, 1, 0, 0),
                (agent_get_position,pos84,"$g_player"),
                (position_move_y, pos84, 15000),
                (position_move_z, pos84, 5000),
                (position_rotate_y, pos84, -180),
                (position_rotate_x, pos84, 120),
                (mission_cam_set_position, pos84),

                (val_add, "$cam_overview", 1),
            (else_try),
                (eq, "$cam_overview", 2),
                (ge, ":cur_time", 1),
                (agent_get_position,pos65,"$g_player"),
                (position_rotate_z, pos65, 180),
                (position_move_y, pos65, -100),
                (position_move_z, pos65, 180),
                (mission_cam_animate_to_position, pos65, 30000, 1),

                (val_add, "$cam_overview", 1),
            (else_try),
                (eq, "$cam_overview", 3),
                (ge, ":cur_time", 31),
                (assign, "$cam_overview", 0),
                (mission_cam_set_mode, 0, 0, 0),
                # (set_camera_in_first_person, 1),
                (assign,"$intro_state",1),
                # (display_message,"@intro_state 1"),
                (agent_set_no_dynamics, "$g_player", 0),
            (try_end),
        ]),
#spawn deaths
    (0, 0, ti_once,
           [
            (eq, "$intro_state", 0),
           ],
           [
            # (get_player_agent_no, "$g_player"),

            (set_show_messages,0),
            (set_fixed_point_multiplier, 100),

            (entry_point_get_position, pos1, 2),
            (set_spawn_position, pos1),
            (spawn_agent, "trp_bandit"),
            (assign, ":agent_id", reg0),
            (agent_set_team,":agent_id",7),
            # (display_message,"@death set"),
            (agent_deliver_damage_to_agent, ":agent_id", ":agent_id", 1000),
            (spawn_item, "itm_crowbar"),

            (entry_point_get_position, pos1, 3),
            (set_spawn_position, pos1),
            (spawn_agent, "trp_bandit"),
            (assign, ":agent_id", reg0),
            (agent_set_team,":agent_id",7),
            # (display_message,"@death set"),
            (agent_deliver_damage_to_agent, ":agent_id", ":agent_id", 1000),
            (spawn_item, "itm_lead_pipe"),

            (entry_point_get_position, pos1, 4),
            (set_spawn_position, pos1),
            (spawn_agent, "trp_bandit"),
            (assign, ":agent_id", reg0),
            (agent_set_team,":agent_id",7),
            # (display_message,"@death set"),
            (agent_deliver_damage_to_agent, ":agent_id", ":agent_id", 1000),
            

            (set_show_messages,1),

           ]),
#set player ani
    (0, 0, 0,
            [
             (eq, "$intro_state", 0),
             # (get_player_agent_no, "$g_player"),
            # (agent_set_no_dynamics, "$g_player", 1),

            ],
            [
             (get_player_agent_no, "$g_player"),
                (agent_set_no_dynamics, "$g_player", 1),

            (agent_get_animation, ":animation", "$g_player", 0),
            (neq, ":animation", "anim_death_pose"),
            (agent_set_stand_animation,"$g_player","anim_death_pose", 0),
            (agent_set_stand_animation,"$g_player","anim_death_pose", 1),
            (agent_set_animation,"$g_player","anim_death_pose", 0),
            (agent_set_animation,"$g_player","anim_death_pose", 1),
            # (display_message,"@anim set"),

       ]),
#first message
    (0, 0, 0,
       [
         (eq, "$intro_state", 1),
       ],
       [
        # (get_player_agent_no, "$g_player"),
        # (agent_set_no_dynamics, "$g_player", 0),

        # (display_message,"@player active"),
        (tutorial_message_set_size, 20, 20),
        (tutorial_message_set_position, 500, 650),
        # (tutorial_message_set_center_justify, 1),
        (tutorial_message_set_center_justify, 0),
        (tutorial_message_set_background, 1),
        (tutorial_message, "@It seems I was attacked, but I just... just can't remember anything... better grab a weapon from the bodies!"),
       ]),
#first item pickup
    (ti_on_item_picked_up, 0, ti_once,
       [
       ],
       [
        (assign,"$intro_state",2),
        (tutorial_message_set_size, 20, 20),
        (tutorial_message_set_position, 500, 650),
        (tutorial_message_set_center_justify, 0),
        (tutorial_message_set_background, 1),
        (tutorial_message, "@Nothing else to find, maybe in the tent..."),

        # (tutorial_message,-1),
        # (assign,"$intro_state",2),
        (assign,"$starting_prop",1),


       ]),

    (0, 0, ti_once, [
        (eq, "$intro_state", 2),
        (eq,"$starting_prop",3),
        (eq, "$sas_loaded", 1),
        (key_clicked, key_enter)

        ],[
        (tutorial_message_set_size, 20, 20),
        (tutorial_message_set_position, 500, 650),
        (tutorial_message_set_center_justify, 0),
        (tutorial_message_set_background, 1),
        (tutorial_message, "@[To fire the gun you first have to aim, you can do this by pressing the right mouse button. ^Left click to fire. ^Shift key to use ironsights/scope.^^ Please press ENTER to continue.]"),
        (assign,"$sas_loaded",2),

        ]),
    (0, 0, ti_once, [
        (eq, "$intro_state", 2),
        (eq,"$starting_prop",3),
        (eq, "$sas_loaded", 2),

        (key_clicked, key_enter)
        ],[
        (tutorial_message,-1),

        # (start_presentation,"prsnt_vats"),
        # (start_presentation,"prsnt_particle_preview"),
        # (start_presentation,"prsnt_sas_intro"),
        # (start_mission_conversation, "trp_start"),
        (assign,"$intro_state",3),

        ]),

    (0, 0, ti_once,
       [
        (eq,"$intro_state",3),
        # (neg|is_presentation_active,"prsnt_sas_intro"),
       ],
       [
        # (get_player_agent_no, "$g_player"),
        (set_fixed_point_multiplier, 100),

        (entry_point_get_position, pos1, 1),
        (copy_position, pos2, pos1),
        (copy_position, pos3, pos1),

        (set_spawn_position, pos1),
        (spawn_agent, "trp_mr_x"),
        (assign, "$next_cam_agent", reg0),
        (agent_set_team,"$next_cam_agent",7),

        (position_move_x, pos2, -100),
        (position_move_x, pos3, 100),

        (set_spawn_position, pos2),
        (spawn_agent, "trp_the_suits"),
        (assign, "$next_cam_agent_2", reg0),
        (agent_set_team,"$next_cam_agent_2",7),
        (agent_equip_item, "$next_cam_agent_2", "itm_flashlight"),
        # (agent_equip_item, "$next_cam_agent_2", "itm_torch"),
        (agent_set_wielded_item, "$next_cam_agent_2", "itm_flashlight"),
        # (agent_set_wielded_item, "$next_cam_agent_2", "itm_torch"),

        (set_spawn_position, pos3),
        (spawn_agent, "trp_the_suits"),
        (assign, "$next_cam_agent_3", reg0),
        (agent_set_team,"$next_cam_agent_3",7),
        (agent_equip_item, "$next_cam_agent_3", "itm_flashlight"),
        # (agent_equip_item, "$next_cam_agent_3", "itm_torch"),
        (agent_set_wielded_item, "$next_cam_agent_3", "itm_flashlight"),
        # (agent_set_wielded_item, "$next_cam_agent_3", "itm_torch"),

        # (display_message,"@bandit set"),
        # (agent_set_no_dynamics, "$g_player", 1),
        (tutorial_message,-1),
        (assign,"$intro_state",4),

       ]),

#cam move to mr. x
    (0,2,ti_once,[
        (eq,"$intro_state",4),
        ],
        [
        (set_fixed_point_multiplier, 100),

        (get_player_agent_no, "$g_player"),

        (agent_get_position, pos89, "$next_cam_agent"),
        # (position_move_y, pos89, 250),
        (position_move_y, pos89, 180),
        (position_move_z, pos89, 180),
        (position_rotate_z, pos89, 180),

        (mission_cam_set_mode, 1, 0, 0),
        (agent_set_no_dynamics, "$g_player", 1),
        (mission_cam_animate_to_position, pos89, 5000, 1),
        (assign,"$intro_state",5),

        ]),
#mr x first message
    (0,8,ti_once,[
        (eq,"$intro_state",5),
        ],
        [
        (set_fixed_point_multiplier, 100),

        # (get_player_agent_no, "$g_player"),

        (tutorial_message_set_size, 20, 20),
        (tutorial_message_set_position, 500, 650),
        (tutorial_message_set_center_justify, 0),
        (tutorial_message_set_background, 1),
        (tutorial_message, "@Unknown: Bring {him/her} to me alive!",red),

        (assign,"$intro_state",6),

        ]),
#spawn riffraff
    (0,4,ti_once,[
        (eq,"$intro_state",6),
        ],
        [
        (set_fixed_point_multiplier, 100),

        (get_player_agent_no, "$g_player"),

        (tutorial_message,-1),
        (mission_cam_set_mode, 0, 0, 0),
        (agent_set_no_dynamics, "$g_player", 0),

        # (agent_get_position, pos1, "$g_player"),

        (try_for_range,":unused",0,3),
            (agent_get_position, pos1, "$g_player"),
            (store_random_in_range,":rn_y",2000,3500),
            (store_random_in_range,":rn_z",0,361),
            (position_rotate_z, pos1,":rn_z"),
            (position_move_y, pos1, ":rn_y"), #200

            (set_spawn_position, pos1),
            (spawn_agent, "trp_bandit"),
            (assign, ":agent_id", reg0),
            (agent_set_team,":agent_id",1),
            (agent_set_is_alarmed,":agent_id",1),
            (try_for_range, ":item_slot", ek_item_0, ek_head),
               (agent_get_item_slot,  ":item", ":agent_id", ":item_slot"),

               (gt, ":item", itm_no_item),
               # (item_get_type, ":type", ":item"),
               # (this_or_next|eq,itp_type_bow,":type",),
               # (this_or_next|eq,itp_type_crossbow,":type",),
               # (this_or_next|eq,itp_type_thrown,":type",),
               # (this_or_next|eq,itp_type_pistol,":type",),
               # (eq,itp_type_musket,":type",),

               (agent_unequip_item, ":agent_id", ":item"),
            (try_end),

            (agent_equip_item, ":agent_id", "itm_club"),
            (agent_set_wielded_item, ":agent_id", "itm_club"),
        (try_end),

        # (display_message,"@enemy set"),
        (assign,"$intro_state",7),

        ]),
#reinforcement for riffraff
    (0.1,0,0,[
        (eq,"$intro_state",7),
        ],
        [
        (set_fixed_point_multiplier, 100),
        (assign,":enemy_count",0),
        (try_for_agents, ":cur_agent"),
             (agent_is_human, ":cur_agent"),
             (agent_is_alive, ":cur_agent"),
             (agent_get_team, ":cur_team", ":cur_agent"),
             (eq, ":cur_team", 1),
             (val_add, ":enemy_count", 1),
        (try_end),
        (lt,":enemy_count", 3),
         # (display_message,"@enemy reinforcement"),

        (get_player_agent_no, "$g_player"),

        (agent_get_position, pos1, "$g_player"),

        (store_random_in_range,":rn_y",2000,3500),
        (store_random_in_range,":rn_z",0,361),
        (position_rotate_z, pos1,":rn_z"),
        (position_move_y, pos1, ":rn_y"), #200

        (set_spawn_position, pos1),
        (spawn_agent, "trp_bandit"),
        (assign, ":agent_id", reg0),
        (agent_set_team,":agent_id",1),
        (agent_set_is_alarmed,":agent_id",1),
        (try_for_range, ":item_slot", ek_item_0, ek_head),
           (agent_get_item_slot,  ":item", ":agent_id", ":item_slot"),

           (gt, ":item", itm_no_item),
           (item_get_type, ":type", ":item"),
           (this_or_next|eq,itp_type_bow,":type",),
           #(this_or_next|eq,itp_type_crossbow,":type",),
           (this_or_next|eq,itp_type_thrown,":type",),
           (this_or_next|eq,itp_type_pistol,":type",),
           (eq,itp_type_musket,":type",),

           (agent_unequip_item, ":agent_id", ":item"),
        (try_end),

        (agent_equip_item, ":agent_id", "itm_club"),
        (agent_set_wielded_item, ":agent_id", "itm_club"),

        ]),
#player defeated
    (1, 0, ti_once,
       [
        (main_hero_fallen),
       ],
       [
        (set_fixed_point_multiplier, 100),

        (mission_cam_animate_to_screen_color, 0xFF000000, 1),
        # (display_message,"@knocked!"),

        (get_player_agent_no, "$g_player"),
        # (agent_get_position, pos1, "$g_player"),
        (entry_point_get_position, pos1, 2),
        (agent_set_position, "$next_cam_agent_2", pos1),
        (agent_equip_item, "$next_cam_agent_2", "itm_torch"),
        (agent_set_wielded_item, "$next_cam_agent_2", "itm_torch"),

        (entry_point_get_position, pos1, 3),
        (agent_set_position, "$next_cam_agent", pos1),

        (entry_point_get_position, pos1, 4),
        (agent_set_position, "$next_cam_agent_3", pos1),
        (agent_equip_item, "$next_cam_agent_3", "itm_torch"),
        (agent_set_wielded_item, "$next_cam_agent_3", "itm_torch"),

        (entry_point_get_position, pos1, 5),
        (agent_set_position, "$g_player", pos1),

        (agent_set_visibility, "$g_player", 0),

        # (position_move_y, pos1, -100),
        # (agent_set_position, "$next_cam_agent", pos1),
        # (copy_position, pos2, pos1),
        # (copy_position, pos3, pos1),

        # (position_move_x, pos2, -100),
        # (position_move_x, pos3, 100),
        # (agent_set_position, "$next_cam_agent_2", pos2),
        # (agent_set_position, "$next_cam_agent_3", pos3),

        (try_for_agents, ":agent_id"),
            (neq,":agent_id","$g_player"),
            (neq,":agent_id","$next_cam_agent"),
            (neq,":agent_id","$next_cam_agent_2"),
            (neq,":agent_id","$next_cam_agent_3"),
            # (agent_is_human, ":agent_id"),
            # (agent_is_alive, ":agent_id"),
            # (agent_get_team, ":cur_team", ":agent_id"),
            # (eq, ":cur_team", 1),
            (entry_point_get_position, pos1, 1),

            # (agent_get_position, pos1, ":agent_id"),
            # (position_move_y, pos1, -350),
            (agent_set_position, ":agent_id", pos1),
            # (agent_get_wielded_item, ":wielded_item", ":agent_id", 0),
            # (gt, ":wielded_item", 0),
            # (neq, ":wielded_item", "itm_torch"),
            # (agent_equip_item, ":agent_id", "itm_torch"),
            # (agent_set_wielded_item, ":agent_id", "itm_torch"),
        (try_end),
        (mission_cam_set_mode, 1, 0, 0),

        (assign,"$intro_state",8),
        ]),
#mr x vs player message
    (0, 5, 0,
       [
        (eq,"$intro_state",8),
       ],
       [

        (agent_get_position, pos89, "$next_cam_agent"),
        (position_move_y, pos89, 180),
        (position_move_z, pos89, 180),
        (position_rotate_z, pos89, 180),
        (mission_cam_set_position, pos89),
        (mission_cam_animate_to_screen_color, 0x00000000, 1500),

        (tutorial_message_set_size, 20, 20),
        (tutorial_message_set_position, 500, 650),
        (tutorial_message_set_center_justify, 0),
        (tutorial_message_set_background, 1),
        (tutorial_message, "@Bandit: Is {he/she} the one Vinny?^^Vinny: Finally! We've been searching all over Acron for that head! You've brought us nothing but trouble.",red),
        # (tutorial_message, "@Bandit: Is {he/she} the one Vinny?^^Vinny: Finally! We've been searching all over Acron for that head! You've brought us nothing but trouble, so I'm more than happy to do what I do next.",red),
        (assign,"$intro_state",9),
       ]),
# #mr. x die message
    # (0, 10, 0,
       # [
        # (eq,"$intro_state",9),
       # ],
       # [
        # (agent_equip_item, "$next_cam_agent", "itm_ai_pistol_sw_model_500"),
        # (agent_set_wielded_item, "$next_cam_agent", "itm_ai_pistol_sw_model_500"),
        # (agent_set_animation, "$next_cam_agent", "anim_ready_pistol"),
        # (tutorial_message, "@Vinny: Time to die!",red),
        # (assign,"$intro_state",10),
       # ]),
# #mr. x shoot
    # (0, 5, ti_once,
       # [
        # (eq,"$intro_state",10),
       # ],
       # [
        # (tutorial_message,-1),
        # (agent_set_attack_action, "$next_cam_agent", 0, 0),
        # (mission_cam_animate_to_screen_color, 0xFF000000, 5000),
        # (assign,"$intro_state",11),
       # ]),
#mr. x shoot
    (0, 6, ti_once,
       [
        (eq,"$intro_state",9),
       ],
       [
        (tutorial_message,-1),
        # (agent_set_attack_action, "$next_cam_agent", 0, 0),
        (mission_cam_animate_to_screen_color, 0xFF000000, 4500),
        (assign,"$intro_state",10),
       ]),
#end
    (0, 6, ti_once,
       [
            (eq,"$intro_state",10),
       ],
       [
               (assign, "$current_startup_quest_phase", 1),

         (change_screen_return),
         (set_trigger_result, 1),
        (finish_mission),
         # (display_message,"@end"),
       ]),

     ]),

("intro_2", mtf_battle_mode,charge,
    "Alley fight",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (1,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (2,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (3,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (4,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (5,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (6,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (7,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (8,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (9,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
    ], tocan_common_triggers+ #+tocan_autofire+tocan_flashlight+
    [
    common_inventory_not_available,

#init
    (ti_before_mission_start, 0, 0, [],[
            (troop_get_inventory_capacity, ":inv_size", "trp_player"),
            (try_for_range, ":item_slot", 0, ":inv_size"),
              (troop_get_inventory_slot, ":item_no", "trp_player", ":item_slot"),
              (ge, ":item_no",0),
              (troop_set_inventory_slot, "trp_player", ":item_slot", -1),
            (try_end),
            (troop_set_inventory_slot, "trp_player", ek_item_0, "itm_stones_alt"),
            (troop_set_inventory_slot, "trp_player", ek_body, "itm_poor_shirt_1"),

            (assign,"$intro_state",0),
            (assign, "$g_thunder", 0),
            (assign, "$all_doors_locked", 1),
            (mission_enable_talk),

            (set_rain, 0),
            (scene_set_day_time, 0),
            (set_cheer_at_no_enemy, 0),
            (set_global_haze_amount, 100),
            (set_fog_distance, 20, 0x252525),

            (set_fixed_point_multiplier, 1),
            (set_shader_param_float, "@vEnvironment", shader_set_1),

            (set_fixed_point_multiplier, 100),

            ]),
    (ti_after_mission_start, 0, 0, [],
            [
            (agent_set_wielded_item, "$g_player", -1),

            (mission_cam_set_screen_color, 0xFF000000),
            (mission_cam_animate_to_screen_color, 0x00000000, 7500),
            ]),
    (ti_tab_pressed, 0, 0,
        [
        # (try_begin),
          # # (eq, "$g_main_attacker_agent", 0),
          # (set_trigger_result, 1),
        # (else_try),
          (display_message, "str_cannot_leave_now",message_alert),
        # (try_end),
        # (jump_to_menu, "mnu_start_phase_2"),

        ], []),
      # (ti_tab_pressed, 0, 0, [],
       # [(question_box,"str_do_you_want_to_retreat"),
        # ]),
      # (ti_question_answered, 0, 0, [],
       # [(store_trigger_param_1,":answer"),
        # (eq,":answer",0),
        # # (jump_to_menu, "mnu_collect_taxes_failed"),
        # (finish_mission),]),

    (ti_on_agent_killed_or_wounded, 0, 0, [],
     [
      (store_trigger_param_1, ":agent_id"),
      (agent_is_human, ":agent_id"),
      (agent_get_troop_id, ":agent_troop_id", ":agent_id"),
      (try_begin),
        (this_or_next|eq, ":agent_id", "$g_player"),
        (main_hero_fallen),#should be same

        (jump_to_menu, "mnu_start_phase_2"),
        # (call_script, "script_fail_quest", "qst_hunt_down_fugitive"), #do this from menu so we can reuse it
        (finish_mission, 4),
      (else_try),
        (eq,":agent_troop_id","trp_intro_prisoner"),

        (assign,"$intro_state",3),
        (assign, "$all_doors_locked", 0),

        (agent_get_position, pos1, "$g_player"),
        (set_spawn_position, pos1),
        (spawn_item, "itm_knife"),

        (tutorial_box, "@You search the dead body and find keys, likely for the cell door. It seems he was no real prisoner, but probably one of your kidnappers. They thought they could trick you to uncover your secret...."),
        (display_message,"@You got the key of the cell door."),
      (try_end),
     ]),
    (ti_on_agent_hit, 0, 0,
      [], [
      (store_trigger_param_1, ":inflicted"),
      (store_trigger_param_3, ":damage"),
      (neg|agent_is_non_player, ":inflicted"),

      (store_agent_hit_points, ":inflicted_hp", ":inflicted", 1),
      (store_sub, ":inflicted_new_hp", ":inflicted_hp", ":damage"),
      (le, ":inflicted_new_hp", 1),
      (set_trigger_result, 0),
	   ]),

    (ti_on_item_picked_up, 0, ti_once,
       [],
       [
        (store_trigger_param_1, ":agent_id"),
        (store_trigger_param_2, ":weapon"),

        (try_for_range, ":item_slot", ek_item_0, ek_horse),
          (agent_get_item_slot, ":item_no", ":agent_id", ":item_slot"),
          (gt, ":item_no", -1),
          (eq, ":item_no", ":weapon"),
          (troop_set_inventory_slot, "trp_player", ":item_slot", ":item_no"),
        (try_end),
       ])

     ]),

("intro_3", mtf_battle_mode,charge,
    "Alley fight",
    [
      (0,mtef_team_0|mtef_scene_source,af_override_horse,0,1,[]),
    ], tocan_common_triggers+ #+tocan_autofire+tocan_flashlight+
    [
    common_inventory_not_available,

#init
    (ti_before_mission_start, 0, 0, [],[
      (assign,"$intro_state",0),
      (assign, "$g_thunder", 0),
      (assign, "$next_cam_agent", -1),
      (assign, "$next_cam_agent_2", -1),
      (assign, "$next_cam_agent_3", -1),
      (assign, "$next_cam_agent_4", -1),
      (assign, "$next_cam_agent_5", -1),
      (assign, "$next_cam_agent_6", -1),
      (assign, "$next_cam_agent_7", -1),
      (assign, "$next_cam_agent_8", -1),
      (assign, "$next_cam_agent_9", -1),
      (assign, "$current_startup_quest_phase", 2),

      (mission_disable_talk),

      (set_rain, 0),
      (scene_set_day_time, 12),
      (set_cheer_at_no_enemy, 0),
      (set_global_haze_amount, 100),
      (set_fog_distance, 15, 0x303030),

      (set_fixed_point_multiplier, 1),
      (set_shader_param_float, "@vEnvironment", shader_set_1),

      (set_fixed_point_multiplier, 100),

    ]),
    (0, 1.5, ti_once, [], [
      (tutorial_box, "@Try to find a way out of the prison.", "@Objective"),
    ]),
    (0, 0, ti_once,
       [
        # (eq,"$intro_state",3),
        # (neg|is_presentation_active,"prsnt_sas_intro"),
       ],
       [

        # (get_player_agent_no, "$g_player"),
        (set_fixed_point_multiplier, 100),

        (try_begin),
          (entry_point_get_position, pos1, 2),

          (set_spawn_position, pos1),
          (spawn_agent, "trp_bandit"),
          (assign, "$next_cam_agent", reg0),
          # (agent_set_team,"$next_cam_agent",1),

          (try_for_range, ":item_slot", ek_item_0, ek_head),
             (agent_get_item_slot,  ":item", "$next_cam_agent", ":item_slot"),

             (gt, ":item", itm_no_item),
             (agent_unequip_item, "$next_cam_agent", ":item"),
          (try_end),
          (agent_equip_item, "$next_cam_agent", "itm_club"),
          (agent_set_wielded_item, "$next_cam_agent", "itm_club"),

          (agent_set_max_hit_points, "$next_cam_agent", 5, 1),
        (try_end),
        (try_begin),
          (entry_point_get_position, pos1, 4),

          (set_spawn_position, pos1),
          (spawn_agent, "trp_bandit"),
          (assign, "$next_cam_agent_2", reg0),
          # (agent_set_team,"$next_cam_agent_2",1),

          (try_for_range, ":item_slot", ek_item_0, ek_head),
             (agent_get_item_slot,  ":item", "$next_cam_agent_2", ":item_slot"),

             (gt, ":item", itm_no_item),
             (agent_unequip_item, "$next_cam_agent_2", ":item"),
          (try_end),
          (agent_equip_item, "$next_cam_agent_2", "itm_torch"),
          (agent_set_wielded_item, "$next_cam_agent_2", "itm_torch"),
        (try_end),
        (try_begin),
          (entry_point_get_position, pos1, 5),

          (set_spawn_position, pos1),
          (spawn_agent, "trp_bandit"),
          (assign, "$next_cam_agent_9", reg0),
          # (agent_set_team,"$next_cam_agent_2",1),
        (try_end),
        (try_begin),
          (entry_point_get_position, pos1, 3),
          (copy_position, pos2, pos1),
          (copy_position, pos3, pos1),
          (copy_position, pos4, pos1),
          (copy_position, pos5, pos1),
          (copy_position, pos6, pos1),
          (set_spawn_position, pos1),
          (spawn_agent, "trp_bandit"),
          (assign, "$next_cam_agent_3", reg0),
          # (agent_set_team,"$next_cam_agent_3",1),
        (try_end),

        (position_move_x, pos2, -200),
        (position_move_x, pos3, 200),
        (position_move_y, pos4, 200),
        (position_move_y, pos5, -200),
        (position_move_x, pos6, 200),
        (position_move_y, pos6, 200),

        (set_spawn_position, pos2),
        (spawn_agent, "trp_bandit"),
        (assign, "$next_cam_agent_4", reg0),
        (set_spawn_position, pos3),
        (spawn_agent, "trp_bandit"),
        (assign, "$next_cam_agent_5", reg0),
        (set_spawn_position, pos4),
        (spawn_agent, "trp_bandit"),
        (assign, "$next_cam_agent_6", reg0),
        (set_spawn_position, pos5),
        (spawn_agent, "trp_bandit"),
        (assign, "$next_cam_agent_7", reg0),
        (set_spawn_position, pos6),
        (spawn_agent, "trp_bandit"),
        (assign, "$next_cam_agent_8", reg0),


        (try_for_agents, ":cur_agent"),
          (agent_is_human, ":cur_agent"),
          (agent_is_alive, ":cur_agent"),
          (agent_is_non_player, ":cur_agent"),

          # remove ranged weapons for this mission
          (try_for_range, ":item_slot", ek_item_0, ek_head),
             (agent_get_item_slot,  ":item", ":cur_agent", ":item_slot"),
             (gt, ":item", itm_no_item),
             (this_or_next|eq, ":item", "itm_throwing_knives"),
             (eq, ":item", "itm_darts"),
             (agent_unequip_item, ":cur_agent", ":item"),
          (try_end),

          (agent_set_team,":cur_agent",1),

          (agent_add_relation_with_agent, ":cur_agent", "$g_player", 1),

          (store_random_in_range,":animation","anim_stand_townguard","anim_wedding_guest"),
          (agent_set_stand_animation, ":cur_agent", ":animation"),
          (agent_set_animation, ":cur_agent", ":animation"),
          (assign,":end",1),
          (convert_to_fixed_point,":end"),
          (store_random_in_range,":progress",0,":end"),
          (agent_set_animation_progress,":cur_agent",":progress"),
        (try_end),


       ]),

    (ti_tab_pressed, 0, 0,
        [
        # (try_begin),
          # # (eq, "$g_main_attacker_agent", 0),
          # (set_trigger_result, 1),
        # (else_try),
          (display_message, "str_cannot_leave_now",message_alert),
        # (try_end),

        # (jump_to_menu, "mnu_start_phase_2"),

        ], []),
      # (ti_tab_pressed, 0, 0, [],
       # [(question_box,"str_do_you_want_to_retreat"),
        # ]),
      # (ti_question_answered, 0, 0, [],
       # [(store_trigger_param_1,":answer"),
        # (eq,":answer",0),
        # # (jump_to_menu, "mnu_collect_taxes_failed"),
        # (finish_mission),]),

    (0.1, 0, 0, [],
            [
            # (agent_get_bone_position, pos1, "$g_player", hb_thorax, 1),
            (mission_cam_get_position, pos1),

            (try_for_agents, ":cur_agent"),
               (agent_is_human, ":cur_agent"),
               (agent_is_alive, ":cur_agent"),
               (agent_is_non_player, ":cur_agent"),
               (agent_get_team, ":cur_team", ":cur_agent"),
               (eq, ":cur_team", 1),
               # (agent_get_position,pos2,":cur_agent"),
               # (agent_get_bone_position, pos1, ":cur_agent", hb_thorax, 1),

              (agent_get_position, pos2, ":cur_agent"),
              (position_move_z, pos2, 145),

              (get_distance_between_positions, ":dist", pos2, pos1),
              (le,":dist",1500),
              (position_has_line_of_sight_to_position, pos1, pos2),
              # (display_message,"@should fire"),
              (agent_clear_relations_with_agents,":cur_agent"),
              (agent_ai_set_aggressiveness, ":cur_agent", 300),

              # (try_begin),
                # (neq,":cur_agent","$next_cam_agent"),
                # (neq,":cur_agent","$next_cam_agent_2"),
                # (neq,":cur_agent","$next_cam_agent_9"),
                # (try_for_agents, ":cur_agent"),
                   # (agent_is_human, ":cur_agent"),
                   # (agent_is_alive, ":cur_agent"),
                   # (agent_is_non_player, ":cur_agent"),
                   # (agent_get_team, ":cur_team", ":cur_agent"),
                   # (eq, ":cur_team", 1),
                   # # (agent_get_position,pos2,":cur_agent"),
                   # # (agent_get_bone_position, pos1, ":cur_agent", hb_thorax, 1),
                  # (agent_clear_relations_with_agents,":cur_agent"),
                  # (agent_ai_set_aggressiveness, ":cur_agent", 199),
                # (try_end),
              # (try_end),
            (try_end),

            ]),

    (ti_on_agent_killed_or_wounded, 0, 0, [],
     [
      (store_trigger_param_1, ":agent_id"),
      (agent_is_human, ":agent_id"),
      # (agent_get_troop_id, ":agent_troop_id", ":agent_id"),
      # (try_begin),
        (this_or_next|eq, ":agent_id", "$g_player"),
        (main_hero_fallen),#should be same

        (jump_to_menu, "mnu_start_phase_2"),
        # (call_script, "script_fail_quest", "qst_hunt_down_fugitive"), #do this from menu so we can reuse it
        (mission_cam_animate_to_screen_color, 0xFF000000, 3000),
        (finish_mission, 4),
      # (else_try),
        # (eq,":agent_troop_id","trp_intro_prisoner"),

        # (assign,"$intro_state",3),
        # (assign, "$all_doors_locked", 0),

        # (spawn_item, "itm_knife"),

        # (display_message,"@You got the key of the cell door."),
      # (try_end),
     ]),

    (ti_on_agent_hit, 0, 0,
      [
      (store_trigger_param_1, ":cur_agent"),

       (agent_get_team, ":cur_team", ":cur_agent"),
       (eq, ":cur_team", 1),

      (agent_clear_relations_with_agents,":cur_agent"),
      (agent_ai_set_aggressiveness, ":cur_agent", 199),
	   ], [
	   ]),

    (ti_on_item_picked_up, 0, ti_once,
       [],
       [
        (store_trigger_param_1, ":agent_id"),
        (store_trigger_param_2, ":weapon"),

        (try_for_range, ":item_slot", ek_item_0, ek_horse),
          (agent_get_item_slot, ":item_no", ":agent_id", ":item_slot"),
          (gt, ":item_no", -1),
          (eq, ":item_no", ":weapon"),
          (troop_set_inventory_slot, "trp_player", ":item_slot", ":item_no"),
        (try_end),
       ])
   ]),

("intro_3b", mtf_battle_mode,charge,
    "Alley fight",
    [
      (0,mtef_team_0|mtef_scene_source,af_override_horse,0,1,[]),
    ], tocan_common_triggers+ #+tocan_autofire+tocan_flashlight+
    [
    common_inventory_not_available,

#init
    (ti_before_mission_start, 0, 0, [],
            [
            (assign,"$intro_state",0),
            (assign, "$g_thunder", 0),
            (assign, "$current_startup_quest_phase", 3),

            (mission_disable_talk),

            (set_rain, 0),
            (scene_set_day_time, 12),
            (set_cheer_at_no_enemy, 0),
            (set_global_haze_amount, 100),
            (set_fog_distance, 30, 0x303030),

            (set_fixed_point_multiplier, 1),
            (set_shader_param_float, "@vEnvironment", shader_set_1),

            (set_fixed_point_multiplier, 100),

            ]),

     (0, 0, ti_once,
       [
        # (eq,"$intro_state",3),
        # (neg|is_presentation_active,"prsnt_sas_intro"),
       ],
       [
        # (get_player_agent_no, "$g_player"),
        (set_fixed_point_multiplier, 100),

        # (try_begin),
          # (entry_point_get_position, pos1, 2),

          # (set_spawn_position, pos1),
          # (spawn_agent, "trp_bandit"),
          # (assign, "$next_cam_agent", reg0),
          # # (agent_set_team,"$next_cam_agent",1),

          # (agent_equip_item, "$next_cam_agent", "itm_club"),
          # (agent_set_wielded_item, "$next_cam_agent", "itm_club"),
          # (agent_set_max_hit_points, "$next_cam_agent", 5, 1),
        # (try_end),
        (try_begin),
          (entry_point_get_position, pos1, 4),

          (set_spawn_position, pos1),
          (spawn_agent, "trp_bandit"),
          (assign, "$next_cam_agent_2", reg0),
          # (agent_set_team,"$next_cam_agent_2",1),

          (try_for_range, ":item_slot", ek_item_0, ek_head),
             (agent_get_item_slot,  ":item", "$next_cam_agent_2", ":item_slot"),

             (gt, ":item", itm_no_item),
             (agent_unequip_item, "$next_cam_agent_2", ":item"),
          (try_end),
          (agent_equip_item, "$next_cam_agent_2", "itm_torch"),
          (agent_set_wielded_item, "$next_cam_agent_2", "itm_torch"),
        (try_end),
        (try_begin),
          (entry_point_get_position, pos1, 5),

          (set_spawn_position, pos1),
          (spawn_agent, "trp_bandit"),
          (assign, "$next_cam_agent_9", reg0),
          # (agent_set_team,"$next_cam_agent_2",1),
          (try_for_range, ":item_slot", ek_item_0, ek_head),
             (agent_get_item_slot,  ":item", "$next_cam_agent_9", ":item_slot"),

             (gt, ":item", itm_no_item),
             (agent_unequip_item, "$next_cam_agent_9", ":item"),
          (try_end),
          (agent_equip_item, "$next_cam_agent_9", "itm_spiked_club"),
          (agent_set_wielded_item, "$next_cam_agent_9", "itm_spiked_club"),
        (try_end),
        (try_begin),
          (entry_point_get_position, pos1, 3),
          (copy_position, pos2, pos1),
          (copy_position, pos3, pos1),
          (copy_position, pos4, pos1),
          (copy_position, pos5, pos1),
          (copy_position, pos6, pos1),
          (set_spawn_position, pos1),
          (spawn_agent, "trp_bandit"),
          (assign, "$next_cam_agent_3", reg0),
          # (agent_set_team,"$next_cam_agent_3",1),
          (try_for_range, ":item_slot", ek_item_0, ek_head),
             (agent_get_item_slot,  ":item", "$next_cam_agent_3", ":item_slot"),

             (gt, ":item", itm_no_item),
             (agent_unequip_item, "$next_cam_agent_3", ":item"),
          (try_end),
          (agent_equip_item, "$next_cam_agent_3", "itm_hatchet"),
          (agent_set_wielded_item, "$next_cam_agent_3", "itm_hatchet"),
        (try_end),


      (try_for_agents, ":cur_agent"),
          (agent_is_human, ":cur_agent"),
          (agent_is_alive, ":cur_agent"),
          (agent_is_non_player, ":cur_agent"),

          # remove ranged weapons for this mission
          (try_for_range, ":item_slot", ek_item_0, ek_head),
             (agent_get_item_slot,  ":item", ":cur_agent", ":item_slot"),
             (gt, ":item", itm_no_item),
             (this_or_next|eq, ":item", "itm_throwing_knives"),
             (eq, ":item", "itm_darts"),
             (agent_unequip_item, ":cur_agent", ":item"),
          (try_end),

          (agent_set_team,":cur_agent",1),

          (agent_add_relation_with_agent, ":cur_agent", "$g_player", 1),

          (store_random_in_range,":animation","anim_stand_townguard","anim_wedding_guest"),
          (agent_set_stand_animation, ":cur_agent", ":animation"),
          (agent_set_animation, ":cur_agent", ":animation"),
          (assign,":end",1),
          (convert_to_fixed_point,":end"),
          (store_random_in_range,":progress",0,":end"),
          (agent_set_animation_progress,":cur_agent",":progress"),
        (try_end),
      ]),


    (ti_tab_pressed, 0, 0,
        [
        # (try_begin),
          # # (eq, "$g_main_attacker_agent", 0),
          # (set_trigger_result, 1),
        # (else_try),
          (display_message, "str_cannot_leave_now",message_alert),
        # (try_end),

        # (jump_to_menu, "mnu_start_phase_2"),

        ], []),
      # (ti_tab_pressed, 0, 0, [],
       # [(question_box,"str_do_you_want_to_retreat"),
        # ]),
      # (ti_question_answered, 0, 0, [],
       # [(store_trigger_param_1,":answer"),
        # (eq,":answer",0),
        # # (jump_to_menu, "mnu_collect_taxes_failed"),
        # (finish_mission),]),

    (0, 0, ti_once, [],
            [

      (try_for_agents, ":cur_agent"),
          (agent_is_human, ":cur_agent"),
          (agent_is_alive, ":cur_agent"),
          (agent_is_non_player, ":cur_agent"),

          (agent_set_team,":cur_agent",1),

          (agent_add_relation_with_agent, ":cur_agent", "$g_player", 1),

          (agent_set_stand_animation, ":cur_agent", "anim_stand_townguard"),
          (agent_set_animation, ":cur_agent", "anim_stand_townguard"),
          (assign,":end",1),
          (convert_to_fixed_point,":end"),
          (store_random_in_range,":progress",0,":end"),
          (agent_set_animation_progress,":cur_agent",":progress"),
        (try_end),
            ]),

    (0.1, 0, 0, [],
            [
            # (agent_get_bone_position, pos1, "$g_player", hb_thorax, 1),
            (mission_cam_get_position, pos1),

            (try_for_agents, ":cur_agent"),
               (agent_is_human, ":cur_agent"),
               (agent_is_alive, ":cur_agent"),
               (agent_is_non_player, ":cur_agent"),
               (agent_get_team, ":cur_team", ":cur_agent"),
               (eq, ":cur_team", 1),
               # (agent_get_position,pos2,":cur_agent"),
               # (agent_get_bone_position, pos1, ":cur_agent", hb_thorax, 1),

              (agent_get_position, pos2, ":cur_agent"),
              (position_move_z, pos2, 145),

              (get_distance_between_positions, ":dist", pos2, pos1),
              (le,":dist",1000),
              (position_has_line_of_sight_to_position, pos1, pos2),
              # (display_message,"@should fire"),
              (agent_clear_relations_with_agents,":cur_agent"),

                # (agent_set_team, ":cur_agent", 1),
              # (assign, "$g_main_attacker_agent", ":cur_agent"),
              (agent_ai_set_aggressiveness, ":cur_agent", 199),
            (try_end),

            ]),

    (ti_on_agent_killed_or_wounded, 0, 0, [],
     [
      (store_trigger_param_1, ":agent_id"),
      (agent_is_human, ":agent_id"),
      # (agent_get_troop_id, ":agent_troop_id", ":agent_id"),
      # (try_begin),
        (this_or_next|eq, ":agent_id", "$g_player"),
        (main_hero_fallen),#should be same

        (jump_to_menu, "mnu_start_phase_2"),
        # (call_script, "script_fail_quest", "qst_hunt_down_fugitive"), #do this from menu so we can reuse it
        (mission_cam_animate_to_screen_color, 0xFF000000, 3000),
        (finish_mission, 4),
      # (else_try),
        # (eq,":agent_troop_id","trp_intro_prisoner"),

        # (assign,"$intro_state",3),
        # (assign, "$all_doors_locked", 0),

        # (spawn_item, "itm_knife"),

        # (display_message,"@You got the key of the cell door."),
      # (try_end),
     ]),

    (ti_on_agent_hit, 0, 0,
      [
      (store_trigger_param_1, ":cur_agent"),

       (agent_get_team, ":cur_team", ":cur_agent"),
       (eq, ":cur_team", 1),

      (agent_clear_relations_with_agents,":cur_agent"),
      (agent_ai_set_aggressiveness, ":cur_agent", 199),
	   ], [
	   ]),

    (ti_on_item_picked_up, 0, ti_once,
       [],
       [
        (store_trigger_param_1, ":agent_id"),
        (store_trigger_param_2, ":weapon"),

        (try_for_range, ":item_slot", ek_item_0, ek_horse),
          (agent_get_item_slot, ":item_no", ":agent_id", ":item_slot"),
          (gt, ":item_no", -1),
          (eq, ":item_no", ":weapon"),
          (troop_set_inventory_slot, "trp_player", ":item_slot", ":item_no"),
        (try_end),
       ])
   ]),

("intro_final", mtf_battle_mode, -1,
    "Alley fight",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
      (1,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
    ], tocan_common_triggers+ #+tocan_autofire+tocan_flashlight+
    [
    common_inventory_not_available,

    #init
    (ti_before_mission_start, 0, 0, [],[
        (assign,"$intro_state",0),
        (assign, "$g_thunder", 0),
        (assign, "$current_startup_quest_phase", 3),

        (mission_disable_talk),

        (set_rain, 0),
        (scene_set_day_time, 18),
        (set_cheer_at_no_enemy, 0),
        (set_global_haze_amount, 0),
        # (set_fog_distance, 30, 0x303030),

        (set_fixed_point_multiplier, 1),
        (set_shader_param_float, "@vEnvironment", shader_set_1),

        (set_fixed_point_multiplier, 100),

      ]),

      (1, 0, ti_once, [
        (get_player_agent_no,":player_agent"),
        (agent_is_active, ":player_agent"),
        (agent_get_position,pos15,":player_agent"),
        (set_fixed_point_multiplier, 100),
        (assign,":continue",0),
        (try_for_agents, ":cur_agent"),
            (agent_is_alive,":cur_agent"),
            (agent_is_human,":cur_agent"),
            (agent_get_troop_id, ":troop", ":cur_agent"),
            (eq, ":troop", "trp_mr_x"),
            (agent_get_position, pos16, ":cur_agent"),
            (get_distance_between_positions,":distance",pos15,pos16),
            (le,":distance",750),
            (assign,":continue",1),
        (try_end),
        (eq,":continue",1),
        (mission_enable_talk),
      ],[
        (start_mission_conversation, "trp_mr_x"),
      ]),

    (0, 0, ti_once, [
      (main_hero_fallen),#should be same
    ],[
      (jump_to_menu, "mnu_start_phase_2"),
      (mission_cam_animate_to_screen_color, 0xFF000000, 3000),
      (finish_mission, 4),
    ]),

  ]),

("just_a_dungeon",mtf_battle_mode,charge,
    "You lead your men to battle.",
    [(1,mtef_team_0|mtef_use_exact_number,af_override_horse,aif_start_alarmed,4,[]),
     (4,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # ], tocan_ambience+tocan_common_triggers+tocan_battle_triggers+
     ], tocan_ambience+tocan_common_triggers+tocan_battle_triggers+tocan_autofire+tocan_flashlight+

    [
      common_inventory_not_available,

      common_battle_init_banner,

      (ti_before_mission_start, 0, 0, [
        (store_random_in_range,":distance",50,251),
        (set_fog_distance, ":distance", 0x232323),
      ], []),

      (ti_after_mission_start, 0, ti_once, [
        (assign,":max",10),
        (store_random_in_range,":troop",bandits_begin,infested_end),

        (try_for_range,":unused",0,":max"),

            # (store_random_in_range,":target_entry_point",2,10),
               (assign,":target_entry_point",4),
            (entry_point_get_position, pos1, ":target_entry_point"),

            (set_spawn_position, pos1),
            (spawn_agent, ":troop"),
            (agent_set_team, reg0, 1),
            (agent_get_troop_id, ":agent_troop_id", reg0),
            (str_store_troop_name, s6, ":agent_troop_id"),
            (display_message, "@A new opponent has appeared nearby! {s6}",message_alert),
        (try_end),
      ], []),

      (ti_tab_pressed, 0, 0, [],
       [(question_box,"str_do_you_want_to_retreat"),
        ]),
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        # (jump_to_menu, "mnu_collect_taxes_failed"),
        (finish_mission),]),

      # (ti_tab_pressed, 0, 0, [(display_message,"str_cannot_leave_now")], []),
      # (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      # (0, 0, ti_once, [],
       # [
         # (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
         # ]),

      # (1, 4, ti_once, [(this_or_next|main_hero_fallen),(num_active_teams_le,1)],
       # [
           # (try_begin),
             # (main_hero_fallen),
             # (jump_to_menu, "mnu_collect_taxes_failed"),
           # (else_try),
             # (jump_to_menu, "mnu_collect_taxes_rebels_killed"),
           # (try_end),
           # (finish_mission),
           # ]),
    ],
  ),

]
# modmerger_start version=201 type=4
try:
    component_name = "mission_templates"
    var_set = { "mission_templates":mission_templates,"common_battle_mission_start":common_battle_mission_start,"common_battle_tab_press":common_battle_tab_press,"common_battle_init_banner":common_battle_init_banner,"common_arena_fight_tab_press":common_arena_fight_tab_press,"common_custom_battle_tab_press":common_custom_battle_tab_press,"custom_battle_check_victory_condition":custom_battle_check_victory_condition,"custom_battle_check_defeat_condition":custom_battle_check_defeat_condition,"common_battle_victory_display":common_battle_victory_display,"common_siege_question_answered":common_siege_question_answered,"common_siege_init":common_siege_init,"common_siege_ai_trigger_init":common_siege_ai_trigger_init,"common_siege_ai_trigger_init_after_2_secs":common_siege_ai_trigger_init_after_2_secs,"common_siege_defender_reinforcement_check":common_siege_defender_reinforcement_check,"common_siege_defender_reinforcement_archer_reposition":common_siege_defender_reinforcement_archer_reposition,"common_siege_attacker_reinforcement_check":common_siege_attacker_reinforcement_check,"common_siege_attacker_do_not_stall":common_siege_attacker_do_not_stall,"common_battle_check_friendly_kills":common_battle_check_friendly_kills,"common_battle_check_victory_condition":common_battle_check_victory_condition,"common_battle_victory_display":common_battle_victory_display,"common_siege_refill_ammo":common_siege_refill_ammo,"common_siege_check_defeat_condition":common_siege_check_defeat_condition,"common_battle_inventory":common_battle_inventory,"common_inventory_not_available":common_inventory_not_available,"tournament_triggers":tournament_triggers, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
