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
  else:
    raise ValueError("A combination must be made out of exactly 2 items")