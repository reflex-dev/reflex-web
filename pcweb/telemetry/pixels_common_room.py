from typing import Generator

import reflex as rx

PIXEL_SCRIPT_COMMONROOM: str = """
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
"""

def get_pixel_website_trackers()-> Generator[rx.Component, None, None]:
    yield rx.script(
        PIXEL_SCRIPT_COMMONROOM,
    )
