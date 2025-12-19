---
name: Add Subscriptions & Plans Management
about: Add plans and subscription lifecycle (expiring alerts, plan changes)
---

### Summary

Add Plans and Subscriptions models and endpoints/UI to assign plans to students, support plan changes, and surface expiring subscriptions with alerts.

### Acceptance Criteria

- Add Plan and Subscription models and migrations
- Endpoints to create/assign/change plans for users
- Background job or scheduled check to flag expiring subscriptions
- UI or API endpoint to list expiring subscriptions

### Notes

Keep subscription billing logic simple (monthly/annual) and extensible later.
