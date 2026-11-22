# Verification Scenario

Run the prototype checks on the 16 December PoC. Run the full-content checks as later milestones integrate that content.

## PoC — 16 December

1. Start a game with three-slot ground and aerial configurations for both modes. Verify that the prototype uses four produced attacks: three sword attacks and one pistol shot reused across combo roles and aerial configurations.
2. Alternate modes in a combo and deliberately miss a move: verify shared progress and a return to the beginner after a finisher.
3. Jump, attack in the air and land: verify index resets and movement built into attacks.
4. Dodge during an attack, launcher or special: verify immediate interruption, index reset and style loss.
5. Test the launcher using a reused sword animation: verify target projection, index reset and the rules for triggering it during a combo.
6. Fight the functional mob: verify that its attack can damage the player and that it can be defeated. Its type remains to be selected.
7. Build style to S on the resistant test target: verify stagger gain, stun and launching during stun. Drop below S and verify that accumulated stagger is retained.
8. Complete the short mission, report to Emmanuel and receive its reward. Complete and replay the test hunt using the same mob: verify rewards and target resets.
9. Use earned money to purchase the special slot. Configure the special with existing attacks, including a follower already in the normal combo. Verify outside-combat configuration, the 5-second cooldown and its continuation after a dodge.
10. Trigger checkpoints through mission start and the test zone transition. Change player and world state, then die: verify restoration of the saved position, HP, enemies, money, purchases and mission state.

## Later milestones — full content

1. Complete the four main missions across the two connected levels and boss arena; verify the three selected enemy types in their encounters.
2. Verify that entering level 2 grants Rising Slash. Test Ascension's aerial follow and the other launcher variants as they are produced.
3. Test Orbital Shot once integrated: measure its 2-second duration and verify that damage applications reset the target's fall.
4. Check the distinct starting moves and additional moves as their production replaces the prototype reuse.
5. Purchase the fourth ground slot and the required distinct followers. Equip four ground moves, keep three aerial moves and verify optional slot activation, shared ground length and duplicate-follower rejection.
6. Run the saving, shop and combat checks through the complete main route. Test each of the six hunts once its design and implementation are complete.

## Related notes

- [[GameDesignDocument/GDD|GDD index]]
- [[GameDesignDocument/Milestones|Milestone planning]]
- [[GameDesignDocument/Planning/Production-Baseline|Production baseline]]
- [[GameDesignDocument/Gameplay/Controls|Controller inputs]]
- [[GameDesignDocument/Gameplay/Combos|Combos and shared index]]
- [[GameDesignDocument/Gameplay/Save-and-Death|Saving and death]]
- [[GameDesignDocument/Planning/Delivery-Tracking|Delivery tracking]]
