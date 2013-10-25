 # Software License Agreement (BSD License)
 #
 #  Copyright (c) 2013-, Stefano Michieletto
 #
 #  All rights reserved.
 #
 #  Redistribution and use in source and binary forms, with or without
 #  modification, are permitted provided that the following conditions
 #  are met:
 #
 #   # Redistributions of source code must retain the above copyright
 #     notice, this list of conditions and the following disclaimer.
 #   # Redistributions in binary form must reproduce the above
 #     copyright notice, this list of conditions and the following
 #     disclaimer in the documentation and/or other materials provided
 #     with the distribution.
 #   # Neither the name of the copyright holder(s) nor the names of its
 #     contributors may be used to endorse or promote products derived
 #     from this software without specific prior written permission.
 #
 #  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 #  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 #  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 #  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 #  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 #  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 #  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 #  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 #  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 #  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 #  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 #  POSSIBILITY OF SUCH DAMAGE.
 #
 # io_export_separate.py
 # Authors: Davide Zanin [davidezanin@gmail.com]
 #	    Roberto Bortoletto [roberto.bortoletto@dei.unipd.it]
 # 	    Stefano Michieletto [stefano.michieletto@dei.unipd.it]
 #      Séverin Lemaignan [severin.lemaignan@epfl.ch]

import bpy

# Make sure all objects are visible
for o in bpy.data.objects:
    o.hide = False

# Keep a copy of user selection 
bpy.ops.object.select_all(action="SELECT")
sel_obs = bpy.context.selected_objects[:] 

for ob in sel_obs: 
    
    # Skip non-mesh objects 
    if ob.type != 'MESH': 
        continue 

    # Clear selection    
    bpy.ops.object.select_all(action="DESELECT") 
    
    # Select single object 
    ob.select = True 
    
    # Export single object to STL 
    bpy.ops.export_mesh.stl(filepath="toto" + ob.name + ".stl") 
    
# Restore user selection 
for ob in sel_obs: 
    ob.select = True 
bpy.context.scene.objects.active = ob
