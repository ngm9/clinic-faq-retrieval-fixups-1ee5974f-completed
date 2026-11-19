## Task Overview

A small medical clinic keeps its internal rules and common questions in a set of local documents. A helper program reads those documents, breaks them into shorter passages, finds the passages that best match a staff member's question, and shows a short block of text with a label for each source. This helps staff trust the answer because they can see exactly which document and section it came from.

Right now the helper is not dependable. Some passages drop a few words where they were split, questions that ask for a specific department still return passages from other departments, the best matches are not always shown first, and the final text block is missing its source labels. Your work is to make the lookup accurate, keep the ordering stable, restore the source labels, and make sure an empty question is handled sensibly.

## Objectives

- Fix the passage splitting so that text near each boundary is preserved and the intended overlap between neighboring passages actually appears, since missing words currently cause good answers to be cut off.
- Ensure that when a question asks for a specific department, only passages from that department are considered, because unrelated departments are leaking into the results today.
- Make the ranking deterministic so the strongest matches appear first and ties are broken consistently, instead of the current unstable order.
- Restore clear source labels on every passage in the assembled text block so readers can tell which document and section each answer came from.
- Handle an empty or missing question by returning a clear, predictable result rather than an error or misleading passages.

## Helpful Tips

- Review how a passage is cut from the raw text and compare the characters at the edges with the original document to spot lost words.
- Consider what happens to neighboring passages when the step between them is larger than intended, and whether any shared text actually remains.
- Analyze how the scores are sorted when two passages score the same, and whether the outcome stays the same every run.
- Explore how a requested department is compared against each passage's own department before scoring begins.
- Think about what the assembled text should include so a reader can trace every line back to its original source.

## How to Verify

- Run the test suite and confirm the previously failing checks now pass.
- Inspect a few returned passages against the source documents to confirm no words are dropped at the edges and that overlap is present.
- Check that a department-filtered question only returns passages belonging to that department.
- Confirm that repeated runs of the same question return results in the same order.
- Observe that the assembled context shows a source label for each passage and that an empty question yields a safe, predictable result.
