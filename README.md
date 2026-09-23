# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size:** for documents having less tha 650 characters - chunk size is the size of document and for documents having more than 650 charcters, the chunk size is the max(average_paragrapgh_length * 4, 400)
**Overlap:** is 100 characters

The documents in the advice_threads and campus_life corpora has a 543 and 317 characters per each document respectively on average. Since in both of these corpora the answer is retrieved from the whole document where the answer is present in one or two sentences. So, to include the complete answer I have considered 650 characters as the size of chunk for the advice_threads and campus_life corpora.

The documents in the city_guides have 2068 characters on average per document, but taking a chunk size that big the answer might get buried. So I want to go for an approach where the chunk itself can answer to some question. I want to split the paragrapghs such that they are associated with the title(What the paragrapgh is about) and at the same time I don't want to split the paragrapgh in middle(where the rest of the part might contain some part of the answer that makes the answer complete)

So, If the length of document is <650(chunk size), I have counted the no.of paragrapghs in that document and then calculated the average length of each paragrapgh. Then I have determined the chunksize by taking the maximum of (average_paragrapgh_length*4, 400) to ensure that the chunksize should be minimum of 400 characters. And also to reduce the missing of context during chunking I have taken overlap of 100 characters.



<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `` — produced by: ``

======================================================================
Chunk 1  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
======================================================================
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

## Straightforward

**Thornby Wells** is the easiest town in the region. It is flat, compact, and
everything is within three minutes of everything else. Parking is free for two
hours anywhere in town and the station is central. The pump room and gardens
are level throughout.

**Marchwood** has a modern tram network with level boarding on all four lines,
running every 8 minutes on weekdays. The city museum and covered market are both
step-free. The distances between districts are the main consideration.

**Chunk 2** — source: `` — produced by: ``
======================================================================
Chunk 2  |  source: guide_corry_vale.md#1  |  produced by: chunker.py::split_documents
======================================================================
## Getting around

Nothing within the valley is walkable from anything else — the villages are two to four miles apart. There is one taxi, based in the largest village, and it must be booked a day ahead. Most visitors drive between villages and walk the footpaths in between.

## Eat and drink

One pub in the largest village serves food seven days a week. A second, in the third village, opens Thursday to Sunday. There is a farm shop at the valley mouth that sells bread, cheese and little else, and it closes at 4pm. Bring supplies; this is not a place with options.

## What to see

The valley itself is the attraction. The footpath network is dense and well marked, and a circuit taking in three of the four villages is about nine miles with 500 metres of ascent. The chapel in the second village is 12th century and always unlocked.

## Where to stay

Perhaps thirty beds in the entire valley, spread across two pubs and a handful of farmhouse rooms. In summer these are booked months ahead. Camping is permitted on two marked fields and nowhere else.

**Chunk 3** — source: `` — produced by: ``
======================================================================
Chunk 3  |  source: guide_givens_mill.md#1  |  produced by: chunker.py::split_documents
======================================================================
## Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.

## What to see

The mill runs tours on the hour from 11 to 3 and the machinery is operating during them, which is loud and much more impressive than a static exhibit. The church has a Saxon doorway. The river walk downstream reaches Brightwater in about three hours.

## Where to stay

Nothing in the village itself. The nearest rooms are in Brightwater, which is close enough that this is not really a problem — most people come for a half day.

## When to go

The mill runs March to November and is closed entirely in winter. Late spring is the best time. Summer Saturdays are busy enough that the car parkbecomes the limiting factor; come on a weekday if you can.

**Chunk 4** — source: `` — produced by: ``
======================================================================
Chunk 4  |  source: guide_marchwood.md#1  |  produced by: chunker.py::split_documents
======================================================================
## Getting around

A tram network of four lines, running every 8 minutes on weekdays and every 15 at weekends, until midnight. A day ticket costs less than two single fares and nobody tells you this at the machine. The centre is walkable but the interesting districts are not adjacent to each other.

## Eat and drink

The best eating is in the Northgate district, a 12-minute tram ride from the station, where about thirty restaurants sit within four streets. The area immediately around the station is uniformly poor and expensive. Marchwood keeps later hours than anywhere else in the region — kitchens serve until 10:30pm, and until midnight on Fridays and Saturdays.

## What to see

The city museum is free and genuinely excellent, particularly the industrial floor. The covered market has operated since 1863 and is at its best on a weekday morning. The canal walk from Northgate to the old lock is 40 minutes and is the thing residents recommend when asked.


**Chunk 5** — source: `` — produced by: ``
======================================================================
Chunk 5  |  source: guide_seasons.md#0  |  produced by: chunker.py::split_documents
======================================================================
# When to visit the region

## Spring, March to May

Days lengthen quickly and businesses that closed for winter reopen through
March and April. By May everything is open and the weather is reliable enough
to plan around. Late May is arguably the best week of the year in Brightwater —
long days, everything running, and the students gone.

The Kestrelford Saturday market builds back to full size through April.

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
     python app.py --corpus advice_threads ask "Is it weird to go to office hours without a specific question?"

**Answer:**

     (best distance 0.390, cutoff 0.6)

     No, it is not weird to go to office hours with no specific question; it is completely normal to say you are following the lectures but do not yet understand the shape of it. 

     Source: `thread_office_hours_etiquette.txt`

     Sources retrieved: thread_commuting.txt, thread_late_work.txt, thread_office_hours_etiquette.txt, thread_professor_email.txt, thread_study_spots.txt

     1 model calls this session, 943 tokens (890 in, 53 out)

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->
     Relevance cutoff I picked - 0.6

| Question                                                        | In corpus? | Best distance |
|-----------------------------------------------------------------|------------|---------------|
| How far in advance should I book to get my adviser hold lifted? |  Yes       | 0.500         |
| How many black-and-white pages does the printing quota cover?   |  Yes       | 0.322         |
| What is there to see in Pellew sands?                           |  Yes       | 0.418         |
|  How late is the library open during term?                      |  Yes       | 0.500         |
| Is it weird to go to office hours without a specific question?  |  Yes       | 0.390         |
| What is the capital of Mongolia?                                |  No        | 0.825         |
| How do I change the oil in a diesel engine?                     |  No        | 0.934         |
| Who won the 1994 World Cup?                                     |  No        | 0.886         |
| What is the recommended dosage of ibuprofen for a headache?     |  No        | 0.844         |
| How do I write a for loop in Rust?                              |  No        | 0.896         |


The gap is from (0.5) t0 (0.8). I have choosen the 0.6 as cutoff because the best_distance to answers for my questions that are in my corpus are ranging from 0.32 to 0.50. And for the out of the scope questions the best_distance is ranging from 0.8 to 0.93. So, I want to keep my cutoff as the 0.6 percent only so that the neither refuses questions it has answers to nor make things up for the questions it doesn't ahve answers for.

I did not change the **GROUNDING_INSTRUCTION** because it is working well and only giving the answers that are pesent in the corpus.
## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**

**2.**

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
