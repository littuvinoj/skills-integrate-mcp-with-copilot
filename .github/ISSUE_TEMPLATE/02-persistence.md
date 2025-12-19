---
name: Implement Database-backed Persistence and Seeders
about: Replace in-memory activities with a database and add migrations/seeders
---

### Summary

Replace the current in-memory `activities` store with a persistent database (SQLite/Postgres), add migrations and seeders for sample activities, users, roles, and permissions.

### Acceptance Criteria

- Add database models for Activities, Users, Roles, Subscriptions, Payments
- Add migrations and seeders to bootstrap demo data
- Update `src/app.py` to use persistent storage instead of in-memory dicts
- Tests or manual instructions to verify persistence across restarts

### Notes

Start with SQLite for simplicity and provide a config path to switch to Postgres.
