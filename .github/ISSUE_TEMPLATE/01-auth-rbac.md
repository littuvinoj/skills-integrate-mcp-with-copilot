---
name: Add Authentication + Role-Based Access Control
about: Add user authentication with roles and permissions, seeders, and route protection
---

### Summary

Add user authentication (login/logout) and Role-Based Access Control (RBAC) so admins and staff can manage activities, members, and billing.

### Acceptance Criteria

- Implement authentication (sessions or JWT) for users
- Implement roles and permissions (Admin, Staff, Student)
- Create seeders to bootstrap admin and staff accounts
- Add middleware / route guards to protect admin/staff endpoints
- Update API docs with auth requirements

### Notes

This will prepare the app for admin workflows and secure endpoints that modify data.
