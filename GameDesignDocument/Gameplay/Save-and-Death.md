# Saving and Death

A checkpoint records the game state at a particular moment. In the PoC, saves are triggered when changing zones and starting a mission. Final checkpoint locations will be decided later.

The save contains the player's state — position, HP, money, owned moves and slots, configurations — together with the state of the world, enemies, missions and unlocks.

After death, a Game Over screen precedes loading the latest checkpoint. The player and world return to the recorded state. Actions, rewards and purchases made since that checkpoint are also restored to that saved state.

## Related notes

- [[GameDesignDocument/GDD|GDD index]]
- [[GameDesignDocument/Gameplay/Gameplay|Gameplay]]
- [[GameDesignDocument/Gameplay/Dodge-and-Health|Dodge and health]]
- [[GameDesignDocument/Gameplay/Shop-and-Economy|Shop and economy]]
- [[GameDesignDocument/Missions/Missions|Missions]]
- [[GameDesignDocument/PoC-Scope|PoC scope]]
