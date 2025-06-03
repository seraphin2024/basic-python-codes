# lucky tarot reader : ) using dictionaries :)
import random 
tarot_cards = {
    1: ("The Fool", "New beginnings, taking a leap of faith, spontaneity."),
    2: ("The Magician", "Manifestation, resourcefulness, power."),
    3: ("The High Priestess", "Intuition, mystery, subconscious mind."),
    4: ("The Empress", "Fertility, nurturing, abundance."),
    5: ("The Emperor", "Stability, structure, authority."),
    6: ("The Hierophant", "Tradition, wisdom, spiritual guidance."),
    7: ("The Lovers", "Love, harmony, relationships."),
    8: ("The Chariot", "Determination, control, victory."),
    9: ("Strength", "Courage, inner strength, compassion."),
    10: ("The Hermit", "Soul-searching, introspection, solitude."),
    11: ("Wheel of Fortune", "Destiny, cycles, turning points."),
    12: ("Justice", "Truth, fairness, law, cause and effect.")
}

card_number = random.randint(1,12)

print("so your reading : ",tarot_cards[card_number])
print("goodluck ! and dont be too harsh on urself .")