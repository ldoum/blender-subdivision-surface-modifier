#written on Tuesdy 9/2/2025 1122pm
import bpy

"""
This function serves as the basic functionality of the subdivision surface modifier.

Variables:
meshy - the 3d object itself
what - the given name of the modifier
"""

def subdivision_mod(meshy, what):
    
    more_faces = meshy.modifiers.new(name=what, type='SUBSURF')

    #input block 1 - type 0 to disable, 1 to enable
    more_faces.show_on_cage = bool(1)
    more_faces.show_in_editmode = bool(1)
    more_faces.show_viewport = bool(1)
    more_faces.show_render = bool(1)

    #input block 2 - set type of subdivision
    more_faces.subdivision_type = 'CATMULL_CLARK' #type 'SIMPLE' if you wish
    more_faces.show_only_control_edges = True   #optimal display

    key = 2
    more_faces.levels = key  #viewport levels
    more_faces.render_levels = key

        
# Iterate over all selected objects
for obj in bpy.context.selected_objects:
    
    if obj.type == 'MESH':  
        
        #input here
        mod_type = 'SUBSURF'
        tag = 'subdivide seriously'
        default = 'no'
   
        match mod_type:
             
            case 'SUBSURF':
                
                if default == 'yes':
                    obj.modifiers.new(name=tag, type=mod_type)
                else: 
                    subdivision_mod(obj, tag)
                        
            case _:
                pass
                 
        bpy.context.view_layer.objects.active = obj #important; adds modifier

