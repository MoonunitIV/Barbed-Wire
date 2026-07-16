    
#######################################################################################################################################
# tocan_ats = [
    # ##VATS DEADEYE
    # # # Hi Tocan!
    # # Thanks dstn!
    # # todo: a lot, 2 prios: 
    # # - shoot spray depending on skill, so they can actually miss
    # # - way to find at least 3 other agents during vats

    # #VARIABLES
    # (ti_before_mission_start,0,0,[
        # (assign, "$vats", 0),
        # (assign, "$vats_agent", -1),
        # (assign, "$vats_restart", -1),
        # # (assign, "$vats_agent_2", -1), 
        # # (assign, "$vats_agent_3", -1),     
        # (assign, "$vats_selected", -1),    
        # (assign, "$vats_ap", 200),  #this will be skill based     
        # # (try_begin),
            # # (store_attribute_level, "$vats_ap", "trp_player", ca_agility),
            # # (val_mul,"$vats_ap",2),
            # # (val_mul,"$vats_ap",10),    
        # # (try_end),    
        # ],
        # []),  
        
    # # #START/CHECK FOR TARGET 
    # (0.0, 0, 0, [
        # (this_or_next|key_clicked, "$key_vats"), #t: for test
        # (eq, "$vats_restart", 1),
        
        # (eq, "$vats", 0),
        # ],
        # [
            # (set_fixed_point_multiplier, 100),
            # (get_player_agent_no,"$g_player"),

            # (agent_get_horse, ":player_horse", "$g_player"), #no horsie

            # (agent_get_wielded_item, ":wielded_item",  "$g_player", 0), #only ranged
            # # (gt, ":wielded_item", -1),
            # # (is_between, ":wielded_item", ranged_weapons_begin, ranged_weapons_end),                

            # (agent_get_ammo, ":ammo", "$g_player", 1),
            # # (gt, ":ammo", 0),
                
            # (try_begin),
                # (ge, "$vats_ap", 25), #t: a minimum - so no spamming without enough points

                # (agent_get_position, pos80, "$g_player"),   
                
                # # (agent_get_horse, ":player_horse", "$g_player"), #no horsie
                # (lt, ":player_horse", 0), #dismounted  

                # (gt, ":wielded_item", -1),
                # (is_between, ":wielded_item", ranged_weapons_begin, ranged_weapons_end),                

                # # (agent_get_ammo, ":ammo", "$g_player"),
                # (gt, ":ammo", 0),
             
                # (agent_get_team, ":p_team", "$g_player"),                
                
                # (assign, "$vats_agent", -1), 
                # # (assign, "$vats_agent_2", -1), 
                # # (assign, "$vats_agent_3", -1),             
                # (assign, "$vats_selected", -1),             
                # (assign, ":shortest_dist", 999999),  
                # # (agent_get_look_position, pos10, "$g_player"), 	# Get Agent's look for math

                # (try_for_agents, ":enemy_agent", pos80, 5000),   #t: choose nearest agent / for test no team check.
                    # (neq, "$g_player", ":enemy_agent"),   
                    # (agent_is_alive, ":enemy_agent"),
                    # (agent_is_human, ":enemy_agent"),
                    # (agent_is_non_player, ":enemy_agent"), 
                    # (agent_get_team, ":a_team", ":enemy_agent"), 
                    # (teams_are_enemies, ":a_team", ":p_team"),                
                    # (agent_get_position, pos81, ":enemy_agent"),
                    
                    # # (neg|position_is_behind_position, pos1, pos2), #in the last test i commented this line and it worked for simply finding the nearest agent

                    # (copy_position, pos82, pos80),
                    # (copy_position, pos83, pos81),

                    # (position_move_z, pos82, 100),
                    # (position_move_z, pos83, 125),

                    # (position_has_line_of_sight_to_position, pos82, pos83),

                    # (get_distance_between_positions, ":distance", pos82, pos83),
                    # (le, ":distance", ":shortest_dist"),
                    
                    # (assign, ":shortest_dist", ":distance"),
                    # (assign, "$vats_agent", ":enemy_agent"),               
                # (try_end),   

                # (ge, "$vats_agent", 0),  #only if agent found
                # (assign,"$vats_selected","$vats_agent"),
                # (assign, "$vats", 1),  #modus change 
                # (mission_set_time_speed, 1),    #t: slow down, d: moves it to 10% speed, it's still mad slow #t: test to 1
                    
                # (agent_set_no_dynamics,"$g_player",1),  #t: let the player not move    
                # (agent_set_animation, "$g_player", "anim_release_musket", 1),

                # (mission_cam_set_mode, 1),      

                # (start_presentation,"prsnt_vats"),
            # (else_try), #no ats points
                # (lt, "$vats_ap", 25), #t: a minimum - so no spamming without enough points
                
                # (display_message, "@Too few A.T.S points for this action!", 0xFF0000),
                # (assign,"$vats_restart",0),

            # (else_try), #no horse            
                # (ge, ":player_horse", 0),  
                # (display_message, "@A.T.S not available on horse!", 0xFF0000),      
                # (assign,"$vats_restart",0),
                
            # (else_try), #no ranged            
                # (neg|is_between, ":wielded_item", ranged_weapons_begin, ranged_weapons_end),                
                # (display_message, "@A.T.S is not compatible with your weapon!", 0xFF0000), 
                # (assign,"$vats_restart",0),
                
            # (else_try), #no ammo            
                # (le, ":ammo", 0),
                # (display_message, "@A.T.S could not register any ammo!", 0xFF0000),    
                # (assign,"$vats_restart",0),            
            # (else_try), #no enemies            
                # (display_message, "@A.T.S can't find a target!", 0xFF0000), 
                # (assign,"$vats_restart",0),
                
            # (try_end),    
    # ]),
    # #VATS 1 -> cam set to the target
    # # (0.5,0,0,[
    # (0.0,0,0,[
            # (eq,"$vats",1),
        # ],
        # [
            # (set_fixed_point_multiplier, 100),
        
            # (agent_get_position, pos89, "$vats_selected"),    
            # (position_move_y, pos89, 250),
            # (position_move_z, pos89, 180),
            # (position_rotate_z, pos89, 180),
            # (mission_cam_set_position, pos89),
            
            # (try_begin),
                # (ge,"$vats_bone",0),
                # (agent_get_bone_position, pos90, "$vats_selected", "$vats_bone", 1),        
          
                # (particle_system_burst, "psys_laser", pos90, 1),
            # (try_end),
    # ]),   
    # (0,1.2,0,[
            # (eq,"$vats",2),
                    # (get_player_agent_no,"$g_player"),

            # (agent_set_animation, "$g_player", "anim_release_musket", 1),
            # (agent_set_attack_action, "$g_player", -1, 0), #cancel
            # (agent_set_defend_action, "$g_player", 0, 1), #cancel             
    # ],
    # [
            # (assign,"$vats",0),
            # (assign,"$vats_restart",1),
      
    # ]), 
    # #this two are just a test
    # # (0,0,0,[
            # # (this_or_next|eq,"$vats",1),
            # # (this_or_next|eq,"$vats",3),
            # # # (this_or_next|eq,"$vats",4),
            # # # (this_or_next|game_key_is_down, gk_attack),        
            # # (eq,"$vats",2),
            
    # # ],
    # # [
            # # (get_player_agent_no,"$g_player"),
            # # # (agent_set_animation, "$g_player", "anim_release_musket", 1),
            # # (agent_set_attack_action, "$g_player", -1, 0), #cancel
            # # (agent_set_defend_action, "$g_player", 0, 1), #cancel      
    # # ]), 
    # # (0.0,0,0,[
            # # (eq,"$vats",4),
    # # ],
    # # [
            # # (get_player_agent_no,"$g_player"),

            # # # (mission_cam_set_mode, 0),
            # # (mission_cam_set_mode, 0, 500, 0),
            # # (mission_set_time_speed, 100),
            
            # # (agent_set_no_dynamics,"$g_player",0),    
            # # (agent_set_attack_action, "$g_player", -1, 0), #cancel
            # # (agent_set_defend_action, "$g_player", 0, 1), #cancel             
            # # (assign,"$vats",0),   
     
    # # ]),    

# ]   

#######################################################################################################################################
  
