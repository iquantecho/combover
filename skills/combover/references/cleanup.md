# Combover Cleanup

Use this reference for consolidating or cleaning a collection of tasks, CRM records, documentation, files, notes, or operational records.

## Method

1. Establish the collection and its authoritative sources before changing anything.
2. Map only the relationships that affect safe cleanup: duplicates, references, owners, statuses, dependencies, history, and destinations.
3. Classify before mutating. Keep unique evidence, decisions, completed history, and records that are still operationally relevant.
4. Merge duplicates into the authoritative record. Do not create a new source of truth just to document the cleanup.
5. Remove or archive only when the user authorized that action and the destination or deletion rule is clear.
6. Use native bulk operations when they preserve meaning. Use per-record work only for exceptions that need judgment.
7. Verify writes with counts, spot checks, or readback. Never infer completion from a successful tool call alone when the system supports verification.

## Human-facing records

Write records for people doing the work, not for an AI documenting its process. Use short action titles, brief actionable descriptions, and native fields for status, owner, dates, relationships, and value. Avoid internal IDs, reconciliation narratives, repeated metadata, or permission boilerplate in human-facing cards unless operationally necessary.

## Output

Leave the collection simpler than you found it, with fewer duplicates and no lost unique information. Report only unresolved items that still need a decision.
