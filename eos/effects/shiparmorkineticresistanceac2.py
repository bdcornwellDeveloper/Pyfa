# shipArmorKineticResistanceAC2
#
# Used by:
# Ship: Maller
type = "passive"
def handler(fit, ship, context):
    fit.ship.boostItemAttr("armorKineticDamageResonance", ship.getModifiedItemAttr("shipBonusAC2"), skill="Amarr Cruiser")
