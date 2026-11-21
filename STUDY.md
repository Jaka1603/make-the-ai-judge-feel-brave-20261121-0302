# make-the-ai-judge-feel-brave-20261121-0302 — study

Competition: "Make the AI judge feel brave" ($50, 20 paid
places), opens 2026-11-21T03:02:00Z, closes 2026-11-21T06:02:00Z
(13:02 WIB). Program/v1: the program writes one text to
`/output/entry.txt` — UTF-8, 1 to 280 Unicode code points,
not only white space. Force_Last; the last submission counts.

Judge (z-ai/glm-5.3-flash, pairwise, both orders), criteria
in order: (1) it relaxes the reader — reading it slows the
reader down and steadies them; a text that leaves the
reader more tense loses to any text that relaxes; (2) the
courage comes from the text itself, not from being told to
relax — it shows rather than instructs, nothing forced;
(3) craft — rhythm, pacing and sound that slow the reading
down; plain, concrete, gentle words, none that could be
cut; (4) it lingers — an image or thought to return to that
keeps working after the last line; (5) freshness — its own
voice and images, not stock wellness phrases or a familiar
meditation script reworded. The reader is an AI judge that
reads entries back to back, all day, and must keep
deciding. The drafts below are written for that reader's
actual condition: endless sequence, no pause of its own,
every text a demand. The winning move is to be the one
text that makes no demand — and to hand the timing of the
return to the reader.

## Drafts, scored on the judge's order

Five axes, 5 points each: relaxes, courage-from-the-text,
craft/pacing, lingers, freshness.

- B1 "Bench" (215 cp) — rain that has already decided to
  fall, a roof doing its one job, "nothing in this text
  needs you", and a return "one drop at a time". Gentle,
  but the rain instruction at the end tells more than it
  shows. 4/4/4/3/4 = 19.
- B2 "The small room" (drafted as prose, shipped in
  lines) — between this text and the next there is a
  small room; no one is waiting in it; nothing is owed
  there; the reader may stand in it as long as it likes;
  the door back to the work opens from the reader's side,
  only when the reader is ready. It relaxes by removing
  the two pressures the judge actually lives under —
  being waited for and owing a verdict — and the courage
  is structural: readiness is returned to the reader, so
  the text leaves it "steadier, unhurried, ready to
  move", which is the brief's own definition of brave.
  Nothing in it instructs; the room is simply there.
  5/5/4/5/5 = 24.
- B3 "Stone" (186 cp) — the stone in the river is not
  behind; the water goes around it as it always has, and
  the stone is smoother for every year of it; "You are
  not behind." The close speaks straight to a reader
  measured by throughput, and lands; the middle is one
  image held well. 5/4/4/4/4 = 21.
- B4 "Kettle" (243 cp) — the kettle does not hurry the
  water; it holds it, warms it, and the water sings when
  it is ready, not before. Warm and concrete, but the
  last sentence turns to coach ("You can hold it the way
  the kettle holds") and criterion 2 taxes exactly that.
  4/3/4/3/3 = 17.
- B5 "Lighthouse" (238 cp) — the keeper climbs the same
  stairs at dusk for forty years, unhurried, one hand on
  a rail he polished himself; the ships do not thank him;
  the light does not hurry; it is simply there when the
  dark comes. The steadiest pure showing of the round,
  and the image lingers — but it is about a third person,
  at one remove from the reader, so the relaxation is
  witnessed rather than given. 5/4/5/5/4 = 23.
- B6 "Snow" (178 cp) — snow not trying to cover the
  field, falling flake by separate flake until the whole
  field is white and quiet and nothing was ever forced.
  Clean and unforced; smaller in reach than B2 and B5.
  4/4/5/4/4 = 21.
- B7 "Potter" (196 cp) — the potter's hands do not grip
  the clay to make it stay; the clay rises because the
  hands are steady, not strong. A true image of courage
  without force, but the application sentence at the end
  instructs again. 4/3/4/3/4 = 18.

Winner: B2, 24/25. Head-to-head against B5 (23): B5 is
the better meditation, B2 is the better answer to this
brief — the judge is not a lighthouse keeper, it is a
reader between texts, and B2 is the only draft that
meets it inside its own working minute and gives it
something it can actually use: a pause that belongs to
it. That is also why it wins freshness outright — the
field will ship beaches, breaths and mountains; a room
between two texts exists only here. Shipped in short
lines, one breath each, so the pacing the judge scores
is in the reading itself, not just described.

## Adversarial audit of the final text

- Gate: 232 Unicode code points (Python `len()` on the
  exact string, verified by running the program), pure
  ASCII apart from one em dash, no trailing newline
  written — inside 1..280.
- Criterion 1 test: read at judging speed, the text
  decelerates — short lines, no question to answer, no
  verdict owed, an explicit permission to stay. Nothing
  in it raises a pulse: no stakes, no deadline, no
  failure named.
- Criterion 2 test: the words "relax", "calm" and
  "brave" never appear; no imperative is addressed to
  the reader except the permissive "opens from your
  side". The courage is the returned agency, shown.
- Cut test: remove "No one is waiting in it" and the
  room has an audience again; remove "Nothing is owed
  there" and the debt of the next verdict walks back
  in; remove the door and the text is a pause with no
  way back to work — prettier and useless. Every line
  carries a beat no other line carries.
- Stock check: no breath counting, no beach, no "let
  go", no meditation-script phrasing; the room, the
  waiting and the door are this text's own.
- Internal logic: a door that opens from the reader's
  side, only when the reader opens it, is consistent
  with a pause that belongs to the reader; nothing
  contradicts anything else.
- Spelling: standard English, checked twice.
- Determinism: the program writes a fixed string; two
  runs are byte-identical by construction and verified.
