The following issues were prepared from comparing `lubusIN/laravel-gymie` features to this repository.

Create these issues (no labels/assignees) in the repository when ready.

1. Add Authentication + Role-Based Access Control

   - Add user authentication (login/logout) and Role-Based Access Control (Admin/Staff/Student).
   - Seeders to bootstrap admin/staff users, and middleware to protect admin routes.

2. Implement Database-backed Persistence and Seeders

   - Replace in-memory `activities` with a persistent DB (SQLite/Postgres).
   - Add migrations and seeders for demo data.

3. Add Subscriptions & Plans Management

   - Add Plans and Subscriptions models, endpoints to assign/change plans, and expiring alerts.

4. Add Payments & Invoicing

   - Implement invoices, payments (partial/full), discounts, and simple reports/exports.

5. Add SMS/Notifications & Logging

   - Integrate SMS/email notification system and persist logs for events like signups and payments.

6. Add Financial / Expense Tracking

   - Expense categories, entries, and reporting for club finances.

7. Add Services & Enquiries Module

   - Services and enquiries endpoints/UI to capture prospective students and manage enquiries.

8. Improve Admin UI (rich editor & templates)

   - Add admin templates or SPA, integrate CKEditor for content editing, and improve responsive styling.

Each of the `.github/ISSUE_TEMPLATE/*.md` files contains the full title, acceptance criteria, and notes.
