---
name: Add SMS/Notifications & Logging
about: Integrate notification system (SMS/email) and store logs for auditing
---

### Summary

Integrate an SMS/email notification system for events (signup, subscription expiring, payments) and store/send logs for auditing.

### Acceptance Criteria

- Notification sending via pluggable providers (Twilio/SMTP/mock)
- Event hooks for signup, subscription expiry, payment events
- Store sent notifications/logs for auditing and retries

### Notes

Start with a mock provider for dev and document provider configuration for production.
