# Warzone Acron automatically generates 2 additional versions of each gun for the ai to use. This is necessary for the toggling aim system the player uses. 
#(You can find it in process_items.py, but you shouldn't need to edit it.)

# This means that adding new guns has additional steps to avoid item ID conflicts when compiling:

##	1. - Only add new guns between the existing "itm_pistol_1911" and "buffer_gun_1" items.  This is the section that gets duplicated for NPC versions.

##	2. - Only add 9 or less new guns at a time. Then compile twice. Then add the next set. Then compile twice, and so on.


#If you mess this up and end up with messages about "itm_ai_gun_whatever" being missing you can maybe fix it by adding it manually to the bottom of your ID_items file, then compiling twice again.

#Additional:
#You should probably check the ranges set in module constants, such as rifle_begin rifle_end. Then place new guns within the appropriate section as some scripts will work differently for them.
#In module_warzone_scripts there is a script called "init_firearms" where you can set the gun's ammo type, animation, if it has a scope and son on. 
#You can also set the ironsight mesh here. Ironsight meshes are technically scene props you have to create. Look in module_scene_props for examples.