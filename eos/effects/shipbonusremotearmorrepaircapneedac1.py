# shipBonusRemoteArmorRepairCapNeedAC1
#
# Used by:
# Ship: Augoror
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Armor Repairer",
                                  "capacitorNeed", ship.getModifiedItemAttr("shipBonusAC"), skill="Amarr Cruiser")
