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
    success page after the Stripe webhook has fired.

    The required block is the bare minimum to provision a tenant; the
    optional block below it pre-populates the branding fields that
    otherwise have to be set by the tenant's admin after login. Anything
    omitted just leaves the corresponding Client column at its default
    (blank/null) — no preconditions on the branding endpoint.
    """

    # ── Required ──────────────────────────────────────────────────────
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

    # ── Optional branding (mirrors tenants.Client columns) ────────────
    display_name = serializers.CharField(
        max_length=120, required=False, allow_blank=True,
    )
    logo = serializers.ImageField(required=False, allow_null=True)
    favicon = serializers.ImageField(required=False, allow_null=True)
    primary_color = serializers.RegexField(
        regex=r'^#[0-9a-fA-F]{6}$',
        required=False, allow_blank=True,
        error_messages={'invalid': 'Use a 6-digit hex color like #1f6feb.'},
    )
    accent_color = serializers.RegexField(
        regex=r'^#[0-9a-fA-F]{6}$',
        required=False, allow_blank=True,
        error_messages={'invalid': 'Use a 6-digit hex color like #94a3b8.'},
    )
    contact_phone = serializers.CharField(
        max_length=40, required=False, allow_blank=True,
    )
    signature_image = serializers.ImageField(required=False, allow_null=True)
    signatory_name = serializers.CharField(
        max_length=120, required=False, allow_blank=True,
    )
    signatory_title = serializers.CharField(
        max_length=120, required=False, allow_blank=True,
    )
    address = serializers.CharField(
        required=False, allow_blank=True,
        style={'base_template': 'textarea.html'},
    )
