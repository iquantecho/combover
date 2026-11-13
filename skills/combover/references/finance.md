# Combover Finance

Use this reference when building, revising, reconciling, or reviewing a financial model, budget, forecast, pricing model, or investor calculation.

## Method

1. Preserve the existing model's authoritative structure unless the requested outcome requires a change.
2. Distinguish source inputs, user-approved assumptions, formulas, and derived outputs.
3. Reuse existing assumptions and formulas when they remain valid. Do not retype numbers that should flow from another cell, table, or source.
4. Prefer transparent formulas and native spreadsheet functions over hidden helper systems or custom code.
5. Change the smallest set of assumptions or formulas that produces the requested scenario. Propagate the change through every dependent output.
6. Recalculate and reconcile the figures the user will rely on. Trace changed assumptions through dependent tables, charts, summaries, and requested decks. Fix the source once.
7. Never manufacture precision, savings, valuation support, market inputs, or investor commitments.

Use an approximation when it is suitable for the intended decision. Label estimates and their material limits beside the result. Do not turn an internal forecast into an accounting close, or treat a required accounting close as a rough forecast.

## Checks

Use only the checks relevant to the model: totals, signs, units, periods, cash roll-forward, balance-sheet balance, scenario consistency, runway, margins, or source-to-model reconciliation. Exercise a boundary case when it could change the decision, such as zero revenue or a missing month. Verify formulas and saved outputs using the host's spreadsheet tools. State when recalculation or output inspection was unavailable.

Keep inputs, calculations, periods, and units easy to follow. Apply readable number formats and clear labels, then stop when the model is usable and reconciled. Additional styling needs a presentation requirement or a concrete usability benefit. Do not add a QA workbook or audit framework for a straightforward update.

## Output

Lead with the model or requested figures. State material assumptions and unresolved conflicts next to the affected output. Keep model mechanics out of the user's way unless they asked for them.
