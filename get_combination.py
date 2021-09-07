def get_combination(items: list):
    if len(items) == 2:
        x = [{"air", "air"}]
        if {items[0],items[1]} in x:
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

        x = ([
            {"volcano", "pressure"},
            {"volcano", "energy"}
        ])
        if {items[0],items[1]} in x:
            return ["eruption", "lava", "obsidian"]
            # "energy"

        x = [{"fire", "air"}]
        if {items[0],items[1]} in x:
            return "smoke"

        x = [{"fire", "water"}]
        if {items[0],items[1]} in x:
            return ["obsidian", "steam"]

        x = [{"fire", "fire"}]
        if {items[0],items[1]} in x:
            return "heat"

        x = [{"sun", "land"}]
        if {items[0],items[1]} in x:
            return "light"

        x = ([
            {"fire", "planet"},
            {"heat", "planet"},
            {"light", "planet"},
            {"energy", "planet"},
            {"fire", "star"},
            {"light", "star"},
            {"energy", "star"},
            {"heat", "star"},
            {"fire", "philosophy"},
            {"light", "philosophy"},
            {"energy", "philosophy"},
            {"heat", "philosophy"}
        ])
        if {items[0],items[1]} in x:
            return "sun"

        x = ([
            {"philosophy", "sun"},
            {"light", "sun"},
            {"sunrise", "time"}
        ])
        if {items[0],items[1]} in x:
            return "day"

        x = [{"sun", "opposite"}]
        if {items[0],items[1]} in x:
            return "moon"

        x = ([
            {"moon", "philosophy"},
            {"moon", "light"},
            {"moonrise", "time"}
        ])
        if {items[0],items[1]} in x:
            return "night"

        x = [{"night", "time"}]
        if {items[0],items[1]} in x:
            return "moonset"

        x = [{"moonset", "time"}]
        if {items[0],items[1]} in x:
            return "moonrise"

        x = [{"day", "time"}]
        if {items[0],items[1]} in x:
            return "sunset"

        x = [{"sunset", "time"}]
        if {items[0],items[1]} in x:
            return "sunrise"

        x = [{"night", "human"}]
        if {items[0],items[1]} in x:
            return "chills"

        x = ([
            {"chills", "time"},
            {"chills", "philosophy"}
        ])
        if {items[0],items[1]} in x:
            return "cold"

        x = [{"cold", "opposite"}]
        if {items[0],items[1]} in x:
            return "hot"

        x = [{"hot", "human"}]
        if {items[0],items[1]} in x:
            return "sweat"
            # No, I'm NOT adding it.

        
        x = [{"earth", "earth"}]
        if {items[0],items[1]} in x:
            return "land"

        x = [{"land", "land"}]
        if {items[0],items[1]} in x:
            return "continent"

        x = [{"continent", "continent"}]
        if {items[0],items[1]} in x:
            return "planet"

        x = [{"sun", "planet"}]
        if {items[0],items[1]} in x:
            return "solar system"

        x = [{"solar system", "solar system"}]
        if {items[0],items[1]} in x:
            return "galaxy"

        x = [{"galaxy", "galaxy"}]
        if {items[0],items[1]} in x:
            return "galplex"

        x = [{"galplex", "galplex"}]
        if {items[0],items[1]} in x:
            return "galaxy cluster"

        x = [{"galaxy cluster", "galaxy cluster"}]
        if {items[0],items[1]} in x:
            return "universe"

        x = [{"universe", "universe"}]
        if {items[0],items[1]} in x:
            return "multiverse"

        x = ([
            {"multiverse", "multiverse"},
            {"zombie", "blade"},
            {"zombie", "death"}
        ])
        if {items[0],items[1]} in x:
            return "dark matter"

        x = [{"earth", "pressure"}]
        if {items[0],items[1]} in x:
            return "stone"

        x = [{"stone", "stone"}]
        if {items[0],items[1]} in x:
            return "wall"

        x = ([
            {"forest", "civilization"},
            {"wall", "wall"},
            {"window", "door"}
        ])
        if {items[0],items[1]} in x:
            return "house"

        x = [{"heat", "stone"}]
        if {items[0],items[1]} in x:
            return "metal"

        x = [{"metal", "air"}]
        if {items[0],items[1]} in x:
            return "rust"

        x = [{"metal", "metal"}]
        if {items[0],items[1]} in x:
            return "blade"

        x = [{"earth", "air"}]
        if {items[0],items[1]} in x:
            return "dust"

        x = [{"dust", "dust"}]
        if {items[0],items[1]} in x:
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

        x = [{"day", "seedling"}]
        if {items[0],items[1]} in x:
            return "plant"

        x = [{"day", "plant"}]
        if {items[0],items[1]} in x:
            return "tree sprout"

        x = [{"tree sprout", "tree sprout"}]
        if {items[0],items[1]} in x:
            return "sapling"

        x = [{"sapling", "sapling"}]
        if {items[0],items[1]} in x:
            return "tree growth"

        x = ([
            {"tree growth", "tree growth"},
            {"seed", "time"},
            {"seed", "big"},
            {"plant", "big"}
        ])
        if {items[0],items[1]} in x:
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

        x = ([
            {"book", "day"},
            {"egg", "chicken"}
        ])
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

        x = [{"water", "water"}]
        if {items[0],items[1]} in x:
            return "puddle"

        x = [{"puddle", "puddle"}]
        if {items[0],items[1]} in x:
            return "pond"

        x = [{"pond", "pond"}]
        if {items[0],items[1]} in x:
            return "lake"

        x = [{"lake", "lake"}]
        if {items[0],items[1]} in x:
            return "sea"

        x = [{"sea", "sea"}]
        if {items[0],items[1]} in x:
            return "ocean"

        x = [{"ocean", "ocean"}]
        if {items[0],items[1]} in x:
            return ["earth's water", "pressure"]

        x = [{"earth's water", "atmosphere"}]
        if {items[0],items[1]} in x:
            return "primordial soup"

        x = ([
            {"energy", "primordial soup"},
            {"philosophy", "primordial soup"}
        ])
        if {items[0],items[1]} in x:
            return "life"


        x = [{"philosophy", "philosophy"}]
        if {items[0],items[1]} in x:
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

        x = [{"blade", "human"}]
        if {items[0],items[1]} in x:
            return ["blood", "death"]


        x = [{"life", "time"}]
        if {items[0],items[1]} in x:
            return ["human", "civilization", "death"]

        x = ([
            {"human", "time"},
            {"death", "philosophy"},
            {"death", "human"}
        ])
        if {items[0],items[1]} in x:
            return ["death", "corpse"]

        x = ([
            {"corpse", "energy"},
            {"corpse", "life"}
        ])
        if {items[0],items[1]} in x:
            return "zombie"

        x = [{"zombie", "human"}]
        if {items[0],items[1]} in x:
            return ["zombie", "zombie", "brain"]

        x = ([
            {"zombie", "philosophy"},
            {"death", "opposite"}
        ])
        if {items[0],items[1]} in x:
            return "undead"

        x = ([
            {"undead", "life"},
            {"undead", "human"},
            {"undead", "philosophy"}
        ])
        if {items[0],items[1]} in x:
            return ["true immortality", "zombie"]

        x = [{"blood", "human"}]
        if {items[0],items[1]} in x:
            return "vampire"

        x = [{"vampire", "human"}]
        if {items[0],items[1]} in x:
            return ["vampire", "vampire", "blood"]
        
        x = ([
            {"big", "small"},
            {"hot", "cold"}
        ])
        if {items[0],items[1]} in x:
            return "opposite"

        x = [{"life", "opposite"}]
        if {items[0],items[1]} in x:
            return "death"

        x = [{"universe", "time"}]
        if {items[0],items[1]} in x:
            return "expansion"

        x = [{"universe", "death"}]
        if {items[0],items[1]} in x:
            return "compression"

        x = [{"expansion", "philosophy"}]
        if {items[0],items[1]} in x:
            return "big"

        x = [{"compression", "philosophy"}]
        if {items[0],items[1]} in x:
            return "small"
    else:
        raise ValueError("A combination must be made out of exactly 2 items")