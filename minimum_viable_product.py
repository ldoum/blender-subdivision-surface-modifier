#first written on Tuesday 9/2/2025 1122pm
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
    
    if obj.type == 'MESH': 
        """
        options 
        1 to add mod, 
        2 for deletion for specific mod, 
        3 for deletion of all mods, 
        4 for applying the existing mod,
        5 for applying all mods in many objects
        """

        #main input
        option = 2

        match option:
        
            case 1:
            
                #input here
                mod_type = 'SUBSURF'
                tag = 'Subdivide surface'
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
            
                del_tag = 'Subdivide surface'
            
                mod_exists = obj.modifiers.get(del_tag)
            
                if mod_exists:
                    remove_exact_mod(obj, del_tag)

            case 3:
            
                for wipe in obj.modifiers:
                    obj.modifiers.remove(wipe)
                
            case 4:
                apply_tag = 'Subdivide surface'
            
                #added the apply modifier
                mod_is_here = obj.modifiers.get(apply_tag)
            
                if mod_is_here:
                
                    bpy.context.view_layer.objects.active = obj #need this before the bottom line
                    bpy.ops.object.modifier_apply(modifier=apply_tag)
                
            case 5:
                
                for supe in obj.modifiers:
                    bpy.context.view_layer.objects.active = obj #need this before the bottom line
                    bpy.ops.object.modifier_apply(modifier=supe.name)
                    
            case _:
                pass
