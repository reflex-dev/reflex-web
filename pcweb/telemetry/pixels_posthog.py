from typing import Generator

import reflex as rx

PIXEL_SCRIPT_POSTHOG: str = """
    !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init ge bs pe cs gs capture Ae Fi Ss register register_once register_for_session unregister unregister_for_session Es getFeatureFlag getFeatureFlagPayload isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSurveysLoaded onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey canRenderSurveyAsync identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty ks ys createPersonProfile xs ps opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing clear_opt_in_out_capturing ws debug $s getPageViewId captureTraceFeedback captureTraceMetric".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
    posthog.init('reflex_pixel_id', {
        api_host: 'https://us.i.posthog.com',
        person_profiles: 'always', // to create profiles for anonymous users as well
    })
"""
REFLEX_PIXEL_ID: str = "phc_A0MAR0wCGhXrizWmowRZcYqyZ8PMhPPQW06KEwD43aC"


def get_pixel_script_posthog(
    reflex_pixel_id: str,
) -> str:
    return PIXEL_SCRIPT_POSTHOG.replace(
        "reflex_pixel_id",
        reflex_pixel_id,
    )


def get_pixel_website_trackers() -> Generator[rx.Component, None, None]:
    yield rx.script(
        get_pixel_script_posthog(
            reflex_pixel_id=REFLEX_PIXEL_ID,
        ),
    )
