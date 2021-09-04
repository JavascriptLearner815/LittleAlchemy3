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

    x = [{"earth", "fire"}]
    if {items[0],items[1]} in x:
      return "magma"

    x = [{"magma", "air"}]
    if {items[0],items[1]} in x:
      return ["lava", "smoke"]

    x = [{"lava", "earth"}]
    if {items[0],items[1]} in x:
      return "volcano"

    x = [{"volcano", "pressure"}, {"volcano", "energy"}]
    if {items[0],items[1]} in x:
      return ["eruption", "energy"]

    x = [{"fire", "air"}]
    if {items[0],items[1]} in x:
      return "smoke"

    x = [{"fire", "water"}]
    if {items[0],items[1]} in x:
      return ["obsidian", "steam"]

    x = ([
      {"fire", "planet"},
      {"light", "planet"},
      {"energy", "planet"},
      {"fire", "star"},
      {"light", "star"},
      {"energy", "star"},
      {"fire", "philosophy"},
      {"light", "philosophy"},
      {"energy", "philosophy"}
    ])
    if {items[0],items[1]} in x:
      return "sun"

    x = [{"philosophy", "sun"}]
    if {items[0],items[1]} in x:
      return "day"

    
    if items[0] == "earth" and items[1] == "earth":
      return "land"

    x = ([
      {"land", "ocean"},
      {"land", "sea"},
      {"land", "lake"},
      {"land", "river"}
    ])
    if {items[0],items[1]} in x:
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

    x = [{"earth's water", "atmosphere"}]
    if {items[0],items[1]} in x:
      return "primordial soup"

    x = [{"energy", "primordial soup"}, {"philosophy", "primordial soup"}]
    if {items[0],items[1]} in x:
      return "life"

  
    if items[0] == "philosophy" and items[1] == "philosophy":
      return "idea"
  else:
    raise ValueError("A combination must be made out of exactly 2 items")