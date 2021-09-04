from get_combination import get_combination

items = ["air", "earth", "fire", "water"]

def show_prompt():
  print(f"Items: {items}")
  first_item = str(input("First item: ")).lower()
  second_item = str(input("Second item: ")).lower()
  
  if not first_item in items:
    return print("You do not have the first item.")
  
  if not second_item in items:
    return print("You do not have the second item.")

  result = get_combination([first_item, second_item])

  if not result:
    return print("Your items fell to the ground. They must not be a valid combination.")
    
  if isinstance(result, str):
    if result in items:
      print(f"That makes {result}. You've already made that item.")
    else:
      items.append(result)
      print(f"That makes {result}. That's a new item!")
  elif isinstance(result, list):
    for i in range(len(result)):
      if result[i] in items:
        print(f"That makes {result[i]}. You've already made that item.")
      else:
        items.append(result[i])
        print(f"That makes {result[i]}. That's a new item!")
  else:
    raise TypeError("Combination did not create a str or list of item(s)")

while True:
  show_prompt()