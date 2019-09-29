import random
import time
import math
from tkinter import *


tk = Tk()

seed = random.randint(1,16284)
biome = 1
cx = 0
start = 64
x = 0
wh = 44

def gen_list(num,lent):
    li = []
    for l in range(lent):
        li.append(num)
    return li

def gen_randint(seed,x,a,b):
    random.seed(seed)
    for num in range(1,x):
        random.randint(a,b)
    ret = random.randint(a,b)
    return ret

def gen_cseed(seed,cx):
    ret = gen_randint(seed,cx,-100,100)
    return ret
    
def gen_ter(octv,ampl,freq,strt,cseed,fdifr,adifr,fadf,rock,bl):
    hm=[]
    frq=math.pi/freq
    px=0
    for ot in range(octv):
        px = px+(math.sin((1+gen_randint(cseed,ot,-1*fadf,fadf))*(frq*gen_randint(cseed,ot,-1*fdifr,fdifr))))*(ampl+gen_randint(cseed,ot,-1*adifr,adifr))
    bala = int(px+strt+gen_randint(cseed,1,-1*rock,rock))-bl[255]
    
    for pxl in range(256):
        px=0
        for ot in range(octv):
            px = px+(math.sin((pxl+gen_randint(cseed,ot,-1*fadf,fadf))*(frq*gen_randint(cseed,ot,-1*fdifr,fdifr))))*(ampl+gen_randint(cseed,ot,-1*adifr,adifr))
        hm.append(int(px+strt+gen_randint(cseed,pxl,-1*rock,rock)-bala))
    return hm


c = Canvas(tk, width = 1024, height = 512)
c.pack()
water = c.create_rectangle(1,512-wh,1024,512,outline='#0000ff', fill='#0000ff')
tk.update()

def rend_ter(hm,cx,x,dist):
    il = []
    for itm in range(256):
        it = c.create_rectangle(itm+512-dist,512-hm[itm]-64,itm+513-dist,512, outline='#00ff00')
        il.append(it)
    return il

chunks = []

co = rend_ter(gen_ter(5,1,100,start,gen_cseed(seed,cx+1),5,0,25,0,gen_list(0,256)),cx+1,x,0)
chunks.append(co)
tk.update()
    

def move_ter(event):
    if event.keysym == "a":
        for cnk in chunks:
            chunk = cnk
            for blk in chunk:
                c.move(blk,3,0)
    elif event.keysym == "d":
        for cnk in chunks:
            chunk = cnk
            for blk in chunk:
                c.move(blk,-3,0)
c.bind_all('<KeyPress-a>', move_ter)
c.bind_all('<KeyPress-d>', move_ter)
tk.update()

time.sleep(10)

while 1:
    xm = 0
    fb = co[0]
    cords = c.coords(fb)
    x = cords[0] - 512 - xm*256
    if x + cx*256 <= -256:
        xm = xm + 1
        cx = cx+1
        nc = rend_ter(gen_ter(5,1,100,start,gen_cseed(seed,cx+1),5,0,25,0,gen_list(0,256)),cx+1,x,16)
        chunks.append(nc)
    tk.update()

