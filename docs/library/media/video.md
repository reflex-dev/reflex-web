---
import reflex as rx
from pcweb.templates.docpage import docdemo

video_example = """rx.video(
    url="https://www.youtube.com/embed/9bZkp7q19f0", 
    width="400px",
    height="auto"
)"""

---
The video component can display a video given an src path as an argment. This could either be a local path from the assets folder or an external link.

```reflex
docdemo(video_example)
```

If we had a local file in the `assets` folder named `test.mp4` we could set `url=test.mp4` to view the video.
