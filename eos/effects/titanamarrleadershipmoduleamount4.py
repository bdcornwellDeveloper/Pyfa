# titanAmarrLeadershipModuleAmount4
#
# Used by:
# Ship: Avatar
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.item.group.name == "Gang Coordinator",
                                     "maxGroupActive", ship.getModifiedItemAttr("titanAmarrBonus4"), skill="Amarr Titan")
