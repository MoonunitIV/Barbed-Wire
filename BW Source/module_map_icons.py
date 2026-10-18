from header_map_icons import *
from module_constants import *
from header_operations import *
from header_triggers import *
from ID_sounds import *

from compiler import *
####################################################################################################################
#  Each map icon record contains the following fields:
#  1) Map icon id: used for referencing map icons in other files.
#     The prefix icon_ is automatically added before each map icon id.
#  2) Map icon flags. See header_map icons.py for a list of available flags
#  3) Mesh name.
#  4) Scale.
#  5) Sound.
#  6) Offset x position for the flag icon.
#  7) Offset y position for the flag icon.
#  8) Offset z position for the flag icon.
####################################################################################################################

banner_scale = 0.3
# avatar_scale = 0.25
avatar_scale = 0.15
town_scale = 0.35
base_scale = 1

map_icons = [
  ("player",0,"map_troop_1", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0),
  ("player_horseman",0,"dummy_mesh", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0),
  # ("player_horseman",0,"player_horseman", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("gray_knight",0,"map_troop_3", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0),
  # ("gray_knight",0,"knight_a", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("vaegir_knight",0,"map_troop_1", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0),
  # ("vaegir_knight",0,"knight_b", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("flagbearer_a",0,"map_troop_3", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0),
  # ("flagbearer_a",0,"flagbearer_a", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("flagbearer_b",0,"map_troop_3", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0),
  # ("flagbearer_b",0,"flagbearer_b", avatar_scale, snd_gallop, 0.15, 0.173, 0),
  ("peasant",0,"map_troop_1", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  # ("peasant",0,"peasant_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  # ("khergit",0,"map_troop_3", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  # ("khergit",0,"khergit_horseman", avatar_scale,snd_gallop, 0.15, 0.173, 0),
  ("khergit_horseman_b",0,"map_troop_1", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  # ("khergit_horseman_b",0,"khergit_horseman_b", avatar_scale,snd_gallop, 0.15, 0.173, 0),
  ("axeman",0,"map_troop_3", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  # ("axeman",0,"bandit_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("woman",0,"woman_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("woman_b",0,"woman_b", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("town",mcn_no_shadow,"map_town_a", town_scale,0),
  ("town_steppe",mcn_no_shadow,"map_town_steppe_a", town_scale,0),
  ("town_desert",mcn_no_shadow,"map_fort_wood", town_scale,0),
  ("village_a",mcn_no_shadow,"map_village_a", town_scale, 0),
  ("village_b",mcn_no_shadow,"map_village_b", town_scale, 0),
  # ("village_c",mcn_no_shadow,"dummy_mesh", town_scale, 0),
  # ("village_burnt_a",mcn_no_shadow,"dummy_mesh", town_scale, 0),
  # ("village_deserted_a",mcn_no_shadow,"dummy_mesh", town_scale, 0),
  # ("village_burnt_b",mcn_no_shadow,"dummy_mesh", town_scale, 0),
  # ("village_deserted_b",mcn_no_shadow,"dummy_mesh", town_scale, 0),
  # ("village_burnt_c",mcn_no_shadow,"dummy_mesh", town_scale, 0),
  # ("village_deserted_c",mcn_no_shadow,"dummy_mesh", town_scale, 0),
  ("village_snow_a",mcn_no_shadow,"dummy_mesh", town_scale, 0),
  # ("village_snow_burnt_a",mcn_no_shadow,"dummy_mesh", town_scale, 0),
  # ("village_snow_deserted_a",mcn_no_shadow,"dummy_mesh", town_scale, 0),
  ("camp",mcn_no_shadow,"camp_tent", avatar_scale, 0),
  ("ship",mcn_no_shadow,"boat_sail_on", avatar_scale, snd_footstep_grass, 0.0, 0.05, 0),
  ("ship_on_land",mcn_no_shadow,"boat_sail_off", avatar_scale, 0),
  ("castle_a",mcn_no_shadow,"map_fort", town_scale,0),
  ("castle_b",mcn_no_shadow,"map_star_fort", town_scale,0),
  # ("castle_c",mcn_no_shadow,"dummy_mesh", town_scale,0),
  # ("castle_d",mcn_no_shadow,"dummy_mesh", town_scale,0),
  # ("town_snow",mcn_no_shadow,"dummy_mesh", town_scale,0),
  # ("castle_snow_a",mcn_no_shadow,"dummy_mesh", town_scale,0),
  # ("castle_snow_b",mcn_no_shadow,"dummy_mesh", town_scale,0),
  ("mule",0,"icon_mule", 0.2,snd_footstep_grass, avatar_scale, 0.25, 0),
  ("cattle",0,"icon_cow", 0.2,snd_footstep_grass, avatar_scale, 0.25, 0),
  # ("training_ground",mcn_no_shadow,"dummy_mesh", town_scale,0),

  ("bridge_a",mcn_no_shadow,"map_river_bridge_a", base_scale,0),
  ("bridge_b",mcn_no_shadow,"map_river_bridge_b", base_scale,0),
  # ("bridge_snow_a",mcn_no_shadow,"dummy_mesh", 1.0,0),

##new
  ("bridge_a2",mcn_no_shadow,"map_river_bridge_a2", base_scale,0),

#player
  ("player_arrow",mcn_no_shadow,"player_arrow", avatar_scale,0),
  ("target_arrow",mcn_no_shadow,"target_arrow", avatar_scale,0),
#troops
  ("map_jeep_beige",0,"map_jeep_beige", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("map_jeep_black",0,"map_jeep_black", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("map_jeep_green",0,"map_jeep_green", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("map_jeep_greenb",0,"map_jeep_greenb", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("map_jeep_tan",0,"map_jeep_tan", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),

  ("map_pickup_a",0,"map_pickup_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("map_pickup_b",0,"map_pickup_b", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  ("map_pickup_c",0,"map_pickup_c", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  # ("map_pickup_d",0,"map_pickup_d", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
  # ("map_pickup_d2",0,"map_pickup_d2", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),

  ("map_uruk",0,"map_uruk", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0),
#camping
  ("map_camp_1",mcn_no_shadow,"map_camp_1", avatar_scale,0),
  ("map_camp_2",mcn_no_shadow,"map_camp_2", avatar_scale,0),

#bryt
  ("map_camp_3",mcn_no_shadow,"bell_tent_old", avatar_scale,0),
  ("map_camp_4",mcn_no_shadow,"command_tent_old", avatar_scale,0),
  ("map_camp_5",mcn_no_shadow,"bell_tent_icon", avatar_scale,0),
  
  ("map_entrench_1",mcn_no_shadow,"entrench_old_icon", avatar_scale,0),
  ("map_entrench_2",mcn_no_shadow,"entrench_tent_icon", avatar_scale,0),
  
  ("map_pyre_1",mcn_no_shadow,"funeral_pyre_icon", avatar_scale,0),

#city
  ("map_city_1",mcn_no_shadow,"map_city_1", town_scale,0),
  ("map_city_1b",mcn_no_shadow,"map_city_1b", town_scale,0),
  ("map_city_2",mcn_no_shadow,"map_city_2", town_scale,0),
  ("map_city_2b",mcn_no_shadow,"map_city_2b", town_scale,0),
  ("map_city_3",mcn_no_shadow,"map_city_3", town_scale,0),
  ("map_city_3b",mcn_no_shadow,"map_city_3b", town_scale,0),

  ("map_city_b1",mcn_no_shadow,"map_city_b1", town_scale,0),
  ("map_city_b2",mcn_no_shadow,"map_city_b2", town_scale,0),
  ("map_city_b3",mcn_no_shadow,"map_city_b3", town_scale,0),
  ("map_city_b4",mcn_no_shadow,"map_city_b4", town_scale,0),
  ("map_city_b5",mcn_no_shadow,"map_city_b5", town_scale,0),
  ("map_city_b6",mcn_no_shadow,"map_city_b6", town_scale,0),
  ("map_city_b7",mcn_no_shadow,"map_city_b7", town_scale,0),
  ("map_city_b8",mcn_no_shadow,"map_city_b8", town_scale,0),
  ("map_city_b9",mcn_no_shadow,"map_city_b9", town_scale,0),
  ("map_city_b10",mcn_no_shadow,"map_city_b10", town_scale,0),

#dest city
  ("map_dest_city",mcn_no_shadow,"map_dest_city", town_scale,0),
  ("map_tower_city",mcn_no_shadow,"map_tower_city", town_scale,0),

#forts
  # ("map_fort_1",mcn_no_shadow,"map_fort_1", town_scale,0),
  # ("map_fort_2",mcn_no_shadow,"map_fort_2", town_scale,0),
  # ("map_fort_3",mcn_no_shadow,"map_fort_3", town_scale,0),
#farm
  ("map_farm_1",mcn_no_shadow,"map_farm_1", town_scale,0),
  ("map_farm_2",mcn_no_shadow,"map_farm_2", town_scale,0),
  ("map_farm_3",mcn_no_shadow,"map_farm_3", town_scale,0),
  ("map_farm_4",mcn_no_shadow,"map_farm_4", town_scale,0),
  ("map_farm_5",mcn_no_shadow,"map_farm_5", town_scale,0),
  
#villages
  ("map_wooden_village",mcn_no_shadow,"map_wooden_village", town_scale,0),
  # ("map_shed_2",mcn_no_shadow,"map_shed_2", town_scale,0),
#towns
  ("map_entenaii_town",mcn_no_shadow,"map_entenaii_town", town_scale,0),
  ("map_dominion_town",mcn_no_shadow,"map_dominion_town", town_scale,0),
  ("map_galvae_town",mcn_no_shadow,"map_galvae_town", town_scale,0),
  ("map_union_town",mcn_no_shadow,"map_union_town", town_scale,0),
  ("map_vitzland_town",mcn_no_shadow,"map_vitzland_town", town_scale,0),
  ("map_republic_town",mcn_no_shadow,"map_republic_town", town_scale,0),
  
#other buildings
  ("map_house",mcn_no_shadow,"map_house", town_scale,0),
  ("map_factory",mcn_no_shadow,"map_factory", town_scale,0),
  ("map_bunker",mcn_no_shadow,"map_concrete_bunker", town_scale,0),
  ("map_tower",mcn_no_shadow,"map_tower", town_scale,0),
  ("map_tower2",mcn_no_shadow,"map_tower2", town_scale,0),
  ("map_hideout",mcn_no_shadow,"map_hideout", town_scale,0),
  ("map_razed_city",mcn_no_shadow,"bfy_map_town_a", town_scale,0),
  ("map_mercenary_camp",mcn_no_shadow,"map_mercenary_camp", town_scale,0),
  ("map_monastery",mcn_no_shadow,"map_monastery", town_scale,0),
  ("map_sacred_forest",mcn_no_shadow,"map_sacred_forest", town_scale,0),
  ("bandit_lair",mcn_no_shadow,"map_bandit_lair", town_scale, 0),
  ("bandit_camp",mcn_no_shadow,"map_bandit_camp", town_scale, 0),

#other
  ("map_boat_1", mcn_no_shadow, "map_boat_1", base_scale, 0, 0, 0, 0),
  # ("map_boat_2", mcn_no_shadow, "map_boat_2", base_scale, 0, 0, 0, 0),
  ("map_dummy", mcn_no_shadow, "dummy_mesh", town_scale, 0, 0, 0, 0),
  ("map_rad", mcn_no_shadow, "map_rad", town_scale, 0, 0, 0, 0),


  # ("region_banner",mcn_no_shadow,"map_test", 2.0, 0,
   # [
     # (ti_on_init_map_icon,
      # [
        # # (store_trigger_param_1, ":party_no"),
        # # (call_script, "script_get_closest_center", ":party_no"),
        # # (assign, ":nearest_center", reg0),

        # # (party_get_slot, ":leader_troop", ":nearest_center", slot_town_lord),
        # # (try_begin),
            # # (ge, ":leader_troop", 0),

            # # (cur_map_icon_set_tableau_material, "tableau_custom_banner_tall", ":leader_troop"),
            # # (cur_map_icon_set_tableau_material, "tableau_custom_banner_tall", "trp_player"),
        # # (try_end),

        # ]),
     # ]),
#

  # ("custom_banner_01",0,"custom_map_banner_01", banner_scale, 0,
   # [
     # (ti_on_init_map_icon,
      # [
        # (store_trigger_param_1, ":party_no"),
        # (party_get_slot, ":leader_troop", ":party_no", slot_town_lord),
        # (try_begin),
          # (ge, ":leader_troop", 0),
          # (cur_map_icon_set_tableau_material, "tableau_custom_banner_square", ":leader_troop"),
        # (try_end),
        # ]),
     # ]),
  # ("custom_banner_02",0,"custom_map_banner_02", banner_scale, 0,
   # [
     # (ti_on_init_map_icon,
      # [
        # (store_trigger_param_1, ":party_no"),
        # (party_get_slot, ":leader_troop", ":party_no", slot_town_lord),
        # (try_begin),
          # (ge, ":leader_troop", 0),
          # (cur_map_icon_set_tableau_material, "tableau_custom_banner_short", ":leader_troop"),
        # (try_end),
        # ]),
     # ]),
  # ("custom_banner_03",0,"custom_map_banner_03", banner_scale, 0,
   # [
     # (ti_on_init_map_icon,
      # [
        # (store_trigger_param_1, ":party_no"),
        # (party_get_slot, ":leader_troop", ":party_no", slot_town_lord),
        # (try_begin),
          # (ge, ":leader_troop", 0),
          # (cur_map_icon_set_tableau_material, "tableau_custom_banner_tall", ":leader_troop"),
        # (try_end),
        # ]),
     # ]),

  # Banners
  ("banner_01",0,"map_flag_01", banner_scale,0),
  ("banner_02",0,"map_flag_02", banner_scale,0),
  ("banner_03",0,"map_flag_03", banner_scale,0),
  ("banner_04",0,"map_flag_04", banner_scale,0),
  ("banner_05",0,"map_flag_05", banner_scale,0),
  ("banner_06",0,"map_flag_06", banner_scale,0),
  ("banner_07",0,"map_flag_07", banner_scale,0),
  ("banner_08",0,"map_flag_08", banner_scale,0),
  ("banner_09",0,"map_flag_09", banner_scale,0),
  ("banner_10",0,"map_flag_10", banner_scale,0),
  ("banner_11",0,"map_flag_11", banner_scale,0),
  ("banner_12",0,"map_flag_12", banner_scale,0),
  ("banner_13",0,"map_flag_13", banner_scale,0),
  ("banner_14",0,"map_flag_14", banner_scale,0),
  ("banner_15",0,"map_flag_15", banner_scale,0),#was map_flag_f21
  ("banner_16",0,"map_flag_16", banner_scale,0),
  ("banner_17",0,"map_flag_17", banner_scale,0),
  ("banner_18",0,"map_flag_18", banner_scale,0),
  ("banner_19",0,"map_flag_19", banner_scale,0),
  ("banner_20",0,"map_flag_20", banner_scale,0),
  ("banner_21",0,"map_flag_21", banner_scale,0),
  ("banner_22",0,"map_flag_22", banner_scale,0),
  ("banner_23",0,"map_flag_23", banner_scale,0),
  ("banner_24",0,"map_flag_24", banner_scale,0),
  ("banner_25",0,"map_flag_25", banner_scale,0),
  ("banner_26",0,"map_flag_26", banner_scale,0),
  ("banner_27",0,"map_flag_27", banner_scale,0),
  ("banner_28",0,"map_flag_28", banner_scale,0),
  ("banner_29",0,"map_flag_29", banner_scale,0),
  ("banner_30",0,"map_flag_30", banner_scale,0),
  ("banner_31",0,"map_flag_31", banner_scale,0),
  ("banner_32",0,"map_flag_32", banner_scale,0),
  ("banner_33",0,"map_flag_33", banner_scale,0),
  ("banner_34",0,"map_flag_34", banner_scale,0),
  ("banner_35",0,"map_flag_35", banner_scale,0),
  ("banner_36",0,"map_flag_36", banner_scale,0),
  ("banner_37",0,"map_flag_37", banner_scale,0),
  ("banner_38",0,"map_flag_38", banner_scale,0),
  ("banner_39",0,"map_flag_39", banner_scale,0),
  ("banner_40",0,"map_flag_40", banner_scale,0),
  ("banner_41",0,"map_flag_41", banner_scale,0),
  ("banner_42",0,"map_flag_42", banner_scale,0),
  ("banner_43",0,"map_flag_43", banner_scale,0),
  ("banner_44",0,"map_flag_44", banner_scale,0),
  ("banner_45",0,"map_flag_45", banner_scale,0),
  ("banner_46",0,"map_flag_46", banner_scale,0),
  ("banner_47",0,"map_flag_47", banner_scale,0),
  ("banner_48",0,"map_flag_48", banner_scale,0),
  ("banner_49",0,"map_flag_49", banner_scale,0),
  ("banner_50",0,"map_flag_50", banner_scale,0),
  ("banner_51",0,"map_flag_51", banner_scale,0),
  ("banner_52",0,"map_flag_52", banner_scale,0),
  ("banner_53",0,"map_flag_53", banner_scale,0),
  ("banner_54",0,"map_flag_54", banner_scale,0),
  ("banner_55",0,"map_flag_55", banner_scale,0),
  ("banner_56",0,"map_flag_56", banner_scale,0),
  ("banner_57",0,"map_flag_57", banner_scale,0),
  ("banner_58",0,"map_flag_58", banner_scale,0),
  ("banner_59",0,"map_flag_59", banner_scale,0),
  ("banner_60",0,"map_flag_60", banner_scale,0),
  ("banner_61",0,"map_flag_61", banner_scale,0),
  ("banner_62",0,"map_flag_62", banner_scale,0),
  ("banner_63",0,"map_flag_63", banner_scale,0),
  # ("banner_64",0,"map_flag_d01", banner_scale,0),
  # ("banner_65",0,"map_flag_d02", banner_scale,0),
  # ("banner_66",0,"map_flag_d03", banner_scale,0),
  # ("banner_67",0,"map_flag_d04", banner_scale,0),
  # ("banner_68",0,"map_flag_d05", banner_scale,0),
  # ("banner_69",0,"map_flag_d06", banner_scale,0),
  # ("banner_70",0,"map_flag_d07", banner_scale,0),
  # ("banner_71",0,"map_flag_d08", banner_scale,0),
  # ("banner_72",0,"map_flag_d09", banner_scale,0),
  # ("banner_73",0,"map_flag_d10", banner_scale,0),
  # ("banner_74",0,"map_flag_d11", banner_scale,0),
  # ("banner_75",0,"map_flag_d12", banner_scale,0),
  # ("banner_76",0,"map_flag_d13", banner_scale,0),
  # ("banner_77",0,"map_flag_d14", banner_scale,0),
  # ("banner_78",0,"map_flag_d15", banner_scale,0),
  # ("banner_79",0,"map_flag_d16", banner_scale,0),
  # ("banner_80",0,"map_flag_d17", banner_scale,0),
  # ("banner_81",0,"map_flag_d18", banner_scale,0),
  # ("banner_82",0,"map_flag_d19", banner_scale,0),
  # ("banner_83",0,"map_flag_d20", banner_scale,0),
  # ("banner_84",0,"map_flag_d21", banner_scale,0),
  # ("banner_85",0,"map_flag_e01", banner_scale,0),
  # ("banner_86",0,"map_flag_e02", banner_scale,0),
  # ("banner_87",0,"map_flag_e03", banner_scale,0),
  # ("banner_88",0,"map_flag_e04", banner_scale,0),
  # ("banner_89",0,"map_flag_e05", banner_scale,0),
  # ("banner_90",0,"map_flag_e06", banner_scale,0),
  # ("banner_91",0,"map_flag_e07", banner_scale,0),
  # ("banner_92",0,"map_flag_e08", banner_scale,0),
  # ("banner_93",0,"map_flag_e09", banner_scale,0),
  # ("banner_94",0,"map_flag_e10", banner_scale,0),
  # ("banner_95",0,"map_flag_e11", banner_scale,0),
  # ("banner_96",0,"map_flag_e12", banner_scale,0),
  # ("banner_97",0,"map_flag_e13", banner_scale,0),
  # ("banner_98",0,"map_flag_e14", banner_scale,0),
  # ("banner_99",0,"map_flag_e15", banner_scale,0),
  # ("banner_100",0,"map_flag_e16", banner_scale,0),
  # ("banner_101",0,"map_flag_e17", banner_scale,0),
  # ("banner_102",0,"map_flag_e18", banner_scale,0),
  # ("banner_103",0,"map_flag_e19", banner_scale,0),
  # ("banner_104",0,"map_flag_e20", banner_scale,0),
  # ("banner_105",0,"map_flag_e21", banner_scale,0),

  # ("banner_106",0,"map_flag_f01", banner_scale,0),
  # ("banner_107",0,"map_flag_f02", banner_scale,0),
  # ("banner_108",0,"map_flag_f03", banner_scale,0),
  # ("banner_109",0,"map_flag_f04", banner_scale,0),
  # ("banner_110",0,"map_flag_f05", banner_scale,0),
  # ("banner_111",0,"map_flag_f06", banner_scale,0),
  # ("banner_112",0,"map_flag_f07", banner_scale,0),
  # ("banner_113",0,"map_flag_f08", banner_scale,0),
  # ("banner_114",0,"map_flag_f09", banner_scale,0),
  # ("banner_115",0,"map_flag_f10", banner_scale,0),
  # ("banner_116",0,"map_flag_f11", banner_scale,0),
  # ("banner_117",0,"map_flag_f12", banner_scale,0),
  # ("banner_118",0,"map_flag_f13", banner_scale,0),
  # ("banner_119",0,"map_flag_f14", banner_scale,0),
  # ("banner_120",0,"map_flag_f15", banner_scale,0),
  # ("banner_121",0,"map_flag_f16", banner_scale,0),
  # ("banner_122",0,"map_flag_f17", banner_scale,0),
  # ("banner_123",0,"map_flag_f18", banner_scale,0),
  # ("banner_124",0,"map_flag_f19", banner_scale,0),
  # ("banner_125",0,"map_flag_f20", banner_scale,0),

  # ("banner_126",0,"map_flag_f01", banner_scale,0),
  # ("banner_127",0,"map_flag_f02", banner_scale,0),
  # ("banner_128",0,"map_flag_f03", banner_scale,0),
  # ("banner_129",0,"map_flag_f04", banner_scale,0),
  # ("banner_130",0,"map_flag_f05", banner_scale,0),
  # ("banner_131",0,"map_flag_f06", banner_scale,0),
  # ("banner_132",0,"map_flag_f07", banner_scale,0),
  # ("banner_133",0,"map_flag_f08", banner_scale,0),
  # ("banner_134",0,"map_flag_f09", banner_scale,0),
  # ("banner_135",0,"map_flag_f10", banner_scale,0),

  ("map_flag_kingdom_a",0,"map_flag_kingdom_a", banner_scale,0),
  ("map_flag_kingdom_b",0,"map_flag_kingdom_b", banner_scale,0),
  ("map_flag_kingdom_c",0,"map_flag_kingdom_c", banner_scale,0),
  ("map_flag_kingdom_d",0,"map_flag_kingdom_d", banner_scale,0),
  ("map_flag_kingdom_e",0,"map_flag_kingdom_e", banner_scale,0),
  ("map_flag_kingdom_f",0,"map_flag_kingdom_f", banner_scale,0),
  ("map_flag_kingdom_g",0,"map_flag_kingdom_g", banner_scale,0),
  ("map_flag_kingdom_h",0,"map_flag_kingdom_h", banner_scale,0),
  ("map_flag_kingdom_i",0,"map_flag_kingdom_i", banner_scale,0),
  ("map_flag_kingdom_j",0,"map_flag_kingdom_j", banner_scale,0),
  ("banner_136",0,"map_flag_15", banner_scale,0),

  # ("map_str_000", mcn_no_shadow, "map_str_000", 5, 0, 0, 0, 0),
  # ("map_str_001", mcn_no_shadow, "map_str_001", 5, 0, 0, 0, 0),
  # ("map_str_002", mcn_no_shadow, "map_str_002", 5, 0, 0, 0, 0),
  # ("map_str_004", mcn_no_shadow, "map_str_004", 5, 0, 0, 0, 0),
  # ("map_str_005", mcn_no_shadow, "map_str_005", 5, 0, 0, 0, 0),
  # ("map_str_006", mcn_no_shadow, "map_str_006", 5, 0, 0, 0, 0),
  # ("map_str_007", mcn_no_shadow, "map_str_007", 5, 0, 0, 0, 0),
  # ("map_str_008", mcn_no_shadow, "map_str_008", 5, 0, 0, 0, 0),
  # ("map_str_010", mcn_no_shadow, "map_str_010", 5, 0, 0, 0, 0),
  # ("map_str_011", mcn_no_shadow, "map_str_011", 5, 0, 0, 0, 0),
  # ("map_str_012", mcn_no_shadow, "map_str_012", 5, 0, 0, 0, 0),
  # ("map_str_013", mcn_no_shadow, "map_str_013", 5, 0, 0, 0, 0),
  # ("map_str_014", mcn_no_shadow, "map_str_014", 5, 0, 0, 0, 0),
  # ("map_str_015", mcn_no_shadow, "map_str_015", 5, 0, 0, 0, 0),
  # ("map_str_016", mcn_no_shadow, "map_str_016", 5, 0, 0, 0, 0),
  # ("map_str_017", mcn_no_shadow, "map_str_017", 5, 0, 0, 0, 0),
  # ("map_str_018", mcn_no_shadow, "map_str_018", 5, 0, 0, 0, 0),
]
# modmerger_start version=201 type=2
try:
    component_name = "map_icons"
    var_set = { "map_icons" : map_icons }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
