# from django.db import models
#
# from LogiSolutions.core.model_mixins import PaymentsStatus
#
#
#
#
#
# class Invoice(models.Model):
#     invoice_number = models.CharField(
#         max_length=20,
#         unique=True
#     )
#     amount_due = models.DecimalField(
#         max_digits=10,
#         decimal_places=2
#     )
#     due_date = models.DateField(
#
#     )
#     payment_status = models.CharField(
#         max_length=PaymentsStatus.max_length(),
#         choices=PaymentsStatus.choices()
#     )
#     related_cargo = models.ForeignKey(
#         'Cargo',
#         on_delete=models.CASCADE
#     )
#
#     def __str__(self):
#         return f"Invoice #{self.invoice_number}"
#
#
