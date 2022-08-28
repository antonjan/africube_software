# this module will be imported in the into your flowgraph
#https://www.youtube.com/watch?v=9bhmF7WRvMQ&t=182s
f1 = 430000000
f2 = 440000000
f = f1
step = 12000

def sweeper(probe_lvl):
    if probe_lvl:
       f += step
    if f >= f2:f=f1
    return f
