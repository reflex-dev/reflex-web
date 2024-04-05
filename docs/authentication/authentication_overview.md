
# Authentication Overview

Almost any non-trivial web app needs a way to identify and authenticate users,
but Reflex does not provide this functionality out of the box because there are
way too many different ways to approach the problem. Thanks to the plethora of
existing React components for performing auth, a wrapper can be created to
include most third-party auth solutions within a Reflex app.

We have four solutions here:

1. Local Auth: Check out how it is set up in this app: https://github.com/reflex-dev/reflex-examples/tree/main/twitter
2. Google Auth: Check out how it is set up with this blog: https://reflex.dev/blog/2023-10-25-implementing-sign-in-with-google/
3. Captcha: Check out this repo: https://github.com/masenf/reflex-google-recaptcha-v2
4. Magic Link Auth: Check out this repo: https://github.com/masenf/reflex-magic-link-auth


There is more thorough authentication documentation on the way. Check back soon!