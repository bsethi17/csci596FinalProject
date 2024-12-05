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
    """Create a transparent box to contain particles."""
    bpy.ops.mesh.primitive_cube_add(size=BOX_SIZE, location=(0, 0, 0))
    box = bpy.context.object
    box.name = "Collision_Box"
    
    # Make the box transparent
    mat = bpy.data.materials.new(name="BoxMaterial")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Transmission"].default_value = 0.8  # Transparency
    bsdf.inputs["Roughness"].default_value = 0.0
    box.data.materials.append(mat)
    box.hide_select = True

def create_particle(index, position, velocity):
    """Create a particle at a given position with a random velocity."""
    bpy.ops.mesh.primitive_uv_sphere_add(radius=PARTICLE_RADIUS, location=position)
    particle = bpy.context.object
    particle.name = f"Particle_{index}"
    particles.append({
        "object": particle,
        "velocity": velocity
    })

def initialize_particles():
    """Initialize particles with random positions and velocities."""
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
    """Initialize the scene with a box and particles."""
    create_box()
    initialize_particles()

def update_particles(scene):
    """Update particle positions and handle wall collisions."""
    for particle in particles:
        obj = particle["object"]
        vel = particle["velocity"]
        obj.location += vel / FRAME_RATE
        
        # Wall collision logic
        for i in range(3):  # Check x, y, z axes
            if obj.location[i] > (BOX_SIZE / 2 - PARTICLE_RADIUS):
                vel[i] *= -1
                obj.location[i] = BOX_SIZE / 2 - PARTICLE_RADIUS  # Correct position
            elif obj.location[i] < (-BOX_SIZE / 2 + PARTICLE_RADIUS):
                vel[i] *= -1
                obj.location[i] = -BOX_SIZE / 2 + PARTICLE_RADIUS  # Correct position

def setup_animation():
    """Setup the animation loop in Blender."""
    bpy.app.handlers.frame_change_pre.clear()  # Clear existing handlers
    bpy.app.handlers.frame_change_pre.append(update_particles)

# Run the simulation setup
initialize_scene()
