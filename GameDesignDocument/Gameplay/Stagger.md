# Stagger

Each enemy has a stagger gauge. Only successful hits at rank S, SS or SSS fill it.

If the player drops below S, accumulated stagger is retained. Hits stop filling the gauge until the player returns to a sufficient rank.

A full gauge temporarily stuns the enemy: its attack is interrupted and it cannot retaliate. Enemies that normally cannot be launched or strongly resist launching become launchable during this window. Enemies that are already launchable can be launched outside stagger.

During the stun, hits deal damage and grant style according to normal rules, but no longer fill stagger. The gauge returns to 0 when the window ends.

If the target is still airborne when stagger ends, the aerial combo continues. Its normal launch resistance returns when it touches the ground.

Stagger gain, stun duration and resistances will be defined for each enemy.

## Related notes

- [[GameDesignDocument/GDD|GDD index]]
- [[GameDesignDocument/Gameplay/Gameplay|Gameplay]]
- [[GameDesignDocument/Gameplay/Style|Style]]
- [[GameDesignDocument/Enemies/Bestiary|Bestiary]]
- [[GameDesignDocument/Gameplay/Launchers|Launchers]]
- [[GameDesignDocument/Gameplay/Aerial-Combat|Aerial combat]]
