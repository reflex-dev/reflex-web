import reflex as rx

from pcweb.constants import ENABLE_FREE_TIER, ENABLE_PRO_TIER


class EnableTiersState(rx.State):
    enable_free_tier: rx.Field[bool] = rx.field(default=ENABLE_FREE_TIER)
    enable_pro_tier: rx.Field[bool] = rx.field(default=ENABLE_PRO_TIER)
