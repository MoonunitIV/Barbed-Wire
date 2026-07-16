from header_sounds import *
from compiler import *

# #######################################################################
#	("sound_id", sound_flags, ["sound-file"]),
#
#	There was never a header to this file.
#		Weird.
#
#	Essentially it's:
#	Field 1: Sound ID
#	Field 2: Flags, see header_sounds
#	Field 3: Sound file, it can be .ogg, .mp3, or .wav
# #######################################################################
# dstn:
# #######################################################################
#	I also took the time to categorize these sounds, It seems like so
#	long as you leave in the ones called by engine events you're good
# #######################################################################

sounds = [
 # UI/UX Sounds
  ("click", sf_2d|sf_vol_1,["ui_popup_messagewindow.wav"]), #ui_menu_ok.wav
  ("tutorial_1", 0,["none.ogg"]),
  ("tutorial_2", 0,["none.ogg"]),
  ("tutorial_fail", 0,["none.ogg"]),
  ("gong", sf_2d|sf_priority_9|sf_vol_9|sf_stream_from_hd, ["ui_popup_experienceup.wav"]),
  ("quest_taken", sf_2d|sf_priority_9|sf_vol_10|sf_stream_from_hd, ["ui_popup_questnew.wav"]),
  ("quest_completed", sf_2d|sf_priority_9|sf_vol_8|sf_stream_from_hd, ["ui_popup_questcomplete.wav"]),
  ("quest_succeeded", sf_2d|sf_priority_9|sf_vol_6|sf_stream_from_hd, ["ui_popup_questcomplete.wav"]),
  ("quest_concluded", sf_2d|sf_priority_9|sf_vol_7|sf_stream_from_hd, ["ui_popup_questnew.wav"]),
  ("quest_failed", sf_2d|sf_priority_9|sf_vol_7|sf_stream_from_hd, ["ui_popup_questupdate.wav"]),
  ("quest_cancelled", sf_2d|sf_priority_9|sf_vol_7|sf_stream_from_hd, ["ui_popup_questupdate.wav"]), 
  ("money_received",sf_2d|sf_priority_10|sf_vol_4, ["coins_dropped_1.wav"]),
  ("money_paid",sf_2d|sf_priority_10|sf_vol_10, ["coins_dropped_2.wav"]),

 # Party Sounds
  ("cow_moo", sf_2d|sf_priority_9|sf_vol_8|sf_stream_from_hd, ["cow_moo_1.ogg"]),
  ("cow_slaughter", sf_2d|sf_priority_3|sf_vol_8|sf_stream_from_hd, ["cow_slaughter.ogg"]),
  ("gallop",sf_vol_3, ["horse_gallop_3.wav","horse_gallop_4.wav","horse_gallop_5.wav"]),
  ("battle",sf_vol_8|sf_stream_from_hd, ["sfx_desert_dstntbttl_os_01.wav","sfx_desert_dstntbttl_os_02.wav","sfx_desert_dstntbttl_os_03.wav","sfx_desert_dstntbttl_os_04.wav","sfx_desert_dstntbttl_os_05.wav","sfx_desert_dstntbttl_os_06.wav"]),
  ("hide",0,["none.ogg"]),
  ("unhide",0,["none.ogg"]),
  
 # # Dialogue Voice Acting
  ("encounter_looters",sf_2d|sf_vol_8|sf_stream_from_hd, ["greeting_looter_fork_it_over.wav","greeting_looter_gimme_all.wav","greeting_looter_what_do_we_have.wav","greeting_looter2_hold_on_tight.wav","greeting_looter2_you_thinks_thats_funny.wav"]), 
  ("encounter_bandits",sf_2d|sf_vol_8|sf_stream_from_hd, ["greeting_criminal_1.wav","greeting_criminal_2.wav","greeting_criminal_3.wav"]),
  ("encounter_farmers",sf_2d|sf_vol_8|sf_stream_from_hd, ["encounter_farmer_2.ogg","encounter_farmer_5.ogg","encounter_farmer_7.ogg","encounter_farmer_9.ogg"]),
  ("encounter_sea_raiders",sf_2d|sf_vol_8|sf_stream_from_hd, ["encounter_sea_raider_5.ogg","encounter_sea_raider_9.ogg","encounter_sea_raider_9b.ogg","encounter_sea_raider_10.ogg"]),
  ("encounter_steppe_bandits",sf_2d|sf_vol_8|sf_stream_from_hd, ["encounter_steppe_bandit_3.ogg","encounter_steppe_bandit_3b.ogg","encounter_steppe_bandit_8.ogg","encounter_steppe_bandit_10.ogg","encounter_steppe_bandit_12.ogg"]),
  ("encounter_nobleman",sf_2d|sf_vol_8|sf_stream_from_hd, ["encounter_nobleman_1.ogg"]),
  ("encounter_vaegirs_ally",sf_2d|sf_vol_8|sf_stream_from_hd, ["encounter_vaegirs_ally.ogg","encounter_vaegirs_ally_2.ogg"]),
  ("encounter_vaegirs_neutral",sf_2d|sf_vol_8|sf_stream_from_hd, ["encounter_vaegirs_neutral.ogg","encounter_vaegirs_neutral_2.ogg","encounter_vaegirs_neutral_3.ogg","encounter_vaegirs_neutral_4.ogg"]),
  ("encounter_vaegirs_enemy",sf_2d|sf_vol_8|sf_stream_from_hd, ["encounter_vaegirs_neutral.ogg","encounter_vaegirs_neutral_2.ogg","encounter_vaegirs_neutral_3.ogg","encounter_vaegirs_neutral_4.ogg"]),
  ("sneak_town_halt",sf_2d|sf_stream_from_hd, ["greeting_usa_1.wav","greeting_usa_2.wav","greeting_usa_6.wav"]),
 
 # Combat Sounds
 # # Attacking Sounds 
  ("sword_clash_1", sf_priority_5|sf_vol_8,["sword_clank_metal_09.wav","sword_clank_metal_09b.wav","sword_clank_metal_10.wav","sword_clank_metal_10b.wav","sword_clank_metal_12.wav","sword_clank_metal_12b.wav","sword_clank_metal_13.wav","sword_clank_metal_13b.wav","weapon_sabre01.wav", "weapon_sabre02.wav", "weapon_sabre03.wav"]),
  ("sword_clash_2", 0, ["none.ogg"]),
  ("sword_clash_3", 0, ["none.ogg"]),
  ("sword_swing", sf_vol_8|sf_priority_2,["s_swordSwing.wav"]),
  # # Equipping/Unequipping Sounds
  ("draw_sword",sf_priority_2|sf_vol_4, ["draw_sword.wav"]),
  ("put_back_sword",sf_priority_1|sf_vol_4, ["put_back_sword.wav"]),
  ("draw_greatsword",sf_priority_2|sf_vol_4, ["draw_greatsword.wav"]),
  ("put_back_greatsword",sf_priority_1|sf_vol_4, ["put_back_sword.wav"]),
  ("draw_axe",sf_priority_2|sf_vol_4, ["draw_mace.wav"]),
  ("put_back_axe",sf_priority_1|sf_vol_4, ["put_back_to_holster.wav"]),
  ("draw_greataxe",sf_priority_2|sf_vol_4, ["draw_greataxe.wav"]),
  ("put_back_greataxe",sf_priority_1|sf_vol_4, ["put_back_to_leather.wav"]),
  ("draw_spear",sf_priority_2|sf_vol_4, ["draw_spear.wav"]),
  ("put_back_spear",sf_priority_1|sf_vol_4, ["put_away_spear_01.wav"]),
  ("draw_crossbow",sf_priority_2|sf_vol_4, ["draw_crossbow.wav"]),
  ("put_back_crossbow",sf_priority_1|sf_vol_4, ["put_back_to_leather.wav"]),
  ("draw_revolver",sf_priority_2|sf_vol_4, ["draw_from_holster.wav"]),
  ("put_back_revolver",sf_priority_1|sf_vol_4, ["put_back_to_holster.wav"]),
  ("draw_dagger",sf_priority_2|sf_vol_4,  ["draw_dagger.wav"]),
  ("put_back_dagger",sf_priority_1|sf_vol_4, ["put_back_dagger.wav"]),
  ("draw_bow",sf_priority_2|sf_vol_4, ["draw_bow.wav"]),
  ("put_back_bow",sf_priority_1|sf_vol_4, ["put_back_to_holster.wav"]),
  ("draw_shield",sf_priority_2|sf_vol_4, ["draw_shield.wav"]),
  ("put_back_shield",sf_priority_1|sf_vol_4, ["put_back_shield.wav"]),
  ("draw_other",sf_priority_2|sf_vol_4, ["draw_other.wav"]),
  ("put_back_other",sf_priority_1|sf_vol_4, ["draw_other2.wav"]),

 # # Biped Movement Sounds
  ("footstep_grass", sf_vol_4|sf_priority_1,["footstep_1.wav","footstep_2.wav","footstep_3.wav","footstep_4.wav"]),
  ("footstep_wood", sf_vol_5|sf_priority_1,["footstep_wood_1.wav","footstep_wood_2.wav","footstep_wood_4.wav"]),
  ("footstep_water", sf_vol_7|sf_priority_3,["water_walk_1.wav","water_walk_2.wav","water_walk_3.wav","water_walk_4.wav"]),
 # # # Biped Jump
  ("jump_begin", sf_vol_6|sf_priority_9,["jump_begin.wav"]),
  ("jump_end", sf_vol_5|sf_priority_9,["jump_end.wav"]),
  ("jump_begin_water", sf_vol_3|sf_priority_9,["jump_begin_water.wav"]),
  ("jump_end_water", sf_vol_3|sf_priority_9,["jump_end_water.wav"]),
 # # Horse Movement Sounds
  ("horse_walk",sf_priority_3|sf_vol_5, ["horse_walk_1.wav","horse_walk_2.wav","horse_walk_3.wav","horse_walk_4.wav"]),
  ("horse_trot",sf_priority_4|sf_vol_6, ["horse_trot_1.wav","horse_trot_2.wav","horse_trot_3.wav","horse_trot_4.wav"]),
  ("horse_canter",sf_priority_4|sf_vol_7, ["horse_canter_1.wav","horse_canter_2.wav","horse_canter_3.wav","horse_canter_4.wav"]),
  ("horse_gallop",sf_priority_5|sf_vol_8, ["horse_gallop_6.wav","horse_gallop_7.wav","horse_gallop_8.wav","horse_gallop_9.wav"]), 
  ("footstep_horse", 0, ["none.ogg"]),
  ("footstep_horse_1b",sf_priority_3|sf_vol_8, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
  ("footstep_horse_1f",sf_priority_3|sf_vol_8, ["s_footstep_horse_2b.wav","s_footstep_horse_2f.wav","s_footstep_horse_3b.wav","s_footstep_horse_3f.wav"]),
  ("footstep_horse_2b",sf_priority_3|sf_vol_8, ["s_footstep_horse_2b.wav"]),
  ("footstep_horse_2f",sf_priority_3|sf_vol_8, ["s_footstep_horse_2f.wav"]),
  ("footstep_horse_3b",sf_priority_3|sf_vol_8, ["s_footstep_horse_3b.wav"]),
  ("footstep_horse_3f",sf_priority_3|sf_vol_8, ["s_footstep_horse_3f.wav"]),
  ("footstep_horse_4b",sf_priority_3|sf_vol_8, ["s_footstep_horse_4b.wav"]),
  ("footstep_horse_4f",sf_priority_3|sf_vol_8, ["s_footstep_horse_4f.wav"]),
  ("footstep_horse_5b",sf_priority_3|sf_vol_8, ["s_footstep_horse_5b.wav"]),
  ("footstep_horse_5f",sf_priority_3|sf_vol_8, ["s_footstep_horse_5f.wav"]),
 # # # Horse Jump 
  ("horse_jump_begin", sf_vol_6|sf_priority_9,["horse_jump_begin.wav"]),
  ("horse_jump_end", sf_vol_7|sf_priority_9,["horse_jump_end.wav"]),
  ("horse_jump_begin_water", sf_vol_10|sf_priority_9,["jump_begin_water.wav"]),
  ("horse_jump_end_water", sf_vol_10|sf_priority_9,["jump_end_water.wav"]),
 # Ranged Attacking Sounds
 # # Readying
  ("reload_crossbow",0, ["none.ogg"]),
  ("reload_crossbow_continue",0, ["none.ogg"]),
  ("pull_bow",sf_vol_5, ["pull_bow_1.wav"]),
  ("pull_arrow",sf_vol_5, ["pull_arrow.wav"]),
 # # Shooting
  ("release_bow",sf_vol_4, ["release_bow_1.wav"]),
  ("release_crossbow",sf_vol_7, ["none.ogg"]),
  ("release_crossbow_medium",0, ["none.ogg"]),
  ("release_crossbow_far",0, ["none.ogg"]),
  ("throw_javelin",sf_vol_5, ["throw_javelin_2.wav"]),
  ("throw_axe",sf_vol_7, ["throw_axe_1.wav"]),
  ("throw_knife",sf_vol_5, ["throw_knife_1.wav"]),
  ("throw_stone",sf_vol_5, ["throw_stone_1.wav"]),
 # # Struck
  ("bullet_hit_body", sf_priority_4, ["body_hit_1.wav", "body_hit_2.wav", "body_hit_3.wav", "impact_body2.wav", "impact_body6.wav"]),
  ("player_hit_by_bullet", sf_priority_11|sf_vol_10, ["body_hit_1.wav", "body_hit_2.wav", "body_hit_3.wav", "impact_body2.wav", "impact_body6.wav"]), 
 # # Fly Past
  ("arrow_pass_by",sf_priority_7, ["arrow_pass_by_1.wav","arrow_pass_by_2.wav","arrow_pass_by_3.wav","arrow_pass_by_4.wav"]),
  ("bolt_pass_by",sf_priority_7, ["bullet_pass_01.wav","bullet_pass_02.wav","bullet_pass_03.wav","bullet_pass_04.wav","bullet_pass_05.wav","bullet_pass_06.wav","bullet_pass_07.wav","bullet_pass_08.wav","bullet_pass_09.wav","bullet_pass_10.wav","bullet_pass_11.wav","bullet_pass_12.wav"]),
  ("javelin_pass_by",sf_priority_7, ["javelin_pass_by_1.wav","javelin_pass_by_2.wav"]),
  ("stone_pass_by",sf_vol_9|sf_priority_7, ["stone_pass_by_1.wav"]),
  ("axe_pass_by",sf_priority_7, ["axe_pass_by_1.wav"]),
  ("knife_pass_by",sf_priority_7, ["knife_pass_by_1.wav"]),
  ("bullet_pass_by",sf_priority_7, ["bullet_pass_01.wav","bullet_pass_02.wav","bullet_pass_03.wav","bullet_pass_04.wav","bullet_pass_05.wav","bullet_pass_06.wav","bullet_pass_07.wav","bullet_pass_08.wav","bullet_pass_09.wav","bullet_pass_10.wav","bullet_pass_11.wav","bullet_pass_12.wav"]),
 
 # # Hit Ground, Aimed Towards Player
  ("incoming_arrow_hit_ground",sf_priority_7|sf_vol_7, ["arrow_hit_ground_2.wav","arrow_hit_ground_3.wav"]),
  ("incoming_bolt_hit_ground",sf_priority_7|sf_vol_7, ["bullet_hit_ground1.wav", "bullet_hit_ground2.wav", "bullet_hit_ground3.wav", "bullet_hit_ground4.wav", "bullet_hit_ground5.wav"]),
  ("incoming_javelin_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.wav"]),
  ("incoming_stone_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.wav"]),
  ("incoming_axe_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.wav"]),
  ("incoming_knife_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.wav"]),
  ("incoming_bullet_hit_ground",sf_priority_7|sf_vol_7, ["bullet_hit_ground1.wav", "bullet_hit_ground2.wav", "bullet_hit_ground3.wav", "bullet_hit_ground4.wav", "bullet_hit_ground5.wav"]),
 # # Hit Ground, Aimed Away From Player
  ("outgoing_arrow_hit_ground",sf_priority_7|sf_vol_7, ["outgoing_arrow_hit_ground.wav"]),
  ("outgoing_bolt_hit_ground",sf_priority_7|sf_vol_7,  ["bullet_hit_ground1.wav", "bullet_hit_ground2.wav", "bullet_hit_ground3.wav", "bullet_hit_ground4.wav", "bullet_hit_ground5.wav"]),
  ("outgoing_javelin_hit_ground",sf_priority_7|sf_vol_10, ["outgoing_arrow_hit_ground.wav"]),
  ("outgoing_stone_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.wav"]),
  ("outgoing_axe_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.wav"]),
  ("outgoing_knife_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.wav"]),
  ("outgoing_bullet_hit_ground",sf_priority_7|sf_vol_7, ["bullet_hit_ground1.wav", "bullet_hit_ground2.wav", "bullet_hit_ground3.wav", "bullet_hit_ground4.wav", "bullet_hit_ground5.wav"]),


 # Death Sounds
  ("body_fall_small",sf_priority_5|sf_vol_9, ["body_fall_small_1.wav","body_fall_small_2.wav"]),
  ("body_fall_big",sf_priority_6|sf_vol_8, ["body_fall_1.wav","body_fall_2.wav","body_fall_3.wav"]),

  ("horse_body_fall_begin",sf_priority_7|sf_vol_10, ["horse_body_fall_begin_1.wav"]),
  ("horse_body_fall_end",sf_priority_7|sf_vol_10, ["horse_body_fall_end_1.wav","body_fall_2.wav","body_fall_very_big_1.wav"]),

  ("hit_wood_wood",sf_priority_7|sf_vol_12, ["hit_wood_wood_1.wav","hit_wood_wood_2.wav","hit_wood_wood_3.wav","hit_wood_wood_4.wav","hit_wood_metal_4.wav","hit_wood_metal_5.wav","hit_wood_metal_6.wav"]),
  ("hit_metal_metal",sf_priority_7|sf_vol_10, ["hit_metal_metal_3.wav","hit_metal_metal_4.wav",
                                              "hit_metal_metal_5.wav","hit_metal_metal_6.wav","hit_metal_metal_7.wav","hit_metal_metal_8.wav",
                                              "hit_metal_metal_9.wav","hit_metal_metal_10.wav",
                                              "clang_metal_1.wav","clang_metal_2.wav","weapon_sabre01.wav", "weapon_sabre02.wav", "weapon_sabre03.wav"]),
  ("hit_wood_metal",sf_priority_7|sf_vol_10, ["hit_metal_metal_1.wav","hit_metal_metal_2.wav","hit_wood_metal_7.wav"]),

  ("shield_hit_wood_wood",sf_priority_7|sf_vol_9, ["shield_hit_wood_wood_1.wav","shield_hit_wood_wood_2.wav","shield_hit_wood_wood_3.wav"]),
  ("shield_hit_metal_metal",sf_priority_7|sf_vol_10, ["shield_hit_metal_metal_1.wav","shield_hit_metal_metal_2.wav","shield_hit_metal_metal_3.wav","shield_hit_metal_metal_4.wav"]),
  ("shield_hit_wood_metal",sf_priority_7|sf_vol_10, ["shield_hit_cut_3.wav","shield_hit_cut_4.wav","shield_hit_cut_5.wav","shield_hit_cut_10.wav"]),
  ("shield_hit_metal_wood",sf_priority_7|sf_vol_10, ["shield_hit_metal_wood_1.wav","shield_hit_metal_wood_2.wav","shield_hit_metal_wood_3.wav"]),
  ("shield_broken",sf_priority_9, ["shield_broken.wav"]),

  ("man_hit", sf_priority_7|sf_vol_7, ["man_pain_1.wav", "man_pain_2.wav", "man_pain_3.wav", "man_pain_4.wav", "man_pain_5.wav", "man_pain_6.wav", "man_pain_7.wav", "man_pain_8.wav", "man_pain_9.wav", "man_pain_10.wav", "man_pain_11.wav", "man_pain_12.wav", "man_pain_13.wav", "man_pain_14.wav", "man_pain_15.wav", "man_pain_16.wav", "man_pain_17.wav", "man_pain_18.wav", "man_pain_19.wav", "man_pain_20.wav", "man_pain_21.wav", "man_pain_22.wav", "man_pain_23.wav", "man_pain_24.wav", "man_pain_25.wav", "man_pain_26.wav", "man_pain_27.wav", "man_pain_28.wav", "man_pain_29.wav"]),
  ("man_die", sf_priority_10|sf_vol_8, ["man_death_1.wav", "man_death_2.wav", "man_death_3.wav", "man_death_4.wav", "man_death_5.wav", "man_death_6.wav", "man_death_7.wav", "man_death_8.wav", "man_death_9.wav", "man_death_10.wav", "man_death_11.wav", "man_death_12.wav", "man_death_13.wav", "man_death_14.wav", "man_death_15.wav", "man_death_16.wav", "man_death_17.wav", "man_death_18.wav", "man_death_19.wav", "man_death_20.wav", "man_death_21.wav", "man_death_22.wav", "man_death_23.wav", "man_death_24.wav", "man_death_25.wav", "man_death_26.wav", "man_death_27.wav", "man_death_28.wav", "man_death_29.wav", "man_death_30.wav", "man_death_31.wav", "man_death_32.wav"]),
  ("woman_hit", sf_priority_7, ["woman_hit_2.wav", "woman_hit_3.wav", "woman_hit_b_2.wav", "woman_hit_b_4.wav", "woman_hit_b_6.wav", "woman_hit_b_7.wav", "woman_hit_b_8.wav", "woman_hit_b_11.wav", "woman_hit_b_14.wav", "woman_hit_b_16.wav", "woman_pain_1.wav", "woman_pain_2.wav", "woman_pain_3.wav", "woman_pain_4.wav", "woman_pain_5.wav", "woman_pain_6.wav", "woman_pain_7.wav", "woman_pain_8.wav", "woman_pain_9.wav", "woman_pain_10.wav", "woman_pain_11.wav", "woman_pain_12.wav"]),
  ("woman_die", sf_priority_10|sf_vol_9, ["woman_fall_1.wav", "woman_hit_b_5.wav", "woman_death_1.wav", "woman_death_2.wav", "woman_death_3.wav", "woman_death_4.wav", "woman_death_5.wav", "woman_death_6.wav", "woman_death_7.wav", "woman_death_8.wav", "woman_death_9.wav", "woman_death_10.wav", "woman_death_11.wav", "woman_death_12.wav", "woman_death_13.wav", "woman_death_14.wav", "woman_death_15.wav", "woman_death_16.wav", "woman_death_17.wav", "woman_death_18.wav", "woman_death_19.wav", "woman_death_20.wav", "woman_death_21.wav", "woman_death_22.wav", "woman_death_23.wav"]),
  ("woman_yell",sf_priority_8|sf_vol_9, ["woman_yell_1.wav","woman_yell_2.wav"]),
  
 # Vocalizations
 # # Human
 # # # Man
 # # # Woman
 # # Horse
  ("horse_breath",sf_priority_1|sf_vol_4, ["horse_breath_4.wav","horse_breath_5.wav","horse_breath_6.wav","horse_breath_7.wav"]),
  ("horse_snort",sf_priority_1|sf_vol_2|sf_stream_from_hd, ["horse_snort_1.wav","horse_snort_2.wav","horse_snort_3.wav","horse_snort_4.wav","horse_snort_5.wav"]),
  ("horse_low_whinny",sf_vol_12|sf_stream_from_hd, ["horse_whinny-1.wav","horse_whinny-2.wav"]),
 
  ("arrow_hit_body",sf_priority_4, ["arrow_hit_body_1.wav","arrow_hit_body_2.wav","arrow_hit_body_3.wav"]),
 
  ("metal_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["sword_hit_lo_armor_lo_dmg_1.wav","sword_hit_lo_armor_lo_dmg_2.wav","sword_hit_lo_armor_lo_dmg_3.wav"]),
  ("metal_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["sword_hit_lo_armor_hi_dmg_1.wav","sword_hit_lo_armor_hi_dmg_2.wav","sword_hit_lo_armor_hi_dmg_3.wav"]),
  ("metal_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["metal_hit_high_armor_low_damage.wav","metal_hit_high_armor_low_damage_2.wav","metal_hit_high_armor_low_damage_3.wav"]),
  ("metal_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["sword_hit_hi_armor_hi_dmg_1.wav","sword_hit_hi_armor_hi_dmg_2.wav","sword_hit_hi_armor_hi_dmg_3.wav"]),
  ("wooden_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["blunt_hit_low_1.wav","blunt_hit_low_2.wav","blunt_hit_low_3.wav"]),
  ("wooden_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_hit_high_1.wav","blunt_hit_high_2.wav","blunt_hit_high_3.wav"]),
  ("wooden_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["wooden_hit_high_armor_low_damage.wav","wooden_hit_high_armor_low_damage_2.wav"]),
  ("wooden_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_hit_high_1.wav","blunt_hit_high_2.wav","blunt_hit_high_3.wav"]),
 
  ("mp_arrow_hit_target",0, ["none.ogg"]),
  ("blunt_hit",sf_priority_5|sf_vol_10, ["punch_1.wav","punch_4.wav","punch_4.wav","punch_5.wav"]),
  ("player_hit_by_arrow",sf_priority_11|sf_vol_10, ["player_hit_by_arrow.wav"]),
  ("pistol_shot",0, ["none.ogg"]),

  ("man_grunt", sf_priority_3|sf_vol_4, ["man_excercise_1.wav", "man_excercise_2.wav", "man_excercise_4.wav"]),
  ("man_breath_hard", sf_priority_3|sf_vol_8, ["man_ugh_1.wav", "man_ugh_2.wav", "man_ugh_4.wav", "man_ugh_7.wav", "man_ugh_12.wav", "man_ugh_13.wav", "man_ugh_17.wav"]),
  ("man_stun", sf_priority_3|sf_vol_8, ["man_stun_1.wav"]),
  ("man_grunt_long", sf_priority_6|sf_vol_7, ["man_grunt_1.wav", "man_grunt_2.wav", "man_grunt_3.wav", "man_grunt_4.wav", "man_grunt_5.wav", "man_grunt_6.wav", "man_grunt_7.wav", "man_grunt_8.wav", "man_grunt_9.wav", "man_grunt_10.wav", "man_grunt_11.wav", "man_grunt_12.wav", "man_grunt_13.wav", "man_grunt_14.wav", "man_grunt_15.wav", "man_grunt_16.wav", "man_grunt_17.wav", "man_grunt_18.wav", "man_grunt_19.wav", "man_grunt_20.wav"]), 
  ("man_yell",sf_priority_5|sf_vol_8, ["man_yell_4.wav","man_yell_4_2.wav","man_yell_7.wav","man_yell_9.wav","man_yell_11.wav","man_yell_13.wav","man_yell_15.wav","man_yell_16.wav","man_yell_17.wav","man_yell_20.wav","man_shortyell_4.wav","man_shortyell_5.wav","man_shortyell_6.wav","man_shortyell_9.wav","man_shortyell_11.wav","man_shortyell_11b.wav",
                        "man_yell_b_18.wav","man_yell_22.wav", "man_yell_c_20.wav"]),

  ("man_warcry",sf_priority_5, ["man_insult_2.wav","man_insult_3.wav","man_insult_7.wav","man_insult_9.wav","man_insult_13.wav","man_insult_15.wav","man_insult_16.wav"]),
 
  ("block_fist",0, ["block_fist_3.wav","block_fist_4.wav"]),

  ("man_hit_blunt_weak", sf_priority_5|sf_vol_10, ["man_pain_1.wav", "man_pain_2.wav", "man_pain_3.wav", "man_pain_4.wav", "man_pain_5.wav", "man_pain_6.wav", "man_pain_7.wav", "man_pain_8.wav", "man_pain_9.wav", "man_pain_10.wav", "man_pain_11.wav", "man_pain_12.wav", "man_pain_13.wav", "man_pain_14.wav", "man_pain_15.wav", "man_pain_16.wav", "man_pain_17.wav", "man_pain_18.wav", "man_pain_19.wav", "man_pain_20.wav", "man_pain_21.wav", "man_pain_22.wav", "man_pain_23.wav", "man_pain_24.wav"]),
  ("man_hit_blunt_strong", sf_priority_5|sf_vol_10, ["man_pain_1.wav", "man_pain_2.wav", "man_pain_3.wav", "man_pain_4.wav", "man_pain_5.wav", "man_pain_6.wav", "man_pain_7.wav", "man_pain_8.wav", "man_pain_9.wav", "man_pain_10.wav", "man_pain_11.wav", "man_pain_12.wav", "man_pain_13.wav", "man_pain_14.wav", "man_pain_15.wav", "man_pain_16.wav", "man_pain_17.wav", "man_pain_18.wav", "man_pain_19.wav", "man_pain_20.wav", "man_pain_21.wav", "man_pain_22.wav", "man_pain_23.wav", "man_pain_24.wav"]),
  ("man_hit_pierce_weak", sf_priority_5|sf_vol_10, ["man_pain_1.wav", "man_pain_2.wav", "man_pain_3.wav", "man_pain_4.wav", "man_pain_5.wav", "man_pain_6.wav", "man_pain_7.wav", "man_pain_8.wav", "man_pain_9.wav", "man_pain_10.wav", "man_pain_11.wav", "man_pain_12.wav", "man_pain_13.wav", "man_pain_14.wav", "man_pain_15.wav", "man_pain_16.wav", "man_pain_17.wav", "man_pain_18.wav", "man_pain_19.wav", "man_pain_20.wav", "man_pain_21.wav", "man_pain_22.wav", "man_pain_23.wav", "man_pain_24.wav"]),
  ("man_hit_pierce_strong", sf_priority_5|sf_vol_10, ["man_pain_1.wav", "man_pain_2.wav", "man_pain_3.wav", "man_pain_4.wav", "man_pain_5.wav", "man_pain_6.wav", "man_pain_7.wav", "man_pain_8.wav", "man_pain_9.wav", "man_pain_10.wav", "man_pain_11.wav", "man_pain_12.wav", "man_pain_13.wav", "man_pain_14.wav", "man_pain_15.wav", "man_pain_16.wav", "man_pain_17.wav", "man_pain_18.wav", "man_pain_19.wav", "man_pain_20.wav", "man_pain_21.wav", "man_pain_22.wav", "man_pain_23.wav", "man_pain_24.wav"]),
  ("man_hit_cut_weak", sf_priority_5|sf_vol_10, ["man_pain_1.wav", "man_pain_2.wav", "man_pain_3.wav", "man_pain_4.wav", "man_pain_5.wav", "man_pain_6.wav", "man_pain_7.wav", "man_pain_8.wav", "man_pain_9.wav", "man_pain_10.wav", "man_pain_11.wav", "man_pain_12.wav", "man_pain_13.wav", "man_pain_14.wav", "man_pain_15.wav", "man_pain_16.wav", "man_pain_17.wav", "man_pain_18.wav", "man_pain_19.wav", "man_pain_20.wav", "man_pain_21.wav", "man_pain_22.wav", "man_pain_23.wav", "man_pain_24.wav"]),
  ("man_hit_cut_strong", sf_priority_5|sf_vol_10, ["man_pain_1.wav", "man_pain_2.wav", "man_pain_3.wav", "man_pain_4.wav", "man_pain_5.wav", "man_pain_6.wav", "man_pain_7.wav", "man_pain_8.wav", "man_pain_9.wav", "man_pain_10.wav", "man_pain_11.wav", "man_pain_12.wav", "man_pain_13.wav", "man_pain_14.wav", "man_pain_15.wav", "man_pain_16.wav", "man_pain_17.wav", "man_pain_18.wav", "man_pain_19.wav", "man_pain_20.wav", "man_pain_21.wav", "man_pain_22.wav", "man_pain_23.wav", "man_pain_24.wav"]),
 
  ("man_victory",sf_priority_5|sf_vol_9, ["man_victory_3.wav","man_victory_4.wav","man_victory_5.wav","man_victory_8.wav","man_victory_15.wav","man_victory_49.wav","man_victory_52.wav","man_victory_54.wav","man_victory_57.wav","man_victory_71.wav"]),
 
 # Scene Sounds
 # # Animal Ambience Sounds
  ("neigh",sf_stream_from_hd, ["horse_exterior_whinny_01.wav","horse_exterior_whinny_02.wav","horse_exterior_whinny_03.wav","horse_exterior_whinny_04.wav","horse_exterior_whinny_05.wav","horse_whinny.wav"]),
  ("distant_dog_bark", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["sfx_dogbarkdistant_os_01.wav","sfx_dogbarkdistant_os_02.wav","sfx_dogbarkdistant_os_03.wav","sfx_dogbarkdistant_os_04.wav","sfx_dogbarkdistant_os_05.wav",]),
  ("distant_owl", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["sfx_desert_owl_os_01.wav","sfx_desert_owl_os_02.wav","sfx_desert_owl_os_03.wav"]),
  ("distant_chicken", 0, ["none.ogg"]),
 # # City Ambience Sounds
  ("distant_worker", sf_priority_6|sf_vol_1|sf_stream_from_hd, ["d_blacksmith2.ogg","d_carpenter1.ogg","d_saw_short3.ogg"]), 
  ("distant_carpenter", 0, ["none.ogg"]),
  ("distant_blacksmith", 0, ["none.ogg"]),
  ("arena_ambiance", sf_2d|sf_priority_8|sf_vol_3|sf_looping|sf_stream_from_hd, ["amb_pittcrowd_ahh_01.wav","amb_pittcrowd_ahh_02.wav","amb_pittcrowd_ahh_03.wav","amb_pittcrowd_cheer_01.wav","amb_pittcrowd_cheer_02.wav","amb_pittcrowd_cheer_03.wav"]),
  ("town_ambiance", 0, ["none.ogg"]),
 # # Weather Sounds
  ("rain",sf_2d|sf_priority_10|sf_vol_4|sf_looping|sf_stream_from_hd, ["rain-amb.wav"]),
 
 # Prop Sounds
  ("fire_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos|sf_stream_from_hd, ["Fire_Torch_Loop3.wav"]),
  ("torch_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos|sf_stream_from_hd, ["Fire_Torch_Loop3.wav"]),
  ("dummy_hit",sf_priority_9, ["shield_hit_cut_3.wav","shield_hit_cut_5.wav"]),
  ("dummy_destroyed",sf_priority_9, ["shield_broken.wav"]),
  ("gourd_destroyed",sf_priority_9|sf_stream_from_hd, ["shield_broken.wav"]),
 
 # Multiplayer Sounds
  ("your_flag_taken", 0, ["none.ogg"]),
  ("enemy_flag_taken", 0, ["none.ogg"]),
  ("flag_returned", 0, ["none.ogg"]),
  ("team_scored_a_point", 0, ["none.ogg"]),
  ("enemy_scored_a_point", 0, ["none.ogg"]),
  
###################################
## NEW
###################################

  ("m4a1", sf_priority_15|sf_vol_4, ["m4a1_01.wav", "m4a1_02.wav", "m4a1_03.wav", "m4a1_04.wav"]),
  ("m1carbine", sf_priority_15|sf_vol_4, ["m1carbine.wav"]),
  ("deagle", sf_priority_15|sf_vol_4, ["deagle_01.wav", "deagle_02.wav", "deagle_03.wav"]),
  ("r700", sf_priority_15|sf_vol_4, ["r700.wav"]),
  ("thompson", sf_priority_15|sf_vol_4, ["thompson.wav"]),
  ("ak47", sf_priority_15|sf_vol_4, ["ak47_01.wav"]),
  ("tec9", sf_priority_15|sf_vol_4, ["tec9.wav"]),
  ("g36c", sf_priority_15|sf_vol_4, ["g36c.wav"]),
  ("colt1911", sf_priority_15|sf_vol_4, ["colt1911.wav"]),
  ("mp5", sf_priority_15|sf_vol_4, ["mp5.wav"]),
  ("ump45", sf_priority_15|sf_vol_4, ["ump45.wav"]),
  ("uzi", sf_priority_15|sf_vol_4, ["uzi.wav"]),
  ("mp40", sf_priority_15|sf_vol_4, ["mp40.wav"]),
  ("mg42", sf_priority_15|sf_vol_4, ["mg42.wav"]),
  ("mauser", sf_priority_15|sf_vol_4, ["mauser.wav"]),
  ("m249", sf_priority_15|sf_vol_4, ["m249.wav"]),
  ("type99", sf_priority_15|sf_vol_4, ["type99.wav"]),
  ("gewehr_sniper", sf_priority_15|sf_vol_4, ["gewehr_sniper.wav"]),
  ("plasmarifle_fire", sf_priority_15|sf_vol_4, ["wpn_plasmarifle_fire_3d_01.wav","wpn_plasmarifle_fire_3d_02.wav"]),
  ("plasmapistol_fire", sf_priority_15|sf_vol_4, ["wpn_plasmapistol_fire_3d_01.wav","wpn_plasmapistol_fire_3d_02.wav"]),
  ("powerfist", sf_priority_15|sf_vol_8, ["wpn_powerfist_fire_3d.wav"]),
  ("9mm_fire", sf_priority_15|sf_vol_4, ["wpn_9mm_fire_3d_01.wav","wpn_9mm_fire_3d_02.wav","wpn_9mm_fire_3d_03.wav","wpn_9mm_fire_3d_04.wav"]),
  ("9mmsmg_fire", sf_priority_15|sf_vol_4, ["wpn_9mmsmg_fire_3d_01.wav","wpn_9mmsmg_fire_3d_02.wav","wpn_9mmsmg_fire_3d_03.wav","wpn_9mmsmg_fire_3d_04.wav"]),
  ("45_smg_fire", sf_priority_15|sf_vol_4, ["wpn_45_smg_3d_01.wav","wpn_45_smg_3d_02.wav","wpn_45_smg_3d_03.wav"]),
  ("10mmpistolfire", sf_priority_15|sf_vol_4, ["wpn_10mmpistolfire_3d_01.wav","wpn_10mmpistolfire_3d_02.wav","wpn_10mmpistolfire_3d_03.wav"]),
  ("policepistolfire", sf_priority_15|sf_vol_4, ["wpn_policepistol_fire_3d_01.wav","wpn_policepistol_fire_3d_02.wav","wpn_policepistol_fire_3d_03.wav"]),
  ("357revolv_fire", sf_priority_15|sf_vol_4, ["wpn_fire_357revolver_3d_01.wav","wpn_fire_357revolver_3d_02.wav","wpn_fire_357revolver_3d_03.wav"]),
  ("44revolv_fire", sf_priority_15|sf_vol_4, ["wpn_44revolv_fire_3d_01.wav","wpn_44revolv_fire_3d_02.wav","wpn_44revolv_fire_3d_03.wav"]),
  ("fire_huntingrevolver", sf_priority_15|sf_vol_4, ["wpn_fire_huntingrevolver_3d_01.wav","wpn_fire_huntingrevolver_3d_02.wav","wpn_fire_huntingrevolver_3d_03.wav"]),
  ("assaultcarb_fire", sf_priority_15|sf_vol_4, ["wpn_assaultcarb_fire_3d_01.wav","wpn_assaultcarb_fire_3d_02.wav","wpn_assaultcarb_fire_3d_03.wav"]),
  ("marksmancarbine", sf_priority_15|sf_vol_4, ["wpn_marksmancarbine_fire_3d_01.wav","wpn_marksmancarbine_fire_3d_02.wav","wpn_marksmancarbine_fire_3d_03.wav"]),
  ("huntingrifle_fire", sf_priority_15|sf_vol_4, ["wpn_huntingrifle_fire_3d_01.wav","wpn_huntingrifle_fire_3d_02.wav","wpn_huntingrifle_fire_3d_03.wav"]),
  ("trailcarbine_fire", sf_priority_15|sf_vol_4, ["wpn_trailcarbine_fire_3d_01.wav","wpn_trailcarbine_fire_3d_02.wav","wpn_trailcarbine_fire_3d_03.wav"]),
  ("pistol22_fire", sf_priority_15|sf_vol_4, ["wpn_pistol22_fire_3d.wav"]),
  ("assault_modern_fire", sf_priority_15|sf_vol_4, ["wpn_rifleassaultg3_fire_3d.wav"]),
  ("autorifle_fire", sf_priority_15|sf_vol_4, ["wpn_autorifle_fire_3d_01.wav","wpn_autorifle_fire_3d_02.wav","wpn_autorifle_fire_3d_03.wav"]),
  ("riflegauss_fire", sf_priority_15|sf_vol_4, ["wpn_riflegauss_fire_3d.wav"]),
  ("huntingshotgun_fire", sf_priority_15|sf_vol_4, ["wpn_huntingshotgun_fire_3d_01.wav","wpn_huntingshotgun_fire_3d_02.wav"]),
  ("riotshotgun_fire", sf_priority_15|sf_vol_4, ["wpn_riotshotgun_fire_3d_01.wav","wpn_riotshotgun_fire_3d_02.wav"]),
  ("sawedoffshotgun_fire", sf_priority_15|sf_vol_4, ["wpn_sawedoffshotgun_fire_3d_01.wav","wpn_sawedoffshotgun_fire_3d_02.wav"]),
  ("shotguncombat_fire", sf_priority_15|sf_vol_4, ["wpn_shotguncombat_fire_3d.wav"]),
  ("silenced_fire", sf_priority_15|sf_vol_4, ["wpn_silenced22smg_fire_3d_01.wav","wpn_silenced22smg_fire_3d_02.wav","wpn_silenced22smg_fire_3d_03.wav"]),
  ("flamer_fire", sf_priority_15|sf_vol_4, ["wpn_flamer_fire_3d_lpm.wav"]),
  ("rpgshot", sf_priority_15|sf_vol_4, ["rpg.wav"]),
  
  ("garand_shot", sf_priority_15|sf_vol_4, ["garand_shot.ogg"]),
  ("garand_ping", sf_2d|sf_priority_15|sf_vol_4, ["garand_ping.wav"]),    

  ("flamer_idle", sf_priority_5|sf_vol_4, ["wpn_flamer_idle_lpm.wav"]),
  ("rifleplasma_idle", sf_priority_5|sf_vol_4, ["wpn_rifleplasma_idle_lpm.wav"]),

  ("9mmreload", sf_2d|sf_priority_10|sf_vol_4, ["wpn_9mmreload.wav"]),
  ("smgreload", sf_2d|sf_priority_10|sf_vol_4, ["wpn_riflesmg_reload.wav"]),
  ("flamer_reload", sf_2d|sf_priority_10|sf_vol_4, ["wpn_flamer_reload.wav"]),
  ("pistolplasma_reload", sf_2d|sf_priority_10|sf_vol_4, ["wpn_pistolplasma_reload.wav"]),
  ("44revolv_reload", sf_2d|sf_priority_10|sf_vol_4, ["wpn_44revolv_reload.wav"]),
  
  ("firedry", sf_2d|sf_priority_10|sf_vol_4, ["wpn_pistol10mm_firedry.wav"]),
  ("flashbang_effect", sf_2d|sf_priority_10|sf_vol_8, ["flash_bang.wav"]),

  ("grenade1", sf_priority_15|sf_vol_15, ["grenade3.wav"]),
  ("molotov", sf_priority_15|sf_vol_15, ["fx_explosion_molotov_01.wav","fx_explosion_molotov_02.wav"]),
  ("flashbang", sf_priority_15|sf_vol_15, ["grenade2.wav"]),
  
  ("ambient_town", sf_2d|sf_priority_8|sf_vol_1|sf_looping, ["amb_slum_day_lp.wav"]),
  ("ambient_day", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["amb_cmpmcrn_day_lp.wav"]),
  ("ambient_night", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["amb_cmpmcrn_night_lp.wav"]),
  ("ambient_plain_day", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["amb_dstrydcty_day_lp.wav"]),
  ("ambient_plain_night", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["amb_dstrydcty_night_lp.wav"]),
  ("ambient_wind_day", sf_2d|sf_priority_8|sf_vol_8|sf_looping, ["ambf_wind_day_lp.wav"]),
  ("ambient_wind_night", sf_2d|sf_priority_8|sf_vol_8|sf_looping, ["ambf_wind_night_lp.wav"]),  
  ("ambient_sandstorm", sf_2d|sf_priority_8|sf_vol_8|sf_looping, ["amb_sandstorm_lp.wav"]),
  ("ambient_thunder_close", sf_2d|sf_priority_8|sf_vol_10|sf_stream_from_hd, ["thunder_close_1.wav","thunder_close_2.wav","thunder_close_3.wav"]),
  ("ambient_thunder", sf_priority_3|sf_vol_10|sf_stream_from_hd, ["amb_blackmountain_thunder_01.wav","amb_blackmountain_thunder_02.wav","amb_blackmountain_thunder_03.wav","amb_blackmountain_thunder_04.wav","amb_blackmountain_thunder_05.wav","amb_blackmountain_thunder_06.wav"]),
  ("ambient_windmill", sf_priority_8|sf_vol_10|sf_looping|sf_stream_from_hd, ["windmill_fan.wav",]),
  ("ambient_storm", sf_priority_3|sf_vol_4|sf_looping|sf_stream_from_hd, ["amb_storm_03.wav","amb_storm_04.wav","amb_storm_01.wav","amb_storm_02.wav"]),
  ("ambient_generator", sf_priority_3|sf_vol_10|sf_looping|sf_stream_from_hd, ["sfx_industrialmachine02_lp.wav"]),
  ("ambient_aircondition", sf_priority_3|sf_vol_10|sf_looping|sf_stream_from_hd, ["sfx_acloop.wav"]),
  ("ambient_brokeglass", sf_priority_8|sf_vol_10|sf_looping|sf_stream_from_hd, ["glass.wav"]),
  ("ambient_holdingtank", sf_priority_3|sf_vol_10|sf_looping|sf_stream_from_hd, ["emt_holdingtank_lp.wav"]),
  ("ambient_steam", sf_priority_3|sf_vol_10|sf_looping|sf_stream_from_hd, ["sfx_steamburst_os_01.wav","sfx_steamburst_os_02.wav","sfx_steamburst_os_03.wav","sfx_steamrelease_os_1.wav","sfx_steamrelease_os_2.wav","sfx_steamrelease_os_3.wav","sfx_steamrelease_os_4.wav"]),
  ("ambient_console", sf_priority_3|sf_vol_10|sf_looping|sf_stream_from_hd, ["sfx_console_01_lp.wav"]),
  ("ambient_lamp", sf_priority_3|sf_vol_10|sf_looping|sf_stream_from_hd, ["sfx_neonsign_pt1.wav"]),
  ("ambient_fire", sf_priority_8|sf_vol_10|sf_looping|sf_stream_from_hd, ["amb_campfire.wav"]),
  ("ambient_rain_roof", sf_looping|sf_priority_3|sf_vol_5|sf_start_at_random_pos|sf_stream_from_hd, ["rain_heavy_roof.wav"]),
  ("ambient_rain_stone", sf_looping|sf_priority_3|sf_vol_5|sf_start_at_random_pos|sf_stream_from_hd, ["rain_heavy_stone.wav"]),
  ("ambient_nuke", sf_priority_8|sf_vol_5|sf_stream_from_hd, ["fx_explosion_nukebig_demo.wav"]),
  ("distant_flies", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["amb_insects_wasteland_flies_01.wav","amb_insects_wasteland_flies_02.wav","amb_insects_wasteland_flies_03.wav","amb_insects_wasteland_flies_04.wav","amb_insects_wasteland_flies_05.wav","amb_insects_wasteland_flies_06.wav","amb_insects_wasteland_flies_07.wav","amb_insects_wasteland_flies_08.wav","amb_insects_wasteland_flies_09.wav","amb_insects_wasteland_flies_10.wav","amb_insects_wasteland_flies_11.wav","amb_insects_wasteland_flies_12.wav"]),
  ("distant_canyonwind", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["amb_canyonwind_01.wav","amb_canyonwind_02.wav","amb_canyonwind_03.wav","amb_canyonwind_04.wav"]),
  ("distant_debris", sf_priority_3|sf_vol_8, ["amb_dstrydcty_debris_02.wav","amb_dstrydcty_debris_03.wav","amb_dstrydcty_debris_04.wav","amb_dstrydcty_debris_05.wav","amb_dstrydcty_debris_06.wav","amb_dstrydcty_debris_07.wav"]),
  ("distant_cricket", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["amb_insects_wasteland_cricket_01.wav","amb_insects_wasteland_cricket_02.wav","amb_insects_wasteland_cricket_03.wav","amb_insects_wasteland_cricket_04.wav","amb_insects_wasteland_cricket_05.wav","amb_insects_wasteland_cricket_06.wav","amb_insects_wasteland_cricket_07.wav","amb_insects_wasteland_cricket_08.wav","amb_insects_wasteland_cricket_09.wav","amb_insects_wasteland_cricket_10.wav","amb_insects_wasteland_cricket_11.wav","amb_insects_wasteland_cricket_12.wav","amb_insects_wasteland_cricket_13.wav","amb_insects_wasteland_cricket_14.wav","amb_insects_wasteland_cricket_15.wav"]),
  ("distant_rustle", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["amb_insects_wasteland_rustle_01.wav","amb_insects_wasteland_rustle_02.wav","amb_insects_wasteland_rustle_03.wav","amb_insects_wasteland_rustle_04.wav","amb_insects_wasteland_rustle_05.wav","amb_insects_wasteland_rustle_06.wav","amb_insects_wasteland_rustle_07.wav","amb_insects_wasteland_rustle_08.wav","amb_insects_wasteland_rustle_09.wav","amb_insects_wasteland_rustle_10.wav"]),
  ("distant_creaking", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["amb_r_creaking_01.wav","amb_r_creaking_02.wav","amb_r_creaking_03.wav","amb_r_creaking_04.wav","amb_r_creaking_05.wav","amb_r_creaking_06.wav","amb_r_creaking_07.wav","amb_r_creaking_08.wav","amb_r_creaking_09.wav","amb_r_creaking_10.wav","amb_r_creaking_11.wav","amb_r_creaking_12.wav","amb_r_creaking_13.wav","amb_r_creaking_14.wav","amb_r_creaking_15.wav","amb_r_creaking_16.wav","amb_r_creaking_17.wav","amb_r_creaking_18.wav"]),
  ("distant_city_creaking", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["amb_regions_city_creaking_b_01.wav","amb_regions_city_creaking_b_02.wav","amb_regions_city_creaking_b_03.wav","amb_regions_city_creaking_b_04.wav","amb_regions_city_creaking_b_05.wav"]),
  ("distant_cicadas", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["sfx_desert_cicadas_os_01.wav","sfx_desert_cicadas_os_02.wav","sfx_desert_cicadas_os_03.wav","sfx_desert_cicadas_os_04.wav"]),
  ("distant_city_gunshots", sf_priority_8|sf_vol_8|sf_stream_from_hd, ["ambr_city_gunshots_low_01.wav","ambr_city_gunshots_low_02.wav","ambr_city_gunshots_low_03.wav","ambr_city_gunshots_low_04.wav","ambr_city_gunshots_low_05.wav"]),
  ("distant_gunshots", sf_priority_8|sf_vol_8|sf_stream_from_hd, ["sfx_desert_dstntbttl_os_01.wav","sfx_desert_dstntbttl_os_02.wav","sfx_desert_dstntbttl_os_03.wav","sfx_desert_dstntbttl_os_04.wav","sfx_desert_dstntbttl_os_05.wav","sfx_desert_dstntbttl_os_06.wav","amb_dstrydcty_guna_01.wav","amb_dstrydcty_guna_02.wav","amb_dstrydcty_guna_03.wav","amb_dstrydcty_guna_04.wav","amb_dstrydcty_guna_05.wav","amb_dstrydcty_guna_06.wav","amb_dstrydcty_guna_07.wav","amb_dstrydcty_gunb_01.wav","amb_dstrydcty_gunb_02.wav","amb_dstrydcty_gunb_03.wav","amb_dstrydcty_gunb_04.wav","amb_dstrydcty_gunb_05.wav","amb_dstrydcty_gunb_06.wav","amb_dstrydcty_gunb_07.wav"]),
  ("distant_eagle", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["sfx_desert_eagle_os_01.wav","sfx_desert_eagle_os_02.wav","sfx_desert_eagle_os_03.wav","sfx_desert_eagle_os_04.wav","sfx_desert_eagle_os_05.wav"]),
  ("distant_hawk", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["sfx_desert_hawk_os_01.wav","sfx_desert_hawk_os_02.wav","sfx_desert_hawk_os_03.wav","sfx_desert_hawk_os_04.wav"]),
  ("distant_rumble", sf_2d|sf_priority_3|sf_vol_8|sf_stream_from_hd, ["ambr_generic_rumble_01_2d.wav","ambr_generic_rumble_02_2d.wav"]),
  ("distant_metalrumble", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["sfx_distantmetalrumble_0s_01.wav","sfx_distantmetalrumble_0s_02.wav"]),
  ("distant_plain_wind", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["ambr_plains_windgust_01.wav","ambr_plains_windgust_02.wav","ambr_plains_windgust_03.wav","ambr_plains_windgust_04.wav","ambr_plains_windgust_05.wav","ambr_plains_windgust_06.wav","ambr_plains_windgust_07.wav","ambr_plains_windgust_08.wav","ambr_plains_windgust_09.wav","ambr_plains_windgust_10.wav","ambr_plains_windgust_11.wav","ambr_plains_windgust_12.wav","ambr_plains_windgust_13.wav"]),
  ("distant_wind", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["sfx_windgust_a01.wav","sfx_windgust_a02.wav","sfx_windgust_a03.wav","sfx_windgust_a04.wav","sfx_windgust_b01.wav","sfx_windgust_b02.wav","sfx_windgust_b03.wav","sfx_windgust_b04.wav","sfx_windgust_c01.wav","sfx_windgust_c02.wav","sfx_windgust_c03.wav","sfx_windgust_c04.wav","sfx_windgust_d01.wav","sfx_windgust_d02.wav","sfx_windgust_d03.wav","sfx_windgust_d04.wav","sfx_windgust_e01.wav","sfx_windgust_e02.wav","sfx_windgust_e03.wav","sfx_windgust_e04.wav","sfx_windgust_f01.wav","sfx_windgust_f02.wav","sfx_windgust_f03.wav","sfx_windgust_f04.wav","sfx_windgust_g01.wav","sfx_windgust_g02.wav","sfx_windgust_g03.wav","sfx_windgust_g04.wav"]),
  ("distant_howls", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["sfx_howls_01.wav","sfx_howls_02.wav","sfx_howls_03.wav","sfx_howls_04.wav","sfx_howls_05.wav","sfx_howls_06.wav"]),
  ("distant_vultures", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["sfx_vultures_01.wav""sfx_vultures_02.wav""sfx_vultures_03.wav""sfx_vultures_04.wav"]),
  ("distant_sand", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["sfx_desert_sand_os_01.wav","sfx_desert_sand_os_02.wav","sfx_desert_sand_os_03.wav","sfx_desert_sand_os_04.wav","sfx_desert_sand_os_05.wav","sfx_desert_sand_os_06.wav","sfx_desert_sand_os_07.wav","sfx_desert_sand_os_08.wav","sfx_desert_sand_os_09.wav","sfx_desert_sand_os_10.wav"]),
  ("distant_snake", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["sfx_desert_snake_os_01.wav","sfx_desert_snake_os_02.wav","sfx_desert_snake_os_03.wav","sfx_desert_snake_os_04.wav","sfx_desert_snake_os_05.wav","sfx_desert_snake_os_06.wav","sfx_desert_snake_os_07.wav"]),
  ("distant_bird", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["sfx_desert_bird-b_os_01.wav","sfx_desert_bird-b_os_02.wav","sfx_desert_bird-b_os_03.wav","sfx_desert_bird-b_os_04.wav","sfx_desert_bird-b_os_05.wav","sfx_desert_bird-b_os_06.wav","sfx_desert_bird-b_os_07.wav","sfx_desert_bird-c_os_01.wav","sfx_desert_bird-c_os_02.wav","sfx_desert_bird-c_os_03.wav","sfx_desert_bird-d_os_01.wav","sfx_desert_bird-d_os_02.wav","sfx_desert_bird-d_os_03.wav","sfx_desert_bird-d_os_04.wav","sfx_desert_bird-e_os_01.wav","sfx_desert_bird-e_os_02.wav","sfx_desert_bird-e_os_03.wav","sfx_desert_bird-f_os_01.wav","sfx_desert_bird-f_os_02.wav","sfx_desert_bird-f_os_03.wav","sfx_desert_bird-f_os_04.wav","sfx_desert_bird-g_os_01.wav","sfx_desert_bird-g_os_02.wav","sfx_desert_bird-g_os_03.wav","sfx_desert_bird-g_os_04.wav","sfx_desert_bird-h_os_01.wav","sfx_desert_bird-h_os_02.wav","sfx_desert_bird-h_os_03.wav","sfx_desert_bird-a_os_01.wav","sfx_desert_bird-a_os_02.wav","sfx_desert_bird-a_os_03.wav"]),
  ("distant_bird_forest", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["ambr_bird_oasis_01.wav","ambr_bird_oasis_02.wav","ambr_bird_oasis_03.wav","ambr_bird_oasis_04.wav","ambr_bird_oasis_05.wav","ambr_bird_oasis_06.wav","ambr_bird_oasis_07.wav","ambr_bird_oasis_08.wav","ambr_bird_oasis_09.wav","ambr_bird_oasis_10.wav","ambr_bird_oasis_11.wav"]),
  ("distant_bird_carrion", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["ambr_bird_carrion_09.wav","ambr_bird_carrion_11.wav","ambr_bird_carrion_12.wav","ambr_bird_carrion_13.wav","ambr_bird_carrion_01.wav","ambr_bird_carrion_02.wav","ambr_bird_carrion_03.wav","ambr_bird_carrion_04.wav","ambr_bird_carrion_05.wav","ambr_bird_carrion_06.wav","ambr_bird_carrion_07.wav","ambr_bird_carrion_08.wav"]),
  ("distant_alarm", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["amb_cmpmcrn_alarm.wav"]),
  ("distant_electric", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["amb_electricarc_small_a_01.wav","amb_electricarc_small_a_02.wav","amb_electricarc_small_a_03.wav","amb_electricarc_small_a_04.wav","amb_electricarc_small_b_01.wav","amb_electricarc_small_b_02.wav","amb_electricarc_small_b_03.wav","amb_electricarc_small_b_04.wav"]),
  ("distant_machine", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["amb_cmpmcrn_machine_01.wav","amb_cmpmcrn_machine_02.wav","amb_cmpmcrn_machine_03.wav","amb_cmpmcrn_machine_04.wav","amb_cmpmcrn_machine_05.wav","amb_cmpmcrn_machine_06.wav","amb_cmpmcrn_machineb_01.wav","amb_cmpmcrn_machineb_02.wav","amb_cmpmcrn_machineb_03.wav","amb_cmpmcrn_machineb_04.wav","amb_cmpmcrn_machineb_05.wav","amb_cmpmcrn_machineb_06.wav"]),
  ("distant_tooldrop", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["amb_cmpmcrn_tooldrop_01.wav","amb_cmpmcrn_tooldrop_02.wav","amb_cmpmcrn_tooldrop_03.wav","amb_cmpmcrn_tooldrop_04.wav","amb_cmpmcrn_tooldrop_05.wav","amb_cmpmcrn_tooldrop_06.wav",]),
  ("ambient_pipewater", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["amb_pipewater_a_01_lp.wav","amb_pipewater_a_02_lp.wav","amb_pipewater_a_03_lp.wav","amb_pipewater_d_01_lp.wav"]),
  ("distant_cantoss", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["sfx_cantossdistant_os_01.wav","sfx_cantossdistant_os_02.wav","sfx_cantossdistant_os_03.wav","sfx_cantossdistant_os_04.wav","sfx_cantossdistant_os_05.wav","sfx_cantossdistant_os_06.wav"]),
  ("distant_leaves", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["sfx_desert_leaves_os_01.wav","sfx_desert_leaves_os_02.wav","sfx_desert_leaves_os_03.wav","sfx_desert_leaves_os_04.wav"]),
  ("distant_twigbreak", sf_priority_3|sf_vol_8|sf_stream_from_hd, ["sfx_desert_twigbreak_os_01.wav","sfx_desert_twigbreak_os_02.wav","sfx_desert_twigbreak_os_03.wav","sfx_desert_twigbreak_os_04.wav","sfx_desert_twigbreak_os_05.wav"]),
  
  ("dog_bark", sf_priority_5|sf_vol_15|sf_stream_from_hd, ["ambient_random_dog_2.wav"]),
  ("dog_whine", sf_priority_5|sf_vol_4|sf_stream_from_hd, ["dog_whine1.wav","dog_whine2.wav","dog_whine3.wav"]),
  ("dog_growl", sf_priority_5|sf_vol_2|sf_stream_from_hd, ["dog_growl3.wav"]),

  ("heli_loop", sf_looping|sf_priority_4|sf_vol_7|sf_stream_from_hd, ["heli.ogg"]),
  ("car_loop", sf_looping|sf_priority_4|sf_vol_8, ["car_loop.wav"]),

  ("heartbeat", sf_2d|sf_looping|sf_vol_3|sf_stream_from_hd, ["ui_health_heartbeat_a_lp.wav"]),
  ("heartbeat_low", sf_2d|sf_looping|sf_vol_3|sf_stream_from_hd, ["ui_health_heartbeat_b_lp.wav"]),
  #("marker_added", sf_2d|sf_vol_1|sf_stream_from_hd, ["ui_popupmapmarkeradded.wav"]),	#annoying
  ("marker_added", sf_2d|sf_vol_1|sf_stream_from_hd, ["amb_insects_wasteland_rustle_03.wav"]),
  ("honour_pos", sf_2d|sf_vol_2|sf_stream_from_hd, ["new_rank_good.wav"]),
  ("honour_neg", sf_2d|sf_vol_2|sf_stream_from_hd, ["new_rank_evil.wav"]),

  ("encounter_cannibal", sf_2d|sf_vol_8|sf_stream_from_hd, ["greeting_cannibal_1.wav", "greeting_cannibal_2.wav", "greeting_cannibal_3.wav"]),
  ("encounter_drunk",sf_2d|sf_vol_8|sf_stream_from_hd, ["greeting_drunkards.wav",]),
  ("encounter_bennet",sf_2d|sf_vol_8|sf_stream_from_hd, ["greeting_bennet_clan_1.wav","greeting_bennet_clan_2.wav","greeting_bennet_clan_1.wav","greeting_bennet_clan_3.wav",]),

  ("radio_1",sf_priority_3|sf_vol_8|sf_looping|sf_stream_from_hd, ["27511__drni__old-radio-noise-findstation-switchoff-ukw.ogg","80399__benboncan__radio-garble.ogg"]),
  ("radio_static",sf_priority_3|sf_vol_8|sf_looping|sf_stream_from_hd, ["xxx_radiostatictestsmall.wav"]),
  ("radio_signal",sf_2d|sf_vol_8|sf_stream_from_hd, ["ui_radio_signallost.wav"]),

  ("scream_man",sf_priority_10|sf_vol_10|sf_stream_from_hd, ["horror_scream_man_0.wav","horror_scream_man_2.wav","horror_scream_man_3.wav","horror_scream_man_4.wav","horror_scream_man_1.wav"]),
  ("usa_cry", sf_priority_10|sf_vol_2|sf_stream_from_hd, ["us_new_taunt_1.wav", "us_new_taunt_2.wav", "us_new_taunt_3.wav", "us_new_taunt_4.wav", "us_new_taunt_5.wav"]),
  ("usa_reloading", sf_priority_10|sf_vol_2|sf_stream_from_hd, ["us_new_reloading.wav","survivor_reloading1.wav","survivor_reloading2.wav"]),
  ("usa_grenade", sf_priority_10|sf_vol_2|sf_stream_from_hd, ["us_new_grenade_1.wav", "us_new_grenade_2.wav","survivor_frag.wav"]),
  ("usa_grenade_smoke", sf_priority_10|sf_vol_2|sf_stream_from_hd, ["us_new_smokegrenade.wav","survivor_smoke.wav"]),
  ("warcry", sf_priority_10|sf_vol_10|sf_stream_from_hd, ["yell1.wav", "yell2.wav", "yell3.wav", "yell4.wav", "yell5.wav", "yell6.wav", "yell7.wav", "yell8.wav", "yell9.wav", "yell10.wav", "yell11.wav", "yell12.wav", "yell13.wav", "yell14.wav", "yell15.wav", "yell16.wav", "yell17.wav", "yell18.wav", "yell19.wav", "yell20.wav", "yell21.wav", "yell22.wav", "yell23.wav", "yell24.wav", "yell25.wav", "yell26.wav", "yell27.wav", "yell28.wav", "yell29.wav", "yell30.wav", "yell31.wav", "yell32.wav"]), #"yell33.wav"
  ("man_cough", sf_priority_8|sf_vol_8|sf_stream_from_hd, ["man_cough_1.wav", "man_cough_2.wav", "man_cough_3.wav"]),
  ("man_random", sf_vol_6|sf_stream_from_hd, ["greeting_usa_4.wav","greeting_random_that_boy_aint.wav","greeting_random_oh_my_god_look.wav","greeting_crazy_hug_a.wav","greeting_crazy_hug_b.wav",
  "greeting_scavenger_1.wav","greeting_scavenger_3.wav","greeting_scavenger_4.wav","greeting_scavenger_5.wav","greeting_southern_1.wav","greeting_southern_2.wav","greeting_southern_2b.wav","greeting_random_whats_up_yall.wav",
  "Hello-SoundBible.com-218208532.wav"]),
  ("generic_robot_1", sf_priority_5|sf_vol_10|sf_stream_from_hd, ["generic_robot_1.ogg"]),

  ("guitar_solo",	sf_priority_3|sf_vol_4|sf_looping|sf_start_at_random_pos|sf_stream_from_hd, ["guitar1.ogg","guitar2.ogg","guitar3.ogg","RBL_See_My_Jumper_Hanging_On_the_Line.ogg"]),

  ("spider_attack", sf_priority_5|sf_vol_8|sf_stream_from_hd, ["spider_battle1.wav","spider_battle2.wav"]),
  ("spider_death", sf_priority_5|sf_vol_8|sf_stream_from_hd, ["spider_death.wav"]),

  ("infected_standard_1", sf_priority_7|sf_vol_5|sf_stream_from_hd, ["infected_standard_1.wav"]),
  ("infected_standard_2", sf_priority_7|sf_vol_6, ["infected_standard_2.wav"]),
  ("infected_alerted_2", sf_priority_7|sf_vol_8, ["infected_alerted_2.wav", "infected_short_1.wav"]),
  ("infected_hit", sf_priority_7|sf_vol_10, ["Zombie_hit_01.wav", "Zombie_hit_02.wav", "Zombie_hit_03.wav"]),
  ("infected_grunt", sf_priority_6|sf_vol_8, ["Zombie_01.wav", "Zombie_02.wav", "Zombie_03.wav", "Zombie_04.wav", "Zombie_05.wav", "Zombie_06.wav", "Zombie_07.wav", "Zombie_08.wav", "Zombie_09.wav", "Zombie_10.wav", "Zombie_11.wav", "Zombie_12.wav", "Zombie_13.wav", "Zombie_14.wav", "Zombie_15.wav", "Zombie_16.wav", "Zombie_17.wav", "Zombie_18.wav", "Zombie_19.wav", "Zombie_20.wav", "Zombie_21.wav", "Zombie_22.wav"]),
  ("infected_grunt_long",sf_priority_5|sf_vol_8, ["Zombie_01.wav", "Zombie_02.wav", "Zombie_03.wav", "Zombie_04.wav", "Zombie_05.wav", "Zombie_06.wav", "Zombie_07.wav", "Zombie_08.wav", "Zombie_09.wav", "Zombie_10.wav", "Zombie_11.wav", "Zombie_12.wav", "Zombie_13.wav", "Zombie_14.wav", "Zombie_15.wav", "Zombie_16.wav", "Zombie_17.wav", "Zombie_18.wav", "Zombie_19.wav", "Zombie_20.wav", "Zombie_21.wav", "Zombie_22.wav"]),
  ("infected_die", sf_priority_8|sf_vol_10, ["Zombie_die_01.wav", "Zombie_die_02.wav", "Zombie_die_03.wav"]),
  ("infected_hit_male", sf_priority_7|sf_vol_10, ["infected_hit.wav"]),
  ("infected_hit_female", sf_priority_7|sf_vol_10, ["infected_hit_female.wav"]),    

  ("nz_hit", sf_priority_5|sf_vol_7, ["nzh2.wav", "nzh3.wav", "nzh4.wav", "nzh5.wav", "nzh6.wav", "nzh7.wav", "nzh8.wav", "nzh9.wav", "nzh10.wav", "nzh11.wav", "nzh12.wav", "nzh13.wav", "nzh14.wav", "nzh15.wav", "nzh16.wav", "nzh17.wav", "nzh18.wav", "nzh19.wav", "nzh20.wav", "nzh21.wav", "nzh22.wav", "nzh23.wav", "nzs1.wav"]),
  ("nz_die", sf_priority_6|sf_vol_8, ["nzd2.wav", "nzd3.wav", "nzd4.wav", "nzd5.wav", "nzd6.wav", "nzd7.wav", "nzd8.wav", "nzd9.wav", "nzd10.wav", "nzd11.wav", "nzg1.wav"]),
  ("nz_victory", sf_priority_8|sf_vol_13, ["nzs2.wav", "nzs3.wav", "nzs4.wav", "nzs5.wav", "nzs6.wav", "nzs7.wav", "nzs8.wav", "nzs9.wav"]),
  ("nz_grunt", sf_priority_4|sf_vol_4, ["nzg2.wav", "nzg3.wav", "nzg4.wav", "nzg5.wav", "nzg6.wav", "nzg7.wav", "nzg8.wav", "nzg9.wav", "nzg10.wav", "nzg11.wav", "nzg12.wav", "nzg13.wav", "nzg14.wav", "nzg15.wav", "nzg16.wav", "nzg17.wav", "nzg18.wav", "nzg19.wav", "nzg20.wav", "nzg21.wav", "nzh1.wav"]),
  ("nz_stun", sf_priority_3|sf_vol_8, ["nzs2.wav", "nzs3.wav", "nzs4.wav", "nzs5.wav", "nzs6.wav", "nzs7.wav", "nzs8.wav", "nzs9.wav"]),
  ("nz_grunt_long", sf_priority_5|sf_vol_7, ["nzg2.wav", "nzg3.wav", "nzg4.wav", "nzg5.wav", "nzg6.wav", "nzg7.wav", "nzg8.wav", "nzg9.wav", "nzg10.wav", "nzg11.wav", "nzg12.wav", "nzg13.wav", "nzg14.wav", "nzg15.wav", "nzg16.wav", "nzg17.wav", "nzg18.wav", "nzg19.wav", "nzg20.wav", "nzg21.wav", "nzh1.wav"]),

  #gamorrean sounds
  ("gamorrean_die",sf_priority_8|sf_vol_10|sf_stream_from_hd, ["gamorrean_death1.ogg","gamorrean_death2.ogg","gamorrean_death3.ogg","gamorrean_falling1.ogg"]),
  ("gamorrean_grunt",sf_priority_6|sf_vol_8|sf_stream_from_hd, ["gamorrean_taunt1.ogg","gamorrean_taunt2.ogg","gamorrean_gloat1.ogg","gamorrean_anger2.ogg"]),
  ("gamorrean_grunt_long",sf_priority_5|sf_vol_8|sf_stream_from_hd, ["gamorrean_taunt1.ogg","gamorrean_taunt2.ogg","gamorrean_gloat1.ogg","gamorrean_anger2.ogg"]),
  ("gamorrean_hit",sf_priority_7|sf_vol_10|sf_stream_from_hd, ["gamorrean_pain25.ogg","gamorrean_pain50.ogg","gamorrean_pain75.ogg","gamorrean_pain100.ogg","gamorrean_gasp.ogg","gamorrean_land1.ogg"]),
  ("gamorrean_victory",sf_priority_5|sf_vol_10|sf_stream_from_hd, ["gamorrean_victory1.ogg","gamorrean_anger2.ogg","gamorrean_taunt1.ogg","gamorrean_taunt2.ogg","gamorrean_gloat1.ogg"]),
  ("gamorrean_yell",sf_priority_6|sf_vol_10|sf_stream_from_hd, ["gamorrean_anger2.ogg","gamorrean_victory1.ogg","gamorrean_taunt1.ogg","gamorrean_taunt2.ogg","gamorrean_gloat1.ogg"]),

  #battledroid sounds
  ("battledroid_die",sf_priority_8|sf_vol_10, ["battledroid_pain25.ogg","battledroid_pain50.ogg","battledroid_pain75.ogg"]),
  ("battledroid_grunt",sf_priority_6|sf_vol_8, ["battledroid_talk01.ogg","battledroid_talk02.ogg","battledroid_talk03.ogg"]),
  ("battledroid_grunt_long",sf_priority_5|sf_vol_8, ["battledroid_talk01.ogg","battledroid_talk02.ogg","battledroid_talk03.ogg"]),
  ("battledroid_hit",sf_priority_7|sf_vol_10, ["battledroid_pain25.ogg","battledroid_pain50.ogg","battledroid_pain75.ogg"]),
  ("battledroid_victory",sf_priority_5|sf_vol_10, ["battledroid_talk01.ogg","battledroid_talk02.ogg","battledroid_talk03.ogg"]),
  ("battledroid_yell",sf_priority_6|sf_vol_10, ["battleroid_talk01.ogg","battledroid_talk02.ogg","battledroid_talk03.ogg"]),

  ### Dice game ### Dice game ###
   ("dice_roll",sf_priority_10|sf_vol_10, ["dice_roll.wav"]),
  ### Dice game ### Dice game ### END ###

# Bartenders - Mongol
# Line ideas submitted largely by Sherry

 ("bartender_male",sf_2d|sf_vol_8|sf_stream_from_hd, ["bar_1.wav","bar_2.wav","bar_3.wav","bar_4.wav","bar_5.wav","bar_6.wav","bar_7.wav","bar_8.wav",]), 
 ("bartender_female",sf_2d|sf_vol_8|sf_stream_from_hd, ["bar_fem_1.wav","bar_fem_2.wav","bar_fem_3.wav","bar_fem_4.wav","bar_fem_5.wav","bar_fem_6.wav","bar_fem_7.wav","bar_fem_8.wav",]), 
 
]
# modmerger_start version=201 type=2
try:
    component_name = "sounds"
    var_set = { "sounds" : sounds }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
