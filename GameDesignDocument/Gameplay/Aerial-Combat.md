# Aerial Combat

A normal jump gives access to the aerial combo. A launcher that carries the player upwards provides another way to join the target in the air.

During an aerial attack animation, Natanael's fall is suspended: he stays at his current height unless the move includes vertical movement. Falling resumes after the animation.

Every hit against an airborne enemy resets its fall. The enemy starts falling again from its current height; between impacts, it resumes falling. Damage applications from Orbital Shot's trail also reset the target's fall.

Some finishers bring the target to the ground. Their downward movement takes priority over the normal fall reset. Other finishers leave Natanael in the air. All finishers reset the index to 0.

Fall parameters and launch reactions are specific to each enemy and will be tuned during playtests.

## Related notes

- [[GameDesignDocument/GDD|GDD index]]
- [[GameDesignDocument/Gameplay/Gameplay|Gameplay]]
- [[GameDesignDocument/Gameplay/Movement-and-Interaction|Movement and interaction]]
- [[GameDesignDocument/Gameplay/Combos|Combos and shared index]]
- [[GameDesignDocument/Gameplay/Launchers|Launchers]]
- [[GameDesignDocument/Gameplay/Move-Catalogue|Move catalogue]]
- [[GameDesignDocument/Gameplay/Stagger|Stagger]]
