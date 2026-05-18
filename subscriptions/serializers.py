from rest_framework import serializers

from .models import Plan


class PlanPublicSerializer(serializers.ModelSerializer):
    """What the pricing page renders. Exposes only what the visitor
    needs to make a buying decision — no Stripe IDs."""

    amount_dollars = serializers.FloatField(read_only=True)

    class Meta:
        model = Plan
        fields = (
            'slug', 'name', 'description',
            'amount_cents', 'amount_dollars', 'currency', 'interval',
            'supports_trial', 'sort_order',
        )


class CreateCheckoutSessionSerializer(serializers.Serializer):
    """Body for POST /api/checkout/create-session/."""

    plan = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Plan.objects.filter(is_active=True),
    )
    with_trial = serializers.BooleanField(required=False, default=False)
    email = serializers.EmailField(max_length=254)
    company_name = serializers.CharField(max_length=200, required=False, allow_blank=True)

    def validate(self, attrs):
        if attrs.get('with_trial') and not attrs['plan'].supports_trial:
            raise serializers.ValidationError({
                'with_trial': f'Plan "{attrs["plan"].slug}" does not support a free trial.',
            })
        return attrs


class TenantOnboardingSerializer(serializers.Serializer):
    """Body for POST /api/tenants/onboard/. Token comes from the
    success page after the Stripe webhook has fired."""

    onboarding_token = serializers.UUIDField()
    schema_name = serializers.RegexField(
        regex=r'^[a-z][a-z0-9_-]{1,62}$',
        max_length=63,
        help_text=(
            'Lower-case letters, digits, hyphens, underscores. Must start with a '
            'letter. Becomes the subdomain (<schema_name>.appfinfire.com).'
        ),
    )
    company_name = serializers.CharField(max_length=200)
    admin_email = serializers.EmailField(max_length=254)
    admin_password = serializers.CharField(min_length=8, max_length=128, write_only=True)
