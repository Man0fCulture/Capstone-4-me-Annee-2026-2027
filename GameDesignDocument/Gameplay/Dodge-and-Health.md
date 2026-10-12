# Dodge and Health

Pressing Circle immediately interrupts any attack and starts a dodge. This applies to beginners, followers, finishers, launchers and the special, both on the ground and in the air.

Each dodge resets the combo index to 0 and removes one style rank. It provides 10 invulnerable frames at a reference rate of 60 FPS, approximately 0.167 seconds. This duration stays constant regardless of the display frame rate.

Movement direction and distance, the start of the invulnerability window and falling during an aerial dodge will be specified during prototyping.

The player has a conventional health pool. Enemy attacks reduce HP. At 0 HP, a Game Over screen appears and the game loads the latest checkpoint save.

## Related notes

- [[GameDesignDocument/GDD|GDD index]]
- [[GameDesignDocument/Gameplay/Gameplay|Gameplay]]
- [[GameDesignDocument/Gameplay/Controls|Controller inputs]]
- [[GameDesignDocument/Gameplay/Combos|Combos and shared index]]
- [[GameDesignDocument/Gameplay/Style|Style]]
- [[GameDesignDocument/Gameplay/Save-and-Death|Saving and death]]
