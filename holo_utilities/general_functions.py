import bpy

class HOLUTS_OT_toggle_hide (bpy.types.Operator):
    bl_idname = 'toggle_hide.operator'
    bl_label = 'Toggle Hide'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = 'Toggles the hide status on objects selected in the outliner.'

    @classmethod
    def poll(cls, context):
        screen = bpy.context.screen
        area = [area for area in screen.areas if area.type == 'OUTLINER'][0]
        region = [region for region in area.regions if region.type == 'WINDOW'][0]

        with bpy.context.temp_override(screen=screen,area=area,region=region):
            return len(context.selected_ids) != 0
        return False
    
    def execute(self, context):
        
        screen = bpy.context.screen
        area = [area for area in screen.areas if area.type == 'OUTLINER'][0]
        region = [region for region in area.regions if region.type == 'WINDOW'][0]

        with bpy.context.temp_override(screen=screen,area=area,region=region):
        
            hide_action = self.unhide_selected
            ids = context.selected_ids        

            objects = [id for id in ids if isinstance(id, bpy.types.Object)]

            for obj in objects:
                if not obj.hide_get() and not obj.hide_viewport:
                    hide_action = self.hide_selected
                    break

            for obj in objects:
                hide_action(obj)

        return {'FINISHED'}
    
    def hide_selected(self, obj):
        obj.hide_set(True)

    def unhide_selected(self, obj):
        obj.hide_viewport = False
        obj.hide_set(False)
        obj.select_set(True)



#classes = (HOLUTS_OT_toggle_hide)

def register():
    #for cls in classes:
    bpy.utils.register_class(HOLUTS_OT_toggle_hide)

def unregister():
    #for cls in classes:
    bpy.utils.unregister_class(HOLUTS_OT_toggle_hide)