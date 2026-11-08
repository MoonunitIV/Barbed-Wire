from header_music import *

from compiler import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
  ("bogus", "none.ogg", 0, 0),
  ("captured", "birds_1.ogg", mtf_persist_until_finished, 0),
  ("empty_village", "birds_1.ogg", mtf_persist_until_finished, 0),
  ("escape", "birds_1.ogg", mtf_persist_until_finished, 0),
  ("victorious_evil", "birds_1.ogg", mtf_persist_until_finished, 0),
  ("wedding", "wedding.ogg", mtf_persist_until_finished, 0),
  ("coronation", "birds_1.ogg", mtf_persist_until_finished, 0),
##new
  ("player_death", "amazing.ogg",mtf_persist_until_finished|mtf_sit_killed, 0),
#main
  ("ross_bugden_something_wicked", "ross_bugden_something_wicked.ogg",mtf_module_track|mtf_culture_all, 0), #mtf_sit_main_title|mtf_start_immediately
  ("rainy_night_in_tallinn", "RAINY_NIGHT_IN_TALLINN.ogg",mtf_module_track, 0),
  
  #("ambient_sandstorm", "amb_sandstorm_lp.wav",mtf_module_track, 0),
#custom
  ("custom_0", "The_Ink_Spots_-_Maybe.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_1", "laura-branigan_self_control.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_2", "abba_lay_all_your_love_on_me.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_3", "desireless_voyage_voyage.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_4", "george-michael_careless_whisper.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_5", "queen_another_one_bites_the_dust.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_6", "Sonne_Rammstein.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_7", "Lil_Baby_Woah.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_8", "Goosebumps.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_9", "02_Enter_Shikari.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_10", "12_Sorry_Youre_Not_a_Winner.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_11", "Ich_tu_dir_weh.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_12", "In_the_Army_Now.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_13", "Where_Is_My_Mind.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_14", "99_Luftballons.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_15", "Coolio_-_Gangstas_Paradise_feat._L.V._Official_Music_Video.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_16", "move_slow.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),
  ("custom_17", "killshot.ogg",mtf_module_track|mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile, mtf_culture_all|mtf_sit_travel|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_town_infiltrate|mtf_sit_arena|mtf_sit_siege|mtf_sit_encounter_hostile),

]
# modmerger_start version=201 type=4
try:
    component_name = "music"
    var_set = { "tracks":tracks, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
