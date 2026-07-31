# Product code survives a concept reset; routing does not

accepted: 2026-07-31
source: review g-37a1 (verdict `obsolete`) — history/2026-07-31-s-review-g-37a1-obsolete-concept-change-001.md
status: current

fact: |
  This direction has now reset its game concept three times, and each reset
  destroyed the ROUTING — the bet, its tasks, lanes, calls and the documents
  written to justify them — while the PRODUCT CODE kept its value untouched.
  At the third reset the surviving asset was measured: 30,326 lines of
  production C# in `Assets/GasCoopGame/**` — a gas simulation on the live tier,
  four gas scenes, the character socket merged to `main`, the FishNet transport
  edge — plus 1,846 green headless tests and 117 negative controls. None of it
  became wrong when the concept changed; only the question of what to build
  NEXT changed.

  The inverse is equally durable: paper written to justify a concept dies WITH
  that concept, in full. The g-37a1 card carried fifteen owner-signed criteria
  and not one of them was closed by product before the node was dropped.

  So a reset is a routing operation, not a demolition. Clearing the bet, its
  tasks, lanes and calls is correct and cheap. Deleting or rewriting working
  code because "the concept changed" is neither, and it is the move that would
  make the next concept start from less than this one did.

read_by: |
  Any `review` closing a bet as `killed` or `obsolete`, before it proposes what
  to drop; and any `frame`/`map` opening a new concept, before it decides what
  the new nodes may assume already exists. Read it first-hand rather than
  inferring the product's state from the dropped node's documents — those
  describe what was planned, not what was built.

END_OF_FILE: live/indie-game-development/knowledge/code-survives-concept-resets.md
