from header_skins import *
from ID_particle_systems import *

from compiler import *
####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################

man_face_keys = [
    (240, 0, -0.4, 0.3, "Chin Size"),
    (230, 0, -0.4, 0.8, "Chin Shape"),
    (250, 0, -0.25, 0.55, "Chin Forward"),
    (130, 0, -0.5, 1, "Jaw Width"),
    (120, 0, -0.5, 0.6, "Lower Lip"),
    (110, 0, -0.2, 0.6, "Upper Lip"),
    (100, 0, 0.2, -0.2, "Mouth-Nose Distance"),
    (90, 0, 0.55, -0.55, "Mouth Width"),
    (30, 0, -0.3, 0.3, "Nostril Size"),
    (60, 0, 0.25, -0.25, "Nose Height"),
    (40, 0, -0.2, 0.3, "Nose Width"),
    (70, 0, -0.3, 0.4, "Nose Size"),
    (50, 0, 0.2, -0.3, "Nose Shape"),
    (80, 0, -0.3, 0.65, "Nose Bridge"),
    (160, 0, -0.2, 0.25, "Eye Width"),
    (190, 0, -0.25, 0.15, "Eye to Eye Dist"),
    (170, 0, -0.85, 0.85, "Eye Shape"),
    (200, 0, -0.3, 0.7, "Eye Depth"),
    (180, 0, -1.5, 1.5, "Eyelids"),
    (20, 0, 0.6, -0.25, "Cheeks"),
    (260, 0, -0.6, 0.5, "Cheek Bones"),
    (220, 0, 0.8, -0.8, "Eyebrow Height"),
    (210, 0, -0.75, 0.75, "Eyebrow Shape"),
    (10, 0, -0.6, 0.5, "Temple Width"),
    (270, 0, -0.3, 1, "Face Depth"),
    (150, 0, -0.25, 0.45, "Face Ratio"),
    (140, 0, -0.4, 0.5, "Face Width"),
    (280, 0, 1, 1, "Post-Edit"),

    # (20,0, 0.7,-0.6, "Chin Size"),
    # (260,0, -0.6,1.4, "Chin Shape"),
    # (10,0,-0.5,0.9, "Chin Forward"),
    # (240,0,0.9,-0.8, "Jaw Width"),
    # (210,0,-0.5,1.0, "Jaw Position"),
    # (250,0,0.8,-1.0, "Mouth-Nose Distance"),
    # (200,0,-0.3,1.0, "Mouth Width"),
    # (50,0,-1.5,1.0, "Cheeks"),

    # (60,0,-0.4,1.35, "Nose Height"),
    # (70,0,-0.6,0.7, "Nose Width"),
    # (80,0,1.0,-0.1, "Nose Size"),
    # (270,0,-0.5,1.0, "Nose Shape"),
    # (90,0,-0.2,1.4, "Nose Bridge"),

    # (100,0,-0.3,1.5, "Cheek Bones"),
    # (150,0,-0.2,3.0, "Eye Width"),
    # (110,0,1.5,-0.9, "Eye to Eye Dist"),
    # (120,0,1.9,-1.0, "Eye Shape"),
    # (130,0,-0.5, 1.1, "Eye Depth"),
    # (140,0,1.0,-1.2, "Eyelids"),

    # (160,0,1.3,-0.2, "Eyebrow Position"),
    # (170,0,-0.1,1.9, "Eyebrow Height"),
    # (220,0,-0.1,0.9, "Eyebrow Depth"),
    # (180,0,-1.1,1.6, "Eyebrow Shape"),
    # (230,0,1.2,-0.7, "Temple Width"),

    # (30,0,-0.6,0.9, "Face Depth"),
    # (40,0,0.9,-0.6, "Face Ratio"),
    # (190,0,0.0,0.95, "Face Width"),

    # (280,0,0.0,1.0, "Post-Edit"),
    ]
woman_face_keys = [
(230,0,1.5,-1.8, "Chin Size"), 
(220,0,-1.7,1.5, "Chin Shape"), 
(10,0,-1.7,2.0, "Chin Forward"),
(20,0,-1.7,2.0, "Jaw Width"), 
(40,0,-1.0,1.5, "Jaw Position"),
(90,0,-1.7,1.7, "Jaw Neck"),
(50,0,-2.0,1.7, "Cheeks"),
(100,0,-1.7,1.7, "Cheek Bones"),
(270,0,1.5,-1.3, "Mouth-Nose Distance"),
(30,0,-1.7,1.5, "Mouth Width"),
(160,0,1.7,-2.0, "Lips Position"),

(60,0,1.5,-1.5, "Nose Height"),
(70,0,-1.5,1.7, "Nose Width"),
(80,0,1.0,-1.0, "Nose Size"),
(240,0,1.4,-1.4, "Nose Shape"),

(150,0,-2.0,1.5, "Eye Width"),
(110,0,1.5,-1.5, "Eye to Eye Dist"),
(120,0,1.9,-1.9, "Eye Shape"),
(130,0,-1.7,1.7, "Eye Position"),
(140,0,-1.0,1.5, "Eyelids"),

(170,0,-2.5,2.0, "Eyebrow Height"),
(180,0,-2.5,1.2, "Eyebrow Shape"),
(260,0,1.5,-1.5, "Temple Width"),

(200,0,1.7,-1.7, "Face tall-short"),
(210,0,-1.7,1.7, "Face Depth"),
(250,0,-1.4,1.4, "Face Ratio"),
(190,0,-2.4,1.7, "Face Width"),

(280,0,0.0,1.0, "Post-Edit"),
]
no_face_keys = []

chin_size = 0
chin_shape = 1
chin_forward = 2
jaw_width = 3
jaw_position = 4
mouth_nose_distance = 5
mouth_width = 6
cheeks = 7
nose_height = 8
nose_width = 9
nose_size = 10
nose_shape = 11
nose_bridge = 12
cheek_bones = 13
eye_width = 14
eye_to_eye_dist = 15
eye_shape = 16
eye_depth = 17
eyelids = 18
eyebrow_position = 19
eyebrow_height = 20
eyebrow_depth = 21
eyebrow_shape = 22
temple_width = 23
face_depth = 24
face_ratio = 25
face_width = 26

comp_less_than = -1;
comp_greater_than = 1;

skins = [
#tf_man
("man", 0,
  "man_body", "dummy_mesh", "m_handL",
  "male_head", man_face_keys,
  ["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", 
  "man_hair_y10", "man_hair_y12", "man_hair_p", "man_hair_r", 
  "man_hair_q", "man_hair_v", "man_hair_t", "man_hair_y6", 
  "man_hair_y3", "man_hair_y7", "man_hair_y9", "man_hair_y11", 
  "man_hair_u", "man_hair_y", "man_hair_y2", "man_hair_y4",
  "man_hair_y4","shortlayer","shoulderhair","hairmessy",
  "slickedback","shortbob","straightshoulder","longshoulder",
  "longstraight","ponytail","courthair","shortcut"
  ],
  [
  "beard_e", "beard_d", "beard_k", "beard_l", 
  "beard_i", "beard_j", "beard_z", "beard_m", 
  "beard_n", "beard_y", "beard_p", "beard_o", 
  "beard_v", "beard_f", "beard_b", "beard_c", 
  "beard_t", "beard_u", "beard_r", "beard_s", 
  "beard_a", "beard_h", "beard_g", 
  "accessory_cigarette", "accessory_cigarette2", 
  "accessory_pipe_1","accessory_pipe_2",
  "accessory_single_earing","accessory_two_earings"
  ],
  ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
  ["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
  [
    ("manface_young_2", 0xFFCBE0E0, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
    ("manface_midage", 0xFFDFEFE1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
    ("manface_young", 0xFFD0E0E0, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("manface_young_3", 0xFFDCEDED, ["hair_blonde"], [0xff2f180e, 0xff171313, 0xff007080c]),
    ("manface_7", 0xFFC0C8C8, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_midage_2", 0xFDE4C8D8, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("manface_rugged", 0xFFB0AAB5, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_asian1", 0xFFE3E8E1, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_asian2", 0xFFE3E8E1, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_asian3", 0xFFBBB6AE, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_mideast1", 0xFFAEB0A6, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_mideast2", 0xFFD0C8C1, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_mideast3", 0xFFE0E8E8, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_black1", 0xFF87655C, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_black2", 0xFF5A342D, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_black3", 0xFF634D3E, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_white1", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
    ("manface_white2", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("manface_white3", 0xFFE0E8E8, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("manface_african", 0xFF807C8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
    ("male_face_1", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("male_face_2", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("male_face_3", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("male_face_4", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("male_face_5", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("male_face_6", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("male_face_7", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("male_face_8", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("male_face_9", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    #
        ("male_face_1_ff",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),
        ("male_face_2_ff",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),
        ("male_face_3_ff",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),
        ("male_face_4_ff",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),
        ("male_face_5_ff",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),
        ("male_face_6_ff",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),
        ("male_face_7_ff",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),
        ("male_face_8_ff",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),
        ("male_face_9_ff",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),
        ("male_face_10_ff",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),
       
        ("male_face_painted_1",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),
        ("male_face_painted_2",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),
        ("male_face_painted_3",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),
        ("male_face_painted_4",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),
        ("male_face_painted_5",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),
        ("male_face_painted_6",0xffffffff,["hair_blonde"],[0xffffffff, 0xff5E534B, 0xff5A382D, 0xff3F1D0E, 0xff120D0B]),	      
    
        ("male_face_10", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
        ("male_face_11", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
        ("male_face_12", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
        ("male_face_15", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
        # ("male_face_16", 0xFFE3E8E1, ["hair_blonde"], [0xff171313, 0xff007080c]),
        ("male_face_20", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
        ("male_face_24", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
        ("male_face_25", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
        #     
        ("highlander_young_b",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
        ("highlander_young_a",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
        ("manface_pict_vae1",0xffdceded,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
        ("manface_pict_vae2",0xffdceded,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
        ("manface_pict_vae3",0xffdceded,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
        ("manface_pict_vae4",0xffdceded,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
        ("manface_pict_vae5",0xffdceded,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
   ], #man_face_textures,
  [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
  "skel_human", 1.0,
  psys_game_blood,psys_game_blood_2,
  [
    [1.6, comp_greater_than, (1, 15),(1, 23)],
    [0.6, comp_less_than, (1, 15),(1, 23)],
    [1.5, comp_greater_than, (1, 25),(1, 6)],
    [0.6, comp_greater_than, (-1, 9),(1, 6)],
    [-1, comp_less_than, (-1, 9),(1, 6)],
  ]),
  
#tf_woman  
("woman", skf_use_morph_key_10,
  "woman_body",  "dummy_mesh", "f_handL",
  "female_head_warren_branch", woman_face_keys,
  ["woman_hair_01","woman_hair_02","woman_hair_03","woman_hair_04",
  "woman_hair_05","woman_hair_06","woman_hair_07","woman_hair_08",
  "woman_hair_09","woman_hair_10","woman_hair_11","woman_hair_12",
  "woman_hair_13","woman_hair_14","woman_hair_15","woman_hair_16",
  "woman_hair_17","woman_hair_18","woman_hair_19","woman_hair_20",
  "woman_hair_21","woman_hair_22","woman_hair_23","woman_hair_24",
  "woman_hair_25","woman_hair_26","woman_hair_27","woman_hair_28",
  "woman_hair_p","woman_hair_n","woman_hair_o","woman_hair_q",
  "woman_hair_r","woman_hair_t","woman_hair_s","female_maidenhair",
  "longstraightfem","ponytailfem"
  ],
  ["accessory_cigarette2", 
  "accessory_pipe_1","accessory_pipe_2",
  "accessory_single_earing","accessory_two_earings",
  "accessory_earring_1","accessory_earring_2","accessory_earring_3","accessory_earring_4",
  "accessory_earrings_1","accessory_earrings_2","accessory_earrings_3","accessory_earrings_4",
  "accessory_earrings_5","accessory_earrings_6","accessory_earrings_7","accessory_earrings_8",
  "accessory_earrings_9","accessory_earrings_10"
  ],
  ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
  [],
  [
   ("womanface_01",0xfff7f7f7,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_02",0xfff4eff1,["hair_blonde"],[0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_03",0xffeaebe5,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_04",0xffd4c0a7,["hair_blonde"],[0xff19100c, 0xff0c0d19, 0xff007080c]),
   ("womanface_05",0xff766668,["hair_blonde"],[0xff120808, 0xff007080c]),
   ("womanface_06",0xfff4eeeb,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_07",0xffeceeeb,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_08",0xffe6d1b4,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_09",0xfff9efe8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_10",0xfff3efed,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_11",0xfff6f3f1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_12",0xfff3eeea,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_13",0xffe9e5e5,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_14",0xffefefee,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_15",0xffebebed,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_16",0xfff7ece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_17",0xffedeae5,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_18",0xfff2f3f2,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_19",0xffe6e4e5,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_20",0xffe7eaea,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_21",0xffeaeae2,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_22",0xffeeece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   
   ("womanface_paint1",0xffeeece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_paint2",0xffeeece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_bpaint1",0xffeeece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_bpaint2",0xffeeece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_cult1",0xffeeece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_cult2",0xffeeece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_cult3",0xffeeece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_scars1",0xffeeece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_scars2",0xffeeece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_mud1",0xffeeece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_mud2",0xffeeece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_blood1",0xffeeece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   ("womanface_blood2",0xffeeece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
   #("womanface_paint1",0xffeeece8,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),

   ],#woman_face_textures
  [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_yell,"snd_woman_yell")], #voice sounds
  "skel_human", 0.95, psys_game_blood,psys_game_blood_2),

#tf_undead
("undead", 0,
  "man_body", "dummy_mesh", "m_handL",
  "dummy_mesh", man_face_keys,
  [
  "man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", 
  "man_hair_y10", "man_hair_y12", "man_hair_p", "man_hair_r", 
  "man_hair_q", "man_hair_v", "man_hair_t", "man_hair_y6", 
  "man_hair_y3", "man_hair_y7", "man_hair_y9", "man_hair_y11", 
  "man_hair_u", "man_hair_y", "man_hair_y2", "man_hair_y4"
  ],
  [
  "beard_e", "beard_d", "beard_k", "beard_l", 
  "beard_i", "beard_j", "beard_z", "beard_m", 
  "beard_n", "beard_y", "beard_p", "beard_o", 
  "beard_v", "beard_f", "beard_b", "beard_c", 
  "beard_t", "beard_u", "beard_r", "beard_s", 
  "beard_a", "beard_h", "beard_g"
  ],
  ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
  ["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
  [
    ("manface_young_2", 0xFFCBE0E0, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
    ("manface_midage", 0xFFDFEFE1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
    ("manface_young", 0xFFD0E0E0, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("manface_young_3", 0xFFDCEDED, ["hair_blonde"], [0xff2f180e, 0xff171313, 0xff007080c]),
    ("manface_7", 0xFFC0C8C8, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_midage_2", 0xFDE4C8D8, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("manface_rugged", 0xFFB0AAB5, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_asian1", 0xFFE3E8E1, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_asian2", 0xFFE3E8E1, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_asian3", 0xFFBBB6AE, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_mideast1", 0xFFAEB0A6, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_mideast2", 0xFFD0C8C1, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_mideast3", 0xFFE0E8E8, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_black1", 0xFF87655C, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_black2", 0xFF5A342D, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_black3", 0xFF634D3E, ["hair_blonde"], [0xff171313, 0xff007080c]),
    ("manface_white1", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
    ("manface_white2", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("manface_white3", 0xFFE0E8E8, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ("manface_african", 0xFF807C8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
   ], #man_face_textures,
  [(voice_die, "snd_infected_hit_male"),(voice_hit, "snd_infected_hit_male"),(voice_grunt, "snd_infected_hit_male"),(voice_grunt_long, "snd_infected_alerted_2"),(voice_yell, "snd_infected_hit_male"),(voice_stun, "snd_infected_hit_male"),(voice_victory, "snd_man_victory")],
  "skel_human", 1.0, 0, 0,[]),   

#tf_infected
("infected", 0,
    "man_body", "dummy_mesh", "m_handL",
    "male_head", man_face_keys,
    [
    "man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", 
    "man_hair_y10", "man_hair_y12", "man_hair_p", "man_hair_r", 
    "man_hair_q", "man_hair_v", "man_hair_t", "man_hair_y6", 
    "man_hair_y3", "man_hair_y7", "man_hair_y9", "man_hair_y11", 
    "man_hair_u", "man_hair_y", "man_hair_y2", "man_hair_y4"
    ],
    [
    "beard_e", "beard_d", "beard_k", "beard_l", 
    "beard_i", "beard_j", "beard_z", "beard_m", 
    "beard_n", "beard_y", "beard_p", "beard_o", 
    "beard_v", "beard_f", "beard_b", "beard_c", 
    "beard_t", "beard_u", "beard_r", "beard_s", 
    "beard_a", "beard_h", "beard_g"
    ],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    ["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
    [
      ("infected_manface_midage", 0xFFDFEFE1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("infected_manface_7", 0xFFC0C8C8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("infected_manface_midage_2", 0xFDE4C8D8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("infected_manface_rugged", 0xFFB0AAB5, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("infected_manface_asian1", 0xFFE3E8E1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("infected_manface_asian2", 0xFFE3E8E1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("infected_manface_asian3", 0xFFBBB6AE, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("infected_manface_mideast1", 0xFFAEB0A6, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("infected_manface_mideast2", 0xFFD0C8C1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("infected_manface_mideast3", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      # ("infected_manface_black1", 0xFF87655C, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      # ("infected_manface_black2", 0xFF5A342D, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      # ("infected_manface_black3", 0xFF634D3E, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      # ("infected_manface_white1", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      # ("infected_manface_white2", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      # ("infected_manface_white3", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      # ("infected_manface_african", 0xFF807C8A, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      # ("infected_manface_aged_midage", 0xFFDFEFE1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      # ("infected_manface_aged_7", 0xFFC0C8C8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      # ("infected_manface_aged_midage_2", 0xFDE4C8D8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      # ("infected_manface_aged_rugged", 0xFFB0AAB5, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      # ("infected_manface_aged_white1", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      # ("infected_manface_aged_white2", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      # ("infected_manface_aged_white3", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
     ], #man_face_textures,
    [(voice_die, "snd_nz_die"),(voice_hit, "snd_nz_hit"),(voice_grunt, "snd_nz_victory"),(voice_grunt_long, "snd_nz_grunt_long"),(voice_stun, "snd_nz_stun"),(voice_victory, "snd_nz_grunt")],
    "skel_human", 1.0, psys_game_blood, psys_game_blood_2, []),  
  
#tf_mutant
("mutant", 0,
    "dummy_mesh", "dummy_mesh", "dummy_mesh",
    "dummy_mesh", no_face_keys,
	[],[],
    ["hair_blonde"], #hair textures
    [], #beard_materials
    [("default",0xffffffff,["hair_blonde"],[]),
     ], #undead_face_textures
    [(voice_die, "snd_infected_hit_male"),(voice_hit, "snd_infected_hit_male"),(voice_grunt, "snd_infected_hit_male"),(voice_grunt_long, "snd_infected_alerted_2"),(voice_yell, "snd_infected_hit_male"),(voice_stun, "snd_infected_hit_male"),(voice_victory, "snd_man_victory")],
    "skel_human", 1.5,
    0, 0,
    # psys_game_blood_green, psys_game_blood_green_2,
    [
  ]),  

#tf_mutant_big
("mutant_big", 0,
    "dummy_mesh", "dummy_mesh", "dummy_mesh",
    "dummy_mesh", no_face_keys,
	[],[],
    ["hair_blonde"], #hair textures
    [], #beard_materials
    [("default",0xffffffff,["hair_blonde"],[]),
     ], #undead_face_textures
    [(voice_die, "snd_infected_hit_male"),(voice_hit, "snd_infected_hit_male"),(voice_grunt, "snd_infected_hit_male"),(voice_grunt_long, "snd_infected_alerted_2"),(voice_yell, "snd_infected_hit_male"),(voice_stun, "snd_infected_hit_male"),(voice_victory, "snd_man_victory")],
    "skel_human", 1.7,
    0, 0,
    # psys_game_blood_green, psys_game_blood_green_2,
    [
  ]),

#tf_ghoul
("ghoul", 0,
    "ghoul_zombie", "dummy_mesh", "dummy_mesh",
    "dummy_mesh", no_face_keys,
	[],[],
    ["hair_blonde"], #hair textures
    [], #beard_materials
    # [
    # ("default",0xffffffff,["hair_blonde"],[]
    [("default",0xffffffff,["hair_blonde"],[]),
    # ("manface_white_1",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
     ], #undead_face_textures
    [(voice_die, "snd_infected_hit_male"),(voice_hit, "snd_infected_hit_male"),(voice_grunt, "snd_infected_hit_male"),(voice_grunt_long, "snd_infected_alerted_2"),(voice_yell, "snd_infected_hit_male"),(voice_stun, "snd_infected_hit_male"),(voice_victory, "snd_man_victory")],
    "skel_ghoul", 1.0,
    0, 0,
    # psys_game_blood_green, psys_game_blood_green_2,
    [
  ]),  

#tf_ghoul_human  
("ghoul_human", 0,
    "human_ghoul_torso", "dummy_mesh", "ghoul_handL",
    "ghoul_head", no_face_keys,
    [
    "man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", 
    "man_hair_y10", "man_hair_y12", "man_hair_p", "man_hair_r", 
    "man_hair_q", "man_hair_v", "man_hair_t", "man_hair_y6", 
    "man_hair_y3", "man_hair_y7", "man_hair_y9", "man_hair_y11", 
    "man_hair_u", "man_hair_y", "man_hair_y2", "man_hair_y4"
    ],
    [
    "beard_e", "beard_d", "beard_k", "beard_l", 
    "beard_i", "beard_j", "beard_z", "beard_m", 
    "beard_n", "beard_y", "beard_p", "beard_o", 
    "beard_v", "beard_f", "beard_b", "beard_c", 
    "beard_t", "beard_u", "beard_r", "beard_s", 
    "beard_a", "beard_h", "beard_g"
    ],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    ["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
    # [
    [("ghoul_face_test",0xffffffff,["hair_blonde"],[]),
    # [("ghoul_face_test",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff632e18, 0xff19100c, 0xff83301a, 0xff0c0d19, 0xff2f180e, 0xff171313, 0xff007080c, 0xff120808]),
    # ("manface_white_1",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
     ], #undead_face_textures
    [(voice_die, "snd_infected_hit_male"),(voice_hit, "snd_infected_hit_male"),(voice_grunt, "snd_infected_hit_male"),(voice_grunt_long, "snd_infected_alerted_2"),(voice_yell, "snd_infected_hit_male"),(voice_stun, "snd_infected_hit_male"),(voice_victory, "snd_man_victory")],
    "skel_human", 1.0,
    0, 0,
    # psys_game_blood_green, psys_game_blood_green_2,
    [
  ]),  
   
#tf_rancor  
("rancor", 0,
    "dummy_mesh", "dummy_mesh", "dummy_mesh",
    "dummy_mesh", no_face_keys,
	[],[], # comment this out and uncomment the previous lines if you want hairy undeads...
    ["hair_blonde"], #hair textures
    [], #beard_materials
    [("default",0xffffffff,["hair_blonde"],[]),
     ], #undead_face_textures
     [(voice_die,"snd_gamorrean_die"),(voice_hit,"snd_gamorrean_hit"),(voice_grunt,"snd_gamorrean_grunt"),(voice_grunt_long,"snd_gamorrean_grunt_long"),(voice_yell,"snd_gamorrean_yell"),(voice_warcry,"snd_gamorrean_victory"),(voice_victory,"snd_gamorrean_victory")], #man voice sounds
     "skel_human", 1.0,
     #"skel_rancor", 1.0,   #new rancor skeleton
    0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
    [
  ]),   

#tf_droid 
("droid", 0,
    "dummy_mesh", "dummy_mesh", "dummy_mesh",
    "dummy_mesh", no_face_keys,
	[],[], # comment this out and uncomment the previous lines if you want hairy undeads...
    ["hair_blonde"], #hair textures
    [], #beard_materials
    [("default",0xffffffff,["hair_blonde"],[]),
     ], #undead_face_textures
     [(voice_die,"snd_battledroid_die"),(voice_hit,"snd_battledroid_hit"),(voice_grunt,"snd_battledroid_grunt"),(voice_grunt_long,"snd_battledroid_grunt_long"),(voice_yell,"snd_battledroid_yell"),(voice_warcry,"snd_battledroid_victory"),(voice_victory,"snd_battledroid_victory")], #r2series voice sounds
    "skel_human", 1.0,
    0,0,
    [
  ]),  
  
#tf_test
("test", 0,
    "dummy_mesh", "dummy_mesh", "dummy_mesh",
    "dummy_mesh", no_face_keys,
	[],[],
    ["hair_blonde"], #hair textures
    [], #beard_materials
    [("default",0xffffffff,["hair_blonde"],[]),
     ], #undead_face_textures
    [], #voice sounds
    "skel_test", 1.0,
    0,0,
    # psys_game_blood,psys_game_blood_2,
    [
  ]),  

#tf_dummy
("dummy", 0,
    "dummy_mesh", "dummy_mesh", "dummy_mesh",
    "dummy_mesh", no_face_keys,
	[],[],
    ["hair_blonde"], #hair textures
    [], #beard_materials
    [("default",0xffffffff,["hair_blonde"],[]),
     ], #undead_face_textures
    [], #voice sounds
    "skel_human", 1.0,
    0,0,
    # psys_game_blood,psys_game_blood_2,
    [
  ]),    

#tf_man_high
("man_high", 0,
    # "man_body", "man_calf_l", "m_handL",
    "man_body", "dummy_mesh", "m_handL",
    "male_head", man_face_keys,
    ["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", "man_hair_y10", "man_hair_y12", "man_hair_p", "man_hair_r", "man_hair_q", "man_hair_v", "man_hair_t", "man_hair_y6", "man_hair_y3", "man_hair_y7", "man_hair_y9", "man_hair_y11", "man_hair_u", "man_hair_y", "man_hair_y2", "man_hair_y4"],
    ["beard_e", "beard_d", "beard_k", "beard_l", "beard_i", "beard_j", "beard_z", "beard_m", "beard_n", "beard_y", "beard_p", "beard_o", "beard_v", "beard_f", "beard_b", "beard_c", "beard_t", "beard_u", "beard_r", "beard_s", "beard_a", "beard_h", "beard_g"],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    ["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
    [
      ("manface_young_2", 0xFFCBE0E0, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
      ("manface_midage", 0xFFDFEFE1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
      ("manface_young", 0xFFD0E0E0, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("manface_young_3", 0xFFDCEDED, ["hair_blonde"], [0xff2f180e, 0xff171313, 0xff007080c]),
      ("manface_7", 0xFFC0C8C8, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_midage_2", 0xFDE4C8D8, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("manface_rugged", 0xFFB0AAB5, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_asian1", 0xFFE3E8E1, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_asian2", 0xFFE3E8E1, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_asian3", 0xFFBBB6AE, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_mideast1", 0xFFAEB0A6, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_mideast2", 0xFFD0C8C1, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_mideast3", 0xFFE0E8E8, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_black1", 0xFF87655C, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_black2", 0xFF5A342D, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_black3", 0xFF634D3E, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_white1", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
      ("manface_white2", 0xFFE0E8E8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("manface_white3", 0xFFE0E8E8, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("manface_african", 0xFF807C8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_stun,"snd_man_stun"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human_high", 1.0,
    0,0,
    [
      [1.6, comp_greater_than, (1, 15),(1, 23)],
      [0.6, comp_less_than, (1, 15),(1, 23)],
      [1.5, comp_greater_than, (1, 25),(1, 6)],
      [0.6, comp_greater_than, (-1, 9),(1, 6)],
      [-1, comp_less_than, (-1, 9),(1, 6)],
    ]
  ),

#tf_skeleton
("skeleton", 0,
    "Body_Skeleton_01", "Legs_Skeleton_01_L", "Hand_Skeleton_02_L",
    "Head_Skeleton_01",
    [
      (20, 0, 0.7, -0.6, "Chin Size"),
      (260, 0, -0.6, 1.4, "Chin Shape"),
      (10, 0, -0.5, 0.9, "Chin Forward"),
      (240, 0, 0.9, -0.8, "Jaw Width"),
      (210, 0, -0.5, 1, "Jaw Position"),
      (250, 0, 0.8, -1, "Mouth-Nose Distance"),
      (200, 0, -0.3, 1, "Mouth Width"),
      (50, 0, -1.5, 1, "Cheeks"),
      (60, 0, -0.4, 1.35, "Nose Height"),
      (70, 0, -0.6, 0.7, "Nose Width"),
      (80, 0, 1, -0.1, "Nose Size"),
      (270, 0, -0.5, 1, "Nose Shape"),
      (90, 0, -0.2, 1.4, "Nose Bridge"),
      (100, 0, -0.3, 1.5, "Cheek Bones"),
      (150, 0, -0.2, 3, "Eye Width"),
      (110, 0, 1.5, -0.9, "Eye to Eye Dist"),
      (120, 0, 1.9, -1, "Eye Shape"),
      (130, 0, -0.5, 1.1, "Eye Depth"),
      (140, 0, 1, -1.2, "Eyelids"),
      (160, 0, 1.3, -0.2, "Eyebrow Position"),
      (170, 0, -0.1, 1.9, "Eyebrow Height"),
      (220, 0, -0.1, 0.9, "Eyebrow Depth"),
      (180, 0, -1.1, 1.6, "Eyebrow Shape"),
      (230, 0, 1.2, -0.7, "Temple Width"),
      (30, 0, -0.6, 0.9, "Face Depth"),
      (40, 0, 0.9, -0.6, "Face Ratio"),
      (190, 0, 0, 0.95, "Face Width"),
      (280, 0, 0, 1, "Post-Edit"),
    ],
    [],
    [],
    ["hair_blonde"],
    [],
    [
      ("skeleton_Head_Diffuse_01", 0xFFCBE0E0, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
    ],
    [(voice_die, "snd_infected_hit_male"),(voice_hit, "snd_infected_hit_male"),(voice_grunt, "snd_infected_hit_male"),(voice_grunt_long, "snd_infected_alerted_2"),(voice_yell, "snd_infected_hit_male"),(voice_stun, "snd_infected_hit_male"),(voice_victory, "snd_man_victory")],
    "skel_human", 1.000000,
    psys_game_blood, psys_game_blood_2,
    [
      [1.7, comp_greater_than, (1, 26),(1, 23)],
      [0.3, comp_less_than, (1, 26),(1, 23)],
      [1.7, comp_greater_than, (1, 26),(1, 24)],
      [0.3, comp_less_than, (1, 20),(1, 19)],
      [1.7, comp_greater_than, (1, 20),(1, 19)],
      [-0.7, comp_less_than, (1, 10),(-1, 11)],
      [0.7, comp_greater_than, (1, 10),(-1, 11)],
      [2.7, comp_greater_than, (1, 0),(1, 5),(1, 8),(-1, 26)],
  ]),

#tf_droid_big
(
    "droid_big", 0,
    "dummy_mesh", "dummy_mesh", "dummy_mesh",
    "dummy_mesh", [
      (20, 0, 0.7, -0.6, "Chin Size"),
      (260, 0, -0.6, 1.4, "Chin Shape"),
      (10, 0, -0.5, 0.9, "Chin Forward"),
      (240, 0, 0.9, -0.8, "Jaw Width"),
      (210, 0, -0.5, 1, "Jaw Position"),
      (250, 0, 0.8, -1, "Mouth-Nose Distance"),
      (200, 0, -0.3, 1, "Mouth Width"),
      (50, 0, -1.5, 1, "Cheeks"),
      (60, 0, -0.4, 1.35, "Nose Height"),
      (70, 0, -0.6, 0.7, "Nose Width"),
      (80, 0, 1, -0.1, "Nose Size"),
      (270, 0, -0.5, 1, "Nose Shape"),
      (90, 0, -0.2, 1.4, "Nose Bridge"),
      (100, 0, -0.3, 1.5, "Cheek Bones"),
      (150, 0, -0.2, 3, "Eye Width"),
      (110, 0, 1.5, -0.9, "Eye to Eye Dist"),
      (120, 0, 1.9, -1, "Eye Shape"),
      (130, 0, -0.5, 1.1, "Eye Depth"),
      (140, 0, 1, -1.2, "Eyelids"),
      (160, 0, 1.3, -0.2, "Eyebrow Position"),
      (170, 0, -0.1, 1.9, "Eyebrow Height"),
      (220, 0, -0.1, 0.9, "Eyebrow Depth"),
      (180, 0, -1.1, 1.6, "Eyebrow Shape"),
      (230, 0, 1.2, -0.7, "Temple Width"),
      (30, 0, -0.6, 0.9, "Face Depth"),
      (40, 0, 0.9, -0.6, "Face Ratio"),
      (190, 0, 0, 0.95, "Face Width"),
      (280, 0, 0, 1, "Post-Edit"),
    ],
    [],
    [],
    ["hair_blonde"],
    [],
    [
      ("skeleton_Head_Diffuse_01", 0xFFCBE0E0, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
    ], #man_face_textures,
    [(voice_die,"snd_battledroid_die"),(voice_hit,"snd_battledroid_hit"),(voice_grunt,"snd_battledroid_grunt"),(voice_grunt_long,"snd_battledroid_grunt_long"),(voice_yell,"snd_battledroid_yell"),(voice_warcry,"snd_battledroid_victory"),(voice_victory,"snd_battledroid_victory")], #r2series voice sounds
    "skel_ssh_flesh_golem", 1.50,
    psys_game_blood,psys_game_blood_2,
  ),    
]# modmerger_start version=201 type=2
try:
    component_name = "skins"
    var_set = { "skins" : skins }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
