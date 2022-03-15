needs_connection = [
    "acceptance",
    "affection",
    "appreciation",
    "belonging",
    "connection",
    "cooperation",
    "communication",
    "closeness",
    "community",
    "companionship",
    "compassion",
    "consideration",
    "inclusion",
    "intimacy",
    "love",
    "mutuality",
    "respect",
    "safety",
    "security",
    "stability",
    "support",
    "to receive empathy",
    "to empathize",
    "to be known",
    "to understand",
    "to be understood",
    "warmth",
]

needs_honesty = [
    "honesty",
    "authenticity",
    "integrity",
    "presence",
    "trust",
]

needs_play = [
    "play",
    "joy",
    "humor",
    "fun",
    "excitement",
    "lightheartedness",
]

needs_peace = [
    "peace",
    "beauty",
    "communion",
    "ease",
    "equality",
    "harmony",
    "inspiration",
    "order",
]

needs_meaning = [
    "awareness",
    "celebration",
    "challenge",
    "clarity",
    "closure",
    "competence",
    "consciousness",
    "contribution",
    "creativity",
    "discovery",
    "efficacy",
    "effectiveness",
    "growth",
    "hope",
    "learning",
    "mourning",
    "participation",
    "purpose",
    "self-expression",
    "stimulation",
    "understanding",
]

needs_autonomy = [
    "choice",
    "freedom",
    "independence",
    "space",
]

needs_physical = [
    "nutrition",
    "sleep",
    "exercise",
    "rest",
    "sexual-expression",
    "safety",
    "touch",
    "water",
    "laughter",
]

needs_all = (
    needs_connection
    + needs_honesty
    + needs_play
    + needs_peace
    + needs_meaning
    + needs_autonomy
    + needs_physical
)

# remove duplicates
needs_all = list(dict.fromkeys(needs_all))
