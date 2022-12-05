import turtle
from random import randint as rando
import random
turtle.clearscreen()
turtle.setup(1000,600)

#SKY
#region

#initialize empty list
sky_xy_coords_list = []

#initialize sky turtle
sky = turtle.Turtle()
sky.hideturtle()
sky.shape("turtle")
sky.pensize(50)
sky.speed(0)
sky.pu()
sky.goto(-550,-275)
sky.pd()
sky_xy_coords_list.append(sky.pos())
sky.showturtle()

# referenced code from https://trinket.io/python/00d2c1a8b3

#used photoshop to create sky gradient references
sky_1_colors = ['A0CCEC','AAD2F0','B5D8F3','BEDEF6','C9E4F8','D0E8FA']
sky_2_colors = ['c2b3c7','cab7c7','d2bbc7','dabfc7','e2c2c7','eac6c7']
sky_3_colors = ['d1d1c9','d8d6c8','e0dbc6','e7dfc5','eee4c3','f5e8c1']

def draw_sky():
    #creating random sky choices based off the color palettes
    def sky_1():
        for i in sky_1_colors:
            color = '#' + i
            sky.color(color)
            sky.fd(1100)
            sky_xy_coords_list.append(sky.pos())
            sky.setheading(90)
            sky.fd(50)
            sky_xy_coords_list.append(sky.pos())
            sky.setheading(180)
            sky.fd(1100)
            sky_xy_coords_list.append(sky.pos())
            sky.setheading(90)
            sky.fd(50)
            sky_xy_coords_list.append(sky.pos())
            sky.setheading(0)
    
    def sky_2():
        for i in sky_2_colors:
            color = '#' + i
            sky.color(color)
            sky.fd(1100)
            sky_xy_coords_list.append(sky.pos())
            sky.setheading(90)
            sky.fd(50)
            sky_xy_coords_list.append(sky.pos())
            sky.setheading(180)
            sky.fd(1100)
            sky_xy_coords_list.append(sky.pos())
            sky.setheading(90)
            sky.fd(50)
            sky_xy_coords_list.append(sky.pos())
            sky.setheading(0)

    def sky_3():
        for i in sky_3_colors:
            color = '#' + i
            sky.color(color)
            sky.fd(1100)
            sky_xy_coords_list.append(sky.pos())
            sky.setheading(90)
            sky.fd(50)
            sky_xy_coords_list.append(sky.pos())
            sky.setheading(180)
            sky.fd(1100)
            sky_xy_coords_list.append(sky.pos())
            sky.setheading(90)
            sky.fd(50)
            sky_xy_coords_list.append(sky.pos())
            sky.setheading(0)
    
    sky_options = [sky_1,sky_2,sky_3]
    random.choice(sky_options)()

    sky.hideturtle()

    #collecting x & y coordinate data
    return sky_xy_coords_list

sky_path = draw_sky()

#endregion

#SUN
#region
#initialize empty list
sun_xy_coords_list = []

#initialize sun turtle
sun = turtle.Turtle()
sun.hideturtle()
sun.color(('#F4E68D'))
sun.shape("turtle")
sun.speed(0)

def draw_sun():
  #draw a polygon (code from class lesson)
  def draw_polygon(turtle_obj, side_number, side_length):
    for side in range(side_number):
      turtle_obj.fd(side_length)
      sun_xy_coords_list.append(sun.pos())
      turtle_obj.lt(360/side_number)

  #draw a circle (code from class lesson)
  def draw_circle(turtle_obj, radius):
    from math import pi as pi
    circumference = 2*pi*radius
    sides = int(circumference/3)+3
    length = circumference/sides
    draw_polygon(turtle_obj, sides, length)

  #random sun location in top region of screen
  sun.pu()
  sun.goto(rando(-500,300),rando(150,290))
  sun.pd()
  sun_xy_coords_list.append(sun.pos())
  sun.showturtle()

  sun.begin_fill()
  draw_circle(sun, 10)
  sun_xy_coords_list.append(sun.pos())
  sun.end_fill()

  sun.hideturtle()

  #collecting x & y coordinate data
  return sun_xy_coords_list

sun_path =  draw_sun()

#endregion

#CLOUDS
#region

#initialize empty list
clouds_xy_coords_list = []

#initialize clouds turtle
clouds = turtle.Turtle()
clouds.hideturtle()
clouds.color(('#E6F2F5'))
clouds.shape("turtle")
clouds.speed(0)

#cloud color choices
greys = ['#EBF2F4', '#DFE4E7', '#F8FBFB']

def draw_cloud():

    #randomizing color and cloud position
    clouds.color(greys[rando(0,2)])
    clouds.pu()
    clouds.goto(rando(-510, 510),rando(90,250))
    clouds.pd()
    clouds_xy_coords_list.append(clouds.pos())
    clouds.showturtle()

    #brush strokes making up cloud
    for i in range(rando(15,25)):
        cloud_brush = rando(30,75)
        cloud_len = rando(-50,55)

        clouds.pensize(cloud_brush)
        clouds.setheading(0)
        clouds.fd(cloud_len)
        clouds_xy_coords_list.append(clouds.pos())
        clouds.setheading(90)
        clouds.fd(3)
        clouds_xy_coords_list.append(clouds.pos())

    clouds.setheading(0)
    clouds.fd(cloud_len)
    clouds_xy_coords_list.append(clouds.pos())

#drawing random amount of clouds
def draw_allclouds():
    for i in range(rando(2,3)):
        draw_cloud()

    clouds.hideturtle()

    #collecting x & y coordinate data
    return clouds_xy_coords_list

clouds_path = draw_allclouds()

#endregion

#MOUNTAINS
#region

#initialize empty lists
bg_mts_xy_coords_list = []
mg_mts_xy_coords_list = []
fg_mts_xy_coords_list = []

#initialize dictionary to receive data for multiple mountains
mts_dict = {
      'bg_mts_xy_coords': '',
      'mg_mts_xy_coords' : '',
      'fg_mts_xy_coords': '',
      }

#initialize mts turtle (mts = mountains)
mts = turtle.Turtle()
mts.hideturtle()
mts.shape("turtle")
mts.speed(0)
mts.color(('#E6E2E1'))

# referenced code from https://trinket.io/python/00d2c1a8b3

def draw_bg_mts():

    mts.color(('#F4EDE8'))
    mts.pu()
    mts.goto((500),rando(100,130))
    mts.pd()
    bg_mts_xy_coords_list.append(mts.pos())
    mts.showturtle()
    mts.begin_fill()

    for i in range(5):
      #creating random lengths and angles for every action so mts are different every time
        mt_len = (rando(95,175))
        mt_ang = (rando(145,160))

        mts.setheading(mt_ang)
        mts.fd(mt_len)
        bg_mts_xy_coords_list.append(mts.pos())
        mts.setheading(-mt_ang)
        mts.fd(mt_len*1.2)
        bg_mts_xy_coords_list.append(mts.pos())

    #completing color fill
    mts.goto(-500,-300)
    bg_mts_xy_coords_list.append(mts.pos())
    mts.goto(500,-300)
    bg_mts_xy_coords_list.append(mts.pos())
    mts.end_fill()

    mts.hideturtle()

    #collecting x & y coordinate data
    return bg_mts_xy_coords_list  

def draw_mg_mts():

    mts.color(('#E1DBD5'))
    mts.pu()
    mts.goto((-500),rando(70,90))
    mts.pd()
    mg_mts_xy_coords_list.append(mts.pos())
    mts.showturtle()
    mts.begin_fill()

    #repeating from bg_mts but adjusting values to draw more mts
    for i in range(8):
        mt_len = (rando(50,175))
        mt_ang = (rando(30,70))

        mts.setheading(mt_ang)
        mts.fd(mt_len)
        mg_mts_xy_coords_list.append(mts.pos())
        mts.setheading(-mt_ang)
        mts.fd(mt_len*1.3)
        mg_mts_xy_coords_list.append(mts.pos())

    #completing color fill
    mts.goto(500,-300)
    mg_mts_xy_coords_list.append(mts.pos())
    mts.goto(-500,-300)
    mg_mts_xy_coords_list.append(mts.pos())
    mts.end_fill()

    mts.hideturtle()

    #collecting x & y coordinate data
    return mg_mts_xy_coords_list

def draw_fg_mts():

    mts.color(('#BFB1AF'))
    mts.pu()
    mts.goto((500),rando(15,40))
    mts.pd()
    fg_mts_xy_coords_list.append(mts.pos())
    mts.showturtle()
    mts.begin_fill()

    #repeating from bg_mts but adjusting values to draw the most mts
    for i in range(12):
        mt_len = (rando(25,150))
        mt_ang = (rando(105,140))

        mts.setheading(mt_ang)
        mts.fd(mt_len)
        fg_mts_xy_coords_list.append(mts.pos())
        mts.setheading(-mt_ang)
        mts.fd(mt_len*1.2)
        fg_mts_xy_coords_list.append(mts.pos())

    #completing color fill
    mts.goto(-500,-300)
    fg_mts_xy_coords_list.append(mts.pos())
    mts.goto(500,-300)
    fg_mts_xy_coords_list.append(mts.pos())
    mts.end_fill()

    mts.hideturtle()

    #collecting x & y coordinate data
    return fg_mts_xy_coords_list  


#populate mts dictionary for data collection
mts_dict['bg_mts_xy_coords'] = bg_mts_xy_coords_list
mts_dict['mg_mts_xy_coords'] = mg_mts_xy_coords_list
mts_dict['fg_mts_xy_coords'] = fg_mts_xy_coords_list

#creating tuples based off the mts functions
bg_mts = draw_bg_mts()
mg_mts = draw_mg_mts()
fg_mts = draw_fg_mts()

#combining tuples for data collection
mts_path = bg_mts + mg_mts + fg_mts

#printing data
print(mts_dict)

#endregion

#LAND
#region

#initialize empty lists
land_xy_coords_before_trail_list = []
land_xy_coords_after_trail_list = []

#initialize dictionary to receive data
land_dict = {
      'before_trail_xy_coords': '',
      'land_trail_xy_coords' : '',
      'after_trail_xy_coords': '',
      }

#land color choices
land_colors = ['#5B8C66', '#497D6E', '#6A9C6B']

#initialize land turtle
land = turtle.Turtle()
land.hideturtle()
land.shape("turtle")
land.speed(0)
land.color(land_colors[rando(0,2)])


def draw_land():

  #random left edge starting location
  land.pu()
  land.goto(-500,rando(-140,-100))
  land.pd()
  land_xy_coords_before_trail_list.append(land.pos())
  land.showturtle()

  #generate "ant trail" (manipulated code from class lesson)
  def ant_trail(turtle_obj, cycles):
    
    #initialize empty lists
    x_steps_list = []
    y_steps_list = []
    land_trail_xy_coords_list = []

    #create list of step numbers for x and y directions
    for i in range(cycles):
      x_step = rando(0,70)
      y_step = rando(-1,1)
      x_steps_list.append(x_step)
      y_steps_list.append(y_step)

    #iterate over step list
    for j in range(cycles):    
      #set random x direction
      start_direction = rando(-15,15)

      #set and test for random y direction
      turtle_obj.setheading(start_direction)

      #test to determine up or down
      turtle_obj.fd(x_steps_list[j])

      turtle_obj.setheading(y_steps_list[j])

      #put data in list
      land_trail_xy_coords_list.append(turtle_obj.pos()) #gets a tuple of x,y coordinates
    
    #collecting only x & y coordinate data
    return land_trail_xy_coords_list  

#creating land fill
  land.begin_fill()
  land_trail = ant_trail(land, 40)
  land.goto(500,-300)
  land_xy_coords_after_trail_list.append(land.pos())
  land.goto(-500,-300)
  land_xy_coords_after_trail_list.append(land.pos())
  land.end_fill()

  land.hideturtle()

  #populate land dictionary for data collection
  land_dict['before_trail_xy_coords'] = land_xy_coords_before_trail_list
  land_dict['land_trail_xy_coords'] = land_trail
  land_dict['after_trail_xy_coords'] = land_xy_coords_after_trail_list

  #collecting all land x & y coordinate data
  return land_dict  

land_path = draw_land()

#endregion

#WATER
#region

#initialize empty lists
water_xy_coords_before_trail_list = []
water_xy_coords_after_trail_list = []

#initialize dictionary to receive data
water_dict = {
      'before_trail_xy_coords': '',
      'water_trail_1_xy_coords' : '',
      'water_trail_2_xy_coords' : '',
      'water_trail_3_xy_coords' : '',
      'after_trail_xy_coords': '',
      }

#water color choices
water_colors = ['#79D7EE', '#3F85C5', '#2750BC']

#initialize water turtle
water = turtle.Turtle()
water.hideturtle()
water.shape("turtle")
water.speed(0)
water.color(water_colors[rando(0,2)])

def draw_water():

  #random starting location
  water.pu()
  water.goto(rando(-400,200), rando(-200,-150))
  water.pd()
  water_xy_coords_before_trail_list.append(water.pos())
  water.showturtle()

  #generate "ant trails" (manipulated code from class lesson)
  def ant_trail_1(turtle_obj, cycles):

    #initialize empty lists
    x_steps_list = []
    y_steps_list = []
    water_trail_1_xy_coords_list = []

    #create list of step numbers for x and y directions
    for i in range(cycles):
      x_step = rando(0,50)
      y_step = rando(-2,2)
      x_steps_list.append(x_step)
      y_steps_list.append(y_step)

    #iterate over step list
    for j in range(cycles):    
      #set random x direction
      start_direction = rando(-40,10)

      #set and test for random y direction
      turtle_obj.setheading(start_direction)

      #test to determine up or down
      turtle_obj.fd(x_steps_list[j])

      turtle_obj.setheading(y_steps_list[j])

      #put data in list
      water_trail_1_xy_coords_list.append(turtle_obj.pos()) #gets a tuple of x,y coordinates

    #collecting only x & y coordinate data
    return water_trail_1_xy_coords_list

  def ant_trail_2(turtle_obj, cycles):

    #initialize empty lists
    x_steps_list = []
    y_steps_list = []
    water_trail_2_xy_coords_list = []

    #create list of step numbers for x and y directions
    for i in range(cycles):
      x_step = rando(-40,0)
      y_step = rando(-2,2)
      x_steps_list.append(x_step)
      y_steps_list.append(y_step)

    #iterate over step list
    for j in range(cycles):    
      #set random x direction
      start_direction = rando(-20,10)

      #set and test for random y direction
      turtle_obj.setheading(start_direction)

      #test to determine up or down
      turtle_obj.fd(x_steps_list[j])

      turtle_obj.setheading(y_steps_list[j])

      #put data in list
      water_trail_2_xy_coords_list.append(turtle_obj.pos()) #gets a tuple of x,y coordinates
    
    #collecting only x & y coordinate data
    return water_trail_2_xy_coords_list  

  def ant_trail_3(turtle_obj, cycles):
    
    #initialize empty lists
    x_steps_list = []
    y_steps_list = []
    water_trail_3_xy_coords_list = []

    #create list of step numbers for x and y directions
    for i in range(cycles):
      x_step = rando(-25,0)
      y_step = rando(-10,40)
      x_steps_list.append(x_step)
      y_steps_list.append(y_step)


    #iterate over step list
    for j in range(cycles):    
      #set random x direction
      start_direction = rando(-70,15)

      #set and test for random y direction
      turtle_obj.setheading(start_direction)

      #test to determine up or down
      turtle_obj.fd(x_steps_list[j])

      turtle_obj.setheading(y_steps_list[j])

      #put data in list
      water_trail_3_xy_coords_list.append(turtle_obj.pos()) #gets a tuple of x,y coordinates
    
    #collecting only x & y coordinate data
    return water_trail_3_xy_coords_list

  #creating water fill
  water.begin_fill()
  water_trail_1 = ant_trail_1(water, 20)
  water.setheading(-45)
  water.fd(7)
  water_xy_coords_after_trail_list.append(water.pos())
  water.setheading(180)
  water_trail_2 = ant_trail_2(water, 20)
  water.setheading(90)
  water_trail_3 = ant_trail_3(water, 15)
  water.end_fill()

  water.hideturtle()

  #populate water dictionary for data collection
  water_dict['before_trail_xy_coords'] = water_xy_coords_before_trail_list
  water_dict['water_trail_1_xy_coords'] = water_trail_1
  water_dict['water_trail_2_xy_coords'] = water_trail_2
  water_dict['water_trail_3_xy_coords'] = water_trail_3
  water_dict['after_trail_xy_coords'] = water_xy_coords_after_trail_list

  #collecting all water x & y coordinate data
  return water_dict  

water_path = draw_water()

#endregion

#GRASS
#region

#initialize empty list
grass_xy_coords_list = []

#initialize grass turtle
grass = turtle.Turtle()
grass.hideturtle()
grass.shape("turtle")
grass.pensize(2)
grass.speed(0)

# referenced code from https://trinket.io/python/00d2c1a8b3

#grass color choices
grass_colors = ['#52B078', '#45824C', '#69945D']

def draw_grass():

    #creating random lengths for every blade of grass so every piece of grass is different every time
    blade_len_1 = rando(10,25)
    blade_len_2 = rando(10,25)
    blade_len_3 = rando(10,25)

    #randomizing color and grass position
    grass.color(grass_colors[rando(0,2)])
    grass.pu()
    grass.goto(rando(-500,500),rando(-300,-160))
    grass.pd()
    grass_xy_coords_list.append(grass.pos())
    grass.showturtle()

    #strokes making up every piece of grass
    grass.setheading(130)
    grass.begin_fill()
    grass.fd(blade_len_1)
    grass_xy_coords_list.append(grass.pos())
    grass.setheading(-40)
    grass.fd(blade_len_1*0.8)
    grass_xy_coords_list.append(grass.pos())
    grass.setheading(85)
    grass.fd(blade_len_2)
    grass_xy_coords_list.append(grass.pos())
    grass.setheading(-85)
    grass.fd(blade_len_2)
    grass_xy_coords_list.append(grass.pos())
    grass.setheading(40)
    grass.fd(blade_len_3*0.8)
    grass_xy_coords_list.append(grass.pos())
    grass.setheading(-130)
    grass.fd(blade_len_3)
    grass_xy_coords_list.append(grass.pos())
    
    grass.end_fill()
    grass.hideturtle()

#drawing random amount of grass
def draw_allgrass():
    for i in range(rando(25,50)):
        draw_grass()

    grass.hideturtle()

    #collecting x & y coordinate data
    return grass_xy_coords_list

grass_path = draw_allgrass()

#endregion

#TREES
#region

#initialize empty list
trees_xy_coords_list = []

#initialize trees turtle
trees = turtle.Turtle()
trees.hideturtle()
trees.shape("turtle")
trees.speed(0)

# referenced code from https://trinket.io/python/00d2c1a8b3

#tree leaves and trunk color choices
greens = ['#4F644E', '#385949', '#2B554F', '#4A774E', '#37723D']
browns = ['#4F3F3F', '#5D3F33', '#5F544F']

def draw_tree():

    #creating random tree leaves choices for variety
    def tree_leaves_1():
        temppos = trees.pos()
        trees.color(greens[rando(0,4)])
        trees.pensize(2)

        #bottom right fill
        trees.setheading(90)
        trees.begin_fill()
        trees.fd(50)
        trees_xy_coords_list.append(trees.pos())
        trees.rt(150)
        trees.fd(70)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(180)
        trees.fd(35)
        trees_xy_coords_list.append(trees.pos())
        trees.end_fill()

        #bottom left fill
        trees.setheading(90)
        trees.goto(temppos)
        trees_xy_coords_list.append(trees.pos())
        trees.begin_fill()
        trees.fd(50)
        trees_xy_coords_list.append(trees.pos())
        trees.lt(150)
        trees.fd(70)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(0)
        trees.fd(35)
        trees_xy_coords_list.append(trees.pos())
        trees.end_fill()

        #mid right fill
        trees.setheading(90)
        trees.goto(temppos)
        trees_xy_coords_list.append(trees.pos())
        trees.begin_fill()
        trees.fd(70)
        trees_xy_coords_list.append(trees.pos())
        trees.rt(150)
        trees.fd(60)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(180)
        trees.fd(30)
        trees_xy_coords_list.append(trees.pos())
        trees.end_fill()

        #mid left fill
        trees.setheading(90)
        trees.goto(temppos)
        trees_xy_coords_list.append(trees.pos())
        trees.begin_fill()
        trees.fd(70)
        trees_xy_coords_list.append(trees.pos())
        trees.lt(150)
        trees.fd(60)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(0)
        trees.fd(30)
        trees_xy_coords_list.append(trees.pos())
        trees.end_fill()

        #top right fill
        trees.setheading(90)
        trees.goto(temppos)
        trees_xy_coords_list.append(trees.pos())
        trees.begin_fill()
        trees.fd(90)
        trees_xy_coords_list.append(trees.pos())
        trees.rt(150)
        trees.fd(50)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(180)
        trees.fd(25)
        trees_xy_coords_list.append(trees.pos())
        trees.end_fill()

        #top left fill
        trees.setheading(90)
        trees.goto(temppos)
        trees_xy_coords_list.append(trees.pos())
        trees.begin_fill()
        trees.fd(90)
        trees_xy_coords_list.append(trees.pos())
        trees.lt(150)
        trees.fd(50)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(0)
        trees.fd(25)
        trees_xy_coords_list.append(trees.pos())
        trees.end_fill()
    
    def tree_leaves_2():
        temppos = trees.pos()
        trees.color(greens[rando(0,4)])
        trees.pensize(2)

        #bottom right fill
        trees.setheading(90)
        trees.begin_fill()
        trees.fd(50)
        trees_xy_coords_list.append(trees.pos())
        trees.rt(165)
        trees.fd(70)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(180)
        trees.fd(20)
        trees_xy_coords_list.append(trees.pos())
        trees.end_fill()

        #bottom left fill
        trees.setheading(90)
        trees.goto(temppos)
        trees_xy_coords_list.append(trees.pos())
        trees.begin_fill()
        trees.fd(50)
        trees_xy_coords_list.append(trees.pos())
        trees.lt(165)
        trees.fd(70)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(0)
        trees.fd(20)
        trees_xy_coords_list.append(trees.pos())
        trees.end_fill()

        #mid right fill
        trees.setheading(90)
        trees.goto(temppos)
        trees_xy_coords_list.append(trees.pos())
        trees.begin_fill()
        trees.fd(70)
        trees_xy_coords_list.append(trees.pos())
        trees.rt(165)
        trees.fd(60)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(180)
        trees.fd(15)
        trees_xy_coords_list.append(trees.pos())
        trees.end_fill()

        #mid left fill
        trees.setheading(90)
        trees.goto(temppos)
        trees_xy_coords_list.append(trees.pos())
        trees.begin_fill()
        trees.fd(70)
        trees_xy_coords_list.append(trees.pos())
        trees.lt(165)
        trees.fd(60)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(0)
        trees.fd(15)
        trees_xy_coords_list.append(trees.pos())
        trees.end_fill()

    def tree_leaves_3():
        temppos = trees.pos()
        trees.color(greens[rando(0,4)])
        trees.pensize(5)

        #diamond shape fill
        trees.setheading(60)
        trees.begin_fill()
        trees.fd(50)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(120)
        trees.fd(50)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(240)
        trees.fd(50)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(300)
        trees.fd(50)
        trees_xy_coords_list.append(trees.pos())
        trees.end_fill()

        trees.setheading(90)
        trees.begin_fill()
        trees.fd(25)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(60)
        trees.fd(45)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(120)
        trees.fd(45)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(240)
        trees.fd(45)
        trees_xy_coords_list.append(trees.pos())
        trees.setheading(300)
        trees.fd(45)
        trees_xy_coords_list.append(trees.pos())
        trees.end_fill()

    #tree trunks
    trees.color(browns[rando(0,2)])
    trees.pensize(rando(5,10))
    trees.pu()
    trees.goto(rando(-500,500),rando(-300,-160))
    trees.pd()
    trees_xy_coords_list.append(trees.pos())
    trees.showturtle()
    trees.setheading(90)
    trees.fd(rando(20,50))
    trees_xy_coords_list.append(trees.pos())

    #creating random tree leaves choices
    tree_leaves = [tree_leaves_1, tree_leaves_2, tree_leaves_3]
    random.choice(tree_leaves)()

#drawing random amount of trees
def draw_alltrees():
    for i in range(rando(25,40)):
        draw_tree()

    trees.hideturtle()

    #collecting x & y coordinate data
    return trees_xy_coords_list

trees_path = draw_alltrees()

#endregion


#save all x & y coordinate data in a dictionary
draw_dict = {
    'turtle_sky': sky_path,
    'turtle_sun': sun_path,
    'turtle_clouds': clouds_path,
    'turtle_mts': mts_path,
    'turtle_land': land_path,
    'turtle_water': water_path,
    'turtle_grass': grass_path,
    'turtle_trees': trees_path,
}


#save as PNG
#region
# ref: https://stackoverflow.com/questions/9886274/how-can-i-convert-canvas-content-to-an-image

from PIL import Image

def save_as_png(fileName):
  # save postscipt image 
  turtle.getcanvas().postscript(file = fileName + '.eps') 
  # use PIL to convert to PNG 
  img = Image.open(fileName + '.eps')
  img.load(scale=4)
  img.save(fileName + '.png', 'png')

save_as_png('Landscape_10')

#endregion


#output data from dictionary
for category, data in draw_dict.items():
  print(f'category: {category} | data: {data}')

#save dictionary data as json file
import json
with open("LandscapePath_10.json", 'w') as json_obj:
  json.dump(draw_dict, json_obj, indent=2)
print('file written')