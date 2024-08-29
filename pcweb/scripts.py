import reflex as rx

PIXEL_COMMON_ROOM_SCRIPT: str = """
<script>
  (function() {
    if (typeof window === 'undefined') return;
    if (typeof window.signals !== 'undefined') return;
    var script = document.createElement('script');
    script.src = 'https://cdn.cr-relay.com/v1/site/b3e8ad62-9c28-4ad4-b014-925c55d56334/signals.js';
    script.async = true;
    window.signals = Object.assign(
      [],
      ['page', 'identify', 'form'].reduce(function (acc, method){
        acc[method] = function () {
          signals.push([method, arguments]);
          return signals;
        };
       return acc;
      }, {})
    );
    document.head.appendChild(script);
  })();
</script>
"""
PIXEL_GOOGLE_TAG_MANAGER_RUNNER_SCRIPT: str = """
window.dataLayer = window.dataLayer || [];
function gtag() {
    window.dataLayer.push(arguments);
}
gtag('js', new Date());
gtag('config', 'G-4T7C8ZD9TR');
"""
PIXEL_POSTHOG_SCRIPT: str = """
! function(t, e) {
    var o, n, p, r;
    e.__SV || (window.posthog = e, e._i = [], e.init = function(i, s, a) {
        function g(t, e) {
            var o = e.split(".");
            2 == o.length && (t = t[o[0]], e = o[1]), t[e] = function() {
                t.push([e].concat(Array.prototype.slice.call(arguments, 0)))
            }
        }(p = t.createElement("script")).type = "text/javascript", p.async = !0, p.src = s.api_host.replace(".i.posthog.com", "-assets.i.posthog.com") + "/static/array.js", (r = t.getElementsByTagName("script")[0]).parentNode.insertBefore(p, r);
        var u = e;
        for (void 0 !== a ? u = e[a] = [] : a = "posthog", u.people = u.people || [], u.toString = function(t) {
                var e = "posthog";
                return "posthog" !== a && (e += "." + a), t || (e += " (stub)"), e
            }, u.people.toString = function() {
                return u.toString(1) + ".people (stub)"
            }, o = "capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled onFeatureFlags getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures getActiveMatchingSurveys getSurveys getNextSurveyStep onSessionId setPersonProperties".split(" "), n = 0; n < o.length; n++) g(u, o[n]);
        e._i.push([i, s, a])
    }, e.__SV = 1)
}(document, window.posthog || []);
posthog.init('phc_JoMo0fOyi0GQAooY3UyO9k0hebGkMyFJrrCw1Gt5SGb', {
    api_host: 'https://us.i.posthog.com',
    person_profiles: 'identified_only'
})
"""
PIXEL_CLEARBIT_SCRIPT_URL: str = (
    "https://tag.clearbitscripts.com/v1/pk_3d711a6e26de5ddb47443d8db170d506/tags.js"
)
PIXEL_GOOGLE_TAG_MANAGER_SCRIPT_URL: str = (
    "https://www.googletagmanager.com/gtag/js?id=G-4T7C8ZD9TR"
)


def get_pixel_website_trackers() -> list[rx.Component]:
    return [
        rx.el.script(
            src=PIXEL_CLEARBIT_SCRIPT_URL,
            referrer_policy="strict-origin-when-cross-origin",
        ),
        rx.script(
            src=PIXEL_GOOGLE_TAG_MANAGER_SCRIPT_URL,
        ),
        rx.script(
            PIXEL_GOOGLE_TAG_MANAGER_RUNNER_SCRIPT,
        ),
        rx.script(
            PIXEL_POSTHOG_SCRIPT,
        ),
        rx.el.script(
            PIXEL_COMMON_ROOM_SCRIPT,
        ),
    ]
