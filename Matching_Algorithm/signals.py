"""Match-notification email intentionally disabled.

Previously this module sent an email (with Excel + Word attachments)
to the tenant's `support_email` whenever a `Match_Data` row was
created. That behaviour was removed at the platform owner's request;
the relevant operational notification is now the new-tenant-paid
email sent from `subscriptions/notifications.py` when a tenant
completes Stripe checkout.

If you re-introduce a match notification later, register the
`post_save` receiver here and remember to import this module from
the app's `AppConfig.ready()`.
"""
