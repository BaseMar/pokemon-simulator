# Stałe gry Pokémon Simulator

# --- Parametry drużyny i walki ---
TEAM_SIZE = 3
DEFAULT_LEVEL = 50
MAX_MOVES = 4

# --- STAB ---
STAB_MULTIPLIER = 1.5

# --- Typy mnożników ---
TYPE_MULTIPLIER_LOG = {
    4: "To było super skuteczne! (4x)",
    2: "To było super skuteczne! (2x)",
    1: "Ruch był skuteczny.",
    0.5: "To było mało skuteczne (1/2).",
    0.25: "To było bardzo mało skuteczne (1/4).",
    0: "To nie działa na tego Pokémona!"
}