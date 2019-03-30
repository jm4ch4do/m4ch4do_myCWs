# ----- Problem: Pete, the baker (5ku)
# ----- URL: https://www.codewars.com/kata/525c65e51bf619685c000059


def cakes(_ing_cake, _ing_all):
    """
    (dict, dict) -> (int)
    :param _ing_cake: dict with ingredients necessary to make one cake
    :param _ing_all: dict with all available ingredients
    :return: int with amount of cakes you can make

    :algorithm:
    For each ingredient(key) in _ing_cake
        .Return 0 IF not in _ing_all or value in _ing_all < value in _ing_cake
        .         ELSE save new_max = value_ing_all/value_ing_cake
                        in max_cakes if not(max_cakes) or max_cakes>new_max

    :examples:
    cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})
    returns 2

    cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000})
    returns 0

    recipe = {'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100, 'cream': 200}
    available = {'flour': 20000, 'oil': 30000, 'cream': 5000, 'milk': 20000, 'sugar': 1700}
    cakes(recipe, available)
    returns 11
    """
    max_cakes = 0
    for ing, amount in _ing_cake.items():
        if _ing_all.get(ing, 0) < amount:
            return 0
        else:
            new_max = int(_ing_all[ing]/amount)
            max_cakes = new_max if (not max_cakes) or (new_max < max_cakes) else max_cakes

    return max_cakes


recipe = {'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100, 'cream': 200}
available = {'flour': 20000, 'oil': 30000, 'cream': 5000, 'milk': 20000, 'sugar': 1700}
result = cakes(recipe, available)

print(result)
