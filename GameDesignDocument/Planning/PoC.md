# PoC — 16 December 2026

**Objective:** prove the combat → mission → reward → purchase → configuration loop in a small playable prototype. Use blockout environments, temporary feedback and reused animations.

**Attack production budget:** four attacks: one sword beginner, one sword follower, one sword finisher and one pistol shot. The prototype reuses the pistol shot in all three combo roles, with parameter or simple effect changes. Aerial combat reuses these animations; the launcher adds upward knockback to an existing sword attack, and the special chains existing attacks. The broader move catalogue is produced across later milestones.

| Work                       | Expected output                                 | Completion criterion                                                                                                                                                                             | Quantity                                                                                       |
| -------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| Normal combat              | Controller-driven character with both modes     | Switching modes preserves the index; missed moves advance it; jump, finisher, launcher, dodge, received hit, landing and timeout apply the GDD resets; aerial attacks reuse prototype animations | 4 attacks to produce; 3 ground slots and 3 aerial slots for each mode                          |
| Launching and special      | One launcher and a purchasable special          | The launcher projects a target using a reused sword animation; the special is configurable, chains existing attacks and recharges in 5 seconds                                                   | 1 test launcher; ground and aerial special configurations using the 4 existing attacks         |
| Defence, style and stagger | Playable encounter with temporary feedback      | Dodge immediately interrupts attacks and gives approximately 0.17 seconds of invulnerability; it removes one style rank; stagger fills from S and opens resistant targets to launching           | 1 functional mob, type to be selected, with at least 1 attack; 1 passive resistant test target |
| World and mission          | Small blockout test area and a short mission    | Complete a combat objective, report to Emmanuel and receive a reward; a zone transition can be tested                                                                                            | 1 combat area, 1 shop space, 1 test transition and 1 short mission                             |
| Shop and configuration     | Shop and outside-combat menu                    | Mission and repeatable-hunt rewards fund the special-slot purchase; money and ownership update; the special can be configured with owned attacks; configuration is disabled in combat            | 1 Emmanuel shop; 1 purchasable special slot; configuration using existing attacks              |
| Saving and death           | Checkpoints and Game Over screen                | Changing zones or starting a mission records the state; death restores player, world, money, purchases and missions to the saved state                                                           | Saves at the 2 selected event types                                                            |
| Repeatable hunt            | Testable contract loop using the functional mob | Accepting, defeating targets, receiving the reward and restarting the same contract resets the targets                                                                                           | 1 test contract reusing the mob; details of the 6 planned contracts deferred                   |
| Combat readability         | Interface and temporary effects                 | Players see HP, objectives, target and special recharge; style rank appears only when points are non-zero                                                                                        | Minimal interface and test effects                                                             |

**Expected delivery:** a controller-playable PC build, controls, a list of remaining tuning work, screenshots or videos demonstrating key criteria, and a post-mortem.

**Later milestones:** the two complete connected levels, boss arena, four main missions and three planned enemy types are assigned to the alpha route. Production of the twelve distinct starting moves, additional followers, launcher variants and additional finishers is distributed across later milestones. The fourth ground slot will be tested when distinct followers are available. The level-2 launcher unlock will be integrated with the main route. The six hunts remain subject to their deferred design.

**Dependencies and risks:** reused animations must still make attacks readable; aerial sustain, camera framing, the functional mob and saving world state need testing. Engine and production workflow: to define at the start of prototyping.

**Integration and fixes:** last 7 days for integration, fixes and build preparation.

## Related notes

- [[GameDesignDocument/GDD|GDD index]]
- [[GameDesignDocument/Milestones|Milestone planning]]
- [[GameDesignDocument/Planning/Schedule|Delivery schedule]]
- [[GameDesignDocument/Planning/Production-Baseline|Production baseline]]
- [[GameDesignDocument/Planning/Verification|Verification scenario]]
- [[GameDesignDocument/Planning/Delivery-Tracking|Delivery tracking]]
- [[GameDesignDocument/Planning/Alpha|Alpha — 10 February 2027]]
