from pymol import cmd


def remove_waters():
    cmd.select("water", "resn HOH")
    cmd.delete("water")


remove_waters()
