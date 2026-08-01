# SPDX-FileCopyrightText: Volker Krause <vkrause@kde.org>
# SPDX-License-Identifier: AGPL-3.0-or-later

from subscriptionHandler.models import Subscription

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptionHandler", "0011_subscription_vapid_public_key"),
    ]

    operations = [
        migrations.RunSQL(
            sql=f"UPDATE \"subscriptionHandler_subscription\" SET \"vapid_public_key\"='{settings.WEB_PUSH_CONFIG_PUBLIC_KEY}' WHERE \"push_service\"={Subscription.PushServices.UNIFIED_PUSH_ENCRYPTED}",
            reverse_sql=migrations.RunSQL.noop
        ),
    ]
