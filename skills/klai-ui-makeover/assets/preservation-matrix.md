# Preservation matrix

```json
{
  "_doc": "Makeover contract. status starts pending. moved needs where. gap needs out-of-scope proof or an explicit quoted owner acceptance — not a hypothetical reason. Route/hook/action ids stay. Labels may change. Permissions and data must stay true.",
  "app": "{name as the user said it}",
  "env": "dev-or-isolated-preview",
  "items": [
    {
      "id": "page:{id}",
      "type": "page | field | namedAction | hook | navItem | role | component",
      "job": "what the user accomplishes",
      "presentation_now": "",
      "presentation_after": "",
      "status": "pending",
      "where": "",
      "label_now": "",
      "label_after": "",
      "reason": "",
      "gap_basis": "none | outside_agreed_scope | explicit_acceptance_quoted",
      "acceptance_quote": "",
      "permissions_unchanged": true,
      "data_shape_unchanged": true,
      "ids_unchanged": true
    }
  ]
}
```

Copy this JSON into the run folder as `preservation.json` and update it live. Markdown tables are fine for small apps if every column is present.
