import string
from module_info import *

dword      = 0x8000000000000000
dword_mask = 0xffffffffffffffff

density_bits      = 32
fkf_density_mask  = 0xFFFF #16K

#terain condition flags
fkf_plain             = 0x00000004
fkf_steppe            = 0x00000008
fkf_snow              = 0x00000010
fkf_desert            = 0x00000020
fkf_plain_forest      = 0x00000400
fkf_steppe_forest     = 0x00000800
fkf_snow_forest       = 0x00001000
fkf_desert_forest     = 0x00002000
fkf_terrain_mask      = 0x0000ffff

fkf_realtime_ligting  = 0x00010000 #deprecated
fkf_point_up          = 0x00020000 #uses auto-generated point-up(quad) geometry for the flora kind
fkf_align_with_ground = 0x00040000 #align the flora object with the ground normal
fkf_grass             = 0x00080000 #is grass
fkf_on_green_ground   = 0x00100000 #populate this flora on green ground
fkf_rock              = 0x00200000 #is rock 
fkf_tree              = 0x00400000 #is tree -> note that if you set this parameter, you should pass additional alternative tree definitions
fkf_snowy             = 0x00800000
fkf_guarantee         = 0x01000000

fkf_speedtree         = 0x02000000  #NOT FUNCTIONAL: we have removed speedtree support on M&B Warband

fkf_has_colony_props  = 0x04000000  # if fkf_has_colony_props -> then you can define colony_radius and colony_treshold of the flora kind


def density(g):
  if (g > fkf_density_mask):
    g = fkf_density_mask
  return ((dword | g) << density_bits)


fauna_kinds = [
##NEW
("new_grass",
  density(1000)|fkf_plain|fkf_plain_forest|fkf_steppe_forest|fkf_point_up|fkf_align_with_ground|fkf_grass|fkf_on_green_ground|fkf_guarantee,
  [["grass1","0"],["grass2","0"],["grass3","0"],["grass4","0"],["grass5","0"]]),
("new_grass2",
  density(750)|fkf_steppe|fkf_point_up|fkf_align_with_ground|fkf_grass|fkf_on_green_ground|fkf_guarantee,
  [["grass1","0"],["grass2","0"],["grass3","0"],["grass4","0"],["grass5","0"]]),
("new_grass3",
  density(250)|fkf_snow|fkf_snow_forest|fkf_point_up|fkf_align_with_ground|fkf_grass|fkf_guarantee,
  [["grass1","0"],["grass2","0"],["grass3","0"],["grass4","0"],["grass5","0"]]),
("new_grass4",
  density(500)|fkf_desert|fkf_desert_forest|fkf_guarantee,
  [["common_plant","0"]]),
 
("new_plant",
  density(25)|fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest,
  [["plant1","0"]]),
("new_plant2",
  density(25)|fkf_steppe|fkf_steppe_forest|fkf_plain|fkf_plain_forest|fkf_desert|fkf_desert_forest,
  [["new_bush_1","0"]]),  
("new_plant3",
  density(25)|fkf_desert|fkf_desert_forest,
  [["cactus_small_1","0"],["cactus_small_2","0"]]),
("new_plant4",
  density(25)|fkf_steppe|fkf_desert|fkf_desert_forest,
  [["bush_agave_a","0"]]),  
  
("new_tree",
  density(6)|fkf_plain|fkf_steppe|fkf_steppe_forest|fkf_desert|fkf_desert_forest|fkf_tree,
  [("new_tree_e_1", "bo_new_tree_e_1",("0","0")),("new_tree_e_2", "bo_new_tree_e_2",("0","0")),("new_tree_e_3", "bo_new_tree_e_3",("0","0"))]),
("new_tree2",
  density(6)|fkf_desert|fkf_desert_forest|fkf_tree,
  [("new_tree_a", "bo_new_tree_a",("0","0")),("new_tree_a_double", "bo_new_tree_a_double",("0","0"))]),
("new_tree3",
  density(6)|fkf_plain|fkf_plain_forest|fkf_tree,
  [("beech_b","bo_beech_b",("0","0")),("beech_c","bo_beech_b",("0","0")),("beech_dd","bo_beech_b",("0","0"))]),
("new_tree4",
  density(6)|fkf_plain|fkf_steppe_forest|fkf_tree,
  [("beech", "bo_beech",("0","0"))]),
("new_tree5",
  density(6)|fkf_plain|fkf_plain_forest|fkf_tree,
  [("pl_fur_tall1", "bo_pl_fur_tall1",("0","0")),("pl_fur_tall2", "bo_pl_fur_tall2",("0","0")),("pl_fur_tall3", "bo_pl_fur_tall3",("0","0"))]),
("new_tree6",
  density(6)|fkf_plain|fkf_plain_forest|fkf_steppe_forest|fkf_tree,
  [("new_tree_f_1", "bo_new_tree_c_1",("0","0")),("new_tree_f_2", "bo_new_tree_c_2",("0","0")),("new_tree_f_3", "bo_new_tree_c_3",("0","0"))]),
("new_tree7",
  density(6)|fkf_plain|fkf_plain_forest|fkf_steppe_forest|fkf_tree,
  [("new_tree_c_1", "bo_new_tree_c_1",("0","0")),("new_tree_c_2", "bo_new_tree_c_2",("0","0")),("new_tree_c_3", "bo_new_tree_c_3",("0","0"))]),
("new_tree8",
  density(6)|fkf_plain|fkf_steppe|fkf_steppe_forest|fkf_tree,
  [("new_tree_2","bo_new_tree_2",("0","0"))]),
("new_tree9",
  density(6)|fkf_plain|fkf_steppe|fkf_steppe_forest|fkf_tree,
  [("new_tree","bo_new_tree",("0","0"))]),

("cactus",
  density(4)|fkf_desert|fkf_desert_forest|fkf_tree,
  [("cactus_a", "bo_cactus_a",("0","0")),("cactus_b", "bo_cactus_b",("0","0")),("cactus_c", "bo_cactus_c",("0","0")),("cactus_d", "bo_cactus_d",("0","0")),("cactus_e", "bo_cactus_e",("0","0"))]),

## NEW END
  
  ("common_plant",fkf_steppe|fkf_steppe_forest|fkf_desert|fkf_desert_forest|density(250),
    [["common_plant","0"]]),
  ("big_bush",fkf_steppe|fkf_steppe_forest|fkf_plain|fkf_plain_forest|fkf_desert|fkf_desert_forest|density(25),
    [["big_bush","0"]]),

  ("grass_purple",0,[["common_plant","0"]]),
  ("buddy_plant",0,[["plant1","0"]]),
  ("spiky_plant",0,[["plant1","0"]]),
  ("seedy_plant",0,[["plant1","0"]]),
  ("blue_flower",0,[["common_plant","0"]]),
  ("bushes02_a",0,[["plant1","0"]]),
  ("bushes03_a",0,[["plant1","0"]]),  
  ("bushes04_a",0,[["plant1","0"]]),  
  ("bushes05_a",0,[["plant1","0"]]),  
  ("bushes06_a",0,[["plant1","0"]]),  
  ("bushes07_a",0,[["plant1","0"]]),  
  ("bushes08_a",0,[["plant1","0"]]),  
  ("bushes09_a",0,[["plant1","0"]]),  
  ("bushes10_a",0,[["plant1","0"]]),  
  ("bushes11_a",0,[["plant1","0"]]),  
  ("bushes12_a",0,[["plant1","0"]]), 
  ("bush_new_1",0,[["plant1","0"]]), 
  ("bush_new_2",0,[["plant1","0"]]), 
  ("bush_new_3",0,[["plant1","0"]]), 
  ("bush_new_4",0,[["plant1","0"]]), 
  ("dry_bush",0,[["plant1","0"]]), 
  ("dry_leaves",0,[["plant1","0"]]), 
  ("yellow_flower",0,[["plant1","0"]]), 
  ("grass_bush_h",0,[["common_plant","0"]]), 
  ("grass_bush_l",0,[["common_plant","0"]]),
  ("small_plant",0,[["plant1","0"]]),
  ("fern",0,[["plant1","0"]]),
  ("grass_bush",0,[["common_plant","0"]]),
  ("grass_saz",0,[["common_plant","0"]]),
  ("grass_bush_g",0,[["common_plant","0"]]),
  ("grass_bush_i",0,[["common_plant","0"]]),
  ("grass_bush_j",0,[["common_plant","0"]]),
  ("grass_bush_k",0,[["common_plant","0"]]),
  ("thorn_a",0,[["plant1","0"]]),
  ("basak",0,[["plant1","0"]]),
    
  ("grass",0,[["dummy_mesh","0"]]),
  ("grass_steppe",0,[["dummy_mesh","0"]]),

  ("aspen",fkf_tree,[("new_tree_e_1", "bo_new_tree_e_1",("0","0"))]),
  ("pine_1",fkf_tree,[("new_tree_e_2", "bo_new_tree_e_2",("0","0"))]),
  ("pine_2",fkf_tree,[("new_tree_e_3", "bo_new_tree_e_3",("0","0"))]),
  ("pine_3",fkf_tree,[("new_tree_e_1", "bo_new_tree_e_1",("0","0"))]),
  ("pine_4",fkf_tree,[("new_tree_e_2", "bo_new_tree_e_2",("0","0"))]),
  ("snowy_pine",fkf_tree,[("new_tree_e_3", "bo_new_tree_e_3",("0","0"))]),
  ("snowy_pine_2",fkf_tree,[("new_tree_e_1", "bo_new_tree_e_1",("0","0"))]),
  ("tree_1",fkf_tree,[("new_tree_e_2", "bo_new_tree_e_2",("0","0"))]),
  ("tree_3",fkf_tree,[("new_tree_e_3", "bo_new_tree_e_3",("0","0"))]),
  ("tree_4",fkf_tree,[("new_tree_e_1", "bo_new_tree_e_1",("0","0"))]),
  ("tree_5",fkf_tree,[("new_tree_e_2", "bo_new_tree_e_2",("0","0"))]),
  ("tree_6",fkf_tree,[("new_tree_e_3", "bo_new_tree_e_3",("0","0"))]),
  ("tree_7",fkf_tree,[("new_tree_e_1", "bo_new_tree_e_1",("0","0"))]),
  ("tree_8",fkf_tree,[("new_tree_e_2", "bo_new_tree_e_2",("0","0"))]),
  ("tree_9",fkf_tree,[("new_tree_e_3", "bo_new_tree_e_3",("0","0"))]),
  ("tree_10",fkf_tree,[("new_tree_e_1", "bo_new_tree_e_1",("0","0"))]),
  ("tree_11",fkf_tree,[("new_tree_e_2", "bo_new_tree_e_2",("0","0"))]),
  ("tree_12",fkf_tree,[("new_tree_e_3", "bo_new_tree_e_3",("0","0"))]),
  ("tree_13",fkf_tree,[("new_tree_e_1", "bo_new_tree_e_1",("0","0"))]),
  ("tree_14",fkf_tree,[("new_tree_e_2", "bo_new_tree_e_2",("0","0"))]),
  ("tree_15",fkf_tree,[("new_tree_e_3", "bo_new_tree_e_3",("0","0"))]),
  ("tree_16",fkf_tree,[("new_tree_e_1", "bo_new_tree_e_1",("0","0"))]),
  ("tree_17",fkf_tree,[("new_tree_e_2", "bo_new_tree_e_2",("0","0"))]),

  ("palm",
    fkf_tree,
    [("new_tree_a", "bo_new_tree_a",("0","0")),("new_tree_a_double", "bo_new_tree_a_double",("0","0"))]),
  ("tree_new_1",fkf_tree,[("new_tree_e_3", "bo_new_tree_e_3",("0","0"))]),
  ("tree_new_2",fkf_tree,[("new_tree_e_1", "bo_new_tree_e_1",("0","0"))]),
  ("tree_new_3",fkf_tree,[("new_tree_e_2", "bo_new_tree_e_2",("0","0"))]),
  ("tree_plane",fkf_tree,[("new_tree_e_3", "bo_new_tree_e_3",("0","0"))]),
  ("tree_19",fkf_tree,[("new_tree_e_1", "bo_new_tree_e_1",("0","0"))]),
  ("beech",fkf_tree,[("new_tree_e_2", "bo_new_tree_e_2",("0","0"))]),
  ("tall_tree",fkf_tree,[("new_tree_e_3", "bo_new_tree_e_3",("0","0"))]),
  ("tree_e",fkf_tree,[("new_tree_e_1", "bo_new_tree_e_1",("0","0"))]),
  ("tree_f",fkf_tree,[("new_tree_e_2", "bo_new_tree_e_2",("0","0"))]),

  ("small_rock",fkf_realtime_ligting|fkf_rock,[["rock_c","bo_rock_c"],["rock_d","bo_rock_d"],["rock_e","bo_rock_e"],["rock_f","bo_rock_f"],["rock_g","bo_rock_g"],["rock_h","bo_rock_h"],["rock_i","bo_rock_i"],["rock_k","bo_rock_k"]]),
  ("rock_snowy",fkf_realtime_ligting|fkf_rock,[["rock_c","bo_rock_c"],["rock_d","bo_rock_d"],["rock_e","bo_rock_e"],["rock_f","bo_rock_f"],["rock_g","bo_rock_g"],["rock_h","bo_rock_h"],["rock_i","bo_rock_i"],["rock_k","bo_rock_k"]]),
  
  ("rock",fkf_align_with_ground|fkf_realtime_ligting|fkf_rock,[["rock1","bo_rock1"],["rock2","bo_rock2"],["rock3","bo_rock3"],["rock4","bo_rock4"],["rock5","bo_rock6"],["rock7","bo_rock7"]]),
  ("rock_snowy2",fkf_align_with_ground|fkf_realtime_ligting|fkf_rock,[["rock1","bo_rock1"],["rock2","bo_rock2"],["rock3","bo_rock3"],["rock4","bo_rock4"],["rock5","bo_rock6"],["rock7","bo_rock7"]]),

  ("grape_vineyard",0,[("homeplant","0")]),
  ("grape_vineyard_stake",0,[("dummy_mesh","0")]),  
  
  ("wheat",0,[["wheat_a","0"],["wheat_b","0"],["wheat_c","0"],["wheat_d","0"]]),
  
  ("valleyRock_rounded",fkf_rock|density(5),[["valleyRock_rounded_1","bo_valleyRock_rounded_1"],["valleyRock_rounded_2","bo_valleyRock_rounded_2"],["valleyRock_rounded_3","bo_valleyRock_rounded_3"],["valleyRock_rounded_4","bo_valleyRock_rounded_4"]]),
  ("valleyRock_flat",fkf_rock|density(5),[["valleyRock_flat_1","bo_valleyRock_flat_1"],["valleyRock_flat_2","bo_valleyRock_flat_2"],["valleyRock_flat_3","bo_valleyRock_flat_3"],["valleyRock_flat_4","bo_valleyRock_flat_4"],["valleyRock_flat_5","bo_valleyRock_flat_5"],["valleyRock_flat_6","bo_valleyRock_flat_6"]]),
  ("valleyRock_flatRounded_small",fkf_rock|density(5),[["valleyRock_flatRounded_small_1","bo_valleyRock_flatRounded_small_1"],["valleyRock_flatRounded_small_2","bo_valleyRock_flatRounded_small_2"],["valleyRock_flatRounded_small_3","bo_valleyRock_flatRounded_small_3"]]),
  ("valleyRock_flatRounded_big",fkf_rock|density(5),[["valleyRock_flatRounded_big_1","bo_valleyRock_flatRounded_big_1"],["valleyRock_flatRounded_big_2","bo_valleyRock_flatRounded_big_2"]]),

  ]
def save_fauna_kinds():
  file = open(export_dir_sky + "flora_kinds.txt","w")
  file.write("%d\n"%len(fauna_kinds))
  for fauna_kind in fauna_kinds:
    meshes_list = fauna_kind[2]
    file.write("%s %d %d\n"%(fauna_kind[0], (dword_mask & fauna_kind[1]), len(meshes_list)))
    for m in meshes_list:
      file.write(" %s "%(m[0]))
      if (len(m) > 1):
        file.write(" %s\n"%(m[1]))
      else:
        file.write(" 0\n")
      if ( fauna_kind[1] & (fkf_tree|fkf_speedtree) ):  #if this fails make sure that you have entered the alternative tree definition (NOT FUNCTIONAL in Warband)
        speedtree_alternative = m[2]
        file.write(" %s %s\n"%(speedtree_alternative[0], speedtree_alternative[1]))
    if ( fauna_kind[1] & fkf_has_colony_props ):
      file.write(" %s %s\n"%(fauna_kind[3], fauna_kind[4]))
  file.close()

def two_to_pow(x):
  result = 1
  for i in xrange(x):
    result = result * 2
  return result

fauna_mask = 0x80000000000000000000000000000000
low_fauna_mask =             0x8000000000000000
def save_python_header():
  file = open("./fauna_codes.py","w")
  for i_fauna_kind in xrange(len(fauna_kinds)):
    file.write("%s_1 = 0x"%(fauna_kinds[i_fauna_kind][0]))
    file.write("%x\n"%(fauna_mask | two_to_pow(i_fauna_kind)))
    file.write("%s_2 = 0x"%(fauna_kinds[i_fauna_kind][0]))
    file.write("%x\n"%(fauna_mask | ((low_fauna_mask|two_to_pow(i_fauna_kind)) << 64)))
    file.write("%s_3 = 0x"%(fauna_kinds[i_fauna_kind][0]))
    file.write("%x\n"%(fauna_mask | ((low_fauna_mask|two_to_pow(i_fauna_kind)) << 64) | two_to_pow(i_fauna_kind)))
  file.close()

print "Exporting flora data..."
save_fauna_kinds()
print "Finished."