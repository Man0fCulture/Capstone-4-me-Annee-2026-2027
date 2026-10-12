# Combos and Shared Index

## Categories and configuration

| Category | Purpose | Configuration |
|---|---|---|
| Beginner | First move of the combo | First slot, replaceable with another beginner |
| Follower | Intermediate move | Middle slots, replaceable with followers |
| Finisher | Last move of the combo | Final slot, replaceable with another finisher |
| Launcher | Launch the target into the air | Dedicated slot, separate from the normal combo |

Each mode starts with beginner → follower → finisher, on the ground and in the air. The fourth ground slot enables beginner → follower → follower → finisher.

Sword and pistol always use the same number of active slots within a configuration. Activating the fourth ground slot activates it for both modes, keeping their finishers at the same index. Using it requires two distinct owned ground followers for each mode.

Ground and aerial configurations are separate. After buying the fourth ground slot, the player can still use three ground moves. Aerial combos remain at three moves in the PoC.

A follower can occupy only one slot within a normal combo. For the PoC, a follower already equipped there may also be selected in the separate special-move configuration. This permission is provisional.

## Shared index

The index identifies the next stage of the combo and is shared by both modes. Switching modes preserves progress through the sequence.

Three-slot example: Swift Slash with the sword → Piercing Shot with the pistol → Heavy Strike with the sword. Players can also complete every stage using the same mode.

| Event | Index behaviour |
|---|---|
| Beginner or follower executed | Advance to the next stage, even if the move misses |
| Finisher completed | Reset to 0, even if it misses |
| Jump | Reset to 0; the aerial combo starts with a beginner |
| Launcher | Reset to 0; the next normal move is a beginner |
| Dodge | Reset to 0 |
| Hit received | Reset to 0 |
| Landing | Reset to 0; the ground combo starts with a beginner |
| Allowed interval between attacks exceeded | Reset to 0 |

At index 0, the next normal attack is the beginner for the selected mode. The combo timeout, when that timer starts, and input buffering will be defined during prototyping.

## Related notes

- [[GameDesignDocument/GDD|GDD index]]
- [[GameDesignDocument/Gameplay/Gameplay|Gameplay]]
- [[GameDesignDocument/Gameplay/Controls|Controller inputs]]
- [[GameDesignDocument/Gameplay/Move-Catalogue|Move catalogue]]
- [[GameDesignDocument/Gameplay/Aerial-Combat|Aerial combat]]
- [[GameDesignDocument/Gameplay/Launchers|Launchers]]
- [[GameDesignDocument/Gameplay/Special-Move|Special move]]
- [[GameDesignDocument/Gameplay/Shop-and-Economy|Shop and economy]]
