from typing import Iterable

class StringGrid:
    """
    Class representing a grid structure. It allows you to access and manipulate 
    elements in a grid using coordinates.
    
    Attributes:
    - grid (str): The grid data in string form, with rows separated by newlines.
    - width (int): The number of columns in the grid.
    - height (int): The number of rows in the grid.
    """
    
    def __init__(self, grid: str):
        """
        Initializes the grid object.
        
        Parameters:
        - grid (str): The grid data in string format.
        """
        self.grid = grid
        self.width = len(self.grid.splitlines()[0])  # Width is determined by the first row
        self.height = len(self.grid.splitlines())    # Height is the number of rows
    
    def grab(self, x: int, y: int) -> str:
        """
        Grabs an element from the grid at the specified (x, y) coordinates.
        
        Parameters:
        - x (int): The column index.
        - y (int): The row index.
        
        Returns:
        - str: The character at the specified location in the grid.
        """
        return self.grid.splitlines()[y][x]

def find_grid_item(x: StringGrid, item: str):
    """
    Finds the coordinates of a specific item (character) in the grid.
    
    Parameters:
    - x (Strid): The grid object containing the grid data.
    - item (str): The character to search for in the grid.
    
    Returns:
    - tuple: The (x, y) coordinates of the found item, or None if not found.
    """
    for y in range(x.height):
        for x2 in range(x.width):
            if x.grab(x2, y) == item:
                return (x2, y)  # Return the coordinates of the found item
    return None  # Return None if the item is not found

def bounds(x: StringGrid) -> str:
    """
    Returns the bounds (width and height) of the grid.
    
    Parameters:
    - x (Strid): The grid object containing the grid data.
    
    Returns:
    - str: A string representing the dimensions of the grid in the format "width x height".
    """
    return f"{x.width}x{x.height}"

def swipe(x: StringGrid, character: str, direction: str, blankness: str = "."):
    """
    Moves a specified character in a direction within a grid, ensuring that it stays
    within bounds. If the move goes out of bounds, returns "OOB".
    
    Parameters:
    - x (Strid): The grid object containing the grid data.
    - character (str): The character to move within the grid.
    - direction (str): The direction to move the character ('left', 'right', 'up', 'down').
    - blankness (str): The character to replace the original position with (default is ".").
    
    Returns:
    - str: The updated grid as a string after the move, or "OOB" if the move is out of bounds.
    """
    # Convert the grid to a list of lists for easier manipulation (strings are immutable)
    rx = [list(row) for row in x.grid.splitlines()]
    
    # Convert the direction to lowercase to handle case insensitivity
    direction = direction.lower()
    
    # Find the current position of the character in the grid
    item = find_grid_item(x, character)
    
    # Extract the width and height from the grid's bounds
    w, h = map(int, bounds(x).split("x"))  # Convert to integers for comparison
    
    # Define the movement directions for left, right, up, down
    directs = {"left": -1, "right": 1, "up": -1, "down": 1}
    
    # Initialize the change in x (dx) and y (dy) coordinates
    dx = dy = 0
    
    # Assign dx or dy based on the direction of movement
    if direction in ["left", "right"]:
        dx = directs[direction]
    else:
        dy = directs[direction]
    
    # Calculate the new position after the move
    new_x = item[0] + dy
    new_y = item[1] + dx
    
    # Check if the new position is out of bounds
    if new_x < 0 or new_x >= h or new_y < 0 or new_y >= w:
        return "OOB"  # Return "OOB" if the position is out of bounds
    
    # Move the character to the new position
    rx[new_x][new_y] = character
    
    # Replace the old position with the blank character
    rx[item[0]][item[1]] = blankness
    
    # Convert the list of lists back to a string grid and return it
    return "\n".join("".join(row) for row in rx)

def chain(i: Iterable):
    """
    Chains the elements of an iterable, yielding each item in turn.
    
    Parameters:
    - i (Iterable): The iterable to iterate over.
    
    Yields:
    - The next item in the iterable.
    """
    for item in i:
        yield item

def joint(x: Iterable, x2: Iterable) -> Iterable:
    """
    Joins two iterables together. Returns a new iterable that combines the two.
    
    Parameters:
    - x (Iterable): The first iterable.
    - x2 (Iterable): The second iterable.
    
    Returns:
    - Iterable: The combined iterable containing all elements of both x and x2.
    """
    i = list(x) + list(x2)  # Concatenate the two iterables
    if isinstance(x, str):
        return ''.join(i)  # If the first iterable is a string, join the result as a string
    elif isinstance(x, list):
        return i  # If the first iterable is a list, return a list
    elif isinstance(x, tuple):
        return tuple(i)  # If the first iterable is a tuple, return a tuple
    else:
        return i  # For other types, return the combined iterable

def select(x: Iterable, matches: list):
    """
    Selects items from the iterable based on a list of matching criteria.
    
    Parameters:
    - x (Iterable): The iterable to filter.
    - matches (list): A list of conditions (as integers) to match against the iterable.
    
    Returns:
    - str: A new iterable with only the items that match the conditions.
    """
    p = ""
    if len(matches) == len(x):
        for index, item in enumerate(matches):
            matches[index] = int(item)
        for index, item in enumerate(x):
            if matches[index] >= 1:
                p += str(item)
        p = type(x)(p)
        if type(p).__name__ != "str":
            for index, item in enumerate(x[:len(p)]):
                p[index] = type(x[index])(item)
        return p
    else:
        return IndexError("Length of matches not length of x")

def listmap(f, args: list[tuple]):
    """
    Applies a function to a list of argument tuples and returns the results.
    
    Parameters:
    - f (function): The function to apply to each argument tuple.
    - args (list): A list of tuples where each tuple is passed as arguments to f.
    
    Returns:
    - list: A list of the results of applying f to each tuple in args.
    """
    r = []
    for item in args:
        r.append(f(*item))  # Apply function to each tuple of arguments
    return r

def zip_iterables(iter1: Iterable, iter2: Iterable) -> Iterable:
    """
    Zips two iterables together, returning a tuple of corresponding elements.
    
    Parameters:
    - iter1 (Iterable): The first iterable.
    - iter2 (Iterable): The second iterable.
    
    Yields:
    - tuple: A tuple of corresponding elements from both iterables.
    """
    min_len = min(len(iter1), len(iter2))
    for i in range(min_len):
        yield (iter1[i], iter2[i])

def unique(iterable: Iterable) -> Iterable:
    """
    Yields only the unique elements from an iterable, removing duplicates.
    
    Parameters:
    - iterable (Iterable): The iterable to filter for unique items.
    
    Yields:
    - The unique items in the iterable.
    """
    seen = set()
    for item in iterable:
        if item not in seen:
            yield item
            seen.add(item)

def partition(iterable: Iterable, condition) -> tuple:
    """
    Partitions the iterable into two parts based on a condition.
    
    Parameters:
    - iterable (Iterable): The iterable to partition.
    - condition (function): A function that returns a boolean value.
    
    Returns:
    - tuple: A tuple containing two lists: one with items that satisfy the condition,
             and one with items that do not.
    """
    true_part, false_part = [], []
    for item in iterable:
        if condition(item):
            true_part.append(item)
        else:
            false_part.append(item)
    return true_part, false_part

def take_while(iterable: Iterable, condition) -> Iterable:
    """
    Yields elements from the iterable as long as they satisfy the condition.
    
    Parameters:
    - iterable (Iterable): The iterable to iterate over.
    - condition (function): A function that returns a boolean value.
    
    Yields:
    - The elements of the iterable that satisfy the condition.
    """
    for item in iterable:
        if not condition(item):
            break  # Stop yielding once the condition is no longer satisfied
        yield item


def make_grid(length:int,width:int,character:str):
    """Makes you a grid made of a character based on the dimensions."""
    return "\n".join([character*width]*length)

def look(x:StringGrid,character:str,lookwhere:str):
    """Uses built-in swipe to look in directions."""
    ch = list(find_grid_item(x,character))

    for letter in lookwhere:
        if letter == "U":
            ch[1] -= 1
        elif letter == "D":
            ch[1] += 1
        elif letter == "L":
            ch[0] -= 1
        elif letter == "R":
            ch[0] += 1
        else:
            raise ValueError("USE UDLR!")
    if ch[0] < 0 or ch[0] > x.width or ch[1] < 0 or ch[1] > x.height:
        return "OOB"
    else:
        return x.grab(ch[0],ch[1])
        
