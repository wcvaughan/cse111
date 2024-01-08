def main():

    pass

def water_column_height(tower_height, tank_height):

    water_column_height = tower_height + (3 * tank_height) / 4

    return water_column_height

def pressure_gain_from_water_height(water_column_height):

    pressure = (998.2 * 9.80665 * water_column_height) / 1000

    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):

    pressure_lost = (-friction_factor * pipe_length * 998.2 * (fluid_velocity ** 2)) / (2000 * pipe_diameter)

    return pressure_lost