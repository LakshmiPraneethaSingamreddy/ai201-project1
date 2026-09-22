# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer
For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
"One of my questions is about a topic only two documents mention, so I expect that one to be hard." 

---

## 2. Every answer names a source
Every answer the system produces names at least one source document.

**Why this target:**
Every retrieved result already includes the source document names from where the chunks are taken from.
---

## 3. The relevance gate stops out-of-corpus questions
When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

**Why this target:**
For the out of context questions, the best distance is always greater than cutoff, so the relevance gate stops the RAG from giving wrong answer, instead it return "I don't have enough information about that"
---

## 4. Right Chunking preserves multi-paragraph answers
For atleast 3 out of 5 questions about the city_guides where answers are present across multiple paragraphs, the system should give an answer that includes all of the required facts. 

**Why this target:**
The city guides documents are longer compared to the campus_life and advice_threads where the answers can be found in a one or two sentences. When the chunks are not the right size, related information can be seperated and the answer might be incomplete.
---

## 5. Answers are given within 10 seconds on local computer 
For all 5 of my 5 test questions, the answer are given with in the 10 seconds of being submitted.

**Why this target:**
The system is fast enough to give answers for the questions about the corpora even when the answers are either present in a single sentence or spread across multiple paragraphs. If we ask out of bound questions, it is still replying within 10 seconds with the answer " I don't have enough information about that".
---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
