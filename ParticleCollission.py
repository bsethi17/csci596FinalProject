import bpy
import random
import mathutils

# Settings
NUM_PARTICLES = 10
BOX_SIZE = 10  # Box size (length of the cube side)
PARTICLE_RADIUS = 0.2
VELOCITY_SCALE = 2.0  # Scale for random initial velocities

# Particle storage
particles = []

def create_box():
   
    bpy.ops.mesh.primitive_cube_add(size=BOX_SIZE, location=(0, 0, 0))
    box = bpy.context.object
    box.name = "Collision_Box"
    
   
    mat = bpy.data.materials.new(name="BoxMaterial")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Transmission"].default_value = 0.8  # Transparency
    bsdf.inputs["Roughness"].default_value = 0.0
    box.data.materials.append(mat)
    box.hide_select = True

def create_particle(index, position, velocity):
    
    bpy.ops.mesh.primitive_uv_sphere_add(radius=PARTICLE_RADIUS, location=position)
    particle = bpy.context.object
    particle.name = f"Particle_{index}"
    particles.append({
        "object": particle,
        "velocity": velocity
    })

def initialize_particles():
    
    for i in range(NUM_PARTICLES):
        position = (
            random.uniform(-BOX_SIZE / 2 + PARTICLE_RADIUS, BOX_SIZE / 2 - PARTICLE_RADIUS),
            random.uniform(-BOX_SIZE / 2 + PARTICLE_RADIUS, BOX_SIZE / 2 - PARTICLE_RADIUS),
            random.uniform(-BOX_SIZE / 2 + PARTICLE_RADIUS, BOX_SIZE / 2 - PARTICLE_RADIUS)
        )
        velocity = mathutils.Vector((
            random.uniform(-VELOCITY_SCALE, VELOCITY_SCALE),
            random.uniform(-VELOCITY_SCALE, VELOCITY_SCALE),
            random.uniform(-VELOCITY_SCALE, VELOCITY_SCALE)
        ))
        create_particle(i, position, velocity)

def initialize_scene():
  
    create_box()
    initialize_particles()

def update_particles(scene):
 
    for particle in particles:
        obj = particle["object"]
        vel = particle["velocity"]
        obj.location += vel / FRAME_RATE
        
       
        for i in range(3): 
            if obj.location[i] > (BOX_SIZE / 2 - PARTICLE_RADIUS):
                vel[i] *= -1
                obj.location[i] = BOX_SIZE / 2 - PARTICLE_RADIUS  
            elif obj.location[i] < (-BOX_SIZE / 2 + PARTICLE_RADIUS):
                vel[i] *= -1
                obj.location[i] = -BOX_SIZE / 2 + PARTICLE_RADIUS  

def setup_animation():
   
    bpy.app.handlers.frame_change_pre.clear()  
    bpy.app.handlers.frame_change_pre.append(update_particles)

def handle_particle_collisions():
    
    for i, p1 in enumerate(particles):
        for j, p2 in enumerate(particles):
            if i >= j:
                continue  

          
            distance = (p1["object"].location - p2["object"].location).length
            if distance < 2 * PARTICLE_RADIUS:
                delta_pos = p1["object"].location - p2["object"].location
                delta_vel = p1["velocity"] - p2["velocity"]

                
                p1["velocity"] -= (delta_vel.dot(delta_pos) / delta_pos.length_squared) * delta_pos
                p2["velocity"] += (delta_vel.dot(delta_pos) / delta_pos.length_squared) * delta_pos


def update_particles(scene):
    for particle in particles:
        obj = particle["object"]
        vel = particle["velocity"]
        obj.location += vel / FRAME_RATE
        
        
        for i in range(3): 
            if obj.location[i] > (BOX_SIZE / 2 - PARTICLE_RADIUS):
                vel[i] *= -1
                obj.location[i] = BOX_SIZE / 2 - PARTICLE_RADIUS
            elif obj.location[i] < (-BOX_SIZE / 2 + PARTICLE_RADIUS):
                vel[i] *= -1
                obj.location[i] = -BOX_SIZE / 2 + PARTICLE_RADIUS

    handle_particle_collisions()  

# Run the simulation setup
initialize_scene()
