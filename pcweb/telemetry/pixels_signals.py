from typing import Generator

import reflex as rx

PIXEL_SCRIPT_SIGNALS: str = """
(function() {
  if (typeof window === 'undefined') return;
  if (typeof window.signals !== 'undefined') return;
  var script = document.createElement('script');
  script.src = 'https://cdn.cr-relay.com/v1/site/b608b3c3-5dea-4365-b685-6b6635c7fda5/signals.js';
  script.async = true;
  window.signals = Object.assign(
    [],
    ['page', 'identify', 'form', 'track'].reduce(function (acc, method){
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


def get_pixel_website_trackers() -> Generator[rx.Component, None, None]:
    yield rx.script(
        PIXEL_SCRIPT_SIGNALS,
    )
