from header_troops import *
from header_skills import *
from names import *
import random
import math
# Python functions used to pop out random troops!

# Globals
s_st = 4
s_ag = 4
s_in = 4
s_ch = 4

def clamp(mn, mx, val):
	val = max(mn, min(val, mx))
	return val

def username(s):

	random.seed(s)
	
	first = random.choice(first_names)
	second = random.choice(secondary_names)
	
	user = first + " " + second
	
	return user

def username_w(s):

	random.seed(s)
	
	first = random.choice(first_names_w)
	second = random.choice(secondary_names)
	
	user = first + " " + second
	
	return user
    
# def username(s):

	# random.seed(s)
	# scrambler = random.randrange(101)
	
	# first = random.choice(first_names)
	# second = random.choice(secondary_names)
	# # numbers = str(random.randrange(0, 999)).zfill(3)

    # user = first + second
	
	# if random.randrange(5) != 1:
		# numbers = ""
		
	# if random.randrange(25) == 1:
		# original = first
		# first = second
		# second = original
		
	# if random.randrange(50) == 1:
		# second = first
		
	# if random.randrange(75) == 1:
		# first = second
	
	# if (scrambler % 2) == 0:
		# first = first.capitalize()
		# second = second.capitalize()
	# elif (scrambler % 3) == 0:
		# first = first.lower()
		# second = "\x7e" + second.lower()
	# elif (scrambler % 5) == 0:
		# first = first.upper()
		# second = "\x7e" + second.upper()
	
	# if(scrambler % 7) == 0:
		# first = "xxX" + first.lower() + "\x7e"
		# second = second.lower() + "Xxx"
		# numbers = ""
	
	# if s < len(premade_names):
		# user = premade_names[s]
	# else:
        # user = first + second
		# user = first + second + numbers
	
	# return user
	
# def monster_type(s):

	# random.seed(s)
	
	# first = random.choice(first_names)
	# second = random.choice(monster_names)
	
	# user = first + " " + second
	
	# return user
	
def random_wp(a, max = 250):

	random.seed(a)
		
	o = random.randrange(max)
	t = random.randrange(max)
	p = random.randrange(max)
	a = random.randrange(max)
	cr = random.randrange(max)
	th = random.randrange(max)
	f = random.randrange(max)
	
	c = wpex(o, t, p, a, cr, th, f)

	return c
	
def random_attrib(seed, max_lvl = 50, max_attr = 15):
	random.seed(seed)
	
	lvl = random.randint(0, max_lvl)
	
	points = int(math.ceil(lvl / 5) + 4)
	
	a = random.randint(0, min(points, max_attr))
	points -= a
	global s_st
	s_st = a + 1
	
	b = random.randint(0, points)
	points -= b
	global s_ag
	s_ag = b + 1
	
	c = random.randint(0, points)
	points -= c
	global s_in
	s_in = c + 1
	
	d = points
	global s_ch
	s_ch = d + 1
	
	a = str_list[a + 1]
	b = agi_list[b + 1]
	c = int_list[c + 1]
	d = cha_list[d + 1]
	
	return a | b | c | d | level(lvl)
	
def random_skills(seed):
	random.seed(seed)
	
	global s_ch
	s_ch = int(min(math.ceil(s_ch / 3), 10))
	
	global s_st
	s_st = int(min(math.ceil(s_st / 3), 10))
	
	global s_ag
	s_ag = int(min(math.ceil(s_ag / 3), 10))
	
	global s_in
	s_in = int(min(math.ceil(s_in / 3), 10))
	
	a = trade_list[random.randint(0, s_ch)]
	b = leadership_list[random.randint(0, s_ch)]
	c = prisoner_management_list[random.randint(0, s_ch)]
	d = persuasion_list[random.randint(0, s_ch)]
	e = engineer_list[random.randint(0, s_in)]
	f = first_aid_list[random.randint(0, s_in)]
	e = surgery_list[random.randint(0, s_in)]
	g = wound_treatment_list[random.randint(0, s_in)]
	h = inventory_management_list[random.randint(0, s_in)]
	i = spotting_list[random.randint(0, s_in)]
	j = pathfinding_list[random.randint(0, s_in)]
	k = tactics_list[random.randint(0, s_in)]
	l = tracking_list[random.randint(0, s_in)]
	m = trainer_list[random.randint(0, s_in)]
	n = looting_list[random.randint(0, s_ag)]
	o = horse_archery_list[random.randint(0, s_ag)]
	p = riding_list[random.randint(0, s_ag)]
	q = athletics_list[random.randint(0, s_ag)]
	r = shield_list[random.randint(0, s_ag)]
	s = weapon_master_list[random.randint(0, s_ag)]
	t = power_draw_list[random.randint(0, s_st)]
	u = power_throw_list[random.randint(0, s_st)]
	v = power_strike_list[random.randint(0, s_st)]
	w = ironflesh_list[random.randint(0, s_st)]
	
	return a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w

def random_troop(seed):
	x = ["npc_%03d" % seed, username(seed), username(seed), tf_hero|tf_randomize_face, 0, 0, 0, [], random_attrib(seed), random_wp(seed), random_skills(seed), mercenary_face_1, mercenary_face_2]
	# x = ["npc_%03d" % seed, username(seed), username(seed), tf_hero|tf_randomize_face, 0, 0, 0, [], random_attrib(seed), random_wp(seed), random_skills(seed), 0]
	return x

def random_troop_w(seed):
	x = ["npc_w_%03d" % seed, username_w(seed), username_w(seed), tf_hero|tf_woman|tf_randomize_face, 0, 0, 0, [], random_attrib(seed), random_wp(seed), random_skills(seed), woman_face_1, woman_face_2]
	# x = ["npc_%03d" % seed, username(seed), username(seed), tf_hero|tf_randomize_face, 0, 0, 0, [], random_attrib(seed), random_wp(seed), random_skills(seed), 0]
	return x
	
# def random_monster(seed):
	# x = ["monster_%03d" % seed, monster_type(seed), monster_type(seed), tf_randomize_face, 0, 0, 0, [], random_attrib(seed, 15), random_wp(seed, 50), random_skills(seed), 0]
	# return x


# lists for functions
str_list = [str_3, str_4, str_5, str_6, str_7, str_8, str_9, str_10, str_11, str_12, str_13, str_14, str_15, str_16, str_17, str_18, str_19, str_20, str_21, str_22, str_23, str_24, str_25, str_26, str_27, str_28, str_29, str_30]
agi_list = [agi_3, agi_4, agi_5, agi_6, agi_7, agi_8, agi_9, agi_10, agi_11, agi_12, agi_13, agi_14, agi_15, agi_16, agi_17, agi_18, agi_19, agi_20, agi_21, agi_22, agi_23, agi_24, agi_25, agi_26, agi_27, agi_28, agi_29, agi_30]
int_list = [int_3, int_4, int_5, int_6, int_7, int_8, int_9, int_10, int_11, int_12, int_13, int_14, int_15, int_16, int_17, int_18, int_19, int_20, int_21, int_22, int_23, int_24, int_25, int_26, int_27, int_28, int_29, int_30]
cha_list = [cha_3, cha_4, cha_5, cha_6, cha_7, cha_8, cha_9, cha_10, cha_11, cha_12, cha_13, cha_14, cha_15, cha_16, cha_17, cha_18, cha_19, cha_20, cha_21, cha_22, cha_23, cha_24, cha_25, cha_26, cha_27, cha_28, cha_29, cha_30]
first_aid_list = [knows_first_aid_1, knows_first_aid_2, knows_first_aid_3, knows_first_aid_4, knows_first_aid_5, knows_first_aid_6, knows_first_aid_7, knows_first_aid_8, knows_first_aid_9, knows_first_aid_10]
trade_list = [knows_trade_1, knows_trade_2, knows_trade_3, knows_trade_4, knows_trade_5, knows_trade_6, knows_trade_7, knows_trade_8, knows_trade_9, knows_trade_10]
leadership_list = [knows_leadership_1, knows_leadership_2, knows_leadership_3, knows_leadership_4, knows_leadership_5, knows_leadership_6, knows_leadership_7, knows_leadership_8, knows_leadership_9, knows_leadership_10]
prisoner_management_list = [knows_prisoner_management_1, knows_prisoner_management_2, knows_prisoner_management_3, knows_prisoner_management_4, knows_prisoner_management_5, knows_prisoner_management_6, knows_prisoner_management_7, knows_prisoner_management_8, knows_prisoner_management_9, knows_prisoner_management_10]
persuasion_list = [knows_persuasion_1, knows_persuasion_2, knows_persuasion_3, knows_persuasion_4, knows_persuasion_5, knows_persuasion_6, knows_persuasion_7, knows_persuasion_8, knows_persuasion_9, knows_persuasion_10]
engineer_list = [knows_engineer_1, knows_engineer_2, knows_engineer_3, knows_engineer_4, knows_engineer_5, knows_engineer_6, knows_engineer_7, knows_engineer_8, knows_engineer_9, knows_engineer_10]
wound_treatment_list = [knows_wound_treatment_1, knows_wound_treatment_2, knows_wound_treatment_3, knows_wound_treatment_4, knows_wound_treatment_5, knows_wound_treatment_6, knows_wound_treatment_7, knows_wound_treatment_8, knows_wound_treatment_9, knows_wound_treatment_10]
inventory_management_list = [knows_inventory_management_1, knows_inventory_management_2, knows_inventory_management_3, knows_inventory_management_4, knows_inventory_management_5, knows_inventory_management_6, knows_inventory_management_7, knows_inventory_management_8, knows_inventory_management_9, knows_inventory_management_10]
spotting_list = [knows_spotting_1, knows_spotting_2, knows_spotting_3, knows_spotting_4, knows_spotting_5, knows_spotting_6, knows_spotting_7, knows_spotting_8, knows_spotting_9, knows_spotting_10]
pathfinding_list = [knows_pathfinding_1, knows_pathfinding_2, knows_pathfinding_3, knows_pathfinding_4, knows_pathfinding_5, knows_pathfinding_6, knows_pathfinding_7, knows_pathfinding_8, knows_pathfinding_9, knows_pathfinding_10]
tactics_list = [knows_tactics_1, knows_tactics_2, knows_tactics_3, knows_tactics_4, knows_tactics_5, knows_tactics_6, knows_tactics_7, knows_tactics_8, knows_tactics_9, knows_tactics_10]
tracking_list = [knows_tracking_1, knows_tracking_2, knows_tracking_3, knows_tracking_4, knows_tracking_5, knows_tracking_6, knows_tracking_7, knows_tracking_8, knows_tracking_9, knows_tracking_10]
trainer_list = [knows_trainer_1, knows_trainer_2, knows_trainer_3, knows_trainer_4, knows_trainer_5, knows_trainer_6, knows_trainer_7, knows_trainer_8, knows_trainer_9, knows_trainer_10]
looting_list = [knows_looting_1, knows_looting_2, knows_looting_3, knows_looting_4, knows_looting_5, knows_looting_6, knows_looting_7, knows_looting_8, knows_looting_9, knows_looting_10]
horse_archery_list = [knows_horse_archery_1, knows_horse_archery_2, knows_horse_archery_3, knows_horse_archery_4, knows_horse_archery_5, knows_horse_archery_6, knows_horse_archery_7, knows_horse_archery_8, knows_horse_archery_9, knows_horse_archery_10]
riding_list = [knows_riding_1, knows_riding_2, knows_riding_3, knows_riding_4, knows_riding_5, knows_riding_6, knows_riding_7, knows_riding_8, knows_riding_9, knows_riding_10]
athletics_list = [knows_athletics_1, knows_athletics_2, knows_athletics_3, knows_athletics_4, knows_athletics_5, knows_athletics_6, knows_athletics_7, knows_athletics_8, knows_athletics_9, knows_athletics_10]
surgery_list = [knows_surgery_1, knows_surgery_2, knows_surgery_3, knows_surgery_4, knows_surgery_5, knows_surgery_6, knows_surgery_7, knows_surgery_8, knows_surgery_9, knows_surgery_10]
shield_list = [knows_shield_1, knows_shield_2, knows_shield_3, knows_shield_4, knows_shield_5, knows_shield_6, knows_shield_7, knows_shield_8, knows_shield_9, knows_shield_10]
weapon_master_list = [knows_weapon_master_1, knows_weapon_master_2, knows_weapon_master_3, knows_weapon_master_4, knows_weapon_master_5, knows_weapon_master_6, knows_weapon_master_7, knows_weapon_master_8, knows_weapon_master_9, knows_weapon_master_10]
power_draw_list = [knows_power_draw_1, knows_power_draw_2, knows_power_draw_3, knows_power_draw_4, knows_power_draw_5, knows_power_draw_6, knows_power_draw_7, knows_power_draw_8, knows_power_draw_9, knows_power_draw_10]
power_throw_list = [knows_power_throw_1, knows_power_throw_2, knows_power_throw_3, knows_power_throw_4, knows_power_throw_5, knows_power_throw_6, knows_power_throw_7, knows_power_throw_8, knows_power_throw_9, knows_power_throw_10]
power_strike_list = [knows_power_strike_1, knows_power_strike_2, knows_power_strike_3, knows_power_strike_4, knows_power_strike_5, knows_power_strike_6, knows_power_strike_7, knows_power_strike_8, knows_power_strike_9, knows_power_strike_10]
ironflesh_list = [knows_ironflesh_1, knows_ironflesh_2, knows_ironflesh_3, knows_ironflesh_4, knows_ironflesh_5, knows_ironflesh_6, knows_ironflesh_7, knows_ironflesh_8, knows_ironflesh_9, knows_ironflesh_10]