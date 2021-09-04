def get_combination(items: list):
  if len(items) == 2:
    # if items[0] == "air" and items[1] == "air":
      # return "surface"

    # if items[0] == "surface" and items[1] == "surface":
      # return "troposphere"

    # if items[0] == "troposphere" and items[1] == "troposphere":
      # return "stratosphere"

    # if items[0] == "stratosphere" and items[1] == "stratosphere":
      # return "ozone layer"

    # if items[0] == "ozone layer" and items[1] == "ozone layer":
      # return "mesosphere"

    # if items[0] == "mesosphere" and items[1] == "mesosphere":
      # return "thermosphere"

    # if items[0] == "thermosphere" and items[1] == "thermosphere":
      # return "ionosphere"

    # if items[0] == "ionosphere" and items[1] == "ionosphere":
      # return "exosphere"

    # if items[0] == "exosphere" and items[1] == "exosphere":
    if items[0] == "air" and items[1] == "air":
      return "atmosphere"


    if items[0] == "earth" and items[1] == "fire" or items[0] == "fire" and items[1] == "earth":
      return "magma"

    if items[0] == "magma" and items[1] == "air" or items[0] == "air" and items[1] == "magma":
      return ["lava", "smoke"]

    if items[0] == "fire" and items[1] == "air" or items[0] == "air" and items[1] == "fire":
      return "smoke"

    if items[0] == "fire" and items[1] == "water" or items[0] == "water" and items[1] == "fire":
      return ["obsidian", "steam"]

    if (
      items[0] == "fire" and items[1] == "planet"
      or items[0] == "light" and items[1] == "planet"
      or items[0] == "energy" and items[1] == "planet"
      or items[0] == "fire" and items[1] == "star"
      or items[0] == "light" and items[1] == "star"
      or items[0] == "energy" and items[1] == "star"
      or items[0] == "planet" and items[1] == "fire"
      or items[0] == "planet" and items[1] == "light"
      or items[0] == "planet" and items[1] == "energy"
      or items[0] == "star" and items[1] == "fire"
      or items[0] == "star" and items[1] == "light"
      or items[0] == "star" and items[1] == "energy"
      or items[0] == "fire" and items[1] == "philosophy"
      or items[0] == "light" and items[1] == "philosophy"
      or items[0] == "energy" and items[1] == "philosophy"
      or items[0] == "philosophy" and items[1] == "fire"
      or items[0] == "philosophy" and items[1] == "light"
      or items[0] == "philosophy" and items[1] == "energy"
    ):
      return "sun"

    if items[0] == "philosophy" and items[1] == "sun" or items[0] == "sun" and items[1] == "philosophy":
      return "day"

    
    if items[0] == "earth" and items[1] == "earth":
      return "land"

    if (
      items[0] == "land" and items[1] == "ocean"
      or items[0] == "land" and items[1] == "sea"
      or items[0] == "land" and items[1] == "lake"
      or items[0] == "land" and items[1] == "river"
      or items[0] == "ocean" and items[1] == "land"
      or items[0] == "sea" and items[1] == "land"
      or items[0] == "lake" and items[1] == "land"
      or items[0] == "river" and items[1] == "land"
    ):
      return "island"

    if items[0] == "water" and items[1] == "water":
      return "puddle"

    if items[0] == "puddle" and items[1] == "puddle":
      return "pond"

    if items[0] == "pond" and items[1] == "pond":
      return "lake"

    if items[0] == "lake" and items[1] == "lake":
      return "sea"

    if items[0] == "sea" and items[1] == "sea":
      return "ocean"

    if items[0] == "ocean" and items[1] == "ocean":
      return ["earth's water", "pressure"]

    if items[0] == "earth's water" and items[1] == "atmosphere" or items[0] == "atmosphere" and items[1] == "earth's water":
      return "primordial soup"

    if (
      items[0] == "energy" and items[1] == "primordial soup"
      or items[0] == "philosophy" and items[1] == "primordial soup"
      or items[0] == "primordial soup" and items[1] == "energy"
      or items[0] == "primordial soup" and items[1] == "philosophy"
    ):
      return "life"

    
    if items[0] == "philosophy" and items[1] == "philosophy":
      return "idea"
  else:
    raise ValueError("A combination must be made out of exactly 2 items")