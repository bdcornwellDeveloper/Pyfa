# shipBonusEwRemoteSensorDampenerMaxTargetRangeBonusGC2
#
# Used by:
# Variations of ship: Celestis (3 of 3)
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Sensor Damper",
                                  "maxTargetRangeBonus", ship.getModifiedItemAttr("shipBonusGC2"), skill="Gallente Cruiser")
