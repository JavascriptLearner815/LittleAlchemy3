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
      return ["eruption", "lava", "obsidian"
      # , "energy"
      ]

    x = [{"fire", "air"}]
    if {items[0],items[1]} in x:
      return "smoke"

    x = [{"fire", "water"}]
    if {items[0],items[1]} in x:
      return ["obsidian", "steam"]

    if items[0] == "fire" and items[1] == "fire":
      return "heat"

    x = [{"sun", "land"}]
    if {items[0],items[1]} in x:
      return "light"

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

    x = [{"philosophy", "sun"}, {"light", "sun"}]
    if {items[0],items[1]} in x:
      return "day"

    
    if items[0] == "earth" and items[1] == "earth":
      return "land"

    if items[0] == "land" and items[1] == "land":
      return "continent"

    if items[0] == "continent" and items[1] == "continent":
      return "planet"

    x = [{"sun", "planet"}]
    if {items[0],items[1]} in x:
      return "solar system"

    if items[0] == "solar system" and items[1] == "solar system":
      return "galaxy"

    if items[0] == "galaxy" and items[1] == "galaxy":
      return "galplex"

    if items[0] == "galplex" and items[1] == "galplex":
      return "galaxy cluster"

    if items[0] == "galaxy cluster" and items[1] == "galaxy cluster":
      return "universe"

    if items[0] == "universe" and items[1] == "universe":
      return "multiverse"

    if items[0] == "multiverse" and items[1] == "multiverse":
      return "dark matter"

    x = [{"earth", "pressure"}]
    if {items[0],items[1]} in x:
      return "stone"

    x = [{"heat", "stone"}]
    if {items[0],items[1]} in x:
      return "metal"

    if items[0] == "metal" and items[1] == "metal":
      return "blade"

    x = [{"earth", "air"}]
    if {items[0],items[1]} in x:
      return "dust"

    if items[0] == "dust" and items[1] == "dust":
      return "dust bunny"

    x = [{"dust bunny", "earth"}]
    if {items[0],items[1]} in x:
      return "pollen"

    x = [{"pollen", "earth"}]
    if {items[0],items[1]} in x:
      return "seed"

    x = [{"day", "seed"}]
    if {items[0],items[1]} in x:
      return "sprout"

    x = [{"day", "sprout"}]
    if {items[0],items[1]} in x:
      return "seedling"

    x = [{"day", "sprout"}]
    if {items[0],items[1]} in x:
      return "plant"

    x = [{"day", "plant"}]
    if {items[0],items[1]} in x:
      return "tree sprout"

    if items[0] == "tree sprout" and items[1] == "tree sprout":
      return "sapling"

    if items[0] == "sapling" and items[1] == "sapling":
      return "tree growth"

    if items[0] == "tree growth" and items[1] == "tree growth":
      return "tree"

    x = [{"blade", "tree"}]
    if {items[0],items[1]} in x:
      return "wood"

    x = [{"wood", "pressure"}]
    if {items[0],items[1]} in x:
      return "paper"

    x = [{"paper", "wood"}]
    if {items[0],items[1]} in x:
      return "book"

    x = [{"book", "day"}, {"egg", "chicken"}]
    if {items[0],items[1]} in x:
      return "philosophy"

    x = [{"tree", "philosophy"}]
    if {items[0],items[1]} in x:
      return "time"


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

    x = [{"idea", "book"}]
    if {items[0],items[1]} in x:
      return ["philosophy", "philosophy"]

    x = [{"life", "philosophy"}]
    if {items[0],items[1]} in x:
      return ["energy", "universe"]

    x = [{"eruption", "philosophy"}]
    if {items[0],items[1]} in x:
      return ["energy", "death"]


    x = [{"life", "time"}]
    if {items[0],items[1]} in x:
      return ["human", "civilization", "death"]

    x = [{"human", "time"}, {"death", "philosophy"}, {"death", "human"}]
    if {items[0],items[1]} in x:
      return ["death", "corpse"]

    x = [{"seed", "time"}]
    if {items[0],items[1]} in x:
      return "tree"
  else:
    raise ValueError("A combination must be made out of exactly 2 items")