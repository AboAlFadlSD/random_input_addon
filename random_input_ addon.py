bl_info = {
    "name": "Random Input",
    "author": "AboAlFadl SerajEddin",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > UI",
    "description": "apply constant or random values to multiple objects",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
}


import bpy
import random
import numpy as np
from math import pi


#methods
#def ranged(li,po,start,end):
 #   m = list(np.arange(0,1,1/(li-1)))
  #  m.append(1)
   # power = po
    #expressed = [(lambda x :x**power)(i)  for i in m]
    #diff= end-start
    #values = [start+(i*diff) for i in expressed]
    #return values


def Random_Location (xs, xe, ys, ye, zs, ze, o):
    
    Selected_objects= bpy.context.selected_objects
    Active_object = bpy.context.view_layer.objects.active
    bpy.ops.object.select_all(action='DESELECT')
    Orient_type_list= ['GLOBAL','LOCAL']
    
    for i in Selected_objects:
        Random_Nx= random.uniform(xs, xe)
        Random_Ny= random.uniform(ys, ye)
        Random_Nz= random.uniform(zs, ze)
        i.select_set(True)
        bpy.context.view_layer.objects.active = i
        bpy.ops.transform.translate(value= (Random_Nx,Random_Ny,Random_Nz ), orient_type=Orient_type_list[o if o==1 or o==0 else 0])
        bpy.ops.object.select_all(action='DESELECT')
    for i in Selected_objects:
        i.select_set(True)
    bpy.context.view_layer.objects.active = Active_object
    
def Ranged_Location (xs, xe, ys, ye, zs, ze, o, po):
    
    Selected_objects= bpy.context.selected_objects
    Active_object = bpy.context.view_layer.objects.active
    bpy.ops.object.select_all(action='DESELECT')
    Orient_type_list= ['GLOBAL','LOCAL']
  
    
    l= len(Selected_objects)
    m = list(np.arange(0,1,1/(l-1)))
    m.append(1)
    expressed = [(lambda x :x**po)(i)  for i in m]
    xd= xe-xs
    yd= ye-ys
    zd= ze-zs
    xv=[xs+(i*xd) for i in expressed]
    yv=[ys+(i*yd) for i in expressed]
    zv=[zs+(i*zd) for i in expressed]
    p=0
    
    for i in Selected_objects:
        Random_Nx= xv[p]
        Random_Ny= yv[p]
        Random_Nz= zv[p]
        i.select_set(True)
        bpy.context.view_layer.objects.active = i
        bpy.ops.transform.translate(value= (Random_Nx,Random_Ny,Random_Nz ), orient_type=Orient_type_list[o if o==1 or o==0 else 0])
        bpy.ops.object.select_all(action='DESELECT')
        p=p+1
  
    for i in Selected_objects:
        i.select_set(True)
    bpy.context.view_layer.objects.active = Active_object
    

def Ranged_Rotation (xs, xe, ys, ye, zs, ze, os, po):
    
    Selected_objects= bpy.context.selected_objects
    Active_object = bpy.context.view_layer.objects.active
    bpy.ops.object.select_all(action='DESELECT')
    Orient_type_list= ['GLOBAL','LOCAL']
    if os == 1:
        o = 1
    else:
        o = 0
    
    l= len(Selected_objects)
    m = list(np.arange(0,1,1/(l-1)))
    m.append(1)
    expressed = [(lambda x :x**po)(i)  for i in m]
    xd= xe-xs
    yd= ye-ys
    zd= ze-zs
    xv=[xs+(i*xd) for i in expressed]
    yv=[ys+(i*yd) for i in expressed]
    zv=[zs+(i*zd) for i in expressed]
    p=0
    
    
    
    
    for i in Selected_objects:
        Random_Nx= xv[p]
        Random_Ny= yv[p]
        Random_Nz= zv[p]
        i.select_set(True)
        bpy.context.view_layer.objects.active = i
        
        bpy.ops.transform.rotate(value=(pi*Random_Nz/180), orient_axis='Z', orient_type= Orient_type_list[o])
        
        bpy.ops.transform.rotate(value=(pi*Random_Nx/180), orient_axis='X', orient_type= Orient_type_list[o])
        
        bpy.ops.transform.rotate(value=(pi*Random_Ny/180), orient_axis='Y', orient_type= Orient_type_list[o])



        bpy.ops.object.select_all(action='DESELECT')
        p=p+1
        
    for i in Selected_objects:
        i.select_set(True)
    bpy.context.view_layer.objects.active = Active_object
    

def Random_Rotation (xs, xe, ys, ye, zs, ze, os):
    
    Selected_objects= bpy.context.selected_objects
    Active_object = bpy.context.view_layer.objects.active
    bpy.ops.object.select_all(action='DESELECT')
    Orient_type_list= ['GLOBAL','LOCAL']
    if os == 1:
        o = 1
    else:
        o = 0
    
    
    
    for i in Selected_objects:
        Random_Nx= random.uniform(xs, xe)
        Random_Ny= random.uniform(ys, ye)
        Random_Nz= random.uniform(zs, ze)
        i.select_set(True)
        bpy.context.view_layer.objects.active = i
        
        bpy.ops.transform.rotate(value=(pi*Random_Nz/180), orient_axis='Z', orient_type= Orient_type_list[o])
        
        bpy.ops.transform.rotate(value=(pi*Random_Nx/180), orient_axis='X', orient_type= Orient_type_list[o])
        
        bpy.ops.transform.rotate(value=(pi*Random_Ny/180), orient_axis='Y', orient_type= Orient_type_list[o])



        bpy.ops.object.select_all(action='DESELECT')
    for i in Selected_objects:
        i.select_set(True)
    bpy.context.view_layer.objects.active = Active_object
    

def Ranged_Scale (xs, xe, ys, ye, zs, ze, o, po): #o=0):
    
    Selected_objects= bpy.context.selected_objects
    Active_object = bpy.context.view_layer.objects.active
    bpy.ops.object.select_all(action='DESELECT')
    Orient_type_list= ['GLOBAL','LOCAL']

    l= len(Selected_objects)
    m = list(np.arange(0,1,1/(l-1)))
    m.append(1)
    expressed = [(lambda x :x**po)(i)  for i in m]
    xd= xe-xs
    yd= ye-ys
    zd= ze-zs
    xv=[xs+(i*xd) for i in expressed]
    yv=[ys+(i*yd) for i in expressed]
    zv=[zs+(i*zd) for i in expressed]
    p=0
    
    
    
    for i in Selected_objects:
        Random_Nx= xv[p]
        Random_Ny= yv[p]
        Random_Nz= zv[p]
        i.select_set(True)
        bpy.context.view_layer.objects.active = i
        
        bpy.ops.transform.resize(value=(Random_Nx,Random_Ny, Random_Nz), orient_type=Orient_type_list[o if o==1 or o==0 else 0])
        
        p=p+1

        bpy.ops.object.select_all(action='DESELECT')
    
    
    for i in Selected_objects:
        i.select_set(True)
    bpy.context.view_layer.objects.active = Active_object
    
    
    
    
def Random_Scale (xs=0, xe=0, ys=0, ye=0, zs=0, ze=0, o=0): #o=0):
    
    Selected_objects= bpy.context.selected_objects
    Active_object = bpy.context.view_layer.objects.active
    bpy.ops.object.select_all(action='DESELECT')
    Orient_type_list= ['GLOBAL','LOCAL']

    
    
    
    for i in Selected_objects:
        Random_Nx= random.uniform(xs, xe)
        Random_Ny= random.uniform(ys, ye)
        Random_Nz= random.uniform(zs, ze)
        i.select_set(True)
        bpy.context.view_layer.objects.active = i
        
        bpy.ops.transform.resize(value=(Random_Nx,Random_Ny, Random_Nz), orient_type=Orient_type_list[o if o==1 or o==0 else 0])




        bpy.ops.object.select_all(action='DESELECT')
    for i in Selected_objects:
        i.select_set(True)
    bpy.context.view_layer.objects.active = Active_object
    


def Random_Scale_Uniform (xs=0, xe=0): #o=0):
    
    Selected_objects= bpy.context.selected_objects
    Active_object = bpy.context.view_layer.objects.active
    bpy.ops.object.select_all(action='DESELECT')


    
    
    
    for i in Selected_objects:
        Random_Nx= random.uniform(xs, xe)
        i.select_set(True)
        bpy.context.view_layer.objects.active = i
        
        bpy.ops.transform.resize(value=(Random_Nx,Random_Nx, Random_Nx), orient_type='LOCAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='LOCAL')




        bpy.ops.object.select_all(action='DESELECT')
    for i in Selected_objects:
        i.select_set(True)
    bpy.context.view_layer.objects.active = Active_object
    
    
def Ranged_Scale_Uniform (xs, xe, po): #o=0):
    
    Selected_objects= bpy.context.selected_objects
    Active_object = bpy.context.view_layer.objects.active
    bpy.ops.object.select_all(action='DESELECT')

  
    l= len(Selected_objects)
    m = list(np.arange(0,1,1/(l-1)))
    m.append(1)
    expressed = [(lambda x :x**po)(i)  for i in m]
    xd= xe-xs

    xv=[xs+(i*xd) for i in expressed]

    p=0
    
    
    
    for i in Selected_objects:
        Random_Nx= xv[p]
        i.select_set(True)
        bpy.context.view_layer.objects.active = i
        
        bpy.ops.transform.resize(value=(Random_Nx,Random_Nx, Random_Nx), orient_type='LOCAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='LOCAL')




        bpy.ops.object.select_all(action='DESELECT')
    for i in Selected_objects:
        i.select_set(True)
    bpy.context.view_layer.objects.active = Active_object
    


######################################################################################################






def Constant_Input (Value) :
    Selected_objects= bpy.context.selected_objects
    Active_object = bpy.context.view_layer.objects.active
    bpy.ops.object.select_all(action='DESELECT')
    Datapath =bpy.context.window_manager.clipboard
    for i in Selected_objects:
        i.select_set(True)
        bpy.context.view_layer.objects.active = i
        Argument= "bpy.context.object." + str(Datapath)
        try:
            exec("%s = %f" % (Argument,Value))
        except:
            pass
        #bpy.context.object.modifiers["Displace"].strength = 0.7
        bpy.ops.object.select_all(action='DESELECT')
    for i in Selected_objects:
        i.select_set(True)
    bpy.context.view_layer.objects.active = Active_object
    
def Random_Input (start , end) :
    Selected_objects= bpy.context.selected_objects
    Active_object = bpy.context.view_layer.objects.active
    bpy.ops.object.select_all(action='DESELECT')
    Datapath =bpy.context.window_manager.clipboard
    for i in Selected_objects:
        Random_N= random.uniform(start, end)
        i.select_set(True)
        bpy.context.view_layer.objects.active = i
        Argument= "bpy.context.object." + str(Datapath)
        try :
            exec("%s = %f" % (Argument,Random_N))
        except :
            pass
        #bpy.context.object.modifiers["Displace"].strength = 0.7
        bpy.ops.object.select_all(action='DESELECT')
    for i in Selected_objects:
        i.select_set(True)
    bpy.context.view_layer.objects.active = Active_object
        
def Range_Input (start , end, po) :
    Selected_objects= bpy.context.selected_objects
    Active_object = bpy.context.view_layer.objects.active
    bpy.ops.object.select_all(action='DESELECT')
    Datapath =bpy.context.window_manager.clipboard
    l=len(Selected_objects)
    
    m = list(np.arange(0,1,1/(l-1)))
    m.append(1)
    power = po
    expressed = [(lambda x :x**power)(i)  for i in m]
    diff= end-start
    values = [start+(i*diff) for i in expressed]
    
    p=0
    
    for i in Selected_objects:
        N= values[p]
        i.select_set(True)
        bpy.context.view_layer.objects.active = i
        Argument= "bpy.context.object." + str(Datapath)
        try :
            exec("%s = %f" % (Argument,N))
        except :
            pass
        #bpy.context.object.modifiers["Displace"].strength = 0.7
        bpy.ops.object.select_all(action='DESELECT')
        p=p+1
    for i in Selected_objects:
        i.select_set(True)
    bpy.context.view_layer.objects.active = Active_object


############################################################################################################






#Variables
class Variables(bpy.types.PropertyGroup):
    constant : bpy.props.FloatProperty(name="constant",default= 1)
    random_min : bpy.props.FloatProperty(name="min", default=0)
    random_max : bpy.props.FloatProperty(name="max", default=1)
    power : bpy.props.EnumProperty(items=[ ('Linear', "linear", ""), ('Quadratic', "quadratic", ""), ('Cubic', "cubic", "")])    #, name="set color", default='NONE', update=change_color)
    
    
    translate_min : bpy.props.FloatVectorProperty( name="min", subtype="XYZ")
    translate_max : bpy.props.FloatVectorProperty( name="max", subtype="XYZ")
    translate_power : bpy.props.EnumProperty(items=[ ('Linear', "linear", ""), ('Quadratic', "quadratic", ""), ('Cubic', "cubic", "")])
    translate_type : bpy.props.EnumProperty(items=[ ('Global', "global", ""), ('Local', "local", "")], default = 'Global')
    
    rotate_min : bpy.props.FloatVectorProperty( name="min", subtype="XYZ")
    rotate_max : bpy.props.FloatVectorProperty( name="max", subtype="XYZ")
    rotate_power : bpy.props.EnumProperty(items=[ ('Linear', "linear", ""), ('Quadratic', "quadratic", ""), ('Cubic', "cubic", "")])
    rotate_type : bpy.props.EnumProperty(items=[ ('Global', "global", ""), ('Local', "local", "")], default = 'Local')
    
    scale_min : bpy.props.FloatVectorProperty( name="min", subtype="XYZ")
    scale_max : bpy.props.FloatVectorProperty( name="max", subtype="XYZ")
    scale_power : bpy.props.EnumProperty(items=[ ('Linear', "linear", ""), ('Quadratic', "quadratic", ""), ('Cubic', "cubic", "")])
    scale_type :  bpy.props.EnumProperty(items=[ ('Global', "global", ""), ('Local', "local", ""), ('Uniform', "uniform", "")], default = 'Local')
    scale_uni_min: bpy.props.FloatProperty( name="min")
    scale_uni_max: bpy.props.FloatProperty( name="max")
    
    
#############################################################################################################







#operations transformation

class INPUT_OT_transform(bpy.types.Operator):
    bl_label = "transform"
    bl_idname = "input.transform"
    bl_description = "moving objects with random values"
    bl_options = {"REGISTER", "UNDO"}
    
    
    
    def execute(self, context):
        scene = context.scene
        
      #  c = scene.myv.constant
        x_s = scene.myv.translate_min[0]
        y_s = scene.myv.translate_min[1]
        z_s = scene.myv.translate_min[2]
        
        x_e = scene.myv.translate_max[0]
        y_e = scene.myv.translate_max[1]
        z_e = scene.myv.translate_max[2]
        
        o = scene.myv.translate_type
        if o =="Global":
            orient = 0
        else:
            orient = 1
        
        Random_Location(x_s, x_e, y_s, y_e, z_s, z_e, orient)
        return {'FINISHED'}
    
class INPUT_OT_transformranged(bpy.types.Operator):
    bl_label = "transform"
    bl_idname = "input.transformranged"
    bl_description = "moving objects with ranged values"
    bl_options = {"REGISTER", "UNDO"}
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    
    @classmethod
    def poll(cls, context):
        return (len(bpy.context.selected_objects)>1)
        
    
    
    
    def execute(self, context):
        scene = context.scene
        
      #  c = scene.myv.constant
        x_s = scene.myv.translate_min[0]
        y_s = scene.myv.translate_min[1]
        z_s = scene.myv.translate_min[2]
        
        x_e = scene.myv.translate_max[0]
        y_e = scene.myv.translate_max[1]
        z_e = scene.myv.translate_max[2]
        
        p = scene.myv.power
        
        if p == "Linear":
            power=1
        elif p == "Quadratic":
            power=2
        else:
            power=3
            
        o = scene.myv.translate_type
        if o =="Global":
            orient = 0
        else:
            orient = 1
        
        Ranged_Location(x_s, x_e, y_s, y_e, z_s, z_e, orient, power)
        return {'FINISHED'}


class INPUT_OT_rotate(bpy.types.Operator):
    bl_label = "rotate"
    bl_idname = "input.rotate"
    bl_description = "rotating objects with random values"
    bl_options = {"REGISTER", "UNDO"}
    
    
    
    def execute(self, context):
        scene = context.scene
        
      #  c = scene.myv.constant
        x_s = scene.myv.rotate_min[0]
        y_s = scene.myv.rotate_min[1]
        z_s = scene.myv.rotate_min[2]
        
        x_e = scene.myv.rotate_max[0]
        y_e = scene.myv.rotate_max[1]
        z_e = scene.myv.rotate_max[2]
        
        o = scene.myv.rotate_type
        if o =="Global":
            orient = 0
        else:
            orient = 1
        
        
        Random_Rotation(x_s, x_e, y_s, y_e, z_s, z_e,orient)
        return {'FINISHED'}


class INPUT_OT_rotateranged(bpy.types.Operator):
    bl_label = "rotate ranged"
    bl_idname = "input.rotateranged"
    bl_description = "rotating objects with ranged values"
    bl_options = {"REGISTER", "UNDO"}
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    
    @classmethod
    def poll(cls, context):
        return (len(bpy.context.selected_objects)>1)
    
    
    def execute(self, context):
        scene = context.scene
        
      #  c = scene.myv.constant
        x_s = scene.myv.rotate_min[0]
        y_s = scene.myv.rotate_min[1]
        z_s = scene.myv.rotate_min[2]
        
        x_e = scene.myv.rotate_max[0]
        y_e = scene.myv.rotate_max[1]
        z_e = scene.myv.rotate_max[2]
        
        p = scene.myv.rotate_power
        
        if p == "Linear":
            power=1
        elif p == "Quadratic":
            power=2
        else:
            power=3
        
        o = scene.myv.rotate_type
        if o =="Global":
            orient = 0
        else:
            orient = 1
        
        
        Ranged_Rotation(x_s, x_e, y_s, y_e, z_s, z_e,orient,power)
        return {'FINISHED'}



class INPUT_OT_scale(bpy.types.Operator):
    bl_label = "scale"
    bl_idname = "input.scale"
    bl_description = "scaling objects with random values"
    bl_options = {"REGISTER", "UNDO"}
    
    
    
    def execute(self, context):
        scene = context.scene
        
      #  c = scene.myv.constant
        x_s = scene.myv.scale_min[0]
        y_s = scene.myv.scale_min[1]
        z_s = scene.myv.scale_min[2]
        
        x_e = scene.myv.scale_max[0]
        y_e = scene.myv.scale_max[1]
        z_e = scene.myv.scale_max[2]
        
        xus = scene.myv.scale_uni_min
        xue = scene.myv.scale_uni_min
        
        o = scene.myv.scale_type
        if o =="Global":
            orient = 0
        else:
            orient = 1
        
        switch = scene.myv.scale_type
        
        if switch =='Local' or switch =='Global':
            Random_Scale(x_s, x_e, y_s, y_e, z_s, z_e,orient)
            
        else:
            Random_Scale_Uniform(xus, xue)
            #Random_Scale(x_s, x_e, y_s, y_e, z_s, z_e,orient)
        return {'FINISHED'}



class INPUT_OT_scaleranged(bpy.types.Operator):
    bl_label = "ranged scale"
    bl_idname = "input.scaleranged"
    bl_description = "scaling objects with ranged values"
    bl_options = {"REGISTER", "UNDO"}
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    
    @classmethod
    def poll(cls, context):
        return (len(bpy.context.selected_objects)>1)
    
    
    def execute(self, context):
        scene = context.scene
        
      #  c = scene.myv.constant
        x_s = scene.myv.scale_min[0]
        y_s = scene.myv.scale_min[1]
        z_s = scene.myv.scale_min[2]
        
        x_e = scene.myv.scale_max[0]
        y_e = scene.myv.scale_max[1]
        z_e = scene.myv.scale_max[2]
        
        xus = scene.myv.scale_uni_min
        xue = scene.myv.scale_uni_min
        
        p = scene.myv.scale_power
        
        if p == "Linear":
            power=1
        elif p == "Quadratic":
            power=2
        else:
            power=3
        
        o = scene.myv.scale_type
        if o =="Global":
            orient = 0
        else:
            orient = 1
        
        if o =='Local' or o =='Global':
            Ranged_Scale(x_s, x_e, y_s, y_e, z_s, z_e,orient,power)
            #Ranged_Scale_Uniform(xus, xue,power)
            
        else:
            Ranged_Scale_Uniform(xus, xue,power)
            #Ranged_Scale(x_s, x_e, y_s, y_e, z_s, z_e,orient,power)
        return {'FINISHED'}


################################################################################################################
#operations constant

class INPUT_OT_constant(bpy.types.Operator):
    bl_label = "Constant input"
    bl_idname = "input.constant"
    bl_description = "Entering constant values in copied data path"
    bl_options = {"REGISTER", "UNDO"}
    
    
    
    def execute(self, context):
        scene = context.scene
        
      #  c = scene.myv.constant
        c = scene.myv.constant
        
        Constant_Input (c)
        return {'FINISHED'}
    

class INPUT_OT_random(bpy.types.Operator):
    bl_label = "Constant input"
    bl_idname = "input.random"
    bl_description = "Entering random values in copied data path"
    bl_options = {"REGISTER", "UNDO"}
    
    
    
    def execute(self, context):
        scene = context.scene
        
      #  c = scene.myv.constant
        min = scene.myv.random_min
        max = scene.myv.random_max
        
        Random_Input (min,max)
        return {'FINISHED'}

class INPUT_OT_range(bpy.types.Operator):
    bl_label = "Constant input"
    bl_idname = "input.range"
    bl_description = "Entering ranged values in copied data path"
    bl_options = {"REGISTER", "UNDO"}
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    
    @classmethod
    def poll(cls, context):
        return (len(bpy.context.selected_objects)>1)
    
    
    def execute(self, context):
        scene = context.scene
        
      #  c = scene.myv.constant
        min = scene.myv.random_min
        max = scene.myv.random_max
        p = scene.myv.power
        
        if p == "Linear":
            power=1
        elif p == "Quadratic":
            power=2
        else:
            power=3
        
        Range_Input (min,max,power)
        return {'FINISHED'}


###########################################################################################################
#panels
class PANEL_PT_constant(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Multi Input"
    bl_idname = "SCENE_PT_constant"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_catogery= "multi_input"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Constant input
        layout.label(text=" constant input:")

        row = layout.row()
        row.prop(scene.myv, "constant")
        sub = row.row()
        sub.scale_x = 1
        sub.operator("input.constant", text="constant")
        
        layout.label(text=" random or ranged input:")

        row = layout.row()
        row.prop(scene.myv, "random_min")
        row.prop(scene.myv, "random_max")

        row = layout.row()

        row.operator("input.random", text="random")
        row.prop(scene.myv, "power", text= "")
        row.operator("input.range", text="ranged")
        
      #  sub = row.row()
      #  sub.scale_x = 0.5
      
 ##########################################################################################################     
      
class PANEL_PT_transform(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Multi Transform"
    bl_idname = "SCENE_PT_transform"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_catogery= "multi_input"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Constant input
        layout.label(text=" random translate:")

        row = layout.row()
        row.prop(scene.myv, "translate_min")
        
        
        row = layout.row()
        row.prop(scene.myv, "translate_max")
        
        
        row = layout.row()

        row.operator("input.transform", text="random")
        row.prop(scene.myv, "translate_type", text= "")
        row.prop(scene.myv, "translate_power", text= "")
        row.operator("input.transformranged", text="ranged")
        
        layout.label(text=" random rotate:")

        row = layout.row()
        row.prop(scene.myv, "rotate_min")
        row = layout.row()
        row.prop(scene.myv, "rotate_max")

        row = layout.row()

        row.operator("input.rotate", text="random")
        row.prop(scene.myv, "rotate_type", text= "")
        row.prop(scene.myv, "rotate_power", text= "")
        row.operator("input.rotateranged", text="ranged")
        
        
        layout.label(text=" random scale:")
        switch = scene.myv.scale_type
        
        if switch =='Uniform':
            row = layout.row()
            row.prop(scene.myv, "scale_uni_min")
            row.prop(scene.myv, "scale_uni_max")
        
       
        
            row = layout.row()
        
            row.operator("input.scale", text="random")
            row.prop(scene.myv, "scale_type", text= "")
            row.prop(scene.myv, "scale_power", text= "")
            row.operator("input.scaleranged", text="ranged")
            
        else:
            row = layout.row()
            row.prop(scene.myv, "scale_min")
            row = layout.row()
            row.prop(scene.myv, "scale_max")
        
       
        
            row = layout.row()
        
            row.operator("input.scale", text="random")
            row.prop(scene.myv, "scale_type", text= "")
            row.prop(scene.myv, "scale_power", text= "")
            row.operator("input.scaleranged", text="ranged")
         
#############################################################################################################
#register
    

classes = [Variables, INPUT_OT_constant, PANEL_PT_constant, INPUT_OT_random, INPUT_OT_range,PANEL_PT_transform,INPUT_OT_transform, INPUT_OT_transformranged, INPUT_OT_rotate, INPUT_OT_rotateranged, INPUT_OT_scaleranged, INPUT_OT_scale]

def register():
    for i in classes:
        bpy.utils.register_class(i)
    bpy.types.Scene.myv = bpy.props.PointerProperty(type=Variables)
   


def unregister():
    for i in classes:
        bpy.utils.unregister_class(i)
    del bpy.types.Scene.myv


if __name__ == "__main__":
    register()
 
 
