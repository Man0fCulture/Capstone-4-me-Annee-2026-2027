# Targeting and Camera

The player can manually lock onto an enemy with R1 and switch targets using the directional buttons. A manual target takes priority. Without manual lock-on, the game automatically selects a target for attacks.

Ground and aerial approach moves use this active target. For initial playtests, automatic selection prioritises a nearby enemy in the direction the character faces and keeps that target during a sequence.

Without manual lock-on, the camera follows Natanael and can be rotated freely. With lock-on, it aims at a point between the player and enemy to keep both visible, rotates gradually and moves slightly farther away as their separation increases.

The camera follows height changes during aerial combat. Movement is smoothed. Lock-on distances, target loss, walls and obstacles will be tuned in the test areas.

## Related notes

- [[GameDesignDocument/GDD|GDD index]]
- [[GameDesignDocument/Gameplay/Gameplay|Gameplay]]
- [[GameDesignDocument/Gameplay/Controls|Controller inputs]]
- [[GameDesignDocument/Gameplay/Movement-and-Interaction|Movement and interaction]]
- [[GameDesignDocument/Gameplay/Aerial-Combat|Aerial combat]]
- [[GameDesignDocument/Interface/Interface|User interface]]
