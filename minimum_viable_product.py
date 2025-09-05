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

    #input 1
    more_faces.show_on_cage = bool(1)
    more_faces.show_in_editmode = bool(1)
    more_faces.show_viewport = bool(1)
    more_faces.show_render = bool(1)

    #input 2
    subdiv_type = 1
   
    match subdiv_type:
            
        case 1:
            more_faces.subdivision_type = 'CATMULL_CLARK'
                
        case 2:
            more_faces.subdivision_type = 'SIMPLE'
            
    #input 3      
    more_faces.show_only_control_edges = True

    #input 4
    key = 2
    
    more_faces.levels = key
    more_faces.render_levels = key
    
#included this feature    
def remove_exact_mod(unwanted, retrieve):
    unwanted.modifiers.remove(unwanted.modifiers[retrieve])

        
# Iterate over all selected objects
for obj in bpy.context.selected_objects:
    
    """
    option 1 to add mod, 2 for deletion for specific mod, 3 for deletion of all mods
    """

    #main input
    option = 2
    
    match option:
        
        case 1:
            
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
                 
            bpy.context.view_layer.objects.active = obj
            
        case 2:
            
            say_name_delete = "Subdivision.001"

            #check if modifier exists before removing
            mod_exists = obj.modifiers.get(say_name_delete)
            
            if mod_exists:
                remove_exact_mod(obj, say_name_delete)
            
            #added the clear all mods feature
        case 3:
            
            for wipe in obj.modifiers:
                obj.modifiers.remove(wipe)

        case _:
            pass
