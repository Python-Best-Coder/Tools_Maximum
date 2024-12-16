from typing import Iterable

class Strid:
    def __init__(self,grid):
        self.grid = grid
        self.width = len(self.grid.splitlines()[0])
        self.height = len(self.grid.splitlines())
    
    def grab(self,x,y):
        return self.grid.splitlines()[y][x]

def distance(x:int,to:int):
    if x < to:
        return to - x
    elif x > to:
        return x - to
    else:
        return 0

def count(i,i2):
    p = i
    i2 += 1
    for _ in range(i2 - i):
        yield p 
        p += 1

def chain(i:Iterable):
    for i2 in range(len(i)):
        yield i[i2]

def joint(x: Iterable, x2: Iterable) -> Iterable:
    i = []
    for item in x:
        i.append(item)
    for item in x2:
        i.append(item)
    
    if isinstance(x, str):
        return ''.join(i) 
    elif isinstance(x, list):
        return i  
    elif isinstance(x, tuple):
        return tuple(i) 
    else:
        return i  

def select(x: Iterable, matches: list):
    p = ""
    if len(matches) == len(x):
        for index,item in enumerate(matches):
            matches[index] = int(item)
        for index,item in enumerate(x):
            if matches[index] >= 1:
                p += str(item)
        p = type(x)(p)
        if type(p).__name__ != "str":
            for index,item in enumerate(x[:len(p)]):
                p[index] = type(x[index])(item)
        return p
    else:
        return IndexError("Length of matches not length of x")

def listmap(f,args:list[tuple]):
    r = []
    for item in args:
        r.append(f(*item))
    return r

def find_grid_item(x:Strid,item:str):
    for y in range(x.height):
        for x2 in range(x.width):
            it = x.grab(x2,y)
            if it == item:
                return (x2,y)
    return None

def zip_iterables(iter1: Iterable, iter2: Iterable) -> Iterable:
    min_len = min(len(iter1), len(iter2))
    for i in range(min_len):
        yield (iter1[i], iter2[i])
        
def unique(iterable: Iterable) -> Iterable:
    seen = set()
    for item in iterable:
        if item not in seen:
            yield item
            seen.add(item)

def partition(iterable: Iterable, condition) -> tuple:
    true_part, false_part = [], []
    for item in iterable:
        if condition(item):
            true_part.append(item)
        else:
            false_part.append(item)
    return true_part, false_part

def take_while(iterable: Iterable, condition) -> Iterable:
    for item in iterable:
        if not condition(item):
            break
        yield item

def bounds(x:Strid):
    return f"{x.width}x{x.height}"

def find_all_grid_items(x: Strid, item: str):
    results = []
    for y in range(x.height):
        for x2 in range(x.width):
            if x.grab(x2, y) == item:
                results.append((x2, y))
    return results

def get_neighbors(x: Strid, cx: int, cy: int):
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < x.width and 0 <= ny < x.height:
            neighbors.append((nx, ny, x.grab(nx, ny)))
    return neighbors

def mirror_grid(x: Strid, axis: str = "horizontal"):
    rows = x.grid.splitlines()
    if axis == "horizontal":
        mirrored = [row[::-1] for row in rows]
    elif axis == "vertical":
        mirrored = rows[::-1]
    else:
        raise ValueError("Axis must be 'horizontal' or 'vertical'")
    x.grid = "\n".join(mirrored)


