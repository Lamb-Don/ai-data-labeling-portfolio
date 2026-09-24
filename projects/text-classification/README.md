# Infrastructure Issue Text Classification

## Objective
Classify public infrastructure issue reports into consistent categories for AI training and analysis.

## Labels
- `pavement_damage`
- `traffic_signal`
- `road_signage`
- `drainage`
- `bridge_structure`
- `other`

## Annotation rules
1. Label the primary issue stated in each report.
2. Do not infer information not included in the text.
3. Use `other` only when no defined label fits.
4. Flag unclear reports for review.

## Quality assurance
- Review ambiguous cases.
- Check label consistency against the guidelines.
- Update definitions when recurring disagreements appear.

## Skills demonstrated
Text annotation, taxonomy design, data quality assurance, technical documentation, and Python-ready dataset preparation.
