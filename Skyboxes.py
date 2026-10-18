import string
from module_info import *

## Flags ##

sf_day        = 0x00000000
sf_dawn       = 0x00000001
sf_night      = 0x00000002  
sf_mask       = 0x00000003 # Code from https://forums.taleworlds.com/index.php?topic=218069.0 Thanks to Xenoargh. 
#                             This Flag means the skybox must be called manually won't appear otherwise. The link has more info for calling a Skybox.
                             
#Global Cloud Amount (GCA) effects when clouds will appear. When GCA is 100 there will be rain or snow present.

sf_clouds_0   = 0x00000000  # GCA 00-15
sf_clouds_1   = 0x00000010  # GCA 16-50
sf_clouds_2   = 0x00000020  # GCA 51-85
sf_clouds_3   = 0x00000030  # GCA 86-100

sf_no_shadows = 0x10000000  # Simply removes shadows
sf_HDR        = 0x20000000  # This will generate HDR-shaded skyboxes, you should make a LDR version of your skybox for compatibility

## Headers ##

# Mesh_Name      - Name of the skybox
# Flags          - When the skybox will appear, effected by time of day, Cloud amount and Haze (Fog)
#         -Flag-   -Condition-          
# 	sf_day      
# 	sf_dawn       
# 	sf_night    
# 	sf_mask       Only when called


# Heading        - Depreciated due to aligning all textures previously (Sun in the middle of the texture)
# Altitude       - 0 = Horizon 90 = Highest Position
# Flare          - Amount of Sun flare 0-1
# Postfx         - How the HDR rendering is effected, lighting was corrected in postfx.py to be uniform for accurate idividual skybox inputs.
# Sun_Colour     - This is the sunlight R G B in the weather settings.
# Hemi_Colour    - Not used.
# Ambient Colour - This is the Ambient R G B in the weather settings.
# Fog Start      - As far as I can tell not used, it is set by global_haze_amount (fog) or set to a default value.
# Fog Colour     - Use the RGB values of Fog in the weather settings and plug them into http://www.colorpicker.com/ to get the Hex colour code, 
#                    NOTE: 0xFF is the unused alpha value and must be before the Hex code.

#     mesh_name          flags,      heading, altitude, flare, postfx,           sun_color,             hemi_color,           ambient_color,        (fog_start, fog_color),

skyboxes = [
  ("skybox_map", sf_mask|sf_HDR, 0, 50, 1, "pfx_sunny", (1.8348, 1.6819, 1.5012), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),

  ("skybox_clearday", sf_day|sf_clouds_0|sf_HDR, 0, 50, 1, "pfx_sunny", (1.3068, 1.1979, 1.0692), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),
  ("skybox_clearday_new_1", sf_day|sf_clouds_0|sf_HDR, 0, 50, 1, "pfx_sunny", (1.3068, 1.1979, 1.0692), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),
  ("skybox_clearday_new_2", sf_day|sf_clouds_0|sf_HDR, 0, 50, 1, "pfx_sunny", (1.3068, 1.1979, 1.0692), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),
  ("skybox_clearday_new_3", sf_day|sf_clouds_0|sf_HDR, 0, 50, 1, "pfx_sunny", (1.3068, 1.1979, 1.0692), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),
  ("skybox_clearday_new_4", sf_day|sf_clouds_0|sf_HDR, 0, 50, 1, "pfx_sunny", (1.3068, 1.1979, 1.0692), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),
  # ("skybox_new_clear_1", sf_day|sf_clouds_0|sf_HDR, 0, 50, 1, "pfx_sunny", (1.3068, 1.1979, 1.0692), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),

  ("skybox_cloud_1", sf_day|sf_clouds_1|sf_HDR, 0, 50, 1, "pfx_sunny", (1.8348, 1.6819, 1.5012), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),
  ("skybox_cloud_1_new_1", sf_day|sf_clouds_1|sf_HDR, 0, 50, 1, "pfx_sunny", (1.8348, 1.6819, 1.5012), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),
  ("skybox_cloud_1_new_2", sf_day|sf_clouds_1|sf_HDR, 0, 50, 1, "pfx_sunny", (1.8348, 1.6819, 1.5012), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),
  ("skybox_cloud_1_new_3", sf_day|sf_clouds_1|sf_HDR, 0, 50, 1, "pfx_sunny", (1.8348, 1.6819, 1.5012), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),
  ("skybox_cloud_1_new_4", sf_day|sf_clouds_1|sf_HDR, 0, 50, 1, "pfx_sunny", (1.8348, 1.6819, 1.5012), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),
  ("skybox_cloud_1_new_5", sf_day|sf_clouds_1|sf_HDR, 0, 50, 1, "pfx_sunny", (1.8348, 1.6819, 1.5012), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),
  ("skybox_cloud_1_new_6", sf_day|sf_clouds_1|sf_HDR, 0, 50, 1, "pfx_sunny", (1.8348, 1.6819, 1.5012), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),
  # ("skybox_new_cloud_1", sf_day|sf_clouds_1|sf_HDR, 0, 50, 1, "pfx_sunny", (1.8348, 1.6819, 1.5012), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),
  # ("skybox_new_cloud_2", sf_day|sf_clouds_1|sf_HDR, 0, 50, 1, "pfx_sunny", (1.8348, 1.6819, 1.5012), (0, 0, 0), (0.053961, 0.079255, 0.150078), (300, 0xFF8CA2AD)),
  
  ("skybox_cloud_2", sf_day|sf_clouds_2|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  ("skybox_cloud_2_new_1", sf_day|sf_clouds_2|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  ("skybox_cloud_2_new_2", sf_day|sf_clouds_2|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  ("skybox_cloud_2_new_3", sf_day|sf_clouds_2|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  ("skybox_cloud_2_new_4", sf_day|sf_clouds_2|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  ("skybox_cloud_2_new_5", sf_day|sf_clouds_2|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  ("skybox_cloud_2_new_6", sf_day|sf_clouds_2|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  ("skybox_cloud_2_new_7", sf_day|sf_clouds_2|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),

  ("skybox_cloud_2_overcast", sf_day|sf_clouds_3|sf_no_shadows|sf_HDR, 0, 50, 0, "pfx_overcast", (0.4, 0.35, 0.31), (0, 0, 0), (0.196078, 0.235294, 0.403922), (120, 0xFF607090)),
  ("skybox_cloud_2_overcast_new_1", sf_day|sf_clouds_2|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  ("skybox_cloud_2_overcast_new_2", sf_day|sf_clouds_2|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  ("skybox_cloud_2_overcast_new_3", sf_day|sf_clouds_2|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  ("skybox_cloud_2_overcast_new_4", sf_day|sf_clouds_2|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  ("skybox_cloud_2_overcast_new_5", sf_day|sf_clouds_2|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  ("skybox_cloud_2_overcast_new_6", sf_day|sf_clouds_2|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  ("skybox_cloud_2_overcast_new_7", sf_day|sf_clouds_2|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  # ("skybox_new_overcast_1", sf_day|sf_clouds_3|sf_no_shadows|sf_HDR, 0, 50, 0, "pfx_overcast", (0.4, 0.35, 0.31), (0, 0, 0), (0.196078, 0.235294, 0.403922), (120, 0xFF607090)),

  # ("skybox_night_1", sf_night|sf_clouds_1|sf_HDR, 0, 35, 0, "pfx_night", (0.066667, 0.082353, 0.105882), (0, 0, 0), (0.017647, 0.017647, 0.052941), (500, 0xFF152035)),
  # ("skybox_night_2", sf_night|sf_clouds_3|sf_HDR, 0, 35, 0, "pfx_night", (0.066667, 0.082353, 0.105882), (0, 0, 0), (0.017647, 0.017647, 0.052941), (500, 0xFF152035)),
  
  ##First release, too dark
  # ("skybox_night_1", sf_night|sf_clouds_1|sf_HDR, 0, 35, 0, "pfx_night", (0.066667, 0.082353, 0.105882), (0, 0, 0), (0.017647, 0.017647, 0.052941), (500, 0xFF05070C)),
  # ("skybox_night_1_new_1", sf_night|sf_clouds_1|sf_HDR, 0, 35, 0, "pfx_night", (0.066667, 0.082353, 0.105882), (0, 0, 0), (0.017647, 0.017647, 0.052941), (500, 0xFF05070C)),
  # ("skybox_night_1_new_2", sf_night|sf_clouds_1|sf_HDR, 0, 35, 0, "pfx_night", (0.066667, 0.082353, 0.105882), (0, 0, 0), (0.017647, 0.017647, 0.052941), (500, 0xFF05070C)),
  # ("skybox_night_1_new_3", sf_night|sf_clouds_1|sf_HDR, 0, 35, 0, "pfx_night", (0.066667, 0.082353, 0.105882), (0, 0, 0), (0.017647, 0.017647, 0.052941), (500, 0xFF05070C)),
  # ("skybox_night_1_new_4", sf_night|sf_clouds_1|sf_HDR, 0, 35, 0, "pfx_night", (0.066667, 0.082353, 0.105882), (0, 0, 0), (0.017647, 0.017647, 0.052941), (500, 0xFF05070C)),
  # ("skybox_night_2", sf_night|sf_clouds_3|sf_HDR, 0, 35, 0, "pfx_night", (0.066667, 0.082353, 0.105882), (0, 0, 0), (0.017647, 0.017647, 0.052941), (500, 0xFF05070C)),
  # ("skybox_night_2_new_1", sf_night|sf_clouds_3|sf_HDR, 0, 35, 0, "pfx_night", (0.066667, 0.082353, 0.105882), (0, 0, 0), (0.017647, 0.017647, 0.052941), (500, 0xFF05070C)),
  
  ##Native
    ("skybox_night_1", sf_night|sf_clouds_1, 152.0, 38.0, 0.0, "pfx_night", (1.0*17.0/255,1.0*21.0/255,1.0*27.0/255),(0.0,0.0,0.0), (0.9*5.0/255,0.9*5.0/255,0.9*15.0/255), (500, 0xFF152035)),
  ("skybox_night_1", sf_night|sf_clouds_1|sf_HDR, 152.0, 38.0, 0.0, "pfx_night", (1.0*17.0/255,1.0*21.0/255,1.0*27.0/255),(0.0,0.0,0.0), (0.9*5.0/255,0.9*5.0/255,0.9*15.0/255), (500, 0xFF152035)),
  ("skybox_night_2", sf_night|sf_clouds_3, 152.0, 38.0, 0.0, "pfx_night", (1.0*17.0/255,1.0*21.0/255,1.0*27.0/255),(0.0,0.0,0.0), (0.9*5.0/255,0.9*5.0/255,0.9*15.0/255), (500, 0xFF152035)),
  ("skybox_night_2", sf_night|sf_clouds_3|sf_HDR, 152.0, 38.0, 0.0, "pfx_night", (1.0*17.0/255,1.0*21.0/255,1.0*27.0/255),(0.0,0.0,0.0), (0.9*5.0/255,0.9*5.0/255,0.9*15.0/255), (500, 0xFF152035)),

  
  # ("skybox_new_sunset_1", sf_dawn|sf_clouds_0|sf_HDR, 0, 45, 0.7, "pfx_sunset", (1.045455, 0.545455, 0.168182), (0, 0, 0), (0.069048, 0.1, 0.190476), (150, 0xFF897262)),    
  # ("skybox_new_sunset_1", sf_dawn|sf_clouds_0|sf_HDR, 0, 12, 0.7, "pfx_sunset", (1.045455, 0.545455, 0.168182), (0, 0, 0), (0.069048, 0.1, 0.190476), (150, 0xFF897262)),  
  ("skybox_sunset_1_new_1", sf_dawn|sf_clouds_1|sf_HDR, 0, 12, 0.7, "pfx_sunset", (1.045455, 0.545455, 0.168182), (0, 0, 0), (0.069048, 0.1, 0.190476), (150, 0xFF897262)),
  ("skybox_sunset_1_new_2", sf_dawn|sf_clouds_1|sf_HDR, 0, 12, 0.7, "pfx_sunset", (1.045455, 0.545455, 0.168182), (0, 0, 0), (0.069048, 0.1, 0.190476), (150, 0xFF897262)),
  ("skybox_sunset_1_new_3", sf_dawn|sf_clouds_1|sf_HDR, 0, 12, 0.7, "pfx_sunset", (1.045455, 0.545455, 0.168182), (0, 0, 0), (0.069048, 0.1, 0.190476), (150, 0xFF897262)),
  ("skybox_sunset_1_new_4", sf_dawn|sf_clouds_1|sf_HDR, 0, 12, 0.7, "pfx_sunset", (1.045455, 0.545455, 0.168182), (0, 0, 0), (0.069048, 0.1, 0.190476), (150, 0xFF897262)),

  ("skybox_sunset_2", sf_dawn|sf_clouds_2|sf_HDR, 0, 12, 0.7, "pfx_sunset", (1.045455, 0.545455, 0.168182), (0, 0, 0), (0.069048, 0.1, 0.190476), (150, 0xFF897262)),
  ("skybox_sunset_2_new_1", sf_dawn|sf_clouds_2|sf_HDR, 0, 12, 0.7, "pfx_sunset", (1.045455, 0.545455, 0.168182), (0, 0, 0), (0.069048, 0.1, 0.190476), (150, 0xFF897262)),
  ("skybox_sunset_2_new_2", sf_dawn|sf_clouds_2|sf_HDR, 0, 12, 0.7, "pfx_sunset", (1.045455, 0.545455, 0.168182), (0, 0, 0), (0.069048, 0.1, 0.190476), (150, 0xFF897262)),
  ("skybox_sunset_2_new_3", sf_dawn|sf_clouds_2|sf_HDR, 0, 12, 0.7, "pfx_sunset", (1.045455, 0.545455, 0.168182), (0, 0, 0), (0.069048, 0.1, 0.190476), (150, 0xFF897262)),
  ("skybox_sunset_2_new_4", sf_dawn|sf_clouds_2|sf_HDR, 0, 12, 0.7, "pfx_sunset", (1.045455, 0.545455, 0.168182), (0, 0, 0), (0.069048, 0.1, 0.190476), (150, 0xFF897262)),
  ("skybox_sunset_2_new_5", sf_dawn|sf_clouds_2|sf_HDR, 0, 12, 0.7, "pfx_sunset", (1.045455, 0.545455, 0.168182), (0, 0, 0), (0.069048, 0.1, 0.190476), (150, 0xFF897262)),


  # ("skybox_vol", sf_mask|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  ("skybox_tox", sf_mask|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  # ("skybox_orange", sf_mask|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  ("skybox_orange_2", sf_mask|sf_HDR, 0, 50, 0, "pfx_cloudy", (0.72, 0.68, 0.6), (0, 0, 0), (0.12549, 0.145882, 0.241569), (120, 0xFF607090)),
  
]

def convert_to_identifier(s0):
  s1 = string.replace(s0," ","_")
  s2 = string.replace(s1,"'","_")
  s3 = string.replace(s2,"`","_")
  s4 = string.replace(s3,"(","_")
  s5 = string.replace(s4,")","_")
  s6 = string.replace(s5,"-","_")
  s7 = string.replace(s6,",","")
  s8 = string.replace(s7,"|","")
  s9 = string.replace(s8,"\t","_") #Tab
  s10 = string.lower(s9)
  return s10

def save_skyboxes():
  file = open(export_dir_sky + "skyboxes.txt","w")
  file.write("%d\n"%len(skyboxes))
  for skybox in  skyboxes:
    file.write("%s %d %f %f %f %s\n"%(skybox[0],skybox[1],skybox[2],skybox[3],skybox[4],skybox[5]))
    file.write(" %f %f %f "%skybox[6])
    file.write(" %f %f %f "%skybox[7])
    file.write(" %f %f %f "%skybox[8])
    file.write(" %f %d\n"%skybox[9])
  file.close()

def save_id_file():
    ofile = open( "./ID_skyboxes.py","w")
    for i_skyboxes in xrange(len(skyboxes)):
        ofile.write("sb_%s = %d\n"%(convert_to_identifier(skyboxes[i_skyboxes][0]),i_skyboxes))
    ofile.write("\n\n")
    ofile.close()

print "Exporting skyboxes..."
save_skyboxes()
save_id_file()
print "Finished."